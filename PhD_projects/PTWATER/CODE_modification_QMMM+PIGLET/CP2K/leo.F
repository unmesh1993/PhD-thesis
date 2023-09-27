!--------------------------------------------------------------------------------------------------!
!   CP2K: A general program to perform molecular dynamics simulations                              !
!   Copyright (C) 2000 - 2018  CP2K developers group                                               !
!--------------------------------------------------------------------------------------------------!

! **************************************************************************************************
!> \brief Driver mode - To communicate with i-PI Python wrapper
!> \par History
!>      none
!> \author Michele Ceriotti 03.2012
! **************************************************************************************************
MODULE leo
   USE ISO_C_BINDING,                   ONLY: C_CHAR,&
                                              C_DOUBLE,&
                                              C_INT,&
                                              C_LOC,&
                                              C_NULL_CHAR,&
                                              C_PTR
   USE bibliography,                    ONLY: Ceriotti2014,&
                                              Kapil2016,&
                                              cite_reference
   USE cell_types,                      ONLY: cell_create,&
                                              cell_release,&
                                              cell_type,&
                                              init_cell
   USE cp_external_control,             ONLY: external_control
   USE cp_log_handling,                 ONLY: cp_logger_get_default_io_unit
   USE cp_para_types,                   ONLY: cp_para_env_type
   USE cp_subsys_types,                 ONLY: cp_subsys_get,&
                                              cp_subsys_set,&
                                              cp_subsys_type
!   USE force_env_methods,               ONLY: force_env_calc_energy_force
   USE force_env_types,                 ONLY: force_env_get,&
                                              force_env_type
   USE global_types,                    ONLY: global_environment_type
   USE input_section_types,             ONLY: section_vals_get_subs_vals,&
                                              section_vals_type,&
                                              section_vals_val_get
   USE kinds,                           ONLY: default_path_length,&
                                              default_string_length,&
                                              dp,&
                                              int_4
   USE message_passing,                 ONLY: mp_bcast,&
                                              mp_irecv,&
                                              mp_send,&
                                              mp_sync,&
                                              mp_testany
   USE virial_types,                    ONLY: virial_type


!!!

USE atomic_kind_list_types,          ONLY: atomic_kind_list_type
USE distribution_1d_types,           ONLY: distribution_1d_type
USE qmmm_create,                     ONLY: qmmm_env_create
USE qmmm_types,                      ONLY: qmmm_env_get
USE qmmmx_types,                     ONLY: qmmmx_env_release,&
                                           qmmmx_env_type
USE qmmmx_util,                      ONLY: setup_force_mixing_qmmm_sections,&
                                           update_force_mixing_labels

USE input_restart_force_eval,        ONLY: update_force_eval
USE input_section_types,             ONLY: section_vals_get,&
                                           section_vals_release
!!!

#include "./base/base_uses.f90"

   IMPLICIT NONE

   PRIVATE

   CHARACTER(len=*), PARAMETER, PRIVATE :: moduleN = 'ipi_driver'

   PUBLIC :: unmesh

CONTAINS

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

   SUBROUTINE unmesh(force_env,subsys)
      INTEGER                           :: output_unit
      INTEGER :: idir,ii,ip
      TYPE(force_env_type), POINTER                      :: force_env
      TYPE(section_vals_type), POINTER                   :: root_section

      TYPE(section_vals_type), POINTER                   :: section_vals
      TYPE(section_vals_type), POINTER                   :: qmmm_core_section, &
                                                            qmmm_extended_Section,&
                                                            qmmm_force_mixing,qmmm_section, &
                                                            subsys_section

      LOGICAL                                            :: force_mixing_active,labels_changed
      TYPE(atomic_kind_list_type), POINTER               :: atomic_kinds,new_atomic_kinds
      TYPE(cp_subsys_type), POINTER                      :: subsys, subsys_new
      TYPE(distribution_1d_type), POINTER                :: local_particles,new_local_particles
      TYPE(qmmmx_env_type), POINTER                      :: new_qmmmx_env




subsys%ref_count = 2
qmmm_section => section_vals_get_subs_vals(force_env%force_env_section, "QMMM",can_return_null=.TRUE.)
qmmm_force_mixing => section_vals_get_subs_vals(qmmm_section, "FORCE_MIXING",can_return_null=.TRUE.)
CALL section_vals_get(qmmm_force_mixing, explicit=force_mixing_active)

CALL update_force_mixing_labels(subsys, qmmm_section,labels_changed=labels_changed)
IF (.NOT. labels_changed) RETURN
CPWARN("Adaptive force-mixing labels changed, rebuilding QM/MM calculations! ")



ALLOCATE (new_qmmmx_env)

CALL setup_force_mixing_qmmm_sections(subsys, qmmm_section, qmmm_core_section,qmmm_extended_section)

subsys_section => section_vals_get_subs_vals(force_env%force_env_section,"SUBSYS")

CALL qmmm_env_create(new_qmmmx_env%core, &
                     force_env%root_section, force_env%para_env, force_env%globenv, &
                           force_env%force_env_section, qmmm_core_section,subsys_section, use_motion_section=.FALSE., &
                           prev_subsys=subsys, ignore_outside_box=.TRUE.)

CALL qmmm_env_create(new_qmmmx_env%ext, &
                     force_env%root_section, force_env%para_env, force_env%globenv, &
                           force_env%force_env_section, qmmm_extended_section, subsys_section, use_motion_section=.FALSE., &
                           prev_subsys=subsys, ignore_outside_box=.TRUE.)


CALL section_vals_release(qmmm_core_section)
CALL section_vals_release(qmmm_extended_section)

! release old qmmmx_env and point to new one
CALL qmmmx_env_release(force_env%qmmmx_env)
force_env%qmmmx_env => new_qmmmx_env


DO ip = 1, subsys%particles%n_els
      DO idir = 1, 3
         ii = ii+1
         subsys%particles%els(ip)%f(idir)=0.0
      END DO
END DO

   END SUBROUTINE

END MODULE leo

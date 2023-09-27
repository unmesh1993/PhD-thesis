%-------------------------- initial code -----------------------
\newif\ifCU@bookmode
\CU@bookmodetrue

\DeclareOption{report}{\CU@bookmodefalse}
\DeclareOption{book}{\CU@bookmodetrue}
\ProcessOptions\relax%

\ifCU@bookmode
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}%
\ProcessOptions\relax%
\ifx\pdfoutput\undefined%
   \LoadClass[dvips, a4paper]{book}%
\else%
   \LoadClass[pdftex, a4paper]{book}%
\fi%
\else
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}%
\ProcessOptions\relax%
\ifx\pdfoutput\undefined%
  \LoadClass[dvips, a4paper]{report}%
\else%
   \LoadClass[pdftex, a4paper]{report}%
\fi%
\fi

\usepackage{setspace}
\usepackage[nottoc]{tocbibind}
%\usepackage{fancyhdr} %REMOVED
\usepackage{eucal}
\usepackage[english]{babel}
\usepackage[usenames, dvipsnames]{color}
\usepackage[perpage]{footmisc}
\usepackage{ifthen}
\usepackage{ifpdf}
\usepackage{tocloft}
\usepackage{xcolor,colortbl}
\definecolor{bl}{rgb}{0.0,0.2,0.6} 
\usepackage{mathtools}
\usepackage{pifont}
\usepackage{amsmath}
\usepackage{upgreek}
\usepackage{times}
\usepackage{enumitem}
\usepackage{cite}
\usepackage[font=small,format=plain,labelfont=bf,up]{caption}
%\usepackage{epstopdf} %REMOVED
\usepackage{setspace}
\usepackage[export]{adjustbox}
\usepackage{array}
\usepackage{float}
\usepackage{wrapfig}
\usepackage[autostyle]{csquotes}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{mdframed}
\usepackage{amsmath,amsfonts,amssymb,amsthm}
\usepackage{braket}

\onehalfspacing

\usepackage{nomencl}
\makenomenclature
\renewcommand\nomgroup[1]{%
  \ifthenelse{\equal{#1}{A}}{%
   \item[\textbf{Roman Symbols}] }{%            
    \ifthenelse{\equal{#1}{G}}{%
     \item[\textbf{Greek Symbols}]}{%             
      \ifthenelse{\equal{#1}{R}}{%
        \item[\textbf{Superscripts}]}{%              
          \ifthenelse{\equal{#1}{S}}{%
           \item[\textbf{Subscripts}]}{{%            
	    \ifthenelse{\equal{#1}{X}}{%
	     \item[\textbf{Other Symbols}]}{{%    
	    \ifthenelse{\equal{#1}{Z}}{%
	     \item[\textbf{Acronyms}]}%              
              			{{}}}}}}}}}}

\ifpdf

    \usepackage[ pdftex, plainpages = false, pdfpagelabels, 
                 pdfpagelayout = OneColumn, 
                 bookmarks,
                 bookmarksopen = true,
                 bookmarksnumbered = true,
                 breaklinks = true,
                 linktocpage,
                 pagebackref,
                 colorlinks = true,
                 urlcolor  = blue,
                 citecolor = blue ,
                 anchorcolor = green,
                 linkcolor = blue,
                 hyperindex = true,
                 hyperfigures
                 ]{hyperref} 
    \usepackage{graphicx}
   \DeclareGraphicsExtensions{.png, .jpg, .pdf}
    \pdfcompresslevel=9
    \graphicspath{{ThesisFigs/PNG/}{ThesisFigs/PDF/}{ThesisFigs/}}
\else
    \usepackage[ dvips, 
                 bookmarks,
                 bookmarksopen = true,
                 bookmarksnumbered = true,
                 breaklinks = true,
                 linktocpage,
                 pagebackref,
                 colorlinks = true,
                 urlcolor  = blue,
                 citecolor = blue,
                 anchorcolor = green,
                 hyperindex = true,
                 hyperfigures
                 ]{hyperref}

\usepackage{epsfig}
 \usepackage{graphicx}
 \DeclareGraphicsExtensions{.eps, .ps}
 \graphicspath{{ThesisFigs/EPS/}{ThesisFigs/}}
\fi

\ifpdf
   \pdfpageheight=297mm
   \pdfpagewidth=210mm
\else
   \setlength{\paperheight}{297mm}
   \setlength{\paperwidth}{210mm}
\fi

\setlength{\hoffset}{0.00cm}
\setlength{\voffset}{0.00cm}

\setlength{\evensidemargin}{1.96cm}
\setlength{\oddsidemargin}{0.54cm}
\setlength{\topmargin}{0mm}
\setlength{\headheight}{0.0cm}
\setlength{\headsep}{0.50cm}
\setlength{\textheight}{21.84cm}
\setlength{\textwidth}{15.04cm}
\setlength{\marginparsep}{1mm}
\setlength{\marginparwidth}{0.00cm}
\setlength{\footskip}{0.60cm}

\pagestyle{fancy}
\addtolength{\headheight}{\baselineskip}
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\chaptername\ \thechapter.\ #1}}{}}
\renewcommand{\sectionmark}[1]{\markright{#1}{}}

\fancyhf{}
\fancyhead[LO,RO]{\color{black} \bfseries \rightmark} %%%changed
\fancyhead[LO,RO]{\color{black} \bfseries \chaptername { }\thechapter}  %%CHANGED
\fancyfoot[C]{{\color{black} {\bfseries --- [ \thepage \ ] ---}}}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.0pt}
\addtolength{\headheight}{0.5pt}
\fancypagestyle{plain}{
  \fancyhead{}
  \renewcommand{\headrulewidth}{0pt}
}

\newcommand{\submittedtexta}{{A thesis submitted\\ in partial fulfillment of the requirements for the degree of\\
}}
\newcommand{\submittedtextb}{{by}}
\newcommand{\submittedtextc}{{Roll No.: 20152031}}

\def\degreedate#1{\gdef\@degreedate{#1}}
\def\degree#1{\gdef\@degree{#1}}
\def\collegeordept#1{\gdef\@collegeordept{#1}}
\def\university#1{\gdef\@university{#1}}
\def\crest#1{\gdef\@crest{#1}}

\newenvironment{alwayssingle}{%
       \@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
       \else\newpage\fi}
       {\if@restonecol\twocolumn\else\newpage\fi}

\renewcommand{\maketitle}{%
\pagenumbering{roman} % 
\setcounter{page}{0}  % 
\begin{alwayssingle}
    \renewcommand{\footnotesize}{\small}
    \renewcommand{\footnoterule}{\relax}
    \thispagestyle{empty}
  \begin{center}
    { \LARGE {\bfseries {\@title}} \par}
\vspace*{20mm}
    {{\submittedtexta} \par}
\vspace*{10mm}
    { {\Large \bfseries {\@degree}} \par}
\vspace*{10mm}
    {{\submittedtextb} \par}
    { \vspace*{15mm}{\Large \bfseries \@author} \par}
\vspace*{5mm}
    {{\bfseries \submittedtextc} \par}
{\large \vspace*{10mm} {{\@crest} \par}\vspace*{10mm}}
{\vspace*{1ex}
    {\Large \bfseries {\@university} \par}
\vspace*{1ex}
    {\Large \bfseries {\@degreedate}}}
  \end{center}
  \null\vfill
\end{alwayssingle}}

\newenvironment{dedication}
{\begin{alwayssingle}
  \pagestyle{empty}
  \begin{center}
  \vspace*{-2ex}
  {\large }
  \end{center}
  \vspace{0cm}
  \begin{quote} \begin{center}}
{\end{center} \end{quote} \end{alwayssingle}}


\newenvironment{acknowledgements}
{\pagestyle{empty}
\begin{alwayssingle}
\begin{flushright}
\vspace*{-2ex}
{\large \it \bfseries Acknowledgements}
\end{flushright}
\vspace{0.5cm}
}
{\end{alwayssingle}}

\newenvironment{declaration} {\begin{alwayssingle} \pagestyle{empty}
  \begin{center}
  \vspace*{2ex}
  \vspace*{14ex}
  {\large \bfseries  Declaration}
  \end{center}
  \vspace{0cm}
   \begin{quote}}
{\end{quote}\end{alwayssingle}}

\newenvironment{certificate} {\begin{alwayssingle} \pagestyle{empty}
  \begin{center}
  \vspace*{14ex}
 \vspace*{2ex}
  {\large \bfseries  CERTIFICATE}
  \end{center}
  \vspace{0cm}
   \begin{quote}}
{\end{quote}\end{alwayssingle}}

\newenvironment{abstracts} {\begin{alwayssingle} \pagestyle{plain}
  \vspace*{-2ex}
  {\large \bfseries  Abstract}
  \vspace{0cm}
   }
{\end{alwayssingle}}

\newenvironment{backcover} {\begin{alwayssingle} \pagestyle{plain}
 \vspace*{-2ex}
  \vspace{0cm}
   }
{\end{alwayssingle}}

\newenvironment{romanpages}
{\setcounter{page}{1}
  \renewcommand{\thepage}{\roman{page}}}
{\newpage\renewcommand{\thepage}{\arabic{page}}\setcounter{page}{1}}


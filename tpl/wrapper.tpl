\documentclass[10pt,letterpaper]{extbook}

\usepackage[head=26pt, includeheadfoot, top=1.5cm, bottom=2cm, left=2cm, right=2cm]{geometry}

\usepackage{import} % for relative import
\usepackage{calc}
\usepackage{hyperref}
\usepackage{color,colortbl,graphicx}
\usepackage{fancyvrb}

%%%% Define Header Footer w/ FancyHdr %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{fancyhdr,etoolbox, xcolor}
\definecolor{midnightblue}{rgb}{0.05,0.05,0.4}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[L]{\fontsize{8}{10} \selectfont \leftmark}
    \fancyhead[R]{\fontsize{8}{10} \selectfont \rightmark}
    \fancyhead[C]{\rule[-4ex]{0pt}{4ex}}
    \fancyfoot[L]{\fontsize{8}{10} \selectfont Corp Confidential}
    \fancyfoot[C]{\fontsize{8}{10} \selectfont - \thepage\ -}
    \fancyfoot[R]{\fontsize{8}{10} \selectfont Author}
    }
\pagestyle{plain}

\renewcommand{\sectionmark}[1]{\markright{#1}{}}
\renewcommand{\headrulewidth}{1.2pt}
\renewcommand{\footrulewidth}{1.2pt}
\newcommand{\headrulecolor}[1]{\patchcmd{\headrule}{\hrule}{\color{#1}\hrule}{}{}}
\newcommand{\footrulecolor}[1]{\patchcmd{\footrule}{\hrule}{\color{#1}\hrule}{}{}}
\headrulecolor{midnightblue}
\footrulecolor{midnightblue}
%%== End of Header/Footer Definition =======================================%%

%%%% Definition of Tables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{ltablex,tabu,multirow,array,booktabs,calc}
\newcolumntype{Y}{>{\centering\arraybackslash}X}
\tabulinesep=1.1mm
\usepackage{setspace}
\onehalfspace
%%== End of Table Definition ===============================================%%

%%%% Definition of Title Page %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\maketitle}{\begin{titlepage} % Create command for title page
    \thispagestyle{empty}
    \raggedleft % right align for all text
    \vspace*{\baselineskip} % Whitespace at the top of the page

    %%{\Large \includegraphics[width=3cm]{./tpl/logo.png}}\\[0.167\textheight]
    {\Large Your Logo }\\[0.167\textheight] % Logo

    {\textcolor{midnightblue}{\Huge Main Title}}\\[\baselineskip]

    {\LARGE\bfseries Subtitle. Manual Template}\\[\baselineskip]

    {\Large \textit{$$date$$}}\par

    \vfill

    {\large Author / $$team$$}\par

    \vspace*{3\baselineskip}
    \pagebreak
    \end{titlepage}
    }
%%== End of Title Definition ===============================================%%

%%%% Table of Contents %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{tocloft}

\setlength\cftparskip{-5pt}
\setlength\cftbeforechapskip{10pt}
\renewcommand{\cfttoctitlefont}{\color{midnightblue}\LARGE\bfseries}
\renewcommand{\cftaftertoctitle}{\hfill}
\setlength{\cftbeforetoctitleskip}{20pt}
\setlength{\cftaftertoctitleskip}{10pt}

\renewcommand{\contentsname}{Table of Contents}

\renewcommand{\cftloftitlefont}{\color{midnightblue}\LARGE\bfseries}
\renewcommand{\cftafterloftitle}{\hfill}
\setlength{\cftbeforeloftitleskip}{20pt}
\setlength{\cftafterloftitleskip}{10pt}
\renewcommand{\cftlottitlefont}{\color{midnightblue}\LARGE\bfseries}
\renewcommand{\cftafterlottitle}{\hfill}
\setlength{\cftbeforelottitleskip}{20pt}
\setlength{\cftafterlottitleskip}{10pt}

%%== End of Table of Contents ==============================================%%


%%%% Other environment settings
%%\let\tempone\itemize
%%\let\temptwo\enditemize
%%\renewenvironment{itemize}{\tempone\addtolength{\itemsep}{0.5\baselineskip}}{\temptwo}

\usepackage{enumitem}
\setitemize{itemsep=0pt}
%%%% END : Other environment settings
\begin{document}
\maketitle


%%subimport
\chapter{Chapter One}
\section{Register Description}


%%%%%%%%%% BEGIN : Mako Template For loop %%%%%%%%%%%%%%%%%%%

% for block in blocks:

\subsection{${block.name | trim}}

% for reg in block.registers:

\textbf{[${reg.name | trim}]} \\\
${reg.desc | trim}

\hspace{10pt}

\begin{tabular}{>{\bfseries}l l}
    Offset: & ${"0x%0.4x" %reg.offset} \\\
    POR:    & ${"0x%0.8x" %reg.por} \\\
\end{tabular}

\begin{longtabu} to \textwidth {*{16}{|Y}|}
\hline
31 & 30 & 29 & 28 & 27 & 26 & 25 & 24 & 23 & 22 & 21 & 20 & 19 & 18 & 17 & 16 \\\hline
% for bit in reg.row0:
    % if len(bit.name) > (bit.high - bit.low + 1)*5 :
        % if bit.high == 31 :
            \multicolumn{${bit.high - bit.low + 1}}{|c|}{\rotatebox{90}{${bit.name | trim}}}
        % else :
            \multicolumn{${bit.high - bit.low + 1}}{c|}{\rotatebox{90}{${bit.name | trim}}}
        % endif
    % else :
        % if bit.high == 31 :
            \multicolumn{${bit.high - bit.low + 1}}{|c|}{${bit.name | trim}}
        % else :
            \multicolumn{${bit.high - bit.low + 1}}{c|}{${bit.name | trim}}
        % endif
    % endif

    % if bit.low != 16:
        &
    % endif
% endfor
\\\hline
% for por_bit in (reg.por_bits)[0:16]:
    ${por_bit}
    % if (loop.last == False):
        &
    % endif
% endfor
\\\hline
\multicolumn{16}{c}{ } \\
\\hline
15 & 14 & 13 & 12 & 11 & 10 &  9 &  8 &  7 &  6 &  5 &  4 &  3 &  2 &  1 &  0 \\\hline

% for bit in reg.row1:
    % if len(bit.name) > (bit.high - bit.low + 1)*5 :
        % if bit.high == 15 :
            \multicolumn{${bit.high - bit.low + 1}}{|c|}{\rotatebox{90}{${bit.name | trim}}}
        % else :
            \multicolumn{${bit.high - bit.low + 1}}{c|}{\rotatebox{90}{${bit.name | trim}}}
        % endif
    % else :
        % if bit.high == 15 :
            \multicolumn{${bit.high - bit.low + 1}}{|c|}{${bit.name | trim}}
        % else :
            \multicolumn{${bit.high - bit.low + 1}}{c|}{${bit.name | trim}}
        % endif
    % endif
    % if bit.low != 0:
        &
    % endif

% endfor
\\\hline
% for por_bit in (reg.por_bits)[16:32]:
    ${por_bit}
    % if (loop.last == False):
        &
    % endif
% endfor
\\\hline
\end{longtabu}



\begin{longtabu} to \textwidth {|c|c|c|X|}
\hline
Bit & Name & Access & Description \\
\\hline
\endhead\relax
% for bit in reg.bits:
[${bit.range}] & ${bit.name | trim} & ${bit.type | trim} & ${bit.description | trim} \\\hline
% endfor
\end{longtabu}
\pagebreak
% endfor # registers
% endfor # blocks
%%%%%%%%%% END : Mako Template For loop %%%%%%%%%%%%%%%%%%%

\end{document}


#  This module is used to read the output from the LLM and use it to generate the Tex files.

def read_output(filename, **kwargs):
    with open(file=filename) as file:
        lines = file.readlines()
        filtered_lines = [line for line in lines if line.strip() and not line.lstrip().startswith(tuple(str(i) + '.' for i in range(1, 8)))]
    return filtered_lines

def get_files(inp: list, **kwargs) -> None:
    """
    This function is currenltly designed for ONLY 7 sections of the slides

    Arguments:
        - inp: The input list of section contents
        - name: Name of the author (optional)
        - title: Title of the project (optional)

    Output:
        - Prints the required tex files and style files for the PDF compilation
    """

    assert len(inp)==7, "Inappropriate number of sections!"

    name = kwargs.get('name', 'No Name')
    title = kwargs.get('title', 'No Title')

    my_latex_document = rf'''
    \documentclass{{beamer}}
    \usepackage{{hyperref}}
    \usepackage[T1]{{fontenc}}

    \usepackage{{latexsym,amsmath,xcolor,multicol,booktabs,calligra}}
    \usepackage{{graphicx,pstricks,listings,stackengine}}

    \author {name}
    \title {title}
    \subtitle{{uchicago Beamer Theme}}
    \institute{{
        Pritzker School of Molecular Engineering \\
        University of Chicago
    }}
    \date{{\small May, 2024}}
    \usepackage{{Ritsumeikan}}

    % defs
    \def\cmd#1{{\texttt{{\color{{red}}\footnotesize $\backslash$#1}}}}
    \def\env#1{{\texttt{{\color{{blue}}\footnotesize #1}}}}
    \definecolor{{deepblue}}{{rgb}}{{0,0,0.5}}
    \definecolor{{deepred}}{{RGB}}{{153,0,0}}
    \definecolor{{deepgreen}}{{rgb}}{{0,0.5,0}}
    \definecolor{{halfgray}}{{gray}}{{0.55}}

    \lstset{{
        basicstyle=\ttfamily\small,
        keywordstyle=\bfseries\color{{deepblue}},
        emphstyle=\ttfamily\color{{deepred}},    % Custom highlighting style
        stringstyle=\color{{deepgreen}},
        numbers=left,
        numberstyle=\small\color{{halfgray}},
        rulesepcolor=\color{{red!20!green!20!blue!20}},
        frame=shadowbox,
    }}

    \begin{{document}}

    \begin{{frame}}[allowframebreaks]
        \titlepage
        \vspace*{{-0.6cm}}
        \begin{{figure}}[htpb]
            \begin{{center}}
                \includegraphics[keepaspectratio, scale=0.14]{{pic/uchicago.png}}
            \end{{center}}
        \end{{figure}}
    \end{{frame}}

    \begin{{frame}}[allowframebreaks]
    \tableofcontents[sectionstyle=show,
    subsectionstyle=show/shaded/hide,
    subsubsectionstyle=show/shaded/hide]
    \end{{frame}}

    \section{{Background}}

    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[0]}
        \end{{itemize}}
    \end{{frame}}

    \section{{Challenge}}

    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[1]}
        \end{{itemize}}
    \end{{frame}}

    \section{{Current Status}}

    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[2]}
        \end{{itemize}}
    \end{{frame}}

    \section{{Methods}}

    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[3]}
        \end{{itemize}}
    \end{{frame}}


    \section{{Results}}
    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[4]}
        \end{{itemize}}
    \end{{frame}}

    \section{{Conclusions}}

    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[5]}
        \end{{itemize}}
    \end{{frame}}

    \section{{Outlook}}

    \begin{{frame}}[allowframebreaks]
        \begin{{itemize}}
            \item {input[6]}
        \end{{itemize}}
    \end{{frame}}

    \begin{{frame}}[allowframebreaks]
        \begin{{center}}
            {{\Huge\calligra Thank You}}
        \end{{center}}
    \end{{frame}}

    \end{{document}}
    '''

    style_file = rf'''
    \mode<presentation>

    \newif\ifbeamer@secheader
    \beamer@secheaderfalse

    %\DeclareOptionBeamer{{secheader}}{{\beamer@secheadertrue}}
    \ProcessOptionsBeamer

    \useoutertheme[footline=authorinstitutetitle,subsection=false]{{smoothbars}}
    \makeatletter % [add curpage/total page at the bottom](http://tex.stackexchange.com/questions/100838/beamer-dresden-theme-miniframes-appeareance-and-frame-number-insertion)
    \newcommand{{\frameofframes}}{{/}}
    \newcommand{{\setframeofframes}}[1]{{\renewcommand{{\frameofframes}}{{#1}}}}

    \setbeamertemplate{{footline}} 
    {{%
        \begin{{beamercolorbox}}[colsep=1.5pt]{{upper separation line foot}}
        \end{{beamercolorbox}}
        \begin{{beamercolorbox}}[ht=2.5ex,dp=1.125ex,%
        leftskip=.3cm,rightskip=.3cm plus1fil]{{author in head/foot}}%
        \leavevmode{{\usebeamerfont{{author in head/foot}}\insertshortauthor}}%
        \hfill%
        {{\usebeamerfont{{institute in head/foot}}\usebeamercolor[fg]{{institute in head/foot}}\insertshortinstitute}}%
        \end{{beamercolorbox}}%
        \begin{{beamercolorbox}}[ht=2.5ex,dp=1.125ex,%
        leftskip=.3cm,rightskip=.3cm plus1fil]{{title in head/foot}}%
        {{\usebeamerfont{{title in head/foot}}\insertshorttitle}}%
        \hfill%
        {{\usebeamerfont{{frame number}}\usebeamercolor[fg]{{frame number}}\insertframenumber~\frameofframes~\inserttotalframenumber}}
        \end{{beamercolorbox}}%
        \begin{{beamercolorbox}}[colsep=1.5pt]{{lower separation line foot}}
        
        \end{{beamercolorbox}}
    }}
    \makeatother

    \useinnertheme{{circles}}

    %\useoutertheme{{default}}
    %\useinnertheme[shadow=true]{{rounded}}
    \xdefinecolor{{ritsumeikan}}{{RGB}}{{128,0,0}}  %RGB#800000
    \setbeamercolor{{footline}}{{bg=ritsumeikan}}
    \setbeamercolor{{frametitle}}{{bg=ritsumeikan,fg=white}}
    \setbeamercolor{{title}}{{bg=ritsumeikan}}
    \setbeamerfont{{frametitle}}{{size=\large}}
    %\setbeamertemplate{{navigation symbols}}{{}}
    \setbeamertemplate{{bibliography item}}[text]
    \setbeamertemplate{{caption}}[numbered]

    \setbeamercolor{{palette primary}}{{use=structure,fg=white,bg=structure.fg}}
    \setbeamercolor{{palette secondary}}{{use=structure,fg=white,bg=structure.fg!75!black}}
    \setbeamercolor{{palette tertiary}}{{use=structure,fg=white,bg=structure.fg!50!black}}
    \setbeamercolor{{palette quaternary}}{{fg=white,bg=structure.fg!50!black}}
    %\setbeamercolor*{{sidebar}}{{use=structure,bg=structure.fg}}
    \setbeamercolor{{titlelike}}{{parent=palette primary}}

    %% try
    \setbeamercolor{{block title}}{{bg=ritsumeikan,fg=white}}
    \setbeamercolor*{{block title example}}{{use={{normal text,example text}},bg=white,fg=ritsumeikan}}
    \setbeamercolor{{fine separation line}}{{}}
    \setbeamercolor{{item projected}}{{fg=white}}
    \setbeamercolor{{palette sidebar primary}}{{use=normal text,fg=normal text.fg}}
    \setbeamercolor{{palette sidebar quaternary}}{{use=structure,fg=structure.fg}}
    \setbeamercolor{{palette sidebar secondary}}{{use=structure,fg=structure.fg}}
    \setbeamercolor{{palette sidebar tertiary}}{{use=normal text,fg=normal text.fg}}
    %\setbeamercolor{{palette sidebar quaternary}}{{fg=white}}
    \setbeamercolor{{section in sidebar}}{{fg=brown}}
    \setbeamercolor{{section in sidebar shaded}}{{fg=grey}}
    \setbeamercolor{{separation line}}{{}}
    \setbeamercolor{{sidebar}}{{bg=ritsumeikan}}
    \setbeamercolor{{sidebar}}{{parent=palette primary}}
    \setbeamercolor{{structure}}{{fg=ritsumeikan}}
    \setbeamercolor{{subsection in sidebar}}{{fg=brown}}
    \setbeamercolor{{subsection in sidebar shaded}}{{fg=grey}}
    \AtBeginSection[]{{
        \begin{{frame}}
            \tableofcontents[sectionstyle=show/shaded,subsectionstyle=show/shaded/hide,subsubsectionstyle=show/shaded/hide]
        \end{{frame}}
    }}
    \AtBeginSubsection[]{{
        \begin{{frame}}
            \tableofcontents[sectionstyle=show/shaded,subsectionstyle=show/shaded/hide,subsubsectionstyle=show/shaded/hide]
        \end{{frame}}
    }}

    \mode
    <all>
    '''

    with open("my_document.tex", "w") as file:
        file.write(my_latex_document)

    with open("Ritsumeikan.sty", "w") as file:
        file.write(style_file)

    return None

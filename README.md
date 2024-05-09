# Slide Generator Using LLM

### An LLM slide generator that summarizes research articles

Short 30s video

[![LLMY Video](https://img.youtube.com/vi/IcEGcZFxXbw/0.jpg)](https://www.youtube.com/watch?v=IcEGcZFxXbw)


#### The pdf verion of slides summarized by LLM can be generated in two ways:

#### To generate slides in the *.tex* format, do the following steps:
1. Place the pdf files of research articles under the `pdf` folder
2. Run `./pdf_gen.sh` to generate slides in `.tex` format
3. Upload `.tex` to overleaf or generate pdf locally using LaTex compilers such as TeXstudio and Texmaker

#### To generate slides in the *.md*, do the following steps:
1. Create a markdown file similar to `output/LIFT_slides.md`.
2. In VS Code, download `Marp` VS Code Extension.
3. Run `Command + Shift + P` to use Marp to export the slide deck.

#### To launch the webapp
```
streamlit run webapp.py  
```

### Developers
Faradawn Yang

Andy Qin

Suraj Sudhakar

Ray Zhu

Jaehee Park

Victor Chen

### Licence
This code is licened under the MIT license.

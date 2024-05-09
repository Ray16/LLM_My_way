# Slide Generator Using LLM

### An LLM slide generator that summarizes research articles

Short 30s video

[![Video Title]()](LLMY_short_video.MOV "LLMY video")


#### This pdf verions of slides can be generated in two ways:

#### To generate slides in the *.tex* format, do the following steps:
1. Place the pdf files of research articles under the `pdf` folder
2. Run `./pdf_gen.sh` to generate slides in `.tex` format
3. Upload `.tex` to overleaf or generate pdf locally using LaTex compilers such as TeXstudio and Texmaker

#### To generate slides in the *.md*, do the following steps:
1. Create a markdown file similar to `output/LIFT_slides.md`.
2. In VS Code, download `Marp` VS Code Extension.
3. Run `Command + Shift + P` to use Marp to export the slide deck.

#### To build the package
1. Add scripts in `llmy/` folder.
2. Include them in `__init__.py`.
3. Build the package as follows
```
pip install wheel
python setup.py sdist bdist_wheel
pip install dist/llmy-0.1.0-py3-none-any.whl

# Use in your code
import llmy
llmy.summarize_pdf('pdf/LIFT_paper.pdf')

# Upload to Pypi (with an account)
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
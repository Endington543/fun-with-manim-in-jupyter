FROM gitpod/workspace-python-3.12

RUN sudo apt update

RUN sudo install-packages \
        build-essential \
        python3-dev \
        libcairo2-dev \
        libpango1.0-dev \
        ffmpeg

RUN sudo install-packages \
texlive \
texlive-latex-extra

RUN pip3 install manim
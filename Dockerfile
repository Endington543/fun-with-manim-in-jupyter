FROM gitpod/workspace-python

RUN sudo apt update

RUN sudo install-packages \
        build-essential \
        python3-dev \
        libcairo2-dev \
        libpango1.0-dev \
        ffmpeg

RUN pip3 install manim

RUN sudo install-packages \
        texlive \
        texlive-latex-extra
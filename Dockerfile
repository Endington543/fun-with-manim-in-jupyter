FROM gitpod/workspace-python-3.11

RUN sudo install-packages \
        libcairo2-dev \
        libpango1.0-dev \
        ffmpeg

RUN pip install manim

RUN sudo install-packages \
        build-essential \
        python3-dev \
        texlive \
        texlive-latex-extra
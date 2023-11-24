FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

ARG USERNAME=vscode

COPY library-scripts/common-debian.sh /tmp/library-scripts/
RUN apt-get update && bash /tmp/library-scripts/common-debian.sh true automatic automatic automatic false true true

# COPY library-scripts/docker-debian.sh /tmp/library-scripts/
# RUN apt-get update && bash /tmp/library-scripts/docker-debian.sh

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir -p /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.zsh_history" \
    && mkdir -p /commandhistory \
    && touch /commandhistory/.zsh_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.zshrc"

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    vim \
    git \
    git-lfs \
    nvtop \
    gpustat \
    zsh \
    tmux \
    wget \
    libgl1 \
    caca-utils \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools

RUN git lfs install

USER vscode 
RUN pip3 install --upgrade pip && pip3 install ipython ipykernel \
fastai duckduckgo_search \
nbdev \
fastbook \
gradio


# ENTRYPOINT ["/usr/local/share/docker-init.sh"]

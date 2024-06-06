FROM gitpod/workspace-full

USER gitpod
RUN sudo apt-get update \
    && sudo apt-get install -y chromium-browser chromium-chromedriver \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

    
FROM gitpod/workspace-mongodb

RUN ps --no-headers -o comm 1 && sudo apt-key list

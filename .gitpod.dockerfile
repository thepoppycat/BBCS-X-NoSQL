FROM gitpod/workspace-mongodb

RUN sudo systemctl daemon-reload && sudo systemctl start mongod

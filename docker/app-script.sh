#!/bin/bash

# Dockerfile만들고, .dockerignore 만들고
# docker build -t <repositoryname>:<version> .
cd ../back-end
docker build . -t flask-api

# docker-compose.yml 활용
# docker-compose pull
cd ../docker
docker-compose -f ./docker-compose.yml -p light-board-app up -d
# docker-compose -f ./docker-compose.yml -p light-board-app down

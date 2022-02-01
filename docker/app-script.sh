#!/bin/bash

# ================================ 최초 실행 ================================ #
# Dockerfile만들고, .dockerignore 만들고
# docker build -t <repositoryname>:<version> .
cd ../back-end
docker build . -t flask-api

# docker-compose.yml 활용
# docker-compose pull
cd ../docker
docker-compose -f ./docker-compose.yml -p light-board-app up -d

# stop 후 start 하기 
docker-compose -f ./docker-compose.yml -p light-board-app stop
docker-compose -f ./docker-compose.yml -p light-board-app start

# mongodb://lightboard:lightboard123%21@localhost:28018/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
# mongo db user setting 관련
# mongo --port 28018 admin -u lightboard -p
# db.getUsers();
# use admin
# db.createUser(
#   {
#     user: "lightboard",
#     pwd: "lightboard123!",
#     roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
#   }
# )
# db.grantRolesToUser('lightboard', [{ role: 'root', db: 'admin' }])

# network test
# docker network ls
# docker network inspect <id>

# ================================ back-end update 시 빌드 및 배포 실행 ================================ #

docker-compose -f ./docker-compose.yml -p light-board-app stop
docker-compose -f ./docker-compose.yml -p light-board-app down
docker image rm -f flask-api
cd ../back-end
docker build . -t flask-api
cd ../docker
docker-compose -f ./docker-compose.yml -p light-board-app up -d
# docker-compose -f ./docker-compose.yml -p light-board-app start
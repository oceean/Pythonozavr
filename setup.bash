#!/bin/bash

sudo docker pull postgres

sudo docker stop mbc-db

sudo docker rm mbc-db

sudo docker run --name mbc-db --network host -e POSTGRES_PASSWORD=KNSMBM -d postgres

sudo docker start mbc-db

sudo docker build -t mbc-server-img .

sudo docker stop mbc-server

sudo docker rm mbc-server

sudo docker run --name mbc-server --network host -d mbc-server-img

sudo docker start mbc-server

python3 -m webbrowser http://localhost:80
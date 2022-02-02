#!/bin/bash
cd /home/ubuntu/projects/light-board-crawler/crawler
source .venv/bin/activate
nohup python main_once.py > /dev/null 2>&1 &
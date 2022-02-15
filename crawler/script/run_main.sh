#!/bin/bash
cd /home/ubuntu/projects/light-board-crawler/crawler
. .venv/bin/activate
python main_once.py > /dev/null 2>&1
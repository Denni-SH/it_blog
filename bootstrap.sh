#!/bin/bash

apt-get update
apt-get install python3-pip -y
pip3 install --upgrade pip
cd /vagrant
pip3 install -r requirements.txt

python3 manage.py runserver 0.0.0.0:8000

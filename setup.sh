#!/usr/bin/env bash

set -x

apt-get update

apt-get install -y python3 python3-pip python3-dev

pip3 install -r /autograder/source/requirements.txt

apt-get install -y r-base r-base-dev

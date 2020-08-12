#!/bin/bash

docker run -v /root/.cache/:/cache/ -dit --name warm0_10_python3 python:rc-alpine3.12; docker exec warm0_10_python3 pip3 install sql
docker exec warm0_10_python3 python3 -m pip install --upgrade pip
docker cp /function/test/test.py warm0_10_python3:/
/function/test/function /function/test/test.py

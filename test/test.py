#!/usr/bin/python

import os
import numpy
from os import path
import sql
import requests
import redis

cmd="cat redis.py | grep ^import | sed -e 's/import//g' | sed 's/ //g'"
cont = os.popen(cmd).read().strip()
lib = cont.split()
print (lib[0])


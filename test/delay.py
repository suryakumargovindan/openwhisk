#!/usr/bin/python

import os
import time
from os import path
env='python'


def main():

    env='python'
    cmd='docker ps --filter "name=warm0_" | grep %s'%(env)
    time.sleep(10)
    print("Hello World!")
    return {cmd}

main()


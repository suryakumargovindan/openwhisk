#!/usr/bin/python

import datetime
from os import path
import sql
env='python'


def main():

    env='python'
    cmd='docker ps --filter "name=warm0_" | grep %s'%(env)
    print("Hello World!")
    return {cmd}

main()


#!/usr/bin/python

import os
from os import path
env='python'


def main():

    env='python'
    cmd='docker ps --filter "name=warm0_" | grep %s'%(env)
    print("Hello World!")
    return {cmd}

main()


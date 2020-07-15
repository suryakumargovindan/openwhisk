#!/usr/bin/python

import sys
import os
from os import path
import time

arguments = sys.argv
arg_count = len(sys.argv)

#print (sys.argv[0])
#print (arg_count)
#exit()


if len(sys.argv) == 2:
    function = sys.argv[1] 


def runtime():

    # Check and confirm that exactly and only one function is passed at a time as argument to this script
    if arg_count == 2:

        if path.exists(function):

            ext = arguments[1].split('.')

            if len(ext) > 1:
                runtime = ext[1]

                if runtime == 'py':
                    print("Runtime is python!")
                    return ("python")
                elif runtime == 'js':
                    print("Runtime is JavaScript!")
                    return ("nodejs")
                elif runtime == 'rb':
                    print("Runtime is Ruby!")
                    return ("ruby")
                elif runtime == 'jar':
                    print("Runtime is Java!")
                    return ("java")
                elif runtime == 'php':
                    print("Runtime is PHP!")
                    return ("php")
                elif runtime == 'swift':
                    print("Runtime is Swift!")
                    return ("swift")
                elif runtime == 'go':
                    print("Runtime is Go!")
                    return ("go")
                else:
                    print("Unknown runtime!")

            else:
                print("Runtime could not be identified! Quitting!")
                exit()

        else:
            print ("\nThe specified function - {} could not be found!\n".format(function))
            print ("Please check the input again!\n")
            print ("Quitting the execution now!\n")
            time.sleep(1)
            exit()

    elif arg_count > 2:
        print ("\nThere are more than one functions found! Please enter only one at a time!\n")
        print ("Quitting the execution now!\n")
        time.sleep(1)
        exit()

    elif arg_count == 1:
        print("\nNo function found to execute! Quitting!\n")
        print("Quitting the execution now!\n")
        time.sleep(1)
        exit()


def resource(env):
    
    pulse = 0
    
    #cmd = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)
    cmd = 'docker ps --filter "name=warm0_" | grep %s | wc -l'%(env)
    cont = os.popen(cmd).read().strip()
    print ("No. of warm {} containers running - {}".format(env,cont))

    # execute if cont is equal or more than 1

    if cont >= 1:
        pulse = 1
        print ("At least one warm container is running!")
        return (pulse)
    


def cache():
    
    cmd = "cat %s | grep ^import | sed -e 's/import//g' | sed 's/ //g'"%(function)
    cont = os.popen(cmd).read().strip()
    lib = cont.split()
    print (lib[0])


    # cache and handle the list of libraries displayed in lib variable


env = runtime()
pulse = resource(env)
cache()

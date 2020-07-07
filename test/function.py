#!/usr/bin/python

import sys

arguments = sys.argv
arg_count = len(sys.argv)


def runtime():

    if arg_count > 1:
        ext = arguments[1].split('.')

        if len(ext) > 1:
            runtime = ext[1]

            if runtime == 'py':
                print("Runtime is python!")
                return ("py")
            elif runtime == 'js':
                print("Runtime is JavaScript!")
                return ("js")
            elif runtime == 'c':
                print("Runtime is C!")
                return ("c")
            elif runtime == 'jar':
                print("Runtime is Java!")
                return ("java")
            else:
                print("Unknown runtime!")

        else:
            print("Runtime could not be identified! Quitting!")
            exit()

    else:
        print("No function found to execute! Quitting!")
        exit()


def execute():




env = runtime()
execute(env)


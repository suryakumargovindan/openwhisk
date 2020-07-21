import subprocess
import os


def request():

    request = "python /delay.py"


    cmd2 = "docker exec -i warm0_8_python2 {0}".format(request)

    p = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)

    poll = p.poll()

    if poll == None:
        print ("The process is still alive")
    


request()

from datetime import datetime
import csv
import sys
import time
import os


arguments = sys.argv
arg_count = len(sys.argv)

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
request_time = dt_string


#print (sys.argv[0])
#print (arg_count)
#exit()


if arg_count == 1:
        print("\nNo function found to execute! Quitting!\n")
        print("Quitting the execution now!\n")
        time.sleep(1)
        exit()


if len(sys.argv) == 2:
    function = sys.argv[1]


def resource():


    pulse = 0

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    req_time = dt_string


    #cmd = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)

    cmd1 = 'echo $(($(date +%s%N)/1000000))'
    exec_start = os.popen(cmd1).read().strip()

    cmd2 = "sudo wsk -i action create helloPython --kind python:3 {} && echo $(($(date +%s%N)/1000000)) > /tmp/whisk_log".format(function)
    os.system(cmd2)

    cmd3 = "sudo wsk -i action invoke helloPython --blocking"
    os.popen(cmd3).read().strip()

    cmd4 = ("sudo cat /tmp/whisk_log")
    exec_end = os.popen(cmd4).read().strip()
    exec_time = (int(exec_end)-int(exec_start))

    cmd5 = "sudo wsk -i action delete helloPython"
    os.system(cmd5)

    #print (req_time +" "+str(exec_time)+"ms")

    with open('whisk_list.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([req_time, function, exec_time])


resource()


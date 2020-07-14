import os
import sys
from datetime import datetime
import pandas
import csv


# datetime object containing current date and time

def resource():

    pulse = 0

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    req_time = dt_string

    
    #cmd = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)

    request = "python /test.py"
        
    cmd1 = 'echo $(($(date +%s%N)/1000000))'
    exec_start = os.popen(cmd1).read().strip()

    cmd2 = "docker exec -i warm0_1_python2 {0} && echo $(($(date +%s%N)/1000000)) > /tmp/2_log".format(request) 
    os.system(cmd2)

    cmd3 = ("cat /tmp/2_log") 

    exec_end = os.popen(cmd3).read().strip()
    exec_time = (int(exec_end)-int(exec_start))


    print (req_time +" "+str(exec_time)+"ms")


    with open('/function/test/dataset.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([req_time, request, exec_time])
    

resource()

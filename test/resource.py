import os
from datetime import datetime

# datetime object containing current date and time

def resource():

    pulse = 0

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    req_time = dt_string

    
    #cmd = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)
    cmd1 = 'echo $(($(date +%s%N)/1000000))'
    exec_start = os.popen(cmd1).read().strip()

    cmd2 = 'docker exec -it warm0_1_python2 python /test.py && echo $(($(date +%s%N)/1000000)) > /tmp/log' 
    os.system(cmd2)

    cmd3 = 'cat /tmp/log' 
    exec_end = os.popen(cmd3).read().strip()

    exec_time = (int(exec_end)-int(exec_start))

    print (req_time +" "+str(exec_time)+"ms")

resource()

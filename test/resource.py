import os
from datetime import datetime

# datetime object containing current date and time

def resource():

    pulse = 0

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    req_time = dt_string


    env = 'python'
    
    cmd1 = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)
    warm = os.popen(cmd1).read().strip()

    if warm >= 1:
        print "At least one warm container is present"
        
        cmd = "docker ps --format '{{.Names}}' | grep -i %s | grep -i warm | grep -v prewarm"%(env)
        out = os.popen(cmd).read().strip().split()
        containers = sorted(out)

        print (containers)
        exit()
    

    cmd2 = 'docker exec -i warm0_1_python2 python /hello.py > /tmp/warm_0_1_log' 
    os.system(cmd2)

resource()

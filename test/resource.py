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

        # Remove pulse here
        cmd2 = "docker exec -i %s python /hello.py > /tmp/warm_0_1_log"%(containers[0])

        
        # Add pulse here again
        print (cmd2)
        exit()

resource()

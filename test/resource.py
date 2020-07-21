import os
from datetime import datetime

# datetime object containing current date and time



def cont_pulse(container):

    cmd = "ps -ef | grep %s | grep docker | wc -l"%(container)
    count =  os.popen(cmd).read().strip()

    if int(count) > 1:
        pulse  = 1
    else:
        pulse = 0

    return (pulse)
    

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


        for x in containers:

            pulse = cont_pulse(x)
            
            if pulse == 0:
                execution_container = x
                print (execution_container)
            #    break
        
        
        
        #print (containers)  

        #pulse = cont_pulse(containers[0])

        #print(pulse)

         


        # Remove pulse here

        # Add pulse here again
        exit()

resource()

import os
from datetime import datetime
import requests

# datetime object containing current date and time



def container_pulse(container):

    cmd = "ps -ef | grep %s | grep docker | wc -l"%(container)
    count =  os.popen(cmd).read().strip()

    if int(count) > 1:
        pulse  = 1          #Pulse = 1 means warm container is already occupied
    else:
        pulse = 0           #Pulse = 0 means warm container is free and not occupied

    return (pulse)
    

def resource():

    pulse = 0

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    req_time = dt_string

    env = 'python'
    
    cmd1 = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)
    warm = os.popen(cmd1).read().strip()

    if warm >= 1:   #This means at least one warm container is present
        
        cmd = "docker ps --format '{{.Names}}' | grep -i %s | grep -i warm | grep -v prewarm"%(env)
        out = os.popen(cmd).read().strip().split()
        containers = sorted(out)

        for x in containers:

            pulse = container_pulse(x)
            
            if pulse == 0:
                container = x
                break
        
        ##execute(container,"test.py")
                
        


    else:        #Create a new warm container and install libraries from Cache

        cmd1 = "docker run -v /root/.cache/:/cache/ -dit --name warm0_12_python2 python:2.7-alpine"

        cmd2 = "cat %s | grep ^import | sed -e 's/import//g' | sed 's/ //g'"%("test.py")
        cont = os.popen(cmd).read().strip()
        lib = cont.split()


        for x in lib:

            response = requests.get("http://pypi.python.org/pypi/{}/json".format(x))

            if response.status_code == 200:
                
                ##call cache.py here and install libraries in the new container
                print ("dummy")
         
        

def execute(container,request): #to execute the function and then stop the container

    cmd1 = "docker exec -i {0} {1}".format(container,request)
    os.system(cmd1)


    cmd2 = "docker container stop {0}".format(container)
    os.system(cmd2)

    cmd3 = "docker container rm {0}".format(container)
    os.system(cmd3)


resource()
#execute("warm0_12_python2","python /delay.py")

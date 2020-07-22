import os
from datetime import datetime
import requests
import redis
from os import path

r1 = redis.StrictRedis(host='34.254.60.203', port=6379, db=1)
r2 = redis.StrictRedis(host='34.254.60.203', port=6379, db=2)
r3 = redis.StrictRedis(host='34.254.60.203', port=6379, db=3)
r4 = redis.StrictRedis(host='34.254.60.203', port=6379, db=4)


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

    if warm == 1:   #This means at least one warm container is present
        
        cmd = "docker ps --format '{{.Names}}' | grep -i %s | grep -i warm | grep -v prewarm"%(env)
        out = os.popen(cmd).read().strip().split()
        containers = sorted(out)

        for x in containers:

            pulse = container_pulse(x)
            
            if pulse == 0:
                container = x
                break
        
        ##install libraries
        ##execute(container,"test.py")
        


    else:        #Create a new warm container and install libraries from Cache

        print ("inside else")

        cmd1 = "docker run -v /root/.cache/:/cache/ -dit --name warm0_12_python2 python:2.7-alpine"
        os.system(cmd1)

        cmd2 = "cat %s | grep ^import | sed -e 's/import//g' | sed 's/ //g'"%("test.py")
        cont = os.popen(cmd2).read().strip()
        lib = cont.split()

        print (lib)

        for x in lib:

            response = requests.get("https://pypi.org/pypi/{}/json".format(x))

            if response.status_code == 200:         #Checks if the library is valid
                
                ##call cache.py here and install libraries in the new container

                print(x)

                lib_cpath = x+'_cpath'
                
                if r3.exists(lib_cpath) == True:

                    ## Use the path, install and call cache.py 

                    whl_path = r3.get(lib_cpath)

                    splt_char = "/"
                    K = 3

                    temp = whl_path.split(splt_char)
                    res = splt_char.join(temp[:K]), splt_char.join(temp[K:])
  
                    whl = '/cache/'+res[1] 

                    cmd = "docker exec -i warm0_12_python2 pip install %s"%whl 
                    os.system(cmd)

                
                else:
                    ##Dowload, install and call the cache.py

                    print("Downloading libraries as it's not found in cache")
                    
                    cmd = "docker exec -i warm0_12_python2 pip install %s"%x
                    os.system(cmd)

        execute("warm0_12_python2", "test.py") 

                

def execute(container,request): #to execute the function and then stop the container


    cmd0 = "docker cp {0} {1}:/".format(request, container)
    os.system(cmd0)

    cmd1 = "docker exec -i {0} python /{1}".format(container,request)
    os.system(cmd1)


    cmd2 = "docker container kill {0}".format(container)
    os.system(cmd2)

    cmd3 = "docker container rm {0}".format(container)
    os.system(cmd3)


def cache(lib):

    lib_freq = lib+'_freq'
    lib_count = lib+'_count'
    lib_cpath = lib+'_cpath'
    lib_last_used = lib+'_last_used'
    cpath = 'None'

    cache_dir = "/root/.cache/pip/wheels"

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    if path.exists(cache_dir):

        cmd = "find %s -name '*.whl' | grep -i %s"%(cache_dir,lib)
        cpath = os.popen(cmd).read().strip()


    entry = r1.exists(lib_freq)
    freq = r1.get(lib_freq)
    print(r1.get(lib_freq))
    print(freq)


    if entry == 0:
        r1.set(lib_freq,'NEW')
        r2.set(lib_count,1)
        r4.set(lib_last_used,today)


    elif (entry !=0 and freq == 'NEW'):
        r1.set(lib_freq,'INFREQUENT')
        r2.set(lib_count,2)
        r4.set(lib_last_used,today)


    elif (entry !=0 and freq == 'INFREQUENT'):

        count = int(r2.get(lib_count))

        if count == 5:

            r1.set(lib_freq,'FREQUENT')
            r4.set(lib_last_used,today)

            # Find the cache path, update it in redis and retain the cache

            if path.exists(cpath):
                r3.set(lib_cpath,cpath)

        elif count < 5:

            count += 1
            r2.set(lib_count,count)
            r4.set(lib_last_used,today)


    elif (entry !=0 and freq == 'FREQUENT'):

        # Check last used date of library, if it's used more than 10 days before then delete it and set status again to infrequent
        print("The library is used frequently!")
        r4.set(lib_last_used,today)

    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    last_used = r4.get(lib_last_used)

    d1 = datetime.strptime(today, "%Y-%m-%d")
    d2 = datetime.strptime(last_used, "%Y-%m-%d")
    difference = (abs((d1 - d2).days))

    if difference == 0:
       print "Library was used very recently!"


    #path = r1.exists(lib_cpath)
    #print (path)



resource()
#execute("warm0_12_python2","python /delay.py")

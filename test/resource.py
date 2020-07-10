import os

def resource():

    pulse = 0

    #cmd = "docker ps | grep -i %s | grep -i warm | grep -v prewarm | wc -l"%(env)
    cmd1 = 'echo $(($(date +%s%N)/1000000))'
    exec_start = os.popen(cmd1).read().strip()

    cmd2 = 'docker exec -it warm0_1_python2 python /test.py && echo $(($(date +%s%N)/1000000)) > /tmp/log' 
    os.popen(cmd2)

    #cmd3 = '/tmp/log' 
    #exec_end = os.popen(cmd3).read().strip()

    #exec_time = (int(exec_end)-int(exec_start))

    #print (exec_time)

resource()

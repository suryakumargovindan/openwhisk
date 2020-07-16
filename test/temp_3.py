
import redis
import os
from datetime import datetime
from os import path

r1 = redis.StrictRedis(host='34.254.60.203', port=6379, db=1)
r2 = redis.StrictRedis(host='34.254.60.203', port=6379, db=2)
r3 = redis.StrictRedis(host='34.254.60.203', port=6379, db=3)
r4 = redis.StrictRedis(host='34.254.60.203', port=6379, db=4)

def cache(lib):

    lib_freq = lib+'_freq'
    lib_count = lib+'_count'
    lib_cpath = lib+'_cpath'
    lib_last_used = lib+'_last_used'
    cpath = 'None'

    cache_dir = "/root/.cache/pip/wheels"

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

    
    elif (entry !=0 and freq == 'NEW'):
        r1.set(lib_freq,'INFREQUENT')
        r2.set(lib_count,2)
    
    
    elif (entry !=0 and freq == 'INFREQUENT'):
    
        count = int(r2.get(lib_count))
    
        if count == 5:
    
            r1.set(lib_freq,'FREQUENT')
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d")
            r4.set(lib_last_used,dt_string)
            
            # Find the cache path, update it in redis and retain the cache

            if path.exists(cpath):
                r3.set(lib_cpath,cpath)
    
        elif count < 5:
    
            count += 1
            r2.set(lib_count,count)
    
    
    elif (entry !=0 and freq == 'FREQUENT'):
    
        # Check last used date of library, if it's used more than 10 days before then delete it and set status again to infrequent
        print("The library is used frequently!")
    
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    last_used = r4.get(lib_last_used)
    
    d1 = datetime.strptime(today, "%Y-%m-%d")
    d2 = datetime.strptime(last_used, "%Y-%m-%d")
    difference = (abs((d1 - d2).days))
    
    if difference == 0:
       print "Last used before 10 days"
    
    
    #path = r1.exists(lib_cpath)
    #print (path)



def find(lib):


    lib_freq = lib+'_freq'
    lib_count = lib+'_count'
    lib_cpath = lib+'_cpath'
    lib_last_used = lib+'_last_used'


    print("\n\n")
    print(r1.get(lib_freq))
    print(r2.get(lib_count))
    print(r3.get(lib_cpath))
    print(r4.get(lib_last_used))



cache('sql')
find('sql')



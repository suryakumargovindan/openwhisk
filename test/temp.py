import redis

r1 = redis.StrictRedis(host='34.254.60.203', port=6379, db=1)
r2 = redis.StrictRedis(host='34.254.60.203', port=6379, db=2)
r3 = redis.StrictRedis(host='34.254.60.203', port=6379, db=3)
r4 = redis.StrictRedis(host='34.254.60.203', port=6379, db=4)

freq = r1.get('sql_freq')
print(freq)


if freq == 'None':
    r1.set('sql_freq','New')

elif freq == 'NEW':
    r2.set('sql_count',1)

elif freq == 'INFREQUENT':
    count = r2.get('sql_count')
    count += 1
    r2.set('sql_count','count')

    if freq == 5
        
        # update the cache path and retain the cache
        r3.set('sql_cpath','/root/.cache/pip/wheels/1a/18/5a/3c918b3de538cabab699fe6a29e0361313bf5a2d7e0b82325a/')

    else

        #check if lib exists in cache path and then delete it
        

elif freq == 'FREQUENT'
    

    # ensure cache path exists in r3 and library is present in the cache



r3.set('sql_cpath','/root/.cache/pip/wheels/1a/18/5a/3c918b3de538cabab699fe6a29e0361313bf5a2d7e0b82325a/')


r2 = redis.StrictRedis(host='34.254.60.203', port=6379, db=2)

path = r1.exists('sql_cpath')
print (path)





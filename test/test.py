import redis

r = redis.StrictRedis(host='34.254.60.203', port=6379, db=0)
r.set('test','/root/.cache/pip/wheels/1a/18/5a/3c918b3de538cabab699fe6a29e0361313bf5a2d7e0b82325a/')

path = r.get('test')
print (path)


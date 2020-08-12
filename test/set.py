import redis
from datetime import datetime

r1 = redis.StrictRedis(host='localhost', port=6379, db=1)
r2 = redis.StrictRedis(host='localhost', port=6379, db=2)
r3 = redis.StrictRedis(host='localhost', port=6379, db=3)
r4 = redis.StrictRedis(host='localhost', port=6379, db=4)




print("\n\n")
r3.set('sql_cpath', "/root/.cache/pip/wheels/1a/18/5a/3c918b3de538cabab699fe6a29e0361313bf5a2d7e0b82325a/sql-0.4.0-py3-none-any.whl")

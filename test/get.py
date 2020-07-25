import redis
from datetime import datetime

r1 = redis.StrictRedis(host='localhost', port=6379, db=1)
r2 = redis.StrictRedis(host='localhost', port=6379, db=2)
r3 = redis.StrictRedis(host='localhost', port=6379, db=3)
r4 = redis.StrictRedis(host='localhost', port=6379, db=4)
r5 = redis.StrictRedis(host='localhost', port=6379, db=5)



print("\n\n")
print(r1.get('sql_freq'))
print(r2.get('sql_count'))
print(r3.get('sql_cpath'))
print(r4.get('sql_last_used'))
print(r5.get('sql_install_time'))


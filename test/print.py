import redis
from datetime import datetime

r1 = redis.StrictRedis(host='34.254.60.203', port=6379, db=1)
r2 = redis.StrictRedis(host='34.254.60.203', port=6379, db=2)
r3 = redis.StrictRedis(host='34.254.60.203', port=6379, db=3)
r4 = redis.StrictRedis(host='34.254.60.203', port=6379, db=4)




print("\n\n")
print(r1.set('sql_freq','NEW'))
print(r2.set('sql_count',1))
print(r3.delete('sql_cpath'))
print(r3.get('sql_last_used'))

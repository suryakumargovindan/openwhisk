import redis
from datetime import datetime

r1 = redis.StrictRedis(host='localhost', port=6379, db=1)
r2 = redis.StrictRedis(host='localhost', port=6379, db=2)
r3 = redis.StrictRedis(host='localhost', port=6379, db=3)
r4 = redis.StrictRedis(host='localhost', port=6379, db=4)




print("\n\n")
print(r1.delete('sql_freq'))
print(r2.delete('sql_count'))
print(r3.delete('sql_cpath'))
print(r4.delete('sql_last_used'))

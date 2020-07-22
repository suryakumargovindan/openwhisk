import redis
from datetime import datetime

r1 = redis.StrictRedis(host='34.254.60.203', port=6379, db=1)
r2 = redis.StrictRedis(host='34.254.60.203', port=6379, db=2)
r3 = redis.StrictRedis(host='34.254.60.203', port=6379, db=3)
r4 = redis.StrictRedis(host='34.254.60.203', port=6379, db=4)




print("\n\n")

whl_path = r3.get('sql_cpath')
print (whl_path)


splt_char = "/"
K = 3


temp = whl_path.split(splt_char)
res = splt_char.join(temp[:K]), splt_char.join(temp[K:])
print (str(res[1]))


if r3.exists('sql_cpath') == True:
    print ("yes")

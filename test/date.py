from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
req_time = dt_string

dt_test = ("2017-07-09")

print (req_time < dt_test)



print(dt_string)
print(dt_test)
d1 = datetime.strptime(dt_string, "%Y-%m-%d")
d2 = datetime.strptime(dt_test, "%Y-%m-%d")
difference = (abs((d1 - d2).days))

if difference > 10:
    print "Last used before 10 days"


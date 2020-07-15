from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
req_time = dt_string

dt_test = ("2017-07-09")

print (req_time < dt_test)


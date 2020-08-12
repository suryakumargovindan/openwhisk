import pandas as pd
import os
from datetime import datetime, timedelta

header_list = ["time"]
filename = "/function/test/forecast.csv"
df = pd.read_csv(filename,names=header_list)

for i in range(len(df)):

    x = (df.loc[i, "time"])
    time = datetime.strptime(x,'%H:%M:%S')
    result = time - timedelta(seconds=4)
    result_time = str(result).split(' ',1)
    y = result_time[1]
    print(y)

    schedule = y.split(':',2)
    hour = schedule[0]
    minute = schedule[1]
    second = schedule[2]

    cmd = "echo 'sleep {0}; docker run -v /root/.cache/:/cache/ -dit --name warm0_10_python3 python:rc-alpine3.12; docker exec warm0_10_python3 pip3 install sql' | at {1}:{2}".format(second, hour, minute)
    os.system(cmd)

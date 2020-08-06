import os
import sys
from datetime import datetime
import csv

def utilization():

    pulse = 0

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    req_time = dt_string


    cmd1 = "free -k | grep Mem | awk '{print $3}'"
    memory = os.popen(cmd1).read().strip()

    cmd2 = "iostat | grep avg-cpu -A1 | awk 'NR>1' | awk '{print $1}'"
    cpu = os.popen(cmd2).read().strip()


    with open('/function/test/utilization.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([req_time, memory, cpu])
    

utilization()

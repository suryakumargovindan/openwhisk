import pandas as pd


header_list = ["time", "command", "duration"]
data_s = pd.read_csv('/function/test/dataset.csv', names=header_list)


commands = (data_s['command'].unique()).tolist()

print (commands)
group = data_s.groupby('command')
df_process = group.apply(lambda x: x['time'].unique())

print(df_process['python /test.py'])

for command in commands:
    times = df_process[command]

    times.str.split("t", n = 1, expand = True)




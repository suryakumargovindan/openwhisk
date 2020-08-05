import pandas as pd

header_list = ["time", "command", "duration"]
#filename = "C:/Users/Surya/OneDrive/NCI/RP/mount/server/dataset.csv"
filename = "/function/test/rp_dataset.csv"

df = pd.read_csv(filename,names=header_list)
df[['date','time']] = df["time"].str.split(" ", 1, expand = True)

df_time = pd.DataFrame()

df_time = df["time"].str.split(':', 0, expand = True)

hour = df_time.iloc[:,0]

minute = df_time.iloc[:,1]

second = df_time.iloc[:,2]

df_time.to_csv("/function/test/rp_formatted.csv", mode='a', sep=',', index=False, header=False)



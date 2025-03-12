import re
from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt

LOG_PATH = '/home/aubrey/Desktop/git_test/logs/2025-03-12.log'

# Read the log file
with open(LOG_PATH) as f:
    lines = f.readlines()

# Parse the log data, extracting timestamp, download_Mbps, and upload_Mbps using regular expressions.
# Result is saved as a list of dicts which can be imported by pandas.
mylist = []
mydict = {}
for line in lines:    
    timestamp = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+,-][0-9]{2}:[0-9]{2})", line)
    if timestamp:  
        if len(mydict) > 0:       
            mylist.append(mydict)
        mydict = {'timestamp': timestamp.group(1), 'download_Mbps': 0, 'upload_Mbps': 0}        
    download_Mbps = re.search(r"Download:\s+([0-9]+\.[0-9]+)\s+Mbit", line)
    if download_Mbps:
        mydict['download_Mbps'] = download_Mbps.group(1)               
    upload_Mbps = re.search(r"Upload:\s+([0-9]+\.[0-9]+)\s+Mbit", line)
    if upload_Mbps:
        mydict['upload_Mbps'] = upload_Mbps.group(1)        
mylist.append(mydict)
# ic(mylist)

# Import data into a pandas dataframe
df = pd.DataFrame(mylist)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['HM'] = df['timestamp'].dt.strftime('%H:%M')
df['download_Mbps'] = df['download_Mbps'].astype(float)
df['upload_Mbps'] = df['upload_Mbps'].astype(float)
# ic(df)

# Plot the data and save as PNG
df.plot(
    x='HM',
    y=['download_Mbps', 'upload_Mbps'],
    ylim=[0,300],
    title=LOG_PATH,
    xlabel='time (hour:minute)',
    ylabel='network speed (Mbps)'
);
plt.savefig(LOG_PATH.replace('.log', '.png'))
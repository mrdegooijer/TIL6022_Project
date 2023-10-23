#import subprocess
#subprocess.call(['pip', 'install', 'pandas', 'openpyxl'])
import pandas as pd
from datetime import datetime

# GitHub file URL
username = 'mrdegooijer'
repository = 'TIL6022_Project'
branch = 'main'
filepath_HS_Rdam = 'Data/Departures_HS_to_Rdam.xlsx'
filepath_Rdam_HS = 'Data/Departures_Rdam_to_HS.xlsx'

HS_Rdam_table = f'https://raw.githubusercontent.com/{username}/{repository}/{branch}/{filepath_HS_Rdam}'
Rdam_HS_table = f'https://raw.githubusercontent.com/{username}/{repository}/{branch}/{filepath_Rdam_HS}'

# Read Excel file into a DataFrame
df_HS_Rdam = pd.read_excel(HS_Rdam_table)
df_Rdam_HS = pd.read_excel(Rdam_HS_table)

# Print the DataFrame
print(df_HS_Rdam)
print(df_Rdam_HS)

#alltrains_df = pd.concat([df_HS_Rdam, df_Rdam_HS])

# Sort the concatenated DataFrame by its first column
#sorted_df = alltrains_df.sort_values(by=alltrains_df.columns[1])

# Print the sorted DataFrame
#print(sorted_df)

deptimes_HS = df_HS_Rdam[df_HS_Rdam.columns[0]].tolist()

# Convert the list elements to datetime format
deptimes_HS = pd.to_datetime(deptimes_HS, format='%H:%M:%S')

# Format the datetime objects as strings (HH:MM:SS)
deptimes_HS = deptimes_HS.strftime('%H:%M:%S').tolist()

traintype_HS = df_HS_Rdam[df_HS_Rdam.columns[8]].tolist()

# Print the list
print(deptimes_HS)
print(traintype_HS)

reference_time = pd.to_datetime('16:00:00', format='%H:%M:%S')
step_list = []
for i in deptimes_HS:
    delta = deptimes_HS[i]-reference_time
    seconds = delta.total_seconds()
    step_list.append(seconds)

print(step_list)

t1 = datetime.strptime(start_time, "%H:%M:%S")
print('Start time:', t1.time())

t2 = datetime.strptime(end_time, "%H:%M:%S")
print('End time:', t2.time())

# get difference
delta = t2 - t1

# time difference in seconds
print(f"Time difference is {delta.total_seconds()} seconds")

# time difference in milliseconds
ms = delta.total_seconds() * 1000
print(f"Time difference is {ms} milliseconds")
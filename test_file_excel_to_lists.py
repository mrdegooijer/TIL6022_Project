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

# Reverse the order of columns in df_Rdam_HS
df_Rdam_HS = df_Rdam_HS.iloc[:, ::-1]
print(df_Rdam_HS)

df_HS_Rdam_sorted = df_HS_Rdam.sort_values(by=df_HS_Rdam.columns[0])
df_Rdam_HS_sorted = df_Rdam_HS.sort_values(by=df_Rdam_HS.columns[7])

# Concatenate the sorted DataFrames
alltrains_df = pd.concat([df_HS_Rdam_sorted, df_Rdam_HS_sorted])
alltrains_sorted = alltrains_df.sort_values(by=alltrains_df.columns[0])
# Print the combined and sorted DataFrame
print(alltrains_sorted)

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

# Print only the time part
print(reference_time.strftime('%H:%M:%S'))

start_location = ["HS"] * len(traintype_HS)

print(start_location)
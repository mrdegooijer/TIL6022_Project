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
df_HS_Rdam = pd.read_excel(HS_Rdam_table, sheet_name='dep_times')
df_Rdam_HS = pd.read_excel(Rdam_HS_table, sheet_name='dep_times')

# Concatenate the sorted DataFrames
frames = [df_HS_Rdam, df_Rdam_HS]
alltrains_df = pd.concat(frames)
alltrains_sorted = alltrains_df.sort_values(by=alltrains_df.columns[0])
# Print the combined and sorted DataFrame
print(alltrains_sorted)

deptimes_alltrains = alltrains_sorted[alltrains_sorted.columns[0]].tolist()

# Convert the list elements to datetime format
deptimes_alltrains = pd.to_datetime(deptimes_alltrains, format='%H:%M:%S', errors='coerce')

# Format the datetime objects as strings (HH:MM:SS)
deptimes_alltrains = deptimes_alltrains.strftime('%H:%M:%S').tolist()

traintypes = alltrains_sorted[alltrains_sorted.columns[1]].tolist()
start_locations = alltrains_sorted[alltrains_sorted.columns[2]].tolist()

# Print the list
# print(deptimes_alltrains)
# print(traintypes)
# print(start_locations)

reference_time = pd.to_datetime('16:00:00', format='%H:%M:%S')

# Print only the time part
print("reference time is ", reference_time.strftime('%H:%M:%S'))

# Convert the list elements to datetime format
deptimes_alltrains = pd.to_datetime(deptimes_alltrains, format='%H:%M:%S')

# Set the start time
start_time = pd.to_datetime('16:00:00', format='%H:%M:%S')

# Calculate the time difference in seconds
time_diff_seconds = (deptimes_alltrains - start_time).total_seconds()

# Convert time difference to steps (assuming each step is 30 seconds)
step_duration_seconds = 30
steps = (time_diff_seconds / step_duration_seconds).astype(int)

departure_steps = steps.tolist()

#print(deptimes_alltrains)
print(departure_steps)
print(traintypes)
print(start_locations)

track_1= { }
track_2= { }
track_3= { }
track_4= { }

for i, (train_type, start_location) in enumerate(zip(traintypes, start_locations)):
    if train_type == 'IC':
        if start_location == 'R':
            track_1[i] = 0
        elif start_location == 'HS':
            track_3[i] = 22600 #aanpassen naar eindafstand
    elif train_type == 'spr':
        if start_location == 'R':
            track_2[i] = 0
        elif start_location == 'HS':
            track_4[i] = 22600 #aanpassen naar eindafstand

print("Track 1 (IC trains with start_location 'R'):", track_1)
print("Track 2 (spr trains with start_location 'R'):", track_2)
print("Track 3 (IC trains with start_location 'HS'):", track_3)
print("Track 4 (spr trains with start_location 'HS'):", track_4)




import pandas as pd
import plotly.express as px



file_path1 = r'C:\Users\Gebruiker\Documents\Delft\TIL6022_Project\Data\disruptions-2021.csv'
file_path2 = r'C:\Users\Gebruiker\Documents\Delft\TIL6022_Project\Data\disruptions-2022.csv'
data1 = pd.read_csv(file_path1)
data2 = pd.read_csv(file_path2)

traject_2021 = data1[data1['rdt_lines_id'] == '11']
traject_2022 = data2[data2['rdt_lines_id'] == '11']




fig1 = px.pie(traject_2021, values='duration_minutes', names='cause_en', title='taart test')
fig2 = px.pie(traject_2022, values='duration_minutes', names='cause_en', title='taart test')
fig1.show()
fig2.show()

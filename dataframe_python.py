import pandas as pd
import plotly.express as px



file_path1 = r'C:\Users\Gebruiker\Documents\Delft\TIL6022_Project\Data\disruptions-2021.csv'
file_path2 = r'C:\Users\Gebruiker\Documents\Delft\TIL6022_Project\Data\disruptions-2022.csv'
data1 = pd.read_csv(file_path1)
data2 = pd.read_csv(file_path2)

traject_2021 = data1[data1['rdt_lines_id'] == '11']
traject_2022 = data2[data2['rdt_lines_id'] == '11']




fig1 = px.pie(traject_2021, values='duration_minutes', names='cause_en')
fig2 = px.pie(traject_2022, values='duration_minutes', names='cause_en')

fig1.update_layout(title_text='Delays by cause 2021', title_x=0.5)
fig2.update_layout(title_text='Delays by cause 2022',title_x=0.5)

fig1.show()
fig2.show()

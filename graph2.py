import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("D:/MSc notes/internship/usa.csv")

grouped_data = data.groupby('MMWRyear')['Deaths'].apply(list).reset_index()

years = grouped_data['MMWRyear']
values = grouped_data['Deaths']

avg_values = [sum(vals) for vals in values]

plt.figure(figsize=(10, 6))

bar_width = 0.4

plt.bar([year - bar_width/2 for year in years], avg_values, width=bar_width, color='blue')

plt.xlabel('Year')
plt.ylabel('Average Values')
plt.title('Non Covid deaths in USA: 15-19 years age group')

plt.xticks(years)

plt.grid(axis='y')
plt.show()

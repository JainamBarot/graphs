import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:/MSc notes/internship/data.csv')

grouped_data = data.groupby('year')['value'].apply(list).reset_index()

years = grouped_data['year']
values = grouped_data['value']

avg_values = [sum(vals) / len(vals) for vals in values]

plt.figure(figsize=(10, 6))  # Adjust figure size as needed

bar_width = 0.4  # Adjust the width of the bars

plt.bar([year - bar_width/2 for year in years], avg_values, width=bar_width, color='blue')

plt.xlabel('Year')
plt.ylabel('Average Values')
plt.title('Excess Deaths in Europe: 15-44 years')

plt.xticks(years)

plt.grid(axis='y')
plt.show()

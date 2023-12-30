
import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_csv("D:/MSc notes/internship/covid.csv",encoding='cp1252')

vaccination_status = ['unvaccinated', '1 dose', '2 dose', 'Booster or 3rd dose']
case_rates = [1092.80,1527.57,2499.52,1466.76]

#confidence_interval = [(1063.90,1121.71),(1462.52,1592.63),(2462.50 ,2536.53),(1418.18 ,1515.33)]



plt.figure(figsize=(10, 6))
plt.bar(vaccination_status, case_rates, alpha=0.7, edgecolor='black', color= ['#006FFF','#FF0707', '#FFEF00', '#38DE1F'])

plt.xlabel('Vaccination status')
plt.title('Age-standardized case rates per 100,000 with 95% Confidence Interval(1 Jan - 7 Jan 2022)')
plt.show()

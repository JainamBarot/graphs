
import matplotlib.pyplot as plt
import pandas as pd

file = pd.ExcelFile("D:/MSc notes/internship/covid1.xlsx")
df1 = pd.read_excel(file,'Sheet2')

vaccination_status = ['unvaccinated', '1 dose', '2 dose', 'Booster or 3rd dose']
mortality_rate = [4.79, 0.36, 7.06,	0.21]

#confidence_interval = [(0.58 - 8.99), (0.00 - 1.05), (3.82 - 10.30), (0.07 - 0.34)]


plt.figure(figsize=(10, 6))
plt.bar(vaccination_status, mortality_rate, alpha=0.7, edgecolor='black', color= ['#006FFF','#FF0707', '#FFEF00', '#38DE1F'])

plt.xlabel('Vaccination status')
#plt.ylabel('Age Standardised Mortality Rate')
plt.title('Age-standardized mortality rate per 100,000(1 Jan - 7 Jan 2022)')
plt.show()

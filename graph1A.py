
import matplotlib.pyplot as plt
import pandas as pd

file = pd.ExcelFile("D:/MSc notes/internship/covid1.xlsx")
df1 = pd.read_excel(file,'Sheet1')

vaccination_status = ['unvaccinated', '1 dose', '2 dose', 'Booster or 3rd dose']
hospitalization_rates = [59.17, 63.78, 130.14, 14.82]

#confidence_interval = [(26.42, 91.92), (12.51, 115.04),(81.50, 178.79)	,(12.12, 17.53)]


plt.figure(figsize=(10, 6))
plt.bar(vaccination_status, hospitalization_rates, alpha=0.7, edgecolor='black', color= ['#006FFF','#FF0707', '#FFEF00', '#38DE1F'])

plt.xlabel('Vaccination status')
#plt.ylabel('Age Standardised hospitalisation Rate')
plt.title('Age-standardized rate of acute Covid-19 hospital admission(1 Jan - 7 Jan 2022)')
plt.show()

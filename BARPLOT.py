# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:04:58 2023

@author: -sm22alb
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from the CSV file
df = pd.read_csv('WB.csv', skiprows=4)

# Selecting data for the chosen countries and years
selected_countries = [
    'United States', 'China', 'United Kingdom', 
    'India', 'France', 'Japan'
]

selected_years = [str(year) for year in range(2010, 2016)]
# Splitting the line and using indentation for better readability
selected_data = df[
    df['Country Name'].isin(selected_countries)
][
    ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + \
   selected_years
]



# Extracting data for each indicator
ghg_emissions = selected_data[selected_data['Indicator Code'] == \
                              'EN.ATM.GHGT.KT.CE']
renewable_energy = selected_data[selected_data['Indicator Code']==\
                                 'EG.FEC.RNEW.ZS']
co2_emm = selected_data[selected_data['Indicator Code'] == 'EN.ATM.CO2E.KT']
power_consumption=selected_data[selected_data['Indicator Code']==\
                                'EG.USE.ELEC.KH.PC']
urban_population=selected_data[selected_data['Indicator Code']==\
                               'SP.URB.TOTL.IN.ZS']
agricultural_land = selected_data[selected_data['Indicator Code']==\
                                  'AG.LND.AGRI.ZS']
mortality_rate = selected_data[selected_data['Indicator Code']=='SH.DYN.MORT']

# Plotting bar graphs for the first two indicators

# Urban population growth
plt.figure(figsize=(10, 9))
sns.barplot(x='Country Name', hue='variable', y='value',\
            data=pd.melt(urban_population, id_vars=['Country Name'],\
                         value_vars=selected_years),palette='RdBu')
plt.xlabel('Country')
plt.ylabel('Urban population (% of total population)')
plt.title('Urban population (% of total population)(2010-2015)')
plt.legend(title='Year')

# Mortality rate
plt.figure(figsize=(10, 9))
sns.barplot(x='Country Name', hue='variable', y='value',\
            data=pd.melt(mortality_rate,\
                         id_vars=['Country Name']\
                             ,value_vars=selected_years),palette='PRGn')
    
plt.xlabel('Country')
plt.ylabel('Mortality rate, under-5 (per 1,000 live births)')
plt.title('Mortality rate, under-5 (per 1,000 live births) (2010-2015)')
plt.legend(title='Year')



plt.tight_layout()
plt.show()


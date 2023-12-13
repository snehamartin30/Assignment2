# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:07:20 2023

@author: -sm22alb
"""

import matplotlib.pyplot as plt
import pandas as pd



# Read data from the CSV file
df = pd.read_csv('WB.csv', skiprows=4)

# Selecting data for the chosen countries and years
selected_countries = ['United States', 'China', 'Germany', 'India', 'France',\
                      'Japan']
selected_years = [str(year) for year in range(2010, 2016)]

selected_data = df[df['Country Name'].isin(selected_countries)]\
    [['Country Name','Country Code', 'Indicator Name', \
      'Indicator Code'] + selected_years]

# Extracting data for each indicator
total_greenhouse_emission = selected_data[selected_data['Indicator Code'] == \
                                          'EN.ATM.GHGT.KT.CE']
renewable_energy = selected_data[selected_data['Indicator Code'] == \
                                 'EG.FEC.RNEW.ZS']
co2_emm = selected_data[selected_data['Indicator Code'] == \
                        'EN.ATM.CO2E.KT']
power_consumption = selected_data[selected_data['Indicator Code'] == \
                                  'EG.USE.ELEC.KH.PC']
urban_population = selected_data[selected_data['Indicator Code'] == \
                                 'SP.URB.TOTL.IN.ZS']
agricultural_land = selected_data[selected_data['Indicator Code']==\
                                  'AG.LND.AGRI.ZS']
mortality_rate = selected_data[selected_data['Indicator Code'] == \
                               'SH.DYN.MORT']
# Assuming power_consumption and ghg_emissions are your datasets

# Plotting line graphs for the first two indicators
plt.figure(figsize=(12, 9))

# Total greenhouse gas emission

for country in total_greenhouse_emission ['Country Name'].unique():
    country_data = total_greenhouse_emission[total_greenhouse_emission\
                                             ['Country Name'] == country]
    plt.plot(selected_years, country_data[selected_years].values.flatten()\
             , label=country, linestyle='--')

plt.xlabel('Year')
plt.ylabel('Total greenhouse gas emissions (kt of CO2 equivalent)')
plt.title('Total greenhouse gas emission(2010-2015)')
plt.legend(title='Country')
plt.grid(True)

# Renewable energy consumption(% of total final energy consumption)
plt.figure(figsize=(12, 9))
for country in renewable_energy['Country Name'].unique():
    country_data =renewable_energy[renewable_energy['Country Name'] == country]
    plt.plot(selected_years, country_data[selected_years].values.flatten()\
             , label=country, linestyle='--')

plt.xlabel('Year')
plt.ylabel('Renewable energy consumption (% of total final energy consumption)\
           ')
plt.title('Renewable energy consumption (% of total final energy consumption) \
          (2010-2015)')
plt.legend(title='Country')
plt.grid(True)

plt.tight_layout()
plt.show()

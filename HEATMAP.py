# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:08:28 2023

@author: -sm22alb
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from stats import skew, kurtosis
selected_countries = ['United States', 'China', 'Germany', 'India', 'France', \
                      'Japan']
selected_years = [str(year) for year in range(2010, 2016)]
selected_indicators = ['SP.URB.TOTL.IN.ZS','EN.ATM.GHGT.KT.CE',\
                       'EG.USE.ELEC.KH.PC','AG.LND.AGRI.ZS','SH.DYN.MORT',\
                           'EN.ATM.CO2E.PC','EG.ELC.RNEW.ZS']

def read_world_bank_data(file_path):
    # Read the World Bank data into a DataFrame
    df = pd.read_csv(file_path, skiprows=4)
    selected_data = df[df['Country Name'].isin(selected_countries)]\
        [['Country Name', 'Indicator Code'] + selected_years]
    selected_data = selected_data[selected_data\
                                  ['Indicator Code'].isin(selected_indicators)]
    selected_data.set_index(['Country Name', 'Indicator Code'], inplace=True)
    return selected_data

def clean_transposed_df(df):
    # Transpose the DataFrame to have years as columns
    df_transposed = df.transpose()

    # Drop rows with missing values
    df_transposed = df_transposed.dropna()

    return df_transposed

def create_heatmap(data, countries, indicators,country_name,indicator_name):
    # Filter the DataFrame for the specified countries and indicators
    #filtered_data = data[data.index.get_level_values('Indicator Code').isin(indicators)]
       
    #filtered_data = filtered_data[filtered_data.index.get_level_values\('Country Name').isin(countries)]

        

    # Transpose the DataFrame to have years as columns
    #transposed_data = filtered_data.transpose()



    
    correlation_matrix = data.corr()

    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, cmap='inferno', annot=True, fmt=".2f",\
                cbar_kws={'label': 'Correlation'}, linewidths=.5)
    plt.title(f"Correlation Heatmap for "+country_name)
    plt.xlabel('indicators')
    plt.ylabel('indicators')
    plt.yticks([i + 0.5 for i in range(len(indicator_name))], indicator_name)
    plt.xticks([i + 0.5 for i in range(len(indicator_name))], indicator_name)

    # Show the plot
    plt.show()
def calculate_skewness_and_kurtosis(data):
    skewness_results = []
    kurtosis_results = []

    for column in data.columns:
        # Skip columns that are not numeric
        if pd.api.types.is_numeric_dtype(data[column]):
            # Calculate skewness and kurtosis using the provided functions
            column_data = data[column].dropna()
            skewness = skew(column_data)
            kurt = kurtosis(column_data)

            # Append results to the lists
            skewness_results.append((column, skewness))
            kurtosis_results.append((column, kurt))

            print(f"Column: {column}")
            print(f"Skewness: {skewness}")
            print(f"Kurtosis: {kurt}\n")

    return skewness_results, kurtosis_results

    
def main():
    file_path = 'WB.csv'

    # Read World Bank data into a DataFrame
    world_bank_df = read_world_bank_data(file_path)

    # Clean and transpose the DataFrame
    transposed_df = clean_transposed_df(world_bank_df)
    df_years = transposed_df.copy()

    # Split the DataFrame into two DataFrames
    df_countries = world_bank_df.copy()
    #import pandas as pd

    # Assuming df_years is your existing DataFrame

    # Set 'Country Name' and 'Indicator Code' as the index
    #df_years.set_index(['Country Name', 'Indicator Code'], inplace=True)

    # Select only the rows where 'Country Name' is 'China'
    country_name = 'France'
    country_values_df = df_years[country_name]
    mean_country_values = country_values_df.mean()
    # Reset the index to make 'Country Name' and 'Indicator Code' regular columns
        
    #china_values_df.reset_index(inplace=True)

    # Display the new DataFrame with only the values for China
    print(country_values_df)
    indicator_name = ['Urban population','Mortality rate',\
                      ' Total greenhouse gas emission','CO2 emission',\
                          'Electric power consumption',\
                              'Renewable energy consumption',\
                                  'Agricultural land']
    

    # Print and visualize the data
    #print(df_years["China"])
    #print(df_years["China"]["EN.ATM.GHGT.KT.CE"])
    #print(df_years.describe())

    #print(df_countries)
    #print(df_countries.xs('EN.ATM.CO2E.KT', level='Indicator Code')["2010"])
    create_heatmap(country_values_df, selected_countries\
                   , selected_indicators,country_name,indicator_name)
    skewness_results, kurtosis_results =\
        calculate_skewness_and_kurtosis(country_values_df)
    # Optionally, you can save these DataFrames to new CSV files
   # df_years.to_csv('output_years.csv')
    #df_countries.to_csv('output_countries.csv')

    #print("DataFrames with years and countries have been created and saved.")

if __name__ == "__main__":
    main()

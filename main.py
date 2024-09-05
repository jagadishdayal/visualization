import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv.csv')

data = data.dropna()


average_growth_rate = data.iloc[:, 2:].mean(axis=1)
data['Average Growth Rate'] = average_growth_rate

top_countries = data.sort_values(by='Average Growth Rate', ascending=False).head(10)

print(top_countries[['Country Name', 'Average Growth Rate']])

# Plot a bar graph for the top 10 countries
plt.figure(figsize=(10, 6))
plt.bar(top_countries['Country Name'], top_countries['Average Growth Rate'], color='skyblue')
plt.xlabel('Country Name')
plt.ylabel('Average Growth Rate (%)')
plt.title('Top 10 Countries with Highest Average Population Growth Rate')
plt.xticks(rotation=45, ha='right')
plt.show()

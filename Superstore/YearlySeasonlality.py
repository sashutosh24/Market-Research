import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = '/mnt/data/superstore12.xlsx'
data = pd.read_excel(file_path)

# Convert Order Date to datetime and extract year and month
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.strftime('%b')

# Create Yearly Seasonality of Profit
monthly_profit = data.groupby(['Year', 'Month'])['Profit'].sum().unstack(level=0)
monthly_profit = monthly_profit.reindex(index=pd.date_range(start='2023-01', end='2023-12', freq='MS').strftime('%b'))

# Plot Yearly Seasonality of Profit
plt.figure(figsize=(10, 5))
for year in monthly_profit.columns:
    plt.plot(monthly_profit.index, monthly_profit[year], marker='o', label=f'Year {year}')
plt.title('Yearly Seasonality of Profit')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.legend(title='Year')
plt.grid(True)
plt.show()

# Create Holiday vs Non-Holiday Profit Impact
data['Holiday'] = data['Ship Mode'].apply(lambda x: 'Holiday' if x in ['Same Day', 'First Class'] else 'Non-Holiday')
holiday_profit = data.groupby(['Year', 'Holiday'])['Profit'].sum().unstack()

# Plot Holiday vs Non-Holiday Profit Impact
holiday_profit.plot(kind='bar', figsize=(10, 5), color=['orange', 'orangered'])
plt.title('Holiday vs Non-Holiday Profit Impact')
plt.xlabel('Year')
plt.ylabel('Total Profit')
plt.legend(title='Period')
plt.grid(axis='y')
plt.show()

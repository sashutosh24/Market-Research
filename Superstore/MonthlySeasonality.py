import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/superstore12.xlsx'
data = pd.read_excel(file_path)

# Convert Order Date to datetime and extract Year and Month
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.strftime('%b')

# Group by Year and Month to calculate total profit
monthly_profit = data.groupby(['Year', 'Month'])['Profit'].sum().unstack(level=0)

# Reorder the months for logical order
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_profit = monthly_profit.reindex(index=months_order)

# Plotting the line chart
plt.figure(figsize=(12, 6))
for year in monthly_profit.columns:
    plt.plot(monthly_profit.index, monthly_profit[year], marker='o', label=f'Year {year}')

# Add titles and labels
plt.title('Monthly Seasonality of Profit Across Years', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Profit', fontsize=12)

# Customize the legend and ticks
plt.legend(title='Year', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout for clarity
plt.tight_layout()

# Display the plot
plt.show()

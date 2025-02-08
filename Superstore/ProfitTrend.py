import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/superstore12.xlsx'
data = pd.read_excel(file_path)

# Convert Order Date to datetime and extract Year-Month
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year-Month'] = data['Order Date'].dt.to_period('M').astype(str)

# Group by Year-Month to calculate total profit
profit_trend = data.groupby('Year-Month')['Profit'].sum()

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(profit_trend.index, profit_trend.values, marker='o', color='orange')

# Add titles and labels
plt.title('Overall Profit Trend Over Time', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Profit', fontsize=12)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()

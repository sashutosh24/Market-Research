import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/superstore12.xlsx'
data = pd.read_excel(file_path)

# Convert Order Date to datetime and extract Month
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.strftime('%b')

# Group by Month to calculate total profit
monthly_profit = data.groupby('Month')['Profit'].sum()

# Reorder the months for chronological order
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_profit = monthly_profit.reindex(months_order)

# Plotting the bar chart
plt.figure(figsize=(12, 6))
plt.bar(monthly_profit.index, monthly_profit.values, color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Total Profit Distribution Across Months', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()

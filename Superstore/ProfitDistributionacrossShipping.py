import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/superstore12.xlsx'
data = pd.read_excel(file_path)

# Group by Ship Mode to calculate total profit
shipping_profit = data.groupby('Ship Mode')['Profit'].sum()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(shipping_profit.index, shipping_profit.values, color='purple', edgecolor='black')

# Add titles and labels
plt.title('Total Profit Distribution Across Shipping Modes', fontsize=14)
plt.xlabel('Shipping Mode', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()

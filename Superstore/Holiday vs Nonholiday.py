import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/superstore12.xlsx'
data = pd.read_excel(file_path)

# Convert Order Date to datetime and extract Year
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year

# Categorize 'Holiday' and 'Non-Holiday' based on Ship Mode
data['Holiday'] = data['Ship Mode'].apply(lambda x: 'Holiday' if x in ['Same Day', 'First Class'] else 'Non-Holiday')

# Group by Year and Holiday category to calculate total profit
holiday_profit = data.groupby(['Year', 'Holiday'])['Profit'].sum().unstack()

# Plotting the bar chart
holiday_profit.plot(kind='bar', figsize=(10, 6), color=['orange', 'orangered'])

# Add titles and labels
plt.title('Holiday vs Non-Holiday Profit Impact', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='Period', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()

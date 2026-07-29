import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the CSV data
# Replace 'your_data.csv' with your actual file path
file_path = 'dataset2.csv'
df = pd.read_csv(file_path)

# Preview columns to make sure you use the correct names
print("Available columns:", df.columns.tolist())

# Set a clean visual style using Seaborn
sns.set_theme(style="darkgrid")

# Create a figure canvas to hold multiple subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- PLOT 1: Line Chart (e.g., Trends over time) ---
# Replace 'Date' and 'Sales' with your column names
sns.lineplot(data=df, x='Date', y='Sales', marker='o', ax=axes[0], color='blue')
axes[0].set_title('Sales Trend Over Time')
axes[0].tick_params(axis='x', rotation=45)

# --- PLOT 2: Bar Chart (e.g., Categorical comparisons) ---
# Replace 'Category' and 'Revenue' with your column names
sns.barplot(data=df, x='Category', y='Revenue', ax=axes[1], palette='viridis')
axes[1].set_title('Revenue by Category')
axes[1].tick_params(axis='x', rotation=45)

# --- PLOT 3: Scatter Plot (e.g., Relationships/Correlations) ---
# Replace 'Budget' and 'Profit' with your column names
sns.scatterplot(data=df, x='Budget', y='Profit', alpha=0.7, ax=axes[2], color='emerald')
axes[2].set_title('Profit vs. Budget Correlation')

# Adjust layout automatically so labels do not overlap
plt.tight_layout()

# Display the visualizations on screen
plt.show()

# Optional: Save the visualization grid as an image file
# fig.savefig('csv_visualization_output.png', dpi=300)

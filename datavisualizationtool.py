import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(42)
data = {
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value': np.random.randn(100),
    'Date': pd.date_range(start='1/1/2020', periods=100)
}
df = pd.DataFrame(data)

# Set the style of seaborn
sns.set(style="whitegrid")

# 1. Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Value', data=df, estimator=np.mean, ci=None)
plt.title('Average Value by Category')
plt.ylabel('Average Value')
plt.xlabel('Category')
plt.show()

# 2. Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Value', data=df, marker='o')
plt.title('Value Over Time')
plt.ylabel('Value')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.show()

# 3. Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Value'], bins=15, kde=True)
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4. Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Value Distribution by Category')
plt.ylabel('Value')
plt.xlabel('Category')
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Date', y='Value', hue='Category', data=df)
plt.title('Value Scatter Plot by Category')
plt.ylabel('Value')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend(title='Category')
plt.show()

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from seaborn
df = sns.load_dataset('iris')

# -----------------------------
# Basic Data Inspection
# -----------------------------

# Shape of the dataset
print("Shape of the dataset:", df.shape)

# Column names
print("\nColumn names:", df.columns.tolist())

# First few rows
print("\nFirst 5 rows:")
print(df.head())

# Data types and non-null counts
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Data Visualization
# -----------------------------

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograms: Feature Distributions
df.hist(figsize=(10, 8), bins=20, edgecolor='black')
plt.suptitle("Histogram of Iris Features", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Box Plots: Outlier Detection
plt.figure(figsize=(12, 8))
for i, column in enumerate(df.select_dtypes(include='number').columns, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(data=df, y=column, x='species')
    plt.title(f'Box Plot of {column}')
    plt.xlabel('Species')
    plt.ylabel(column)
    plt.tight_layout()

plt.suptitle("Box Plots for Each Feature by Species", fontsize=16, y=1.02)
plt.show()

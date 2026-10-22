# Import necessary libraries for data manipulation and visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in Iris dataset
df = sns.load_dataset('iris')

# Display the first 5 rows of the dataset to inspect structure
print("--- First 5 Rows ---")
print(df.head())

# Generate summary statistics for numerical columns
print("\n--- Summary Statistics ---")
print(df.describe())

# Check for any missing values in the dataset
print("\n--- Missing Values Check ---")
print(df.isnull().sum())

# Create a pairplot visualization grouped by flower species
sns.pairplot(df, hue='species', markers=["o", "s", "D"])
plt.suptitle('Iris Dataset Exploratory Data Analysis', y=1.02)

# Show the generated plot
plt.show()
# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Task 1: Load and Explore the Dataset

    # Load Iris dataset CSV directly from URL
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)

    # Show first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nData types and missing values:")
    print(df.info())
    print(df.isnull().sum())

        # Task 2: Basic Data Analysis

    print("\nBasic statistics:")
    print(df.describe())

    # Group by 'species' and find mean sepal_length
    grouped = df.groupby('species')['sepal_length'].mean()
    print("\nMean Sepal Length per Species:")
    print(grouped)

    # Task 3: Data Visualization

    # 1. Line chart - mean sepal length by species
    grouped.plot(kind='line', marker='o', title='Mean Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Mean Sepal Length (cm)')
    plt.grid(True)
    plt.show()

    # 2. Bar chart - average petal length per species
    df.groupby('species')['petal_length'].mean().plot(kind='bar', color='skyblue', title='Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.show()

    # 3. Histogram - distribution of sepal width
    df['sepal_width'].plot(kind='hist', bins=15, color='lightgreen', edgecolor='black', title='Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.show()

    # 4. Scatter plot - sepal length vs petal length by species
    colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}
    plt.figure(figsize=(8,6))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.scatter(subset['sepal_length'], subset['petal_length'], label=species, color=colors[species])
    plt.title('Sepal Length vs Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

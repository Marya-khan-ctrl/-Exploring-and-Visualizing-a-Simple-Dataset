# -Exploring-and-Visualizing-a-Simple-Dataset

# Iris Dataset Exploration and Visualization

## Objective

The goal of this project is to explore and visualize the classic Iris dataset using Python. This includes loading the data, performing basic inspection and summary statistics, and generating a variety of plots to identify patterns, distributions, and potential outliers.

---

## Dataset

- **Name:** Iris Dataset  
- **Source:** Built-in seaborn dataset  
- **Classes:** 3 (Setosa, Versicolor, Virginica)  
- **Features:**  
  - sepal_length  
  - sepal_width  
  - petal_length  
  - petal_width  
  - species (target label)

---

## Technologies Used

- **Python 3.x**
- **Pandas** – for data loading and analysis
- **Seaborn** – for statistical visualization
- **Matplotlib** – for general plotting

---

## Steps Performed

### 1. Data Loading and Inspection

- Loaded the dataset using `seaborn.load_dataset()`.
- Inspected data using:
  - `.shape`
  - `.columns`
  - `.head()`
  - `.info()`
  - `.describe()`

### 2. Data Visualization

- **Scatter Plot:**  
  - Sepal Length vs Petal Length, colored by species.

- **Histograms:**  
  - Distribution of all numeric features.

- **Box Plots:**  
  - Comparison of features across species to identify potential outliers and variability.

---

## How to Run

1. Install required packages:
    ```bash
    pip install pandas seaborn matplotlib
    ```

2. Run the Python script:
    ```bash
    python iris_analysis.py
    ```

3. The script will display summary statistics and generate plots for data exploration.

---

## Output

The script generates the following visual outputs:
- A scatter plot comparing `sepal_length` and `petal_length` by species.
- Histograms of all numerical features.
- Box plots for each feature segmented by species.

---

## Conclusion

This project demonstrates basic techniques in data analysis and visualization, which are essential for any data science workflow. The Iris dataset is a great example for practicing these skills due to its simplicity and structure.

---


# Movie Industry Analysis: Correlation and Trends

## 🎥 Project Overview

This project explores the movie industry from **1980 to 2016** to identify the key factors that drive financial success. Using a dataset of over **6,800 films**, the analysis focuses on identifying which variables—such as budget, company, or user ratings—have the strongest relationship with a movie's gross revenue.

## 📂 Files in this Repository

| File Name | Description |
| --- | --- |
| `Movie Portfolio Project.ipynb` | Jupyter Notebook containing Python code for data cleaning, EDA, and visualization. |
| `movies.csv` | The raw dataset containing 15 distinct features for 6,820 movies. |

## 📊 Dataset Summary

* **Total Records:** 6,820 movies
* **Time Period:** 1980 – 2016
* **Key Variables:** * **Financial:** Budget, Gross
* **Descriptive:** Genre, Runtime, Rating, Year
* **Credits:** Company, Director, Writer, Star



## 🛠️ Technical Implementation

The analysis was performed using **Python** with the following library stack:

* **Pandas & NumPy:** Data manipulation and cleaning.
* **Seaborn & Matplotlib:** Statistical visualizations and heatmaps.

### Key Steps

1. **Data Cleaning:**
* Handled missing values and identified null percentages.
* Converted data types (Budget/Gross) to integers for clarity.
* Extracted standardized years from release dates to ensure chronological consistency.


2. **Exploratory Data Analysis (EDA):**
* Identified top-grossing films and removed duplicate entries.


3. **Correlation Analysis:**
* Created regression plots for **Budget vs. Gross**.
* Generated a **Pearson Correlation Matrix** to compare numeric features.
* Factorized categorical data (e.g., Company) to include them in the heatmap.



## 💡 Key Findings

* **Top Predictors:** **Budget** and **Votes** (user engagement) have the highest correlation with a movie's gross revenue.
* **Company Influence:** While production companies matter, their numeric correlation to gross was lower than the direct investment (budget).
* **Financial Trends:** There is a clear, positive linear relationship between investment and box office earnings.

---

## 🚀 How to Use

1. Clone this repository.
2. Ensure you have the required libraries installed:
```bash
pip install pandas numpy seaborn matplotlib

```

3. Open `Movie Portfolio Project.ipynb` in Jupyter Notebook or VS Code to view the analysis.

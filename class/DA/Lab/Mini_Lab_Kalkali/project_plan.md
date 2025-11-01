# Project Plan: Telco Customer Churn Prediction

This project plan outlines the steps to analyze the provided telco customer churn dataset and build a predictive model. The plan follows the structure outlined in the "Data Analytics Using Python" mini-project instructions.

## 1. Problem Definition & Dataset Selection

*   **Objective:** To analyze the factors influencing customer churn and to build a predictive model that can identify customers who are likely to churn. This is a classification problem.
*   **Dataset:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`. This dataset contains customer information and their churn status.
*   **Dataset Description:**
    *   **Rows:** 7043
    *   **Columns:** 21
    *   **Variables:** A mix of categorical (e.g., `gender`, `InternetService`) and numerical (e.g., `tenure`, `MonthlyCharges`) variables. The target variable is `Churn`.

## 2. Data Cleaning & Preparation

1.  **Load Data:** Load the `WA_Fn-UseC_-Telco-Customer-Churn.csv` file into a pandas DataFrame.
2.  **Handle Missing Values:** The `TotalCharges` column has missing values. These will be handled by removing the corresponding rows, as they represent a small fraction of the total data.
3.  **Remove Duplicates:** Check for and remove any duplicate rows.
4.  **Handle Outliers:** Investigate numerical columns for outliers using methods like the IQR or z-score and decide on a suitable handling strategy (e.g., capping, transformation).
5.  **Encode Categorical Data:** Convert categorical variables into a numerical format using one-hot encoding for nominal variables and label encoding for ordinal variables if any.
6.  **Normalize/Scale Data:** Scale numerical features using a suitable scaler (e.g., StandardScaler or MinMaxScaler) to ensure that all features contribute equally to the model.

## 3. Exploratory Data Analysis (EDA)

1.  **Univariate Analysis:**
    *   Create histograms and boxplots for numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`) to understand their distributions.
    *   Create bar charts for categorical features to visualize the distribution of customers across different categories.
2.  **Bivariate/Multivariate Analysis:**
    *   Create pairplots and a correlation heatmap to understand the relationships between numerical features.
    *   Use stacked bar charts or grouped bar charts to analyze the relationship between categorical features and the `Churn` variable.
3.  **Descriptive Statistics:** Calculate and interpret descriptive statistics (mean, median, standard deviation, etc.) for numerical columns.
4.  **Identify Patterns:** Look for trends, correlations, and anomalies in the data that might be indicative of churn.

## 4. Statistical Analysis & Hypothesis Testing

1.  **Formulate Hypotheses:**
    *   **H0 (Null Hypothesis):** There is no significant difference in the monthly charges between customers who churn and those who do not.
    *   **H1 (Alternative Hypothesis):** There is a significant difference in the monthly charges between customers who churn and those who do not.
2.  **Choose Statistical Test:** Use an appropriate statistical test, such as a t-test (to compare the means of two groups) or a chi-square test (to test the independence of two categorical variables).
3.  **Interpret Results:** Interpret the p-value and confidence intervals to determine the statistical significance of the findings.
4.  **Type I and Type II Errors:** Discuss the implications of Type I (false positive) and Type II (false negative) errors in the context of churn prediction.

## 5. Modeling and Pattern Discovery

This is a classification problem, so we will proceed with **Option B: Classification**.

1.  **Model Selection:** We will use **Logistic Regression** and **K-Nearest Neighbors (KNN)** as our classification models.
2.  **Train-Test Split:** Split the data into training and testing sets to evaluate the model's performance on unseen data.
3.  **Model Training:** Train the Logistic Regression and KNN models on the training data.
4.  **Model Evaluation:** Evaluate the models using metrics such as:
    *   **Accuracy:** The proportion of correctly classified instances.
    *   **Precision:** The proportion of positive identifications that were actually correct.
    *   **Recall:** The proportion of actual positives that were identified correctly.
    *   **F1-Score:** A weighted average of precision and recall.
    *   **Confusion Matrix:** To visualize the performance of the classification model.
    *   **ROC Curve and AUC:** To measure the model's ability to distinguish between classes.

## 6. Interpretation & Inference

1.  **Summarize Findings:** Summarize the key insights from the EDA and modeling steps.
2.  **Business Implications:** Discuss the business significance of the findings. For example, which customer segments are most at risk of churning? What actions could the business take to reduce churn?
3.  **Reflection:**
    *   What are the most significant predictors of churn?
    *   How did statistical testing validate the observations from EDA?
    *   What could be improved with more data or different features?

## 7. Visualization and Presentation

*   Use `Matplotlib` and `Seaborn` to create clear and informative visualizations throughout the analysis.
*   Ensure all plots have a title, axis labels, and a short caption explaining the visualization.

## 8. Conclusion

*   Provide a clear summary of the project's findings and conclusions.
*   Discuss the limitations of the analysis and suggest potential future improvements.

## Deliverables

1.  **Jupyter Notebook:** A notebook containing all the code, visualizations, and explanations for each step of the project.
2.  **Short Report (1-2 pages):** A summary of the project's objective, data source, methods, and key insights.

Data Analytics Using Python (CSE2101)

This teaching guide covers the core topics of Data Analytics Using Python in depth, including explanations of key concepts, practical Python examples, and illustrative visuals. The course emphasizes a hands-on introduction using environments like Google Colab or Jupyter Notebook, with focus on libraries such as Pandas, NumPy, Matplotlib, and Seaborn ￼. Below, each major topic is presented with clear explanations, example code, and supportive diagrams.

Introduction to Python for Data Analytics

Python is a versatile language widely used in data analysis and scientific computing. Its simple syntax and powerful libraries make it ideal for handling data and performing analytics tasks. Students should learn basic Python structures (lists, dictionaries, loops, functions) and environment tools (Jupyter notebooks, Google Colab). Jupyter notebooks allow writing code and documentation in one place, which is crucial for reproducible data science work ￼.
	•	Python basics: Variables, data types (strings, numbers, lists, dicts), control flow (if, for, while), and functions form the foundation.
	•	Interactive tools: Jupyter Notebook (and Colab) is a web-based interactive environment for running Python code in cells, combining text and visuals ￼.
	•	Example: A simple Python script manipulating a list and dictionary:

# Python basics: list and dictionary usage
numbers = [10, 20, 30, 40]
info = {'a': 1, 'b': 2, 'c': 3}

for num in numbers:
    print(f"Value: {num}, 'a' in dict?: {info.get('a')}")

This code creates a list of numbers and a dictionary, then iterates to print each number alongside a dictionary lookup. Such simple exercises build comfort with Python syntax.

Early on, emphasize installing packages (using pip), understanding environments, and loading data (e.g. reading files). For example, using !pip install pandas in a notebook to install packages. The course handout notes the aim to “combine foundational programming skills with practical techniques for analyzing data” ￼, which this section addresses by getting students familiar with the Python environment and syntax.

Data Handling and Manipulation (Pandas, NumPy)

Data often comes as tables or arrays, which Python handles via NumPy (numerical arrays) and Pandas (tabular data). These libraries are central: NumPy provides efficient n-dimensional array objects, and Pandas builds on NumPy to provide the DataFrame (2D labeled data) and Series (1D) structures. A DataFrame holds tabular data (rows and columns), similar to SQL tables or spreadsheets, and is widely used in data science ￼.

Key points:
	•	NumPy arrays: multidimensional arrays for numeric data. Useful for computations (vectorized math, linear algebra). For example, creating an array of values and performing element-wise operations:

import numpy as np

# NumPy array example
arr = np.array([1, 2, 3, 4])
print("Mean:", arr.mean(), "Std Dev:", arr.std())

	•	Pandas DataFrame: 2D data structure with labeled rows/columns. Supports mixed data types and powerful operations.
	•	Creating DataFrames: from lists/dicts or by reading files. Example: create a DataFrame and inspect it:

import pandas as pd

# Create DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 32, 37],
    'Score': [88.5, 92.0, 79.5]
}
df = pd.DataFrame(data)
print(df.head())

	•	Reading data: Often data is in CSV/Excel. Use pd.read_csv('file.csv') or pd.read_excel.
	•	Basic operations: df.describe() gives summary stats (count, mean, std, quartiles). Selection by column (df['Age']), row (via .loc or .iloc), filtering (df[df['Score'] > 80]), sorting, and grouping (e.g. df.groupby('Category') then aggregate) are essential tools.
	•	Example: Filter rows and compute group statistics:

# Filter and group example
df_filtered = df[df['Age'] > 30]  # select rows where Age > 30
print(df_filtered)

# Suppose we had a 'Department' column; group by it:
# df.groupby('Department')['Score'].mean()

Lists of common Pandas operations:
	•	Missing data handling (dropna, fillna; see below).
	•	Merging/joining DataFrames (pd.merge).
	•	Time-series support (date indices, resampling).
	•	Applying functions across columns: df['Col'].apply(func).

Pandas seamlessly interoperates with NumPy: columns of a DataFrame are numpy arrays internally ￼. Understanding these structures lets students quickly manipulate datasets in Python.

Data Visualization (Matplotlib, Seaborn)

Visualizing data is critical to understanding patterns. Python’s Matplotlib (low-level plotting) and Seaborn (higher-level interface) enable creating charts like line plots, scatter plots, histograms, bar charts, heatmaps, etc. The principle is to choose the right plot for the data: for example, use line charts for time trends, scatter plots for relationships between variables, and histograms to view distributions of a single variable.
	•	Matplotlib basics: The matplotlib.pyplot module (plt) provides functions like plt.plot(), plt.scatter(), plt.hist(), plt.bar(), etc. Always label axes (plt.xlabel, plt.ylabel) and add a title (plt.title). Example:

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y, marker='o')
plt.title("Sample Line Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

	•	Scatter plots: Show relationship/correlation between two numeric variables.
	•	Histograms: Show distribution of a single numeric variable (counts in bins). They reveal shape (normal, skewed), spread, and outliers.
Histogram of 100 samples from a standard normal distribution. Histograms help identify distribution shape and variability.
	•	Bar charts: Useful for categorical counts or comparing groups.
	•	Seaborn: Built on Matplotlib, simplifies complex plots and aesthetics. For example, sns.histplot(), sns.boxplot(), sns.pairplot() (for scatter-plot matrix), sns.heatmap(). Seaborn can plot a correlation matrix heatmap or categorical distributions easily.

Example using Seaborn:

import seaborn as sns

# Load an example dataset
df_iris = sns.load_dataset('iris')
# Pairplot shows scatter plots of each pair of variables, colored by species
sns.pairplot(df_iris, hue='species')

Plots like these can quickly reveal clusters (by species) and relationships between features. Good visuals make patterns and anomalies obvious, an essential step before modeling.

Fundamentals of Data Science (Types of Data, Lifecycle)

Data science blends statistics, computation, and domain knowledge. Key concepts:
	•	Types of data:
	•	Structured data: Organized in fixed tables (rows/columns), e.g. spreadsheets or SQL tables ￼. Easy to query and analyze.
	•	Unstructured data: No fixed schema (text, images, audio, etc.); more complex to process ￼. For instance, tweets, images, or PDFs require special handling (NLP, image analysis).
	•	Quantitative vs Qualitative: Quantitative data is numeric (counts, measurements); qualitative (categorical) data describes categories or characteristics.
	•	Data science lifecycle: An iterative process of obtaining and using data. A common workflow (similar to CRISP-DM) includes:
	1.	Business understanding: Define goals.
	2.	Data collection: Gather relevant data.
	3.	Data understanding & preparation: Clean and preprocess data.
	4.	Exploratory Data Analysis (EDA): Use statistics and visualization to explore data (see next section).
	5.	Modeling: Apply statistical or ML models.
	6.	Evaluation: Assess models (e.g. metrics, cross-validation).
	7.	Deployment/Communication: Present results or deploy model.

Data science “aims to convert large amounts of raw, unstructured data into meaningful insights” ￼. Understanding the lifecycle helps students approach problems methodically: for example, starting with cleaning data before jumping into modeling.

Data Collection and Preparation (Missing Data, Normalization)

Real-world data often has issues: missing values, outliers, inconsistent formats, etc. Data preparation is arguably the most time-consuming step and crucial for quality analysis.
	•	Missing data: Values can be missing at random or with a pattern. Common strategies:
	•	Drop missing: Remove rows/columns with missing entries (df.dropna()) ￼. Useful if few values are missing.
	•	Impute missing: Fill with a value, such as a constant or statistic (mean/median) using df.fillna(value=...) ￼.
	•	Flag missingness: Create an indicator variable for missing.
	•	Interpolation: For time series, fill based on neighboring values (df.interpolate()).

Example: Drop any row with a missing value, or fill missing with 0:

df_clean = df.dropna(axis=0, how='any')   # drop rows with any NaNs
df_fill = df.fillna(value=0)              # replace NaNs with 0

	•	Outliers: Extreme values can skew results. Detect via boxplots or Z-scores. Decide to remove or transform them.
	•	Normalization/Scaling: Many algorithms (e.g. KNN, K-Means) are sensitive to feature scales. Normalization typically means scaling numeric features:
	•	Min-max scaling: rescales values to [0,1]: X_scaled = (X - X.min())/(X.max()-X.min()).
	•	Z-score standardization: subtract mean and divide by standard deviation (using sklearn.preprocessing.StandardScaler).

Example using scikit-learn:

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # X is a numeric data matrix

Scaling ensures each feature contributes proportionally.
	•	Data encoding: Categorical variables need encoding (one-hot, label encoding). For instance, use pd.get_dummies(df, columns=['Category']) to convert categories into binary columns.

Preparing data carefully (handling missing values, encoding and scaling) is essential before analysis. Poorly handled data can lead to misleading results.

Exploratory Data Analysis (Distributions, Trends, Moments, Variability)

Exploratory Data Analysis (EDA) involves summarizing and visualizing the data to uncover patterns, anomalies, or hypotheses. Key aspects include:
	•	Distributions: Use histograms or density plots to inspect how values are spread. Check for normality or skewness.
Example: A histogram (below) shows the approximate normal distribution of data:
Histogram of random normal data illustrating a bell-shaped distribution.
This helps identify if data is centered (mean), spread out (variance), or has outliers.
	•	Trends and relationships: Scatter plots or line charts can reveal relationships between variables or temporal trends. For example, plotting sales vs. time might show seasonality or growth.
	•	Moments: Statistical moments quantify distribution shape:
	•	1st moment = mean (average); measures central location.
	•	2nd moment = variance (spread, square of std dev).
	•	3rd moment = skewness (asymmetry of distribution).
	•	4th moment = kurtosis (tailedness/peakedness).
In probability, mean is expectation, variance is second central moment, and skewness/kurtosis are standardized third/fourth moments ￼.
Example in code: df['Value'].mean(), .var(), .skew(), .kurt().
	•	Variability measures: Range, interquartile range (IQR), standard deviation all describe how spread out data is. Box plots are useful to visualize median, quartiles, and outliers.
	•	Summary statistics: Use df.describe() to get count, mean, std, min/max, quartiles for numeric features. For categorical data, df['Category'].value_counts() shows counts.

EDA is iterative and hypothesis-driven: e.g., “Does variable X correlate with Y?” Visual checks (scatter plots, correlation heatmaps) and statistics (correlation coefficient) help answer such questions.

Statistical Foundations (Hypothesis Testing, Confidence Intervals)

Data analytics relies on statistical inference to draw conclusions from samples. Two foundational concepts:
	•	Hypothesis testing: Formal method to test assumptions about data. You set up a null hypothesis H_0 (e.g. “no difference” or “parameter equals a value”) and an alternative H_A. Compute a test statistic (e.g., t-score, chi-square) and a p-value, the probability of observing data as extreme as that seen under H_0. If the p-value is below a significance level (commonly α=0.05), we reject H_0 (result is “statistically significant”) ￼.
	•	For example, a t-test can compare means of two groups (scipy.stats.ttest_ind(group1, group2)).
	•	p-value definition: Given H_0 is true, p-value is the probability of getting a test statistic at least as extreme as observed ￼. Small p-value (≤α) indicates the data is unlikely under H_0.
	•	Confidence intervals (CI): Instead of testing, we can estimate parameters with an interval. A 95% CI for a mean means that if we repeated sampling many times, about 95% of such intervals would contain the true population mean. Computed as \bar{x} \pm z^*\frac{\sigma}{\sqrt{n}} (for large samples) or using t-distribution for small samples. In practice, many libraries (like statsmodels or scipy) can compute CIs.
Example: For a sample mean mean = 50, std s = 5, n=100, a 95% CI is approximately 50 ± 1.96*(5/√100) = (49.02, 50.98).

Understanding statistical inference ensures that models have rigor: e.g. “We are 95% confident that the true difference in means lies in [a, b]” or “p=0.01 indicates significance”. Combining hypothesis testing with confidence intervals provides a complete view of uncertainty.

Machine Learning Basics (KNN, K-Means, Model Evaluation)

Supervised vs Unsupervised:
	•	Supervised learning uses labeled data (input features X and known outputs y) to train models that predict y.
	•	Unsupervised learning finds patterns in unlabeled data (no y provided), e.g. clustering.

K-Nearest Neighbors (KNN)

KNN is a simple, intuitive supervised classification algorithm. To classify a new point:
	1.	Compute its distance to all training points.
	2.	Find the k nearest neighbors (usually by Euclidean distance).
	3.	Assign the class most common among those neighbors ￼.

For example, with k=3: look at the 3 closest training points; if 2 are class A and 1 is class B, classify as A. KNN can also do regression (output the average value of neighbors). It is non-parametric (makes no explicit model assumptions) ￼.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Example: KNN on iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print("Test accuracy:", knn.score(X_test, y_test))

KNN’s accuracy can depend on k (too small can overfit, too large can smooth over differences) and on feature scaling (hence earlier normalization).

K-Means Clustering

K-Means is a simple unsupervised clustering algorithm. It partitions data into k clusters by iteratively:
	1.	Randomly initialize k centroids.
	2.	Assign each observation to the nearest centroid.
	3.	Update each centroid to be the mean of assigned points.
	4.	Repeat until convergence (assignments no longer change).

K-means aims to minimize within-cluster variance (sum of squared distances to centroids) ￼. Each cluster is represented by its centroid (mean). This algorithm assumes spherical clusters of similar size.

The image below illustrates K-means initialization and clustering steps:
Example of K-Means clustering: random points are iteratively assigned to the nearest centroids (colored), which are then updated until stable.

K-means is sensitive to the initial centroids and the choice of k. A common practice is to try different k (e.g. elbow method on inertia). In Python, use sklearn.cluster.KMeans:

from sklearn.cluster import KMeans

X = iris.data[:, :2]  # just first 2 features for visualization
kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(X)
print("Cluster centers:", kmeans.cluster_centers_)

Model Evaluation

After training a supervised model, evaluate its performance using appropriate metrics:
	•	Classification: Accuracy, precision, recall, F1-score, confusion matrix (e.g. sklearn.metrics.accuracy_score, confusion_matrix).
	•	Regression: Mean squared error (MSE), root MSE, R² (coefficient of determination).

Example of computing accuracy:

from sklearn.metrics import accuracy_score

y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

Always separate data into training and testing (or use cross-validation) to assess generalization. A low p-value or high accuracy suggests a model is capturing real patterns.

Feature Engineering and Dimensionality Reduction (Feature Selection, PCA)

Feature engineering involves creating or transforming variables to improve model performance. This includes:
	•	Generating new features: e.g. combining features (Feature * Feature), or extracting components (like date → day/month).
	•	Encoding categorical variables: using one-hot encoding (pd.get_dummies) or ordinal encoding.
	•	Selecting features: removing irrelevant features to reduce noise. Methods include:
	•	Filter methods: compute correlation of features with target (e.g. Pearson), drop low-correlation features.
	•	Wrapper methods: recursive feature elimination (RFE) using a model to score subsets.
	•	Embedded methods: regularization (Lasso) that shrinks coefficients of irrelevant features.

For example, sklearn.feature_selection.SelectKBest can pick top-k features by statistical test.

Dimensionality Reduction (PCA): Principal Component Analysis (PCA) is a technique to reduce many correlated variables to a smaller number of principal components that capture the majority of variance. PCA finds new orthogonal axes (directions) in the feature space. The first component explains the most variance, the second explains the next most, etc. By projecting data onto the top few components, we reduce dimensionality while retaining structure ￼.

from sklearn.decomposition import PCA

X_std = StandardScaler().fit_transform(iris.data)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)
print("Explained variance ratios:", pca.explained_variance_ratio_)

This might reduce 4 original features to 2 principal components while preserving, say, 90% of variance. PCA is useful for visualization (2D/3D plots) and speeding up models.

By engineering features carefully and reducing dimensions, we help algorithms learn better and faster. For instance, dropping redundant features can avoid the “curse of dimensionality,” and PCA can mitigate multicollinearity.

Predictive Modeling with Regression (Linear and Logistic Regression)

Regression models predict numeric or categorical outcomes from features:
	•	Linear Regression: Fits a linear model y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p + \varepsilon. Ordinary Least Squares (OLS) finds coefficients \beta that minimize the sum of squared errors. Use sklearn.linear_model.LinearRegression. Example on synthetic data:

from sklearn.linear_model import LinearRegression

# Synthetic linear data: y = 2*x + noise
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2.1, 3.9, 6.0, 8.2, 9.9])

model = LinearRegression()
model.fit(X, y)
print("Slope (beta):", model.coef_, "Intercept:", model.intercept_)
y_pred = model.predict(X)

Evaluate by R² score or MSE. A plot of y vs X with the fitted line illustrates the fit.

Linear regression example: data points (blue) and the fitted regression line (red).
	•	Logistic Regression: Used for classification when the target is binary (0/1). It models the log-odds of the probability p of class 1 as a linear combination of inputs ￼:
\log\frac{p}{1-p} = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p.
The model maps input to a probability via the logistic (sigmoid) function. In Python: sklearn.linear_model.LogisticRegression. For example, classifying iris species (setosa vs others):

from sklearn.linear_model import LogisticRegression

# Binary classification: is iris flower species 'setosa'?
y_bin = (iris.target == 0).astype(int)
logreg = LogisticRegression()
logreg.fit(iris.data, y_bin)
print("Coefficients:", logreg.coef_)
prob = logreg.predict_proba([[5.0, 3.0, 1.5, 0.2]])
print("Predicted probability of setosa:", prob[0][1])

Logistic regression outputs class probabilities; a cutoff (0.5 by default) yields predicted classes. Its strength is interpreting how each feature (via coefficients) affects the log-odds of the outcome.

Key metrics:
	•	For linear regression: R² (variance explained) and RMSE.
	•	For logistic regression: accuracy, ROC-AUC, confusion matrix.

Both regression methods build on the mathematical idea of fitting a function to data. Linear regression is solved by OLS (analytically or via numerical solvers) and logistic by maximizing likelihood.

References
	•	Course handout overview and aims ￼ ￼.
	•	Pandas DataFrame introduction ￼ ￼.
	•	Structured vs unstructured data ￼.
	•	Data science lifecycle steps ￼.
	•	Statistical moments (mean, variance, skewness, kurtosis) ￼.
	•	Hypothesis testing and p-value definition ￼.
	•	k-NN classification description ￼.
	•	k-Means clustering definition ￼.
	•	PCA dimensionality reduction ￼.
	•	Logistic regression model description ￼.

Each topic above includes practical Python examples and visuals. Students are encouraged to experiment with the code and modify examples to deepen understanding. This resource provides a comprehensive foundation for data analytics tasks in Python, aligning with the course outline and objectives.
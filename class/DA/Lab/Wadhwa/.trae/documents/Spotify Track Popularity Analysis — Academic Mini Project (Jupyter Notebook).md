## Project Overview
- Title: Robust Analysis of Spotify Track Popularity and Release Patterns
- Dataset: `spotify_data clean.csv` in project folder (only dataset)
- Objective: Predict popularity and investigate effects of explicitness, release type, genre, and timing using reproducible, well-validated methods.
- Style: Academic narrative and structure aligned with the provided inspiration notebook and DAP guidelines.

## Key Robustness Enhancements
- Reproducibility: Set global random seed; record library versions in the notebook.
- Clean Parsing: Strict dtype coercion; defensive handling for `album_release_date`, `explicit`, and numeric conversions.
- Genre Engineering: Multi-hot tokenization of `artist_genres` (split tokens, top-20 tokens one-hot; others bucketed) instead of single primary genre.
- Temporal Feature: `release_age_days` with robust fallback for missing dates; optional `release_weekday` categorical for timing patterns.
- Outlier Handling: Log-transform `artist_followers`; winsorize extreme numeric features (optional, configurable).
- Statistical Tests: Welch’s t-test for explicit vs non-explicit; one-way ANOVA for `album_type`; bootstrap confidence intervals to complement parametric results.
- Modeling: Compare LinearRegression with Ridge and ElasticNet; 5-fold cross-validation; pipeline with `ColumnTransformer`, imputation, scaling, and one-hot encoding.
- Evaluation: Train/test split + cross-val metrics; report `R²`, `RMSE`, `MAE`; residual diagnostics and permutation importance.
- Visualization Quality: Consistent styling; labeled axes and captions; readable color palette; tight layout.

## Notebook Structure (Cells)

### 1. Cover & Metadata
- Markdown: Title, student details (fill-in placeholders), course, institution, submission date
- Markdown: About project, dataset origin (local Spotify-curated data), purpose, academic framing

### 2. Environment & Imports
- Code: Seed set via `numpy` and Python `random`
- Code: Imports — `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy.stats`, `sklearn` (model_selection, preprocessing, compose, linear_model, metrics, inspection)
- Code: Print versions for reproducibility

### 3. Data Loading & Overview
- Code: Read CSV (relative path), show `shape`, `head`, `info`
- Markdown: Dataset overview, variable types (numeric, categorical, date)

### 4. Data Cleaning & Preparation
- Code: Defensive conversions
  - `album_release_date` → datetime with `errors='coerce'`
  - `explicit` string → boolean
  - Numeric coercions for `track_popularity`, `artist_popularity`, `artist_followers`, `track_duration_min`, `track_number`, `album_total_tracks`
- Code: Feature engineering
  - `release_age_days` from current date; `release_weekday` categorical
  - `log_followers` = `log1p(artist_followers)`
  - Genre tokens: split `artist_genres` on commas, trim, lowercase; top-20 tokens one-hot; others bucket
- Code: Duplicates removal by `track_id`
- Code: Optional winsorization for extreme numeric features
- Markdown: Justifications for each step

### 5. Exploratory Data Analysis (EDA)
- Univariate: Histograms of popularity, duration, `artist_popularity`, `log_followers`
- Bivariate: Boxplots of popularity by `explicit` and `album_type`; bar chart of mean popularity by top genre tokens; scatter of `artist_popularity` vs popularity colored by `album_type`
- Multivariate: Correlation heatmap for numeric features; pairplot (subset)
- Descriptive stats: mean, median, std, skewness, kurtosis; short insights

### 6. Statistical Analysis & Hypothesis Testing
- H0/H1 definitions
- Welch’s t-test for explicitness groups (with bootstrap 95% CI for mean difference)
- One-way ANOVA for `album_type` (with post-hoc pairwise t-tests, Bonferroni correction)
- Markdown: p-values, confidence intervals, Type I/II error discussion

### 7. Modeling and Validation
- Target: `track_popularity`
- Features: numeric + encoded categorical (`explicit`, `album_type`, genre tokens, `release_weekday`)
- Split: Train/test (80/20, `random_state=42`)
- Pipelines:
  - Baseline: `LinearRegression`
  - Regularized: `Ridge` (alpha grid) and `ElasticNet` (alpha, l1_ratio grid)
- Cross-validation: 5-fold on training data; report mean CV scores and std
- Evaluation: Test `R²`, `RMSE`, `MAE`; residual plot; permutation importance for best model
- Markdown: Interpretation of results and practical significance

### 8. Visualization & Presentation
- Consistent Matplotlib/Seaborn styling; titles, labels, legends, captions
- Layout calls to keep figures neat

### 9. Conclusion
- Summary of findings; limitations (no audio features like danceability/energy); future improvements (audio features, playlist data, regional context)

## Implementation Notes
- Use `ColumnTransformer` with `SimpleImputer` (median for numeric; most_frequent for categorical) and `StandardScaler`
- OneHotEncoder with `handle_unknown='ignore'`
- Metric functions: `r2_score`, `mean_squared_error` (sqrt), `mean_absolute_error`
- Permutation importance via `sklearn.inspection.permutation_importance`

## Deliverable
- Notebook file saved as `mini_project_spotify_CSE200.ipynb` in the working directory
- Only `spotify_data clean.csv` is used
- Academic narrative matching the inspiration notebook style

## Execution Plan
- Create the notebook with all sections and cells
- Run and verify cells end-to-end; ensure plots render and metrics compute
- Finalize and save the notebook
# CCOPD Exacerbation Prediction Webpage

This project creates a webpage using **Streamlit** to display visual results from Logistic Regression and XGBoost models on COPD data, featuring comparisons of model performance on raw and imputed datasets, along with performance metrics and feature importance visualization. 


## Workflow

1. **Types of Data Used**
   - **Raw Data**: Original COPD dataset without modifications.
   - **Imputed Data**: Dataset with missing values imputed to address data gaps.
   - **Imputed + Transformed Data**: Imputed dataset with additional data transformations and feature engineering applied.

2. **Modeling and Evaluation**
    - **Logistic Regression**
     - Conduct Logistic Regression on **Imputed Data** and  **Imputed + Transformed Data**.
     - Perform grid search for hyperparameter tuning.
     - Select features based on SHAP (SHapley Additive exPlanations) feature importance (50th percentile).
     - Generate insights and their model performance metrics
   - **XGBoost**
     - Conduct XGBoost on **Raw Data**, **Imputed Data** and  **Imputed + Transformed Data**.
     - Conduct XGBoost on model performance metrics of insights generated from LR and compare its first and final XGboost after feature selection
     - Compare logistic regression and XGBoost results for **Imputed Data** and  **Imputed + Transformed Data**.
     - SHAP feature selection (50th percentile)

3. **Visualization**
   - Logistic Regression evaluations/plots for **Imputed Data** and **Imputed + Transformed Data**.
   - XGBoost evaluations/plots for **Raw Data**, **Imputed Data** and  **Imputed + Transformed Data**.
   - Comparisons of XGBoost and Logistic Regressions for **Raw Data** vs **Imputed Data** and **Imputed + Transformed Data**.
   - SHAP plots for XGBoost on **Raw Data**.

These visualizations will allow users to explore model performance across different data types, view the results of feature selection, and interpret feature importance through SHAP analyses.


## Webpage Structure

The webpage will display the following components:

1. **Logistic Regression Visualizations**
   - **Imputed Data**: Performance metrics and evaluation plots for Logistic Regression on imputed data.
   - **Imputed + Transformed Data**: Performance metrics and evaluation plots for Logistic Regression on imputed and transformed data.

2. **XGBoost Visualizations**
   - **Raw Data**: Performance metrics and evaluation plots for XGBoost on raw COPD data.
   - **Imputed Data**: Performance metrics and evaluation plots for XGBoost on imputed data.
   - **Imputed + Transformed Data**: Performance metrics and evaluation plots for XGBoost on imputed and transformed data.

3. **SHAP Visualizations**
   - SHAP plots for XGBoost on raw data, comparing feature importance across data types to interpret model behavior.
   - **SHAP Analysis (LR)**: SHAP plots highlighting feature importance based on Logistic Regression results.
   - **SHAP Analysis (XGB)**: SHAP-based feature selection plots (50th percentile) for XGBoost, visualizing the most impactful features.

4. **Comparative Visualizations**
   - **LR vs XGB Comparison**: Side-by-side comparison of Logistic Regression and XGBoost performance on raw, imputed, and imputed + transformed data.
   - **First and Final XGB Comparison**: Visual comparison of the initial vs. final XGBoost model after feature selection and tuning, showcasing changes in performance metrics.


## How to Use

1. **Clone this Repository**
   git clone https://github.com/xinyelee/COPD_Webpage_Synergy.git
   cd COPD_Webpage_Synergy

2. **Run and Test the App Locally**
To ensure everything works correctly, test the app on your local machine.
Run the Streamlit app:
    streamlit run app.py
This command will open a local server at http://localhost:8501. Open this link in your browser to see the app.
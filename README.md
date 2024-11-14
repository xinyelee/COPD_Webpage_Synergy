# COPD Exacerbation Prediction Webpage

This project uses **Streamlit** to create a webpage displaying visual results from Logistic Regression and XGBoost models on COPD data. It features model performance comparisons on raw and imputed datasets, along with performance metrics and SHAP-based feature importance visualizations.

## Workflow Overview

1. **Data Types**:
   - **Raw Data**: Original COPD dataset.
   - **Imputed Data**: Dataset with missing values imputed.
   - **Imputed + Transformed Data**: Imputed data with additional transformations.

2. **Modeling and Evaluation**
    - **Logistic Regression**: Run on **Imputed Data** and  **Imputed + Transformed Data** with hyperparameter tuning and SHAP feature importance selection (50th percentile).
   - **XGBoost**: Run on all data types with with feature selection using SHAP and comparison to Logistic Regression.
    
3. **Visualization**
   - Logistic Regression plots for **Imputed Data** and  **Imputed + Transformed Data**
   - XGBoost plots for all threee types of data.
   - SHAP analysis for feature importance
   - Comparative visualizations for Logistic Regression vs. XGBoost and initial vs. final XGBoost 

## Webpage Structure

The webpage displays:
- **Logistic Regression Visualizations**: Performance metrics for **Imputed Data** and **Imputed + Transformed Data**
- **XGBoost Visualizations**: Performance metrics across raw, imputed, and transformed data
- **SHAP Visualizations**: Feature importance for both Logistic Regression and XGBoost.
- **Comparative Visualizations**: Side-by-side comparisons of model performance (LR vs XGB) and initial vs. final XGBoost model after feature selection and tuning, showcasing changes in performance metrics.


## How to Use

1. **Clone this Repository**
   ```bash
   git clone https://github.com/xinyelee/COPD_Webpage_Synergy.git
   cd COPD_Webpage_Synergy

2. **Run and Test the App Locally**

- **Install Dependencies**
   ```bash
   pip install -r requirements.txt
- **Run the Streamlit App**
   ```bash
   streamlit run app.py
- **Access the Local Server**
   Open http://localhost:8501 in your browser to view the app.
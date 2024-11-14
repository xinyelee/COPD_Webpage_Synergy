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
   - XGBoost plots for all three types of data.
   - SHAP analysis for feature importance
   - Comparative visualizations for Logistic Regression vs. XGBoost and initial vs. final XGBoost 

## Webpage Structure

The webpage displays:
- **Logistic Regression Visualizations**: Performance metrics for **Imputed Data** and **Imputed + Transformed Data**
- **XGBoost Visualizations**: Performance metrics across raw, imputed, and transformed data
- **SHAP Visualizations**: Feature importance for both Logistic Regression and XGBoost.
- **Comparative Visualizations**: Side-by-side comparisons of model performance (LR vs XGB) and initial vs. final XGBoost model after feature selection and tuning, showcasing changes in performance metrics.


## How to Use

1. **Access the Deployed App**
   - The app is deployed on Streamlit Cloud. You can access it directly at:
     [https://copd-dashboard-smu-fyp-team-synergy.streamlit.app/](https://copd-dashboard-smu-fyp-team-synergy.streamlit.app/)

2. **Run Locally**

   If you want to run the app locally, follow these steps:

   - **Clone this Repository**
     ```bash
     git clone https://github.com/xinyelee/COPD_Webpage_Synergy.git
     cd COPD_Webpage_Synergy
     ```

   - **Install Dependencies**
     ```bash
     pip install -r requirements.txt
     ```

   - **Run the Streamlit App**
     ```bash
     streamlit run app.py
     ```

   - **Access the Local Server**
     Open [http://localhost:8501](http://localhost:8501) in your browser to view the app.

## Updates and Redeployment

The app will automatically redeploy on Streamlit Cloud whenever changes are pushed to the main branch of this repository. Simply commit and push any updates (including new images in the `assets` folder) to see them reflected in the deployed app.

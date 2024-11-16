# COPD Exacerbation Prediction Webpage

This webpage leverages **Streamlit** to display insights from Logistic Regression and XGBoost models applied to COPD datasets.

## Key information:
   - Datasets: Raw, Imputed, and Imputed + Transformed.
   - Imputation: Techniques like MICE and missForest to handle missing values.
   - Logistic Regression on Imputed and Imputed + Transformed datasets only 
   - XGBoost on all three types of datasets
   - SHAP analysis for features selection
   - **Comparison**:
      - Evaluates baseline and fine-tuned models
      - Comparison between Logistic Regression and XGBoost for final model selection.
## Webpage Overview:
  - Overview Page: Project description 
  - EDA Page: all EDA related plots
  - First Iteration Page: all plots generated from first iteration
  - Final Methodology Page: all plots generated from final methodology 


## How to Use

1. **Access the Deployed App**
   - The app is deployed on Streamlit Cloud. You can access it directly at: https://copd-dashboard-smu-fyp-team-synergy.streamlit.app/ 

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

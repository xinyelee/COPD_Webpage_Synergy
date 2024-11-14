import streamlit as st
from PIL import Image
import os
from datetime import datetime

# Define paths to image directories based on dataset type
ASSETS_DIR = "assets"
DATA_TYPES = {
    "Raw Data": "Raw",
    "Imputed Data": "Imputed",
    "Imputed + Transformed Data": "Imputed_Transformed"
}

# Set page title and icon
st.set_page_config(page_title="COPD Data Dashboard", page_icon="📊", layout="wide")

# Title and description
st.title("📊 COPD Exacerbation Prediction Dashboard")
st.write("""
This dashboard, created by SMU Team Synergy, provides an analysis of COPD patient data using Logistic Regression and XGBoost models across different preprocessing techniques.
""")

# Sidebar options
st.sidebar.header("Filter Options")
data_type_choice = st.sidebar.selectbox("Select Data Type", list(DATA_TYPES.keys()))
data_type_folder = DATA_TYPES[data_type_choice]
st.sidebar.info(f"Dashboard by SMU Team Synergy | Last updated: {datetime.today().strftime('%d %b %Y')}")

# Key Features Section
st.markdown("## Key Features in the Dataset")
st.write("""
This dataset includes key features that impact COPD exacerbation risk, along with engineered features aimed at enhancing prediction accuracy and model insights:

- **Age**: Older age is often associated with higher exacerbation risk.
- **Smoking History**: Duration of smoking, critical in assessing respiratory conditions.
- **Spirometry Values (FEV1, FVC)**: Measures of lung function; lower values indicate severe airflow limitation.
- **Engineered Features**: Includes rolling averages and lagged spirometry values to capture temporal trends.
- **Comorbidities**: Presence of other conditions, such as cardiovascular issues, may influence exacerbation risk.
""")

# Key Insights Section
st.markdown("## Key Insights")
st.write("""
Here are some primary insights derived from the models and SHAP analysis:

- **Age** and **Smoking History** are significant predictors of exacerbation risk.
- **Spirometry Values** (FEV1, FVC) are crucial indicators, with lower values linked to higher risk.
- **Comorbidities** add valuable context for assessing risk among patients with complex health profiles.
""")

# Helper function to load and display image, with download option if image exists
def load_image_with_download(path, caption):
    if os.path.exists(path):
        img = Image.open(path)
        st.image(img, caption=caption)
        with open(path, "rb") as file:
            btn = st.download_button(
                label=f"Download {caption}",
                data=file,
                file_name=os.path.basename(path),
                mime="image/png"
            )
    else:
        st.warning(f"{caption} image is not available. Please upload the necessary files to the assets folder.")

# Section 1: Logistic Regression Visualizations
st.markdown("---")
st.header("1. Logistic Regression Visualizations")
st.write("""
Logistic Regression is used to analyze binary outcomes (exacerbation vs. no exacerbation) and is effective when linear relationships exist between predictors and log-odds. Key performance metrics include AUPRC, balanced accuracy, and log loss.
""")
lr_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"LR_{data_type_folder.lower()}.png")
load_image_with_download(lr_image_path, f"Logistic Regression on {data_type_choice}")

# Section 2: XGBoost Visualizations
st.markdown("---")
st.header("2. XGBoost Visualizations")
st.write("""
XGBoost is well-suited for handling non-linear relationships and imbalanced data. This section highlights performance metrics across raw, imputed, and transformed datasets, showcasing improvements in prediction accuracy when using engineered features and imputation.
""")
xgb_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"XGB_{data_type_folder.lower()}.png")
load_image_with_download(xgb_image_path, f"XGBoost on {data_type_choice}")

# Section 3: SHAP Feature Importance
st.markdown("---")
st.header("3. SHAP Analysis")
st.write("""
SHAP analysis provides insights into feature importance, showing how each feature impacts model predictions on an individual level.
""")

# SHAP for XGBoost (all data types)
st.subheader("XGBoost SHAP Analysis")
st.write("""
The SHAP summary plot for XGBoost reveals key features such as **Age**, **Smoking History**, and **FEV1**. By examining SHAP values, clinicians can understand the direction and magnitude of each feature's influence on exacerbation predictions.
""")
shap_xgb_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_XGB_{data_type_folder.lower()}.png")
load_image_with_download(shap_xgb_path, f"SHAP Feature Importance for XGBoost on {data_type_choice}")

# SHAP for Logistic Regression (only for imputed and transformed data)
if data_type_choice in ["Imputed Data", "Imputed + Transformed Data"]:
    st.subheader("Logistic Regression SHAP Analysis")
    st.write("""
    The SHAP plot for Logistic Regression emphasizes features impacting the linear model’s decisions. Differences from the XGBoost SHAP analysis may reveal insights specific to linear relationships in exacerbation risk.
    """)
    shap_lr_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_LR_{data_type_folder.lower()}.png")
    load_image_with_download(shap_lr_path, f"SHAP Feature Importance for Logistic Regression on {data_type_choice}")

# Section 4: Comparative Visualizations
st.markdown("---")
st.header("4. Comparative Visualizations")
st.write("""
Comparison charts allow for visual evaluation of Logistic Regression versus XGBoost, and initial versus tuned XGBoost models. These comparisons reveal how feature selection, data imputation, and hyperparameter tuning improve model performance.
""")

with st.expander("Logistic Regression vs XGBoost Comparison", expanded=True):
    comparison_lr_xgb_path = os.path.join(ASSETS_DIR, "Comparisons", "LR_vs_XGB.png")
    load_image_with_download(comparison_lr_xgb_path, "Comparison of Logistic Regression and XGBoost")

with st.expander("Initial vs Final XGBoost Comparison", expanded=True):
    comparison_xgb_final_path = os.path.join(ASSETS_DIR, "Comparisons", "XGB_initial_vs_final.png")
    load_image_with_download(comparison_xgb_final_path, "Comparison of Initial and Final XGBoost Models")

# Footer with information about the project and sources
st.markdown("---")
st.markdown("**COPD Exacerbation Prediction Dashboard**")


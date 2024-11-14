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
This dataset includes key features known to impact COPD exacerbation risk, as well as engineered features to enhance prediction accuracy:

- **Age**: Age of the patient, with older age often associated with higher exacerbation risk.
- **Smoking History**: Number of years of smoking, a significant factor in respiratory conditions.
- **Spirometry Values (FEV1, FVC)**: Measures of lung function. Lower values indicate more severe airflow limitation.
- **Engineered Features**: Derived features, such as rolling averages and lagged values of spirometry measurements, to capture temporal patterns in the data.
""")

# Key Insights Section
st.markdown("## Key Insights")
st.write("""
- **Age** and **Smoking History** are significant predictors of exacerbation risk.
- **Spirometry Values** indicate lung function, with lower values associated with higher risk.
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
st.markdown("---")  # Section divider
st.header("1. Logistic Regression Visualizations")
lr_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"LR_{data_type_folder.lower()}.png")
load_image_with_download(lr_image_path, f"Logistic Regression on {data_type_choice}")

# Section 2: XGBoost Visualizations
st.markdown("---")
st.header("2. XGBoost Visualizations")
xgb_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"XGB_{data_type_folder.lower()}.png")
load_image_with_download(xgb_image_path, f"XGBoost on {data_type_choice}")

# Section 3: SHAP Feature Importance
st.markdown("---")
st.header("3. SHAP Analysis")

# SHAP for XGBoost (all data types)
st.subheader("XGBoost SHAP Analysis")
shap_xgb_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_XGB_{data_type_folder.lower()}.png")
load_image_with_download(shap_xgb_path, f"SHAP Feature Importance for XGBoost on {data_type_choice}")

# SHAP for Logistic Regression (only for imputed and transformed data)
if data_type_choice in ["Imputed Data", "Imputed + Transformed Data"]:
    st.subheader("Logistic Regression SHAP Analysis")
    shap_lr_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_LR_{data_type_folder.lower()}.png")
    load_image_with_download(shap_lr_path, f"SHAP Feature Importance for Logistic Regression on {data_type_choice}")

# Section 4: Comparative Visualizations
st.markdown("---")
st.header("4. Comparative Visualizations")

with st.expander("Logistic Regression vs XGBoost Comparison", expanded=True):
    comparison_lr_xgb_path = os.path.join(ASSETS_DIR, "Comparisons", "LR_vs_XGB.png")
    load_image_with_download(comparison_lr_xgb_path, "Comparison of Logistic Regression and XGBoost")

with st.expander("Initial vs Final XGBoost Comparison", expanded=True):
    comparison_xgb_final_path = os.path.join(ASSETS_DIR, "Comparisons", "XGB_initial_vs_final.png")
    load_image_with_download(comparison_xgb_final_path, "Comparison of Initial and Final XGBoost Models")

# Footer with information about the project and sources
st.markdown("---")
st.markdown("**COPD Exacerbation Prediction Dashboard**")
st.write("""
This dashboard is developed by SMU Team Synergy to provide insights into COPD exacerbation risk factors and model performance. For more information, see the [Streamlit documentation](https://docs.streamlit.io/).
""")

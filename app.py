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

st.set_page_config(page_title="COPD Exacerbation Prediction Dashboard", page_icon="📊", layout="wide")

# Title and description
st.title("📊 COPD Exacerbation Prediction Dashboard")
st.write("""
This dashboard displays visual results from Logistic Regression and XGBoost models on COPD data, 
featuring comparisons of model performance across different data types, along with feature importance visualizations.
""")

# Sidebar Filter for Data Type
st.sidebar.header("Filter Options")
data_type_choice = st.sidebar.selectbox("Select Data Type", list(DATA_TYPES.keys()))
data_type_folder = DATA_TYPES[data_type_choice]

# Sidebar information about the dashboard
st.sidebar.markdown("### About This Dashboard")
last_updated_date = datetime.today().strftime("%d %b %Y") 
st.sidebar.info(f"This dashboard is created by SMU Team Synergy and last updated on {last_updated_date}.")

# Loading spinner for visual feedback while loading images
with st.spinner("Loading images and visualizations..."):

    # Helper function to load an image if it exists
    def load_image(path, caption):
        if os.path.exists(path):
            img = Image.open(path)
            st.image(img, caption=caption)
        else:
            st.warning(f"{caption} image is not available. Please upload the necessary files to the assets folder.")

    # Section 1: Logistic Regression Visualizations
    st.markdown("---")  # Section divider
    st.header("1. Logistic Regression Visualizations")
    lr_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"LR_{data_type_folder.lower()}.png")
    load_image(lr_image_path, f"Logistic Regression on {data_type_choice}")

    # Section 2: XGBoost Visualizations
    st.markdown("---")
    st.header("2. XGBoost Visualizations")
    xgb_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"XGB_{data_type_folder.lower()}.png")
    load_image(xgb_image_path, f"XGBoost on {data_type_choice}")

    # Section 3: SHAP Feature Importance
    st.markdown("---")
    st.header("3. SHAP Analysis")
    st.subheader("XGBoost SHAP Analysis")
    shap_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_XGB_{data_type_folder.lower()}.png")
    load_image(shap_image_path, f"SHAP Feature Importance for XGBoost on {data_type_choice}")

    # Section 4: Comparative Visualizations
    st.markdown("---")
    st.header("4. Comparative Visualizations")
    with st.expander("Logistic Regression vs XGBoost Comparison", expanded=True):
        comparison_lr_xgb_path = os.path.join(ASSETS_DIR, "Comparisons", "LR_vs_XGB.png")
        load_image(comparison_lr_xgb_path, "Comparison of Logistic Regression and XGBoost")

    with st.expander("Initial vs Final XGBoost Comparison", expanded=True):
        comparison_xgb_final_path = os.path.join(ASSETS_DIR, "Comparisons", "XGB_initial_vs_final.png")
        load_image(comparison_xgb_final_path, "Comparison of Initial and Final XGBoost Models")

# Additional interactive widget (tbc)


# Footer with information about the project and sources
st.markdown("---")
st.markdown("**COPD Exacerbation Prediction Dashboard**")

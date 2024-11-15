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
This dashboard, created by SMU Team Synergy, provides insights into model performance on COPD datasets. 
It includes visualizations for Logistic Regression and XGBoost models, as well as SHAP analysis to understand feature importance.
""")

# Sidebar options
st.sidebar.header("Filter Options")
display_all_data_types = st.sidebar.checkbox("All Data Types")
if not display_all_data_types:
    data_type_choice = st.sidebar.selectbox("Select Data Type", list(DATA_TYPES.keys()))
    data_type_folder = DATA_TYPES[data_type_choice]
else:
    data_type_choice = "All Data Types"

# Checkboxes for Visualization Sections
st.sidebar.subheader("Select Sections")
select_all = st.sidebar.checkbox("Select All", value=True)

view_logistic_regression = st.sidebar.checkbox("Logistic Regression", value=select_all)
view_xgboost = st.sidebar.checkbox("XGBoost", value=select_all)
view_shap_analysis = st.sidebar.checkbox("SHAP Analysis", value=select_all)
view_comparative_insights = st.sidebar.checkbox("Comparative Insights", value=select_all)

# Set a fixed "last updated" date
last_updated_date = datetime(2024, 11, 14)
st.sidebar.info(f"Dashboard by SMU Team Synergy | Last updated: {last_updated_date.strftime('%d %b %Y')}")

# Helper function to load and display image, with error message if image is missing
def load_image_with_download(path, caption):
    if os.path.exists(path):
        img = Image.open(path)
        st.image(img, caption=caption)
        with open(path, "rb") as file:
            st.download_button(
                label=f"Download {caption}",
                data=file,
                file_name=os.path.basename(path),
                mime="image/png"
            )
    else:
        st.warning(f"{caption} image is not available. Please upload the necessary files to the assets folder.")

# Section to display key features and insights
st.markdown("## Key Features in the Dataset")
st.write("""
This dataset includes key features impacting COPD exacerbation risk, along with engineered features aimed at enhancing prediction accuracy:

- **Age**: Older age often correlates with higher exacerbation risk.
- **Smoking History**: Duration and status of smoking, critical in respiratory conditions.
- **Spirometry Values (FEV1, FVC)**: Measures of lung function, where lower values indicate airflow limitation.
- **Engineered Features**: Includes rolling averages, lagged values, and interaction terms for temporal patterns.
- **Comorbidities**: Presence of conditions like cardiovascular disease may influence exacerbation risk.
""")

st.markdown("## Key Insights")
st.write("""
Insights derived from the models and SHAP analysis include:

- **Age** and **Smoking History** are consistent predictors of exacerbation risk.
- **Spirometry Values** (FEV1, FVC) are strong indicators, with lower values linked to higher risk.
- **Comorbidities** add context for assessing risk in patients with complex health profiles.
""")

# Display sections based on sidebar selections
if view_logistic_regression:
    st.markdown("---")
    st.header("Logistic Regression Visualizations")
    st.write("Logistic Regression is applied to imputed and transformed datasets to predict binary outcomes (exacerbation vs. no exacerbation).")
    
    if display_all_data_types:
        for data_type, folder in DATA_TYPES.items():
            if data_type != "Raw Data":  # Only show for Imputed and Transformed Data
                lr_image_path = os.path.join(ASSETS_DIR, folder, f"LR_{folder.lower()}.png")
                load_image_with_download(lr_image_path, f"Logistic Regression for {data_type}")
    else:
        if data_type_choice != "Raw Data":  # Only show for Imputed and Transformed Data
            lr_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"LR_{data_type_folder.lower()}.png")
            load_image_with_download(lr_image_path, f"Logistic Regression for {data_type_choice}")

if view_xgboost:
    st.markdown("---")
    st.header("XGBoost Visualizations")
    st.write("XGBoost is applied across raw, imputed, and transformed datasets, capturing complex non-linear patterns in COPD data.")
    
    if display_all_data_types:
        for data_type, folder in DATA_TYPES.items():
            xgb_image_path = os.path.join(ASSETS_DIR, folder, f"XGB_{folder.lower()}.png")
            load_image_with_download(xgb_image_path, f"XGBoost for {data_type}")
    else:
        xgb_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"XGB_{data_type_folder.lower()}.png")
        load_image_with_download(xgb_image_path, f"XGBoost for {data_type_choice}")

if view_shap_analysis:
    st.markdown("---")
    st.header("SHAP Analysis for Feature Importance")
    st.write("SHAP analysis provides insights into the influence of each feature on model predictions.")
    
    if display_all_data_types:
        for data_type, folder in DATA_TYPES.items():
            if data_type != "Raw Data":  # Only show Logistic Regression SHAP for Imputed and Transformed Data
                st.subheader(f"SHAP Analysis for Logistic Regression on {data_type}")
                shap_lr_path = os.path.join(ASSETS_DIR, folder, f"SHAP_LR_{folder.lower()}.png")
                load_image_with_download(shap_lr_path, f"SHAP Feature Importance for Logistic Regression on {data_type}")
            
            st.subheader(f"SHAP Analysis for XGBoost on {data_type}")
            shap_xgb_path = os.path.join(ASSETS_DIR, folder, f"SHAP_XGB_{folder.lower()}.png")
            load_image_with_download(shap_xgb_path, f"SHAP Feature Importance for XGBoost on {data_type}")
    else:
        if data_type_choice != "Raw Data":  # Only show Logistic Regression SHAP for Imputed and Transformed Data
            st.subheader(f"SHAP Analysis for Logistic Regression on {data_type_choice}")
            shap_lr_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_LR_{data_type_folder.lower()}.png")
            load_image_with_download(shap_lr_path, f"SHAP Feature Importance for Logistic Regression on {data_type_choice}")
        
        st.subheader(f"SHAP Analysis for XGBoost on {data_type_choice}")
        shap_xgb_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_XGB_{data_type_folder.lower()}.png")
        load_image_with_download(shap_xgb_path, f"SHAP Feature Importance for XGBoost on {data_type_choice}")

if view_comparative_insights:
    st.markdown("---")
    st.header("Comparative Visualizations")
    st.write("""
    Comparative insights highlight differences between Logistic Regression and XGBoost, as well as initial vs. final XGBoost models.
    """)
    with st.expander("Logistic Regression vs XGBoost Comparison", expanded=True):
        comparison_lr_xgb_path = os.path.join(ASSETS_DIR, "Comparisons", "LR_vs_XGB.png")
        load_image_with_download(comparison_lr_xgb_path, "Comparison of Logistic Regression and XGBoost")

    with st.expander("Initial vs Final XGBoost Comparison", expanded=True):
        comparison_xgb_final_path = os.path.join(ASSETS_DIR, "Comparisons", "XGB_initial_vs_final.png")
        load_image_with_download(comparison_xgb_final_path, "Comparison of Initial and Final XGBoost Models")

# Footer with information about the project
st.markdown("---")
st.markdown("**COPD Exacerbation Prediction Dashboard**")

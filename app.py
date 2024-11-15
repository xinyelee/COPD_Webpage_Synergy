import streamlit as st
from PIL import Image
import os
from datetime import datetime
from zipfile import ZipFile

# Define paths to image directories based on dataset type
ASSETS_DIR = "assets"
EDA_DIR = os.path.join(ASSETS_DIR, "EDA")  # Updated EDA directory path
DATA_TYPES = {
    "Raw Data": "Raw",
    "Imputed Data": "Imputed",
    "Imputed + Transformed Data": "Imputed_Transformed"
}

# Set page title and icon
st.set_page_config(page_title="COPD Data Dashboard", page_icon="📊", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "EDA Overview"])

# Fixed last updated date
last_updated_date = datetime(2024, 11, 14)
st.sidebar.info(f"Dashboard by SMU Team Synergy | Last updated: {last_updated_date.strftime('%d %b %Y')}")

# Helper function to load and display image, with error message if image is missing
def load_image(path, caption):
    if os.path.exists(path):
        img = Image.open(path)
        st.image(img, caption=caption)
    else:
        st.warning(f"{caption} image is not available. Please upload the necessary files to the assets folder.")

# Dashboard Page
if page == "Dashboard":
    st.title("📊 COPD Exacerbation Prediction Dashboard")
    st.write("""
    This dashboard provides insights into model performance on COPD datasets using Logistic Regression and XGBoost models.
    It includes model-specific visualizations and SHAP analysis to understand feature importance.
    """)

    # Data type selection
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

    # Logistic Regression Visualizations
    if view_logistic_regression:
        st.markdown("---")
        st.header("Logistic Regression Visualizations")
        st.write("Logistic Regression is applied to imputed and transformed datasets to predict binary outcomes (exacerbation vs. no exacerbation).")
        
        if display_all_data_types:
            for data_type, folder in DATA_TYPES.items():
                if data_type != "Raw Data":  # Only show for Imputed and Transformed Data
                    lr_image_path = os.path.join(ASSETS_DIR, folder, f"LR_{folder.lower()}.png")
                    load_image(lr_image_path, f"Logistic Regression for {data_type}")
        else:
            if data_type_choice != "Raw Data":  # Only show for Imputed and Transformed Data
                lr_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"LR_{data_type_folder.lower()}.png")
                load_image(lr_image_path, f"Logistic Regression for {data_type_choice}")

    # XGBoost Visualizations
    if view_xgboost:
        st.markdown("---")
        st.header("XGBoost Visualizations")
        st.write("XGBoost is applied across raw, imputed, and transformed datasets, capturing complex non-linear patterns in COPD data.")
        
        if display_all_data_types:
            for data_type, folder in DATA_TYPES.items():
                xgb_image_path = os.path.join(ASSETS_DIR, folder, f"XGB_{folder.lower()}.png")
                load_image(xgb_image_path, f"XGBoost for {data_type}")
        else:
            xgb_image_path = os.path.join(ASSETS_DIR, data_type_folder, f"XGB_{data_type_folder.lower()}.png")
            load_image(xgb_image_path, f"XGBoost for {data_type_choice}")

    # SHAP Analysis
    if view_shap_analysis:
        st.markdown("---")
        st.header("SHAP Analysis for Feature Importance")
        st.write("SHAP analysis provides insights into the influence of each feature on model predictions.")
        
        if display_all_data_types:
            for data_type, folder in DATA_TYPES.items():
                if data_type != "Raw Data":  # Only show Logistic Regression SHAP for Imputed and Transformed Data
                    st.subheader(f"SHAP Analysis for Logistic Regression on {data_type}")
                    shap_lr_path = os.path.join(ASSETS_DIR, folder, f"SHAP_LR_{folder.lower()}.png")
                    load_image(shap_lr_path, f"SHAP Feature Importance for Logistic Regression on {data_type}")
                
                st.subheader(f"SHAP Analysis for XGBoost on {data_type}")
                shap_xgb_path = os.path.join(ASSETS_DIR, folder, f"SHAP_XGB_{folder.lower()}.png")
                load_image(shap_xgb_path, f"SHAP Feature Importance for XGBoost on {data_type}")
        else:
            if data_type_choice != "Raw Data":  # Only show Logistic Regression SHAP for Imputed and Transformed Data
                st.subheader(f"SHAP Analysis for Logistic Regression on {data_type_choice}")
                shap_lr_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_LR_{data_type_folder.lower()}.png")
                load_image(shap_lr_path, f"SHAP Feature Importance for Logistic Regression on {data_type_choice}")
            
            st.subheader(f"SHAP Analysis for XGBoost on {data_type_choice}")
            shap_xgb_path = os.path.join(ASSETS_DIR, data_type_folder, f"SHAP_XGB_{data_type_folder.lower()}.png")
            load_image(shap_xgb_path, f"SHAP Feature Importance for XGBoost on {data_type_choice}")

    # Comparative Insights
    if view_comparative_insights:
        st.markdown("---")
        st.header("Comparative Visualizations")
        st.write("""
        Comparative insights highlight differences between Logistic Regression and XGBoost, as well as initial vs. final XGBoost models.
        """)
        with st.expander("Logistic Regression vs XGBoost Comparison", expanded=True):
            comparison_lr_xgb_path = os.path.join(ASSETS_DIR, "Comparisons", "LR_vs_XGB.png")
            load_image(comparison_lr_xgb_path, "Comparison of Logistic Regression and XGBoost")

        with st.expander("Initial vs Final XGBoost Comparison", expanded=True):
            comparison_xgb_final_path = os.path.join(ASSETS_DIR, "Comparisons", "XGB_initial_vs_final.png")
            load_image(comparison_xgb_final_path, "Comparison of Initial and Final XGBoost Models")

# EDA Overview Page
elif page == "EDA Overview":
    st.title("Exploratory Data Analysis (EDA) Overview")

    # Display EDA images
    st.subheader("Correlation Matrix")
    display_image_path = os.path.join(EDA_DIR, "correlation_matrix.png")
    load_image(display_image_path, "Correlation Matrix of Key Variables")

    st.subheader("Histograms")
    histograms = {
        "Distribution of Visit Counts": "visit_counts_histogram.png",
        "Distribution of Max Eosinophil Count (2015)": "max_eos_count_2015_histogram.png",
        "Distribution of FEV1/FVC Ratio Mean": "fev1_fvc_ratio_mean_histogram.png",
        "Distribution of Days Since Last Exacerbation": "days_since_last_exacerbation_histogram.png",
        "Distribution of Annual Exacerbation Rate": "exacerbation_rate_histogram.png"
    }
    for caption, filename in histograms.items():
        display_image_path = os.path.join(EDA_DIR, filename)
        load_image(display_image_path, caption)

    st.subheader("Box Plots")
    box_plots = {
        "Distribution and Box Plot of Max PEFR Personal Best": "pefr_best_combined.png",
        "Distribution and Box Plot of Mean PEFR": "mean_pefr_combined.png",
        "Distribution and Box Plot of Number of Exacerbations (2019)": "no_exacerbations_2019_combined.png"
    }
    for caption, filename in box_plots.items():
        display_image_path = os.path.join(EDA_DIR, filename)
        load_image(display_image_path, caption)

    # Download button for all EDA images
    with ZipFile('EDA_images.zip', 'w') as zipf:
        for filename in os.listdir(EDA_DIR):
            zipf.write(os.path.join(EDA_DIR, filename), filename)

    with open("EDA_images.zip", "rb") as zip_file:
        st.download_button(
            label="Download All EDA Images",
            data=zip_file,
            file_name="EDA_images.zip",
            mime="application/zip"
        )

# Footer with information about the project
st.markdown("---")
st.markdown("**COPD Exacerbation Prediction Dashboard**")

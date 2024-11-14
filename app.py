import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import os

# Define paths to image directories
LR_PATH = "assets/1_LR"
XGB_PATH = "assets/2_XGB"
SHAP_PATH = "assets/3_SHAP"
COMPARISON_PATH = "assets/4_Comparisons"

st.title("COPD Exacerbation Prediction Dashboard")

st.write("""
This dashboard displays visual results from Logistic Regression and XGBoost models on COPD data, 
featuring comparisons of model performance across different data types, along with feature importance visualizations.
""")

# Sidebar Filters
st.sidebar.header("Filter Options")
data_type = st.sidebar.selectbox("Select Data Type", ["Raw Data", "Imputed Data", "Imputed + Transformed Data"])

# Section 1: Logistic Regression Visualizations
st.header("1. Logistic Regression Visualizations")
if data_type in ["Imputed Data", "Imputed + Transformed Data"]:
    st.subheader(f"Logistic Regression on {data_type}")
    lr_image_path = os.path.join(LR_PATH, f"{data_type.replace(' ', '_').lower()}.png")
    if os.path.exists(lr_image_path):
        img_lr = Image.open(lr_image_path)
        st.image(img_lr, caption=f"Logistic Regression results for {data_type}")
    else:
        st.write(f"Image for Logistic Regression on {data_type} not found.")

# Section 2: XGBoost Visualizations
st.header("2. XGBoost Visualizations")
st.subheader(f"XGBoost on {data_type}")
xgb_image_path = os.path.join(XGB_PATH, f"{data_type.replace(' ', '_').lower()}.png")
if os.path.exists(xgb_image_path):
    img_xgb = Image.open(xgb_image_path)
    st.image(img_xgb, caption=f"XGBoost results for {data_type}")
else:
    st.write(f"Image for XGBoost on {data_type} not found.")

# Section 3: SHAP Visualisations
st.header("3. SHAP Analysis")
st.subheader("Logistic Regression SHAP Analysis")
shap_lr_image_path = os.path.join(SHAP_PATH, "SHAP_LR.png")
if os.path.exists(shap_lr_image_path):
    img_shap_lr = Image.open(shap_lr_image_path)
    st.image(img_shap_lr, caption="SHAP Feature Importance for Logistic Regression")
else:
    st.write("SHAP image for Logistic Regression not found.")

st.subheader("XGBoost SHAP Analysis")
shap_xgb_image_path = os.path.join(SHAP_PATH, "SHAP_XGB.png")
if os.path.exists(shap_xgb_image_path):
    img_shap_xgb = Image.open(shap_xgb_image_path)
    st.image(img_shap_xgb, caption="SHAP Feature Importance for XGBoost")
else:
    st.write("SHAP image for XGBoost not found.")

# Section 4: Comparative Visualizations
st.header("4. Comparative Visualizations")
st.subheader("Logistic Regression vs XGBoost Comparison")
comparison_lr_xgb_path = os.path.join(COMPARISON_PATH, "LR_vs_XGB_initial.png")
if os.path.exists(comparison_lr_xgb_path):
    img_lr_vs_xgb = Image.open(comparison_lr_xgb_path)
    st.image(img_lr_vs_xgb, caption="Comparison of Logistic Regression and XGBoost")
else:
    st.write("Comparison image for Logistic Regression vs XGBoost not found.")

st.subheader("Initial vs Final XGBoost Comparison")
comparison_xgb_final_path = os.path.join(COMPARISON_PATH, "XGBoost_final_vs_initial.png")
if os.path.exists(comparison_xgb_final_path):
    img_xgb_final = Image.open(comparison_xgb_final_path)
    st.image(img_xgb_final, caption="Comparison of Initial and Final XGBoost Models")
else:
    st.write("Comparison image for Initial vs Final XGBoost not found.")
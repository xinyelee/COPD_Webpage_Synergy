#Streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Set the title of the webpage
st.title("SMU FYP Team Synergy COPD Dashboard")

st.write("""
This dashboard displays visual results from Logistic Regression and XGBoost models on COPD data, 
comparing model performance across data types, along with feature importance visualizations.
""")

# Sidebar Filters
st.sidebar.header("Filter Options")
data_type = st.sidebar.selectbox("Select Data Type", ["Raw Data", "Imputed Data", "Imputed + Transformed Data"])

# Displaying Images for Each Section
st.header("1. Logistic Regression Visualizations")
if data_type in ["Imputed Data", "Imputed + Transformed Data"]:
    st.subheader(f"Logistic Regression on {data_type}")
    #img_lr = Image.open(f"assets/LR_{data_type.replace(' ', '_').lower()}.png")
    #st.image(img_lr, caption=f"Logistic Regression results for {data_type}")

st.header("2. XGBoost Visualizations")
st.subheader(f"XGBoost on {data_type}")
#img_xgb = Image.open(f"assets/XGB_{data_type.replace(' ', '_').lower()}.png")
#st.image(img_xgb, caption=f"XGBoost results for {data_type}")

st.header("3. SHAP Visualisations")
st.subheader("Logistic Regression SHAP Analysis")
#img_shap_lr = Image.open("assets/SHAP_LR.png")
#st.image(img_shap_lr, caption="SHAP Feature Importance for Logistic Regression")

st.subheader("XGBoost SHAP Analysis")
#img_shap_xgb = Image.open("assets/SHAP_XGB.png")
#st.image(img_shap_xgb, caption="SHAP Feature Importance for XGBoost")

st.header("4. Comparative Visualizations")
st.subheader("Initial Logistic Regression vs XGBoost Comparison")
#img_lr_vs_xgb = Image.open("assets/LR_vs_XGB_initial.png")
#st.image(img_lr_vs_xgb, caption="Initial Comparison of Logistic Regression and XGBoost")

st.subheader("Initial vs Final XGBoost Comparison")
#img_xgb_final = Image.open("assets/XGBoost_final_vs_initial.png")
#st.image(img_xgb_final, caption="Comparison of Initial and Final XGBoost Models")

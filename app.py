import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="COPD Exacerbation Prediction",
    layout="wide",
)

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Overview"

# Sidebar Navigation
st.sidebar.title("COPD Dashboard")
st.sidebar.markdown("### Navigation")

# Navigation options
pages = {
    "Overview": "This section gives an overview of the COPD prediction project.",
    "Exploratory Data Analysis (EDA)": "Explores the dataset and key variables.",
    "First Iteration Results": "Highlights the results and insights from the first iteration.",
    "Final Methodology": "Details the final methodology and results."
}

# Use radio buttons to switch between pages
selected_page = st.sidebar.radio("Go to:", list(pages.keys()), index=list(pages.keys()).index(st.session_state.page))

# Save the selected page to session state
st.session_state.page = selected_page

# Add a footer or additional notes to the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("Last Updated: 17 Nov 2024")


# Display Selected Page
if st.session_state.page == "Overview":
    st.markdown("# Overview")
    st.markdown(pages["Overview"])
   
    st.markdown("## Details")
    st.markdown("""
    - **Datasets:** Raw, Imputed and Imputed + Transformed Data
    - **Imputation Techniques:** MICE Forest for missing value handling
    - **Validation of Imputation:** Use raw bias (RB) and coverage rate (CR) to validate imputation quality, ensuring low bias and appropriate confidence intervals
    - **Model:** Logistic Regression (LR) and XGBoost (XGB) with SHAP analysis
    - **Iterations:** First Iteration and Final Methodology
    """)

    st.markdown("### First Iteration")
    st.markdown("""
    - **Summary:** Identified the best data type (Raw Data with selected features), validated XGBoost’s performance over Logistic Regression, and refined features for predicting COPD exacerbations.
    - **Feature Selection:** Used SHAP values at the 50th percentile to identify a subset of important features from the imputed data.
    - **Conclusion:** XGBoost on Raw Data with selected features performed slightly better than other configurations.
    """)

    st.markdown("### Final Adjustments")
    st.markdown("""
    - Removed Columns:
        - **Age_bins:** Replaced with continuous "Age."
        - **Died:** Excluded as it’s not predictive of exacerbation events.
        - **Age at First Exacerbation:** Removed for lack of added interpretability.
    """)

    st.markdown("### Final Methodology")
    st.markdown("""
    - **Feature Selection Adjustments:**
        - Removed Age_bins, Died, and Age at First Exacerbation.
    - **Model Configurations:**
        - Logistic Regression: Evaluated on Imputed Data (Baseline and Fine-Tuned).
        - XGBoost: Evaluated on Imputed and Raw Data.
    - **Evaluation Metrics:**
        - Recall: Minimize false negatives.
        - Balanced Accuracy: Address class imbalance.
        - AUROC: Assess model discrimination.
    """)

    st.markdown("### Key Findings")
    st.markdown("""
    - **Prioritizing Recall and Balanced Accuracy:**
        - Top Performer: Logistic Regression on Imputed Data.
        - Second: XGBoost on Raw Data.
    - **Prioritizing AUROC:**
        - Top Performer: XGBoost on Raw Data.
        - Second: Logistic Regression on Imputed Data.
    - **Final Model Choice:** XGBoost (Fine-Tuned) on Raw Data for its strong performance across metrics.
    """)

    st.markdown("### SHAP Analysis")
    st.markdown("""
    - Used to identify impactful features using summary, cohort, bar, and dependence plots.
    - Tested interaction features and polynomial terms across XGBoost configurations.
    """)

    st.markdown("### Final Outcome")
    st.markdown("""
    - The refined feature set improved both XGBoost and Logistic Regression performance.
    - Validated the feature engineering approach for predicting exacerbation risks in COPD patients.
    """)

elif st.session_state.page == "Exploratory Data Analysis (EDA)":
    st.markdown("# Exploratory Data Analysis (EDA)")
    st.markdown(pages["Exploratory Data Analysis (EDA)"])

    # Correlation Matrix
    st.markdown("### Correlation Matrix")
    st.image("assets/1_EDA/correlation_matrix.png", caption="Correlation Matrix")
    st.markdown(
        "The correlation matrix provides insights into relationships between key features. "
        "Strong correlations (e.g., between exacerbation counts across years) can guide feature selection and modeling decisions."
    )

    # Days Since Last Exacerbation
    st.markdown("### Days Since Last Exacerbation")
    st.image("assets/1_EDA/days_since_last_exacerbation_histogram.png", caption="Days Since Last Exacerbation Distribution")
    st.markdown(
        "The distribution of days since the last exacerbation is right-skewed, indicating that many patients recently experienced exacerbations, "
        "while others have been stable for longer periods."
    )

    # Exacerbation Rate
    st.markdown("### Exacerbation Rate")
    st.image("assets/1_EDA/exacerbation_rate_histogram.png", caption="Exacerbation Rate Distribution")
    st.markdown(
        "This chart highlights the distribution of annual exacerbation rates. Most patients have low rates, while a small proportion exhibits high exacerbation frequencies."
    )

    # FEV1/FVC Ratio Mean
    st.markdown("### FEV1/FVC Ratio Mean")
    st.image("assets/1_EDA/fev1_fvc_ratio_mean_histogram.png", caption="FEV1/FVC Ratio Mean Distribution")
    st.markdown(
        "The histogram illustrates the distribution of FEV1/FVC ratios. The data appears normally distributed, reflecting varying levels of airflow limitation among the patient population."
    )

    # Max Eosinophil Count (2015)
    st.markdown("### Max Eosinophil Count (2015)")
    st.image("assets/1_EDA/max_eos_count_2015_histogram.png", caption="Max Eosinophil Count in 2015 Distribution")
    st.markdown(
        "This chart presents the distribution of maximum eosinophil counts in 2015. "
        "The skewed data suggests most patients have low eosinophil counts, with a few having higher values, potentially indicating inflammation severity."
    )

    # Mean PEFR
    st.markdown("### Mean PEFR")
    st.image("assets/1_EDA/mean_pefr_combined.png", caption="Mean PEFR (Histogram and Boxplot)")
    st.markdown(
        "- **Histogram**: Shows the distribution of mean PEFR values, peaking at around 400-500.\n"
        "- **Boxplot**: Provides a concise summary of the data's central tendency and dispersion, with a few notable outliers."
    )

    # Number of Exacerbations in 2019
    st.markdown("### Number of Exacerbations in 2019")
    st.image("assets/1_EDA/no_exacerbations_2019_combined.png", caption="Number of Exacerbations in 2019 (Histogram and Boxplot)")
    st.markdown(
        "- **Histogram**: Displays the frequency of exacerbation counts in 2019. Most patients have a low number of exacerbations, "
        "with a few experiencing significantly more.\n"
        "- **Boxplot**: Summarizes the spread of exacerbation data, showing a high number of outliers."
    )

    # PEFR Best
    st.markdown("### PEFR Best")
    st.image("assets/1_EDA/pefr_best_combined.png", caption="PEFR Best (Histogram and Boxplot)")
    st.markdown(
        "- **Histogram**: Shows the distribution of PEFR (Peak Expiratory Flow Rate) Best values. "
        "Most values cluster around 300-400, with a few outliers on both ends.\n"
        "- **Boxplot**: Highlights the median PEFR Best value and the spread of the data, including outliers. "
        "Outliers likely represent exceptional cases or data entry errors."
    )

    # Visit Counts Distribution
    st.markdown("### Visit Counts Distribution")
    st.image("assets/1_EDA/visit_counts_histogram.png", caption="Visit Counts Distribution")
    st.markdown(
        "This histogram represents the distribution of visit counts among COPD patients. "
        "The right-skewed nature indicates most patients have few visits, with a small subset having significantly higher visit counts."
    )


elif st.session_state.page == "First Iteration Results":
    st.markdown("# First Iteration Results")
    st.markdown(pages["First Iteration Results"])
    
    # Folder: Logistic Regression (LR) Results
    st.markdown("## Logistic Regression (LR) Results")
    st.markdown("""
    **Question:** Does transforming the data improve performance?  
    **Answer:** Imputed data that hasn't been transformed performs better.  
    **Conclusion:** We will continue testing on raw and imputed data without transformations.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/2_First_Iteration/0./LR_non_transform.png", caption="Logistic Regression - Imputed Data")
    with col2:
        st.image("assets/2_First_Iteration/0./LR_transform.png", caption="Logistic Regression - Imputed + Transformed Data")

    # Folder: SHAP Plots from XGBoost Insights
    st.markdown("## XGBoost Insights")
    st.markdown("""
    Using the findings from the Logistic Regression analysis, where raw data performed better than imputed data, we utilized SHAP to filter out the top 50th percentile of important features. 
    These features were then fed into the XGBoost model, tested with different dataset types to understand performance differences.
    """)

    # Display XGBoost results side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/2_First_Iteration/1./xgb_imputed.png", caption="For Imputed Data")
    with col2:
        st.image("assets/2_First_Iteration/1./xgb_raw.png", caption="For Raw Data")
    with col3:
        st.image("assets/2_First_Iteration/1./xgb_transformed.png", caption="For Imputed + Transformed Data")

    st.markdown("""
    **Key Insights:**
    **Insights:**  
    - Raw data consistently outperformed imputed datasets.  
    - Imputed data might introduce biases, so we prioritized raw data for future analysis.
    The performance metrics validate our approach:  
    - **Raw Data:** Achieved a balanced accuracy of 0.7963 with significantly better recall and precision.  
    - **Imputed Data:** Showed lower accuracy and recall, further supporting the conclusion that raw data is more reliable.
    """)
   
    # Folder: Feature Importance
    st.markdown("## SHAP-Based Feature Insights")
    st.markdown("""
    These SHAP plots provide insights into feature contributions across various datasets and transformations.
    """)

    st.image("assets/2_First_Iteration/1./sp_raw.png", caption="SHAP Plot - Feature Contributions")
    st.markdown("""
    **Key Observation from SHAP Analysis:**  
    - "Age at First Exacerbation" was identified as the most important feature based on SHAP values.  
    - However, its SHAP value was much higher than all other features (close to 2), dominating the model.  
    - The model incorrectly interpreted this feature: higher age at first exacerbation reduced the risk of COPD exacerbations, which contradicts medical knowledge.  

    **Action Taken:**  
    - Removed "Age at First Exacerbation" due to its misleading influence on the model.  
    - Removed "Died" as it fed the model incorrect future information, not relevant for predicting exacerbations.  
    - Removed "Age_bins" as it was hard to interpret and lacked observable trends.  

    **Conclusion:**  
    Refining the feature set through SHAP analysis has helped ensure that the model aligns better with domain expertise and provides actionable insights.
    """)

    st.markdown("## Other Plots")
   # Blood Pressure (BP) SHAP Plots side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/2_First_Iteration/1./bp_imputed.png", caption="SHAP Plot - BP Feature (Imputed Data)")
    with col2:
        st.image("assets/2_First_Iteration/1./bp_raw.png", caption="SHAP Plot - BP Feature (Raw Data)")
    with col3:
        st.image("assets/2_First_Iteration/1./bp_transformed.png", caption="SHAP Plot - BP Feature (Transformed Data)")


    # Interaction Visualizations (IV)
    st.image("assets/2_First_Iteration/1./iv_raw.png", caption="SHAP Interaction Plot - Raw Data")


    # Spirometry (SP) SHAP Plots side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/2_First_Iteration/1./sp_imputed.png", caption="SHAP Plot - Spirometry Feature (Imputed Data)")
    with col2:
        st.image("assets/2_First_Iteration/1./sp_raw.png", caption="SHAP Plot - Spirometry Feature (Raw Data)")
    with col3:
        st.image("assets/2_First_Iteration/1./sp_transformed.png", caption="SHAP Plot - Spirometry Feature (Transformed Data)")
    
    
elif st.session_state.page == "Final Methodology":
    st.markdown("# Final Methodology")
    st.markdown(pages["Final Methodology"])
  

# Add a footer to the main page
st.markdown("---")
st.markdown("**Developed by SMU Team Synergy**")

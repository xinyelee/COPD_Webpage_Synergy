import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="COPD Exacerbation Prediction",
    layout="wide",
)

# Sidebar Navigation
st.sidebar.title("COPD Prediction Dashboard")

# Create sections with a header for better organization
st.sidebar.header("Sections")
pages = [
    "Overview",
    "Exploratory Data Analysis (EDA)",
    "First Iteration Results",
    "Final Methodology"
]
selected_page = st.sidebar.radio("Select a section:", pages)

# Add a footer or additional notes to the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("Last Updated: 16 Nov 2024")


# Display Selected Page
if selected_page == "Overview":
    st.markdown("# COPD Exacerbation Prediction")
    st.markdown("This dashboard provides insights into predicting COPD exacerbations using Logistic Regression and XGBoost.")

    st.markdown("## Details")
    st.markdown("""
    - **Datasets:** Raw, Imputed and Imputed + Transformed Data
    - **Imputation Techniques:** MICE (Multiple Imputation by Chained Equations) and missForest for missing value handling
    - **Validation of Imputation:** Use raw bias (RB) and coverage rate (CR) to validate imputation quality, ensuring low bias and appropriate confidence intervals
    - **Model:** Logistic Regression (LR) and XGBoost (XGB) with SHAP analysis
    - **Iterations:** First Iteration and Final Methodology
    """)

    st.markdown("### First Iteration")
    st.markdown("""
    - **Summary:** Identified the best data type (Raw Data with selected features), validated XGBoost’s performance over Logistic Regression, and refined features for predicting COPD exacerbations.
    - **Imputed Data:**
        - AUC: 0.825
        - Balanced Accuracy: 0.613
        - Recall: 0.613
        - Precision: 0.285
    - **Imputed + Transformed Data:**
        - AUC: 0.770
        - Balanced Accuracy: 0.555
        - Recall: 0.555
        - Precision: 0.208
    - **Feature Selection:** Used SHAP values at the 50th percentile to identify a subset of important features from the imputed data.
    - **XGBoost Results (Selected Features):**
        - ROC AUC: 0.772
        - Balanced Accuracy: 0.509
        - Precision: 0.1
        - Recall: 0.0178
        - Average Precision: 0.263
        - Specificity: 0.999
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

elif selected_page == "Exploratory Data Analysis (EDA)":
    st.markdown("# Exploratory Data Analysis (EDA)")
    st.markdown("Explore data distribution, missing values, and relationships between variables.")

    # Display each graph with captions
    st.markdown("#### Correlation Matrix")
    st.image("assets/1_EDA/correlation_matrix.png", caption="Correlation Matrix")

    st.markdown("#### Days Since Last Exacerbation Histogram")
    st.image(
        "assets/1_EDA/days_since_last_exacerbation_histogram.png",
        caption="Days Since Last Exacerbation Distribution",
    )

    st.markdown("#### Exacerbation Rate Histogram")
    st.image(
        "assets/1_EDA/exacerbation_rate_histogram.png",
        caption="Exacerbation Rate Distribution",
    )

    st.markdown("#### FEV1/FVC Ratio Mean Histogram")
    st.image(
        "assets/1_EDA/fev1_fvc_ratio_mean_histogram.png",
        caption="FEV1/FVC Ratio Mean Distribution",
    )

    st.markdown("#### Max Eosinophil Count (2015) Histogram")
    st.image(
        "assets/1_EDA/max_eos_count_2015_histogram.png",
        caption="Max Eosinophil Count in 2015 Distribution",
    )

    st.markdown("#### Mean PEFR Combined")
    st.image("assets/1_EDA/mean_pefr_combined.png", caption="Mean PEFR Combined")

    st.markdown("#### No Exacerbations (2019) Combined")
    st.image(
        "assets/1_EDA/no_exacerbations_2019_combined.png",
        caption="No Exacerbations in 2019 Combined",
    )

    st.markdown("#### PEFR Best Combined")
    st.image("assets/1_EDA/pefr_best_combined.png", caption="PEFR Best Combined")

    st.markdown("#### Visit Counts Histogram")
    st.image(
        "assets/1_EDA/visit_counts_histogram.png", caption="Visit Counts Distribution"
    )


elif selected_page == "First Iteration Results":
    st.markdown("# First Iteration")
    st.markdown("This section focuses on the all the plots/charts generated from first iteration.")

    # Section: Logistic Regression (LR) Results
    st.markdown("## Logistic Regression (LR) Results")
    st.image("assets/2_First_Iteration/LR_impute.png", caption="Logistic Regression - Imputed Data")
    st.image("assets/2_First_Iteration/LR_impute_transformed.png", caption="Logistic Regression - Transformed Data")
    st.image("assets/2_First_Iteration/LR_impute_XGB_raw_iter1_comparison.png", caption="Comparison: Logistic Regression vs. XGBoost on Raw Data")

    # Section: SHAP Contributions for LR
    st.markdown("## SHAP Contributions for Logistic Regression")
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Chronic_Kidney_Disease.png", caption="SHAP Contribution: Chronic Kidney Disease")
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Gender_MALE.png", caption="SHAP Contribution: Gender (Male)")
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Hypertension.png", caption="SHAP Contribution: Hypertension")
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Ischemic_Heart_Disease.png", caption="SHAP Contribution: Ischemic Heart Disease")
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Pneumonia.png", caption="SHAP Contribution: Pneumonia")

    # Section: XGBoost Results
    st.markdown("## XGBoost Results")
    st.image("assets/2_First_Iteration/xgb_imputed_data_iter1_bp.png", caption="XGBoost: Imputed Data BP Analysis")

    # Subsection: SHAP Contributions for XGBoost
    st.markdown("### SHAP Contributions for XGBoost")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_age_days_since_last_exac.png", caption="SHAP Contribution: Age and Days Since Last Exacerbation")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_normal.png", caption="SHAP Contribution: BMI (Normal)")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_obese.png", caption="SHAP Contribution: BMI (Obese)")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_overweight.png", caption="SHAP Contribution: BMI (Overweight)")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_underweight.png", caption="SHAP Contribution: BMI (Underweight)")

    # Subsection: Feature-Specific Analyses
    st.markdown("### Feature-Specific Analyses")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_count_2015.png", caption="COPD Duration and Exacerbation Count (2015)")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_count_2018_2019.png", caption="COPD Duration and Exacerbation Count (2018-2019)")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_count_2022.png", caption="COPD Duration and Exacerbation Count (2022)")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_rate.png", caption="COPD Duration and Exacerbation Rate")

    # Subsection: Other Key Features
    st.markdown("### Other Key Features")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_hypertension.png", caption="Hypertension")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_pneumonia.png", caption="Pneumonia")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_unstable_angina.png", caption="Unstable Angina")
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_visit_counts_pneumonia.png", caption="Visit Counts and Pneumonia")

elif selected_page == "Final Methodology":
    st.markdown("# Final Methodology")
    st.markdown("This section presents the final evaluation of models, including SHAP force plots, model comparisons, and feature importance analyses.")

    # Section: SHAP Force Plots
    st.markdown("## SHAP Force Plots")
    st.markdown("Force plots provide detailed insights into individual predictions made by the models.")
    # Display SHAP force plots for Logistic Regression
    st.markdown("### Logistic Regression Force Plot")
    st.components.v1.html(open("assets/3_Final_Method/html/force_plot_LR.html").read(), height=500)

    # Display SHAP force plots for XGBoost
    st.markdown("### XGBoost Force Plot")
    st.components.v1.html(open("assets/3_Final_Method/html/force_plot_xgb.html").read(), height=500)

    # Section: SHAP Analysis
    st.markdown("## SHAP Analysis")
    st.markdown("SHAP summary and interaction plots showing feature importance and contributions for predictions.")
    st.image("assets/3_Final_Method/LR_SHAP_analysis.png", caption="Logistic Regression SHAP Analysis")
    st.image("assets/3_Final_Method/XGB_SHAP_analysis.png", caption="XGBoost SHAP Analysis")

    # Section: Model Comparisons
    st.markdown("## Model Comparisons")
    st.markdown("Comparison of model performances across different configurations and datasets.")
    st.image("assets/3_Final_Method/LR_XGB_compare_imputed_iter1_no_age_bins_brief.png", caption="Logistic Regression vs XGBoost: Imputed Data (Brief)")
    st.image("assets/3_Final_Method/LR_XGB_compare_imputed_iter1_no_age_bins.png", caption="Logistic Regression vs XGBoost: Imputed Data (Detailed)")
    st.image("assets/3_Final_Method/XGB_raw_XGB_imputed_LR_imputed_compare_iter1_no_age_bins.png", caption="Raw vs Imputed Data: XGBoost and Logistic Regression")

    # Section: Final Model Evaluation
    st.markdown("## Final Model Evaluation")
    st.markdown("Evaluation of the final XGBoost model with interaction features.")
    st.image("assets/3_Final_Method/bestmodel_eval_xgb_3_IF_Test.png", caption="XGBoost Final Model Evaluation with Interaction Features")


# Add a footer to the main page
st.markdown("---")
st.markdown("**Developed by SMU Team Synergy**")

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
selected_page = st.sidebar.radio("Go to:", pages)

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



elif selected_page == "First Iteration Results":
    st.markdown("# First Iteration")
    st.markdown("This section focuses on the all the plots/charts generated from first iteration.")

   # Section: Logistic Regression (LR) Results
    st.markdown("## Logistic Regression (LR) Results")

    # Logistic Regression - Transformed Data
    st.image("assets/2_First_Iteration/LR_transform.png", caption="Logistic Regression - Transformed Data")
    st.markdown(
        "This graph represents the performance of Logistic Regression on imputed and transformed data. "
        "The model achieved an **AUC score of 0.77**, with high accuracy at **92%**. "
        "However, the recall for class 1 (exacerbation cases) is low at **0.25**, indicating challenges in identifying positive cases. "
        "The precision and f1-score for class 1 further reflect the difficulty of predicting minority class outcomes, "
        "despite adjustments for class imbalance. "
        "These results suggest the need for further feature engineering or advanced techniques to better capture exacerbation events."
    )

    
    # Section: SHAP Contributions for Logistic Regression
    st.markdown("## SHAP Contributions for Logistic Regression")
    # Pneumonia
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Pneumonia.png", caption="SHAP Contribution: Pneumonia")
    st.markdown(
        "Pneumonia is identified as a significant factor influencing the Logistic Regression model's predictions. "
        "Its SHAP value highlights its direct impact on increasing the risk of COPD exacerbations."
    )

    # Ischemic Heart Disease
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Ischemic_Heart_Disease.png", caption="SHAP Contribution: Ischemic Heart Disease")
    st.markdown(
        "Ischemic Heart Disease contributes moderately to the Logistic Regression model's predictions. "
        "This reflects its role as a secondary risk factor influencing COPD exacerbation outcomes."
    )

    # Hypertension
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Hypertension.png", caption="SHAP Contribution: Hypertension")
    st.markdown(
        "Hypertension is highlighted as an important predictor of COPD exacerbations. Its SHAP value underscores its contribution "
        "to the model, particularly in cases where hypertension co-occurs with other risk factors."
    )

    # Gender (Male)
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Gender_MALE.png", caption="SHAP Contribution: Gender (Male)")
    st.markdown(
        "The male gender is shown to have a moderate impact on exacerbation risk predictions. SHAP analysis reveals "
        "its influence is less pronounced compared to other clinical factors but still noteworthy."
    )

    # Chronic Kidney Disease
    st.image("assets/2_First_Iteration/LR_iter1_SHAP_Contribution_Chronic_Kidney_Disease.png", caption="SHAP Contribution: Chronic Kidney Disease")
    st.markdown(
        "Chronic Kidney Disease emerges as one of the top predictors in Logistic Regression. Its SHAP value "
        "demonstrates a strong association with increased exacerbation risk, likely due to its impact on overall patient health."
    )

    # Section: XGBoost Results
    st.markdown("## XGBoost Results")
    st.markdown("This section highlights the XGBoost results, SHAP contributions, and dependence plots for key predictors.")

    # SHAP Contributions for XGBoost
    st.markdown("## SHAP Contributions for XGBoost")

    # Pneumonia
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_pneumonia.png", caption="SHAP Contribution: Pneumonia")
    st.markdown(
        "Pneumonia is one of the most significant predictors in XGBoost, contributing to a higher risk of COPD exacerbations. "
        "Patients with pneumonia consistently show higher SHAP values."
    )

    # Unstable Angina
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_unstable_angina.png", caption="SHAP Contribution: Unstable Angina")
    st.markdown(
        "Unstable angina has a moderate influence on the predictions. Patients with this condition are at a higher risk of exacerbation."
    )

    # Hypertension
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_hypertension.png", caption="SHAP Contribution: Hypertension")
    st.markdown(
        "Hypertension is an important predictor of exacerbation risk. This SHAP plot shows its impact on the model, especially in patients with additional comorbidities."
    )

    # Cerebral Infarction
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_cerebral_infarction.png", caption="SHAP Contribution: Cerebral Infarction")
    st.markdown(
        "Cerebral infarction plays a notable role in predictions. Patients with this condition demonstrate higher SHAP values, indicating an elevated risk."
    )

    # SHAP Dependence and Interaction Plots
    st.markdown("### SHAP Dependence and Interaction Plots")

    # Pneumonia and Visit Counts
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_visit_counts_pneumonia.png", caption="SHAP Dependence Plot: Pneumonia and Visit Counts")
    st.markdown(
        "This dependence plot highlights how pneumonia and visit counts interact in the model. "
        "Patients with pneumonia and frequent visits tend to have higher SHAP values."
    )

    # Age and Days Since Last Exacerbation
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_age_days_since_last_exac.png", caption="SHAP Dependence Plot: Age and Days Since Last Exacerbation")
    st.markdown(
        "Age and days since the last exacerbation show a complex interaction. Older patients tend to have lower SHAP values, "
        "indicating reduced exacerbation risk."
    )

    # Section: SHAP Dependence for Eosinophil Counts
    st.markdown("### SHAP Dependence for Eosinophil Counts")
    
    # Max Eosinophil Count 2015 and 2016
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_max_eos_count_2015_2016.png", caption="SHAP Dependence: Max Eosinophil Count (2015 and 2016)")
    st.markdown(
        "These dependence plots show how eosinophil counts in 2015 and 2016 contribute to exacerbation risk. "
        "Higher eosinophil counts are associated with increased SHAP values, indicating higher risk."
    )

    # Max Eosinophil Count 2017 and 2018
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_max_eos_count_2017_2018.png", caption="SHAP Dependence: Max Eosinophil Count (2017 and 2018)")
    st.markdown(
        "Eosinophil counts in 2017 and 2018 show a consistent trend with exacerbation risk. SHAP values suggest "
        "a positive correlation between higher eosinophil counts and exacerbations."
    )

    # Max Eosinophil Count 2019 and 2020
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_max_eos_count_2019_2020.png", caption="SHAP Dependence: Max Eosinophil Count (2019 and 2020)")
    st.markdown(
        "For more recent years, eosinophil counts continue to play a significant role. SHAP values remain consistent "
        "with prior years, highlighting the importance of this feature in predictions."
    )

    # Section: SHAP Dependence for Exacerbations
    st.markdown("### SHAP Dependence for Exacerbations")
    
    # No. of Exacerbations 2015
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_no_of_exac_2017_pneumonia.png", caption="SHAP Dependence: No. of Exacerbations (2015)")
    st.markdown(
        "This plot examines the relationship between exacerbations in 2015 and risk. Higher SHAP values indicate "
        "a strong association with COPD exacerbation predictions, especially in patients with pneumonia."
    )

    # Section: COPD Duration and Exacerbation Trends
    st.markdown("### SHAP Dependence: COPD Duration and Exacerbation Trends")

    # COPD Duration and Exacerbation Count (2015)
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_count_2015.png", caption="SHAP Dependence: COPD Duration and Exacerbation Count (2015)")
    st.markdown(
        "COPD duration and exacerbation counts for 2015 show a strong relationship. Prolonged COPD duration often correlates with higher exacerbation risk."
    )

    # COPD Duration and Exacerbation Count (2018-2019)
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_count_2018_2019.png", caption="SHAP Dependence: COPD Duration and Exacerbation Count (2018-2019)")
    st.markdown(
        "The exacerbation patterns observed in 2018-2019 continue to reflect the impact of COPD duration on exacerbation risk. "
        "This emphasizes the cumulative nature of COPD's progression."
    )

    # COPD Duration and Exacerbation Count (2022)
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_count_2022.png", caption="SHAP Dependence: COPD Duration and Exacerbation Count (2022)")
    st.markdown(
        "In 2022, similar trends persist. Longer COPD durations are associated with increased SHAP values, reflecting their influence on exacerbation predictions."
    )

    # COPD Duration and Exacerbation Rate
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_exac_rate.png", caption="SHAP Dependence: COPD Duration and Exacerbation Rate")
    st.markdown(
        "Exacerbation rates show a clear dependence on COPD duration. Higher rates align with increased SHAP values, emphasizing their predictive importance."
    )

    # COPD Duration and Pneumonia
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_copd_duration_pneumonia.png", caption="SHAP Dependence: COPD Duration and Pneumonia")
    st.markdown(
        "The interaction between COPD duration and pneumonia further highlights the complexity of exacerbation predictions. "
        "Patients with pneumonia often show elevated SHAP values, especially with longer COPD durations."
    )

    # BMI-Specific SHAP Contributions
    st.markdown("### SHAP Contributions for BMI Categories")

    # BMI - Normal
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_normal.png", caption="SHAP Summary Plot: BMI (Normal)")
    st.markdown(
        "Patients with normal BMI show moderate SHAP values for predictors like COPD Duration and Annual Exacerbation Rate. "
        "This group represents the baseline risk level."
    )

    # BMI - Obese
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_obese.png", caption="SHAP Summary Plot: BMI (Obese)")
    st.markdown(
        "Obesity is associated with higher SHAP values across key predictors. This group exhibits elevated exacerbation risks."
    )

    # BMI - Overweight
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_overweight.png", caption="SHAP Summary Plot: BMI (Overweight)")
    st.markdown(
        "The overweight BMI group shows consistent feature importance, with SHAP values highlighting COPD Duration and Pneumonia as key factors."
    )

    # BMI - Underweight
    st.image("assets/2_First_Iteration/xgb_raw_data_iter1_bmi_underweight.png", caption="SHAP Summary Plot: BMI (Underweight)")
    st.markdown(
        "Underweight patients show lower SHAP values compared to other BMI categories. However, COPD Duration and Annual Exacerbation Rate remain significant predictors."
    )

elif selected_page == "Final Methodology":
    st.markdown("# Final Methodology")
    st.markdown("This section presents the final methodology and results, highlighting the most impactful features and model performances.")

    # Section: Logistic Regression SHAP Analysis
    st.markdown("## Logistic Regression SHAP Analysis")
    st.image("assets/3_Final_Method/LR_SHAP_analysis.png", caption="SHAP Analysis for Logistic Regression")
    st.markdown(
        "This SHAP analysis identifies key features influencing Logistic Regression predictions. "
        "**Number of Comorbidities**, **COPD Duration**, and **Pneumonia** are the most significant predictors of exacerbation risk."
    )

    # Section: Model Comparison - Logistic Regression vs XGBoost
    st.markdown("## Comparison of Logistic Regression and XGBoost Models")
    st.image("assets/3_Final_Method/LR_XGB_compare_imputed_iter1_no_age_bins_brief.png", caption="Model Comparison: LR and XGB on Imputed Data")
    st.markdown(
        "This comparison shows the performance metrics of Logistic Regression and XGBoost models on imputed data without age bins. "
        "Logistic Regression achieves an AUC of **0.765**, while XGBoost achieves an AUC of **0.738**, indicating slightly lower performance."
    )

    # Section: Extended Comparison
    st.image("assets/3_Final_Method/XGB_raw_XGB_imputed_LR_imputed_compare_iter1_no_age_bins.png", caption="Extended Model Comparison")
    st.markdown(
        "This graph compares Logistic Regression and XGBoost models trained on both raw and imputed datasets. "
        "The XGBoost model with raw data achieves the highest AUC of **0.791**, highlighting its superior predictive power."
    )

    # Section: XGBoost SHAP Analysis
    st.markdown("## XGBoost SHAP Analysis")
    st.image("assets/3_Final_Method/XGB_SHAP_analysis.png", caption="SHAP Analysis for XGBoost")
    st.markdown(
        "SHAP analysis for XGBoost highlights the most impactful features for predictions. "
        "**Annual Exacerbation Rate**, **COPD Duration**, and **Pneumonia** emerge as critical factors influencing model predictions."
    )

    # Section: Best Model Evaluation
    st.markdown("## Best Model Evaluation: XGBoost")
    st.image("assets/3_Final_Method/bestmodel_eval_xgb_3_IF_Test.png", caption="Evaluation of the Best XGBoost Model")
    st.markdown(
        "The best-performing model, XGBoost, demonstrates strong predictive performance with an AUC of **0.973**. "
        "Precision and specificity are also high, underscoring its robustness in distinguishing between exacerbation and non-exacerbation cases."
    )

    # Section: SHAP Force Plots
    st.markdown("## SHAP Force Plots")
    st.markdown("Force plots provide detailed insights into individual predictions made by the models.")

    # Display SHAP force plots for Logistic Regression
    st.markdown("### Logistic Regression Force Plot")
    st.components.v1.html(open("assets/3_Final_Method/html/force_plot_LR.html").read(), height=500)

    # Display SHAP force plots for XGBoost
    st.markdown("### XGBoost Force Plot")
    st.components.v1.html(open("assets/3_Final_Method/html/force_plot_xgb.html").read(), height=500)

# Add a footer to the main page
st.markdown("---")
st.markdown("**Developed by SMU Team Synergy**")

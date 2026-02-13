# Survival Analysis of Heart Failure Patients: A Frequentist and Bayesian Approach

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Lifelines](https://img.shields.io/badge/Library-Lifelines-lightgrey)
![PyMC](https://img.shields.io/badge/Library-PyMC-red)

## 📌 Project Overview
Heart failure is a complex clinical syndrome and a leading cause of mortality globally. This repository contains a comprehensive survival analysis of 299 heart failure patients, aimed at identifying the most critical clinical biomarkers that influence mortality risk. 

By bridging standard clinical statistics with advanced probabilistic programming, this project utilises a dual-modelling strategy:
1.  **Frequentist Inference:** Utilising Kaplan-Meier estimators and Cox Proportional Hazards to establish baseline Hazard Ratios (HR).
2.  **Bayesian Inference:** Implementing a Weibull Accelerated Failure Time (AFT) model via Markov Chain Monte Carlo (MCMC) sampling to quantify parameter uncertainty and generate posterior distributions.

## 🗄️ Dataset
The analysis uses the **Heart Failure Clinical Records Dataset** sourced from the UCI Machine Learning Repository (available in the `data/` directory). 
* **Source:** [UCI Machine Learning Repository: Heart Failure Clinical Records](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records)
* **Observations:** 299 patients (105 women, 194 men)
* **Features:** 13 clinical features including age, anaemia, ejection fraction, serum creatinine, and smoking status.
* **Target:** `time` (follow-up period in days) and `DEATH_EVENT` (boolean).

## 📊 Key Findings & Results
The model achieved a robust **Concordance Index (C-index) of 0.72**.

* **Renal Function is the Primary Risk Factor:** Serum Creatinine was identified as the strongest predictor of mortality ($HR = 1.43, p < 0.005$). 
* **Cardiac Function is Protective:** Higher Ejection Fraction significantly reduces mortality risk ($HR = 0.95, p < 0.005$).
* **Methodological Convergence:** Both Frequentist Maximum Likelihood Estimation and Bayesian MCMC sampling yielded highly consistent coefficients for Ejection Fraction ($\beta \approx -0.05$), confirming the robustness of the physiological effect.
* **Negative Findings:** Within this specific established heart failure cohort, smoking status did not show a statistically significant impact on short-term survival ($p = 0.75$).

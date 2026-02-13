import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter, CoxPHFitter
import pymc as pm
import arviz as az
import warnings

warnings.filterwarnings('ignore')

url = "https://raw.githubusercontent.com/arnavxox/Bayesian-Health-Analysis/main/heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(url)

# Kaplan-Meier Curve
kmf = KaplanMeierFitter()
kmf.fit(durations=df['time'], event_observed=df['DEATH_EVENT'])

plt.figure(figsize=(8, 5))
kmf.plot_survival_function(linewidth=2)
plt.title("Global Survival Function (Kaplan-Meier)")
plt.ylabel("Survival Probability")
plt.xlabel("Days")
plt.grid(True, alpha=0.3)
plt.show()

# Cox Proportional Hazards
features = ['time', 'DEATH_EVENT', 'age', 'ejection_fraction', 'serum_creatinine', 'sex', 'smoking']
df_cox = df[features]

cph = CoxPHFitter()
cph.fit(df_cox, duration_col='time', event_col='DEATH_EVENT')

plt.figure(figsize=(8, 5))
cph.plot()
plt.title("Hazard Ratios (Cox Proportional Hazards)")
plt.show()

# Bayesian Analysis Setup
df['age_std'] = (df['age'] - df['age'].mean()) / df['age'].std()
df['ef_std'] = (df['ejection_fraction'] - df['ejection_fraction'].mean()) / df['ejection_fraction'].std()

mask_dead = df['DEATH_EVENT'] == 1
time_obs = df.loc[mask_dead, 'time'].values
age_obs = df.loc[mask_dead, 'age_std'].values
ef_obs = df.loc[mask_dead, 'ef_std'].values

# MCMC Sampling
with pm.Model() as weibull_model:
    beta_age = pm.Normal('beta_age', mu=0, sigma=1)
    beta_ef = pm.Normal('beta_ef', mu=0, sigma=1)
    intercept = pm.Normal('intercept', mu=0, sigma=5)
    
    alpha = pm.Exponential('alpha', lam=1.0)
    mu = intercept + beta_age * age_obs + beta_ef * ef_obs
    
    y_obs = pm.Weibull('y_obs', alpha=alpha, beta=pm.math.exp(mu), observed=time_obs)
    idata = pm.sample(1000, tune=1000, return_inferencedata=True, chains=2, progressbar=False)

# Bayesian Visualisations
plt.figure(figsize=(8, 4))
az.plot_forest(idata, var_names=['beta_age', 'beta_ef'], combined=True)
plt.title("Bayesian Credible Intervals (Posterior)")
plt.axvline(0, color='red', linestyle='--')
plt.show()

az.plot_posterior(idata, var_names=['beta_ef'], ref_val=0)
plt.title("Posterior Distribution: Ejection Fraction")
plt.show()

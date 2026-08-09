import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the existing dataset created in Project 01
data = pd.read_csv("nitrogen_yield_data.csv")

# 2. Run One-Way ANOVA
groups = [group['Yield_t_ha'].values for name, group in data.groupby('Nitrogen_Rate')]
f_stat, p_val = stats.f_oneway(*groups)

print("--- ONE-WAY ANOVA RESULTS (PYTHON) ---")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_val:.4e}\n")

# 3. Run Tukey HSD Post-Hoc Test
tukey = pairwise_tukeyhsd(endog=data['Yield_t_ha'], groups=data['Nitrogen_Rate'], alpha=0.05)
print("--- TUKEY HSD POST-HOC TEST (PYTHON) ---")
print(tukey)

# 4. Create Visualization (Boxplot)
plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

sns.boxplot(x='Nitrogen_Rate', y='Yield_t_ha', data=data, palette="YlGnBu")
sns.stripplot(x='Nitrogen_Rate', y='Yield_t_ha', data=data, color='black', alpha=0.5, jitter=0.2)

plt.title("Maize Yield Response across Nitrogen Rates (Python Implementation)", fontsize=12, fontweight='bold')
plt.xlabel("Nitrogen Application Rate", fontsize=10)
plt.ylabel("Yield (tonnes/ha)", fontsize=10)

plt.tight_layout()
plt.savefig("nitrogen_yield_boxplot_python.png", dpi=300)
plt.show()

print("\nPython script executed successfully!")

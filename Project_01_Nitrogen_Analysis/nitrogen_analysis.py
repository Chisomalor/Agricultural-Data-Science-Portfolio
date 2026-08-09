import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the existing dataset created in Project 01
data = pd.read_csv("nitrogen_trial_data.csv")

# Clean column names (removes hidden spaces)
data.columns = data.columns.str.strip()

# Automatically detect the right column names
nitro_col = [c for c in data.columns if 'nitro' in c.lower() or 'rate' in c.lower() or 'treatment' in c.lower()][0]
yield_col = [c for c in data.columns if 'yield' in c.lower()][0]

# 2. Run One-Way ANOVA
groups = [group[yield_col].values for name, group in data.groupby(nitro_col)]
f_stat, p_val = stats.f_oneway(*groups)

print("--- ONE-WAY ANOVA RESULTS (PYTHON) ---")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_val:.4e}\n")

# 3. Run Tukey HSD Post-Hoc Test
tukey = pairwise_tukeyhsd(endog=data[yield_col], groups=data[nitro_col], alpha=0.05)
print("--- TUKEY HSD POST-HOC TEST (PYTHON) ---")
print(tukey)

# 4. Create visualization (Boxplot)
plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

sns.boxplot(x=nitro_col, y=yield_col, data=data, palette="YlGnBu")
sns.stripplot(x=nitro_col, y=yield_col, data=data, color='black', alpha=0.5, jitter=0.2)

plt.title("Maize Yield Response across Nitrogen Rates (Python Implementation)", fontsize=12, fontweight='bold')
plt.xlabel("Nitrogen Application Rate", fontsize=10)
plt.ylabel("Yield (tonnes/ha)", fontsize=10)

plt.tight_layout()
plt.savefig("nitrogen_yield_boxplot_python.png", dpi=300)
plt.show()

print("\nPython script executed successfully!")




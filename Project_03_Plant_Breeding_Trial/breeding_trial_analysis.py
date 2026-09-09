import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset (already generated and saved as CSV)
data = pd.read_csv("breeding_trial_data.csv")

# Clean column names (removes hidden spaces from copy-paste)
data.columns = data.columns.str.strip()

variety_col = "Variety"
yield_col = "Yield_tha"
block_col = "Block"

# 2. Summary Statistics per Variety
summary_stats = (
    data.groupby(variety_col)[yield_col]
    .agg(["mean", "std", "count"])
    .sort_values("mean", ascending=False)
)
print("--- SUMMARY STATISTICS (PYTHON) ---")
print(summary_stats)

# 3. Run One-Way ANOVA on Variety
# (Note: a full two-way RCBD ANOVA needs statsmodels' OLS + anova_lm;
#  shown here for environments where statsmodels formula API is available)
groups = [group[yield_col].values for name, group in data.groupby(variety_col)]
f_stat, p_val = stats.f_oneway(*groups)

print("\n--- ONE-WAY ANOVA RESULTS (PYTHON) ---")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_val:.4e}\n")

# Optional: full RCBD two-way ANOVA (Variety + Block) if statsmodels is available
try:
    from statsmodels.formula.api import ols
    from statsmodels.stats.anova import anova_lm

    model = ols(f"{yield_col} ~ C({variety_col}) + C({block_col})", data=data).fit()
    anova_table = anova_lm(model, typ=2)
    print("--- TWO-WAY RCBD ANOVA TABLE (PYTHON) ---")
    print(anova_table)
except ImportError:
    print("statsmodels formula API not available; ran one-way ANOVA only.")

# 4. Run Tukey HSD Post-Hoc Test
tukey = pairwise_tukeyhsd(endog=data[yield_col], groups=data[variety_col], alpha=0.05)
print("\n--- TUKEY HSD POST-HOC TEST (PYTHON) ---")
print(tukey)

# 5. Create visualization (ranked bar chart with error bars)
plot_data = (
    data.groupby(variety_col)[yield_col]
    .agg(["mean", "sem"])
    .sort_values("mean", ascending=False)
    .reset_index()
)

plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

sns.barplot(x=variety_col, y="mean", data=plot_data, order=plot_data[variety_col],
            palette="YlGn", errorbar=None)
plt.errorbar(x=range(len(plot_data)), y=plot_data["mean"], yerr=plot_data["sem"],
             fmt="none", c="black", capsize=4)

plt.title("Grain Yield by Variety in RCBD Trial (Python Implementation)", fontsize=12)
plt.xlabel("Variety", fontsize=10)
plt.ylabel("Mean Yield (t/ha)", fontsize=10)

plt.tight_layout()
plt.savefig("breeding_variety_barplot_python.png", dpi=300)
plt.show()

print("\nPython script executed successfully!")

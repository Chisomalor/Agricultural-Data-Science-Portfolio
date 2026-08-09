"""
Project 02: Soil Health & Nutrient Modeling for Crop Yield
Author: Alor Chisom Lydia
Description: Multiple linear regression and correlation analysis evaluating
the relationship between soil health indicators (pH, Organic Matter,
Available Nitrogen, Phosphorus) and crop yield.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 1. Load Dataset (Assuming soil_health_data.csv is in the project folder)
# If your filename differs, update it here:
df = pd.read_csv("soil_health_data.csv")

print("--- Dataset Preview ---")
print(df.head())

# 2. Descriptive Statistics & Correlation Matrix
print("\n--- Summary Statistics ---")
print(df.describe())

correlation_matrix = df.corr(numeric_only=True)
print("\n--- Correlation Matrix ---")
print(correlation_matrix)

# 3. Fit Multiple Linear Regression Model
# Using exact CSV column names: Yield_t_ha, Soil_pH, SOC_percent, Nitrogen_ppm, Phosphorus_ppm
model = smf.ols(
"Yield_t_ha ~ Soil_pH + SOC_percent + Nitrogen_ppm + Phosphorus_ppm",
data=df,
).fit()

print("\n--- Regression Model Summary ---")
print(model.summary())

# 4. Generate Publication-Ready Pairplot / Correlation Heatmap
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 8))

# Pairplot for visualizing relationships
pair_plot = sns.pairplot(
df,
diag_kind="kde",
plot_kws={"alpha": 0.6, "color": "seagreen"},
diag_kws={"color": "seagreen", "fill": True},
)
pair_plot.fig.suptitle(
"Soil Health Indicators vs. Crop Yield - Regression Relationships", y=1.03
)

# Save visualization
output_filename = "soil_health_correlation_python.png"
plt.savefig(output_filename, dpi=300, bbox_inches="tight")
print(f"\nVisualization successfully saved as '{output_filename}'")

plt.show()


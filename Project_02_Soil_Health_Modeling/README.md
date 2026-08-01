# Project 02: Soil Health Dynamics & Crop Yield Prediction

## 📌 Project Overview
This project investigates the multi-factorial relationships between soil chemical/biological properties—**Soil Organic Carbon (SOC)**, **Nitrogen (N)**, **Phosphorus (P)**, and **pH**—and crop grain yield. Using **Multiple Linear Regression** and **Correlation Analysis**, we model yield drivers to provide data-driven agronomic recommendations.

## 🔬 Dataset Overview
* **Sample Size:** 60 geo-referenced field samples ($N = 60$)
* **Variables Evaluated:**
* `Soil_pH`: Soil reaction (5.5 - 7.5 scale)
* `SOC_percent`: Soil Organic Carbon (%)
* `Nitrogen_ppm`: Available Nitrogen (ppm)
* `Phosphorus_ppm`: Available Phosphorus (ppm)
* `Yield_t_ha`: Crop Grain Yield (t/ha)

---

## 📊 Correlation Matrix Analysis

![Soil Health Correlation Matrix](soil_correlation_matrix.png)

### Key Insights from Heatmap:
* **Soil Organic Carbon (SOC):** Exhibited the strongest positive correlation with yield ($r \approx 0.78$), highlighting the central role of soil organic matter in nutrient retention and crop productivity.
* **Nitrogen & Phosphorus:** Strong positive correlations with yield ($r \approx 0.65$ and $r \approx 0.55$, respectively).

---

## 📈 Multiple Linear Regression Model Results

$$Yield = \beta_0 + \beta_1(SOC) + \beta_2(N) + \beta_3(P) + \beta_4(pH) + \epsilon$$

| Predictor Variable | Coefficient ($\beta$) | Std. Error | $p$-value | Significance |
| :--- | :--- | :--- | :--- | :--- |
| **(Intercept)** | 1.15 | 0.42 | 0.008 | ** |
| **SOC (%)** | 0.82 | 0.08 | < 0.001 | *** |
| **Nitrogen (ppm)** | 0.04 | 0.005 | < 0.001 | *** |
| **Phosphorus (ppm)**| 0.03 | 0.008 | < 0.001 | *** |
| **Soil pH** | 0.14 | 0.06 | 0.024 | * |

* **Model Performance:** Adjusted $R^2 = 0.84$ ($p < 0.001$).
* **Interpretation:** 84% of the variance in crop yield is explained by SOC, available N, P, and pH combined.

---

## 💡 Soil Management Takeaway
1. **Prioritize Organic Matter:** Increasing SOC by 1% yields an estimated yield boost of **~0.82 t/ha**, outperforming simple inorganic N/P additions alone.
2. **Balanced Balanced Nutrition:** Soil pH maintenance around neutral (6.5–7.0) optimizes nutrient availability.

---

## 🛠️ Repository & Tooling
* **Author:** Alor Chisom Lydia
* **Language/Environment:** R / RStudio (`ggplot2`, `dplyr`, `reshape2`)
* **Script:** `soil_health_analysis.R`

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset (already generated and saved as CSV)
data = pd.read_csv("snp_genotype_data.csv")
data.columns = data.columns.str.strip()

marker_cols = [c for c in data.columns if c.startswith("SNP_")]
X = data[marker_cols].values

# 2. Run PCA on the SNP marker matrix
pca = PCA(n_components=5)
pcs = pca.fit_transform(X)
var_explained = np.round(pca.explained_variance_ratio_ * 100, 1)

print("--- VARIANCE EXPLAINED BY TOP 5 PCs (%) (PYTHON) ---")
for i, v in enumerate(var_explained, start=1):
    print(f"PC{i}: {v}%")

# 3. Build a dataframe of PC scores for plotting
pca_scores = pd.DataFrame({
    "Individual_ID": data["Individual_ID"],
    "Population": data["Population"],
    "PC1": pcs[:, 0],
    "PC2": pcs[:, 1],
})

# 4. PCA Scatterplot (population structure)
plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")
sns.scatterplot(x="PC1", y="PC2", hue="Population", data=pca_scores,
                 palette="Set2", s=100, alpha=0.85)
plt.title("PCA of SNP Marker Data (Python Implementation)", fontsize=12)
plt.xlabel(f"PC1 ({var_explained[0]}% variance)", fontsize=10)
plt.ylabel(f"PC2 ({var_explained[1]}% variance)", fontsize=10)
plt.tight_layout()
plt.savefig("pca_population_structure_python.png", dpi=300)
plt.show()

# 5. Scree Plot
plt.figure(figsize=(7, 5))
sns.barplot(x=[f"PC{i}" for i in range(1, 6)], y=var_explained, color="forestgreen")
plt.title("Scree Plot: Variance Explained per Principal Component")
plt.xlabel("Principal Component")
plt.ylabel("% Variance Explained")
plt.tight_layout()
plt.savefig("scree_plot_python.png", dpi=300)
plt.show()

print("\nPython script executed successfully!")

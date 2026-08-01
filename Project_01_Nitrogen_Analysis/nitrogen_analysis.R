############################################################
# Project 01
#
# Title:
# Effect of Nitrogen Fertilizer on Maize Yield
#
# Research Question:
# Does increasing nitrogen fertilizer significantly
# improve maize yield?
#
# Author:
# Alor Chisom Lydia
#
############################################################

# Create Project directory if it doesn't exist
if (!dir.exists("Project_01_Nitrogen_Analysis")) {
  dir.create("Project_01_Nitrogen_Analysis")
}

# Set seed for reproducibility
set.seed(42)

# Simulate 10 replications per nitrogen treatment level (kg/ha)
n_reps <- 10
nitrogen_levels <- factor(c(rep("N0_Control", n_reps),
                            rep("N50_Low", n_reps),
                            rep("N100_Medium", n_reps),
                            rep("N150_High", n_reps)),
                          levels = c("N0_Control", "N50_Low", "N100_Medium", "N150_High"))

# Generate yields (tons per hectare) with realistic variation
yield_N0 <- rnorm(n_reps, mean = 2.5, sd = 0.35)
yield_N50 <- rnorm(n_reps, mean = 4.2, sd = 0.40)
yield_N100 <- rnorm(n_reps, mean = 6.8, sd = 0.45)
yield_N150 <- rnorm(n_reps, mean = 6.9, sd = 0.42) # Plateau effect

nitrogen_data <- data.frame(
  Plot_ID = 1:(n_reps * 4),
  Treatment = nitrogen_levels,
  Yield_t_ha = round(c(yield_N0, yield_N50, yield_N100, yield_N150), 2)
)

# Save to CSV inside Project 1 folder
write.csv(nitrogen_data, "Project_01_Nitrogen_Analysis/nitrogen_trial_data.csv", row.names = FALSE)
cat("Dataset successfully created and saved in Project_01_Nitrogen_Analysis/!\n")



# Install required packages if not already installed
packages <- c("ggplot2", "dplyr")
new_pkgs <- packages[!(packages %in% installed.packages()[,"Package"])]
if(length(new_pkgs)) install.packages(new_pkgs)

library(ggplot2)
library(dplyr)

# 1. Load Data
df <- read.csv("Project_01_Nitrogen_Analysis/nitrogen_trial_data.csv")
df$Treatment <- factor(df$Treatment, levels = c("N0_Control", "N50_Low", "N100_Medium", "N150_High"))

# 2. Summary Statistics
summary_stats <- df %>%
  group_by(Treatment) %>%
  summarise(
    Mean_Yield = mean(Yield_t_ha),
    SD = sd(Yield_t_ha),
    Count = n()
  )
print("--- SUMMARY STATISTICS ---")
print(summary_stats)

# 3. Fit One-Way ANOVA Model
anova_model <- aov(Yield_t_ha ~ Treatment, data = df)
print("--- ANOVA TABLE ---")
print(summary(anova_model))

# 4. Tukey HSD Post-Hoc Test
tukey_results <- TukeyHSD(anova_model)
print("--- TUKEY HSD TEST RESULTS ---")
print(tukey_results)

# 5. Create High-Quality Plot
p <- ggplot(df, aes(x = Treatment, y = Yield_t_ha, fill = Treatment)) +
  geom_boxplot(alpha = 0.7, outlier.shape = 16) +
  geom_jitter(width = 0.15, size = 2, alpha = 0.6) +
  scale_fill_brewer(palette = "YlGn") +
  labs(
    title = "Effect of Nitrogen Fertilizer Rates on Maize Grain Yield",
    subtitle = "One-Way ANOVA & Tukey HSD Analysis",
    x = "Nitrogen Treatment Rate (kg/ha)",
    y = "Maize Yield (t/ha)",
    caption = "Source: Simulated Field Trial Data | Agricultural Data Science Portfolio"
  ) +
  theme_minimal(base_size = 13) +
  theme(legend.position = "none", plot.title = element_text(face = "bold"))

# Save the plot
ggsave("Project_01_Nitrogen_Analysis/nitrogen_yield_boxplot.png", plot = p, width = 8, height = 5, dpi = 300)
cat("Plot saved as nitrogen_yield_boxplot.png!\n")





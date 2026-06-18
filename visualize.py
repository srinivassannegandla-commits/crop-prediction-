import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Crop_recommendation.csv")

# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(
    df.drop("label", axis=1).corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# Crop Distribution
plt.figure(figsize=(12,6))
sns.countplot(x="label", data=df)
plt.xticks(rotation=90)
plt.title("Crop Distribution")
plt.tight_layout()
plt.show()
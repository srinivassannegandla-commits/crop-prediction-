import pandas as pd

df = pd.read_csv("Crop_recommendation.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())
import pandas as pd
import numpy as np

df = pd.read_csv("../data/raw/dirty_cafe_sales.csv")
print("Shape of df: ", df.shape)
print("\nInfo of df: ")
print(df.info())

print("\nMissing values: ")
print(df.isnull().sum())

print("\nDuplicate: ")
print(df.duplicated().sum())

print("\nItem: ")
print(df['Item'].value_counts(normalize=True))

print("\nFirst 5 items: ")
print(df.head(5))
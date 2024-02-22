import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir("C:/Users/CSE-Lab1/Documents/aia")
filepath = "C:/Users/CSE-Lab1/Documents/aia/world_population_data.csv"
df_csv = pd.read_csv(filepath, low_memory=False)
df_csv.to_csv("file.csv", index=False)

print("column names:", df_csv.columns)
print("row names :")
for row in df_csv.index:
    print(row, end=" ")

# print("row names:", pd.io.parsers.read_csv(filepath, sep="\t", index_col=0))

print("\nData types:\n", df_csv.dtypes)

print("dimensions:", df_csv.shape)

feature_stats = df_csv["2022 population"].describe()
mean = feature_stats['mean']
Min = feature_stats['min']
Max = feature_stats['max']
std = feature_stats['std']
mode = df_csv["2022 population"].mode().iloc[0]

print('mean:', mean)
print('max:', Max)
print('min:', Min)
print('Std  deviation:', std)
print('mode :', mode)

freq = df_csv["2022 population"].value_counts()
missingvalues = df_csv["2015 population"].isnull().sum()

print("frequency distribution :\n", freq)
print("missing values in feature  :\n", missingvalues)

df_csv.drop_duplicates()
plt.style.use('ggplot')
df_csv['2022 population'].hist()

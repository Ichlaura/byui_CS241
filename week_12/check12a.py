import matplotlib
import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)

c_d = pd.read_csv("census.csv")

mean_ = f"Mean: {c_d.income.mean()}"
median_ = f"Median: {c_d.income.median()}"
max_ = f"Max: {c_d.income.max()}"

print(mean_)
print(median_)
print(max_)

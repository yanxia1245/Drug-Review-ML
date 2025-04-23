# import libraries
import pandas as pd
raw_data = pd.read_csv("datasets/drugsCom_raw.tsv", sep="\t")
raw_data.head()
raw_data.info()
missing_values = raw_data.isnull().sum()
print(missing_values)
print(raw_data.describe())
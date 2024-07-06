import pandas as pd
import numpy as np

#import, read file then print its content
print("FOR: GENGER SUMBISSION.CSV\n ")
fileI = 'gender_submission.csv'
data_frame = pd.read_csv(fileI)
print(data_frame.head())

#dropping rows wth missing values
print("Dropping rows with missing values")
print(data_frame.dropna())






print("\nFOR TEST.CSV\n")

fileII ='test.csv'
df2 = pd.read_csv(fileII)
print(df2.head)
print("Dropping rows with missing values")
print(df2.dropna())


import pandas as pd
import xlsxwriter
import os

# df1 = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", nrows=2, index_col=False, skipinitialspace=True, usecols=fields)
# print(df1)
# print("")
#
# df = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", skiprows=13, index_col=False, skipinitialspace=True,  usecols=fields)
# print(df)
#
# print("")
# df1.merge(df)
# print(df1)
# with open("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx", "w") as my_empty_csv:
#   # now you have an empty file already
#   pass


fields = [0,1]
df1 = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", nrows=2, index_col=False, skipinitialspace=True, usecols=fields)
print(df1)
print("")

df = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", skiprows=13, index_col=False, skipinitialspace=True,  usecols=fields)
print(df)

with open("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.csv", 'w') as f:
    pd.concat([df1, df, ], axis=1).to_csv('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.csv')
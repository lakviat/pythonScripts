import pandas as pd
import pyodbc

df = pd.read_excel('testing.xlsx')
df2 = pd.read_csv('testing.xlsx')

print(df)
print(df2)
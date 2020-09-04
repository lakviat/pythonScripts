import pandas as pd
import xlsxwriter
import os
import time
import openpyxl

fields = [0,1]
first_part = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", nrows=2, index_col=False, skipinitialspace=True, usecols=fields)
#print(first_part)
second_part = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", nrows=2, index_col=False, skipinitialspace=True,  usecols=fields)
#print(second_part)

third_part = pd.read_excel("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.xlsx", skiprows=5,  index_col=False, skipinitialspace=True,  usecols=fields)

writer = pd.ExcelWriter('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\SKIP.xlsx', engine='xlsxwriter')
third_part.to_excel(writer, sheet_name="TEST", index=False)
writer.save()

with pd.ExcelWriter("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\SKIP.xlsx", engine="openpyxl", mode="a") as writer:
    second_part.to_excel(writer, sheet_name="PROD")



# writer = pd.ExcelWriter('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx', engine='xlsxwriter')
# first_part.to_excel(writer, sheet_name='TEST', index=False)
#
# writer = pd.ExcelWriter('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\SKIP.xlsx', engine='xlsxwriter')
# third_part.to_excel(writer, sheet_name='TEST', index=False)
#
# for df in (third_part):
#     df.to_excel(writer, sheet_name="TEST", index=False)

# offset = len(first_part) + 1
# for df in (second_part, third_part):
#     df.to_excel(writer, sheet_name='TEST', startrow=offset,
#                 header=False, index=False)
#     offset += len(df)
# writer.save()

#df = pd.read_csv('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx', engine='xlsxwriter')
df = pd.read_excel('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx')
df2 = pd.read_excel('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx')



writer = pd.ExcelWriter('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='PROD', index=False)
df2.to_excel(writer, sheet_name='TEST', index=False)
writer.save()

wb = openpyxl.load_workbook('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx')
summary = wb.create_sheet(title="hello")
summary['A1'] = "columnm1"
wb.save('C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\MERGED.xlsx')

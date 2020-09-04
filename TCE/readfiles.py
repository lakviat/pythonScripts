import glob
import pandas as pd
for file in glob.glob("C:\\Users\\Lakvi\\OneDrive\\Рабочий стол\\Reports\\TCE\\mainsheet.dat"):
    df = pd.read_table(file, sep=",", index_col=False, nrows=5)
    print(df.head())
    df.to_csv("Kotok.csv")
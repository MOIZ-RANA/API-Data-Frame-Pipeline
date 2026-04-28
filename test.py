import pandas as pd 

df = pd.read_csv(r"D:\DataEngineering\Pandas\DataSets\Titanic-Dataset.csv")
# print(df)


print(df.loc[(df["Pclass"] == 3) & (df["Sex"] == "male")])

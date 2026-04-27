import pandas as pd 

df = pd.read_csv(r"D:\DataEngineering\Pandas\DataSets\Titanic-Dataset.csv")
# print(df)

# df = df[[["Pclass"] == 3 ] & [["Sex"] == 'male']]
# print(df)

df.info()
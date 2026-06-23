import pandas as pd 

df = pd.read_csv(r"D:\DataEngineering\Pandas\DataSets\Titanic-Dataset.csv")
# print(df)
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file
# WE have made changes to this file

print(df.loc[(df["Pclass"] == 3) & (df["Sex"] == "male")])

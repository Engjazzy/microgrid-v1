import pandas as pd

gen = pd.read_csv(
    "data/de_Actual_generation.csv",
    sep=";",
    thousands=",",
)
cons= pd.read_csv("data/de_Actual_consumption.csv",
sep=";",
thousands=",",
)
print(gen.columns)
print(gen.head())
print(cons.columns)
print(cons.head())
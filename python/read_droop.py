import pandas as pd

df = pd.read_csv("python/droop.csv")
print(df)
print("G1/G2 power ratio:")
print(df["Pgen1_pu"] / df["Pgen2_pu"])
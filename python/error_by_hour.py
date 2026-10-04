import pandas as pd

df = pd.read_csv("data/persistence_june.csv")
df["Start date"] = pd.to_datetime(df["Start date"])
df["hour"] = df["Start date"].dt.hour

by_hour = df.groupby("hour")["error"].mean()
print(by_hour)
print("worst hour", by_hour.idxmax(), "MAE", by_hour.max())
by_hour.to_csv("data/error_by_hour.csv")
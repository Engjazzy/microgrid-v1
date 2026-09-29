import pandas as pd

gen = pd.read_csv("data/Actual_generation_June_hour.csv",
sep =";",
thousands= ",",
)

gen["Start date"] = pd.to_datetime(gen["Start date"])
pv = "Photovoltaics [MWh] Calculated resolutions"

df = gen[["Start date", pv]].copy()
df["pred"]= df[pv].shift(1)
df["error"]= (df[pv] - df["pred"]).abs()

print(df.head(8))
print("MAE MWh", df["error"].mean())
print("rows", len(df), "non-empty pred", df["pred"].notna().sum())

df.to_csv("data/persistence_june.csv", index=False)
print("saved data/persistence_june.csv")
import pandas as pd

load = pd.read_csv(
    "data/de_Actual_consumption.csv",
    sep=";",
    thousands=",",
)

load["Start date"] =pd.to_datetime(load["Start date"])
res ="Residual load [MWh] Calculated resolutions"

df = load[["Start date", res]].copy()
df["action"] = "hold"
df.loc[df[res] < 0, "action"] = "charge"
df.loc[df[res] > 30000, "action"] = "discharge"

print(df["action"].value_counts())
df.to_csv("data/battery_rule.csv", index=False)
print("saved data/battery_rule.csv")
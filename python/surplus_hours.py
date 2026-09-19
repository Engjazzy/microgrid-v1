import pandas as pd

gen = pd.read_csv("data/de_Actual_generation.csv",
sep =";",
thousands =",",
)
load = pd.read_csv("data/de_Actual_consumption.csv",
sep =";",
thousands =",",
)
gen["Start date"] = pd.to_datetime(gen["Start date"])
load["Start date"] = pd.to_datetime(load["Start date"])

df = gen.merge(load, on="Start date")

pv = "Photovoltaics [MWh] Calculated resolutions"
w_on = "Wind onshore [MWh] Calculated resolutions"
w_off = "Wind offshore [MWh] Calculated resolutions"
grid = "grid load [MWh] Calculated resolutions"
res = "Residual load [MWh] Calculated resolutions"

df["residual_calc"] = df[grid]- df[pv]-df[w_on] - df[w_off]
df["diff"] = df[res]- df["residual_calc"]

df.to_csv("data/merge_file.csv")

surplus_df = df.loc[df[res] < 0, ["Start date", res]]
surplus_df.to_csv("data/surplus_hours.csv", index=False)

print(df[["Start date", res, "residual_calc", "diff"]].head(8))
print("mean diff", df["diff"].mean())
print("surplus hours (SMARD residual < 0)", (df[res] < 0).sum())

n = len(df)
surplus = (df[res] < 0).sum()
print("hours in week", n)
print("surplus hours", surplus)
print("surplus share", surplus / n)

print("surplus hours", len(surplus_df), "of", len(df))


import pandas as pd

gen = pd.read_csv(
    "data/de_Actual_generation.csv",
    sep=";",
    thousands=",",
)

load = pd. read_csv(
    "data/de_Actual_consumption.csv",
sep = ";",
thousands = ",",
)
gen["Start date"] = pd.to_datetime(gen["Start date"])
load["Start date"] = pd.to_datetime(load["Start date"])

pv_col = "Photovoltaics [MWh] Calculated resolutions"
res_col = "Residual load [MWh] Calculated resolutions"
grid_col = "grid load [MWh] Calculated resolutions"

df = gen.merge(load, on="Start date")
df["day"] = df["Start date"].dt.date

daily = df.groupby("day").agg(
    pv_max=(pv_col, "max"),
    residual_min=(res_col, "min"),
    grid_max=(grid_col, "max"),
)
print(daily)
daily.to_csv("data/daily_smard.csv")
print(" saved data/daily_smard.csv")
import pandas as pd
import matplotlib.pyplot as plt

gen = pd.read_csv(
    "data/de_Actual_generation.csv",
    sep=";",
    thousands=",",
)
load = pd.read_csv(
    "data/de_Actual_consumption.csv",
    sep=";",
    thousands=",",
)

gen["Start date"] = pd.to_datetime(gen["Start date"])
load["Start date"] = pd.to_datetime(load["Start date"])

pv_col = "Photovoltaics [MWh] Calculated resolutions"
res_col = "Residual load [MWh] Calculated resolutions"

df = gen.merge(load, on="Start date")

plt.plot(df["Start date"], df[pv_col], label="PV generation")
plt.plot(df["Start date"], df[res_col], label="Residual load")
plt.xlabel("Time")
plt.ylabel("MWh")
plt.title("Germany PV vs residual load — 31 Aug–6 Sep 2026 (SMARD)")
plt.legend()
plt.grid(True, axis="y")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/10_pv_vs_residual.png")
print("saved figures/10_pv_vs_residual.png")
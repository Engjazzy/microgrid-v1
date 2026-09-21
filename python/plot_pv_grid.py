import pandas as pd
import matplotlib.pyplot as plt

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
grid = "grid load [MWh] Calculated resolutions"

plt.plot(df["Start date"], df[pv], label="PV")
plt.plot(df["Start date"], df[grid], label="Grid load")
plt.ylabel("MWh")
plt.xlabel("Time")
plt.title("Germany PV vs grid load — 31 Aug–6 Sep 2026 (SMARD)")
plt.legend()
plt.grid(True, axis="y")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/Python plots/13_pv_vs_grid.png")
print("saved figures/Python plots/13_pv_vs_grid.png")

import pandas as pd
import matplotlib.pyplot as plt

gen = pd.read_csv("data/de_Actual_generation.csv",
sep =";",
thousands = ",",
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



plt.plot(df["Start date"], df[res], label="SMARD residual")
plt.plot(df["Start date"], df["residual_calc"], label="calculated")
plt.ylabel("Residual load(MWh)")
plt.title("SMARD residual vs calculated")
plt.xlabel("Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, axis="y")
plt.savefig("figures/Python plots/12_residual_check.png.")
print("saved12_residual_check.png")
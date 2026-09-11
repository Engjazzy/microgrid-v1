import pandas as pd
import matplotlib.pyplot as plt

gen = pd.read_csv(
    "data/de_Actual_generation.csv",
    sep=";",
    thousands=",",
)
gen["Start date"] = pd.to_datetime(gen["Start date"])

pv_col = "Photovoltaics [MWh] Calculated resolutions"

plt.plot(gen["Start date"], gen[pv_col])
plt.xlabel("Time")
plt.ylabel("Photovoltaics [MWh]")
plt.title("Germany PV — 31 Aug to 6 Sep 2026 (SMARD)")
plt.grid(True, axis="y")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/09_smard_pv.png")
print("saved figures/09_smard_pv.png")
print(gen[pv_col].max())
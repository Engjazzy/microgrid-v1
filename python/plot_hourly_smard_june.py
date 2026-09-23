import pandas as pd
import matplotlib.pyplot as plt

daily = pd.read_csv("data/Actual_generation_June_hour.csv",
sep= ";",
thousands= ",",
)
pv_col = "Photovoltaics [MWh] Calculated resolutions"

daily["Start date"] = pd.to_datetime(daily["Start date"])

plt.plot(daily["Start date"], daily[pv_col])
plt.xlabel("Time")
plt.ylabel("Photovoltaics (MWh)")
plt.title("Germany PV — 1–7 Jun 2026 (SMARD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/Python plots/14_smard_pv_june.png")
print("saved figures/Python plots/14_smard_pv_june.png")
print(daily[pv_col].max())
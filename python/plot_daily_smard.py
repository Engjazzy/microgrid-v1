import pandas as pd
import matplotlib.pyplot as plt

daily = pd.read_csv("data/daily_smard.csv")

plt.bar(daily["day"].astype(str), daily["pv_max"])
plt.xlabel("Day")
plt.ylabel("Max hourly PV (MWh)")
plt.title("Germany daily peak PV — 30 Aug–6 Sep 2026")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/11_daily_pv_max.png")
print("saved figures/11_daily_pv_max.png")
print(daily)
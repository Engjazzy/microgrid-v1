import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/battery_rule.csv")
df["Start date"] = pd.to_datetime(df["Start date"])

cap = 10000
step = 2000
soc = 0.5 * cap
socs = []



for action in df["action"]:
    if action == "charge":
        soc = min(cap, soc + step)
    elif action == "discharge":
        soc = max(0, soc - step)
    socs. append(soc)

df["soc_mwh"] = socs
df.to_csv("data/battery_soc.csv", index=False)

plt.plot(df["Start date"], df["soc_mwh"])
plt.ylabel("SOC (MWh)")
plt.xlabel("Time")
plt.title("Dummy battery SOC — 31 Aug–6 Sep 2026")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/Python plots/15_battery_soc.png")
print("saved figures/Python plots/15_battery_soc.png")
print(df["action"].value_counts())
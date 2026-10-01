import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/persistence_june.csv")
df["Start date"] = pd.to_datetime(df["Start date"])

pv = "Photovoltaics [MWh] Calculated resolutions"

plt.plot(df["Start date"],  df[pv], label = "Actual PV" )
plt.plot(df["Start date"], df["pred"], label = "Persistence" )
plt.ylabel("MWh")
plt.xlabel("Time")
plt.title("June 2026 PV: actual vs next-hour persistence")
plt.grid(True, axis="y")
plt.legend()
plt.xticks(rotation =45)
plt.tight_layout()


plt.savefig("figures/Python plots/17_persistence")
print("You be agba coder")
print("saved figures/17_ persistence")
print("MAE MWh", df["error"].mean())

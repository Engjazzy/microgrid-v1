import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/persistence_june.csv")
df["Start date"] = pd.to_datetime(df["Start date"])

pv = "Photovoltaics [MWh] Calculated resolutions"

df["pred_yday"] = df[pv].shift(24)
df["error_yday"] = (df[pv] - df["pred_yday"]).abs()


plt.plot(df["Start date"], df["error"], label = "persistence error")
plt.plot(df["Start date"], df["error_yday"],label = "yesterday error")
plt.legend()
plt.ylabel("MWh")
plt.xlabel("Time")
plt.title("Persistence error vs Yesterday error")
plt.xticks(rotation = 45)
plt.tight_layout()





print("persistence MAE", df["error"].mean())
print("yesterday MAE", df["error_yday"].mean() )
print("hours with yesterday", df["pred_yday"].notna().sum(),"of", len(df))

out = df.dropna(subset=["pred_yday"])
print("persistence MAE on same hours", out["error"].mean())

plt.savefig("figures/Python plots/18_persistence_error_vs_yesterday_error.png")
print("you be agba coder")
print("saved figures/Python plots/18_persistence_error_vs_yesterday_error")
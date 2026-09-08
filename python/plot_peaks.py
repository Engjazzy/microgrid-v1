import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("python/peaks.csv")

plt.plot(df["sun_wm2"], df["pac_w"], marker="o")
plt.xlabel("Peak irradiance (W/m2)")
plt.ylabel("Peak P_AC (W)")
plt.title("MPPT peaks from CSV")
plt.grid(True)
plt.savefig("figures/07_pandas_plot.png")
print("saved figures/07_pandas_plot.png")
print(df)
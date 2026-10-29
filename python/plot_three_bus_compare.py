import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/three_bus_compare.csv")

x = range(len(df))
plt.bar([i - 0.2 for i in x], df["voltage_with_pv"], width=0.4, label="with PV")
plt.bar([i + 0.2 for i in x], df["voltage_without_pv"], width=0.4, label="no PV")
plt.xticks(list(x), df["bus"])
plt.ylim(0.997, 1.002)
plt.ylabel("Voltage (pu)")
plt.title("Three-bus: with PV vs no PV")
plt.legend()
plt.tight_layout()
plt.savefig("figures/Python plots/25_three_bus_compare.png")
print("saved figures/Python plots/25_three_bus_compare.png")
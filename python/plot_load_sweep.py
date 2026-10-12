import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/load_sweep.csv")

plt.bar(df["p_mw"].astype(str), df["vm_load_pu"])
plt.ylim(0.9985, 1.0005)
plt.xlabel("Load (Mw)")
plt.ylabel("Load-bus voltage (pu)")
plt.title("1 km feeder: voltage falls as load rises")
plt.tight_layout()
plt.savefig("figures/Python plots/20_load_sweep.png")
print("saved figures/Python plots/20_load_sweep.png")
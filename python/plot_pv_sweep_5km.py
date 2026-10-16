import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/pv_sweep_5km.csv")

plt.bar(df["pv_mw"].astype(str), df["vm_load_pu"])
plt.ylim(0.998, 1.005)
plt.xlabel("PV (MW)")
plt.ylabel("Load-bus voltage (pu)")
plt.title("5 km feeder, 0.5 MW load: larger voltage rise")
plt.tight_layout()
plt.savefig("figures/Python plots/23_pv_sweep_5km.png")
print("saved figures/Python plots/23_pv_sweep_5km.png")
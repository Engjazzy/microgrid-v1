import pandas as pd
import matplotlib.pyplot as plt

load = pd.read_csv("data/load_sweep.csv")
pv = pd.read_csv("data/pv_sweep.csv")

fig, ax = plt.subplots(1, 2, figsize=(9, 4))

ax[0].bar(load["p_mw"].astype(str), load["vm_load_pu"])
ax[0].set_ylim(0.9985, 1.001)
ax[0].set_xlabel("Load (MW)")
ax[0].set_ylabel("Load-bus voltage (pu)")
ax[0].set_title("More load → lower voltage")

ax[1].bar(pv["pv_mw"].astype(str), pv["vm_load_pu"])
ax[1].set_ylim(0.9985, 1.001)
ax[1].set_xlabel("PV (MW)")
ax[1].set_title("More PV → higher voltage")

fig.suptitle("Same 1 km feeder, 0.5 MW base load")
fig.tight_layout()
fig.savefig("figures/Python plots/22_load_vs_pv.png")
print("saved figures/Python plots/22_load_vs_pv.png")
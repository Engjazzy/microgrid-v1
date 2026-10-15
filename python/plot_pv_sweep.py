import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("data/pv_sweep.csv")

plt.bar(df["pv_mw"].astype(str), df["vm_load_pu"] )
plt.ylim(0.999,1.001)
plt.ylabel("Load-bus voltage(pu)")
plt.xlabel("PV(MW)")
plt.title("1 km feeder, 0.5 MW load, voltage rises with PV")
plt.tight_layout()

plt.savefig("figures/Python plots/21_pv_sweep.png")
print("code cooked")
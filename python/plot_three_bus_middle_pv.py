import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/three_bus_pv_middle_bus.csv", index_col=0)

plt.bar(["slack", "middle", "far end"], df["vm_pu"])
plt.ylim(0.999, 1.001)
plt.ylabel("Voltage (pu)")
plt.title("Three-bus: PV at middle bus")
plt.tight_layout()
plt.savefig("figures/Python plots/26_three_bus_pv_middle.png")
print("saved figures/Python plots/26_three_bus_pv_middle.png")
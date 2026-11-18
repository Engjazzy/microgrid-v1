import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("data/three_bus_long_middle.csv", index_col=0)

plt.bar(["slack", "middle", "far end"], df["vm_pu"])
plt.ylim(0.999, 1.002)
plt.ylabel("Voltage (pu)")
plt.title("Three-bus: 4 km + 2.5 km, PV at far end")
plt.tight_layout()
plt.savefig("figures/Python plots/27_three_bus_long_middle.png")
print("saved figures/Python plots/27_three_bus_long_middle.png")
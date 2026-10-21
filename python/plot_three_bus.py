import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/three_bus.csv", index_col=0)

plt.bar(["slack","middle bus","far end"], df["vm_pu"])
plt.ylim(0.999, 1.001)
plt.ylabel("Voltage(per unit)")
plt.xlabel("The three buses")
plt.title("Three-bus feeder voltages")
plt.tight_layout()
plt.savefig("figures/Python plots/24_three_bus.png")
print("code cooked")
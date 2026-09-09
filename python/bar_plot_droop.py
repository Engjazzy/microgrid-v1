import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("python/droop.csv")

x = range(len(df))
plt.bar([i - 0.22 for i in x], df["Pgen1_pu"], width=0.4, color="crimson", label="G1")
plt.bar([i + 0.22 for i in x], df["Pgen2_pu"], width=0.4, color="navy", label="G2")
plt.xticks(list(x), df["case"])
plt.ylabel("Active power (pu)")
plt.title ("Droop cases:who produces P")
plt.legend()
plt.grid(True, axis="y")
plt.savefig("figures/08_droop_share.png")
print("saved figures/08_droop_share.png")
print (df)
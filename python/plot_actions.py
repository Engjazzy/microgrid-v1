import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/battery_soc.csv")
counts = df["action"].value_counts()
print(counts)

plt.bar(counts.index, counts.values)
plt.ylabel("Hours")
plt.title("Dummy rule: hours by action (31 Aug–6 Sep)")
plt.tight_layout()
plt.savefig("figures/Python plots/16_action_counts.png")
print("saved figures/Python plots/16_action_counts.png")
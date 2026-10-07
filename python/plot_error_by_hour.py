import pandas as pd
import matplotlib.pyplot as plt 

by_hour = pd.read_csv("data/error_by_hour.csv", index_col=0)
by_hour = by_hour.squeeze()

plt.bar(by_hour.index, by_hour.values)
plt.xlabel("Hour of the day")
plt.ylabel("Mean persistence error(MWh)")
plt.title("June 2026: persistence error by clock hour")
plt.tight_layout()

plt.savefig("figures/Python plots/19_error_by_hour.png")
print("saved figures/Python plots/picture")
print(by_hour.idxmax(),"th hour is the hour with the highest MAE", by_hour.max(), "IS THE VALUE FOR THAT HOUR")
import pandas as pd

gen = pd.read_csv("data/Actual_generation_June.csv",
sep= ";",
thousands= ",",
)

load = pd.read_csv("data/Actual_consumption_June.csv",
sep= ";",
thousands= ",",
)

grid_load = "grid load [MWh] Calculated resolutions"
pv = "Photovoltaics [MWh] Calculated resolutions"

print(gen[pv])
print(load[grid_load])
print("You be agba coder, I hail thee human")
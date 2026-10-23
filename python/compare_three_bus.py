import pandas as pd

pv = pd.read_csv("data/three_bus.csv")
nopv = pd.read_csv("data/three_bus_nopv.csv")

df = pd.DataFrame({
    "bus": ["bus1-slack", "bus2-middle", "bus3-far end"],
    "voltage_with_pv": pv["vm_pu"],
    "voltage_without_pv": nopv["vm_pu"]
})

print(df.to_string(index=False))
df.to_csv("data/three_bus_compare.csv", index=False)
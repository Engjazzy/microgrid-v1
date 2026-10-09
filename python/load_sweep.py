import pandapower as pp
import pandas as pd

rows = []
for p in [0.5, 1.0, 2.0]:
    net = pp.create_empty_network()
    b0 = pp.create_bus(net, vn_kv=20.0)
    b1 = pp.create_bus(net, vn_kv=20.0)
    pp.create_ext_grid(net, bus=b0, vm_pu=1.0)
    pp.create_line(net, from_bus=b0, to_bus=b1, length_km=1.0, std_type="NAYY 4x150 SE")
    pp.create_load(net, bus=b1, p_mw=p, q_mvar=0.1)
    pp.runpp(net)
    rows.append({"p_mw": p, "vm_load_pu": net.res_bus.vm_pu.at[1]})

df = pd.DataFrame(rows)
print(df)
df.to_csv("data/load_sweep.csv", index=False)
print("saved data/load_sweep.csv")


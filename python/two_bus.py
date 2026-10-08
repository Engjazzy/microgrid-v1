import pandapower as pp

net = pp.create_empty_network()
b0 = pp.create_bus(net, vn_kv=20.0, name="slack")
b1 = pp.create_bus(net, vn_kv=20.0, name="load")
pp.create_ext_grid(net, bus=b0, vm_pu=1.0)
pp.create_line(net, from_bus=b0, to_bus=b1, length_km=1.0, std_type="NAYY 4x150 SE")
pp.create_load(net, bus=b1, p_mw=0.5, q_mvar=0.1)
pp.runpp(net)
print(net.res_bus[["vm_pu", "p_mw"]])
net.res_bus.to_csv("data/two_bus_result.csv")
print("saved data/two_bus_result.csv")
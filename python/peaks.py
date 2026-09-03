import matplotlib.pyplot as plt

sun = [1200, 900, 600]
pac = [380, 281.4, 182.2]

plt.plot(sun, pac, marker="o")
plt.xlabel("Peak irradiance (W/m2)")
plt.ylabel("Peak P_AC (W)")
plt.title("MPPT test: power vs irradiance")
plt.grid(True)
plt.savefig("figures/06_python_pac_vs_sun.png")
print("saved figures/06_python_pac_vs_sun.png")


# microgrid-v1

Public write-up of MathWorks “Modeling a Hybrid Microgrid” (Simscape Electrical).
I ran the Test / System models, changed irradiance and droop parameters, and
plotted the measured results with Python.

Germany / Energiewende: PV power follows sun, and droop is how sources share
load when many inverters sit on one grid.

## MATLAB experiments

- b_test_solar_MPPT: PV power follows irradiance; V_cell stayed near 30 V (MPPT).
- c_test_AC_droop: generators share P; lower droop → that machine produces more P.
- a_AC_DC_System: battery follows P_batt_ref; AC gens share load.

### Irradiance (b_test_solar_MPPT)

Default profile × scale. Default *200 → peak sun 1200 W/m².

| Scale | Peak sun | Peak P_AC | V_cell |
|---|---|---|---|
| *200 | 1200 W/m² | ~380 W | ~30 V |
| *150 | 900 W/m² | ~281.4 W | ~30 V |
| *100 | 600 W/m² | ~182.2 W | ~30 V |

### Droop (c_test_AC_droop)

Workspace `droopP1` / `droopP2`. Q–V droops stayed 0.05.

| Case | droopP1 | droopP2 | Result |
|---|---|---|---|
| Equal | 0.05 | 0.05 | One slope. G1 and G2 both ~0.40 pu at ~0.98 pu |
| G2 lower droop | 0.05 | 0.025 | G1 ~0.27 pu, G2 ~0.53 pu, f ~0.987 pu |
| G1 lower droop | 0.0125 | 0.05 | G1 ~0.63 pu, G2 ~0.16 pu, f ~0.992 pu |

0.05/0.025 = 2 ≈ 0.53/0.27; 0.05/0.0125 = 4 ≈ 0.63/0.16.

## Python

Numbers live in CSV files. Scripts read those files and plot.

```bash
cd microgrid-v1
python3 -m pip install -r requirements.txt
python3 python/plot_peaks.py
python3 python/bar_plot_droop.py
```

| File | Role |
|---|---|
| python/peaks.csv | MPPT peaks |
| python/peaks.py | plot from lists → figures/06_python_pac_vs_sun.png |
| python/read_peaks.py | print table and P_AC / sun (~0.31) |
| python/plot_peaks.py | plot from CSV → figures/07_pandas_plot.png |
| python/droop.csv | droop cases |
| python/read_droop.py | print table and Pgen1/Pgen2 |
| python/bar_plot_droop.py | bar chart → figures/08_droop_share.png |


![MPPT peaks](figures/Python%20plots/07_pandas_plot.png)

![Droop share](figures/Python%20plots/08_droop_share.png)

![MPPT POWER VS IRRADIANCE](figures/Python%20plots/06_python_pac_vs_sun.png)


## v2 — SMARD week (31 Aug–6 Sep 2026)

German actual generation and consumption from SMARD / Bundesnetzagentur.
Files in data/. python/peek_data.py loads them with sep=";" and thousands=",".
Next: plot Photovoltaics vs time.

python/plot_smard_pv.py → figures/09_smard_pv.png
Source: SMARD / Bundesnetzagentur, actual generation.

plot_smard_pv.py → figures/09_smard_pv.png (peak PV ~47692 MWh).
plot_smard_compare.py → figures/10_pv_vs_residual.png
Residual load (SMARD) = consumption − wind − PV.
Negative hours: wind+PV exceeded load.

![SMARD GERMAN PV ACTUAL GENERATION](figures/Python%20plots/09_smard_pv.png)
![ACTUAL GENERTAION VS RESIDUAL LOAD](figures/Python%20plots/10_pv_vs_residual.png)

6 Sep: highest PV hour (~47692 MWh) and deepest surplus (residual_min ~-8399 MWh).
Weekday grid_max > weekend (typical).
30 Aug row is only 23:00 (file start); PV is 0 because it is night, not a full day.
 daily_smard.py printed the results  of the highest PV generation hour, highest residual load hour, and highest load grid cosumption hour into data/daily_smard.csv

 Bar chart plot of the max pv of the SmARD for the one week.
 plot_daily_smard.py printed the results  of the highest PV generation for each day into figures/Python plots/11_daily_pv_max.png

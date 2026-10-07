## What this repo shows
1. MATLAB hybrid microgrid: PV follows irradiance; lower droop → larger power share.
2. SMARD Germany: one late-August week + one June week. Residual = grid load − wind − PV. Formula checked (figure 12).
3. Dummy battery rule on the August residual: charge if residual < 0, discharge if residual > 30000 MWh, else hold. Toy 10000 MWh. SOC pegs at 0 and at cap.

Not an optimiser. Not a forecast.



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
`peek_data.py` loads the CSVs with `sep=";"` and `thousands=","`.

Residual load (SMARD) = grid consumption − wind − PV.
Negative residual: wind+PV exceeded load that hour.

| File | Role |
|---|---|
| data/de_Actual_generation.csv | Hourly generation by technology |
| data/de_Actual_consumption.csv | Grid load, pumps, residual load |
| python/peek_data.py | Print columns and first rows |
| python/plot_smard_pv.py | figures/Python plots/09_smard_pv.png |
| python/plot_smard_compare.py | figures/Python plots/10_pv_vs_residual.png |
| python/daily_smard.py | data/daily_smard.csv |
| python/plot_daily_smard.py | figures/Python plots/11_daily_pv_max.png |

Peak hourly PV in the week ~47692 MWh.
6 Sep: highest PV hour and deepest surplus (residual_min ~-8399 MWh).
Weekday grid_max > weekend.
30 Aug in the daily table is only 23:00 (file start); PV is 0 because it is night.

Same lesson as the MATLAB MPPT test: more sun → more PV. Here the scale is national.

![SMARD PV](figures/Python%20plots/09_smard_pv.png)
![PV vs residual load](figures/Python%20plots/10_pv_vs_residual.png)
![Daily peak PV](figures/Python%20plots/11_daily_pv_max.png)

## Residual check
check_residual.py: residual_calc = grid load − PV − wind onshore − wind offshore.
mean diff ≈ 0.00047619047614436534 MWh
surplus hours: 37 of 168.

plot_residual_check.py → figures/Python plots/12_residual_check.png
SMARD residual and calculated residual overlap (grid − PV − wind).
![Curve of SMARD residual load vs calculated residual load](figures/Python%20plots/12_residual_check.png)

data/surplus_hours.csv — hours where residual < 0 (wind+PV covered load).
37 of 168 hours this week.

plot_pv_grid.py → figures/Python plots/13_pv_vs_grid.png
PV vs total grid load (not residual). On 6 Sep peak PV ≈ grid load; other days PV stays below demand.
Weekend grid load is lower than weekdays.

![PV vs grid load](figures/Python%20plots/13_pv_vs_grid.png)

June 2026 week CSVs in data/ (not plotted yet).
Confirmed Photovoltaics and grid load exist using peek_June_data.py
They followed the same seperator and thousands format

## June 2026 week
File: data/Actual_generation_June_hour.csv (1–7 Jun, SMARD generation).
plot → figures/Python plots/14_smard_pv_june.png
June peak hourly PV ≈ 46102.94 MWh
31 Aug–6 Sep peak ≈ 47692 MWh
![June PV](figures/Python%20plots/14_smard_pv_june.png)

| Week | Peak hourly PV (MWh) |
|---|---|
| 31 Aug–6 Sep 2026 | 47692 |
| 1–7 Jun 2026 | 46102.94 |


## Dummy battery rule (v3)
If residual < 0: charge. If residual > 30000 MWh: discharge. Else hold.
See data/battery_rule.csv. Not a real battery — a policy on SMARD residual.

## Dummy battery (v3)
Rule: residual < 0 charge; residual > 30000 discharge; else hold.
Toy battery 10000 MWh, step 2000 MWh/h, start 50%.
battery_rule.py → data/battery_rule.csv
battery_soc.py → data/battery_soc.csv and figures/Python plots/15_battery_soc.png

![Dummy SOC](figures/Python%20plots/15_battery_soc.png)

## Dummy battery (v3)
Rule: residual < 0 charge; residual > 30000 MWh discharge; else hold.
Toy battery 10000 MWh, step 2000 MWh/h, start 50%.
SOC hits 0 and 10000 because the tank is tiny vs national residual.

Hours this week: hold 101, charge 37, discharge 30.
battery_rule.py → data/battery_rule.csv
battery_soc.py → data/battery_soc.csv, figures/Python plots/15_battery_soc.png
plot_actions.py → figures/Python plots/16_action_counts.png

![Dummy SOC](figures/Python%20plots/15_battery_soc.png)
![Action counts](figures/Python%20plots/16_action_counts.png)

## Persistence baseline (analyst toolkit)
Next-hour PV forecast = last hour's PV (June 2026 SMARD).
MAE ≈ 3249.7629 MWh.
See python/persistence_pv.py and data/persistence_june.csv.
Not a model. This is the baseline any later forecast must beat.



python/plot_persistence shows the Actual PV vs persistence curves
![Actual PV vs Persistence](figures/Python%20plots/17_persistence.png)
persistence misses the morning rise and evening drop.

On the 144 hours that have both guesses:
persistence MAE ≈ 3129 MWh, same-hour-yesterday MAE ≈ 3574 MWh.
Persistence wins on this June week (~445 MWh closer).
![Persistence vs yesterday error](figures/Python%20plots/18_persistence_error_vs_yesterday_error.png)

Persistence error by clock hour: worst around 08:00 (MAE ≈ 8361.731 MWh).
Night hours are easy because PV stays near 0.

Persistence error by clock hour: worst around 08:00 (MAE ≈ 8362 MWh).
Night hours are easy because PV stays near 0.
![Error by hour](figures/Python%20plots/19_error_by_hour.png)
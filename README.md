# microgrid-v1# Hybrid microgrid — first public version

MathWorks project: Modeling a Hybrid Microgrid (Simscape Electrical).
I already worked through most of the live script sections
(Essentials → Test → System). This repo is the clean public copy.

What I will likely add next session(probably more) (screenshots + short notes):
- PV / MPPT: 2. Test / b_test_solar_MPPT.slx
- AC droop: 2. Test / c_test_AC_droop.slx
- Hybrid AC/DC system: 3. System / a_AC_DC_System.slx

First run already produced PV power curves vs irradiance
and AC waveforms from the Getting Started model.

Germany link: PV + droop + AC/DC coupling is the same
problem as high solar share on German distribution grids.


## What I ran
- b_test_solar_MPPT: PV power follows irradiance; V_cell held near 30 V
- c_test_AC_droop: equal droop 0.05, generators share; f ≈ 0.98 pu at 0.4 pu power
- a_AC_DC_System: battery follows P_batt_ref; AC gens share load; AC/DC link tracks P_AC_ref

Models are from MathWorks “Modeling a Hybrid Microgrid.”


## Irradiance experiments (b_test_solar_MPPT)

The irradiance block is a 24-step profile times a scale factor.
Default: [0 0 1 1 ... 6 6 ... 1 1]*200  → peak sun 1200 W/m².

| Scale | Peak sun | Peak P_AC | V_cell |
|---|---|---|---|
| *200 (default) | 1200 W/m² | ~380 W | ~30 V |
| *150 | 900 W/m² | ~281.4W | ~30 V |
| *100 | 600 W/m² | ~182.2 W | ~30 V |

Less sun = less current = less power.
V_cell stayed near 30 V because MPPT holds the panel at its MPP voltage.

Figures: in folder "irradiance runs"
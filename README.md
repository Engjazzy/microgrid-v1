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

30.8

## What I ran
- b_test_solar_MPPT: PV power follows irradiance; V_cell held near 30 V
- c_test_AC_droop: equal droop 0.05, generators share; f ≈ 0.98 pu at 0.4 pu power
- a_AC_DC_System: battery follows P_batt_ref; AC gens share load; AC/DC link tracks P_AC_ref

Models are from MathWorks “Modeling a Hybrid Microgrid.”
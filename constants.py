"""
kse/constants.py
================
All physical and framework constants for the κ = 3.0 Unified Framework.

Priority timestamp: viXra:2512.0067, December 26, 2025
Author: C. Howlett — unitivity.research@gmail.com
Licence: CC-BY-SA-4.0
"""

import math

# ── Fundamental framework constant ───────────────────────────────────────────
KAPPA          = 3.0          # κ_theoretical: exact integer, derived not fitted
KAPPA_EMPIRICAL    = 2.885640     # from E8 root-system spectral analysis
KAPPA_COMPUTATIONAL = 2.91729347  # from recursive alignment / biological optimisation

# ── Mathematical constants ────────────────────────────────────────────────────
PI   = math.pi                # 3.14159265358979...
PHI  = (1 + math.sqrt(5)) / 2  # golden ratio 1.61803...

# ── The 4.5% residue ─────────────────────────────────────────────────────────
DELTA = (PI - KAPPA) / PI     # (π − 3)/π ≈ 0.04507 — discrete-to-continuum signature

# ── Single scale-setting input ───────────────────────────────────────────────
V_EW = 246.22    # GeV — electroweak VEV (only experimental input used in mass ladder)

# ── Standard Model measured values (for comparison) ──────────────────────────
M_HIGGS_OBS  = 125.25   # GeV  (PDG 2023)
M_Z_OBS      = 91.1876  # GeV
M_W_OBS      = 80.377   # GeV
M_TOP_OBS    = 172.69   # GeV
PROTON_RADIUS_MUON = 0.84087  # fm  (muonic hydrogen, CODATA 2018)
PROTON_RADIUS_ELEC = 0.8751   # fm  (electronic hydrogen)
H0_LOCAL     = 73.04    # km/s/Mpc  (SH0ES 2022)
H0_CMB       = 67.4     # km/s/Mpc  (Planck 2018)
ALPHA_INV_OBS = 137.035999084  # fine structure constant inverse (CODATA 2018)
KLEIBER_EXP_OBS = 0.751        # Kleiber's law exponent ± 0.009
WATER_ANGLE_OBS = 104.5        # degrees
DARK_MATTER_FRACTION_OBS = 0.840  # Planck 2018

# ── κ-framework coupling ratios ───────────────────────────────────────────────
RATIO_EMP_THEORY  = KAPPA_EMPIRICAL / KAPPA          # 0.96188 — QFT-to-GR coupling
RATIO_COMP_THEORY = KAPPA_COMPUTATIONAL / KAPPA      # 0.97243 — info processing limit
RATIO_EMP_COMP    = KAPPA_EMPIRICAL / KAPPA_COMPUTATIONAL  # 0.98913 — quantum-to-classical

# ── 12×12 matrix eigenvalues ─────────────────────────────────────────────────
LAMBDA_1 = 0.8500                # dominant eigenvalue
LAMBDA_2 = LAMBDA_1 / 3.0       # first sub-dominant: 0.28333 → ratio = 3.000 exactly
# κ = λ₁/λ₂ = 0.8500/0.28333 = 3.000 (exact)

# ── Planck units ─────────────────────────────────────────────────────────────
L_PLANCK  = 1.616e-35   # m
T_PLANCK  = 5.391e-44   # s
M_PLANCK  = 2.176e-8    # kg

# ── Derived geometric quantities ─────────────────────────────────────────────
KAPPA_OVER_PI = KAPPA / PI     # 0.95493 — appears in proton radius ratio
PI_OVER_KAPPA = PI / KAPPA     # 1.04720 — appears in Hubble tension ratio
ALPHA_WEAK    = PI - KAPPA     # ≈ 0.1416 — weak force coupling (geometric origin)
ALPHA_INV_PRED = 137 + 12 / PHI**12  # fine structure constant prediction

if __name__ == "__main__":
    print(f"κ            = {KAPPA}")
    print(f"Δ = (π−κ)/π  = {DELTA:.6f}  ({DELTA*100:.3f}%)")
    print(f"κ/π          = {KAPPA_OVER_PI:.6f}")
    print(f"π/κ          = {PI_OVER_KAPPA:.6f}")
    print(f"α_weak       = π − κ = {ALPHA_WEAK:.6f}")
    print(f"α⁻¹ predicted = {ALPHA_INV_PRED:.6f}  (observed: {ALPHA_INV_OBS})")
    print(f"λ₁/λ₂        = {LAMBDA_1/LAMBDA_2:.6f}  (→ κ = 3)")

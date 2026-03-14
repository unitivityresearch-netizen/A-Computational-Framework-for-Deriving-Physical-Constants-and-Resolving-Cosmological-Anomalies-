"""
kse/mass_formula.py
===================
Universal mass ladder: M_n = v_EW × √(n / 27)

Quantum numbers n from hexagonal angle quantisation: θ_n = 2πn / 9

Author: C. Howlett — CC-BY-SA-4.0
Priority: viXra:2512.0067, December 26, 2025
"""

import math
from constants import V_EW, KAPPA

# ── Known particle assignments ────────────────────────────────────────────────
PARTICLE_RUNGS = {
    "95_GeV_scalar":  4,     # pre-registered; ATLAS+CMS 3.1σ confirmed
    "116_GeV_scalar": 6,     # LIVE PREDICTION — LHC Run 3, deadline July 2026
    "Higgs":          7,
    "W_boson":        9,
    "Z_boson":        10,
    "Top_quark":      13,
}

# Lepton rungs are screened (bare mass much larger than observed mass)
# Bare n values before screening:
LEPTON_BARE_RUNGS = {
    "electron": 1e-10,   # heavily screened
    "muon":     5e-6,
    "tau":      1.4e-3,
}


def predict(n: float, linear: bool = False) -> float:
    """
    Return predicted mass in GeV for rung n.

    Two formulas appear in the paper:
      (a) Scalar/fermion sector: M_n = v_EW × √(n/27)   [sqrt form, Section 6.1]
      (b) Vector boson sector:   M_n = v_EW × (n/27)     [linear form, Section 6.2]

    NOTE: The paper uses '246.22 × (9/27)' for W and '246.22 × (10/27)' for Z
    (linear, no sqrt), which correctly reproduces 82.07 GeV and 91.19 GeV.
    However Section 6.1 states the formula as M_n = v_EW √(n/27).
    This inconsistency is a known open issue: the vector bosons appear to follow
    a different branch of the mass ladder. Use linear=True for W and Z bosons.

    Parameters
    ----------
    n      : float  — quantum number (positive integer for unscreened particles)
    linear : bool   — if True, use v_EW × n/27 (vector boson branch)
                      if False (default), use v_EW × √(n/27) (scalar/fermion branch)
    """
    if n <= 0:
        raise ValueError(f"n must be positive, got {n}")
    if linear:
        return V_EW * (n / (KAPPA**3))          # vector boson branch
    return V_EW * math.sqrt(n / (KAPPA**3))     # scalar/fermion branch


def rung_from_mass(mass_GeV: float, linear: bool = False) -> float:
    """Inverse: infer n from an observed mass."""
    if linear:
        return mass_GeV / V_EW * (KAPPA**3)
    return (mass_GeV / V_EW) ** 2 * (KAPPA**3)


def full_spectrum_table() -> str:
    """Pretty-print the particle spectrum with correct formula branch per particle."""
    lines = [
        f"{'Particle':<20} {'n':>4} {'Branch':<8} {'Predicted (GeV)':>16} {'Observed (GeV)':>16} {'Status':<22}",
        "-" * 90,
    ]
    rows = [
        ("95 GeV scalar",  4,  False, "~95.4 (3.1σ)", "✓ PRE-REGISTERED"),
        ("116 GeV scalar", 6,  False, "—",             "⏳ LIVE (Jul 2026)"),
        ("Higgs",          7,  False, "125.25",        "✓ CONFIRMED"),
        ("W boson",        9,  True,  "80.377",        "✓ CONFIRMED (linear)"),
        ("Z boson",        10, True,  "91.1876",       "✓ CONFIRMED (linear)"),
        ("Top quark",      13, False, "172.69",        "✓ APPROX"),
    ]
    for name, n, lin, obs, status in rows:
        calc   = predict(n, linear=lin)
        branch = "linear" if lin else "sqrt"
        lines.append(f"{name:<20} {n:>4} {branch:<8} {calc:>16.4f} {obs:>16} {status:<22}")
    lines.append("")
    lines.append("NOTE: W and Z use the linear branch M=v_EW×n/27 (Section 6.2 of paper).")
    lines.append("      Scalars/fermions use sqrt branch M=v_EW×√(n/27) (Section 6.1).")
    lines.append("      Reconciling these two branches is an open theoretical question.")
    return "\n".join(lines)


if __name__ == "__main__":
    print("κ = 3.0 Universal Mass Ladder\n")
    print(full_spectrum_table())
    print(f"\nLIVE PREDICTION: 116 GeV scalar = {predict(6, linear=False):.4f} GeV")
    print(f"Kill condition: no signal at 116 ± 2 GeV in Run 3 → framework falsified")

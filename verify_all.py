#!/usr/bin/env python3
"""
scripts/verify_all.py
=====================
Run all κ = 3.0 framework predictions vs observed values.
No dependencies beyond numpy and Python standard library.

Usage: python scripts/verify_all.py

Author: C. Howlett — CC-BY-SA-4.0
Priority: viXra:2512.0067, December 26, 2025
"""

import math


from constants import KAPPA, PI, DELTA, V_EW, PHI
from mass_formula import predict, full_spectrum_table
from fixed_point import verify_fixed_point, iterate
from matrix12 import build_matrix, compute_kappa
from anomaly_resolver import run_all
from predictions import print_scorecard


def header(title: str):
    print(f"\n{'='*65}")
    print(f"  {title}")
    print(f"{'='*65}")


def main():
    print("κ = 3.0 UNIFIED FRAMEWORK — FULL VERIFICATION")
    print("I = MC²  |  Author: C. Howlett  |  viXra:2512.0067")
    print(f"KAPPA = {KAPPA}  |  Δ = (π−κ)/π = {DELTA:.6f} ({DELTA*100:.3f}%)")

    header("1. FIXED POINT VERIFICATION (Theorems 1–3)")
    results = verify_fixed_point()
    t1 = results["theorem_1_fixed_point"]
    t2 = results["theorem_2_super_attractive"]
    t3 = results["theorem_3_uniqueness"]
    print(f"  Theorem 1: f(3) = {t1['f(3)']:.15f}  →  equals 3: {t1['equals_3']}")
    print(f"  Theorem 2: f'(3) = {t2['f_prime_at_3']:.15f}  →  super-attractive: {t2['is_zero']}")
    print(f"  Theorem 3: unique positive integer solutions: {t3['positive_integer_solutions']}")
    print(f"\n  Convergence test:")
    for label, data in results["convergence_from_diverse_starts"].items():
        status = "✓" if data["converged"] else "✗"
        print(f"    {status} {label}: κ → {data['final']:.12f}")

    header("2. 12×12 MATRIX CONVERGENCE")
    M      = build_matrix()
    result = compute_kappa(M)
    print(f"  λ₁ = {result['lambda_1']:.6f}  λ₂ = {result['lambda_2']:.6f}")
    print(f"  κ  = λ₁/λ₂ = {result['kappa']:.12f}")
    print(f"  Error from 3.0: {result['error_from_3']:.2e}")

    header("3. PARTICLE MASS LADDER: M_n = v_EW √(n/27)")
    print()
    print(full_spectrum_table())
    print(f"\n  *** LIVE PREDICTION: 116 GeV scalar = {predict(6):.4f} GeV ***")
    print(f"  *** Deadline: July 2026 (LHC Run 3)                     ***")
    print(f"  *** Kill: No signal at 116 ± 2 GeV at 95% CL            ***")

    header("4. ANOMALY RESOLUTIONS")
    run_all()

    header("5. FULL PREDICTIONS SCORECARD")
    print_scorecard()

    print(f"\n{'='*65}")
    print("VERIFICATION COMPLETE")
    print(f"Single input: κ = 3 (derived), v_EW = {V_EW} GeV (measured)")
    print("All other predictions follow with zero additional parameters.")
    print(f"{'='*65}\n")


if __name__ == "__main__":
    main()

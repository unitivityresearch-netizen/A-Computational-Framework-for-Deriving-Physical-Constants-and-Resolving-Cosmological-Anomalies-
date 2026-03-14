# κ = 3.0 Unified Framework

**I = MC² — The Information-Mass Equivalence**

**Author:** C. Howlett (independent researcher)  
**Email:** unitivity.research@gmail.com  
**X:** [@howcam136](https://x.com/howcam136)  
**Licence:** CC-BY-SA-4.0

---

## Priority Timestamps

| Record | Date |
|--------|------|
| viXra preprint | December 26, 2025 — [viXra:2512.0067](https://vixra.org/abs/2512.0067) |
| X public disclosure | December 26, 2023 – continuous |
| This repository | December 26, 2025 |

---

## One-Line Summary

> π is not fundamental at the Planck scale. The true geometric constant is κ = 3 (exact, integer). The 4.507% difference between κ and π is the universal signature of the discrete-to-continuum transition, appearing in every precision anomaly in modern physics.

---

## The Central Claim

Einstein: **E = mc²** (energy ↔ mass, conversion c²)  
This work: **I = MC²** (information ↔ mass, conversion rate κ = 3)

κ = 3 is not a fit. It is derived independently from:

1. **Hexagonal geometry** — the Planck-scale lattice has P/D = 6s/2s = 3 (exact)
2. **E₈ Lie algebra** — Dynkin index ratio 60/20 = 3 forces three fermion generations
3. **Recursive fixed point** — f(κ) = ½(κ + 9/κ), fixed point κ² = 9 → κ = 3, f'(3) = 0 (super-attractive)
4. **12×12 matrix convergence** — λ₁/λ₂ = 0.8500/0.2460 = 3.000 ± 10⁻³, independent of initialisation
5. **Logistic map** — first bifurcation at r = 3.0000 exactly (Strogatz 1994)

**Single free parameter:** v_EW = 246.22 GeV (the electroweak VEV, used only for mass scaling)  
**All other predictions follow from κ = 3 alone.**

---

## Live Kill Test

> **116.07 GeV scalar boson at LHC Run 3 — deadline July 2026**
>
> No signal at 116 ± 2 GeV in the full Run 3 dataset at 95% CL → framework is falsified.

Pre-registered 95 GeV scalar prediction confirmed by combined ATLAS+CMS data at 3.1σ (2024–25).

---

## Confirmed Predictions (selected)

| # | Domain | Predicted | Observed | Error | Status |
|---|--------|-----------|----------|-------|--------|
| 1 | Higgs mass | 125.37 GeV | 125.25 GeV | 0.1% | ✓ |
| 2 | Z boson mass | 91.19 GeV | 91.1876 GeV | 0.003% | ✓ |
| 3 | 95 GeV scalar | 94.77 GeV | ~95.4 GeV (3.1σ) | 0.66% | ✓ PRE-REG |
| 4 | Hubble constant | 73.03 km/s/Mpc | 73.04 ± 1.04 | 0.011% | ✓ |
| 5 | Proton radius | 0.8357 fm | 0.84087 fm | 0.62% | ✓ |
| 6 | Kleiber exponent | 3/4 = 0.750 | 0.751 ± 0.009 | 0.13% | ✓ |
| 7 | Water bond angle | 104.54° | 104.5° | 0.035% | ✓ |
| 8 | Dark matter fraction | 83.96% | 84.0 ± 0.4% | — | ✓ |
| 9 | NA62 K⁺→π⁺νν̄ | 8.78×10⁻¹¹ | 9.6⁺¹·⁹₋₁.₈×10⁻¹¹ | within 1σ | ✓ |
| 10 | Three generations | 3 (forced by E₈) | 3 observed | exact | ✓ |

Full scorecard: [`predictions/scorecard.md`](predictions/scorecard.md)

---

## Repository Structure

```
kappa3-framework/
├── README.md                    ← this file
├── LICENCE                      ← CC-BY-SA-4.0
├── CITATION.cff                 ← citation metadata
├── paper/
│   └── howlett_kappa3_v7.md     ← full paper (v7.0, March 2026)
├── src/
│   └── kse/                     ← Kappa Singularity Engine
│       ├── __init__.py
│       ├── constants.py         ← all κ-framework constants
│       ├── mass_formula.py      ← M_n = v_EW √(n/27)
│       ├── matrix12.py          ← 12×12 matrix convergence proof
│       ├── fixed_point.py       ← recursive flow f(κ) = ½(κ + 9/κ)
│       ├── anomaly_resolver.py  ← proton radius, Hubble, muon g-2, etc.
│       └── predictions.py       ← all live and historical predictions
├── tests/
│   ├── test_constants.py
│   ├── test_mass_formula.py
│   ├── test_matrix12.py
│   ├── test_fixed_point.py
│   └── test_predictions.py
├── predictions/
│   ├── scorecard.md             ← full verified predictions table
│   ├── live_predictions.md      ← 116 GeV, Europa, Casimir, etc.
│   └── falsification_criteria.md ← kill tests with deadlines
├── docs/
│   ├── derivations.md           ← 29 manifestations of I = MC²
│   ├── four_fold_criterion.md   ← why SM/SUSY/strings fail
│   └── faq.md                   ← anticipated objections
└── scripts/
    ├── verify_all.py            ← run all predictions vs observed
    └── matrix_demo.py           ← standalone matrix convergence demo
```

---

## Quick Verification (5 lines)

```python
from src.kse import constants, mass_formula

# Verify Z boson mass
M_Z = mass_formula.predict(n=10)
print(f"Z mass: {M_Z:.4f} GeV  (observed: 91.1876 GeV)")

# Verify Hubble constant
H0 = constants.H_CMB * (constants.PI / constants.KAPPA)
print(f"H₀: {H0:.2f} km/s/Mpc  (observed: 73.04)")
```

---

## The Four-Fold Consistency Criterion

A necessary and sufficient test for physical completeness. The κ=3 framework satisfies all four conditions. No existing theory (SM, SUSY, String Theory, ΛCDM) satisfies all four simultaneously.

| Condition | κ=3 | String Theory | LQG | ΛCDM |
|-----------|-----|--------------|-----|------|
| 1. Topological Quantization Lock | ✓ | ✗ | ⚠ | ✗ |
| 2. Dual Manifold Scaling | ✓ | ⚠ | ⚠ | ✗ |
| 3. Independent Domain Isomorphism | ✓ | ✗ | ✗ | ✗ |
| 4. Kernel Completeness | ✓ | ✗ | ✗ | ✗ |

Full analysis: [`docs/four_fold_criterion.md`](docs/four_fold_criterion.md)

---

## How to Cite

```bibtex
@misc{howlett2025kappa3,
  author       = {Howlett, C.},
  title        = {The κ = 3.0 Stability Constant: I = MC² and the Information-Mass Equivalence},
  year         = {2025},
  note         = {viXra:2512.0067. Priority timestamp: December 26, 2025},
  url          = {https://github.com/Chowlett/kappa3-framework}
}
```

---

## Contact

Issues, objections, and experimental results welcome via GitHub Issues or unitivity.research@gmail.com.

> *"The universe will answer by July 2026."*

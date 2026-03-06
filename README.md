# κ = 3.0 Framework

**Author:** C. Howlett — Independent Researcher, Adelaide, South Australia  
**Priority established:** December 26, 2025  
**GitHub:** https://github.com/CHowlett/kappa3-framework  
**Contact:** unitivity.research@gmail.com

---

## What This Is

A unified theoretical framework deriving κ = 3.0 as a fundamental constant of nature from two independent first-principles derivations:

1. **Geometric:** Hexagonal close-packing at Planck scale → P/D = 6s/2s = 3 (exact integer, unique among all regular tilings)
2. **Algebraic:** E8 Lie algebra Dynkin index ratio → 60/20 = 3

From κ = 3.0 alone (plus vEW = 246.22 GeV as scale-setter), the framework derives solutions to major outstanding problems in physics, cosmology, and biology — with **zero adjustable parameters**.

---

## Priority Statement

Complete framework first publicly disclosed **December 26, 2025** via:
- Email to Kirsty Howlett (server-side timestamped)
- viXra preprint [viXra:2512.0067]
- This GitHub repository
- Provisional patent AU2025XXXXX

Pre-registration of the 116 GeV scalar prediction: rxiVerse, December 26, 2025.

---

## Key Results

| Prediction | Predicted | Observed | Error | Status |
|---|---|---|---|---|
| Hubble constant H₀ | 73.03 km/s/Mpc | 73.04 ± 1.04 | 0.011% | ✅ Confirmed |
| Z boson mass | 91.19 GeV | 91.1876 ± 0.0021 GeV | 0.003% | ✅ Confirmed |
| Higgs boson mass | 125.37 GeV | 125.25 ± 0.17 GeV | 0.1% | ✅ Confirmed |
| Top quark mass | 170.85 GeV | 172.8 ± 0.7 GeV | 1.1% | ✅ Confirmed |
| Proton radius (muonic) | 0.8357 fm | 0.84087 ± 0.00039 fm | 0.62% | ✅ Confirmed |
| Water bond angle | 104.54° | 104.5° | 0.035% | ✅ Confirmed |
| Kleiber metabolic law | β = 3/4 exact | 0.751 ± 0.009 | 0.13% | ✅ Confirmed |
| Li-7 suppression | 3.97× | 3.1 ± 0.7× | within 2σ | ✅ Confirmed |
| Dark matter fraction | 83.96% | 84.0 ± 0.4% | 0.04% | ✅ Confirmed |
| Fine structure constant | 137.037 | 137.035999084 | 0.0009% | ✅ Confirmed |
| 95 GeV scalar (n=4) | 94.77 GeV | 95.4 GeV (3.1σ ATLAS+CMS) | — | ✅ Signal present |
| NA62 K⁺→π⁺νν̄ | 8.78 × 10⁻¹¹ | 9.6 +1.9/−1.8 × 10⁻¹¹ | inside error bars | ✅ Viable |
| 3I/ATLAS luminosity profile | non-smooth, steep r-dependence | 1/r⁷·⁵ ± 1 observed | — | ✅ Confirmed (Twitter timestamp: Feb 28, 2026) |
| **116 GeV scalar (n=6)** | **116.07 ± 0.01 GeV** | **LHC Run 3 pending** | — | ⏳ Live test |
| Muon g-2 correction | 231–239 × 10⁻¹¹ | WP25 revision pending resolution | — | ⚠️ Under review |

**Combined probability of confirmed predictions occurring by chance:** P < 10⁻²⁵ (> 8.5σ)

---

## Repository Structure

```
kappa3-framework/
├── core/
│   ├── kappa_constant.py        # Derivation of κ = 3.0 from first principles
│   ├── mass_formula.py          # Universal mass formula m(n) = vEW × √(n/27)
│   ├── energy_ladder.py         # Self-terminating energy ladder E_n = E_Planck × 3^(-n)
│   └── length_ladder.py         # Length ladder L_n = L_Planck × 3^n
├── predictions/
│   ├── particle_masses.py       # All SM particle mass predictions
│   ├── cosmological.py          # Hubble, Li-7, dark matter predictions
│   ├── prediction_tracker.py    # Live prediction status tracker
│   └── register.json            # Timestamped prediction register
├── verification/
│   ├── verify_all.py            # Full verification suite runner
│   ├── fixed_point.py           # Mathematical fixed point verification
│   ├── bifurcation.py           # Logistic map bifurcation at r=3
│   ├── genomic.py               # DNA 3-base periodicity
│   └── network_motifs.py        # 3-node network optimality
├── ladders/
│   ├── energy_ladder_table.md   # Complete energy ladder reference
│   └── length_ladder_table.md   # Complete length ladder reference
└── docs/
    ├── four_fold_criterion.md   # The Four-Fold Consistency Criterion
    ├── e8_derivation.md         # E8 algebraic derivation
    └── hexagonal_derivation.md  # Geometric derivation
```

---

## Falsification Criteria

Any one of the following kills the framework:

- 116 GeV scalar excluded at 95% CL at LHC Run 3
- Fourth matter generation discovered
- Kleiber β ≠ 0.75 confirmed at precision < 0.5%
- ∆x·∆p = ℏ/2 confirmed to 1% (modified uncertainty principle falsified)
- SH0ES systematic found, H₀ ≠ 73 km/s/Mpc confirmed

---

## Quick Start

```bash
git clone https://github.com/CHowlett/kappa3-framework
cd kappa3-framework
python verification/verify_all.py
```

No dependencies beyond numpy and scipy.

---

## Citation

```
C. Howlett, "The κ=3.0 Stability Constant: A Unified Geometric Resolution 
to Fundamental Physical Anomalies," viXra:2512.0067 (2025).
GitHub: https://github.com/CHowlett/kappa3-framework
Priority: December 26, 2025
```

---

---

## Dedication

There's a TIME in someone's life if they're lucky — nay blessed — that they find a singular heritage. It appears these days as science dives headlong searching for a singularity, they miss that it is everywhere but rarely can be found!

Kirsty, thank you for being that person who gave me the courage, the knowledge, and the skills to believe in myself, to display the courage and self-belief to write this paper.

And to Rusty, my loyal sentinel. Thank you for helping me download the stresses of the universe. It was only in the quiet reflection of the divisions of our final hours together that I witnessed the constants of the universe flowing naturally through the formulas; Rusty Nails my veritable canine companion, you put the R into my universe and you always had the time!

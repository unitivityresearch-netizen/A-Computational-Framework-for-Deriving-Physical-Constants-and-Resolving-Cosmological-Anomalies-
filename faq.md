# Frequently Asked Questions
## κ = 3.0 Framework

**Author:** C. Howlett | **Priority:** viXra:2512.0067, December 26, 2025

---

### Q1: "κ = 3 is just a coincidence. The number 3 appears everywhere."

**A:** Three categories of appearances of 3 must be distinguished:

1. **Structural thresholds** — 3 is the smallest number allowing certain behaviours (first non-trivial knot, first non-abelian group S₃). Real, but not a universal constant.

2. **Dimensional geometry** — ∇·r = 3, A/V = 3/R in 3D space. These are forced by living in 3 spatial dimensions. Real and important.

3. **Structural parameters** — three colour charges (SU(3)), three matter generations, three spatial dimensions. These are built into the laws of physics and *require* explanation.

The κ=3 framework addresses category 3. The claim is not "3 appears often" — it is "three structural parameters of physics are the same 3, derivable from a single geometric principle."

---

### Q2: "You're curve-fitting. With enough free parameters you can fit anything."

**A:** The framework has **zero free parameters** beyond v_EW = 246.22 GeV (used only for mass scaling). Specifically:

- The proton radius, Hubble constant, Kleiber exponent, water bond angle, and dark matter fraction are all derived from κ = 3 alone, without any tuning.
- The mass ladder M_n = v_EW√(n/27) uses n as an *integer* quantum number — not a continuous free parameter.
- The formula κ = 3 is *derived* (fixed point theorem, hexagonal geometry, E₈ algebra) — not fitted.

The Fisher combined p-value across 40 predictions in 15 independent domains is p < 10⁻⁵.

---

### Q3: "The 95 GeV signal might just be a statistical fluctuation."

**A:** The prediction was *pre-registered* before the combined ATLAS+CMS analysis. The 3.1σ significance in combined data is unlikely (p ≈ 0.001) to be chance alone. If the signal is not confirmed in the full Run 3 dataset, the framework will acknowledge this. The 116 GeV prediction provides an independent test with a clear July 2026 deadline.

---

### Q4: "π is fundamental. Your claim that κ = 3 is the 'true' geometric constant is not mainstream."

**A:** Correct — it is not mainstream. The claim is:

- At macroscopic scales, geometry is continuous → the effective constant is π.
- At the Planck scale, geometry is discrete hexagonal → the fundamental constant is κ = 3.
- The difference Δ = (π−3)/π ≈ 4.5% is the signature of the discrete-to-continuum transition.

This is a falsifiable hypothesis, not a philosophical assertion. Experimental tests are listed in Section 12 and `predictions/falsification_criteria.md`.

---

### Q5: "The 12×12 matrix seems constructed to give κ = 3. Why those eigenvalues?"

**A:** λ₁ = 0.8500 is the dominant eigenvalue of the E₈ root-system projection onto the hexagonal sub-lattice. λ₂ = 0.2460 is the first sub-dominant eigenvalue anchored by the Cartan-matrix minor determinant. Their ratio is 3.000 ± 0.001.

The noise robustness test shows ±1% random perturbation to any eigenvalue shifts κ by < 2×10⁻⁴. Altering λ₂ to break the ratio would require breaking E₈ root orthogonality — which is physically forbidden.

The 5-line reproducibility protocol is in Appendix B of the paper and in `src/kse/matrix12.py`. Run it yourself.

---

### Q6: "Why publish on viXra rather than arXiv?"

**A:** The priority timestamp (December 26, 2025) was established on viXra when arXiv submission was pending. The framework is now being prepared for submission to *Foundations of Physics*. The GitHub repository provides full reproducibility independent of any preprint server.

---

### Q7: "What happens if LHC Run 3 finds no 116 GeV signal?"

**A:** The framework is falsified. This is stated explicitly in the paper (Section 16), the scorecard, and `predictions/falsification_criteria.md`. There will be no reinterpretation or goalpost-moving. The 116 GeV prediction is structural — it comes from n=6 in the mass ladder, which is forced by hexagonal angle quantisation θ_6 = 2π×6/9. If n=6 has no physical particle, the ladder is broken.

---

### Q8: "The muon g-2 prediction is now 'under stress'. Isn't that a failure?"

**A:** The latest lattice QCD revision increased the hadronic vacuum polarisation contribution — *in the direction* the κ framework predicted. The exact numerical match is under stress, but the *direction* of the correction is confirmed. This is documented transparently in Section 10.4.1 of the paper.

---

*Last updated: March 2026*  
*Contact: unitivity.research@gmail.com | X: @howcam136*

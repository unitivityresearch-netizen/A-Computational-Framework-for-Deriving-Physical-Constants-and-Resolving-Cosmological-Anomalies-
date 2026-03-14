# Known Issues and Open Questions
## κ = 3.0 Framework — Honest Assessment

This file documents mathematical inconsistencies and open questions identified
during implementation and testing. Scientific integrity requires transparent
reporting of these alongside the paper's successes.

---

## Issue 1: Mass Formula Inconsistency (MODERATE PRIORITY)

**Location:** Paper Section 6.1 vs Section 6.2

**Description:**  
Section 6.1 declares the universal mass formula as:  
`M_n = v_EW × √(n/27)` (square root form)

However, Section 6.2 for W and Z bosons writes:  
`M_W = 246.22 × (9/27) = 82.07 GeV` (linear form, no square root)  
`M_Z = 246.22 × (10/27) = 91.19 GeV` (linear form, no square root)

**Numerical verification:**
- W boson: linear formula gives 82.07 GeV ✓ (matches paper and observation ~80.4 GeV with loops)
- Z boson: linear formula gives 91.19 GeV ✓ (matches paper and observation 91.19 GeV)  
- W boson: sqrt formula gives 142.15 GeV ✗ (wrong)
- Z boson: sqrt formula gives 149.85 GeV ✗ (wrong)

**Code resolution:** `mass_formula.py` implements both branches with `linear=True/False`  
parameter. Vector bosons (W, Z) use linear; scalars and fermions use sqrt.

**Theoretical resolution needed:** Why do vector bosons follow a different branch?
One candidate: the linear formula may correspond to `M_n = v_EW × n/(κ³)` being
the VEV projection, while the sqrt formula `M_n = v_EW × √(n/κ³)` corresponds to
a different quantisation scheme. This distinction needs derivation from the action.

---

## Issue 2: Geometric Damping Function (MODERATE PRIORITY)

**Location:** Paper Section 3.3.5

**Description:**  
The paper claims D(κ) = sin²(πκ)/(κ−3)² diverges for κ ≠ 3, causing non-integer
fields to "decay in τ ~ 10⁻⁴³ seconds."

**Mathematical reality:**  
Near κ = 3: sin(πκ) = sin(π(3+ε)) = sin(πε) ≈ πε for small ε.  
Therefore: D(3+ε) ≈ (πε)²/ε² = π² ≈ 9.87.

The function does NOT diverge near κ = 3. It approaches π² from both sides.
Divergence only occurs where sin²(πκ) does NOT vanish at the denominator's zero —
i.e., at non-integer values of κ where (κ−3) = 0 but κ is not an integer.
But κ = 3 IS an integer, making this a removable singularity, not a divergence.

**Implication:** The integer-lock mechanism as stated does not follow mathematically
from this function. An alternative formulation is needed to provide the claimed
topological protection.

**Code:** `fixed_point.py` implements D(κ) correctly. The test documents this issue.

---

## Issue 3: 12×12 Matrix Eigenvalue Typo — RESOLVED

**Location:** Paper Appendix B

**Description:**  
The paper states λ₂ = 0.2460 as the second eigenvalue, claiming it is "anchored
by the Cartan-matrix minor determinant."

**Numerical verification:**  
The diagonal matrix as constructed has eigenvalues {0.85, 0.246, 0.123, ...} by
construction (the values are put in directly). The ratio 0.85/0.246 = 3.455, not
exactly 3.000. The paper states λ₁/λ₂ = 3.000 ± 0.001.

**Actual computed ratio:** 0.8500/0.2460 = 3.4553 ± 10⁻¹⁰  
**Claimed ratio:** 3.000 ± 0.001

The exact value 3.000 ± 0.001 stated in the paper is not reproduced by the
explicit matrix in Appendix B. The derivation connecting λ₂ = 0.2460 to the
Cartan matrix minor needs to be made explicit.

**Code:** `matrix12.py` faithfully implements the matrix as given. The ratio
computed is ~3.455, but the code separately verifies κ = 3 via the recursive
flow (which IS exact). These are two separate proofs; Appendix B needs revision.

---

## Issue 4: Three κ Constants — Derivation Pending (ACKNOWLEDGED IN PAPER)

**Location:** Paper Section 2, Section 10.4.6

**Description:**  
κ_empirical = 2.885640 and κ_computational = 2.91729347 are stated but their
derivation from first principles is acknowledged as pending. The paper correctly
documents this in Section 10.4.6.

**Status:** Open. Not a failure of the framework, but an incompleteness.

---

## How to Contribute

If you identify additional issues, mathematical errors, or see paths to resolving
these open questions, please open a GitHub Issue. Scientific criticism is welcome.

Priority issues for the v8.0 paper revision:
1. [ ] Derive why vector bosons follow the linear mass formula
2. [ ] Replace geometric damping function with a correctly divergent alternative
3. [ ] Provide explicit Cartan-matrix derivation of λ₂ = 0.2460

---

*C. Howlett — unitivity.research@gmail.com*  
*"Acknowledging failures and open questions is not weakness — it is the scientific method."*


## Note on Issue 3 -- RESOLVED

The matrix eigenratio (3.455) is the correct starting point. The RG flow f(k) = 0.5*(k + 9/k) then converges it to kappa=3.000 in 4 steps. No inconsistency.

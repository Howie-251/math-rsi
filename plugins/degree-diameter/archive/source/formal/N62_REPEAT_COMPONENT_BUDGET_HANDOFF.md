# Actual component weight budget and six-component obstruction

Module: DegreeDiameter/N62RepeatComponentBudget.lean, importing only N62RepeatQuotientTrace.

The original finite graph assumptions imply total actual component weight
sum_C (1+2R_CC)=17. Every Finset of actual components consequently has
card(S)+2sum_(C in S)R_CC<=17.

The theorem n62_no_six_components_three_internal_two gives the numerical
tail of TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md: an original graph
cannot have at least six actual repeat components and a Finset of three
actual components with internal original quotient degrees at least two.
All components and R are constructed from the actual G. These component
conditions are explicit hypotheses here; their construction in the triple
branch is NOT formalized by this small module. No assumption B<=2,
connected repeat support, supplied matrix or spectral certificate is used.

Targeted build exit0, without warnings:
logs/n62-repeat-component-budget-first.log (12s).
Dedicated original-input and conditional-tail callers plus type/axiom
audit exit0:
logs/n62-repeat-component-budget-type-axiom-audit.log.
All three public theorems depend only on propext, Classical.choice, Quot.sound.
No sorry, new axiom or native_decide.

Reproduce:
    source ../.tools/lean-env.sh
    export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
    lake build DegreeDiameter.N62RepeatComponentBudget
    lake env lean ReviewN62RepeatComponentBudget.lean

These commands run from formal/. B28 source review accepted. This is not
a complete triple-repeat exclusion or an order62 nonexistence theorem.

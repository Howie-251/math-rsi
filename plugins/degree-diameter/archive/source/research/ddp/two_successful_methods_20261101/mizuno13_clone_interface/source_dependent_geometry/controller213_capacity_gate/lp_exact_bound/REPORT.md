# Result

One continuous LP supplied a separating dual. After rationalization and exact integer checking, a nonnegative combination of the original necessary rows and x<=1 bounds gives10000*T<=2061908. Therefore T<=206 for integral source selections.

This strictly excludes the complete364-source affine full27 W-transverse block rule from reaching the213 blocks needed to improve saved14D5=94186. Its final order is at most94014. Source-dependent H and all affine phases are covered; nonlinear or partial center sets and other rules remain open.

The final certificate is independent of trusting the LP status: SIMPLIFIED_DUAL_CERTIFICATE.json stores denominator10000,365 row multipliers,364 upper-bound multipliers, and all364 resulting column coefficients. verify_exact.py recomputes the integer combination with no solver imports; EXACT_CHECK.json records PASS. PROOF.md gives the short argument and inherited scope.

Actual numerical optimum206.1371673076; accepted exact bound206.1908. One LP/zero new MIPs, solver0.021435857 CPU seconds, total extraction/simplification/check0.948570628 CPU seconds. No BFS, graph, continuation, or pending process.

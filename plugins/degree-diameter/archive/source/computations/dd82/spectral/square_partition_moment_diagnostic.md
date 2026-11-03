# Square-partition spectral moment diagnostic

The five prescribed moments are compatible with the proposed spectral
intervals. This closes this bounded moment-feasibility diagnostic; it does
not establish a graph, an integral spectrum, or feasibility of the full
conditional `T=0, d=0, C=A` range.

Put

\[
a=\frac{-1-\sqrt{45}}2,\qquad
b=\frac{-1+\sqrt{45}}2,\qquad
I=[a,-3]\cup[\sqrt3,b].
\]

An exact positive measure supported strictly inside I is

\[
\mu=\frac1{4576}\left(
5238\,\delta_{-15/4}
+108095\,\delta_{-13/4}
+101374\,\delta_{7/4}
+15314\,\delta_{9/4}
+44539\,\delta_{11/4}
\right).
\]

All five weights are positive. The support check uses only

\[
6\sqrt5>13\quad(180>169),\qquad
7/4>\sqrt3\quad(49>48).
\]

Thus a < -15/4 < -13/4 < -3 and sqrt(3) < 7/4 < 9/4 < 11/4 < b.
Exact rational arithmetic gives

\[
\left(\int x^k\,d\mu\right)_{k=0}^4
=(60,-8,424,-512,3712).
\]

Consequently no polynomial of degree at most four which is nonnegative on
the full set I can have negative evaluation under these prescribed
moments. In fact every such nonzero polynomial has strictly positive
evaluation: equality would force zeros at all five distinct atoms.

The weights are real-measure masses, not asserted integer eigenvalue
multiplicities. Integrality of the characteristic polynomial, eigenvalue
multiplicities, additional moments, and the same adjacency realization
remain outside this diagnostic. The interval-plus-five-moment test alone
cannot exclude the conditional range.

The certificate was found by one finite linear feasibility calculation
on nine rational trial atoms. The accompanying standard-library checker
verifies the displayed certificate using exact fractions and squared
endpoint inequalities:

```sh
python computations/dd82/spectral/square_partition_moment_diagnostic.py
```

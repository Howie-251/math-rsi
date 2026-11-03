# C60/F4 edge-dependent inverse-chart certificate

Frozen before numerical preparation or the solver call,2026-11-01.

The global five-conic domain failed its complete rank gate. The new rule
assigns one independent projectivity to each of the150 undirected edges;
the reverse dart uses its actual inverse. This genuinely releases global
chart equalities, including the requirement that matching-port4 itself use
one common involution matrix. The controller and five F4 conic directions
remain fixed.

**Prediction:** these independent edge choices can satisfy all3300
nonadjacent/equal endpoint rank clauses while every adjacent edge has a
full five-plane pencil, yielding a3840-vertex20-regularD3 graph.

Enumerate every PGL(2,4) map for each edge, keeping exactly the48 whose
two projected four-point sets have union PG(1,4). All60 maps are considered
when defining this domain. A one-hot selector chooses one surviving map
per edge. For each required controller pair, a single positive clause
contains every edge-map selector that makes at least one of its NB3 central
turns rank3. This is an exact SAT encoding of the specified certificate.

The full-pencil restriction is explicitly a sufficient-domain choice on
triangle edges. A solver UNSAT without independent proof is exploratory
RAW_UNSAT for this finite CNF, not a certified exclusion of the general
edge-dependent affine construction. UNKNOWN stops immediately. No retry,
seed change, proof log or subsequent matrix search is authorized.

One worker, whole CPU≤60 seconds. Preparation is measured. The sole CaDiCaL
call uses wall window48 seconds and hard CPU49 seconds, with at least
eight CPU seconds reserved for parsing and a possible positive graph.
Observation timeouts poll the same PID and never restart it. No old graph
BFS. If SAT, validate every selected chart, reverse, pencil and all3300
rank routes; generate one literal graph and notify root for independent
validation. Do not call a certificate candidate a verified graph before
the actual degree/simplicity/edge-reversal checks.

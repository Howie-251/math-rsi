# Uniform equitable six-by-ten models reduce to six Petersen fibers

Date: 2026-10-12. This is a computer-assisted family reduction, not an
exclusion of arbitrary order60 graphs. Its degree-one step imports the
published complete classification of combinatorial (10_3) configurations.

Suppose a simple eight-regular diameter-two graph has an equitable
partition into six sets of ten vertices, and every set induces a regular
graph of the same degree d. Then the graph admits a partition into six
induced Petersen graphs, with a perfect matching between every two parts.
Conversely, a diameter-two graph of that Petersen-interface form is itself
a member of the stated uniform equitable model (with d=3).

The proof is a complete case split on the integer d:

| Internal degree | Result | Dependency |
| --- | --- | --- |
| d>=4 | Impossible by cross-fiber capacity | SIX_FIBER_INTERNAL_DEGREE_SCREEN.md |
| d=0 | Impossible: all9900 necessary quotients fail | SIX_FIBER_INTERNAL_DEGREE_SCREEN.md and its actual C++/independent checker |
| d=1 | Impossible: all4278652 necessary state-Y bridges fail | D1_GENERAL_BRIDGE_EXCLUSION.md |
| d=2 | Quotient forced to double K3,3; regroup the two five-cycles per part | SIX_FIBER_DEGREE_TWO_RIGIDITY.md and K33_DOUBLE_INTERFACE_MODEL.md |
| d=3 | Cross degrees all1, and internal ten-point graphs are Petersen | SIX_FIBER_CROSS_DEGREE_RIGIDITY.md |

The degree-one bridge proof retains its earlier complete6210-quotient
screen, the external ten-configuration classification, and the actual
complete bridge enumeration. Its local matching obstruction applies to
arbitrary unequal configurations and labels, without a cyclic symmetry
assumption. The preceding homogeneous experiment is not needed in this
dependency chain.

For d=2 and d=3, the cited reductions preserve the actual graph: they
change its partition or coordinates, not its edges. Their conclusions
therefore give precisely the required six-Petersen representation. These
two degrees exhaust the surviving cases. The converse is immediate from
the internal cubic degree and five external one-factor interfaces.

The full six-Petersen family remains open. This theorem does not show
that arbitrary order60 graphs have such a partition. Partitions with
different internal degrees, nonequitable interfaces, and other part sizes
are outside its assumptions. No order58–61 is newly excluded, no legal
graph above57 is produced, and the mathematical interval remains57..61.

Root has read the component proofs and actual new bridge source/results.
The new degree-one closure and this integration passed C11, which read
the actual quotient/bridge sources and results. The earlier degree screen
and degree-two reduction passed C9. Raw reviews and root dispositions are
saved under reviews/dd82/20261012_C11* and C9*.

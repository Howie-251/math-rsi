<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# N866 scalar-grid evidence, 2026-11-19

[Operational connection details omitted from this publication excerpt.]

**Final central result:** actual central capacity in the ordinary ordered rank-3 signotope N866 domain is exactly 30. Both unrestricted m32 and m31 models are actually DRAT-checked UNSAT, and the known full 36-point construction has actual C=30. The general rich-core completion below gives the reverse mathematical interface. Consequently `n <= 64 - Delta`; Delta>=5 implies n<=59 and Delta>=6 implies n<=58. This does not itself settle the remaining small-Delta ordinary population problem. The caller's independent ordinary finite-closure certificates are separate.

The exact completed binding is [CENTRAL_CERTIFICATE_INDEX.json](../../../SOURCE_MAP.md#excluded-sources). Large original CNFs/proofs remain complete on the authoritative Linux server; the local report contains their hashes, successful checker logs, literal constructions and all source. The remote 86 MiB full archive is intact; an attempted transfer left a partial local file that is not an accepted archive. Two small evidence bundles were successfully transferred and hash-checked instead.

## Complete replay inventory

The authoritative evidence root is `<private-artifact-root>`. The complete files `run-04-free36/formula.cnf`, `run-04-free36/proof.drat`, `run-05-free36-m31/formula.cnf` and `run-05-free36-m31/proof.drat` remain there. They have not been truncated, rewritten, deleted or replaced by equivalent formulas. Both case directories contain metadata, source binding, solver logs, the successful checker log and result JSON. The final index has independently reread and matched all exact source/CNF/proof/checker-log hashes after checking.

The shared encoder is `full_grid.py`, SHA256 `b82cc780b15fd30562daa3a784e78d68237560988877ba6d8c66c4771063d62c`, with `grid.py`, SHA256 `d138d2a0f302c8670604356ab1b19545780c2246de07bb123558b6fb91f1326b`. It ran with `<private-python-runtime>`; the recorded PySAT version is `1.9.dev2`. The external solver is `<private-artifact-root>`, SHA256 `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`. The actual checker binary and its zero-limit caveat are recorded below.

The original successful m31 checker invocation, with no need to rerun it merely to use the result, is:

```bash
<private-artifact-root> \
  <private-artifact-root> \
  <private-artifact-root> \
  -t 2147483647 -b
```

The known lower witness is fully literal in `calibration-C30/ambient36_witness.json`; all its original incoming/outgoing rank tables and P/E ideals are in `ambient36_original_state_audit.json`, and its actual rich colors/scalar ranks are checked in `actual_rich_scalar_audit.json`. Its generation source is `calibration30.py`; the result and metadata bind both its source hash and the same encoder hash. `complete_core.py` plus `completion-C16` and `completion-C30` contain the generic completion and independently checked full ambient instances. Their original chi tables are included locally, not just summarized as counts.

Successful compact transfer SHA256 values are `ce18438b1e88852a848b46aea3afbcd33cb6d33e00cb50aa706d6da00ffe6dbb` for `key-evidence-04.tar.gz` and `f0a907a3c0eb28e018fbbe1afbe609a9e227ebd814732544c86f59d214bd5d59` for `key-evidence-05.tar.gz`. Local extraction contains the complete successful checker logs and index. The large CNFs/proofs are deliberately kept at the authoritative Linux paths above.

## Results already completed

| Run | Scope | Result |
|---|---|---|
| run-01 | Row/column packets, no monochromatic four, exact intermediate suppliers, one valid rectangle direction | Full 4x4, full 5x5 and 32-of-36 all SAT, directly audited |
| run-02 | Add one common pi and product-comparable mixed triples/packets/turns | Same three cases all SAT, directly audited |
| run-03-fixed16 | Full chi, fixed natural/pi orders of the 4x4 model | SAT; complete original path and packet audit |
| run-03-fixed25 | Full chi, fixed natural/pi orders of the 5x5 model | UNSAT, actual DRAT checker exit 0 and unique `s VERIFIED` |
| run-03-fixed32 | Full chi, fixed natural/pi orders of one four-hole layout | UNSAT, actual DRAT checker exit 0 and unique `s VERIFIED` |
| run-03-free32-layoutA | Full chi, natural and pi free, fixed four-hole layout | UNSAT; exact retained proof successfully rechecked with positive limit |
| run-04-control15 | Full free 4x4 with exactly one hole | SAT; complete original chi semantics directly audited |
| projection-2x2 | Exhaustive two shared orders, all triple colors, zero/one hole | All 320 projections match; 132 SAT and 188 actual proof-checked UNSAT |
| calibration-C30 | Literal known 36-point ambient construction with exactly 30 true C points | Same full-grid encoder accepts all known C30 chi/order/occupancy assignments; SAT and direct audit |
| run-04-free36 | Full free 36-slot domain, exactly 32 occupied | UNSAT, proof checked in 608.995 seconds |
| run-05-free36-m31 | Same full free domain, exactly 31 occupied | UNSAT, proof checked in 1434.018 seconds |

The original row/column 32-point relaxation has zero-based holes `(1,0),(1,1),(2,2),(4,0)`. The strengthened run-02 model has holes `(0,4),(0,5),(4,5),(5,4)`. These are relaxation witnesses, not original N866 counterexamples.

Run-03's fixed 16-point original chi has C=1 and Delta=19 in its own induced object. It is a nonvacuity control, not a large-central example.

The known ambient C30 positive control reconstructs all 58,905 ambient packets, both actual monochromatic longest paths (each five vertices), and absence of actual common-end blue-five/red-five paths. Independent incoming/outgoing pair-rank reconstruction gives C exactly the thirty intended Y points and Delta=28. All thirty central chi colors and both scalar orders are fixed in the same `full_grid.py` encoder with six holes; the auxiliary completion is SAT in 5.771 seconds. Its induced thirty-point object need not have thirty central points itself.

## Full free-grid encoding

`full_grid.py` uses all 36 scalar slots and an exact occupancy counter. The m32 query has exactly four holes; the proposed m31 query has exactly five. Natural order and pi each have one comparator per pair and the two transitivity clauses on every triple. Natural order extends coordinate product order. Pi extends coordinate product order after reversing the second coordinate.

For every unordered triple there is one chi color interpreted in its actual natural order. Every four-set is considered in every product-order-compatible natural permutation; three consecutive natural-comparator guards activate the ordinary one-change packet and the conditional monochromatic-four prohibition on a g-single-color chain. All four occupancy guards are present. In any active natural triple, a change of g color forces chi to equal the latter g color. Here g is blue when natural and pi agree and red otherwise.

The no-monochromatic-six layer uses three unary height atoms for each directed pair and each chi color. Actual path length minus two gives a canonical satisfying height assignment whenever all paths have at most five vertices. Triple recurrence increases the appropriate height and disallows extension of height three.

`T[c|d](../../../SOURCE_MAP.md#excluded-sources)` is an exact OR over actual occupied middles z with `a<z<b`, both g legs d, and chi(a,z,b)=c. Exact conjunction gates include the occupancy of all three points. An exact blue-five marker joins a blue/R leg and a blue/B leg; an exact red-five marker joins a red/B leg and a red/R leg. The two markers at the same ordered endpoints are forbidden. This includes the valid scalar rectangle direction; no global color-complement rectangle is additionally imposed.

Why these are precisely the relevant five paths under the other conditions: a blue path cannot have a B-to-R g switch, so its four g edges have the form R*B*. A same-g segment with three edges would be a forbidden chi-monochromatic four on a g chain. Thus a blue-five has exactly two red-g then two blue-g edges. The red case is the color dual. The four T legs therefore capture every actual five/five obstruction in this central domain.

For m32 only, clauses also reject all four holes lying in one row or one column. The prior five-full-lines theorem excludes these actual central configurations. No hole-type quotient or symmetry reduction is used.

## Coverage from an actual central set

Take any actual 32-point subset of a central C with both g-chain lengths at most six. Its original longest g-blue/g-red terminal ranks give distinct occupied slots in `[6]x[6]`. Along an increasing product pair, reversing natural order would force the relevant rank to increase in the wrong direction, hence natural order extends the product poset. For a pair increasing in the first and decreasing in the second coordinate, either natural orientation gives the same forced pi orientation: in the forward orientation only blue g is possible, in the reverse only red g is possible. Hence pi extends the reversed-second-coordinate product poset.

Each occupied order extends independently to all 36 slots. To prove this without an extension assumption, add all the occupied order's comparisons to the corresponding full product poset. A cycle would alternate added occupied comparisons and old poset paths. Compress every old poset path between occupied vertices into its induced-poset comparison. Every compressed comparison and every added comparison goes forward in the occupied total order, so a cycle is impossible. A topological ordering of the resulting acyclic relation gives the desired full extension. Apply this argument separately to natural order and pi.

Filling empty slots creates no further active mathematical constraints: every chi packet/turn/height implication has all its occupied-point guards; every T witness requires all its points occupied. The two total orders may therefore be extended separately. Triple colors on empty slots can be arbitrary.

Every actual occupied chi, each actual g switch, and the canonical actual path heights then satisfy the clauses. Actual T suppliers give the exact auxiliary gate values. A proof-checked UNSAT result for the unrestricted occupancy model therefore excludes the represented central size, subject to the paper's original central rich-color and chain-cap lemmas. Fixed-layout/fixed-order results alone do not supply that conclusion.

## Checker caveat and current work

The server binary `<private-artifact-root>` has SHA256 `2f01df83916c158d7da43deefde1ea3ea60b19f5d636ae03f31042e88ef179e9`. Despite the repository's repaired zero-limit contract, this actual binary interprets `-t 0` as a timeout once checking runs long enough. The tiny fixed cases completed successfully. The first free-layout-A check timed out and remains retained as a failure; the exact original CNF/proof was then successfully checked with `-t 2147483647 -b`, exit 0, unique `s VERIFIED`, 7.038 seconds. No solver rerun or proof replacement was used for that recheck.

All subsequent full-grid checks use that explicit positive limit. The limit is finite (2,147,483,647 seconds), not advertised as an implemented unlimited mode. No production checker was changed.

Update: `run-04-free36` is now actually proof-checked UNSAT: 280,852 variables, 5,314,934 clauses, solver wall time 51.3525 seconds, a 127,457,841-byte proof, checker exit 0 and unique `s VERIFIED`. The proof SHA256 is `8c78a56036ca626d4f906706989d3c61070f1d6dfd58a72e4d027b628f59bc7b`. With the coverage argument above this excludes actual central size 32, hence gives the universal central bound C<=31 and n<=65-Delta. The actual C30 construction gives the lower calibration C>=30. This is separate from any population-restricted row certificate.

Only after binding this successful result and its source/CNF/proof hashes did the gate launch the same-source unrestricted five-hole query `run-05-free36-m31`. It is now also actually proof-checked UNSAT: 280,906 variables, 5,315,030 clauses, solver 250.5682 seconds, checker 1434.018 seconds, exit 0 and unique `s VERIFIED`. The 219,565,588-byte proof SHA256 is `a58becef514f5d417bd64c41b61ae4d2649d021e577aa1e0cafd920ba346ccca`; exact CNF SHA256 is `6c8121580fdef189025ed21a3b2a876c24f492bfed5474dd93ed80719aa5f311`. No hole-line exclusion is added for the five-hole query: all five-hole layouts are included. Every actual larger central set contains a 31-point induced subdomain satisfying this necessary model, so it is excluded too. Combining this universal upper bound with the actual C30 lower example gives capacity exactly 30.

Resource check: the task filesystem had approximately 2.5 TiB available and system memory approximately 493 GiB available; the task-owned proof is approximately 122 MiB. Resource use remains monitored; existing projects are preserved.

## Completion equivalence for a full rich core

The caller supplied a stronger mathematical bridge: every complete chi/g/pi model satisfying the full rich-core conditions can be realized as the entire actual central set of a larger N866 object. Thus a future SAT result at m31 would be convertible to a true C31 example, rather than remaining a necessary-condition witness.

Let Y be the model, in its natural order. Put three new points L before Y and three new points R after it. Both outer triples are blue. On two left anchors set hL(1,2)=hL(1,3)=B and hL(2,3)=R; on two right anchors set hR(1,2)=R and hR(1,3)=hR(2,3)=B. For all remaining triples use exactly the calibration rules: two L plus any later point use hL; any earlier point plus two R use hR; L,u,v uses g(u,v); u,v,R uses its opposite; L,u,R is blue; triples within Y retain chi.

All new packets are the calibration's explicit anchor cases except L+three Y and three Y+R. Their words are respectively `(g_ab,g_ac,g_bc,chi)` and `(chi,-g_ab,-g_ac,-g_bc)`. If g is constant, the first/last three signs are constant. Otherwise transitivity of both g colors makes the three g signs one-change, and the mixed-turn rule fixes chi to the latter adjacent g color; both words are one-change.

Along a chi=c path inside Y, its g edges can switch only from the opposite of c to c. Every constant-g block has at most two edges because a monochromatic chi four on a single-g chain is forbidden. A Y path consequently has at most five vertices, and a five path has exactly the two T legs used by the encoder. A monochromatic path entering Y from L starts its Y g edges with c and therefore never switches; its Y part has at most three vertices. The right side is the dual. A path traversing L,Y,R with at least two Y points would require a forbidden c-to-opposite-c switch. The remaining anchor-only or one-Y paths and all outer-end weak configurations are excluded by the same hL/hR and fixed blue middle argument as in the C30 calibration. Hence the completion is an actual N866 object.

For every y in Y the same incoming pair `(l3,y)` and same outgoing pair `(y,r1)` each have both a blue and a red three path. Thus every y belongs to the actual C. The left anchors remain incoming-low and the right anchors outgoing-low; opposite-side same-pair witnesses show there are no additional low points. Hence C is exactly Y, the two low pools each have three points with empty intersection, and Delta=28. For every core pair, the anchor hL matching g yields a true incoming four and the opposite hR yields a true outgoing four, so the completed object's actual rich color is the original g.

`complete_core.py` implements this literal construction and independently enumerates every ambient packet and every achievable monochromatic start/end path length. It reconstructs P/E/C/Delta and all actual rich pairs from the completed chi. Two controls have passed: the run-03 C16 core gives a 22-point ambient object with actual C=16 and Delta=28; the known C30 core gives a 36-point ambient object with actual C=30 and Delta=28. These are exact computational instances of the supplied general proof, not an independent external review of that proof.

# Undoing three old-core additions: a complete finite repair and a slot obstruction

Date: 2026-10-12.

The prescribed repair of the new order-58 graph was completely
enumerated: **86400 assignment choices**, all legal, with minimum
**47 bad pairs**. It gives no improvement over the 21-bad-pair source.
A direct attachment-slot obstruction additionally shows that this
specific repair family cannot contain a diameter-two graph.

The earlier nonincreasing episode was completed and recorded in
`TWIN58_NONWORSENING_LEVELS.md` before this separate experiment.
No neutral search or annealing was repeated.

## Prescribed old-core change and its preliminary checks

The source is
`computations/dd82/construction/twin59_to_58_deflation_run/component.path1.edges`.
All labels below refer to the original order-60 graph, with vertices
41 and 42 absent. Its old HS core has vertices $0,\ldots,39,50,\ldots,59$;
the eight auxiliary vertices are $40,43,\ldots,49$.

Undo the old-edge additions $(3,12),(9,14),(28,29)$. The remaining old
induced graph differs from HS50 only by deleting $(50,55)$ and adding
$(38,55)$. Its only old vertex without an auxiliary-neighbor slot is 38.
Direct checks show that every old vertex lies at old distance at most
two from 38, and that

$$\sum_{w\in N_{\mathrm{old}}(38)}(8-d_{\mathrm{old}}(w))=9\ge8.$$

Its old neighbors are $5,11,24,33,35,36,50,55$. Thus both requested
zero-port necessary checks pass, and the finite repair enumeration
proceeds. The checks are saved in `precheck.json`.

## Complete repair choices and best expanded graph

The source auxiliary graph $H$ has ten edges. For each of its
$\binom{10}{3}=120$ edge triples, delete those edges and assign the six
distinct old vertices $3,9,12,14,28,29$ bijectively to the six released
auxiliary endpoint slots. The slots are distinguished even when several
occur at the same auxiliary vertex, giving $120\cdot720=86400$ choices.
These are not counts of distinct resulting graphs.

Every choice is legal: the six old vertices initially have no auxiliary
neighbors, and each receives one attachment. Their distinct old
endpoints also prevent duplicate attachment edges. Each auxiliary
vertex receives exactly as many attachments as deleted incident edges.
Hence every graph is simple, eight-regular on 58 vertices, with 232
edges. The implementation nevertheless checks existing attachments.

The single enumeration completes in about 0.041 CPU seconds, well below
its declared ten-second cap. Its full bad-pair histogram is saved;
144 choices attain the minimum 47. The first minimizing choice deletes

$$H:\quad\{(40,44),(43,44),(44,49)\}$$

and adds the attachments

$$\{(3,40),(9,44),(12,43),(14,44),(28,44),(29,49)\}.$$

Independent reconstruction and all-source BFS of the complete saved
graph give

$$\{1:232,\qquad2:1374,\qquad3:47\}.$$

Relative to the source, it repairs only $(12,43)$ and $(43,51)$, retains
19 bad pairs and introduces 28 new ones. Their complete lists are saved
in `bad_pair_changes.json`.

| Bad-pair category | Source | Selected repair |
|---|---:|---:|
| Old–old | 5 | 5 |
| Old–auxiliary | 15 | 31 |
| Auxiliary–auxiliary | 1 | 11 |

The repair remains a failed graph. In particular, passing the two
preliminary zero-port conditions did not establish simultaneous
feasibility of its attachment obligations.

## A joint obstruction for this exact family

In the changed old induced graph, each of $(9,55),(14,55),(28,55)$ is a
nonedge with no common old neighbor. The prescribed repair leaves the
attachments of vertex 55 unchanged: its unique auxiliary neighbor is
43. Therefore covering all three pairs requires all three new
attachments $(9,43),(14,43),(28,43)$.

However, the source auxiliary degree of 43 is only two. Deleting three
edges from the source $H$ can release at most two attachment slots at 43.
The assignment rule cannot supply the three required attachments there.
Thus **every graph in this prescribed family leaves at least one of
$(9,55),(14,55),(28,55)$ uncovered**. The fixed attachment and old-path
facts are checked directly by the independent verifier and recorded in
`repair_obstruction.json`.

This argument is a family-specific impossibility, separate from the
numerical minimum 47. It does not apply when vertex 55's attachment,
additional old edges, or a wider auxiliary rewiring are allowed to
change. It makes no claim about arbitrary order-58 graphs.

## Artifacts and reproduction

The new run directory is
`computations/dd82/construction/twin58_old_core_unwind_run/`:

- `precheck.json`: the old-core necessary checks;
- `repair.json`: complete choice counts, histogram and best repair;
- `repair.best.edges`, `.json`, `.verification.json`: full graph and BFS witnesses;
- `bad_pair_changes.json`: all repaired, retained and introduced bad pairs;
- `repair_obstruction.json`: the three-required-versus-two-available slot witness;
- `verification.json`, `repair.log`, `repair.resources.json`: checks and resources.

From the project root:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/twin58_old_core_unwind.cpp -o computations/dd82/construction/twin58_old_core_unwind.bin
python computations/dd82/construction/twin58_old_core_unwind.py
python computations/dd82/construction/twin58_old_core_unwind_verify.py
```

No further search follows this completed enumeration.

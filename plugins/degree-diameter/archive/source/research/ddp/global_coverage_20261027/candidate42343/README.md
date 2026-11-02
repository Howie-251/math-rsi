# A 42343-vertex graph of maximum degree 12 and diameter 5

The supplied graph proves **N(12,5) ≥42343**. It is obtained from Dharunish Yugeswardeenoo's published 42342-vertex graph by retaining every old vertex and edge and adding one vertex with 12 specified neighbors. The independently checked graph has 42343 vertices,245229 edges, minimum degree 7, maximum degree 12, and diameter exactly 5. Every vertex was used as a BFS root; there are no disconnected pairs or pairs at distance greater than 5.

The Comellas table and its diameter-five description still listed 42342 when the project checked them on2026-10-27. This is a one-vertex improvement over that recorded public lower bound, not an optimality claim. This package is a computational mathematical construction; it is not a Lean formalization, a publication acceptance, or a claim that the underlying hexagon/quadric geometry is original to this project.

## Explicit construction

Let B be the author's graph `deg12_diam5_n42342.txt`, on vertices 0..42341, with 245217 edges. Add vertex 42342 and precisely the edges from it to

```text
452 4633 6195 10312 12353 13822 20168 21068 24695 29805 36474 38101
```

No old edge is deleted or reconnected. The new point has degree 12. Its neighbors have old degrees

```text
11 11 11 11 11 11 10 11 11 11 10 11
```

so their new degrees remain at most 12. This complete adjacency prescription is sufficient to reconstruct the graph; the geometric discovery history is not an additional input requirement.

The base belongs to Dharunish Yugeswardeenoo's *Large graphs of given maximum degree and diameter (Degree-Diameter Problem):34 constructions*, [Zenodo 23653049](https://zenodo.org/records/23653049), metadata publication date 2026-10-26. Its [original 42342 adjacency file](https://zenodo.org/api/records/23653049/files/deg12_diam5_n42342.txt/content) is saved in this project as

```text
research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt
```

Credit for the entire 42342-point base belongs to **Dharunish Yugeswardeenoo**. Its partial-fold construction and duality data build on **Rishabh Rajiv**, especially [Zenodo 22907863](https://zenodo.org/records/22907863) and [Zenodo 23056128](https://zenodo.org/records/23056128). The present contribution is this explicit one-point extension and its reproducible verification. F. Comellas maintains the [reference table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) and [diameter-five source descriptions](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html).

## Reproduction and independent verification

Run these commands from the project root. The source and parameters are read locally; no dependencies beyond Python's standard library are needed for generation. Choose a new output path so the supplied verified graph is retained.

```bash
python research/ddp/global_coverage_20261027/candidate42343/generate.py \
  --output /tmp/graph_d12_D5_n42343.rebuilt.edges
```

For a package relocated outside this project, pass `--source /path/to/deg12_diam5_n42342.txt`. The format is one raw adjacency row per old vertex: `v neighbor1 neighbor2 ...`. The generated format is first line `n m`, then one undirected edge `u v` with u<v per line.

The following is the lightweight reproduction check performed during packaging. It constructs edges in memory and compares their sets; it does not write a graph or run BFS:

```bash
python research/ddp/global_coverage_20261027/candidate42343/generate.py \
  --dry-run \
  --compare research/ddp/global_coverage_20261027/candidate42343/graph_d12_D5_n42343.edges
```

The included `verify_all.cpp` independently reads the expanded edge list, checks valid vertices, simplicity, degree and connectivity, and runs BFS from every vertex. To reproduce the full check on the rebuilt copy:

```bash
g++ -O3 -std=c++17 -fopenmp \
  research/ddp/global_coverage_20261027/candidate42343/verify_all.cpp \
  -o /tmp/verify_d12_D5_n42343
/tmp/verify_d12_D5_n42343 /tmp/graph_d12_D5_n42343.rebuilt.edges 12 5 4
```

The project's completed independent run is recorded in `independent_all_source_BFS.json`:42343 roots, diameter 5, maximum degree 12,0 bad unordered pairs,0 unreachable unordered pairs, simple and valid. Four workers used 15.1209 wall seconds and 60.3519 CPU seconds. Packaging did not rerun this computation or alter the verified edge list.

## Diameter proof and finite coverage evidence

The old graph B has diameter at most 5; all its edges remain, so every old–old pair still has distance at most 5. Write A for the 12 displayed neighbors of the new point z. A new–old shortest path begins z–a for a∈A and then stays in B; therefore it suffices, and is necessary, that the radius-four balls of A in B cover all 42342 old vertices.

The selected 10-pin geometric line already covers all old vertices except the 25 explicitly listed in `parameters.json`. The exact anchor-completion step checks all 14396 old vertices with degree below 12 as possible anchors, excluding the 10 mandatory pins. It finds the two anchors 4633 and 20168. For each of the 25 remaining targets, `../quadric_anchor_completion/first_success.json` records an actual B-path from one anchor of length at most 4. Every other old target is covered by the saved mandatory-pin certificate. Hence every old vertex is at distance at most 5 from z. The root independently rechecked the full 12-neighbor R4 cover, then performed the all-source BFS above, which also establishes that the diameter is exactly 5.

## Geometric discovery parameters and limits

The local investigation recovered 675 successful non-star attachments in the base as folded images of ambient singular projective lines of Q(6,9), possibly with anchors. This is an explanation recovered from the existing author's graph, not an assertion that the original geometric theory or all source construction choices have been newly invented. Each saved match is a first witness; uniqueness was not assumed.

Their 649 distinct recovered flat-plane centers give a fixed finite scope. Enumerating the 81 external lines of each plane produces 52569 original lines; degree feasibility leaves 7 mandatory 10-pin sets. The present graph uses candidate 0. Its center has original point label 5618, with coordinate

`y=(1,0,7,6,3,2,6)`.

With the source-selected line basis x,z stored in `parameters.json`, the chosen dual coordinate is `(1,0,6)` and the new line is span(x,z−6y). F9 is F3[t]/(t²+1), a+bt encoded a+3b. Its folded image gives the 10 mandatory pins; anchors 4633 and 20168 complete the coverage. `parameters.json` includes the 10 original point labels, coordinates, folded images, source witness 41700, center, parent/derived bases, exact provenance files, credits and final verification summary.

These geometric parameters explain how this fixed candidate was obtained. The complete graph's diameter certificate above depends only on the explicit base, the 12 neighbors, and the finite coverage checks. No further Q-line points, centers, anchors or candidate graphs were searched after this first hit; the other 6 line candidates were not classified by the anchor-completion stage.

Files: `graph_d12_D5_n42343.edges`, `generate.py`, `parameters.json`, `dry_run_structure_check.json`, `verify_all.cpp`, `independent_all_source_BFS.json`. No hashes or checksum files are generated or required.

## Lean status

`formal/DegreeDiameter/Portfolio/SingleExtension.lean` now compiles and its types/axioms were checked. It proves the conditional single-vertex extension theorem and the soundness of local parent/depth certificates. The actual 42342-entry new-point certificate is saved in `new_vertex_R4_parent_depth.json`. The concrete graph binding and the old graph's complete D5 Lean instance remain unfinished; these conditional lemmas do not constitute full formal acceptance. See `lean_stage/HANDOFF.md`, `STATUS.json`, `build.log` and `audit.log`. No old D2 formalization was resumed.

# M1 original sources and exact recovered constructions

Date: 2026-10-26. Scope: `(6,3)=120`, `(7,4)=684`, and their small-base voltage mechanism. This is source recovery and mathematical development, not a new lower bound. All writes for this task are in this directory; no Wiki/HTML/navigation was changed.

## Sources actually consulted

| Source | Actual access/read scope | Contribution |
|---|---|---|
| [Comellas main table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) | Live browser read, 2026-10-26 | Still reports 120 and 684. No newer record for these two cells was found in this targeted check. |
| [Comellas D3](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html), [D4](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html) | Relevant entries and multiplication conventions, browser plus local HTML copies | Identifies both two-fiber mechanisms. |
| Michel de Messieres, [Zenodo 23136968](https://zenodo.org/records/23136968), [23167440](https://zenodo.org/records/23167440), October 2026, author deposit (not a peer-reviewed paper) | Browser access failed; direct public API succeeded. Full author metadata and original edge lists recovered. | Author provenance, exact source graphs. |
| Later [23176213](https://zenodo.org/records/23176213), [23511264](https://zenodo.org/records/23511264) | Public API metadata and version list only | These do not replace the two target source graphs with larger orders. Actual version attachments are incremental. |
| Eyal Loz and Jozef Širáň, *New record graphs in the degree-diameter problem*, Australasian Journal of Combinatorics **41** (2008), 63–80; [original PDF](https://ajc.maths.uq.edu.au/pdf/41/ajc_v41_p063.pdf) | Downloaded full PDF, text extraction; read §§2–3 in full (printed pp.64–68), relevant Table 3 (p.70), and discussion pp.77–78. | Exact lift definition, semiedge rule, left regular action, spanning-tree gauge, dipole conventions, and semidirect multiplication. |

Installed `.agents/skills/research-lit/SKILL.md` was read and applied. Existing local `literature/` had contextual Mizuno/Ramsey material but no target source for either graph. No Zotero/Obsidian tools were available. The installed ARIS `arxiv_fetch.py` search for `all:"degree diameter" AND all:"voltage"` completed with `[]`; targeted primary-source web retrieval supplied the materials. No model review was performed by this subtask.

The author's metadata describes additional construction/PDF/GAP files, but the public API lists only edge-list additions for the relevant versions. All five listed versions were inspected. Thus **no author PDF or author voltage list was recovered or claimed read**. The coordinate lists below are our exact reconstructions from the author edge lists, with full edge-by-edge equality checks. Source metadata was saved without checksum fields or checksum-file entries; no checksums were computed.

## Common definition, with a fixed multiplication convention

For a finite group `G`, take vertices `(i,g)`, where `i=0,1`. Choose inverse-closed internal sets `A0,A1` avoiding the identity, and cross set `T` of distinct group elements. Edges are

- `(0,g)—(0,g a)` for `a in A0`;
- `(1,g)—(1,g b)` for `b in A1`;
- `(0,g)—(1,g t)` for `t in T`.

The reverse cross voltages are `T^-1`. Degrees are `|A0|+|T|`, `|A1|+|T|`; order is `2|G|`. Distinct group elements give distinct neighbors, internal nonidentity prevents loops, and the two vertex types prevent cross loops. Unordered edges are deduplicated in the explicit output.

Left multiplication `(i,g) -> (i,hg)` is an automorphism: `h(g s)=(hg)s`. Consequently the two roots `(0,e),(1,e)` cover all distance obligations, once this action is connected to the actual generated edge rules. Full all-source BFS remains a simple independent final check at these sizes.

For the 684 graph use **Loz–Širáň's convention**

`G = Z_m ⋊_r Z_n`, `(a,b)(c,d)=(a+r^b c mod m,b+d mod n)`, requiring `r^n=1 mod m`.

Inverse is `(-r^(-b)a,-b)`. Comellas writes the cyclic factors in the opposite order with a right-action multiplication. These formulas are isomorphic conventions but should not be mixed while preserving the same numeric voltage list.

## Exact 120 graph

Files: `graph_6_3_n120.txt` (author data), `120_recovered_construction.json`, `120_automorphism_generators.json`, `recover_120.py`.

Use `G=C5×A4`, with a permutation written as the tuple of its images on `0,1,2,3`; multiply `(k,p)(l,q)=((k+l) mod 5,p∘q)`, where `(p∘q)[i]=p[q[i]]`.

```
a = (0,(1,0,3,2))
b = (0,(3,2,1,0))
T = [(1,(0,3,1,2)),
     (1,(3,2,1,0)),
     (3,(1,2,0,3)),
     (4,(0,1,2,3)),
     (2,(3,0,2,1))]
A0={a}; A1={b}
```

The reconstruction found three graph automorphisms using NetworkX VF2 with root-distance colors, closed the generated permutation group (exactly 60 elements), found a central order-five generator and an `A4` subgroup, and supplied a complete bijection between these coordinates and all 120 source vertex labels. Rebuilding from the displayed rules produced **exactly all 360 source edges**, not merely an isomorphic graph assertion. Parent/root independently ran its own BFS baseline regression successfully.

This graph is the source baseline. The underlying dimension formula `2×12×m=24m` would exceed 120 at `m≥6`, but the naive enlargement keeping both involutions in the `A4` factor is impossible; see the separate mathematical note. This warning materially changes which parameters should be searched.

## Exact 684 graph

Files: `graph_7_4_n684.txt` (author data), `684_recovered_construction.json`, `recover_684.py`.

Use `(m,n,r)=(38,9,23)` and vertex label `i*342+a*9+b`.

```
A0 = {(4,4),(8,5),(25,3),(29,6)}
A1 = {(10,1),(23,6),(26,8),(29,3)}
T  = {(2,2),(2,6),(24,3)}
```

Both `Ai` are inverse-closed and have four elements; `T` has three. The generated **2394** edges equal the entire original edge set exactly. Two representative BFS checks give the same layer sizes `1,7,42,233,401`, hence diameter exactly four. These validations recover a known graph, not a new bound.

For candidate generation retain degree allocation `4+3`: two inverse pairs in each internal set and three cross voltages (one normalizable to identity). The parameter formula is `N=2mn`, `Delta=7`; target `mn>342`, and the actual diameter-four condition still requires all short-walk voltage sets between all base pairs to cover `G`. Examples with nontrivial semidirect actions available just above the threshold include `(m,n)=(29,12)` (696 vertices, action order up to4), `(71,5)` (710 vertices, action order5), `(61,6)` (732 vertices, action order6), `(31,12)` (744 vertices, action order6). These are admissible group orders, **not known successful graphs or ranked chances**. No voltage optimization was launched by this source subtask.

## Reproduction

From the project root:

```
python3 research/ddp/m1_sources/recover_120.py
python3 research/ddp/m1_sources/recover_684.py
python3 research/ddp/m1_sources/central_halfturn_profile.py
python3 research/ddp/m1_sources/complete_c6_a4.py
```

The last two commands check one explicitly limited 144-vertex construction family. They are not a claim about all `(6,3)` graphs or other degree allocations over the same group.

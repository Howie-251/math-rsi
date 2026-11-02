# Accepted degree11/12 finals: complete full-neighborhood clone obstruction

The first complete full-neighborhood eligibility profiles of these two final accepted graphs find zero legal prototypes. Source37631/205329 at degree11 has minimum one saturated neighbor (15 vertices attain it); source42402/245937 at degree12 also has minimum one (20 vertices attain it). Their actual free-vertex counts are2471 and13857. The full per-vertex saturated-neighbor arrays, degree arrays, histograms and first minimum witnesses are saved.

A clone z of a nonisolated prototype v joined exactly to its complete current N(v) would inherit D<=5: replace the first vertex of a shortest v-to-t path by z for t!=v, and use z-u-v for t=v. Old-old paths remain. This is a complete route proof and requires no new distance BFS or R4 computation. The only missing condition here is degree legality: every N(v) contains an already saturated pin. Thus there is no legal first full-neighborhood clone on either fixed source, and no pure sequential cloning batch can start.

Each current edge table was read once, then degree and neighborhood sets were scanned. The actual sources are h9_d11_followups/graph_d11_D5_n37631.edges and h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges, not the older42398 base. No full source D5 revalidation, radius computation, solver or new graph occurred. The degree13 full-neighborhood obstruction was inherited and not rescanned.

Measured scan CPU0.514673336seconds, wall0.516864613, within10CPU. Both frozen existence predictions are refuted. The closure covers this exact full-N(v), all-old-edges-retained rule on these two current graphs; partial neighborhoods, guards, other cooperative rules and edge changes are not excluded. No such follow-on was launched. Existing delivery, accepted sequences and103 examples remain unchanged.

## Paired adjacent-clone variant

The saved profile also closes the exact adjacent two-prototype copy rule: a legal oldedge uv would require SatN(u)={v} and SatN(v)={u}. Degree11 has no full satN1 endpoints; degree12 has only28565 and36331, which are nonadjacent and share unique saturated neighbor27674. The separate complete read-only gate costs0.124853835 CPU seconds and produces no graph, BFS, R4 or solver call. Shared-boundary multiplicities independently overfill seven pins. This is one subordinate variant of this record; original scan counts and timings above are unchanged. See ../h9_paired_full_neighborhood_clone_rule/REPORT.md and BINDING_RESULT.json.

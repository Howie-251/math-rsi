# Frozen finite consistency specification

Prepared before implementation on 2026-10-28. Main-session mathematical generation; native Sol/high execution only. New derivations remain unreviewed/unaccepted. This bounded check is neither a general proof nor independent mathematical review.

## Scope and boundaries

Only this fresh local directory, its fresh authoritative Linux counterpart `/data/ktqiu_hdd/math_agent/tmp/n7_tail_interval_stability_20261028`, the new additive research report, and append-only MANIFEST entries may be written. No old file, task status, acceptance, runtime, job, solver, campaign, network download, or proof replay is changed. Reuse the established SSH transport without exposing credentials. All scientific enumeration executes on Linux only; local operations are file/transport/document mechanics.

## Main-supplied mathematics to be checked

For p>=3 let X be a complete ordered rank-3 signotope with no blue(p+1) or red(p+1). S is the set of actual red-p sources; h=max S. For every actual red-p path starting at h, its p-1 later vertices form a red tail T. L contains tail vertices t for which S+t contains blue-p. Graph G has edge i,j exactly when some actual blue(p-2) path Q in S followed by t_i,t_j is blue-p. Use ALL actual prefixes. Check for every A subset T that S+A has no blue-p iff A avoids L and has no G edge. Check edge i,k implies i,j for i<j<k, every edge right endpoint is an actual blue-p endpoint, and a tail vertex outside E_B has no incoming or crossing edge. For p>=4 every edge witness Q ending u,q whose right endpoint is not looped has q<h and colors (u,q,h)=R, (q,h,t_i)=(q,h,t_j)=B. For p=3 the unlooped graph is empty.

The capacity statement w=alpha(G[T minus L])<=a requires the separately supplied effective bound b and weak-n inheritance; small enumerations do not test b25 or establish a global capacity. The full theorem, saturation, four-role identities, and the full-path obstruction dual are written from the main's frozen derivations, not inferred by the executor.

## One combined scientific run

Phase 1: exhaust all 2^10 triple colorings on five vertices. Retain every valid four-packet coloring. Check packet (q,t_i,t_j,t_k) with its second entry B and last R forces first B. When positions 2,3,4 form a red triple, check blue-join positions of prefix(0,1) form an interval and c_jk=B implies c_ik=c_ij=B for c_ij=color(1,t_i,t_j). On positions u0,q1,h2,t_i3,t_j4, under color(u,q,t_i)=B, color(q,t_i,t_j)=B, color(h,t_i,t_j)=R and not both color(u,q,h)=B and color(q,h,t_j)=B, require R/B/B at (u,q,h),(q,h,t_i),(q,h,t_j).

Phase 2: enumerate every right endpoint vector r_i in [i,m-1] for 1<=m<=7. Define edge i,j iff i<j<=r_i. Independently compare interval intersections. Greedily choose a remaining interval with least right endpoint, remove all intervals containing it as one clique, and compare the number of cliques and chosen independent intervals with brute-force maximum independent sets. For m<=4 repeat on every vertex-induced subgraph. Synthetic negative controls reject a missing right-closure edge, an invalid clique partition, and a fake independent witness.

Phase 3: enumerate all 2^20 triple colorings on six vertices, rejecting invalid complete packets early. For every valid coloring independently enumerate all monochromatic paths by all triples, and compare with consecutive triples. For p=3,4,5 retain the no blue(p+1)/red(p+1) cases. Derive S_R and E_B from actual paths; enumerate ALL red-p paths starting at max S_R, construct all L and edges from all prefix paths, then check the preceding exact structural claims. Do not impose weak n or b25 for these structural checks. Save exact totals per phase and p, elapsed times, maxRSS and hashes.

Positive controls exercise valid packets and nonempty valid graph witnesses. A synthetic BRBR packet must be rejected. Negative controls are labeled synthetic and never presented as actual signotope counterexamples.

One run maximum, external wall bound 180 seconds with TERM then KILL after 2 seconds, process CPU 175 seconds, address space 512 MiB, internal deadline 150 seconds. Check the deadline frequently and record INCOMPLETE_BUDGET rather than widening scope. Failure records raw evidence and stops; no scientific retry, repair rerun, continuation, solver or certificate invocation. Fetch raw result/stdout and source identity. Finite success cannot upgrade a theorem or acceptance state.

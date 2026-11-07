# Single bounded verification of the main-supplied Q_n family

Prepared before implementation and execution, 2026-10-28. This is finite consistency evidence for the main session's proposed family, not independent proof review or acceptance. All previous protected files remain byte-for-byte unchanged. Only this isolated directory and its fresh authoritative Linux counterpart may be written.

## Inputs and exact colors

Only n=7 and n=8. The ordered vertices of D are A=(a1,...,a_(n-1)), followed by B=(b1,...,b_(n-5)). All AAA triples are red, all BBB and AAB triples are blue, and ABB is red if and only if its A vertex is a_(n-1). X adds a greatest h and assigns blue to every triple containing h. D has 2n-6 vertices, X has 2n-5. No random input, solver, external scientific dependency, search or optimization is used.

## Enumeration and independently computed quantities

Enumerate every four-packet in the order abc,abd,acd,bcd and require at most one color change. For every subset of size at least two, independently test the consecutive-triple and all-triple definitions of each monochromatic path and require exact agreement. Save every monochromatic path, complete color tables, every fixed-end maximum, and the complete long-path lists (length at least n-3). The two-color maxima at each actual pair must have sum at most n+1, equivalent here to no weak n.

D expectations: no blue(n-2), no weak n; exactly one red(n-1) path, namely A; End_R(n-2)={a_(n-2),a_(n-1)}, Src_B(n-3)={a1,...,a_(n-3)}, and their intersection is empty.

X expectations: no blue(n-1), no red n, no weak n; mixed sources Src_R(n-1) intersect Src_B(n-2)={a1}; the complete red(n-1) terminal set of a1 is {a_(n-1)}, while the complete blue(n-2) second-vertex set of a1 is {a2,...,a_(n-2)}. F+ consists of mixed sources where those two nonempty sets are the same singleton. F- is the order-reversed same-color definition: at a mixed terminal, use all red(n-1) sources and all blue(n-2) penultimate vertices. Both locked families must be empty. Every blue(n-2) ends at h, and every red(n-1) ends at a_(n-1).

Canonical reconstruction follows R7 sections 1-2: red a<b<c imposes ab<ac<bc; blue imposes the reverse. Build all constraints, take one deterministic lexicographic topological extension, choose the minimum incident pair at every vertex, and independently test that it reaches every alternative incident pair. No lambda optimization. Compute P+ and P- from actual p, then inside actual P+ compute G=End_R(n-2) intersect Src_B(n-3), H=P- union G, R=P+ minus G. Expected p(v)=h for every v in D, p(h)=last B, P+=D, P-={h}, G empty, H={h}, R=D. Save all triple comparisons, linear extension and reachability tests.

## Negative controls and stop conditions

On a fresh copy of D change only a1a2a3 and a1a3a4 from red to blue. The packet (a1,a2,a3,a4) must be BRBR and must be rejected. A separate all-red coloring on X must pass packets but fail the long-red cap (it contains red n). Neither control changes the original family.

One combined deterministic scientific execution only. Wall limit 120 seconds, CPU limit 115 seconds, address-space limit 1 GiB. External timeout sends TERM then KILL after 2 seconds. Fail at the first unexpected result, save failure evidence, and stop without repairs, reruns, retries or continuation. No solver/checker invocation, old job changes, capacity upgrade, acceptance upgrade or independent Claude calls. Only the Linux script executes science; local Python is transport only.

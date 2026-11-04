# Core 0 c4 endpoint-spectrum diagnostic

Date: 2026-11-01. Status: producer diagnostic; independent verification
and full c4 closure are not claimed. Work stopped at the parent agent's
request because its new proof route supersedes this enumeration route.
No previously audited c0 proof or certificate was changed.

Use the local labeling and two-bridge transfer of
`T15_CORE0_C2_PROGRESS.md`, now with four original crossing ports per face.
For each omitted retained-hole choice $u=3,5,6$, there are 15 abstract
pairings on the six A forest endpoints: four crossing ports and the two
bridge endpoints. A spectrum is consequently a 45-bit mask.

`t15_core0_c4_spectrum_antichain.cpp` enumerates all $51975$ internal A
matchings and their complete short-edge forest spectra. It finds 31383
distinct masks. Closing these under all $24$ permutations of crossing
ports yields 554328 masks. Their inclusion-minimal antichain has 34488
masks, each with at least 21 available bits. Data:

- `t15_core0_c4_A_spectra.txt`: every original A input and its mask.
- `t15_core0_c4_antichain.json`: counts and all minimal masks.
- `t15_core0_c4_minimal_masks.txt`: the same minimal-mask list for the B test.

`t15_core0_c4_B_compatibility.cpp` enumerates all
$\binom{14}{4}9!!=945945$ internal B matchings. For every abstract endpoint
pairing it inserts the bridge edges and the B matching, rejects cycles,
suppresses the internal bridge labels, and checks the resulting B matching
against the exact Q4 three-avoid negative list. It queries a binary trie
of the A minimal antichain for an A mask disjoint from the B good mask.

There are only 2161 different B good masks. Exactly two B inputs have a
disjoint A mask; both have zero B good mask. All other B inputs intersect
every A spectrum under every crossing bijection. The two exact B inputs
are in `t15_core0_c4_B_failures.txt`: each row has the B good mask, a
witnessing A spectrum, four sorted B ports, and five B matching edges.
The report is `t15_core0_c4_B_compatibility.json`.

Thus this producer reduces c4 to at most
$2\cdot51975\cdot24=2494800$ full Q5 inputs. These full inputs have not
been searched or certified here. A zero B spectrum means this sufficient
double-bridge construction is unavailable; it is not a T15 counterexample.
The A/B enumeration, permutation closure, antichain reduction and trie
query still require independent verification before using this as a proof.

The separately completed c2 theorem and its independent check reports are
in `T15_CORE0_C2_PROGRESS.md` and `t15_core0_c2_verification.json`; their
fresh-context audit remains pending. No entire-core or global coverage
claim is made by this diagnostic.

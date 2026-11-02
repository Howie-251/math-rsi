# Exact model and conditional scope

For a fixed accepted source G with diameter at mostD and eligible old pins F, append z adjacent to a distinct S subsetF. A shortest z-to-old-target path exits z once and never revisits it, hence d(z,t)=1+d_G(S,t). Thus the new-root bound is exactly full R_(D-1)(S) coverage, while old-old distances are retained. Individual pin variables with cardinality<=15 model this full single-append condition.

For the known source inversion iota, S and iota(S) have equal cardinality and coverage. Ordering nonfixed pairs by their smaller label, the first differing pair is selected at its lower endpoint in exactly one of these two representatives. Tracking prefix equality makes this a genuine isomorphism normalization. It does not require either pair's variables to be equal and does not fold any target constraint.

With p_i <-> p_previous AND (x_low <-> x_high), p_0=true, the five stored clauses are the exact equivalence. The clause(-p_previous OR x_low OR -x_high) selects the canonical first difference. Adding -p_final restricts to asymmetric sets. It is mathematically complete for that subdomain independent of prior solver outcomes; covering the full unrestricted domain additionally requires the separate invariant-domain exclusion. Here both asymmetric solver calls ended UNKNOWN, so no full-domain negative follows.

Packed support uses arbitrary-width rows, full source-target axes and all independent pins. LSB bit_length returns the matching1-based selector, including variables above64. Auxiliary variables start beyond the pin range. All source/cache binding and no-new-BFS claims are unchanged from the complete all-free direction interface.

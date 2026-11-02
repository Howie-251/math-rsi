"""Exact maximum union of independently translated finite linear subspaces.

ForF2^4, every state is a16-bit mask, so there are at most65536 states.
Repeated subspaces are separate route choices and must not be deduplicated.
No global-offset consistency constraints or offset search are implemented.
"""
from itertools import product


def vector_id(coords, q):
    return sum(int(x)*q**i for i,x in enumerate(coords))


def vector_coords(v, q, dimension):
    return tuple((v//q**i)%q for i in range(dimension))


def add_ids(a, b, q, dimension):
    if q==2:
        return a ^ b
    return vector_id(((x+y)%q for x,y in
                      zip(vector_coords(a,q,dimension),vector_coords(b,q,dimension))),q)


def hyperplane(normal, q):
    """Convenience fixture input: all vectors with normal dot x=0."""
    return [vector_id(x,q) for x in product(range(q),repeat=len(normal))
            if sum(a*b for a,b in zip(x,normal))%q==0]


def translation_cosets(subspace, q=2, dimension=4):
    """Return unique coset masks with one representative shift per coset."""
    subspace=tuple(sorted(set(subspace)))
    assert subspace and subspace[0]==0
    size=q**dimension
    assert all(0<=v<size for v in subspace)
    cosets={}
    for shift in range(size):
        mask=0
        for v in subspace:
            mask |= 1 << add_ids(v,shift,q,dimension)
        cosets.setdefault(mask,shift)
    # This is also a lightweight check that the supplied set has coset partition size.
    assert len(cosets)*len(subspace)==size
    return tuple((mask,shift) for mask,shift in cosets.items())


def maximum_translated_union(subspaces, q=2, dimension=4):
    """Exact value, witness shifts, and state counts for independent translations.

    subspaces[i] belongs to route i. Equal sets at different i remain distinct.
    The input contract is a sequence of actual Fq-linear subspaces, encoded by
    vector IDs. q is prime here, as used by the F2 and F3 fixtures.
    """
    subspaces=[tuple(sorted(set(s))) for s in subspaces]
    options=[translation_cosets(s,q,dimension) for s in subspaces]
    size=q**dimension
    full=(1<<size)-1
    states={0:()}
    counts=[1]
    union_attempts=0
    full_stage=None
    for i,cosets in enumerate(options):
        next_states={}
        for covered,shifts in states.items():
            for mask,shift in cosets:
                union_attempts+=1
                joined=covered|mask
                if joined not in next_states:
                    next_states[joined]=shifts+(shift,)
        states=next_states
        counts.append(len(states))
        if full in states:
            # No union can improve on the whole space. Complete the witness with
            # arbitrary shifts for remaining routes; this is an exact early stop.
            full_stage=i+1
            shifts=states[full]+tuple(cosets[0][1] for cosets in options[i+1:])
            best_mask=full
            break
    else:
        best_mask=max(states,key=int.bit_count)
        shifts=states[best_mask]
    # Independent direct reconstruction of the returned union witness.
    direct=0
    for subspace,shift in zip(subspaces,shifts):
        for v in subspace:
            direct |= 1 << add_ids(v,shift,q,dimension)
    assert direct==best_mask
    return dict(q=q,dimension=dimension,point_count=size,route_count=len(subspaces),
                subspace_sizes=[len(s) for s in subspaces],
                translation_cosets_each=[len(c) for c in options],
                exact_max_union=best_mask.bit_count(),can_cover_all=best_mask==full,
                best_shift_representatives=list(shifts),best_union_mask=best_mask,
                missing_vectors=[v for v in range(size) if not (best_mask>>v)&1],
                states_by_stage=counts,union_attempts=union_attempts,
                full_cover_reached_at_stage=full_stage,
                route_multiplicity_retained=True,
                consistent_global_offsets_searched=False)

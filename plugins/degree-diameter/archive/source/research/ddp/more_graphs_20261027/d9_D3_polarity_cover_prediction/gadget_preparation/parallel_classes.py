"""Pure BLOCKS combinatorics for a supplied portp; no source adjacency or BFS.

This helper is saved for reproducibility, not executed in preparation. The
proposed redirect gadget already has a paper newroot obstruction.
"""


def derived_parallel_classes(block_records, p):
    """Return the nine eight-circle classes in the derived affine plane atp.

    A circle is represented by its oldcore vertex label. Two distinct circles
    throughp are parallel precisely when their portsets intersect only inp.
    """
    selected = {row["vertex"]: frozenset(row["ports"])
                for row in block_records if p in row["ports"]}
    assert len(selected) == 72
    remaining = set(selected)
    classes = []
    while remaining:
        first = min(remaining)
        one_class = sorted(v for v in selected
                           if v == first or selected[v] & selected[first] == {p})
        assert len(one_class) == 8
        assert set(one_class) <= remaining
        for i, u in enumerate(one_class):
            for v in one_class[i+1:]:
                assert selected[u] & selected[v] == {p}
        assert len(set().union(*(selected[v] - {p} for v in one_class))) == 64
        classes.append(one_class)
        remaining.difference_update(one_class)
    assert len(classes) == 9
    return classes


def omit_port_neighborhood_class(classes, actual_neighbors_of_p):
    """N_G(p) must come from the shared literal binding, never labels guessed."""
    special = set(actual_neighbors_of_p)
    assert len(special) == 8
    assert sum(set(c) == special for c in classes) == 1
    return [c for c in classes if set(c) != special]


def synchronous_equivariant_choices(anchor_class, sigma, eligible_neighbors):
    """Seven synchronized choices only, not all7^4 equivariant assignments.

    sigma is the supplied actual graphautomorphism. Each anchor pair chooses
    its lexrepresentative's jth eligible neighbor, then takes sigma for its
    partner, using the samej=0..6 across all fourpairs.
    """
    assert all(sigma[sigma[v]] == v for v in anchor_class)
    assert all(sigma[v] in anchor_class and sigma[v] != v for v in anchor_class)
    representatives = sorted(v for v in anchor_class if v < sigma[v])
    assert len(representatives) == 4
    assert all(len(eligible_neighbors[v]) == 7 for v in representatives)
    result = []
    for j in range(7):
        choice = {}
        for v in representatives:
            w = sorted(eligible_neighbors[v])[j]
            choice[v] = w
            choice[sigma[v]] = sigma[w]
        result.append(choice)
    return result

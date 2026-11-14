"""Geometry certificates for the audited controlled two-return bridge theorem.

Build the audited registries once and call find_plan with actual seven-bit even
and odd labels of an independent fourteen-hole set. Use plans instead when
every successful geometry is needed.

T44_same_face and the T15 easy faces use Q6_TWO_AVOIDED_EASY_REVIEW.
T44_isolated_mark uses Q6_T44_SINGLETON_REVIEW. The exact T15 and T63
registries come from the previously audited distance-two replay helpers.
This module never scans an input domain or runs a matching or rank computation.
"""

from functools import cache
from itertools import combinations
import json

from R7_CONTROLLED_CYCLE_DONOR_PROBE import project as project_face
from R7_DELTA2_DISTANCE2_BROAD_CHECK import core_transport
from R7_DELTA2_DISTANCE2_BROAD_CONTROLLED_CHECK import marked_ranks, new_ranks, tool
from R7_MU3_BROAD_T15_DONOR_PROBE import BITS, RESEARCH, accepted_cores, marked_signature, project


def build_registry():
    cores = accepted_cores()
    profile = json.loads((RESEARCH / "Q6_T15_ACTUAL_PROFILE.json").read_text(encoding="utf-8"))
    targets = {row["index"]: row for row in profile["orbits"]}
    old_t63, _ = marked_ranks()
    new_t63 = new_ranks()

    @cache
    def lookup_t15(retained, marks):
        index = cores.get(marked_signature(retained, marks))
        if index is None:
            return None
        return dict(kind="T15_exact_core", index=index,
                    normalized_groups=[retained, marks],
                    coordinate_transport=core_transport([retained, marks], targets[index]))

    @cache
    def lookup_receiver(minority, majority, marks):
        config = dict(q=len(marks), minority=minority, majority=majority, marks=marks)
        return tool(config, old_t63, new_t63)

    return lookup_t15, lookup_receiver


def donor_interface(outer, minority, retained, marks, lookup_t15):
    holes = minority | retained | marks
    prefix = "T15" if minority else "T44"
    for direction, bit in enumerate(BITS):
        if direction == outer:
            continue
        zero = {p for p in holes if not p & bit}
        one = holes - zero
        if not zero or not one:
            return dict(kind=prefix + "_same_face", inner=direction, inner_side=int(bool(one)))
        for side, points in enumerate((zero, one)):
            if len(points) == 1 and points <= marks:
                return dict(kind=prefix + "_isolated_mark", inner=direction, inner_side=side,
                            isolated_mark=next(iter(points)))
    if not minority:
        return None
    a, = minority
    groups = tuple(tuple(sorted(project(p ^ a, outer) for p in group)) for group in (retained, marks))
    exact = lookup_t15(*groups)
    return dict(exact, normalization_root=a) if exact else None


def plans(even, odd, registry):
    colors = set(even), set(odd)
    lookup_t15, lookup_receiver = registry
    for j, outer in enumerate(BITS):
        for side in (0, 1):
            for beta in (0, 1):
                alpha_holes, beta_holes = colors[1 - beta], colors[beta]
                a_minor = {p for p in alpha_holes if bool(p & outer) == side}
                a_major = {p for p in beta_holes if bool(p & outer) == side}
                k = len(a_major) - len(a_minor)
                if k not in (4, 5, 6) or len(a_minor) > 1:
                    continue
                b_major, b_minor = alpha_holes - a_minor, beta_holes - a_major
                for x in combinations(sorted(a_major), k - 2):
                    retained_a = a_major - set(x)
                    y = {p ^ outer for p in x}
                    for u in combinations(sorted(b_major), 2):
                        v = {p ^ outer for p in u}
                        donor = donor_interface(j, a_minor, retained_a, v, lookup_t15)
                        if donor is None:
                            continue
                        retained_b = b_major - set(u)
                        for inner, bit in enumerate(BITS):
                            if inner == j:
                                continue
                            axes = [axis for axis in BITS if axis not in (outer, bit)]
                            faces = []
                            for inner_side in (0, 1):
                                minor = {p for p in b_minor if bool(p & bit) == inner_side}
                                major = {p for p in retained_b if bool(p & bit) == inner_side}
                                marks = {p for p in y if bool(p & bit) == inner_side}
                                q = len(marks)
                                if q not in (1, 2, 3) or len(major) - len(minor) != q:
                                    break
                                groups = tuple(tuple(sorted(project_face(p, axes) for p in group))
                                               for group in (minor, major | marks, marks))
                                receiver = lookup_receiver(*groups)
                                if receiver is None:
                                    break
                                faces.append(dict(inner_side=inner_side, minority=groups[0], majority=groups[1],
                                                  marks=groups[2], interface=receiver))
                            if len(faces) == 2:
                                yield dict(gate="controlled_two_return", k=k, outer=j, donor_side=side,
                                           donor_majority_parity=beta, source_x=x, source_u=u,
                                           donor_minority=sorted(a_minor), donor_retained=sorted(retained_a),
                                           donor_marks=sorted(v), donor_interface=donor, inner=inner,
                                           receiver_axes=[axis.bit_length() - 1 for axis in axes],
                                           receiver_marks=sorted(y), receiver_faces=faces)


def find_plan(even, odd, registry):
    return next(plans(even, odd, registry), None)

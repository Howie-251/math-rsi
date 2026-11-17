"""Check the nineteen stored empty-small-face geometries against accepted gates."""

import json
import sys
from collections import Counter
from itertools import product
from pathlib import Path
from time import perf_counter

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mu1_global_2026_11_15"))

from MU0_JOINT_NECESSARY import ALPHA, AXES, BETA, OUTER, digest
from EDGE_MENU_PROBE import pointwise_gates
from EDGE_LOW_GAP_PROBE import central_column_hit, peeled_outer_type
from EDGE_HIGH_GAP_PROBE import validate_high_geometry
from JOINT_GAP_PROBE import old_phi
from PROBE import oriented_cut

BASE = HERE/"MU0_A0_BASIS_PREFLIGHT.json"
LOW = "R7_CENTRAL_JOINT_COLUMN_ALPHABET.md"
CONTROLLED = "R7_MU3_CONTROLLED_AND_T63_REVIEW.md"
HIGH = "mu3_hard_first_2026_11_15/ODD_HIGH_GAP_WHOLE_PAIR_REVIEW.md"
SMALL = "mu1_global_2026_11_15/q6_a8/Q6_A8_APPLICATIONS_REVIEW.md"


def block(vertices, i, side):
    return tuple(sorted(v for v in vertices if ((v >> i) & 1) == side))


def halves(first, second, i, side):
    s, t = len(block(first, i, side)), len(block(second, i, side))
    return [[s, t], [len(first)-s, len(second)-t]]


def physical_holes(rep):
    odd = tuple(64 | v for v in rep["L"])
    even = tuple(64 | (63 ^ v) for v in rep["V"])
    assert len(set(odd)) == len(set(even)) == 8
    assert all(v.bit_count() % 2 for v in odd)
    assert all(v.bit_count() % 2 == 0 for v in even)
    assert all((u ^ v).bit_count() != 1 for u in odd for v in even)
    return set(odd+even), (even, odd)


def direct_outer(colors):
    for j in AXES:
        x,y = (len(block(group,j,1)) for group in colors)
        k = abs(x-y)
        small = min(x,y,8-x,8-y)
        if k == 0 and small >= 3:
            theorem = "R7_HIGHER_HOLE_CUTS_REVIEW.md"
        elif k == 1 and small in (2,3):
            theorem = SMALL
        elif peeled_outer_type(x,y) and k == 2:
            theorem = (
                "R7_E16_TWO_HOLE_FACE_FULL_CLOSURE_REVIEW.md",
                "R7_E16_INITIAL_REDUCTION_REVIEW.md",
                "R7_SIX_HOLE_RECEIVER_MULTI_LAYER_REVIEW.md",
            )[small]
        elif peeled_outer_type(x,y) and k == 3:
            theorem = "R7_E16_THREE_MONOCHROMATIC_CLOSURE_REVIEW.md"
        else:
            continue
        return dict(gate="direct_outer", theorem=theorem, outer_axis=j,
                    original_even_odd_halves=[[x,y],[8-x,8-y]])
    return None


def direct_column(colors):
    for j, receiver in product(AXES, (0,1)):
        aa, ab, ba, bb = oriented_cut(colors,j,receiver)
        r,s,k = len(aa),len(bb),len(ba)-len(bb)
        assert r+s+k == 8 and len(ab) == r+k
        if k not in (2,3,4):
            continue
        for i,t in product(AXES, (0,1)):
            if i==j:
                continue
            side, other = block(ab,i,t), block(ab,i,1-t)
            a,b,c = len(block(bb,i,t)),len(block(ba,i,t)),len(side)
            d = b-a
            e = k-d
            root = None
            if r <= 5 and (d,e) in product((1,2),repeat=2) and c >= d and len(other) >= e:
                if (d == 1 or a <= 1) and (e == 1 or s-a <= 1):
                    X = side[:d] + other[:e]
                    mode = "controlled_positive_split"
                    theorem = CONTROLLED
                else:
                    X = None
            else:
                X = None
            if X is None and (k,r,s) == (2,3,3) and central_column_hit(a,b,c):
                theorem = LOW
                if d == 1:
                    if c in (0,5):
                        source, root_side = (side,t) if c else (other,1-t)
                        X = source[:2]
                        root = block(bb,i,root_side)[0]
                        mode = "central_single_root_same_side"
                    else:
                        X = side[:1]+other[:1]
                        mode = "central_positive_split"
                elif d == 2 and c == 1:
                    X = side + other[:1]
                    marks = {v ^ (1 << j) for v in X}
                    root = next(u for u in block(bb,i,1-t) if (u ^ (1 << i)) not in marks)
                    mode = "central_single_root_split"
                else:
                    X = side[:2]
                    mode = {2:"central_balanced_complement",3:"central_majority_root",
                            4:"central_two_majority_roots"}[d]
            if X is None:
                continue
            assert len(X)==k and set(X)<=set(ab)
            Y = [v ^ (1 << j) for v in X]
            return dict(gate=mode, theorem=theorem, outer_axis=j, receiver_bit=receiver,
                        alpha_parity=ba[0].bit_count()%2, inner_axis=i, inner_side=t,
                        original_outer_halves_alpha_beta=[[r,r+k],[s+k,s]], X=X, Y=Y, root=root,
                        original_seen_column=dict(minor=a, majority=b, sources=c),
                        modified_receiver_halves_alpha_beta=halves(set(ba)|set(Y),bb,i,t),
                        marks_by_half=[len(block(Y,i,t)),len(block(Y,i,1-t))])
    return None


def physical_positive_split(colors, hit):
    j, side, k = hit["outer"], hit["side"], hit["gap"]
    aa, ab, ba, bb = map(set, oriented_cut(colors,j,side))
    r,s = len(aa),len(bb)
    X,U = set(hit["X"]),set(hit["U"])
    assert X<=ab and U<=ba and len(X)==k-2 and len(U)==2
    Y,V = ({v^(1<<j) for v in group} for group in (X,U))
    modified_A = (ab-X)|V
    modified_B = (ba-U)|Y
    receiver = None
    donor = None
    for i in AXES:
        if i == j:
            continue
        q = len(block(Y,i,0))
        qe = len(Y)-q
        profiles = halves(modified_B,bb,i,0)
        if q in (1,2) and qe in (1,2) and profiles[0][0]-profiles[0][1]==2*q:
            if (q==1 or profiles[0][1]<=1) and (qe==1 or profiles[1][1]<=1):
                assert profiles[1][0]-profiles[1][1]==2*qe
                receiver = (i, profiles, (q,qe))
                break
    for h,t in product(AXES,(0,1)):
        if h == j or len(block(V,h,t))!=2:
            continue
        profiles = halves(aa,modified_A,h,t)
        a,b = profiles[0]
        if old_phi(r,a,b-a):
            donor = (h,t,profiles)
            break
    assert receiver is not None and donor is not None
    i, receiver_counts, marks = receiver
    h,t, donor_counts = donor
    return dict(gate="high_positive_split", theorem=HIGH, outer_axis=j, receiver_bit=side,
                original_outer_halves_alpha_beta=[[r,r+k],[s+k,s]], alpha_parity=min(ba).bit_count()%2,
                X=sorted(X),U=sorted(U),Y=sorted(Y),V=sorted(V),donor_inner=[h,t],receiver_inner=[i,0],
                modified_donor_halves_alpha_beta=donor_counts,
                modified_receiver_halves_alpha_beta=receiver_counts, receiver_marks=marks)


def direct_geometry(rep):
    H,colors=physical_holes(rep)
    by_count = direct_outer(colors)
    by_column = direct_column(colors)
    by_small = pointwise_gates(H)
    by_high = validate_high_geometry(H)
    first = by_count or by_column
    if first is None and by_small:
        first = dict(by_small[0], theorem=SMALL, source_plan="actual source and returns")
    if first is None and by_high["positive_split"]:
        first = physical_positive_split(colors,by_high["positive_split"][0])
    if first is None and by_high["whole_pair"]:
        record = by_high["whole_pair"][0]
        first = dict(record["first_plan"], gate="high_double_whole", theorem=HIGH,
                     outer_axis=record["outer"],receiver_bit=record["receiver_bit"])
    return dict(H_even=colors[0],H_odd=colors[1],
                global_odd_minus_even=[len(block(colors[1],j,1))-len(block(colors[0],j,1)) for j in AXES],
                menu_hits=dict(direct_outer=by_count is not None, direct_column=by_column is not None,
                               forward_or_split=bool(by_small),
                               high_positive_split=bool(by_high["positive_split"]),
                               high_double_whole=bool(by_high["whole_pair"])),
                first_plan=first)


def main():
    start=perf_counter()
    source=json.loads(BASE.read_text(encoding="utf-8"))
    assert source["status"]=="COMPLETE" and len(source["representatives"])==19
    path=HERE/"MU0_A0_BASIS_PLANS.json"
    if path.exists():
        raise FileExistsError("Fixed geometry pass already exists")
    results=[dict(index=i, **direct_geometry(rep)) for i,rep in enumerate(source["representatives"])]
    missed=[row["index"] for row in results if row["first_plan"] is None]
    summary=Counter(row["first_plan"]["gate"] for row in results if row["first_plan"])
    result=dict(scope="One fixed pass on exactly nineteen stored empty-small-face representatives",
                representatives_checked=len(results), missed_indices=missed, first_gate_counts=summary,
                solver_calls=0, original_matching_enumerations=0, wall_seconds=perf_counter()-start,
                basis_sha256=digest(BASE), source_sha256=digest(Path(__file__)),results=results)
    path.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print({k:v for k,v in result.items() if k!="results"},flush=True)


if __name__=="__main__":
    main()

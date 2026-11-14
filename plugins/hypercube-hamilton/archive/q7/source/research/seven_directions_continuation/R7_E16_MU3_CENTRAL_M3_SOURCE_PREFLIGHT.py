"""Freeze the central m=3 source basis and count actual minority completions."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from time import process_time

import numpy as np

from E16_MU3_CENTRAL_LOCAL_HIGH_M_SOURCE_QUOTIENT import move, root_stabilizer
import R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT as pre


CPU_LIMIT = 30
RAW_LIMIT = 13754
SOURCE_LIMIT = 5259
PAIR_LIMIT = 150138
FROZEN = Path(__file__).with_name("R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json")
FROZEN_SHA256 = "59ae221dc88eb374927c390cee705165171a1e569a694ac9d88d8f27b2a0516f"


class StopPreflight(Exception):
    pass


def check_time(start):
    if process_time()-start >= CPU_LIMIT:
        raise StopPreflight("cpu_limit")


def source_fibers(w, sparse_axes, sparse_values):
    axes = tuple(pre.AXES[i] for i in sparse_axes)
    mask = sum(axes)
    majority = sum(bit for bit,b in zip(axes,sparse_values) if b >= 5)
    active = tuple(bit for bit,b in zip(axes,sparse_values) if b in (1,5))
    assert len(active) in (2,3)
    fibers = defaultdict(tuple)
    for point in pre.ODD:
        if point not in w:
            profile = (point ^ majority) & mask
            fibers[profile] += (point,)
    return fibers, active


def fiber_candidates(fibers, active):
    zero_count = 6-len(active)
    for zero in combinations(fibers[0],zero_count):
        for units in product(*(fibers[bit] for bit in active)):
            yield zero+units
    if len(active) == 3:
        for zero in combinations(fibers[0],4):
            for bit in active:
                for singleton,pair in product(fibers[bit],fibers[sum(active)^bit]):
                    yield zero+(singleton,pair)


def positive_load_weights(s, row, case, fibers, active, alphabet):
    choices = [tuple(values) for values in row["b_projection"]]
    for axis,b in zip(row["sparse_axes"],case["b"]):
        choices[axis] = (b,)
    relations = [tuple(term for term in alphabet[tuple(load)] if term[1] in values)
                 for load,values in zip(row["loads_c_d"],choices)]
    relaxed = tuple(v for v in pre.EVEN if v not in s
                    and len(set(fibers[0]) - pre.NEIGHBORS[v]) >= 6-len(active))
    relaxed = pre.shrink_minority(relaxed,relations)
    assert len(relaxed) == case["U_pool_size"]
    weights = pre.minority_coefficients(relaxed)
    for values,terms in zip(choices,relations):
        matrix = np.zeros((4,len(values)),dtype=np.int32)
        columns = {b:i for i,b in enumerate(values)}
        for a,b,gap in terms:
            assert gap <= 6
            matrix[a,columns[b]] = 1
        weights = np.tensordot(weights,matrix,axes=(0,0))
    return {tuple(choices[i][j] for i,j in enumerate(position)):int(weights[tuple(position)])
            for position in np.argwhere(weights > 0)}


def actual_source(s,w,y,loads,alphabet,b):
    forbidden = set(s).union(*(pre.NEIGHBORS[point] for point in y))
    raw_pool = tuple(v for v in pre.EVEN if v not in forbidden)
    columns = tuple(tuple(term for term in alphabet[tuple(load)] if term[1] == value)
                    for load,value in zip(loads,b))
    assert all(columns)
    allowed = tuple(tuple(sorted({a for a,_,_ in terms})) for terms in columns)
    allowed5 = tuple(tuple(sorted({a for a,_,gap in terms if gap <= 5})) for terms in columns)
    reduced = pre.shrink_minority(raw_pool,columns)
    return dict(S=s,W=w,Y=y,b_loads=b,U_pool_raw=raw_pool,U_pool=reduced,allowed_a=allowed,
                allowed_a_no_gap_six=allowed5)


def verify_transport(row,target,order,shift,action):
    assert move(row["S"],action)==target["S"] and move(row["W"],action)==target["W"]
    assert move(row["Y"],action)==target["Y"]
    for name in ("U_pool_raw","U_pool"):
        assert move(row[name],action)==target[name]
    for i,j in enumerate(order):
        flip = bool(shift & pre.AXES[j])
        assert (6-row["b_loads"][i] if flip else row["b_loads"][i])==target["b_loads"][j]
        for name in ("allowed_a","allowed_a_no_gap_six"):
            values = row[name][i]
            if flip:
                values = tuple(sorted(3-a for a in values))
            assert values==target[name][j]


def completion_count(row,field):
    pool = row["U_pool"]
    choices = row[field]
    if len(pool)<3 or not all(choices):
        return 0
    return int(pre.minority_coefficients(pool)[np.ix_(*choices)].sum())


def run():
    start = process_time()
    raw = FROZEN.read_bytes()
    assert sha256(raw).hexdigest()==FROZEN_SHA256
    data = json.loads(raw)
    templates = [row for row in data["rows"] if row["m"]==3]
    assert Counter(row["h"] for row in templates)=={2:111,4:79,6:4}
    assert sum(row["source_upper_bound"] for row in templates)==SOURCE_LIMIT
    assert sum(row["pair_upper_bound"] for row in templates)==PAIR_LIMIT
    alphabet = {(item["c"],item["d"]): tuple(tuple(term) for term in item["rows"])
                for item in data["allowed_a_b_gap"]}
    groups = {h:tuple(root_stabilizer(h)) for h in (2,4,6)}
    by_h = defaultdict(Counter)
    total = Counter()
    sources = []
    representatives = []
    status = "complete"
    try:
        for template in templates:
            check_time(start)
            h,w = template["h"],tuple(template["W"])
            s = (0,(1 << h)-1)
            counts = by_h[h]
            counts["templates"] += 1
            rows = {}
            for case in template["sparse_cases"]:
                check_time(start)
                fibers,active = source_fibers(w,template["sparse_axes"],case["b"])
                weights = positive_load_weights(s,template,case,fibers,active,alphabet)
                y_count = weight_count = 0
                for points in fiber_candidates(fibers,active):
                    total["raw_choices"] += 1
                    counts["raw_choices"] += 1
                    if total["raw_choices"] > RAW_LIMIT:
                        raise StopPreflight("raw_choice_limit")
                    b = tuple(sum(bool(v & bit) for v in points) for bit in pre.AXES)
                    if b not in weights:
                        continue
                    total["admitted_sources"] += 1
                    total["relaxed_pairs"] += weights[b]
                    if total["admitted_sources"] > SOURCE_LIMIT or total["relaxed_pairs"] > PAIR_LIMIT:
                        raise StopPreflight("relaxed_source_or_pair_limit")
                    y = tuple(sorted(points))
                    assert len(set(y))==6 and not set(y)&set(w) and y not in rows
                    rows[y] = dict(h=h,**actual_source(s,w,y,template["loads_c_d"],alphabet,b))
                    y_count += 1
                    weight_count += weights[b]
                assert y_count==case["source_upper_bound"] and weight_count==case["pair_upper_bound"]
            assert len(rows)==template["source_upper_bound"]
            counts["admitted_sources"] += len(rows)
            receiver_group = tuple((p,z,action) for p,z,action in groups[h] if move(w,action)==w)
            assert receiver_group
            ids = {y:len(sources)+i for i,y in enumerate(sorted(rows))}
            multiplicities = Counter()
            for y in sorted(rows):
                canonical,order,shift,action = min((move(y,g),p,z,g) for p,z,g in receiver_group)
                row,target = rows[y],rows[canonical]
                verify_transport(row,target,order,shift,action)
                multiplicities[canonical] += 1
                sources.append(dict(**row, representative_index=ids[canonical],
                                    axis_destination=order,xor_after_permutation=shift))
            for y,multiplicity in sorted(multiplicities.items()):
                check_time(start)
                row=rows[y]
                count=completion_count(row,"allowed_a")
                no_six=completion_count(row,"allowed_a_no_gap_six")
                assert no_six <= count
                counts["representative_sources"] += 1
                counts["representatives_with_U"] += int(count>0)
                counts["quotient_pair_count"] += count
                counts["quotient_pair_count_no_gap_six"] += no_six
                counts["pair_count_before_source_quotient"] += count*multiplicity
                representatives.append(dict(source_index=ids[y],source_orbit_size=multiplicity,
                                            U_coefficients=count,U_coefficients_no_gap_six=no_six))
                total["pair_count_before_source_quotient"] += count*multiplicity
                if total["pair_count_before_source_quotient"] > PAIR_LIMIT:
                    raise StopPreflight("actual_pair_limit")
        check_time(start)
        assert total["raw_choices"]==RAW_LIMIT and total["admitted_sources"]==SOURCE_LIMIT
        assert total["relaxed_pairs"]==PAIR_LIMIT
        assert len(sources)==SOURCE_LIMIT
    except StopPreflight as stopped:
        status=str(stopped)
    return dict(status=status,frozen_sha256=FROZEN_SHA256,by_h=by_h,totals=total,
                sources=sources,representatives=representatives,
                cpu_seconds=process_time()-start,cpu_limit_seconds=CPU_LIMIT,
                complete_U_generated=0,complete_geometries_generated=0,plan_searches=0,
                original_matchings_enumerated=0,solver_calls=0,rank_runs=0)


if __name__ == "__main__":
    data=run()
    with Path(__file__).with_suffix(".json").open("x",encoding="utf-8",newline="\n") as file:
        json.dump(data,file,separators=(",",":")); file.write("\n")
    print(json.dumps({key:value for key,value in data.items() if key not in ("sources","representatives")},indent=2))

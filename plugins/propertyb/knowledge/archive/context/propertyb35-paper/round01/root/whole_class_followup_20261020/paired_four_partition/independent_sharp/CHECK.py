"""Independent full labeled margin domain and exact block-event IE.

No coloring subsets or center-color assignments are enumerated.
The primary output is read only after independent domain/count construction.
"""
from collections import Counter
from itertools import permutations
from math import comb
from pathlib import Path
from time import process_time
import json

HERE = Path(__file__).resolve().parent
PRIMARY = HERE.parent / "sharp_gate"
PERMS = tuple(permutations(range(4)))


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def encode(flat):
    key = 0
    for value in flat:
        key = 5*key+value
    return key


def labeled_domain():
    """Fill cells with remaining row/column capacities, with no orbit pruning."""
    row_left = [4]*4
    col_left = [4]*4
    flat = [0]*16
    result = []
    def visit(pos):
        if pos == 16:
            assert not any(row_left) and not any(col_left)
            result.append(tuple(flat))
            return
        i,j = divmod(pos,4)
        if i == 3:
            options = (col_left[j],)
        elif j == 3:
            options = (row_left[i],)
        else:
            options = range(min(row_left[i],col_left[j])+1)
        for value in options:
            if not (0 <= value <= row_left[i] and value <= col_left[j]):
                continue
            row_left[i] -= value
            col_left[j] -= value
            flat[pos] = value
            visit(pos+1)
            row_left[i] += value
            col_left[j] += value
    visit(0)
    assert len(result)==len(set(result))==10147
    return result


def row_sorted(flat):
    return tuple(x for row in sorted(tuple(flat[4*i:4*i+4]) for i in range(4)) for x in row)


def canonical_full_group(flat):
    """Explicit all 24*24 row/column permutations, independently of primary."""
    return min(tuple(flat[4*rp[i]+cp[j]] for i in range(4) for j in range(4))
               for rp in PERMS for cp in PERMS)


def block_masks(flat):
    rows = [0]*4
    cols = [0]*4
    label = 0
    for i in range(4):
        for j in range(4):
            for _ in range(flat[4*i+j]):
                rows[i] |= 1<<label
                cols[j] |= 1<<label
                label += 1
    assert label==16 and all(x.bit_count()==4 for x in rows+cols)
    return rows,cols


def pattern_list(blocks, both_required):
    """Red-group required; blue-group required or an arbitrary forbidden subset."""
    unions = [0]*16
    for mask in range(1,16):
        last = mask & -mask
        unions[mask] = unions[mask ^ last] | blocks[last.bit_length()-1]
    result = []
    for red in range(1,16):
        for blue in range(1 if both_required else 0,16):
            if red & blue:
                continue
            sign = -1 if (red.bit_count()+blue.bit_count())%2 else 1
            result.append((unions[red],unions[blue],sign))
    assert len(result)==(50 if both_required else 65)
    return result


def forced_count(pats_p,pats_q,universe,quota,swap=False):
    total=0
    for pr,pb,ps in pats_p:
        for qr,qb,qs in pats_q:
            red,blue = pr|qr,pb|qb
            if red & blue:
                continue
            if swap:
                red,blue = blue,red
            r,b = red.bit_count(),blue.bit_count()
            total += ps*qs*choose(universe-r-b,quota-b)
    return total


def exact_failure(flat):
    rows,cols = block_masks(flat)
    both_p,both_q = pattern_list(rows,True),pattern_list(cols,True)
    require_p,require_q = pattern_list(rows,False),pattern_list(cols,False)
    # Four existence groups: red/blue in P, red/blue in Q.
    joint = forced_count(both_p,both_q,19,9)
    single = 12*comb(11,5)-12*comb(7,1)-12*comb(7,5)+6*comb(3,1)
    root_union = 2*single-joint
    # T blue: X quota six blue, require red blocks and forbid all blue blocks.
    blue_core = forced_count(require_p,require_q,16,6)
    # T red: X quota nine blue, require blue blocks and forbid all red blocks.
    red_core = forced_count(require_p,require_q,16,9,swap=True)
    assert min(joint,root_union,blue_core,red_core)>=0
    return dict(failure_count=root_union+blue_core+red_core,
                conflict_union=root_union,T_blue_forced_core=blue_core,
                T_red_forced_core=red_core,root_conflict_intersection=joint)


def main():
    start=process_time()
    all_labeled=labeled_domain()
    domain_time=process_time()
    sorted_rows=sorted(set(map(row_sorted,all_labeled)))
    assert len(sorted_rows)==465
    canonical={f:canonical_full_group(f) for f in sorted_rows}
    orbit_counts=Counter(canonical[row_sorted(f)] for f in all_labeled)
    reps=sorted(orbit_counts)
    assert len(reps)==43 and sum(orbit_counts.values())==10147
    orbit_time=process_time()
    records=[]
    for index,flat in enumerate(reps):
        records.append(dict(id=index,key=encode(flat),
                            matrix=[list(flat[4*i:4*i+4]) for i in range(4)],
                            row_column_labeled_matrix_count=orbit_counts[flat],
                            **exact_failure(flat)))
    count_time=process_time()
    # Read primary only after independent construction and arithmetic.
    primary=json.loads((PRIMARY/"RESULT.json").read_text())
    primary_reps=json.loads((PRIMARY/"REPRESENTATIVES.json").read_text())
    assert primary["complete"] and primary["checked"]==43
    assert len(primary["records"])==len(primary_reps)==43
    fields=("id","key","matrix","failure_count","conflict_union",
            "T_blue_forced_core","T_red_forced_core")
    for own,source,source_rep in zip(records,primary["records"],primary_reps):
        for field in fields:
            assert own[field]==source[field],(own["id"],field,own[field],source[field])
            assert own[field]==source_rep[field],(own["id"],field)
        assert own["row_column_labeled_matrix_count"]==source_rep["row_column_labeled_matrix_count"]
    primary_map=dict(tuple(map(int,line.split())) for line in
                     (PRIMARY/"DOMAIN_MAP.tsv").read_text().splitlines())
    own_map={encode(f):encode(canonical[f]) for f in sorted_rows}
    assert own_map==primary_map
    minimum=min(r["failure_count"] for r in records)
    maximum=max(r["failure_count"] for r in records)
    assert minimum==10986 and maximum==12324
    worst=[r["id"] for r in records if r["failure_count"]==maximum]
    assert worst==[42] and records[42]["matrix"]==[[1]*4 for _ in range(4)]
    assert records[42]["conflict_union"]==10452
    assert records[42]["T_blue_forced_core"]==1296
    assert records[42]["T_red_forced_core"]==576
    with (HERE/"LABELED_DOMAIN.tsv").open("w") as output:
        for flat in all_labeled:
            output.write(f"{encode(flat)}\t{encode(canonical[row_sorted(flat)])}\n")
    result=dict(status="PASS",scope="full independent labeled matrix domain and block-event IE",
                labeled_matrices=10147,row_sorted_classes=465,orbits=43,
                records=records,minimum_failure=minimum,maximum_failure=maximum,
                worst_ids=worst,all_at_most_12763=maximum<=12763,
                caller_fixed_fee=79614,caller_total=79614+maximum,
                caller_margin=92378-79614-maximum,
                cpu_seconds=dict(labeled_domain=domain_time-start,
                                 full_group_canonicalization=orbit_time-domain_time,
                                 inclusion_exclusion=count_time-orbit_time,
                                 total=process_time()-start))
    (HERE/"RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
    comparison=dict(status="PASS",primary_files=["RESULT.json","REPRESENTATIVES.json","DOMAIN_MAP.tsv"],
                    exact_count_records_compared=43,counts_per_record=4,
                    orbit_size_records_compared=43,row_sorted_transport_rows_compared=465,
                    independently_generated_labeled_matrices=10147,
                    no_coloring_subsets_enumerated=True)
    (HERE/"COMPARISON.json").write_text(json.dumps(comparison,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="records"},indent=2))


if __name__=="__main__":
    main()

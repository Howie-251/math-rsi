"""Four exhaustive single-center shapes, each tested by literal balanced subsets."""
from itertools import combinations
from math import comb
from pathlib import Path
from time import process_time
import json

def blocks_for(shape):
    shared = {
        "one_triple": [(0,1,2)],
        "two_doubles_same": [(0,1),(0,1)],
        "two_doubles_adjacent": [(0,1),(1,2)],
        "two_doubles_disjoint": [(0,1),(2,3)],
    }[shape]
    blocks = [set() for _ in range(5)]
    label = 0
    for membership in shared:
        for i in membership:
            blocks[i].add(label)
        label += 1
    for block in blocks:
        while len(block)<4:
            block.add(label)
            label += 1
    assert label==18 and len(set.union(*blocks))==18
    assert sum(map(len,blocks))==20 and len({tuple(sorted(b)) for b in blocks})==5
    return blocks

def main():
    t0=process_time()
    entries=[]
    for shape in ("one_triple","two_doubles_same","two_doubles_adjacent","two_doubles_disjoint"):
        blocks=blocks_for(shape)
        masks=[sum(1<<i for i in q) for q in blocks]
        counts={}
        for blue_count in (8,9):
            conflict=0
            for subset in combinations(range(18),blue_count):
                blue=sum(1<<i for i in subset)
                conflict += any((blue&q)==q for q in masks) and any((blue&q)==0 for q in masks)
            counts[str(blue_count)]=conflict
        entries.append(dict(shape=shape,blocks=[sorted(q) for q in blocks],conflicts=counts))
    c8=max(e["conflicts"]["8"] for e in entries)
    c9=max(e["conflicts"]["9"] for e in entries)
    fixed8={str(d):5*3003+(d-1)*1001+(15-d)*1573 for d in range(6,16)}
    bounds8={d:fixed+3*c8 for d,fixed in fixed8.items()}
    bounds9={str(d):5*2002+(d-1)*2002+(15-d)*1430+3*c9 for d in range(6,16)}
    assert [e["conflicts"]["8"] for e in entries]==[2557,3186,2967,2940]
    assert [e["conflicts"]["9"] for e in entries]==[3186,3996,3708,3672]
    independent=json.loads(Path(__file__).with_name("independent").joinpath("RESULT.json").read_text())
    for literal, ie in zip(entries, independent["rows"]):
        assert literal["conflicts"]["8"]==ie["eight_blue_ten_red"]["conflict"]
        assert literal["conflicts"]["9"]==ie["nine_blue_nine_red"]["conflict"]
    Path(__file__).with_name("COMPARISON.json").write_text(json.dumps(
        dict(status="PASS",shape_count=4,quota_count=2,
             compared_values=8,methods=["literal blue subsets","nonempty block-subset inclusion-exclusion"]),
        indent=2)+"\n")
    out=dict(status="PASS",scope="four single-center shapes; literal blue subsets only",
             entries=entries,sample_spaces={"8":comb(18,8),"9":comb(18,9)},
             max_single_conflict={"8":c8,"9":c9},
             eight_blue_bounds_by_d= bounds8,nine_blue_bounds_by_d=bounds9,
             cpu_seconds=process_time()-t0)
    Path(__file__).with_name("RESULT.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()

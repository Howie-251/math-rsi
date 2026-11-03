"""Exact nine-element field probe of one new blocking-set shape."""
from pathlib import Path
import json
import time

OUT=Path(__file__).resolve().parent
START=time.process_time()
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_probe']
def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x):return -x%3+3*(-(x//3)%3)
def mul(x,y):return ((x%3)*(y%3)+2*(x//3)*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
def power(x,n):
    y=1
    for _ in range(n):y=mul(y,x)
    return y
def inverse(x):
    assert x
    return power(x,7)
def dot(a,b):
    y=0
    for x,z in zip(a,b):y=add(y,mul(x,z))
    return y
def normalize(p):
    scale=inverse(next(x for x in p if x))
    return tuple(mul(x,scale) for x in p)
f=[power(x,5) for x in range(9)]
directions={mul(add(f[x],neg(f[y])),inverse(add(x,neg(y)))) for x in range(9) for y in range(9) if x!=y}
B={(1,x,f[x]) for x in range(9)}|{(0,1,m) for m in directions}
allpoints={normalize((a,b,c)) for a in range(9) for b in range(9) for c in range(9) if a or b or c}
assert len(allpoints)==91
lines={line:{p for p in B if dot(line,p)==0} for line in allpoints}
fixed={p for p in B if normalize(tuple(power(x,3) for x in p))==p}
tangents={p:[line for line,hit in lines.items() if hit=={p}] for p in B}
triangle_sides=[line for line,hit in lines.items() if len(hit)==6]
assert len(triangle_sides)==3
covered_by_sides={p for p in allpoints if any(dot(line,p)==0 for line in triangle_sides)}
assert B<=covered_by_sides
result=dict(status='COMPLETE_EXACT_F9_SHAPE_PROBE',directions=sorted(directions),raw_points=[list(p) for p in sorted(B)],
            point_count=len(B),all91_lines_blocked=all(lines.values()),minimal_blocking=all(tangents.values()),
            line_intersection_histogram={str(k):sum(len(hit)==k for hit in lines.values()) for k in sorted({len(hit) for hit in lines.values()})},
            Frobenius_stable={normalize(tuple(power(x,3) for x in p)) for p in B}==B,
            fixed_points=[list(p) for p in sorted(fixed)],fully_unsplit_pin_count=(len(B)+len(fixed))//2,
            triangle_sides=[list(line) for line in triangle_sides],
            no_full_F9_line=max(map(len,lines.values()))<10,
            no_Baer13_reason='B iscontainedintheunionof3lines; eachambientlinehasatmost4pointsofanyBaerPG2F3,soatmost12ofits13pointsareinthose3lines.',
            tangent_witness={str(p):[list(line) for line in ls] for p,ls in tangents.items()},
            CPU_seconds=time.process_time()-START,new_graphs=0,new_lower_bounds=0)
(OUT/'SHAPE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['raw_points','tangent_witness']},ensure_ascii=False))

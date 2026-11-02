"""Construct a degree-eight seed via a non-polar dominating neighborhood.

This changes the insertion neighborhood and then repairs degrees by edge
transfers. A positive uncovered-pair count means the graph is not a target.
"""
from pathlib import Path
import json
import time

base = Path(__file__).parent
started = time.monotonic()
rows = [tuple(map(int, s.split())) for s in (base/'brown57.edges').read_text().splitlines()]
assert rows[0] == (57,224)
g = [0]*58
for u,v in rows[1:]:
    g[u] |= 1<<v; g[v] |= 1<<u
original = {tuple(sorted(e)) for e in rows[1:]}
C = {v for v in range(57) if g[v].bit_count()==7}
S = set(json.loads((base/'brown_dominating8_nonline/result.json').read_text())['selected'])
assert len(S)==8
def bits(mask):
    while mask:
        low=mask&-mask; yield low.bit_length()-1; mask-=low
def score():
    answer=0
    for v in range(58):
        cover=g[v]|(1<<v)
        for u in bits(g[v]): cover |= g[u]
        answer += 58-cover.bit_count()
    return answer//2
def transfer(s,c,u):
    g[s]^=1<<u; g[u]^=1<<s
    g[c]^=1<<u; g[u]^=1<<c
for s in S:
    g[s]|=1<<57; g[57]|=1<<s
initial_uncovered=score()
assert initial_uncovered==0
over = S-C; under=C-S; steps=[]
while over:
    best=None
    for s in sorted(over):
        for c in sorted(under):
            for u in bits(g[s]&~(1<<57)&~(1<<c)&~g[c]):
                transfer(s,c,u)
                candidate=(score(),s,c,u)
                transfer(s,c,u)
                if best is None or candidate<best: best=candidate
    assert best is not None
    value,s,c,u=best
    transfer(s,c,u);over.remove(s);under.remove(c)
    steps.append(dict(old_edge=[s,u],new_edge=[c,u],uncovered_pairs=value))
assert all(mask.bit_count()==8 for mask in g)
edges=[(u,v) for u in range(58) for v in bits(g[u]) if u<v]
assert len(edges)==232
out=base/'brown_dominating8_nonline/degree_repaired58.edges'
out.write_text('58 232\n'+''.join(f'{u} {v}\n' for u,v in edges))
now_old={(u,v) for u,v in edges if v<57}
report=dict(status='candidate_requires_independent_verification' if score()==0 else 'diagnostic_not_a_target_graph',
            selected=sorted(S),initial_uncovered_pairs_before_degree_repair=initial_uncovered,
            final_uncovered_pairs=score(),old_deletions=len(original-now_old),old_additions=len(now_old-original),
            seconds=time.monotonic()-started,steps=steps)
(out.parent/'degree_repair.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

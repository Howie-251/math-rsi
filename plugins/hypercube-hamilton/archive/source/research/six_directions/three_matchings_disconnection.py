"""Finite basis for blocking at most three boundary pairings.

For N=6,8 normalize the first perfect matching and certify every ordered
pair of the others by an explicit matching D disconnected from all three.
For larger even N, the proof uses a greedy shared-edge argument.
"""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
def pairings(vs):
    if not vs:yield frozenset();return
    a=vs[0]
    for b in vs[1:]:
        for p in pairings(tuple(v for v in vs if v not in (a,b))):yield p|{(a,b)}
def connected(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    seen={0};todo=[0]
    while todo:
        for b in adj[todo.pop()]:
            if b not in seen:seen.add(b);todo.append(b)
    return len(seen)==n
def main():
    families=[]
    for n in (6,8):
        ms=list(pairings(tuple(range(n))));full=(1<<len(ms))-1
        masks=[sum(1<<j for j,D in enumerate(ms) if not connected(n,D|P)) for P in ms]
        witness=[]
        for a in range(len(ms)):
            for b in range(len(ms)):
                valid=masks[0]&masks[a]&masks[b];assert valid
                d=(valid&-valid).bit_length()-1
                assert all(not connected(n,ms[d]|ms[k]) for k in (0,a,b))
                witness.append(d)
        families.append(dict(n=n,matchings=[sorted(p) for p in ms],base_index=0,
            ordered_pairs=len(witness),witness_D_indices=witness))
    out=dict(status='PASS_FINITE_BASIS',scope='N6/N8 all triples after fixing first perfect matching',
        families=families,larger_even_N='Analytic greedy selection for N>=10; see proof',full_p6_proved=False)
    (R/'three_matchings_disconnection.json').write_text(json.dumps(out)+'\n')
    print([(x['n'],len(x['matchings']),x['ordered_pairs']) for x in families])
if __name__=='__main__':main()

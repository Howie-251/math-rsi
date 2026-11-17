"""Independent complete checks of five explicit fixtures; Linux execution only."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import heapq
import json
import platform
import resource
import time

HERE = Path(__file__).resolve().parent


def analyze(names, colors):
    n = len(names)
    vs = tuple(range(n))
    def color(t):
        return colors[tuple(t)]
    def label(s):
        return [names[x] for x in s]
    paths = {c: [] for c in 'RB'}
    endpoints = {c: defaultdict(int) for c in 'RB'}
    for size in range(1, n + 1):
        for s in combinations(vs, size):
            for c in 'RB':
                local = all(color(s[j:j+3]) == c for j in range(size-2))
                global_ = all(color(t) == c for t in combinations(s, 3))
                assert local == global_, ('path closure', s, c)
                if global_:
                    paths[c].append(s)
                    if size >= 2:
                        endpoints[c][s[0], s[-1]] = max(size, endpoints[c][s[0], s[-1]])
    packets = []
    for q in combinations(vs, 4):
        word = ''.join(color(t) for t in combinations(q, 3))
        # combinations order is abc,abd,acd,bcd.
        assert sum(a != b for a, b in zip(word, word[1:])) <= 1, (q, word)
        packets.append({'points': label(q), 'word': word})
    endpoint_rows = [{'points': label(st), 'R': endpoints['R'][st], 'B': endpoints['B'][st],
                      'sum': endpoints['R'][st]+endpoints['B'][st]} for st in combinations(vs, 2)]
    assert max(r['sum'] for r in endpoint_rows) <= 8, 'weak7'
    assert max(map(len, paths['R'])) <= 6, 'R7'
    assert max(map(len, paths['B'])) <= 5, 'B6'
    pairs = list(combinations(vs, 2))
    edges = {p: set() for p in pairs}
    for (a,b,c), paint in colors.items():
        order = [(a,b),(a,c),(b,c)]
        if paint == 'B':
            order.reverse()
        for p,q in combinations(order,2):
            edges[p].add(q)
    degree = {p:0 for p in pairs}
    for out in edges.values():
        for q in out:
            degree[q] += 1
    queue = [p for p in pairs if not degree[p]]
    heapq.heapify(queue)
    order = []
    while queue:
        p = heapq.heappop(queue)
        order.append(p)
        for q in sorted(edges[p]):
            degree[q]-=1
            if not degree[q]: heapq.heappush(queue,q)
    assert len(order) == len(pairs), 'pair-order cycle'
    rank = {p:i for i,p in enumerate(order)}
    pn = {}
    for u in vs:
        incident = sorted((p for p in pairs if u in p), key=rank.__getitem__)
        assert all(q in edges[incident[0]] for q in incident[1:])
        pn[u] = next(x for x in incident[0] if x != u)
    plus = {u for u in vs if u < pn[u]}
    minus = set(vs)-plus
    def fam(c,k,inside=None):
        return [p for p in paths[c] if len(p)==k and (inside is None or set(p)<=inside)]
    g = {p[-1] for p in fam('R',5,plus)} & {p[0] for p in fam('B',4,plus)}
    h,r = minus|g, plus-g
    red6,blue5 = fam('R',6),fam('B',5)
    sr = {p[0] for p in red6}
    sb = {p[0] for p in blue5}
    locks=[]
    for s in sorted(sr&sb):
        t={p[-1] for p in red6 if p[0]==s}
        q={p[1] for p in blue5 if p[0]==s}
        locks.append({'source':names[s],'T':label(sorted(t)),'Q':label(sorted(q)),
                      'locked':len(t|q)==1})
    h_sources=sr&h
    w={p[-1] for p in red6 if p[0] in h and p[-1] in r}
    return {'names':names, 'triples':[{'points':label(t),'color':c} for t,c in colors.items()],
            'packets':packets, 'all_subset_paths':{c:[label(p) for p in ps] for c,ps in paths.items()},
            'endpoint_maxima':endpoint_rows,'max_endpoint_sum':max(z['sum'] for z in endpoint_rows),
            'max_R':max(map(len,paths['R'])),'max_B':max(map(len,paths['B'])),
            'R6':[label(p) for p in red6],'B5':[label(p) for p in blue5],
            'SrcR6':label(sorted(sr)),'SrcB5':label(sorted(sb)),
            'p':{names[u]:names[v] for u,v in pn.items()},
            'pair_linear_extension':[label(p) for p in order],
            'Pplus':label(sorted(plus)),'Pminus':label(sorted(minus)), 'G':label(sorted(g)),
            'H':label(sorted(h)),'R':label(sorted(r)), 'H_ambient_R6_sources':label(sorted(h_sources)),
            'locks':locks,'F':[z['source'] for z in locks if z['locked']], 'W':label(sorted(w))}


def geometry(names,points):
    colors={}
    for t in combinations(range(len(names)),3):
        (a,b,c)=[points[x] for x in t]
        det=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        assert det != 0
        colors[t]='R' if det>0 else 'B'
    return colors


def main():
    assert platform.system()=='Linux'
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    start=time.monotonic()
    results={}
    n7=['u','a','b','z','c','d','e']
    b7={(0,1,3),(0,2,3),(1,2,3)}
    results['7']=analyze(n7,{t:'B' if t in b7 else 'R' for t in combinations(range(7),3)})
    n8=['a1','a2','m1','m2','m3','m4','b1','b2']
    results['8']=analyze(n8,{t:'B' if (t[0]<2 and t[1]<2 and 2<=t[2]<6) or (2<=t[0]<6 and t[1]>=6) else 'R' for t in combinations(range(8),3)})
    n11=['p0','p1','p2','p3','u']+['h'+str(j) for j in range(1,6)]+['v']
    points=[(-rr,10*rr**2-130*rr) for rr in [4,3,2,1,0]]+[(j,100*j*j-400*j+({3:1,5:5}.get(j,0))) for j in range(1,6)]+[(6,800)]
    results['11']=analyze(n11,geometry(n11,points))
    n12=n11+['w']
    results['12']=analyze(n12,geometry(n12,points+[(7,701)]))
    n13=['v','u','a-','a','b-','b','z-','z','c-','c','d-','d','e']
    projection=[None,0,1,1,2,2,3,3,4,4,5,5,6]
    colors={}
    for t in combinations(range(13),3):
        a,b,c=t
        if a==0:
            paint='R' if c==12 else 'B'
        else:
            pa,pb,pc=[projection[x] for x in t]
            if pa==pb: paint='R'
            elif pb==pc: paint='B'
            else: paint='B' if (pa,pb,pc) in b7 else 'R'
        colors[t]=paint
    results['13']=analyze(n13,colors)
    assert results['8']['H']==n8[2:] and results['8']['R']==n8[:2]
    assert results['11']['H']==n11[5:] and results['11']['R']==n11[:5]
    assert results['12']['H']==n12[5:10]+['w'] and results['12']['R']==n12[:5]+['v']
    assert results['13']['p']['u']=='z' and set(['a','b','c','d','e'])<=set(results['13']['H'])
    assert all(not r['F'] and not r['W'] for r in results.values())
    assert all(not results[n]['B5'] for n in ['7','8','11','12'])
    assert [list(p) for p in results['13']['SrcR6']]==[list(p) for p in ['u','a-','b-']]
    report={'scope':'Independent deterministic full checks of five explicit finite fixtures; no general proof/acceptance',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'PASS','seconds':time.monotonic()-start,'fixtures':results}
    with (HERE/'finite_fixtures_result.json').open('x') as out: json.dump(report,out,indent=2)
    print(json.dumps({'status':'PASS','seconds':report['seconds'],
                      'fixtures':{n:{k:r[k] for k in ['max_R','max_B','max_endpoint_sum','p','H','R','F','W','SrcR6','H_ambient_R6_sources']} for n,r in results.items()}},indent=2))


if __name__=='__main__': main()

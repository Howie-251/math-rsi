"""Independent positive checks and exact complementary-factor negatives.

Does not use the block-DFS producer. Exhausts new-degree completions by
choosing the two edges at the sole free retained vertex, then a short matching.
"""
import itertools,json,hashlib,collections
from pathlib import Path
R=Path(__file__).resolve().parent
V=set(range(16))
edge=lambda a,b:tuple(sorted((a,b)))
def pairings(vs,short=False,forbidden=frozenset()):
    if not vs:yield frozenset();return
    a=min(vs)
    for b in sorted(vs-{a}):
        if edge(a,b) in forbidden or (short and (a^b).bit_count()!=1):continue
        for f in pairings(vs-{a,b},short,forbidden):yield f|{edge(a,b)}
def components(vertices,edges):
    adj={v:[] for v in vertices}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    assert all(len(n)==2 for n in adj.values())
    unseen=set(vertices);sizes=[]
    while unseen:
        stack=[unseen.pop()];size=0
        while stack:
            a=stack.pop();size+=1
            for b in adj[a]:
                if b in unseen:unseen.remove(b);stack.append(b)
        sizes.append(size)
    return tuple(sorted(sizes))
def main():
    reports=[]
    for omitted in ((3,5,1),(3,6,1)):
        name='q4_three_avoided_%d_%d_%d.bin'%omitted
        data=(R/name).read_bytes();holes={0,*omitted};support=V-set(omitted)
        universe=set(pairings(V-holes));assert len(universe)==10395 and len(data)==10395*29
        negatives=[];positive=0
        for off in range(0,len(data),29):
            m=data[off:off+16];cycle=data[off+16:off+29]
            assert {v for v in V if m[v]==255}==holes
            assert all(v!=m[v] and m[m[v]]==v for v in V-holes)
            f=frozenset((v,m[v]) for v in V-holes if v<m[v]);assert f in universe;universe.remove(f)
            if cycle!=bytes([255])*13:
                p=list(cycle);assert len(set(p))==13 and set(p)==support
                edges={edge(a,b) for a,b in zip(p,p[1:]+p[:1])}
                assert f<=edges and all((a^b).bit_count()==1 for a,b in edges-f);positive+=1
            else:
                hist=collections.Counter();neighbors={v for v in support if v.bit_count()==1}
                for a,b in itertools.combinations(sorted(neighbors),2):
                    for short in pairings(support-{0,a,b},True,f):
                        added=short|{edge(0,a),edge(0,b)}
                        assert len(added)==7 and not added&f
                        sizes=components(support,f|added);assert len(sizes)>1
                        hist[sizes]+=1
                negatives.append(dict(matching=sorted(f),completion_count=sum(hist.values()),
                    component_size_histogram={str(k):v for k,v in sorted(hist.items())}))
        assert not universe
        reports.append(dict(holes=sorted(holes),omitted=list(omitted),positive=positive,negative=len(negatives),
            negative_records=negatives,input_sha256=hashlib.sha256(data).hexdigest()))
    result=dict(status='PASS',scope='Two complete marked Q4 three-avoided geometries, all K matchings',
        negative_basis='All possible short new-degree completions independently enumerated; every union disconnected',
        families=reports,full_t15_proved=False,full_p6_proved=False)
    (R/'q4_three_avoided_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([dict(omitted=r['omitted'],positive=r['positive'],negative=r['negative'],
        negative_completions=sum(t['completion_count'] for t in r['negative_records'])) for r in reports]))
if __name__=='__main__':main()

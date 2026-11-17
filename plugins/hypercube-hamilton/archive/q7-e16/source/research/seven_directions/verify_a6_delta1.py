"""Independent exhaustive domain/orbit/barrier verification, standard library only."""
import json
from itertools import combinations, permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def bitperm(v, p):
    return sum(((v >> j)&1) << p[j] for j in range(6))

def regenerate():
    odds=[x for x in range(64) if x.bit_count()%2]
    remaining=set()
    total=0
    for q in (3,15,63):
        allowed=[x for x in odds if x.bit_count()!=1 and (x^q).bit_count()!=1]
        for triple in combinations(allowed,3):
            for z in odds:
                if z in triple: continue
                total+=1
                usable=False
                for j in range(6):
                    side=[v for v in (0,q,z,*triple) if ((v^z)>>j)&1 == 0]
                    e=sum(v.bit_count()%2==0 for v in side)
                    o=len(side)-e
                    if o-e in (2,3) or (e,o)==(0,1):
                        usable=True
                        break
                if not usable: remaining.add((q,z,tuple(triple)))
    assert total==110780 and len(remaining)==3012
    return remaining

def graph(row):
    q=row['minority'][1]
    z=row['forbidden']
    H={0,q,z,*row['other_majority']}
    anchors={}
    for j in range(6):
        e=[v for v in (0,q) if not ((v^z)&(1<<j))]
        o=[v for v in (z,*row['other_majority']) if not ((v^z)&(1<<j))]
        if len(e)==1 and len(o)==2:
            anchors[j]=e[0]^(1<<j)
            assert anchors[j] not in H
    adj={v:set() for v in range(64) if v not in H}
    for a,b in combinations(adj,2):
        if all(not ((a^b)&(1<<j)) or a==w or b==w for j,w in anchors.items()):
            adj[a].add(b)
            adj[b].add(a)
    return adj,anchors

def components(adj, removed):
    unseen=set(adj)-removed
    result=[]
    while unseen:
        start=min(unseen)
        unseen.remove(start)
        todo=[start]
        comp={start}
        while todo:
            v=todo.pop()
            fresh=adj[v]&unseen
            unseen-=fresh
            comp|=fresh
            todo.extend(fresh)
        result.append(comp)
    return result

def main():
    target=regenerate()
    data=json.loads((ROOT/'A6_DELTA1_PROBE.json').read_text(encoding='utf-8'))
    covered=set()
    counts={'TUTTE_CERTIFICATE':0,'METHOD_RESIDUAL':0}
    geom={k:0 for k in counts}
    groups={q:[p for p in permutations(range(6)) if bitperm(q,p)==q] for q in (3,15,63)}
    for record in data['records']:
        row=record['representative']
        q=row['minority'][1]
        orbit=set()
        for p in groups[q]:
            z=bitperm(row['forbidden'],p)
            w=[bitperm(v,p) for v in row['other_majority']]
            for flip in (0,q):
                orbit.add((q,z^flip,tuple(sorted(v^flip for v in w))))
        assert not (covered&orbit)
        assert orbit<=target and len(orbit)==record['size']
        covered|=orbit
        adj,anchors=graph(row)
        assert anchors=={int(j):w for j,w in record['delta1_anchors'].items()}
        status=record['status']
        counts[status]+=1
        geom[status]+=len(orbit)
        if status=='TUTTE_CERTIFICATE':
            barrier=record['barrier']
            removed=set(barrier['removed'])
            assert len(removed)==len(barrier['removed']) and removed<=set(adj)
            odd=[c for c in components(adj,removed) if len(c)%2]
            assert len(odd)>len(removed)
            assert {tuple(sorted(c)) for c in odd}=={tuple(c) for c in barrier['odd_components']}
        else:
            M=record['perfect_matching']
            flat=[v for e in M for v in e]
            assert len(flat)==len(set(flat))==58 and set(flat)==set(adj)
            assert all(b in adj[a] for a,b in M)
            for j,w in anchors.items():
                cross=[e for e in M if (e[0]^e[1])&(1<<j)]
                assert len(cross)==1 and w in cross[0]
    assert covered==target and counts==data['statuses'] and geom==data['status_geometries']
    result=dict(status='PASS', regenerated_normalized_domain=110780, regenerated_residual=3012,
                explicit_group_orbits=len(data['records']), status_orbits=counts, status_geometries=geom,
                solver_used=False, full_A6_6_proved=False, full_P7_proved=False)
    (ROOT/'A6_DELTA1_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__': main()

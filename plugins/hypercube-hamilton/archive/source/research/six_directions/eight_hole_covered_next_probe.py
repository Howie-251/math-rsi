"""Diagnostic finite checks for the next covered reductions; no closure certificate."""
from pathlib import Path
import json

B=Path(__file__).resolve().parent
pc=int.bit_count
examples=[(1,[3,5,9],[14,31,47,62]),(7,[3,5,6],[8,16,32,56]),
          (7,[3,5,15],[8,25,41,56]),(7,[3,15,23],[25,26,56,59]),
          (7,[15,23,39],[56,59,61,62]),(31,[15,23,27],[1,2,32,35]),
          (31,[15,23,63],[32,35,37,38])]
results=[]
for v,z,w in examples:
    holes={0,*z,*w}
    for i in range(6):
        inA=lambda x: ((x^v)&(1<<i))==0
        if sum(map(inA,z))!=2 or any(map(inA,w)): continue
        S={x^(1<<i) for x in w}
        # Try to realize this geometry with no possible exposed-port edge.
        def allowed(a,b):
            if pc(a^b)!=1:return False
            if inA(a)==inA(b):return True
            x=a if inA(a) else b
            return pc(x)%2==0 or all(pc(x^s)!=1 for s in S)
        ev=[x for x in range(64) if x not in holes and pc(x)%2==0]
        od=[x for x in range(64) if x not in holes and pc(x)%2==1]
        adj={a:[b for b in od if allowed(a,b)] for a in ev}
        mate={}
        def augment(a,seen):
            for b in adj[a]:
                if b in seen:continue
                seen.add(b)
                if b not in mate or augment(mate[b],seen):
                    mate[b]=a;return True
            return False
        feasible=all(augment(a,set()) for a in ev)
        item={'target':v,'Z':z,'W':w,'cut':i,'delta':int(inA(0)),
              'no_exposure_matching_found':feasible}
        if feasible:
            matching=sorted([[a,b] for b,a in mate.items()])
            assert len(matching)==28 and len({x for e in matching for x in e})==56
            assert all(pc(a^b)==1 for a,b in matching)
            assert set(range(64))-{x for e in matching for x in e}==holes
            X={a if inA(a) else b for a,b in matching if inA(a)!=inA(b)}
            oddports={x for x in X if pc(x)%2}
            assert all(pc(q^s)!=1 for q in oddports for s in S)
            item.update(matching=matching,odd_ports=sorted(oddports),mirror_holes=sorted(S))
        results.append(item)
joint=[]
for v,z,w in examples:
    holes={0,*z,*w}
    cuts=[i for i in range(6) if sum(((x^v)&(1<<i))==0 for x in z)==2
          and not any(((x^v)&(1<<i))==0 for x in w)]
    def joint_allowed(a,b):
        if pc(a^b)!=1:return False
        for i in cuts:
            ina=lambda x:((x^v)&(1<<i))==0
            if ina(a)==ina(b):continue
            x=a if ina(a) else b
            if pc(x)%2 and any(pc(x^(t^(1<<i)))==1 for t in w):return False
        return True
    ev=[x for x in range(64) if x not in holes and pc(x)%2==0]
    od=[x for x in range(64) if x not in holes and pc(x)%2==1]
    adj={a:[b for b in od if joint_allowed(a,b)] for a in ev}
    mate={}
    def augment(a,seen):
        for b in adj[a]:
            if b in seen:continue
            seen.add(b)
            if b not in mate or augment(mate[b],seen):
                mate[b]=a;return True
        return False
    for a in ev:augment(a,set())
    feasible=len(mate)==len(ev)
    item={'target':v,'Z':z,'W':w,'cuts':cuts,'simultaneous_no_exposure_matching_found':feasible}
    if feasible:
        matching=sorted([[a,b] for b,a in mate.items()])
        assert len(matching)==28 and len({x for e in matching for x in e})==56
        assert all(pc(a^b)==1 for a,b in matching)
        assert set(range(64))-{x for e in matching for x in e}==holes
        for i in cuts:
            ina=lambda x:((x^v)&(1<<i))==0
            X={a if ina(a) else b for a,b in matching if ina(a)!=ina(b)}
            assert all(pc(q^(t^(1<<i)))!=1 for q in X if pc(q)%2 for t in w)
        item['matching']=matching
    else:
        reached=set(ev)-set(mate.values())
        frontier=list(reached)
        while frontier:
            a=frontier.pop()
            for b in adj[a]:
                if b in mate and mate[b] not in reached:
                    reached.add(mate[b]);frontier.append(mate[b])
        neighbours={b for a in reached for b in adj[a]}
        assert len(neighbours)<len(reached)
        item['hall_even_subset']=sorted(reached)
        item['hall_odd_neighbours']=sorted(neighbours)
        item['hall_deficiency']=len(reached)-len(neighbours)
    joint.append(item)
out={'scope':'diagnostic only; not a proof of T15 or covered closure','results':results,'joint_results':joint}
(B/'eight_hole_covered_next_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(results),'no_exposure_matchings':sum(x['no_exposure_matching_found'] for x in results),
                  'joint_cases':len(joint),'joint_no_exposure_matchings':sum(x['simultaneous_no_exposure_matching_found'] for x in joint)}))

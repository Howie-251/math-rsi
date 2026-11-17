"""Finite Q7 reconnaissance. Positive witnesses only; no timeout is a negative proof."""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
import json, random, time, hashlib
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix

ROOT=Path(__file__).resolve().parent
def dump(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
def parity(v): return v.bit_count()%2
def short(a,b): return a!=b and (a^b)&((a^b)-1)==0
def cube_edges(n):
    return [(x,x^(1<<i)) for x in range(1<<n) for i in range(n) if not x&(1<<i)]
def check_matching(n,M,holes=None):
    endpoints=[v for e in M for v in e]
    assert len(set(endpoints))==len(endpoints) and all(0<=v<1<<n for v in endpoints)
    if holes is not None: assert set(range(1<<n))-set(endpoints)==set(holes)
def check_cycle(n,M,z,cycle):
    assert len(cycle)==(1<<n)-1 and set(cycle)==set(range(1<<n))-{z}
    edges={tuple(sorted((cycle[i],cycle[(i+1)%len(cycle)]))) for i in range(len(cycle))}
    required={tuple(sorted(e)) for e in M}
    assert required<=edges
    assert all(short(a,b) for a,b in edges-required)

def geometry_census():
    odd=[x for x in range(64) if parity(x)]
    nonadj=[x for x in odd if x.bit_count()>1]
    domain={(z,a,b) for a,b in combinations(nonadj,2) for z in odd if z not in (a,b)}
    assert len(domain)==9750
    maps=[]
    for p in permutations(range(6)):
        maps.append([sum(((x>>p[j])&1)<<j for j in range(6)) for x in range(64)])
    remaining=set(domain); orbits=[]
    while remaining:
        rep=min(remaining);z,a,b=rep
        orbit={(m[z],*sorted((m[a],m[b]))) for m in maps}
        assert orbit<=domain and orbit<=remaining
        remaining-=orbit
        good=[i for i in range(6) if z&(1<<i) and bool(a&(1<<i))!=bool(b&(1<<i))]
        mask=sum(1<<i for i in good)
        blocks=Counter(x&mask for x in range(64) if x not in (0,z,a,b))
        forced=bool(good) and any(v%2 for v in blocks.values())
        orbits.append({'representative':list(rep),'size':len(orbit),
                       'z_weight':z.bit_count(),'span':(z|a|b).bit_count(),
                       'good_directions':good,'crossing_forced_by_odd_block':forced})
    result={'minority_hole':0,'domain_count':len(domain),'orbit_count':len(orbits),
            'group':'all 720 coordinate permutations; forbidden majority hole is marked',
            'orbits':orbits,'raw_domain_sha256':hashlib.sha256(json.dumps(sorted(domain)).encode()).hexdigest(),
            'universally_closed_orbits_by_positive_cut':sum(o['crossing_forced_by_odd_block'] for o in orbits),
            'universally_closed_geometries_by_positive_cut':sum(o['size'] for o in orbits if o['crossing_forced_by_odd_block'])}
    dump('Q6_A4_GEOMETRY.json',result)
    return orbits

def prescribed_matching(holes,kind,rng):
    available=set(range(64))-set(holes); M=[]
    if kind=='zero_good_crossings':
        _,z,a,b=holes
        good=[i for i in range(6) if z&(1<<i) and bool(a&(1<<i))!=bool(b&(1<<i))]
        if not good:return None
        mask=sum(1<<i for i in good)
        blocks={signature:sorted(v for v in available if v&mask==signature) for signature in {v&mask for v in available}}
        if any(len(vertices)%2 for vertices in blocks.values()):return None
        for vertices in blocks.values():
            rng.shuffle(vertices);M.extend(zip(vertices[::2],vertices[1::2]))
        M=sorted(tuple(sorted(e)) for e in M);check_matching(6,M,holes)
        return M
    if kind=='half_layer':
        good=[i for i in range(6) if all(not ({a,b}&set(holes)) for a,b in cube_edges(6)
              if (a^b)==1<<i and parity(a if not a&(1<<i) else b)==1)]
        if not good:return None
        i=good[0]
        M=[(a,b) for a,b in cube_edges(6) if (a^b)==1<<i and parity(a if not a&(1<<i) else b)==1]
        for a,b in M:available.remove(a);available.remove(b)
    if kind=='uniform':
        vertices=sorted(available);rng.shuffle(vertices)
        M.extend(zip(vertices[::2],vertices[1::2]))
    else:
        evens=sorted(x for x in available if not parity(x));odds=sorted(x for x in available if parity(x))
        rng.shuffle(evens);rng.shuffle(odds)
        assert len(evens)==len(odds)+2
        M.append((evens.pop(),evens.pop()))
        M.extend(zip(evens,odds))
    M=[tuple(sorted(e)) for e in M];check_matching(6,M,holes)
    return sorted(M)

def solve_cycle(M,z,seconds=3):
    t0=time.monotonic();vertices=sorted(set(range(64))-{z});index={v:i for i,v in enumerate(vertices)}
    required=set(M);es=sorted(required|{e for e in cube_edges(6) if z not in e})
    E=len(es);lo=np.array([int(e in required) for e in es],float)
    incidence=np.zeros((len(vertices),E))
    for j,(a,b) in enumerate(es):incidence[index[a],j]=incidence[index[b],j]=1
    cuts=[];cut_bounds=[];rounds=0
    while time.monotonic()-t0<seconds:
        rows=np.vstack([incidence,*cuts]) if cuts else incidence
        lb=[2.]*len(vertices)+[-np.inf]*len(cuts)
        ub=[2.]*len(vertices)+cut_bounds
        res=milp(np.zeros(E),integrality=np.ones(E),bounds=Bounds(lo,np.ones(E)),
          constraints=LinearConstraint(csc_matrix(rows),lb,ub),
          options={'time_limit':max(.01,seconds-(time.monotonic()-t0)),'mip_rel_gap':0})
        rounds+=1
        if res.x is None:
            return {'status':'SOLVER_INFEASIBLE_UNCERTIFIED' if res.status==2 else 'UNKNOWN',
                    'rounds':rounds,'seconds':time.monotonic()-t0}
        bits=np.rint(res.x)
        if np.max(np.abs(bits-res.x))>1e-6 or not np.array_equal(incidence@bits,np.full(len(vertices),2)):
            return {'status':'UNKNOWN','rounds':rounds,'seconds':time.monotonic()-t0}
        assert np.all(bits>=lo)
        adj={v:[] for v in vertices}
        for j,(a,b) in enumerate(es):
            if bits[j]:adj[a].append(b);adj[b].append(a)
        unseen=set(vertices);components=[]
        while unseen:
            first=min(unseen); todo=[first];comp=set()
            while todo:
                v=todo.pop()
                if v in comp:continue
                comp.add(v);unseen.discard(v);todo.extend(w for w in adj[v] if w not in comp)
            components.append(comp)
        if len(components)==1:
            cycle=[vertices[0]];previous=None
            while True:
                nxt=next(v for v in adj[cycle[-1]] if v!=previous)
                if nxt==cycle[0]:break
                previous=cycle[-1];cycle.append(nxt)
            check_cycle(6,M,z,cycle)
            return {'status':'FOUND','cycle':cycle,'rounds':rounds,'seconds':time.monotonic()-t0}
        for comp in components:
            row=np.array([int(a in comp and b in comp) for a,b in es],float)
            cuts.append(row);cut_bounds.append(len(comp)-1)
    return {'status':'UNKNOWN','rounds':rounds,'seconds':time.monotonic()-t0}

def rooted_witness():
    old=ROOT.parent/'six_directions'/'rooted_23_matching.json'
    L=[tuple(e) for e in json.loads(old.read_text(encoding='utf-8'))['matching']]
    H=set(range(64))-{x for e in L for x in e};assert 0 in H
    a=min(x for x in H if short(0,x));full=L+[(0,a)]
    best=None
    for t in range(64):
        M=L+[(64+(x^t),64+(y^t)) for x,y in full]
        free=set(range(128))-{x for e in M for x in e}
        for x in range(1,64):
            if x in free and x+64 in free:M.append((x,x+64));free-={x,x+64}
        if best is None or len(M)<len(best):best=M
    check_matching(7,best)
    covered={x for e in best for x in e};assert 0 not in covered
    assert all(short(a,b) for a,b in best)
    assert all(a in covered or b in covered for a,b in cube_edges(7) if a and b)
    result={'status':'EXPLICIT_WITNESS','root':0,'matching':best,'size':len(best),
            'holes':sorted(set(range(128))-covered),'sharp_bound_claimed':False}
    dump('Q7_ROOTED_WITNESS.json',result)
    print('rooted witness',len(best),'edges',128-2*len(best),'holes',flush=True)

def main():
    t0=time.monotonic();rooted_witness();orbits=geometry_census();print('A4 geometries',9750,'orbits',len(orbits),flush=True)
    rng=random.Random(20261102);cases=[]
    for i,orbit in enumerate(orbits):
        z,a,b=orbit['representative'];holes=[0,z,a,b]
        for kind in ('uniform','parity_mixed','half_layer','zero_good_crossings'):
            M=prescribed_matching(holes,kind,rng)
            if M is None:continue
            result=solve_cycle(M,z)
            cases.append({'orbit':i,'kind':kind,'holes':holes,'forbidden':z,'matching':M,**result})
        print(i+1,len(orbits),dict(Counter(c['status'] for c in cases)),flush=True)
        dump('Q6_A4_PILOT.json',{'scope':'finite positive samples, NOT universal A4','seed':20261102,'cases':cases,
                              'summary':dict(Counter(c['status'] for c in cases)),'seconds':time.monotonic()-t0})

if __name__=='__main__':main()

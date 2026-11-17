"""Exact final geometric cover and transports; does not assert certificate acceptance."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
def perm(v,p):return sum(((v>>j)&1)<<p[j] for j in range(len(p)))
def project(v,j):return (v&((1<<j)-1))|((v>>(j+1))<<j)

def main():
    odds=[v for v in range(64) if v.bit_count()%2]
    counts=Counter();remaining=set()
    for q in (3,15,63):
        good=[v for v in odds if v.bit_count()!=1 and (v^q).bit_count()!=1]
        for W in combinations(good,3):
            for z in odds:
                if z in W:continue
                cuts=[]
                for j in range(6):
                    e=sum(not ((v^z)&(1<<j)) for v in (0,q))
                    o=sum(not ((v^z)&(1<<j)) for v in (z,*W))
                    cuts.append((e,o))
                if any(o-e==2 for e,o in cuts):kind='D2'
                elif any(o-e==3 for e,o in cuts):kind='D3'
                elif (0,1) in cuts:kind='I1'
                elif any(o-e==1 and e in (1,2) for e,o in cuts):kind='D1_full'
                else:kind='LAST_CORES';remaining.add((q,z,W))
                counts[kind]+=1
    p6=[p for p in permutations(range(6)) if perm(3,p)==3]
    cores=[dict(minority=[0,3],forbidden=2,other_majority=[13,49,61]),
           dict(minority=[0,3],forbidden=7,other_majority=[28,44,52])]
    cover=set()
    for core in cores:
        orbit={(3,perm(core['forbidden'],p)^flip,tuple(sorted(perm(w,p)^flip for w in core['other_majority'])))
               for p in p6 for flip in (0,3)}
        assert not cover&orbit
        core['normalized_orbit_size']=len(orbit)
        cover|=orbit
    assert cover==remaining and counts['LAST_CORES']==14 and sum(counts.values())==110780
    transports=[]
    def add_transport(kind,j,holes,omit):
        H=sorted(project(v,j) for v in holes)
        U=sorted(project(v,j) for v in omit)
        found=None
        for shift in U:
            for p in permutations(range(5)):
                if sorted(perm(v^shift,p) for v in H)==[0,3,5,27] and sorted(perm(v^shift,p) for v in U)==[0,5]:
                    found=dict(xor=shift,permutation=p);break
            if found:break
        assert found
        transports.append(dict(kind=kind,cut_coordinate=j,global_holes=sorted(holes),global_omit=sorted(omit),
                               local_holes=H,local_omit=U,transport=found))
    W=cores[0]['other_majority']
    for j in range(2,6):
        Bholes=[v for v in W if v&(1<<j)]
        assert len(Bholes)==2
        bridges=[1<<j,(1<<j)^3]
        assert not set(bridges)&{0,3,2,*W}
        add_transport('all_zero_core',j,Bholes+bridges,bridges)
    W=cores[1]['other_majority']
    for t,s in combinations(W,2):
        mirrors=[t^4,s^4]
        assert not set(mirrors)&{0,3,7,*W}
        add_transport('delta4_core',2,[0,3,*mirrors],mirrors)
    S={v for v in range(64) if (v>>2).bit_count()<=1}
    H={0,3,2,13,49,61}
    assert len(S)==20 and S&H=={0,3,2} and len(S-H)==17
    for a in S:
        for b in set(range(64))-S:
            assert any(not (a&(1<<j)) and (b&(1<<j)) and b not in (1<<j,(1<<j)^3) for j in range(2,6))
    result=dict(status='GEOMETRY_PASS_ONLY',rank_certificates_independently_accepted=False,
                full_A6_6_proved=False,total_normalized=110780,counts=dict(counts),cores=cores,
                remaining_configurations=[dict(q=q,z=z,W=w) for q,z,w in sorted(remaining)],
                transport_count=len(transports),transports=transports,
                odd_set_certificate=dict(vertices=sorted(S),holes=sorted(S&H),covered_count=17))
    (ROOT/'A6_FINAL_TRANSPORT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('transports','remaining_configurations','odd_set_certificate')},ensure_ascii=False))

if __name__=='__main__':main()

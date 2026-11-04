"""Complete short-complement forest spectrum for the last marked A10 orbit.

Producer only. No matching-extension sampling and no universal-F assertion.
P record:22 bytes, canonical sorted original-label endpoint pairs.
Witness record:40 bytes, canonical sorted original-label short S edges.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
H={0,1,2,4,8,15,23,27,29,30};covered=tuple(sorted(set(range(32))-H));K=set(covered)
holes=sorted(H-{0});low=[x for x in holes if x.bit_count()%2];high=[x for x in holes if x not in low]
N={x:{y for y in range(1,32) if (x^y).bit_count()==1} for x in range(1,32)}
assert all(not(N[x]&set(holes)) for x in holes)
assert len(low)==4 and len(high)==5
def assignments(sources):
    out=[]
    def rec(i,used,pairs,witness):
        if i==len(sources):out.append((used,tuple(sorted(pairs)),tuple(sorted(witness))));return
        h=sources[i]
        for a,b in combinations(sorted((N[h]&K)-used),2):
            rec(i+1,used|{a,b},pairs+[(a,b)],witness+[tuple(sorted((h,a))),tuple(sorted((h,b)))])
    rec(0,set(),[],[]);return out
L=assignments(low);U=assignments(high)
assert all(len(used)==8 for used,_,_ in L)
assert all(16 not in used for used,_,_ in U)
even={x for x in K if x.bit_count()%2==0};odd=K-even
def encode(edges):return bytes(x for e in sorted(tuple(sorted(e)) for e in edges) for x in e)
spectrum={};raw_forests=0;residue_hist=Counter();partner31=Counter();partner16=Counter()
for usedL,pL,wL in L:
    remainE=sorted(even-usedL);assert len(remainE)==2
    for usedU,pU,wU in U:
        remainO=sorted(odd-usedU);assert len(remainO)==2 and 16 in remainO
        for po in (remainO,list(reversed(remainO))):
            cross=list(zip(remainE,po))
            if not all(b in N[a] for a,b in cross):continue
            raw_forests+=1
            edges=pL+pU+tuple(tuple(sorted(e)) for e in cross)
            rec=encode(edges);w=encode(wL+wU+tuple(tuple(sorted(e)) for e in cross))
            assert len(rec)==22 and set(rec)==K and len(w)==40
            if rec in spectrum:assert spectrum[rec]==w,'distinct S with same P'
            else:
                spectrum[rec]=w
                mates={}
                for a,b in edges:mates[a]=b;mates[b]=a
                partner31[mates[31]]+=1;partner16[mates[16]]+=1
            residue_hist[tuple(remainE+remainO)]+=1
records=sorted(spectrum)
(R/'A10_ORBIT3_SPECTRUM_pairs.bin').write_bytes(b''.join(records))
(R/'A10_ORBIT3_SPECTRUM_forests.bin').write_bytes(b''.join(spectrum[k] for k in records))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
out={'status':'COMPLETE_SPECTRUM_ENUMERATED_UNIVERSAL_COVERAGE_UNPROVED','holes':sorted(H),'omitted':0,
     'covered_vertex_order':covered,'low_cherry_assignments':len(L),'high_cherry_assignments':len(U),
     'low_high_assignment_pairs':len(L)*len(U),'short_complement_forests':raw_forests,'distinct_endpoint_pairings':len(records),
     'forest_to_pairing_injective':raw_forests==len(records),
     'P31_partner_counts':dict(sorted(partner31.items())),'P16_partner_counts':dict(sorted(partner16.items())),
     'leftover_terminal_choices':len(residue_hist),'matching_instances_F_enumerated':0,
     'records':{'pairs':{'file':'A10_ORBIT3_SPECTRUM_pairs.bin','record_bytes':22,'sha256':sha('A10_ORBIT3_SPECTRUM_pairs.bin')},
                'forests':{'file':'A10_ORBIT3_SPECTRUM_forests.bin','record_bytes':40,'sha256':sha('A10_ORBIT3_SPECTRUM_forests.bin')}},
     'full_A10_orbit3_proved':False,'full_A10_proved':False,'full_P6_proved':False,
     'producer_sha256':sha(Path(__file__).name)}
(R/'A10_ORBIT3_SPECTRUM_manifest.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

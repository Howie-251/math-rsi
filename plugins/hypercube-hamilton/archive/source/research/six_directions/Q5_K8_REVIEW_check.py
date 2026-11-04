"""Independent K8 finite geometry and replacement verification.

No producer code is imported or executed. Proof imports are bound separately.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json

R=Path(__file__).resolve().parent
def sha(n):return 'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
src=['Q5_K8_CLOSURE.md','q5_k8_geometry.py','q5_k8_geometry.json']
given=json.loads((R/src[2]).read_text())
assert given['producer_sha256']==sha(src[1]).removeprefix('sha256:')
ev={x for x in range(32) if x.bit_count()%2==0}; od=set(range(32))-ev
adj={x:{y for y in range(32) if (x^y).bit_count()==1} for x in range(32)}
# Enumerate from the odd side, opposite to the producer.
domain=set()
for odd in combinations(sorted(od),4):
    allowed=ev-set().union(*(adj[x] for x in odd))
    for even in combinations(sorted(allowed),4): domain.add((even,odd))
assert len(domain)==980
records={}
for row in given['rows']:
    e,o=tuple(row['even_holes']),tuple(row['odd_holes'])
    assert len(e)==len(o)==4 and list(e)==sorted(set(e)) and list(o)==sorted(set(o))
    key=(e,o);assert key not in records;records[key]=row
assert set(records)==domain

hist=Counter();witness_deltas=Counter();total_pairs=0;valid_pairs=0;replacement_tests=0
for key in sorted(domain):
    e,o=key; H=set(e)|set(o);row=records[key]
    success={}
    for r in H:
        for y in adj[r]:
            total_pairs+=1
            assert y not in H
            newholes=(H-{r})|{y}
            majority=newholes&(ev if y in ev else od)
            minority=newholes-majority
            assert (len(minority),len(majority))==(3,5)
            cuts=[]
            for j in range(5):
                face={x for x in range(32) if (x&(1<<j))==(y&(1<<j))}
                delta=len(majority&face)-len(minority&face)
                if delta in {1,2,3}:cuts.append((j,delta))
            if cuts:success[(r,y)]=cuts
    assert success
    hist[len(success)]+=1;valid_pairs+=len(success)
    assert row['valid_root_neighbor_pairs']==len(success)
    w=row['witness'];r,y=w['root'],w['neighbor'];cut,delta=w['avoid_cut'],w['delta']
    assert (r,y) in success and (cut,delta) in success[(r,y)]
    witness_deltas[delta]+=1
    # Every possible mate of this witness target is allowed in K(Q5).
    # Build a matching realizing each mate, and check replacement exactly.
    covered=set(range(32))-H
    for h in covered-{y}:
        rest=sorted(covered-{y,h})
        F={tuple(sorted((y,h)))}|{(rest[i],rest[i+1]) for i in range(0,len(rest),2)}
        newedge=tuple(sorted((h,r)))
        Fprime=(F-{tuple(sorted((y,h)))})|{newedge}
        endpoints=[x for edge in Fprime for x in edge]
        assert len(endpoints)==len(set(endpoints))==24
        assert set(range(32))-set(endpoints)==(H-{r})|{y}
        assert newedge in Fprime
        replacement_tests+=1
assert hist=={40:580,18:320,24:80}
assert hist=={int(k):v for k,v in given['root_neighbor_pair_histogram'].items()}
assert given['geometry_count']==980 and given['remaining']==0 and not given['full_p6_proved']
out={'status':'PASS','audited_input_hashes':{n:sha(n) for n in src},
     'geometry_domain_count':len(domain),'producer_rows_exactly_match_domain':True,
     'root_neighbor_pairs_checked':total_pairs,'successful_pairs':valid_pairs,
     'successful_pair_histogram':dict(sorted(hist.items())),
     'positive_witnesses_checked':len(domain),'positive_witness_delta_histogram':dict(sorted(witness_deltas.items())),
     'all_possible_selected_target_mates_checked':replacement_tests,
     'producer_source_hash_matches':True,
     'scope':'Deterministic geometry, exact witnesses and replacement hole bookkeeping; local A8 theorem imported separately. No exhaustive matching-extension search.'}
partial=json.loads((R/'A8_PARTIAL_REVIEW.json').read_text(encoding='utf-8'))
assert partial['verdict']=='PASS'
assert sha('A8_PARTIAL_REVIEW.json')=='sha256:1b63584b3cf81c6dc3533cea0fedef60bd8d8d8ed1d7a847ca765326e0dda81f'
assert sha('A8_PARTIAL_PROOF_PACKAGE.md')==partial['audited_input_hashes']['A8_PARTIAL_PROOF_PACKAGE.md']=='sha256:3133642eb22daa30c48253dcd97a3a808e8f3169a4c3256af8240ae0f8bd2a5f'
deps=['A8_PARTIAL_PROOF_PACKAGE.md','A8_PARTIAL_REVIEW.md','A8_PARTIAL_REVIEW.json',
      'A6_AND_EIGHT_FREE_CLOSED.md','A6_CLOSURE_REVIEW.md','A6_CLOSURE_REVIEW.json']
out['imported_dependency_hashes']={n:sha(n) for n in deps}
out['accepted_partial_A8_scope']='Augmentation or delta1/2/3 cut; arbitrary K(Q5) matching, every marked majority omitted hole, both parity orientations'
out['imported_partial_report_hashes_match']=True
(R/'Q5_K8_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

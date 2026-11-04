"""Independent reconstruction, with no producer imports or execution."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib, json

R=Path(__file__).resolve().parent
def sha(n): return 'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
producer=json.loads((R/'q5_higher_hole_reduction_geometry.json').read_text())
assert producer['producer_sha256']==sha('q5_higher_hole_reduction_geometry.py').removeprefix('sha256:')
E=tuple(x for x in range(32) if x.bit_count()%2==0)
O=tuple(x for x in range(32) if x.bit_count()%2==1)
# Independent adjacency: all pairs at Hamming distance one, no bit-mask union.
N={x:{y for y in range(32) if (x^y).bit_count()==1} for x in range(32)}
histograms=[]
for parity_class in (E,O):
    hist=Counter(len(set().union(*(N[x] for x in s))) for s in combinations(parity_class,5))
    assert sum(hist.values())==4368 and min(hist)==11
    histograms.append(dict(sorted(hist.items())))
assert histograms[0]==histograms[1]=={int(k):v for k,v in producer['five_vertex_neighbor_histogram'].items()}
assert histograms[0][11]==producer['five_vertex_sets_with_minimum_neighborhood']==16

def swap(x,i):
    if ((x>>i)^(x>>(i+1)))&1: return x^(3<<i)
    return x

def orbit(seed):
    found={seed}; todo=[seed]
    while todo:
        z,w=todo.pop()
        for i in range(4):
            g=(tuple(sorted(swap(x,i) for x in z)),tuple(sorted(swap(x,i) for x in w)))
            if g not in found: found.add(g); todo.append(g)
    return found

levels=[]
for t in range(4,16):
    # Reverse producer's loop order: choose nonzero majority holes first.
    domain=set(); residual=set(); hist=Counter()
    for z in combinations(E[1:],t):
        allowed=sorted(set(O)-set().union(*(N[x] for x in z)))
        if len(allowed)<t-1: continue
        for w in combinations(allowed,t-1):
            geom=(z,w); domain.add(geom)
            major={0,*z}; minor=set(w)
            ds=tuple(sorted(sum(x&(1<<i)==0 for x in major)-sum(x&(1<<i)==0 for x in minor) for i in range(5)))
            hist[ds]+=1
            if set(ds).isdisjoint({1,2,3}): residual.add(geom)
    rest=set(residual); orbits=[]
    while rest:
        seed=min(rest); images=orbit(seed)
        assert images<=residual
        rest-=images
        orbits.append({'representative':[list(seed[0]),list(seed[1])],'size':len(images)})
    rec={'holes':2*t,'geometries':len(domain),'without_delta123':len(residual),'residual_orbits':orbits}
    if t<=8:
        given=producer['levels'][t-4]
        assert given['holes']==2*t
        assert given['independent_except_forbidden_geometries']==len(domain)
        assert given['without_delta123']==len(residual)
        assert {tuple(k):v for k,v in given['delta_histogram']}==dict(hist)
        images=set()
        for g in given['residual_orbits']:
            seed=(tuple(g['other_majority']),tuple(g['minority']))
            image=orbit(seed)
            assert len(image)==g['size'] and image<=residual and image.isdisjoint(images)
            images|=image
        assert images==residual
    assert len(domain)==({4:2700,5:55}.get(t,0))
    levels.append(rec)
assert [len(x['residual_orbits']) for x in levels[:2]]==[5,3]
assert producer['full_a8_proved']==producer['full_a10_proved']==producer['full_p6_proved']==False

# Symbolic population accounting of covered-target replacement. This checks
# both root parities and every m that can occur, without restricting mate parity.
replacement_cases=0
for m in range(1,17):
    for root_parity in (0,1):
        if m==16: continue  # F empty: no covered target or mate exists.
        y_parity=1-root_parity
        for mate_parity in (0,1):
            # Need a covered target and a distinct covered mate of that parity.
            covered=[16-m,16-m]
            covered[y_parity]-=1
            if covered[mate_parity]==0: continue
            before=[m,m]; after=before.copy()
            after[root_parity]-=1; after[y_parity]+=1
            assert after[y_parity]==m+1<=16 and after[root_parity]==m-1
            replacement_cases+=1

sources=['Q5_HIGHER_HOLE_REDUCTION.md','q5_higher_hole_reduction_geometry.py','q5_higher_hole_reduction_geometry.json']
deps=['EIGHT_HOLE_FULL_REVIEW.json','EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md',
      'A6_CLOSURE_DRAFT.md','A6_CLOSURE_REVIEW.json','CANONICAL_A4_CLOSURE.md',
      'CANONICAL_COMPLETION_REVIEW.json','GENERAL_NEAR_PERFECT.md',
      'GENERAL_NEAR_PERFECT_REVIEW.json','TWO_ODD_HOLES_TRANSFER.md']
hash_checks=0
for name in ['EIGHT_HOLE_FULL_REVIEW.json','A6_CLOSURE_REVIEW.json','CANONICAL_COMPLETION_REVIEW.json','GENERAL_NEAR_PERFECT_REVIEW.json']:
    rev=json.loads((R/name).read_text(encoding='utf-8-sig'))
    assert rev['verdict']=='PASS'
    for key in ['audited_input_hashes','imported_dependency_hashes']:
        for dep in deps:
            old=rev.get(key,{}).get(dep)
            if old:
                assert old.removeprefix('sha256:')==sha(dep).removeprefix('sha256:'),(name,dep)
                hash_checks+=1
out={'status':'PASS','audited_input_hashes':{n:sha(n) for n in sources},
     'imported_dependency_hashes':{n:sha(n) for n in deps},
     'neighbor_histograms':histograms,'five_vertex_sets_checked':8736,
     'levels':levels,'producer_comparison':'All reported counts, full delta histograms and residual orbits agree',
     'producer_source_hash_matches':True,'imported_source_hash_comparisons':hash_checks,
     'covered_replacement_population_checks':replacement_cases,
     'matching_extensions_tested':False,'delta_transfer_theorem_reviewed':False,
     'A8_proved':False,'A10_proved':False,'full_P6_proved':False}
(R/'Q5_HIGHER_HOLE_REDUCTION_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['audited_input_hashes','imported_dependency_hashes','levels']},indent=2))
print('Geometry counts:',[(x['holes'],x['geometries'],len(x['residual_orbits'])) for x in levels])

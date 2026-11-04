"""Independent exact marked geometry assembly and final-import hash binding."""
from pathlib import Path
import json,hashlib,itertools,collections,time
R=Path(__file__).resolve().parent
def load(p): return json.loads((R/p).read_text(encoding='utf-8-sig'))
def digest(p):
    h=hashlib.sha256()
    with (R/p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
imports=['Q5_A8_FULL_REVIEW.json','A10_FIRST_ORBIT_REVIEW.json','A10_ORBIT2_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json','A10_ORBIT3_UNIVERSAL_REVIEW.json']
hashes={}; checked=0
for name in imports:
    d=load(name); assert d['verdict']=='PASS',name
    hashes[name]=digest(name)
    # Final reports are imported; rehash their audited artifacts/evidence,
    # never rerun their large matching-domain/positive-cycle verification.
    for key in ['audited_input_hashes','imported_dependency_hashes','accepted_orbit_evidence_hashes','checker_artifact_hashes']:
        for p,h in d.get(key,{}).items():
            assert digest(p)==h.removeprefix('sha256:'),(name,p)
            hashes[p]=digest(p); checked+=1
    for key in ['report_hash']:
        if key in d:
            p=d['trace_path']; assert digest(p)==d[key].removeprefix('sha256:'); hashes[p]=digest(p)
    for p,h in d.get('evidence',{}).items():
        if p.endswith(('.md','.py','.json')) and len(h.removeprefix('sha256:'))==64:
            assert digest(p)==h.removeprefix('sha256:'); hashes[p]=digest(p); checked+=1
even=[v for v in range(1,32) if v.bit_count()%2==0]
odd=[v for v in range(32) if v.bit_count()%2]
domain=set()
for W in itertools.combinations(odd,4):
    eligible=[z for z in even if all((z^w).bit_count()!=1 for w in W)]
    for Z in itertools.combinations(eligible,5): domain.add((Z,W))
def swap(v,i):
    a,b=(v>>i)&1,(v>>(i+1))&1
    return v^((1<<i)|(1<<(i+1))) if a!=b else v
def orbit(rep):
    todo=[rep]; seen={rep}
    while todo:
        Z,W=todo.pop()
        for i in range(4):
            out=(tuple(sorted(swap(v,i) for v in Z)),tuple(sorted(swap(v,i) for v in W)))
            if out not in seen: seen.add(out);todo.append(out)
    return seen
reps=[((3,5,6,15,23),(8,16,25,26)),((3,5,6,15,23),(8,25,26,28)),((15,23,27,29,30),(1,2,4,8))]
orbits=[orbit(r) for r in reps]
assert [len(o) for o in orbits]==[30,20,5]
assert all(not a&b for a,b in itertools.combinations(orbits,2))
assert set.union(*orbits)==domain and len(domain)==55
# Independently recheck the small finite neighbor import to remove any
# dependence on its histogram for the consequence step.
mins=[]
for parity in range(2):
    vertices=[v for v in range(32) if v.bit_count()%2==parity]
    hist=collections.Counter()
    for five in itertools.combinations(vertices,5):
        nbrs={v^(1<<i) for v in five for i in range(5)}
        hist[len(nbrs)]+=1
    assert min(hist)==11; mins.append(dict(sorted(hist.items())))
hashes['Q5_A10_FULL_CLOSURE.md']=digest('Q5_A10_FULL_CLOSURE.md')
out={'status':'PASS','final_imports':imports,'final_import_gates_PASS':True,
     'recorded_hash_comparisons':checked,'geometry_domain':55,'orbit_sizes':[30,20,5],
     'pairwise_disjoint':True,'exact_domain_union':True,'five_subset_neighbor_histograms':mins,
     'prior_matching_certificates_rerun':False,'audited_input_hashes':hashes}
(R/'Q5_A10_FULL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='audited_input_hashes'},indent=2))

"""Fresh geometry, parity and transfer-topology checks. No producer imports.
Run with Python; writes only A8_PARTIAL_REVIEW_check.json.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json
P=Path(__file__).resolve().parent
def sha(n):return 'sha256:'+hashlib.sha256((P/n).read_bytes()).hexdigest()
N={x:{x^(1<<i) for i in range(5)} for x in range(32)}
E=[x for x in range(1,32) if x.bit_count()%2==0]
O=[x for x in range(32) if x.bit_count()%2]
def deltas(z,w):
    return tuple(len(({0}|set(z))&{x for x in range(32) if x&(1<<i)==0})
                 -len(set(w)&{x for x in range(32) if x&(1<<i)==0}) for i in range(5))
def swap(x,i):
    return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
def orbit(seed):
    found={seed};todo=[seed]
    while todo:
        z,w=todo.pop()
        for i in range(4):
            g=(tuple(sorted(swap(x,i) for x in z)),tuple(sorted(swap(x,i) for x in w)))
            if g not in found:found.add(g);todo.append(g)
    return found
# Reverse this writer's loop order: select the three minority holes first.
domain={};hist=Counter();residual=set();populations=Counter()
for w in combinations(O,3):
    allowed=[x for x in E if all(x not in N[y] for y in w)]
    for z in combinations(allowed,4):
        ds=deltas(z,w);good=tuple(i for i,d in enumerate(ds) if d in (1,2,3))
        domain[z,w]=(ds,good);hist[tuple(sorted(ds))]+=1
        if not good:residual.add((z,w))
        for i,d in enumerate(ds):
            if d in (1,2,3):
                k=sum(x&(1<<i)==0 for x in w) # minority in A
                if d==1:assert k>=2
                if d==2:assert k==1
                if d==3:assert k+3-1>=2
                hA=2*k+d;hB=8-hA
                feasible=tuple(c for c in range(min(16-hA,16-hB)+1) if (16-hA-c)%2==0)
                assert feasible
                if d in (1,3):assert 0 not in feasible and all(c%2==1 for c in feasible)
                if d==2:assert all(c%2==0 for c in feasible)
                populations[d,k,feasible]+=1
assert len(domain)==2700 and len(residual)==160
given=json.loads((P/'A8_geometry_census.json').read_text())
assert given['normalized_forbidden']==0
assert (given['total'],given['good'],given['residual'])==(2700,2540,160)
assert {tuple(k):v for k,v in given['histogram']}==dict(hist)
seen=set();orbits=[]
for g in given['residual_orbits']:
    seed=(tuple(g['Z']),tuple(g['W']));images=orbit(seed)
    assert min(images)==seed and len(images)==g['size']
    assert tuple(g['deltas'])==deltas(*seed)
    assert not seen&images and images<=residual
    members=set()
    for row in g['members']:
        k=(tuple(row['Z']),tuple(row['W']))
        assert k not in members and k in images
        assert (tuple(row['deltas']),tuple(row['good_cuts']))==domain[k]
        members.add(k)
    assert members==images
    seen|=images;orbits.append({'Z':list(seed[0]),'W':list(seed[1]),'size':len(images),'deltas':list(deltas(*seed))})
assert seen==residual and len(orbits)==5
# Compare with the earlier independently reviewed producer as a second
# external consistency check, after reconstructing all new-writer fields.
prior=json.loads((P/'q5_higher_hole_reduction_geometry.json').read_text())['levels'][0]
assert prior['holes']==8 and prior['independent_except_forbidden_geometries']==2700
assert prior['without_delta123']==160
assert {tuple(k):v for k,v in prior['delta_histogram']}==dict(hist)
assert [(tuple(g['other_majority']),tuple(g['minority']),g['size']) for g in prior['residual_orbits']]==[(tuple(g['Z']),tuple(g['W']),g['size']) for g in orbits]
priorcheck=json.loads((P/'Q5_HIGHER_HOLE_REDUCTION_REVIEW_check.json').read_text())
assert priorcheck['status']=='PASS'
assert priorcheck['levels'][0]['geometries']==2700
assert priorcheck['levels'][0]['without_delta123']==160

# Q4 two-versus-three independent-hole fact, both parity orientations.
q4_neighbor_checks=0
for parity in (0,1):
    for x,y in combinations([x for x in range(16) if x.bit_count()%2==parity],2):
        nx={x^(1<<i) for i in range(4)};ny={y^(1<<i) for i in range(4)}
        assert len(nx|ny)>=6
        assert sum(all((z^t).bit_count()!=1 for t in (x,y)) for z in range(16) if z.bit_count()%2!=parity)<=2
        q4_neighbor_checks+=1

# Test every possible matching of removed edges in a labeled15-cycle.
# Its endpoint pairings encode every cyclic order relevant to the proofs;
# labels for B ports/crossing partners are arbitrary, not mirror-assumed.
def edge(a,b):return tuple(sorted((a,b)))
cycle={edge(i,(i+1)%15) for i in range(15)}
def assert_forest(edges,expected_endpoints,interior):
    adj={}
    for a,b in edges:
        assert a!=b
        adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
    assert all(len(v)<=2 for v in adj.values())
    assert {x for x,v in adj.items() if len(v)==1}==expected_endpoints
    assert all(len(adj[x])==2 for x in interior)
    todo=set(adj);pairs=[]
    while todo:
        start=next(iter(todo));stack=[start];component=set()
        while stack:
            x=stack.pop()
            if x in component:continue
            component.add(x);stack.extend(adj[x]-component)
        todo-=component
        ends=component&expected_endpoints
        assert len(ends)==2 # rules out circles, loops, isolated interiors
        pairs.append(tuple(sorted(ends)))
    assert len(pairs)*2==len(expected_endpoints)
    return pairs

topology=Counter();matching_sizes=Counter()
for bits in range(1,1<<15):
    if bits&(bits<<1) or (bits&1 and bits&(1<<14)):continue
    D={edge(i,(i+1)%15) for i in range(15) if bits&(1<<i)}
    endpoints={x for e in D for x in e};assert len(endpoints)==2*len(D)
    matching_sizes[len(D)]+=1
    # delta2 positive crossings: all removed endpoints attach by arbitrary
    # required crossing edges to different B vertices.
    ports={100+x for x in endpoints}
    graph=(cycle-D)|{edge(x,100+x) for x in endpoints}
    assert_forest(graph,ports,set(range(15)));topology['delta2_positive']+=1
    for t in endpoints:
        partner=next(b if a==t else a for a,b in D if t in (a,b))
        # Internal mirror: its required mate k is outside all B ports.
        # Adding wk before compression verifies suppression and excludes k=q.
        w=500;k=501
        ports={100+x for x in endpoints if x!=t}
        graph=(cycle-D)|{edge(x,100+x) for x in endpoints if x!=t}|{edge(t,w),edge(w,k)}
        assert_forest(graph,ports|{k},set(range(15))|{w})
        topology['delta3_internal']+=1
        topology['delta1_internal']+=1
        # Port mirror: the A required partner is precisely the endpoint
        # paired with t in D (or d after deleting dy in delta1).
        if len(D)>=2:
            ports={100+x for x in endpoints if x not in (t,partner)}
            graph=(cycle-D)|{edge(x,100+x) for x in endpoints if x not in (t,partner)}|{edge(t,w),edge(partner,w)}
            assert_forest(graph,ports,set(range(15))|{w})
            topology['delta3_port_prescribed_gap']+=1
            topology['delta1_port_root_partner']+=1
        else:
            # This is exactly the forbidden c1 port-mirror situation.
            graph=(cycle-D)|{edge(t,w),edge(partner,w)}
            assert all(sum(x in e for e in graph)==2 for x in range(15))
            topology['c1_port_mirror_circle_excluded']+=1

# Relevant declared theorem/review hashes in accepted imports must remain fixed.
imports=['A6_CLOSURE_DRAFT.md','A6_CLOSURE_REVIEW.md','A6_CLOSURE_REVIEW.json',
 'Q4_GENERAL_AUGMENTATION.md','Q4_CORE_AND_A4_SPLIT.md','Q4_CORE_REVIEW.json',
 'A6_FINITE_INPUTS_REVIEW.md','A6_FINITE_INPUTS_REVIEW.json',
 'Q5_HIGHER_HOLE_REDUCTION_REVIEW.md','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json',
 'Q5_HIGHER_HOLE_REDUCTION_REVIEW_check.py','Q5_HIGHER_HOLE_REDUCTION_REVIEW_check.json',
 'q5_higher_hole_reduction_geometry.py','q5_higher_hole_reduction_geometry.json']
hash_comparisons=0
for name in ('A6_CLOSURE_REVIEW.json','A6_FINITE_INPUTS_REVIEW.json','Q4_CORE_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json'):
    report=json.loads((P/name).read_text(encoding='utf-8-sig'));assert report.get('verdict',report.get('status'))=='PASS'
    for field in ('audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes'):
        for n in imports:
            h=report.get(field,{}).get(n)
            if h:
                assert h.removeprefix('sha256:')==sha(n).removeprefix('sha256:'),(name,n)
                hash_comparisons+=1
sources=['A8_PARTIAL_PROOF_PACKAGE.md','A8_geometry_census.py','A8_geometry_census.json']
out={'status':'PASS','audited_input_hashes':{n:sha(n) for n in sources},
 'imported_dependency_hashes':{n:sha(n) for n in imports},
 'checker_source_hash':sha('A8_PARTIAL_REVIEW_check.py'),
 'geometry_count':len(domain),'proved_by_delta123':len(domain)-len(residual),
 'residual_count':len(residual),'residual_orbits':orbits,
 'all_writer_histogram_and_residual_member_fields_equal':True,
 'agrees_with_prior_independent_geometry_review':True,
 'q4_neighbor_pair_checks':q4_neighbor_checks,
 'feasible_delta_k_populations':[{'delta':d,'k':k,'crossing_counts':list(c),'cuts':n} for (d,k,c),n in sorted(populations.items())],
 'cycle_deleted_matching_sizes':dict(sorted(matching_sizes.items())),
 'abstract_topology_checks':dict(topology),'imported_source_hash_comparisons':hash_comparisons,
 'producer_imported_or_executed':False,'matching_extension_sampling_used':False,
 'partial_A8_branches_proved':True,'full_A8_proved':False,'full_P6_proved':False}
(P/'A8_PARTIAL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ('audited_input_hashes','imported_dependency_hashes')},indent=2))

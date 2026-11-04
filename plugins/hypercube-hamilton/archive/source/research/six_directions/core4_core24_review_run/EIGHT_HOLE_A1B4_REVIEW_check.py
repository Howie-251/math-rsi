"""Reviewer-owned audit: full residual records, dependency freshness, topology.

No producer module is imported. Geometry counts are not matching counts.
Topology tests are finite illustrations; universal surgery is reviewed in prose.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
import hashlib, json
from datetime import datetime, timezone

B = Path(__file__).resolve().parent
STEM = 'EIGHT_HOLE_A1B4_REVIEW_check'
def sha(name):
    return 'sha256:' + hashlib.sha256((B/name).read_bytes()).hexdigest()
def load(name):
    return json.loads((B/name).read_text(encoding='utf-8-sig'))

def dependencies():
    reports = ['T44_Q5_CLOSURE_REVIEW.json', 'CANONICAL_COMPLETION_REVIEW.json',
               'A4_SINGLE_GEOMETRY_REVIEW.json', 'GENERAL_NEAR_PERFECT_REVIEW.json']
    out = {}
    for name in reports:
        r = load(name)
        assert r['verdict'] == 'PASS'
        checked = {}
        for key in ('audited_input_hashes', 'imported_dependency_hashes'):
            for file, expected in r.get(key, {}).items():
                assert sha(file) == expected, (name, file, expected, sha(file))
                checked[file] = expected
        d = r.get('details', {})
        for fk, hk in [('independent_checker', 'independent_checker_sha256'),
                       ('independent_checker_result', 'independent_checker_result_sha256')]:
            if fk in d and hk in d:
                assert sha(d[fk]) == d[hk]
                checked[d[fk]] = d[hk]
        out[name] = dict(sha256=sha(name), verdict=r['verdict'], checked=checked)
    # Also verify every direct audited dependency of the imported T44 report.
    for name in ['Q4_CORE_REVIEW.json', 'Q4_TWO_AVOIDED_REVIEW.json',
                 'Q4_RICH_GLUING_REVIEW.json', 'T44_SAMEFACE_ZERO_CROSSING_REVIEW.json']:
        r = load(name)
        assert r['verdict'] == 'PASS'
        checked = r.get('audited_input_hashes', {})
        for file, expected in checked.items():
            assert sha(file) == expected, (name, file)
        out[name] = dict(sha256=sha(name), verdict='PASS', checked=checked)
    return out

def geometry():
    census = load('covered_eight_geometry_census_independent_check.json')
    rowsout = []
    good = {(0,1),(0,2),(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3)}
    for v, expected_total, expected_closed, expected_remaining in [
            (1,19530,7535,11995),(7,22472,8319,14153),(31,24125,8815,15310)]:
        name = f'covered_eight_residual_{v}.bin'
        data = (B/name).read_bytes()
        old = next(x for x in census['targets'] if x['v']==v)
        assert sha(name).split(':')[1] == old['record_sha256']
        assert len(data) == 7 * expected_total
        seen = set(); remaining = []; exceptional = []; closed = 0
        for pos in range(0,len(data),7):
            record = data[pos:pos+7]
            assert record not in seen
            seen.add(record)
            z,w = record[:3],record[3:]
            assert list(z)==sorted(set(z)) and list(w)==sorted(set(w))
            assert all(0<x<64 and x.bit_count()%2==0 for x in z)
            assert all(0<x<64 and x.bit_count()%2==1 and x!=v for x in w)
            assert all((x^y).bit_count()!=1 for x in z for y in w)
            rr = [(sum(((x^v)>>i)&1==0 for x in z),
                   sum(((x^v)>>i)&1==0 for x in w)) for i in range(6)]
            assert good.isdisjoint(rr)
            if (1,4) in rr:
                closed += 1
                # Every bridge choice avoiding root has internally covered mirrors
                # for any realizing short matching, by exact hole/port exclusions.
                for i,row in enumerate(rr):
                    if row != (1,4): continue
                    candidates = [x^(1<<i) for x in w if x^(1<<i)!=0]
                    assert len(candidates)>=3
                    assert all(y not in {0,*z,*w} for y in candidates)
            else:
                remaining.append(record)
                if (2,1) not in rr:
                    assert Counter(rr)==Counter({(2,0):3,(3,2):3})
                    exceptional.append(tuple(record))
        assert closed==expected_closed and len(remaining)==expected_remaining
        dest = f'remaining_eight_after_a1b4_{v}.bin'
        (B/dest).write_bytes(b''.join(remaining))
        # Reconstruct stabilizer orbits independently only for the 50 exceptions.
        maps=[]
        for p in permutations(range(6)):
            if sum(((v>>i)&1)<<p[i] for i in range(6)) == v:
                maps.append(tuple(sum(((x>>i)&1)<<p[i] for i in range(6)) for x in range(64)))
        pending=set(exceptional); orbits=[]
        while pending:
            g=min(pending)
            orb={tuple(sorted(t[x] for x in g[:3]))+tuple(sorted(t[x] for x in g[3:])) for t in maps}
            assert orb<=pending
            pending-=orb
            orbits.append(dict(Z=g[:3],W=g[3:],size=len(orb)))
        rowsout.append(dict(v=v,total=expected_total,closed_a1b4=closed,
                            remaining=len(remaining),remaining_a2b1=len(remaining)-len(exceptional),
                            remaining_without_a2b1=len(exceptional),exception_orbits=orbits,
                            input_sha256=sha(name),remaining_file=dest,remaining_sha256=sha(dest)))
    assert sum(x['total'] for x in rowsout)==66127
    assert sum(x['closed_a1b4'] for x in rowsout)==24669
    assert sum(x['remaining'] for x in rowsout)==41458
    assert sum(x['remaining_a2b1'] for x in rowsout)==41408
    assert sum(len(x['exception_orbits']) for x in rowsout)==7
    return rowsout

def pairings(xs):
    if not xs:
        yield []
        return
    a=xs[0]
    for i in range(1,len(xs)):
        for tail in pairings(xs[1:i]+xs[i+1:]):
            yield [(a,xs[i])]+tail

def topology():
    counts=[]
    # All abstract T pairings for small admissible c, both conflict patterns,
    # and every possible tag position (delta=0 forces tag incident to u).
    for delta,cs in [(1,[2,4,6,8]),(0,[3,5,7])]:
        for c in cs:
            endpoints=list(range(c))+['y0','y1']+(['u'] if delta==0 else [])
            checked=0; joined=0
            for pairs in pairings(endpoints):
                for tag_index,pair in enumerate(pairs):
                    if delta==0 and 'u' not in pair: continue
                    # B vertices: ports, Y, K, two surviving holes, optional root,
                    # plus filler matched internally to reach 32.
                    bv=endpoints+['k0','k1','h0','h1']
                    filler=[f'f{i}' for i in range(32-len(bv))]
                    bv+=filler
                    mb=[('y0','k0'),('y1','k1')]+list(zip(filler[::2],filler[1::2]))
                    av=['v']+(['u'] if delta else [])
                    av += [f'a{i}' for i in range(32-len(av))]
                    interiors=[[] for _ in pairs]
                    if delta:
                        interiors[tag_index]=['u','v']; av=av[2:]
                    else:
                        interiors[tag_index]=['v']; av=av[1:]
                    # Put no filler after v in the tagged path: this explicitly
                    # realizes the delicate temporarily isolated target-port
                    # boundary. Other path interiors absorb all unused A points.
                    for i in range(len(pairs)):
                        if i!=tag_index: interiors[i].append(av.pop())
                    interiors[next(i for i in range(len(pairs)) if i!=tag_index)]+=av
                    paths=[]
                    for i,(a,b) in enumerate(pairs):
                        if delta==0 and i==tag_index and b=='u': a,b=b,a
                        paths.append([a]+interiors[i]+[b])
                    adj={}
                    expansions={}
                    for path in paths+[[a,b] for a,b in mb]:
                        a,b=path[0],path[-1]
                        assert a!=b
                        adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
                        expansions[frozenset((a,b))]=path
                    assert {x for x,ns in adj.items() if len(ns)==2}=={'y0','y1'}
                    compressed=[];used=set()
                    for start in adj:
                        if len(adj[start])!=1 or start in used: continue
                        chain=[start];prev=None;cur=start
                        while True:
                            ns=[x for x in adj[cur] if x!=prev]
                            if not ns: break
                            nxt=ns[0];part=expansions[frozenset((cur,nxt))]
                            if part[0]!=cur:part=part[::-1]
                            chain+=part[1:];prev,cur=cur,nxt
                        used.update(x for x in chain if x in adj)
                        compressed.append(chain)
                    assert used==set(adj)
                    covered=[x for p in compressed for x in (p[0],p[-1])]
                    assert len(covered)==len(set(covered))
                    assert set(bv)-set(covered)=={'h0','h1','y0','y1'}
                    # Any local cycle containing compressed edges expands to a
                    # single 64-circle. Here build one abstract cycle of blocks.
                    cycle=[x for p in compressed for x in p]+['h0','h1']
                    assert len(cycle)==len(set(cycle))==64
                    edges={frozenset((cycle[i],cycle[(i+1)%64])) for i in range(64)}
                    assert frozenset(('u','v')) in edges
                    assert all(frozenset(e) in edges for e in mb)
                    for path in paths:
                        assert all(frozenset(e) in edges for e in zip(path,path[1:]))
                    checked+=1
                    joined+=any(set(p)=={'y0','y1'} for p in pairs)
            counts.append(dict(delta=delta,c=c,tagged_pairings_checked=checked,
                               same_component_conflicts=joined))
    return counts

def remaining_core_cover():
    """Filter previously audited map; independently prove minimum hitting set."""
    prior=load('EIGHT_T15_CORE_MAP_REVIEW.json')
    assert prior['verdict']=='PASS'
    assert sha('eight_t15_core_map.json')==prior['audited_input_hashes']['eight_t15_core_map.json']
    old=load('eight_t15_core_map.json')
    remaining=set()
    for v in (1,7,31):
        raw=(B/f'remaining_eight_after_a1b4_{v}.bin').read_bytes()
        remaining.update((v,tuple(raw[i:i+7])) for i in range(0,len(raw),7))
    signatures=Counter(); used=set(); mapped=set()
    for item in old['targets']:
        key=(item['target'],tuple(item['Z']+item['W']))
        if key not in remaining: continue
        assert key not in mapped
        mapped.add(key)
        s=tuple(sorted(item['core_choices']))
        assert s
        signatures[s]+=1; used.update(s)
    assert len(mapped)==41408 and len(remaining-mapped)==50
    assert len(used)==37 and len(signatures)==31
    forced={s[0] for s in signatures if len(s)==1}
    assert forced=={0,1,2,4,5,8,10,13,14,15,19,23,24,27}
    constraints={frozenset(s) for s in signatures if forced.isdisjoint(s)}
    # Drop supersets for the exact lower-bound certificate.
    constraints={s for s in constraints if not any(t<s for t in constraints)}
    groups=[]
    while constraints:
        component={constraints.pop()}
        while True:
            vertices=set().union(*component)
            touch={s for s in constraints if not s.isdisjoint(vertices)}
            if not touch:break
            component|=touch;constraints-=touch
        groups.append(component)
    assert len(groups)==6
    # Each component requires at least one core; their vertex sets are disjoint.
    # Every component has a common core, so one core is also sufficient.
    chosen=set(forced)
    for group in groups:
        common=set.intersection(*(set(s) for s in group))
        assert common
        chosen.add(min(common))
    assert len(chosen)==20 and all(chosen.intersection(s) for s in signatures)
    return dict(status='PASS',scope='Filtered already-audited orbit map; no T15 theorem proved.',
                source_sha256=sha('eight_t15_core_map.json'),source_review_sha256=sha('EIGHT_T15_CORE_MAP_REVIEW.json'),
                remaining_with_a2b1=41408,remaining_without_a2b1=50,used_core_count=37,
                distinct_choice_sets=31,forced_cores=sorted(forced),
                independent_constraint_groups=[[sorted(s) for s in sorted(g,key=lambda t:sorted(t))] for g in groups],
                minimum_cover_size=20,sufficient_cover=sorted(chosen),
                lower_bound='14 singleton-forced cores plus 6 disjoint nonempty constraint components; each component has a common core.')

if __name__=='__main__':
    result=dict(status='PASS',dependency_freshness=dependencies(),geometry=geometry(),
                abstract_topology=topology(),
                remaining_core_cover=remaining_core_cover(),
                checker_sha256=sha(STEM+'.py'),
                draft_sha256=sha('EIGHT_HOLE_A1B4_DRAFT.md'),
                limitation='Not a matching census; topology finite tests supplement universal prose review; imported theorem certificates not rerun.')
    (B/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    review=dict(
        audit_skill='proof-checker',verdict='PASS',
        reason_code='all_row_a1b4_obligations_complete_relative_to_explicit_imports',
        summary='The covered-target eight-hole (1,4) row closes for every realizing short matching; 24669 residual geometries close and 41458 remain. Full eight-hole and P6 remain open.',
        reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',
        model_selection_source='User-authorized route relayed by parent',
        reviewer_family='openai',executor_family='openai',
        review_independence='same-family',acceptance_status='provisional',
        thread_id='/root/eight_a1b4_audit',generated_at=datetime.now(timezone.utc).isoformat(),
        trace_path='EIGHT_HOLE_A1B4_REVIEW.md',
        audited_input_hashes={'EIGHT_HOLE_A1B4_DRAFT.md':result['draft_sha256'],
                             'SIX_HOLE_MIXED_AND_GEOMETRY.md':sha('SIX_HOLE_MIXED_AND_GEOMETRY.md'),
                             'covered_eight_geometry_census_independent_check.json':sha('covered_eight_geometry_census_independent_check.json'),
                             **{f'covered_eight_residual_{v}.bin':sha(f'covered_eight_residual_{v}.bin') for v in (1,7,31)}},
        details=dict(proof_obligations=[dict(id=f'AB{i:02}',status='PASS') for i in range(1,21)],
                     issues=[],open_counts=dict(FATAL=0,CRITICAL=0,MAJOR=0,MINOR=0),
                     independent_checker=STEM+'.py',independent_checker_sha256=sha(STEM+'.py'),
                     independent_checker_result=STEM+'.json',independent_checker_result_sha256=sha(STEM+'.json'),
                     dependency_freshness=result['dependency_freshness'],geometry=result['geometry'],
                     abstract_topology=result['abstract_topology'],
                     remaining_core_cover=result['remaining_core_cover'],
                     scope='Full 66127 previously audited residual hole geometries, universal prose proof for row (1,4); not a census of matchings or realizability.',
                     imported_certificates_rerun=False,original_inputs_or_main_state_modified=False,
                     closure_claims=dict(row_a1b4_proved_relative_to_explicit_imports=True,
                                         newly_closed_geometries=24669,remaining_geometries=41458,
                                         remaining_with_a2b1=41408,remaining_without_a2b1=50,
                                         full_T15_proved=False,EP0_proved=False,R8_covered_proved=False,
                                         full_eight_hole_proved=False,full_P6_proved=False)))
    (B/'EIGHT_HOLE_A1B4_REVIEW.json').write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['dependency_freshness']}))

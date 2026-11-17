"""Independent scoped checks; writes reviewer outputs only, never producers."""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter
from datetime import datetime, timezone
import hashlib, json

R = Path(__file__).resolve().parent
def read(name): return json.loads((R/name).read_text(encoding='utf-8-sig'))
def sha(name): return 'sha256:' + hashlib.sha256((R/name).read_bytes()).hexdigest()
def base(inputs):
    return dict(audit_skill='proof-checker', verdict='PASS',
                review_independence='same-family', acceptance_status='provisional',
                reviewer_model='gpt-6.1-sol', reviewer_reasoning='high',
                model_selection_source='explicit user override relayed by parent',
                backend_identity_independently_certified=False,
                reviewer_family='openai', executor_family='openai',
                thread_id='/root/q5_three_target_counter_audit',
                generated_at=datetime.now(timezone.utc).isoformat(),
                protected_files_modified=False, open_fatal=0, open_critical=0, issues=[],
                full_Q6_T15_proved=False, full_P7_proved=False,
                audited_input_hashes={n:sha(n) for n in inputs})
def write(name, obj):
    (R/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def connected(adj, start):
    seen={start}; todo=[start]
    for u in todo:
        for v in adj[u]:
            if v not in seen: seen.add(v); todo.append(v)
    return seen

# Counterexample: reconstruct the cube cut directly, independently of rank data.
ce=read('Q5_THREE_TARGET_LAYER_COUNTEREXAMPLE.json')
V=set(range(32)); H={0,1}; K=V-H; targets={14,22,26}
F={tuple(e) for e in ce['matching']}
cube={e for e in combinations(sorted(V-{0}),2) if (e[0]^e[1]).bit_count()==1}
cut={e for e in cube if (e[0]^e[1])==1}
assert F==cut=={(2*k,2*k+1) for k in range(1,16)}
assert len(F)==15 and {v for e in F for v in e}==K
assert all(not(t&1) for t in targets)
assert (ce['holes'],ce['omitted'],ce['allowed_endpoints'])==([0,1],0,sorted(targets))
assert ce['dimension']==5 and ce['cross_direction']==0
assert ce['prescribed_cross_edges']==ce['available_cross_edges']==15
assert ce['all_allowed_endpoints_on_side']==0 and not ce['affects_full_Q6_T15_or_P7']
profile=read('Q6_T15_ACTUAL_PROFILE.json'); c85=profile['orbits'][85]
assert c85['index']==85 and c85['included']==[31,47,55] and c85['omitted']==[1,2]
original_H={0,*c85['included'],*c85['omitted']}
assert {v for v in original_H if not(v&1)}=={0,2}
mirrors={v^1 for v in c85['included']}
assert mirrors=={30,46,54}
project=lambda x:(x^2)>>1
assert {project(v) for v in (0,2)}==H
assert project(2)==0 and project(0)==1
assert {project(v) for v in mirrors}==targets
assert (R/'Q5_THREE_TARGET_CORE85_config.txt').read_text().split()==['0','1','14','22','26']

# Validate every stored selected forest and its contraction, then test full
# connectivity against F via ordinary undirected BFS, not alternating orbits.
fb=(R/'Q5_THREE_TARGET_CORE85_forests.bin').read_bytes()
pb=(R/'Q5_THREE_TARGET_CORE85_pairs.bin').read_bytes()
assert len(fb)%34==len(pb)%30==0 and len(fb)//34==len(pb)//30==16127
compatible=0
for i in range(16127):
    row=fb[34*i:34*i+34]; edges=[tuple(row[j:j+2]) for j in range(0,34,2)]
    assert len(set(edges))==17 and all(0<=a<b<32 for a,b in edges)
    adj={v:[] for v in V}
    for a,b in edges:
        assert (a==0 and b in targets) or (a!=0 and (a^b).bit_count()==1)
        adj[a].append(b); adj[b].append(a)
    assert all(len(adj[v])==(2 if v in H else 1) for v in V)
    assert set(adj[0])<=targets and len(set(adj[0]))==2
    seen=set(); endpoint_pairs=set()
    for v in sorted(V):
        if v in seen: continue
        comp=connected(adj,v); seen|=comp
        assert sum(len(adj[u]) for u in comp)//2==len(comp)-1
        ends=sorted(u for u in comp if u in K)
        assert len(ends)==2; endpoint_pairs.add(tuple(ends))
    assert len(endpoint_pairs)==15
    pairs=pb[30*i:30*i+30]
    assert {tuple(pairs[j:j+2]) for j in range(0,30,2)}==endpoint_pairs
    for a,b in F: adj[a].append(b); adj[b].append(a)
    compatible+=len(connected(adj,0))==32
assert compatible==ce['compatible_selected_forests']==0
assert ce['selected_forest_rows_checked']==16127
assert ce['sha256']['Q5_THREE_TARGET_CORE85_pairs.bin']==sha('Q5_THREE_TARGET_CORE85_pairs.bin')[7:]
q5=base(['Q5_THREE_TARGET_LAYER_COUNTEREXAMPLE.md','Q5_THREE_TARGET_LAYER_COUNTEREXAMPLE.json',
         'check_q5_three_target_layer_counterexample.py','Q6_T15_THREE_TARGET_TRANSFER.md',
         'Q5_THREE_TARGET_CORE85_config.txt','Q5_THREE_TARGET_CORE85_forests.bin',
         'Q5_THREE_TARGET_CORE85_pairs.bin','Q6_T15_ACTUAL_PROFILE.json',
         'Q5_Q6_FRONTIER_REVIEW_check.py'])
q5.update(reason_code='explicit_counterexample_verified',
          summary='The candidate universal Q5 three-target local claim is false; its explicit layer matching and core85 projection check exactly.',
          local_claim_status='REFUTED', candidate_not_used_by_existing_proofs=True,
          allowed_endpoints=sorted(targets), omitted=0, holes=[0,1],
          prescribed_and_available_coordinate0_edges=15,
          selected_forests_independently_validated=16127,compatible_selected_forests=0,
          producer_rank_certified=False, exhaustive_forest_count_certified=False,
          rank_matrix_audited=False,
          scope='Only the unused universal local sufficient claim is refuted; no conclusion of failure of T15, P7, or accepted S2/two-target transfers follows.',
          trace_path='Q5_Q6_FRONTIER_REVIEW_check.py')
write('Q5_THREE_TARGET_LAYER_COUNTEREXAMPLE_REVIEW.json',q5)

# Frontier: accepted sets are imports, not new semantic proof judgments here.
oldreview=read('Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json')
newreview=read('Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
assert oldreview['verdict']==newreview['verdict']=='PASS'
old=set(oldreview['union_closed_core_indices']); extra=set(newreview['closed_core_indices'])
assert len(old)==1009 and len(extra)==24 and len(extra-old)==8
assert extra-old==set(newreview['new_core_indices'])
assert old=={v['core_index'] for v in read('Q6_T15_S2_COMBINED_ALL_CLOSED.json')['cores']}
assert extra=={v['core_index'] for v in read('Q6_T15_GOOD_ROOT_COMPONENTS.json')['closed_cores']}
closed=old|extra
recorded=[v['core_index'] for v in read('Q6_T15_GOOD_ROOT_ALL_CLOSED.json')['cores']]
assert len(closed)==len(recorded)==1017 and sorted(closed)==recorded
remaining=Counter()
for row in profile['choice_sets']:
    assert row['choices']==sorted(set(row['choices'])) and row['count']>0
    if not closed.intersection(row['choices']): remaining[tuple(row['choices'])]+=row['count']
expected={(85,):84068,(386,):4788,(1007,):4776,(1054,):4064,(2189,):670}
assert remaining==expected and sum(remaining.values())==98366
out=read('Q6_T15_AFTER_GOOD_ROOT_FRONTIER.json')
assert out['forced_orbits']==out['one_minimum_cover']==[85,386,1007,1054,2189]
assert out['minimum_count']==out['remaining_actual_cores']==out['remaining_choice_sets']==5
assert out['closed_core_count']==1017 and out['remaining_with21']==98366
assert not out['selected_cores_proved'] and not out['full_P7_proved'] and out['components']==[]
hist=Counter(); lookup={}
for detail in out['selected_details']:
    cid=detail['core_index']; core=profile['orbits'][cid]
    assert detail['included']==core['included'] and detail['omitted']==core['omitted']
    assert detail['remaining_parent_count']==remaining[(cid,)]
    cuts=[]
    for j in range(6):
        face={v for v in {0,*core['included'],*core['omitted']} if not(v>>j&1)}
        n=len(face)-1; om=len(face.intersection(core['omitted'])); hist[n,om]+=1
        cuts.append(dict(coordinate=j,majority_in_minority_face=n,omissions_in_minority_face=om))
    assert cuts==detail['cuts']
    # Build coordinate-orbit keys for these five cores independently, rather
    # than import the previous 1,055,600-key lookup or producer classifier.
    for perm in permutations(range(6)):
        def pm(v):return sum(((v>>j)&1)<<perm[j] for j in range(6))
        key=tuple(sorted(pm(v) for v in core['included']))+tuple(sorted(pm(v) for v in core['omitted']))
        assert key not in lookup or lookup[key]==cid
        lookup[key]=cid
assert sorted(d['core_index'] for d in out['selected_details'])==[85,386,1007,1054,2189]
assert out['cut_histogram']==[dict(majority_in_minority_face=n,omissions_in_minority_face=o,count=k) for (n,o),k in sorted(hist.items())]

authority='Q7_EIGHT_COVERED_AFTER_GOOD_ROOTS.bin'; data=(R/authority).read_bytes()
assert sha(authority)==newreview['residual_sha256']
assert len(data)==8*117602
choices=Counter(); no21=0; previous=None
for pos in range(0,len(data),8):
    row=tuple(data[pos:pos+8]); target=row[0]; even=row[1:4]; odd=row[4:]
    assert previous is None or previous<row
    previous=row
    assert target in {1,7,31,127} and len({0,*row})==9 and max(row)<128
    assert tuple(sorted(even))==even and tuple(sorted(odd))==odd
    assert all(v.bit_count()%2==0 for v in even) and all(v.bit_count()%2 for v in odd)
    assert all((a^b).bit_count()!=1 for a in even for b in odd)
    rowcores=set()
    for j in range(7):
        same=lambda x:((x^target)>>j&1)==0
        ea=[v for v in even if same(v)]; ob=[v for v in odd if not same(v)]
        if len(ea)!=2 or len(ob)!=3: continue
        anchor=next(v for v in even if not same(v))
        def proj(v):
            z=v^anchor
            return (z&((1<<j)-1))|((z>>(j+1))<<j)
        key=tuple(sorted(proj(v) for v in ob))+tuple(sorted(proj(v) for v in ea))
        assert key in lookup
        rowcores.add(lookup[key])
    if rowcores: choices[tuple(sorted(rowcores))]+=1
    else: no21+=1
assert choices==expected and no21==19236
assert out['remaining_no21_after_EP0']==no21 and out['original_no21_before_EP0']==profile['parent_no_a2b1']==24130
q6=base(['Q6_T15_ACTUAL_PROFILE.json','Q6_T15_AFTER_GOOD_ROOT_FRONTIER.json',
         'Q6_T15_GOOD_ROOT_ALL_CLOSED.json','Q6_T15_S2_COMBINED_ALL_CLOSED.json',
         'Q6_T15_GOOD_ROOT_COMPONENTS.json','Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json',
         'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json',authority,'Q5_Q6_FRONTIER_REVIEW_check.py'])
q6.update(reason_code='exact_frontier_accounting_verified_modulo_accepted_imports',
          summary='Accepted union has1017 cores; exactly five singleton obligations remain, accounting for98366 with21 parents plus19236 no21 parents.',
          imports=['Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json: accepted1009-core union',
                   'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json: accepted24 good-root cores,8 new; authoritative residual provenance'],
          closed_core_count=1017,new_core_indices=sorted(extra-old),
          remaining_choices=[dict(choices=list(k),count=v) for k,v in sorted(choices.items())],
          selected_cores_proved=False, remaining_actual_cores=5,minimum_count=5,
          minimum_proof='Each of five distinct singleton constraints forces its unique core; their union meets all constraints.',
          remaining_with21=98366,remaining_no21=19236,residual_rows=117602,
          authority_directly_reclassified=True, authority_sha256=sha(authority),
          cut_histogram=out['cut_histogram'],selected_details=out['selected_details'],
          trace_path='Q5_Q6_FRONTIER_REVIEW_check.py')
write('Q6_T15_AFTER_GOOD_ROOT_FRONTIER_REVIEW.json',q6)
print('PASS: Q5 explicit counterexample and16127 forests; Q6 union1017, five singleton cores,117602 authority rows independently reclassified.')

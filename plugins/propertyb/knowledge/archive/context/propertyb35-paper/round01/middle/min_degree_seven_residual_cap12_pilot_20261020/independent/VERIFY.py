"""Independent exact-high-trace domain, D8 transport, tau caller,35-index replay.
Read-only for the pilot; old10^4 certificates are imported without rerunning.
"""
from pathlib import Path
from itertools import product,permutations,combinations
from collections import Counter,defaultdict
from fractions import Fraction
from math import comb
import json,sys,time

P=Path(__file__).resolve().parent;BASE=P.parent;B=BASE.parent;ROOT=P.parents[5]
START=time.process_time();LIMIT=58
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
primary=json.loads((BASE/'RESULT.json').read_text())
root=json.loads((ROOT/'context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/FINAL_LAMBDA4_VERIFY.json').read_text())
jobs=[j for j in root['jobs'] if not j['strict'] and not j['lambda4_subcase_only']]
assert len(jobs)==13 and sum(j['survivor_count'] for j in jobs)==63
proj={j['spectrum_id']:j for j in json.loads((B/'min_degree_seven_cap12_transfer_20261020/PROJECTION.json').read_text())}
known={tuple(j['quad']) for j in json.loads((B/'c13_remaining_actual_quads_20261020/ALL_RESULT.json').read_text())['quad_support']}
high=json.loads((ROOT/'context/propertyb35-paper/round01/root/tau_shared_capacities_20261020/HIGH_ROW_CHECK.json').read_text())
G={j['D']:j['G_D_tau0_through140'] for j in high['tables']}
support=defaultdict(list)
for j in jobs:
    qs=set(combinations(j['degrees'],4))
    assert qs=={tuple(q) for q in proj[j['spectrum_id']]['all_actual_selected_quads']}
    missing=[]
    for q in sorted(qs):
        covered=q in known or q.count(7)>=3 or q==(8,8,8,8)
        covered |= q==(9,10,10,10) and j['degrees'].count(7)>=5
        covered |= q==(10,10,10,10) and j['degrees'].count(7)==9 and j['degrees'].count(8)==0
        if not covered:missing.append(q);support[q].append(j)
    assert missing==[tuple(q) for q in proj[j['spectrum_id']]['missing']]
assert len(support)==37

PP=(3,5,6,9,10,12);CROSS=(5,6,9,10);TM=(7,11,13,14)
# Different from primary inclusive enumeration: enumerate exact cross/triple
# quantities and side exactpair quantities, then degree singletons and empty.
highshapes=[]
for tri in (0,*TM):
    caps={p:4-int(bool(tri) and p&tri==p) for p in PP}
    for cv in product(*(range(caps[p]+1) for p in CROSS)):
        if sum(cv)<13:continue
        for sides in product(range(1,caps[3]+1),range(1,caps[12]+1)):
            mu=[0]*16
            if tri:mu[tri]=1
            for m,n in zip(CROSS,cv):mu[m]=n
            mu[3],mu[12]=sides
            highshapes.append(tuple(mu))
assert len(highshapes)==800

def transport(mu,perm):
    out=[0]*16
    for mask,n in enumerate(mu):
        target=sum(1<<perm[i] for i in range(4) if mask>>i&1)
        out[target]=n
    return tuple(out)

# Orbit closure by three actual generators, not primary's permutations list.
generators=((1,0,2,3),(0,1,3,2),(2,3,0,1))
perms={(0,1,2,3)};front=list(perms)
while front:
    p=front.pop()
    for g in generators:
        q=tuple(g[p[i]] for i in range(4))
        if q not in perms:perms.add(q);front.append(q)
assert len(perms)==8
assert all({frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))} for p in perms)

def degree(mu):
    return tuple(sum(n for m,n in enumerate(mu) if m>>v&1) for v in range(4))

def row17_min(total):
    if not 17<=total<=68:return None
    q,r=divmod(total,17)
    return (17-r)*comb(q-1,2)+r*comb(q,2)

quadresults=[];activeall={};legacyall={};labels_total=reps_total=0
primary_quads={tuple(q['quad']):q for q in primary['full_missing_quad_projection']}
for q,src in sorted(support.items()):
    old=primary_quads[q]
    if q==(10,10,10,10):
        reps={tuple(x['counts']) for x in old['all_cases']}
        assert len(reps)==310
        labeled=None
    else:
        labeled=set()
        for ds in set(permutations(q)):
            for highmu in highshapes:
                mu=list(highmu)
                for v,d in enumerate(ds):mu[1<<v]=d-sum(n for m,n in enumerate(highmu) if m>>v&1)
                mu[0]=35-sum(mu)
                if min(mu)<0:continue
                assert degree(mu)==ds
                labeled.add(tuple(mu))
        assert labeled=={tuple(k) for k in old['labeled_keys']}
        unseen=set(labeled);reps=set();orbit_sizes=[]
        while unseen:
            seed=min(unseen);orbit={seed};front=[seed]
            while front:
                x=front.pop()
                for g in generators:
                    y=transport(x,g)
                    if y not in orbit:orbit.add(y);front.append(y)
            assert orbit<=unseen
            unseen-=orbit;reps.add(min(orbit));orbit_sizes.append(len(orbit))
        assert reps=={tuple(x['counts']) for x in old['all_cases']}
        assert sum(orbit_sizes)==len(labeled)
        labels_total+=len(labeled);reps_total+=len(reps)
    cases=[];oldcases={tuple(x['counts']):x for x in old['all_cases']}
    for mu in sorted(reps):
        ds=degree(mu);inc={p:sum(n for m,n in enumerate(mu) if m&p==p) for p in PP}
        assert min(inc.values())>=1 and max(inc.values())<=4
        Kcost=sum(comb(lam-1,2) for lam in inc.values())
        rowcosts=[]
        for v,d in enumerate(ds):
            internal=sum(lam for pair,lam in inc.items() if pair>>v&1)
            cost=row17_min(4*d-internal)
            assert cost is not None
            rowcosts.append(cost)
        outside=sum(rowcosts);contexts=[]
        for j in src:
            guaranteed_outside=j['degrees'].count(j['D'])>q.count(j['D'])
            required=Kcost+max(outside,max(0,4*j['D']-40) if guaranteed_outside else 0)
            for ki,key in enumerate(j['survivors']):
                if key['tau']>=required and G[j['D']][key['tau']]>=13:
                    contexts.append({'spectrum_id':j['spectrum_id'],'survivor_index':ki,
                                     'tau':key['tau'],'required_tau':required,
                                     'outside_seven_pool':j['degrees'].count(7)-q.count(7)})
        saved=oldcases[mu]
        assert ds==tuple(saved['degrees']) and Kcost==saved['K6_tau_cost']
        assert outside==saved['K_to_exterior_tau_lower']
        assert contexts==saved['active_contexts'] and bool(contexts)==saved['active']
        entry={'counts':list(mu),'degrees':ds,'K6_cost':Kcost,'four_outside_row_costs':rowcosts,
               'active_contexts':contexts,'active':bool(contexts)}
        cases.append(entry)
        if contexts:
            if q==(10,10,10,10):legacyall[mu]=saved
            else:activeall[mu]={'quad':q,**entry}
    quadresults.append({'quad':q,'new_domain':q!=(10,10,10,10),
                        'labeled_count':len(labeled) if labeled is not None else None,
                        'representative_count':len(reps),'active_representatives':sum(x['active'] for x in cases),
                        'labeled_keys':[list(k) for k in sorted(labeled)] if labeled is not None else None,
                        'cases':cases})
    assert time.process_time()-START<LIMIT
assert labels_total==22684 and reps_total==2901 and len(activeall)==2633 and len(legacyall)==140
newprimary={tuple(z['counts']):z for z in primary['checked_cases'] if not z['legacy']}
assert set(activeall)==set(newprimary)
domainout={'status':'PASS_COMPLETE_INDEPENDENT_DOMAIN_TAU_CONTEXT','new_quads':36,
           'exact_high_shapes':800,'D8_order':8,'new_labels':labels_total,'new_D8_representatives':reps_total,
           'new_active_representatives':len(activeall),'legacy_active_imported_without_replay':len(legacyall),
           'full63_actual_contexts_equal':True,'quad_results':quadresults,'cpu_seconds':time.process_time()-START}
(P/'DOMAIN_CHECK.json').write_text(json.dumps(domainout,separators=(',',':'))+'\n')
print('DOMAIN_PASS',labels_total,reps_total,len(activeall),'CPU',time.process_time()-START,flush=True)

# First profile the entire smallest active actual quad; proceed only if feasible.
qcounts=Counter(tuple(z['quad']) for z in activeall.values())
profilequad=min(qcounts,key=lambda q:(qcounts[q],q))
order=sorted(activeall,key=lambda mu:(tuple(activeall[mu]['quad'])!=profilequad,
                                    tuple(activeall[mu]['quad']),mu))
replay_start=time.process_time();profile=None;strict=failed=rows_total=0;maximum=Fraction();failures=[]
receipt=[]
with (P/'REPLAY.jsonl').open('w') as out:
    for idx,mu in enumerate(order,1):
        own=activeall[mu];saved=newprimary[mu]
        masks=[m for m,n in enumerate(mu) for _ in range(n)]
        assert len(masks)==35
        stubs=[frozenset(v+1 for v in range(4) if m>>v&1) for m in masks]
        pos=tuple(saved['best']['positions'])
        assert pos in ((8,9,20,21),(9,10,20,21),(9,20,10,21))
        rr=independent_rows(21,pos,stubs)
        value=sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction())
        assert value==Fraction(saved['best']['bound'])
        assert (value<1)==saved['best']['strict']
        strict+=int(value<1);failed+=int(value>=1);rows_total+=21
        if value<1:maximum=max(maximum,value)
        item={'quad':own['quad'],'counts':list(mu),'degrees':own['degrees'],
              'expanded35_masks':masks,'positions':pos,'bound':str(value),'strict':value<1,
              'active_contexts':own['active_contexts'],'quota':0,
              'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rr]}
        out.write(json.dumps(item,separators=(',',':'))+'\n')
        receipt.append({'counts':list(mu),'quad':own['quad'],'bound':str(value),'strict':value<1})
        if value>=1:failures.append({k:v for k,v in item.items() if k!='rows'})
        if idx==qcounts[profilequad]:
            cpu=time.process_time()-replay_start
            estimate=cpu*len(order)/idx
            profile={'quad':profilequad,'inventories':idx,'replay_cpu':cpu,
                     'estimated_full_replay_cpu':estimate,'domain_cpu':domainout['cpu_seconds']}
            (P/'PROFILE.json').write_text(json.dumps(profile,indent=2)+'\n')
            print('PROFILE',profile,flush=True)
            assert estimate<52,'profile exceeds authorized complete budget'
        if idx%500==0:print('REPLAY',idx,'STRICT',strict,'FAIL',failed,'CPU',time.process_time()-START,flush=True)
        assert time.process_time()-START<LIMIT,'58 CPU cutoff'
assert strict==2620 and failed==13 and rows_total==55293
legacy_fail=[{'quad':z['quad'],'counts':z['counts'],'bound':z['best']['bound'],
              'active_contexts':z['active_contexts'],'legacy':True,'replayed_in_this_run':False}
             for z in legacyall.values() if not z['best']['strict']]
assert len(legacy_fail)==4
assert {(tuple(z['counts']),z['bound']) for z in failures}=={
    (tuple(z['counts']),z['best']['bound']) for z in primary['all_nonstrict'] if not z['legacy']}

bycase={tuple(z['counts']):z['best']['strict'] for z in primary['checked_cases']}
context_results=[]
for oldctx in primary['context_scope']:
    sid=oldctx['spectrum_id'];ki=oldctx['survivor_index'];states=[]
    for qr in quadresults:
        if sid not in primary_quads[tuple(qr['quad'])]['source_spectrum_ids']:continue
        active=[z for z in qr['cases'] if any(c['spectrum_id']==sid and c['survivor_index']==ki for c in z['active_contexts'])]
        fail=sum(not bycase[tuple(z['counts'])] for z in active)
        states.append({'quad':list(qr['quad']),'tau_eligible_representatives':len(active),
                       'unprocessed':0,'nonstrict':fail,'cap12_gate_discovered':fail==0})
    assert states==oldctx['missing_quad_states']
    ready=all(z['cap12_gate_discovered'] for z in states)
    assert ready==oldctx['all_missing_quad_gates_discovered']
    context_results.append({'spectrum_id':sid,'survivor_index':ki,'all_missing_gates_strict':ready})
assert sum(c['all_missing_gates_strict'] for c in context_results)==49
out={'status':'PASS_COMPLETE_SCOPED_INDEPENDENT_VERIFICATION','review_independence':'same-family',
     'acceptance_status':'provisional','scope':__doc__,'domain_source':'DOMAIN_CHECK.json',
     'profile':profile,'new_labels':22684,'new_D8_representatives':2901,
     'new_relevant_representatives_replayed':2633,'strict_new_certificates':strict,
     'nonstrict_new_certificates_retained':failed,'maximum_strict_bound':str(maximum),
     'original_indices_per_case':35,'ordered_distinct_pairs_per_case':1190,
     'replayed_position_rows':rows_total,'replay_source':'REPLAY.jsonl','receipt':receipt,
     'new_nonstrict_cases':failures,'legacy_nonstrict_imports':legacy_fail,
     'old10power4_certificates_rerun':False,'full63_contexts_equal':True,
     'contexts_with_all_missing_gates_strict':49,'contexts':context_results,
     'new_layout_search':False,'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS','STRICT',strict,'NEWFAIL',failed,'LEGACYFAIL',len(legacy_fail),
      'ROWS',rows_total,'MAXSTRICT',maximum,'CPU',out['cpu_seconds'],flush=True)

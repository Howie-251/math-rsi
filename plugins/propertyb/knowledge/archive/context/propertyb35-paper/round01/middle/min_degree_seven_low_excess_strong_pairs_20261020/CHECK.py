"""Actual degree-pair projection of99 fixed min7/e<=4 spectra.
Reuse existing local certificates; only absent keys receive the old fixed2 menu.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import Counter,defaultdict
from fractions import Fraction
import json,time,sys

P=Path(__file__).resolve().parent
ROOT=P.parents[4]
BASE=P.parent
START=time.process_time()
source=json.loads((BASE/'min_degree_seven_gamma_four_low_excess_diagnostic_20261020/RESULT.json').read_text())
spectra=source['jobs'];assert len(spectra)==99
sharp=[([7]*8+[8]+[9]*9+[10]*3),([7]*9+[9]*8+[10]*4),
       ([7]*7+[8]*3+[9]*8+[10]*3),([7]*9+[8]+[9]*7+[10]*3+[11]),
       ([7]*10+[9]*7+[10]*3+[12])]
sharp={tuple(sorted(ds)) for ds in sharp}
assert len(sharp)==5 and all(len(ds)==21 and sum(ds)==175 for ds in sharp)

# Every entry is a generic selected-pair certificate. DOUBLES additionally uses
# actual point-pair coverage for its saved quotas; all99 callers have paircover.
files=[ROOT/'context/propertyb35-paper/round01/twentyone-high/DOUBLES.json',
       BASE/'generic_high_degree_pair_gates_20261020/FULL.json',
       BASE/'generic_high_degree_pair_gates_20261020/REFINE.json',
       BASE/'two_six_transfer_20261020/PAIR_RESULT.json',
       BASE/'delta8_strong_pair_transfer_20261020/PAIR_RESULT.json']
lookup=defaultdict(list)
for fp in files:
    data=json.loads(fp.read_text())
    for z in data['cases']:
        if 'degrees' not in z or len(z['degrees'])!=2 or 'codegree' not in z:continue
        du,dv=z['degrees'];c=z['codegree']
        bound=z.get('bound',z.get('best_bound'))
        pos=z.get('positions',z.get('best_positions'))
        assert bound is not None and pos is not None
        counts={int(m):n for m,n in z['counts'].items() if n}
        expected={0:35-du-dv+c,1:du-c,2:dv-c,3:c}
        assert counts=={m:n for m,n in expected.items() if n}
        assert Fraction(bound)<1 if z['strict'] else Fraction(bound)>=1
        lookup[(du,dv,c)].append({'source':str(fp.relative_to(ROOT)),
                                'degrees':[du,dv],'codegree':c,'bound':bound,
                                'positions':pos,'strict':z['strict'],
                                'uses_paircover_quotas':fp.name=='DOUBLES.json' and any(Fraction(r['deduction']) for r in z['rows'])})

projection=defaultdict(set);pairtypes=defaultdict(set)
for job in spectra:
    histogram=Counter(job['degrees']);assert len(job['degrees'])==21 and sum(job['degrees'])==175
    for du,dv in combinations_with_replacement(sorted(histogram),2):
        if du==dv and histogram[du]<2:continue
        pairtypes[(du,dv)].add(job['spectrum_id'])
        for c in range(5,min(du,dv)+1):projection[(du,dv,c)].add(job['spectrum_id'])

missing=sorted(set(projection)-set(lookup));new=[]
if missing:
    sys.dont_write_bytecode=True
    sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
    from subset_position_dp import SubsetEngine
    from independent_structure_bounds import independent_rows
    for du,dv,c in missing:
        ns={0:35-du-dv+c,1:du-c,2:dv-c,3:c}
        engine=SubsetEngine(21,2,ns);engine.inv={p:(0,0,[]) for p in engine.inv}
        vals=[];cache={}
        for pos in ((10,21),(21,10)):
            bp={k:1<<v for v,k in enumerate(pos)};left=0;rr=[]
            for k in range(1,22):
                p=bp.get(k,0);rr.append(engine.value(k,left,p));left|=p
            val=Fraction(sum(rr),engine.D);vals.append((val,pos));cache[pos]=rr
        value,pos=min(vals)
        masks=[m for m,n in ns.items() for _ in range(n)]
        stubs=[frozenset(v+1 for v in range(2) if m>>v&1) for m in masks]
        rr=independent_rows(21,pos,stubs)
        assert value==sum((min(r['A'],r['B'],r['C']) for r in rr),Fraction())
        assert all(Fraction(a,engine.D)==min(b['A'],b['B'],b['C']) for a,b in zip(cache[pos],rr))
        z={'source':'NEW_FIXED2_ZERO_QUOTA','degrees':[du,dv],'codegree':c,
           'bound':str(value),'positions':pos,'strict':value<1,'uses_paircover_quotas':False,
           'expanded35_masks':masks,'all_fixed':[{'bound':str(v),'positions':p} for v,p in vals],
           'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rr]}
        lookup[(du,dv,c)].append(z);new.append(z)
        assert time.process_time()-START<10,'10 CPU cutoff'

keys=[];best={}
for key,ids in sorted(projection.items()):
    # Prefer an existing zero-quota strict certificate over a quota import when
    # either is sufficient; within a class the smallest exact bound is retained.
    candidates=lookup[key]
    choice=min(candidates,key=lambda z:(not z['strict'],z['uses_paircover_quotas'],Fraction(z['bound'])))
    best[key]=choice
    keys.append({'degrees':list(key[:2]),'codegree':key[2],'spectrum_ids':sorted(ids),
                 'strict':choice['strict'],'selected_certificate':choice,
                 'all_existing_certificates':candidates})
jobs=[]
for job in spectra:
    sid=job['spectrum_id'];hist=Counter(job['degrees']);exceptions=[];actualpair=[]
    for du,dv in sorted(pairtypes):
        if sid not in pairtypes[(du,dv)]:continue
        multiplicity=hist[du]*hist[dv] if du!=dv else hist[du]*(hist[du]-1)//2
        failed=[c for c in range(5,min(du,dv)+1) if not best[(du,dv,c)]['strict']]
        actualpair.append({'degrees':[du,dv],'actual_pointpair_count':multiplicity,
                           'all_codegrees_checked':list(range(5,min(du,dv)+1)),
                           'not_excluded_codegrees':failed})
        if failed:exceptions.append({'degrees':[du,dv],'actual_pointpair_count':multiplicity,
                                     'not_excluded_codegrees':failed})
    excluded_sharp=tuple(sorted(job['degrees'])) not in sharp
    fully_capped=not exceptions
    jobs.append({'spectrum_id':sid,'degrees':job['degrees'],'a7':job['a7'],'a8':job['a8'],
                 'e':job['e'],'part':job['part'],'W':job['W'],'scalar_strict':job['all_strict'],
                 'scalar_maximum_twice_L':job['maximum_twice_L'],
                 'actual_selected_degree_pairs':actualpair,'exceptional_pair_types':exceptions,
                 'maximum_number_of_potential_exceptional_actual_pairs':sum(z['actual_pointpair_count'] for z in exceptions),
                 'all_lambda_le4_under_nonB':fully_capped,
                 'not_in_sharp_q3_five_spectra':excluded_sharp,
                 'Gamma_min4_via_sharp_q3_contrapositive':excluded_sharp,
                 'ready_scope_given_declared_imports':job['all_strict'] and fully_capped and excluded_sharp})

strictjobs=[j for j in jobs if j['scalar_strict']]
ready=[j['spectrum_id'] for j in jobs if j['ready_scope_given_declared_imports']]
result={'status':'COMPLETE_99_ACTUAL_PAIR_PROJECTION','scope':__doc__,
        'review_independence':'same-family','acceptance_status':'provisional',
        'spectra':99,'actual_degree_pair_types':len(pairtypes),'degree_pair_codegree_keys':len(projection),
        'existing_source_files':[str(f.relative_to(ROOT)) for f in files],
        'missing_old_keys':missing,'new_fixed2_certificates':new,
        'nonB_all_lambda_le4_spectrum_ids':[j['spectrum_id'] for j in jobs if j['all_lambda_le4_under_nonB']],
        'spectra_with_unexcluded_pairs':[j['spectrum_id'] for j in jobs if not j['all_lambda_le4_under_nonB']],
        'unexcluded_degree_pair_codegree_keys':[{'degrees':list(k[:2]),'codegree':k[2],
                                               'spectrum_ids':sorted(projection[k]),'best_bound':best[k]['bound']}
                                              for k in sorted(projection) if not best[k]['strict']],
        'scalar_strict_spectrum_count':len(strictjobs),
        'strict_spectra_in_sharp_q3_five':[j['spectrum_id'] for j in strictjobs if not j['not_in_sharp_q3_five_spectra']],
        'strict_spectra_with_unexcluded_pairs':[j['spectrum_id'] for j in strictjobs if not j['all_lambda_le4_under_nonB']],
        'ready_scope_given_declared_imports_ids':ready,'ready_scope_count':len(ready),
        'keys':keys,'jobs':jobs,'no_unstrict_key_asserted_realizable':True,
        'no_min8_global_theorem_imported':True,'no_old_certificates_rerun':True,
        'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'READY_SCOPE.json').write_text(json.dumps([j for j in jobs if j['ready_scope_given_declared_imports']],indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('keys','jobs','new_fixed2_certificates')}))

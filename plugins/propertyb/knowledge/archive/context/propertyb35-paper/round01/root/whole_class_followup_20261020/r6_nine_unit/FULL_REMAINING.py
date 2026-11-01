"""Authorized once-only completion of the 87 remaining exact-DP orbits.
Reuse13 existing DP witnesses and5 already-strict old affine layouts.
Same SubsetEngine and quotas, no new locks, model or position algorithm.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5]
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
D=json.loads((P/'DOMAIN.json').read_text());old=json.loads((P/'RESULT.json').read_text())
(P/'FIRST_STOP_RESULT.json').write_text(json.dumps(old,indent=2)+'\n')
records=D['records'];groups={}
for z in records:groups.setdefault((tuple(z['canonical_large']),z['canonical_lowmask']),[]).append(z)
cache={(tuple(z['canonical_large']),z['canonical_lowmask']):z for z in old['records']}
assert len(cache)==13

def convert(x):
 if isinstance(x,Fraction):return str(x)
 if isinstance(x,dict):return {str(k):convert(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [convert(v) for v in x]
 return x

def projection(entry):
 ns={int(t):n for t,n in entry['counts'].items()};low=set(entry['low']);lm=sum(1<<i for i in low);high=sorted(set(range(9))-low)
 signatures=[]
 for x in high:
  M=[];S=[];pure=[]
  for t,n in ns.items():
   if not(t>>x&1):continue
   lt=sorted(i for i in low if t>>i&1)
   if len(lt)==2:M.append(lt)
   elif len(lt)==1:S.append(lt[0])
   elif not lt:pure.append({'trace':t,'multiplicity':n})
   else:raise AssertionError
  assert sorted(sum(M,[])+S)==sorted(low)
  signatures.append({'high':x,'matching':sorted(M),'private_lows':sorted(S),'s':len(S),'dF':len(M)+len(S),'d0':sum(z['multiplicity'] for z in pure),'pure_high_traces':pure})
 pairs=[]
 for x,y in combinations(high,2):
  common=[{'trace':t,'low_trace':[i for i in low if t>>i&1],'multiplicity':n} for t,n in ns.items() if t>>x&1 and t>>y&1]
  assert sum(z['multiplicity'] for z in common)==1
  pairs.append({'pair':[x,y],'common':common})
 hm=sum(1<<i for i in high)
 triple=[{'trace':t,'low_trace':[i for i in low if t>>i&1],'multiplicity':n} for t,n in ns.items() if t&hm==hm]
 sizes=sorted(z['s'] for z in signatures)
 return {'signatures':signatures,'private_size_multiset':sizes,'seven_pairs':pairs,'seven_triple_common':triple,
         'same_pure_high_edge':ns.get(hm,0)==1,'in_first_failure_necessary_class':sizes==[0,2,4] and ns.get(hm,0)==1}

start=time.process_time();done=[];processed=set();new_dp=0;reason='complete'
for key,zs in groups.items():
 if time.process_time()-start>=44:reason='45_CPU_budget_with_one_second_reserve';break
 z=zs[0];ns={int(t):n for t,n in z['counts'].items()};tm=time.process_time()
 if key in cache:
  entry=dict(cache[key]);entry['new_cpu_seconds']=0;entry['completion_source']='reused_13_prior_exact_DP'
 elif Fraction(z['old_17_layout_bound'])<1:
  eng=SubsetEngine(25,9,ns);w=eng.verify({'bound':Fraction(z['old_17_layout_bound']),'positions':z['old_positions'],'counts':ns})
  entry={'base':z['base'],'low':z['low'],'source':'old_affine_layout_new_row_replay','new_cpu_seconds':time.process_time()-tm,'completion_source':'reused_5_old_affine_strict_layouts',**w}
 else:
  eng=SubsetEngine(25,9,ns);w=eng.verify(eng.solve());new_dp+=1
  entry={'base':z['base'],'low':z['low'],'source':'remaining_exact_DP','new_cpu_seconds':time.process_time()-tm,'completion_source':'new_remaining_exact_DP',**w}
 entry['raw_witness_bound']=BareLayout(25,entry['positions']).bound(ns)
 entry['canonical_large']=key[0];entry['canonical_lowmask']=key[1]
 entry['orbit_size']=len(zs);entry['colored_orbit_labels']=[v['low'] for v in zs]
 entry['projection']=projection(entry)
 done.append(entry);processed.add(key)
 print('done',len(done),'base',z['base'],'bound',entry['bound'],'newDP',new_dp,'CPU',time.process_time()-start,flush=True)
remaining=[{'base':zs[0]['base'],'low':zs[0]['low'],'low_labels':[z['low'] for z in zs],'canonical_large':key[0],'canonical_lowmask':key[1]} for key,zs in groups.items() if key not in processed]
failed=[z for z in done if Fraction(z['bound'])>=1]
strict=[z for z in done if Fraction(z['bound'])<1]
certs=[]
for entry in done:
 key=(tuple(entry['canonical_large']),entry['canonical_lowmask']);zs=groups[key];rep=zs[0]
 cp=[0]*9
 for i,j in enumerate(rep['old_to_canonical']):cp[j]=entry['positions'][i]
 for z in zs:
  certs.append({'base':z['base'],'low':z['low'],'counts':z['counts'],'positions':[cp[z['old_to_canonical'][i]] for i in range(9)],'bound':entry['bound'],'raw_witness_bound':entry['raw_witness_bound'],'strict':Fraction(entry['bound'])<1,'representative_base':entry['base'],'representative_low':entry['low'],'canonical_large':key[0],'canonical_lowmask':key[1]})
summary={'complete':not remaining,'stop_reason':reason,'domain_labels':140,'domain_orbits':105,
 'processed_orbits':len(done),'processed_labels':len(certs),'new_DP_orbits':new_dp,'reused_prior_DP_orbits':13,
 'reused_old_affine_strict_orbits':sum(z['completion_source']=='reused_5_old_affine_strict_layouts' for z in done),
 'strict_orbits':len(strict),'strict_labels':sum(z['orbit_size'] for z in strict),
 'failed_orbits':len(failed),'failed_labels':sum(z['orbit_size'] for z in failed),
 'all_failed_in_first_necessary_class':all(z['projection']['in_first_failure_necessary_class'] for z in failed),
 'remaining_orbits':len(remaining),'new_CPU_seconds':time.process_time()-start,
 'prior_profile_DP_CPU':old['prior_profile_cpu_seconds'],'prior_first_stop_CPU':old['new_cpu_seconds']}
(P/'FULL_RESULT.json').write_text(json.dumps(convert({'summary':summary,'records':done,'remaining':remaining}),indent=2)+'\n')
(P/'FAILED_SIGNATURES.json').write_text(json.dumps(convert([{'base':z['base'],'low':z['low'],'low_labels':z['colored_orbit_labels'],'orbit_size':z['orbit_size'],'counts':z['counts'],'bound':z['bound'],'positions':z['positions'],'raw_witness_bound':z['raw_witness_bound'],'projection':z['projection']} for z in failed]),indent=2)+'\n')
(P/'ALL140_CERTIFICATES.json').write_text(json.dumps(convert(certs),indent=2)+'\n')
(P/'COMPLETION_SUMMARY.json').write_text(json.dumps(convert(summary),indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

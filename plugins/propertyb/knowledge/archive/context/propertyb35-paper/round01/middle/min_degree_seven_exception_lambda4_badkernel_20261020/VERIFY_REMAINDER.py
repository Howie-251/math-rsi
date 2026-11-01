"""Resume only remaining97 new certificates after the bounded350 prefix; no complete-domain or prior-certificate rerun."""
from pathlib import Path
from fractions import Fraction
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
st=time.process_time();r=json.loads((P/'RESULT.json').read_text());prefix=json.loads((P/'VERIFY_RESULT.json').read_text());assert prefix['status']=='CPU_BOUNDED_PARTIAL';done=prefix['new_original35_certificates_replayed'];cases=[z for z in r['all_checked_cases'] if not z['reused_verified_previous_case']];assert done==350 and len(cases)==447
saved=[json.loads(s) for s in (P/'VERIFY_ROWS.jsonl').read_text().splitlines()];assert len(saved)==done
for a,b in zip(saved,cases):assert a['counts']==b['counts'] and a['bound']==b['best']['bound']
maximum=Fraction(prefix['maximum_strict_bound']);stream=(P/'VERIFY_REMAINDER_ROWS.jsonl').open('w');n=0
for z in cases[done:]:
 masks=[m for m,num in enumerate(z['counts']) for _ in range(num)];assert len(masks)==35;types=[frozenset(i+1 for i in range(4) if m>>i&1) for m in masks];rr=independent_rows(21,tuple(z['best']['positions']),types);v=sum((min(x['A'],x['B'],x['C']) for x in rr),Fraction());assert v==Fraction(z['best']['bound'])<1;n+=1;maximum=max(maximum,v)
 stream.write(json.dumps({'counts':z['counts'],'quad':z['quad'],'expanded35_masks':masks,'positions':z['best']['positions'],'bound':str(v),'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in x.items()} for x in rr]})+'\n')
stream.close();assert n==97
out={'status':'PASS_COMPLETE_447_WITH_FULL_DOMAIN_AND_CONTEXTS','scope':__doc__,'complete_domain_verification_source':'VERIFY_RESULT.json','complete_lowcost_quad_domains':29,'complete_lowcost_labeled_keys':7952,'complete_lowcost_D8_representatives':1002,'all24_taucontexts_independently_equal':True,'reused_previously_audited_certificates':226,'original35_new_certificates_replayed':done+n,'position_rows':21*(done+n),'strict_new_certificates':done+n,'maximum_strict_bound':str(maximum),'prefix_cpu_seconds':prefix['cpu_seconds'],'continuation_cpu_seconds':time.process_time()-st,'total_independent_cpu_seconds':prefix['cpu_seconds']+time.process_time()-st,'primary_pilot_cpu_seconds':r['cpu_seconds'],'original_budget_cutoff_preserved':True,'remainder_only_authorized_by_parent':True};(P/'FINAL_VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

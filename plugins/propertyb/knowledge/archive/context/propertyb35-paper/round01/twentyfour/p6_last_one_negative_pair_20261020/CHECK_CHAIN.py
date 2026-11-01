"""Exact setpartition of the existing123621 necessary P-source keys, no newdomain."""
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;start=time.process_time()
def key(r):
 if 'source_key' in r:return json.dumps(r['source_key'],separators=(',',':'))
 return json.dumps([r['inventory'],r['nine'],r['higher'],r['J']],separators=(',',':'))
def load(p):
 out=set();n=0
 with p.open() as f:
  for s in f:
   r=json.loads(s);k=key(r);assert k not in out;out.add(k);n+=1
 return out
c=BASE/'p6_residual_census_20261020';b=BASE/'positive_occ_three/nine_positive_joint_negative_budget_20261020/budget21_difference';a=BASE/'p6_tail79_common_gate_20261020'
prefix=load(c/'CENSUS_PASSED.jsonl');pending=load(c/'CENSUS_NONGATED.jsonl');assert len(prefix)==115052 and len(pending)==8569 and not prefix&pending
stages=[('nine20',c/'nine_gate_selection_20261020/NINE_CANDIDATE_SOURCES.jsonl',c/'nine_gate_selection_20261020/TAIL549.jsonl',8020,549),
 ('eight_oneT20B',c/'tail186_analysis/NEW_EIGHT_363.jsonl',c/'tail186_analysis/TAIL186.jsonl',363,186),
 ('eight_mixed_B21',c/'tail186_analysis/MIXED21_SOURCES47.jsonl',c/'tail186_analysis/AFTER_MIXED21_TAIL139.jsonl',47,139),
 ('nine21',b/'P6_OWN_SOURCES.jsonl',b/'P6_REMAINING.jsonl',60,79),
 ('ten_twoT',a/'TEN_SOURCES59.jsonl',a/'ROOT_CURRENT_TAIL20.jsonl',59,20),
 ('new_mixed_eight_twoT19B',a/'CANDIDATE_MIXED8_SOURCES19.jsonl',a/'IF_MIXED8_ACCEPTED_TAIL1.jsonl',19,1)]
allcovered=set(prefix);report=[]
for name,wp,rp,wcount,rcount in stages:
 wins=load(wp);remaining=load(rp)
 assert len(wins)==wcount and len(remaining)==rcount
 assert not wins&remaining and wins|remaining==pending and not wins&allcovered
 report.append({'gate':name,'incoming':len(pending),'accepted_keys':wcount,'remaining':rcount,'winner_file':str(wp.relative_to(BASE)),'tail_file':str(rp.relative_to(BASE))})
 allcovered|=wins;pending=remaining
assert len(allcovered)==123620 and len(pending)==1 and not allcovered&pending
last=json.loads((HERE/'CHECK.json').read_text());lastkey=json.dumps(last['own_source_key'],separators=(',',':'));assert pending=={lastkey}
assert len(allcovered|pending)==123621
out={'status':'PASS','scope':'ExistingnecessaryPdomain only. Import earlierprovedselectors; lasttwo newgates retain root/audit statuses separately.','domain_keys':123621,'original_passed':len(prefix),'stages':report,'last_actual_negativepair_caller':lastkey,'keys_after_new_N2_gate':123621,'all_disjoint_and_exhaustive':True,'not_an_H_realization_claim':True,'cpu_seconds':time.process_time()-start}
(HERE/'CHECK_CHAIN.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='stages'})

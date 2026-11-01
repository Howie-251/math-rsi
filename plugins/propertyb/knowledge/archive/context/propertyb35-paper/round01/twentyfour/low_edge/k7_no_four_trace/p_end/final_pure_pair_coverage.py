"""Final six/seven/eight actual callers; frozen P graph domain is corroboration only."""
from coverage_eight_positive import *
def callers(edges):
 s,private,w=classify(edges);co=Counter(tuple(e) for e in edges);six=[];seven=[];eight=[]
 for a,b in combinations(range(1,7),2):
  if (a,b) in MISSING or co[a,b]:continue
  q=s[a]+s[b]
  if not 2<=q<=4:continue
  cut=dict(blue=[a,b],G_degree_sum=q,positive_four=10-q,negative_three=5-q,negative_four=16+q)
  if q==4:six.append(cut)
  if q==3:seven.append(cut)
  if q==2:eight.append(cut)
 return s,private,w,dict(Cprime6=six,I7=seven,H8_c3=eight)
def main():
 st=time.time();d=json.loads((HERE/'DOMAIN.json').read_text());auts=[p for p in permutations(range(7)) if {tuple(sorted((p[a],p[b]))) for a,b in MISSING}==MISSING];assert len(auts)==16
 rows=[];rep={};counts=Counter()
 for r in d['orbits']:
  edges=[tuple(e)for e in r['edges']];s,private,w,gates=callers(edges)
  assert 5<=sum(s[1:])<=10 and (gates['H8_c3'] or gates['I7'])
  old=any(w[k] for k in 'ABCDEFG');H=bool(w['H']);c6=bool(gates['Cprime6']);i7=bool(gates['I7'])
  status=dict(old_AG=old,H8_all=H,Cprime6=c6,I7=i7,H8_c3=bool(gates['H8_c3']),H8_plus_Cprime6=H or c6,old_AG_H8_Cprime6=old or H or c6,final_AG_H8_Cprime6_I7=old or H or c6 or i7,unified_c3_three_gates=any(gates.values()),unified_c3_seven_eight=bool(gates['H8_c3']or gates['I7']))
  for p in auts:
   moved=[tuple(sorted((p[a],p[b])))for a,b in edges];_,_,_,mg=callers(moved)
   for key in gates:
    expected={tuple(sorted((p[z['blue'][0]],p[z['blue'][1]])))for z in gates[key]}
    assert expected=={tuple(z['blue'])for z in mg[key]}
  rep[r['id']]=status
  chosen=next((key,z) for key in ('H8_c3','I7','Cprime6')for z in gates[key])
  row=dict(id=r['id'],edges=edges,degrees=s,singleton_counts=private,labelled_count=r['labelled_count'],status=status,chosen_gate=chosen[0],chosen_cut=chosen[1],all_new_callers=gates)
  rows.append(row)
  for key,val in status.items():
   counts[key+'_orbits']+=val;counts[key+'_labels']+=r['labelled_count']*val
 for lab in d['labelled']:
  edges=[PAIRS[k]for k in lab['edge_indices']];_,_,w,gates=callers(edges)
  status=rep[lab['orbit']]
  assert status['old_AG']==any(w[k]for k in 'ABCDEFG') and status['H8_all']==bool(w['H'])
  for key in ('Cprime6','I7','H8_c3'):assert status[key]==bool(gates[key])
  assert gates['H8_c3'] or gates['I7']
 assert len(rows)==3326 and len(d['labelled'])==40968
 out=dict(status='PASS',scope=__doc__,domain_orbits=len(rows),domain_labels=len(d['labelled']),automorphism_order=16,counts=dict(counts),unified_three_gate_chosen_orbits=dict(Counter(r['chosen_gate']for r in rows)),corroborates_analytic_selection_lemma=True,rows=rows,elapsed_seconds=time.time()-st)
 (HERE/'final_pure_pair_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
if __name__=='__main__':main()

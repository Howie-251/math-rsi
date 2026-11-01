"""New actual eight-positive caller on frozen DOMAIN; preserves all old A--G files."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json,time
HERE=Path(__file__).parent
PAIRS=list(combinations(range(7),2));MISSING={(0,1),(0,2),(3,4),(5,6)}
C=[2]+[3]*6
def classify(edges):
 mult=Counter(tuple(e) for e in edges);s=[0]*7
 for (a,b),n in mult.items():s[a]+=n;s[b]+=n
 private=[8-C[i]-s[i] for i in range(7)]
 w={k:[] for k in 'ABCDEFGH'}
 for a,b in PAIRS:
  h=mult[a,b];missing=(a,b) in MISSING
  if a and b and not missing:
   if s[a]==s[b]==3 and h>=1:w['A'].append([a,b])
   if sorted((s[a],s[b]))==[2,3] and h==1:w['B'].append([a,b])
   if s[a]==s[b]==2 and h==0:w['C'].append([a,b])
   if sorted((s[a],s[b]))==[2,3] and h==2:w['G'].append([a,b])
  if not missing and all(a in e or b in e for e in edges):w['E'].append([a,b])
  if a and b and missing and s[a]==s[b]==3 and h==3:w['F'].append([a,b])
  # Full exact two-blue cut, reconstructed from the original actual edge types.
  internal=[set(range(7))-set(e) for e in MISSING]
  blue={a,b};red=set(range(7))-blue
  if any(e<=blue or e<=red for e in internal):continue
  pos4=sum(private[v] for v in blue);pos3=sum(n for e,n in mult.items() if set(e)<=blue)
  neg3=sum(n for e,n in mult.items() if set(e)<=red);neg4=sum(private[v] for v in red)
  if pos3==0 and pos4==8 and neg3<=3 and neg4<=18:
   w['H'].append(dict(blue=[a,b],positive_four=pos4,positive_three=pos3,negative_three=neg3,negative_four=neg4,blue_G_degrees=[s[a],s[b]],blue_internal_degrees=[C[a],C[b]]))
 if s[0]==5:w['D'].append([0])
 return s,private,w
def main():
 st=time.time();d=json.loads((HERE/'DOMAIN.json').read_text());old=json.loads((HERE/'EXTENDED_COVERAGE.json').read_text());auts=[p for p in permutations(range(7)) if {tuple(sorted((p[a],p[b]))) for a,b in MISSING}==MISSING]
 assert len(auts)==16 and all(p[0]==0 for p in auts)
 rows=[];repcache={};all_keys=set();types=Counter()
 old_surv={r['id'] for r in old['survivors']['ABCDEFG']}
 for r in d['orbits']:
  edges=[tuple(e) for e in r['edges']];s,private,w=classify(edges)
  before=any(w[k] for k in 'ABCDEFG');after=before or bool(w['H'])
  assert (not before)==(r['id'] in old_surv)
  for p in auts:
   moved=[tuple(sorted((p[a],p[b]))) for a,b in edges];_,_,ww=classify(moved)
   expected={tuple(sorted((p[h['blue'][0]],p[h['blue'][1]]))) for h in w['H']}
   assert expected=={tuple(h['blue']) for h in ww['H']}
   assert before==any(ww[k] for k in 'ABCDEFG')
  repcache[r['id']]=(before,after,bool(w['H']))
  row=dict(id=r['id'],edges=edges,degrees=s,singleton_counts=private,degree_profile=r['degree_profile'],labelled_count=r['labelled_count'],old_AG_covered=before,new_eight_positive_covered=bool(w['H']),newly_covered=not before and bool(w['H']),remaining=not after,witnesses=w['H'])
  rows.append(row)
  if row['newly_covered']:
   for h in w['H']:types[str((h['blue_internal_degrees'],h['blue_G_degrees']))]+=1
 for lab in d['labelled']:
  ids=lab['edge_indices'];edges=[PAIRS[k] for k in ids];_,_,w=classify(edges)
  before=any(w[k] for k in 'ABCDEFG');after=before or bool(w['H']);assert repcache[lab['orbit']]==(before,after,bool(w['H']))
  all_keys.add(tuple(ids))
 assert len(all_keys)==len(d['labelled'])==40968 and len(rows)==3326
 counts={}
 for key in ('old_AG_covered','new_eight_positive_covered','newly_covered','remaining'):
  counts[key+'_orbits']=sum(r[key] for r in rows);counts[key+'_labels']=sum(r['labelled_count'] for r in rows if r[key])
 result=dict(status='PASS',scope=__doc__,domain_labels=len(all_keys),domain_orbits=len(rows),automorphism_order=16,counts=counts,new_witness_types=dict(types),remaining_degree_profiles=dict(Counter(str(r['degree_profile']) for r in rows if r['remaining'])),newly_covered=[r for r in rows if r['newly_covered']],remaining=[r for r in rows if r['remaining']],all_eight_positive_callers=[r for r in rows if r['new_eight_positive_covered']],elapsed_seconds=time.time()-st)
 (HERE/'coverage_eight_positive.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('newly_covered','remaining','all_eight_positive_callers')},indent=2))
 print('first remaining',[(r['id'],r['edges'],r['degrees']) for r in result['remaining'][:15]])
if __name__=='__main__':main()

"""Complete necessary seven-P-point graph: five loopless edges WITH repetitions, s0<=5, si<=3 for i>0.
No hypergraph or external incidence layout is enumerated. Quotient by the true Aut(P3+2K2).
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
import json,time
HERE=Path(__file__).parent;PAIRS=list(combinations(range(7),2));IDX={p:i for i,p in enumerate(PAIRS)};MISSING={(0,1),(0,2),(3,4),(5,6)}

def classify(edgeids):
 mult=Counter(edgeids);s=[0]*7
 for k,n in mult.items():
  i,j=PAIRS[k];s[i]+=n;s[j]+=n
 witnesses={x:[] for x in 'ABCD'}
 for i,j in combinations(range(1,7),2):
  if (i,j) in MISSING:continue
  h=mult.get(IDX[i,j],0)
  if s[i]==s[j]==3 and h>=1:witnesses['A'].append([i,j,h])
  if sorted((s[i],s[j]))==[2,3] and h==1:witnesses['B'].append([i,j,h])
  if s[i]==s[j]==2 and h==0:witnesses['C'].append([i,j,h])
 if s[0]==5:witnesses['D'].append([0])
 return s,witnesses

def describe(edgeids):
 s,w=classify(edgeids);mult=Counter(edgeids);seen=set();components=[]
 for i in range(7):
  if i in seen:continue
  stack=[i];seen.add(i);comp=[]
  while stack:
   v=stack.pop();comp.append(v)
   for k in mult:
    if v in PAIRS[k]:
     z=PAIRS[k][1] if v==PAIRS[k][0] else PAIRS[k][0]
     if z not in seen:seen.add(z);stack.append(z)
  components.append(sorted(comp))
 return dict(edges=[PAIRS[k] for k in edgeids],edge_multiplicities=[dict(pair=PAIRS[k],multiplicity=n) for k,n in sorted(mult.items())],degrees=s,degree_profile=[s[0],sorted(s[1:],reverse=True)],num_degree3=sum(d==3 for d in s[1:]),num_degree2=sum(d==2 for d in s[1:]),max_multiplicity=max(mult.values()),components=components,callers={k:bool(z) for k,z in w.items()},caller_witnesses=w)

def main():
 st=time.time();auts=[]
 for p in permutations(range(7)):
  if {tuple(sorted((p[i],p[j]))) for i,j in MISSING}==MISSING:auts.append(p)
 assert len(auts)==16 and all(p[0]==0 for p in auts);maps=[(p,[IDX[tuple(sorted((p[i],p[j])))] for i,j in PAIRS]) for p in auts];seen={};orbits=[];labelled=[];counts=Counter();profiles=Counter();input_count=0
 for edgeids in combinations_with_replacement(range(21),5):
  input_count+=1;s,w=classify(edgeids)
  if s[0]>5 or max(s[1:])>3:continue
  covered=any(w.values());counts['valid']+=1;counts['covered' if covered else 'uncovered']+=1;profiles[str([s[0],sorted(s[1:],reverse=True)])]+=1
  for c in 'ABCD':counts['caller_'+c]+=bool(w[c])
  if edgeids not in seen:
   idx=len(orbits);z=describe(edgeids);z.update(id=idx,labelled_count=0);orbits.append(z)
   for p,mp in maps:seen[tuple(sorted(mp[k] for k in edgeids))]=(idx,p)
  idx,p=seen[edgeids];orbits[idx]['labelled_count']+=1;labelled.append(dict(edge_indices=edgeids,orbit=idx,from_representative_permutation=p))
 uncovered=[r for r in orbits if not any(r['callers'].values())];uprof=Counter(str(r['degree_profile']) for r in uncovered);ulabelprof=Counter()
 for r in uncovered:ulabelprof[str(r['degree_profile'])]+=r['labelled_count']
 result=dict(scope=__doc__,complete=True,input_multisets=input_count,pair_types=PAIRS,missing_edges=sorted(MISSING),automorphisms=auts,automorphism_order=16,counts=dict(counts),orbit_count=len(orbits),covered_orbits=len(orbits)-len(uncovered),uncovered_orbits=len(uncovered),degree_profile_labelled_counts=dict(profiles),uncovered_degree_profile_orbit_counts=dict(uprof),uncovered_degree_profile_labelled_counts=dict(ulabelprof),uncovered_representatives=uncovered,elapsed_seconds=time.time()-st)
 assert input_count==53130
 (HERE/'BASELINE_COVERAGE.json').write_text(json.dumps(result,indent=2)+'\n');(HERE/'DOMAIN.json').write_text(json.dumps(dict(scope=__doc__,complete=True,orbits=orbits,labelled=labelled),indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('pair_types','automorphisms','uncovered_representatives','degree_profile_labelled_counts')})
if __name__=='__main__':main()

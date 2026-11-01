from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction as Q
import json
P=Path(__file__).resolve().parent;B=P.parent
D=json.loads((B/'DOMAIN.json').read_text())['records'];G=defaultdict(list)
for i,z in enumerate(D):G[(tuple(z['canonical_large']),z['canonical_lowmask'])].append(i)
lookup={(z['base'],tuple(z['low'])):(tuple(z['canonical_large']),z['canonical_lowmask']) for z in D}
oldpilots={lookup[(z['base'],tuple(z['low']))] for z in json.loads((B/'PROFILE.json').read_text())['records']}
counts=Counter();candidates=[]
for key,ids in G.items():
 good=[i for i in ids if Q(D[i]['old_bound'])<1]
 counts['all_old_strict' if len(good)==len(ids) else 'some_old_strict' if good else 'no_old_strict']+=1
 if good or key in oldpilots:continue
 idx=min(ids,key=lambda i:(Q(D[i]['old_bound']),i));z=D[idx];ns={int(t):v for t,v in z['counts'].items()};lm=sum(1<<i for i in z['low'])
 private=sorted(sum(v for t,v in ns.items() if t>>i&1 and (t&lm).bit_count()==1) for i in range(9) if not(lm>>i&1))
 assert all(s in (1,3,5) for s in private)
 maxblock=max(t.bit_count() for t in ns);sizehist=tuple(sum(v for t,v in ns.items() if t.bit_count()==k) for k in range(2,6))
 z={**z,'domain_record':idx,'orbit_records':ids,'orbit_size':len(ids),'seven_private_signature':private,'max_block':maxblock,'empty':ns.get(0,0),'large_size_histogram':sizehist}
 candidates.append(z)
ordered=sorted(candidates,key=lambda z:(Q(z['old_bound']),z['domain_record']))
for rank,z in enumerate(ordered):z['old_bound_rank_bin']=min(4,5*rank//len(ordered))
def feats(z):
 return [('private',tuple(z['seven_private_signature'])),('maxblock',z['max_block']),('empty',z['empty']),('oldbin',z['old_bound_rank_bin']),('joint',tuple(z['seven_private_signature']),z['max_block'],z['empty']),('hist',tuple(z['large_size_histogram']))]
# Greedy novelty across true structural categories; bound extremes break ties.
chosen=[];seen=Counter();remaining=list(candidates)
for k in range(40):
 def score(z):return (sum((2 if f[0] in ('private','maxblock','empty','oldbin') else 1)/(1+seen[f]) for f in feats(z)),Q(z['old_bound']),-z['domain_record'])
 z=max(remaining,key=score);remaining.remove(z);chosen.append(z)
 for f in feats(z):seen[f]+=1
assert len({(tuple(z['canonical_large']),z['canonical_lowmask']) for z in chosen})==40
out={'scope':'Forty diverse genuinely old-uncovered colored orbits, excluding all three earlier pilots; not a domain sweep','old_coverage_counts':dict(counts),'prior_pilot_orbits':3,'genuine_uncovered_after_old_and_pilot':len(candidates),'selected':40,'selected_private_signatures':sorted({tuple(z['seven_private_signature']) for z in chosen}),'selected_maxblocks':sorted({z['max_block'] for z in chosen}),'selected_empties':sorted({z['empty'] for z in chosen}),'selected_old_bins':sorted({z['old_bound_rank_bin'] for z in chosen}),'records':chosen}
(P/'SELECTION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'}))

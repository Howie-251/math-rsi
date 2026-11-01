#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
from fractions import Fraction as Q
from time import process_time
import json,sys
P=Path(__file__).resolve().parent;ROOT=next(p for p in P.parents if (p/'computations').exists());S=ROOT/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True;sys.path.insert(0,str(S))
from unit_catalogue import fullblocks,canonical
start=process_time();src=json.loads((S/'UNIT_CATALOGUE_9.json').read_text());old=json.loads((ROOT/'context/propertyb35-paper/round01/twentyfive/UNIT9_MIXED_AFFINE.json').read_text());oldfamilies={z['base']:z for z in old['families']};records=[];groups=defaultdict(list);counts=Counter()
assert src['complete'] and len(src['orbits'])==374 and old['complete']
for base,big in enumerate(src['orbits']):
 bs=fullblocks(big,9);h=[7-sum(bool(t>>i&1) for t in bs) for i in range(9)]
 for low in combinations(range(9),4):
  lm=sum(1<<i for i in low)
  if any((t&lm).bit_count()>2 for t in bs):counts['excluded_low_ge3']+=1;continue
  singles=[h[i]-int(i in low) for i in range(9)];empty=39-len(bs)-sum(h)
  if min(singles+[empty])<0:counts['excluded_negative']+=1;continue
  ns={t:1 for t in bs};ns.update({1<<i:n for i,n in enumerate(singles) if n})
  if empty:ns[0]=empty
  assert sum(ns.values())==35
  assert all(sum(n for t,n in ns.items() if t>>i&1)==7-int(i in low) for i in range(9))
  assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==1 for i,j in combinations(range(9),2))
  f=oldfamilies[base];assert f['feasible'];c=next(c for c in f['cases'] if c['q']==4)
  oldns={t:1 for t in f['full']};oldns.update({1<<i:n-int(i in low) for i,n in enumerate(f['single_high']) if n-int(i in low)})
  if c['empty']:oldns[0]=c['empty']
  assert ns==oldns
  values=[Q(a)+sum(Q(lay['slopes'][i]) for i in low) for a,lay in zip(c['layout_constants'],f['layouts'])];j=min(range(len(values)),key=values.__getitem__)
  canonical_big,perm=canonical(big,9,extra=[int(i in low) for i in range(9)],with_perm=True);color=sum(1<<perm[i] for i in low)
  private=sorted(sum(n for t,n in ns.items() if t>>i&1 and (t&lm).bit_count()==1) for i in range(9) if i not in low)
  assert all(s in (0,2,4) for s in private)
  z={'base':base,'low':low,'counts':ns,'canonical_large':canonical_big,'canonical_lowmask':color,'old_to_canonical':perm,'old_bound':str(values[j]),'positions':f['layouts'][j]['positions'],'seven_private_signature':private,'max_block':max(t.bit_count() for t in ns),'empty':empty}
  groups[(tuple(canonical_big),color)].append(len(records));records.append(z)
summary={'all_markings':374*126,**counts,'feasible_markings':len(records),'base_families':len({z['base'] for z in records}),'colored_orbits':len(groups),'old_strict_markings':sum(Q(z['old_bound'])<1 for z in records),'old_strict_orbits_any':sum(any(Q(records[i]['old_bound'])<1 for i in ids) for ids in groups.values()),'old_uncovered_orbits':sum(all(Q(records[i]['old_bound'])>=1 for i in ids) for ids in groups.values()),'cpu_seconds':process_time()-start}
out={'scope':'Actual25/35 pair-cover, exact four6 locks and five7 pairwiseunit locks, lowtrace<=2; exception caller separate. Full374 decomposition catalogue, all126 four-low markings.','complete_domain':True,'summary':summary,'records':records}
(P/'DOMAIN.json').write_text(json.dumps(out,indent=2)+'\n');(P/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))

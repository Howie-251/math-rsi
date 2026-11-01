"""Read every nongated P key; rebuild its own 35 traces and all blue choices.
No generating census import and no transfer of a menu's sample blue labels.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time

HERE=Path(__file__).resolve().parent;BASE=HERE.parent
PAIRS=tuple(combinations(range(6),2))
MASK=lambda s:sum(1<<v for v in s)
BLUE=[(tuple(s),MASK(s)) for k in (2,3) for s in combinations(range(6),k)]
KEYS=('P4','P3','P2','P1','N1','N2','N3','N4')

def main():
 start=time.process_time();census=json.loads((BASE/'CENSUS.json').read_text())
 menus={x['id']:{tuple(z['counts']) for z in x['signatures']} for x in census['menus']}
 totals=Counter();caseprofiles=Counter();two_profiles=Counter();groupsizes=Counter()
 bybest=Counter();bounds=Counter();examples={};inputs=[];allcases=[]
 rows=[json.loads(x) for x in (BASE/'CENSUS_NONGATED.jsonl').read_text().splitlines()]
 for iid,row in enumerate(rows):
  higher=[MASK(s) for s in row['higher']];d=[8]*6;d[row['nine']]=9
  si=[0]*6;edges=[]
  for (a,b),m in zip(PAIRS,row['J']):
   si[a]+=m;si[b]+=m;edges.extend([MASK((a,b))]*m)
  hi=[sum(bool(T>>v&1) for T in higher) for v in range(6)]
  ui=[d[v]-(v<5)-hi[v]-si[v] for v in range(6)]
  lb=[max(0,18-3*si[v]-sum(5-T.bit_count() for T in higher if T>>v&1)) for v in range(6)]
  assert min(ui)>=0 and all(lb[v]<=4*ui[v] for v in range(6))
  traces=[31]+higher+edges+[1<<v for v in range(6) for _ in range(ui[v])]
  assert len(traces)==35
  signatures=set();matches=[]
  for blue,bm in BLUE:
   cnt=Counter();colors=[]
   for trace in traces:
    hit=trace&bm
    if hit and hit!=trace:colors.append('.');continue
    kind=('P' if hit==trace else 'N')+str(5-trace.bit_count())
    cnt[kind]+=1;colors.append(kind)
   assert not set(cnt)-set(KEYS)
   sig=tuple(cnt[k] for k in KEYS)+(max(lb[v] for v in blue),)
   signatures.add(sig)
   if not (sig[:6]==(9,0,0,0,0,0) and sig[6]<=3 and sig[6]+sig[7]<=20):continue
   gs=[dict(vertex=v,private_edges=ui[v],private_union_lower_bound=lb[v],
            nine=(v==row['nine']),J_degree=si[v],high_count=hi[v],
            higher_exterior_capacity=sum(5-T.bit_count() for T in higher if T>>v&1))
       for v in blue if ui[v]]
   # A sufficient bound for a <=6-edge subfamily: keep a full star if <=6,
   # otherwise discard at most ui-6 four-sets, losing at most4 per removal.
   sub6=max(max(0,g['private_union_lower_bound']-4*max(0,g['private_edges']-6)) for g in gs)
   profile=tuple(sorted((g['private_edges'],g['private_union_lower_bound'],g['nine']) for g in gs))
   case=dict(input_id=iid,blue=list(blue),groups=gs,signature=list(sig),
             nine_selected=row['nine'] in blue,certified_union_for_at_most6=sub6,source_categories=colors)
   matches.append(case);allcases.append(case);caseprofiles[str(profile)]+=1
   if len(blue)==2:two_profiles[str(profile)]+=1
   groupsizes[len(gs)]+=1
  assert signatures==menus[row['menu_id']],('member menu mismatch',iid)
  if not matches:totals['without_nine_interface']+=1;continue
  totals['with_nine_interface']+=1
  two=[c for c in matches if len(c['blue'])==2]
  totals['has_two_blue']+=bool(two);totals['requires_three_blue']+=not bool(two)
  totals['has_nine_not_selected']+=any(not c['nine_selected'] for c in matches)
  totals['has_nine_selected']+=any(c['nine_selected'] for c in matches)
  haslarge=any(any(g['private_edges']>=6 and g['private_union_lower_bound']>=16 for g in c['groups']) for c in matches)
  totals['has_one_star_at_least6_union16']+=haslarge
  bestunion=max(c['signature'][8] for c in matches)
  bestsub=max(c['certified_union_for_at_most6'] for c in matches)
  bounds[f'best_total_union={bestunion};best_6sub_union={bestsub}']+=1
  totals['has_certified_6sub_union16']+=bestsub>=16
  best=min(matches,key=lambda c:(-c['certified_union_for_at_most6'],-c['signature'][8],len(c['blue']),c['blue']))
  bybest[str(tuple(sorted((g['private_edges'],g['private_union_lower_bound'],g['nine']) for g in best['groups'])))]+=1
  out=dict(input_id=iid,P_key=row,all_nine_choices=len(matches),two_blue_choices=len(two),
           best_union=bestunion,best_6sub_union=bestsub,best_choice=best)
  inputs.append(out)
  for label,condition in [('no_two_blue',not two),('no_large_star',not haslarge),('no_6sub16',bestsub<16),
                          ('lowest_total_union',bestunion<16),('nine_forced',all(c['nine_selected'] for c in matches))]:
   if condition and label not in examples:examples[label]=out
 totals['all_nine_choices']=len(allcases)
 result=dict(complete=True,scope=__doc__,input_rows=len(rows),totals=dict(totals),
             all_choice_group_count_histogram=dict(groupsizes),all_choice_profiles=dict(caseprofiles),
             two_blue_profiles=dict(two_profiles),best_choice_profiles=dict(bybest),
             per_input_best_union_histogram=dict(bounds),examples=examples,
             all_member_menus_independently_reconstructed=True,process_seconds=time.process_time()-start)
 (HERE/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
 with (HERE/'ALL_NINE_CHOICES.jsonl').open('w') as f:
  for c in allcases:f.write(json.dumps(c,separators=(',',':'))+'\n')
 with (HERE/'INPUT_GEOMETRY.jsonl').open('w') as f:
  for c in inputs:f.write(json.dumps(c,separators=(',',':'))+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('all_choice_profiles','two_blue_profiles','best_choice_profiles','examples')},indent=2))
 assert totals['with_nine_interface']==8020

if __name__=='__main__':main()

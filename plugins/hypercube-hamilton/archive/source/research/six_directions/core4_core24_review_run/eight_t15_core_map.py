"""Map the actual a2b1 compressed hole configurations to T15 orbit cores."""
import collections,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
 source=json.loads((ROOT/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits']
 transforms=[[sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)] for p in itertools.permutations(range(5))]
 lookup={}
 for i,row in enumerate(source):
  for tr in transforms:
   key=(tuple(sorted(tr[x] for x in row['avoided'])),tuple(sorted(tr[x] for x in row['included'])))
   assert key not in lookup or lookup[key]==i;lookup[key]=i
 targets=[];frequency=collections.Counter();no21=[]
 for v in (1,7,31):
  raw=(ROOT/f'covered_eight_residual_{v}.bin').read_bytes()
  for off in range(0,len(raw),7):
   Z=list(raw[off:off+3]);W=list(raw[off+3:off+7]);choices=set();witnesses=[]
   for i in range(6):
    za=[x for x in Z if (x>>i&1)==(v>>i&1)];wa=[x for x in W if (x>>i&1)==(v>>i&1)]
    if len(za)!=2 or len(wa)!=1:continue
    q=next(x for x in Z if x not in za)
    def project(x):
     x^=q
     return (x&((1<<i)-1))|((x>>(i+1))<<i)
    key=(tuple(sorted(project(x^(1<<i)) for x in za)),tuple(sorted(project(x) for x in W if x not in wa)))
    assert key in lookup,(v,Z,W,i,key)
    core=lookup[key];choices.add(core);witnesses.append({'cut':i,'core':core})
   row={'target':v,'Z':Z,'W':W,'core_choices':sorted(choices),'cut_witnesses':witnesses}
   if choices:
    targets.append(row)
    for i in choices:frequency[i]+=1
   else:no21.append(row)
 uncovered=set(range(len(targets)));selection=[]
 while uncovered:
  counts=collections.Counter(i for t in uncovered for i in targets[t]['core_choices'])
  i,n=max(counts.items(),key=lambda p:(p[1],-p[0]));selection.append({'core':i,'newly_covered_geometries':n})
  uncovered={t for t in uncovered if i not in targets[t]['core_choices']}
 used=[{'core':i,**source[i],'parent_geometries':frequency[i]} for i in sorted(frequency)]
 result={'scope':'Exact normalized geometry map, not a proof of any T15 core or Q6 path',
 'total_R8_geometries':len(targets)+len(no21),'with_a2b1':len(targets),'without_a2b1':len(no21),
 'distinct_T15_core_orbits':len(used),'used_cores':used,'greedy_sufficient_core_cover':selection,
 'greedy_cover_size':len(selection),'greedy_cover_optimality_claimed':False,
 'without_a2b1_by_target':dict(collections.Counter(r['target'] for r in no21)),
 'without_a2b1_geometries':no21,'targets':targets,'full_eight_hole_proved':False,'full_p6_proved':False}
 (ROOT/'eight_t15_core_map.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:result[k] for k in ('total_R8_geometries','with_a2b1','without_a2b1','distinct_T15_core_orbits','greedy_cover_size','greedy_sufficient_core_cover','without_a2b1_by_target')}))
if __name__=='__main__':main()

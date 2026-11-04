"""Independent projection, orbit, geometry-test and greedy-cover verifier."""
import collections,itertools,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=list(itertools.permutations(range(5)))
MAP=[tuple(sum(((x>>p[j])&1)<<j for j in range(5)) for x in range(32)) for p in P]
CACHE={}
def canonical(Y,I):
 key=(tuple(sorted(Y)),tuple(sorted(I)))
 if key not in CACHE:
  CACHE[key]=min((tuple(sorted(tr[x] for x in Y)),tuple(sorted(tr[x] for x in I))) for tr in MAP)
 return CACHE[key]

def tests(Y,I):
 H={0,*Y,*I};splits=[];same=[]
 for j in range(5):
  side={x for x in H if ((x>>j)&1)==((Y[0]>>j)&1)}
  if ((Y[0]^Y[1])>>j)&1:
   if sum(x.bit_count()%2 for x in side)-int(0 in side)==2:splits.append(j)
  elif 0 not in side and len(side)==4:same.append(j)
 J=sorted(set(splits+same))
 cells=collections.Counter(tuple((x>>j)&1 for j in J) for x in range(32) if x not in H)
 oddcells=any(n%2 for n in cells.values()) if J else False
 return splits,same,oddcells

def rowkey(row):return (row['target'],tuple(row['Z']),tuple(row['W']))

def main():
 analytic=json.loads((ROOT/'t15_analytic_geometry.json').read_text())['T15']
 source=analytic['residual_orbits'];assert len(source)==54
 sourcekeys=[]
 for row in source:
  key=canonical(row['avoided'],row['included']);assert key==(tuple(row['avoided']),tuple(row['included']))
  sourcekeys.append(key)
 assert len(set(sourcekeys))==54
 ids={key:i for i,key in enumerate(sourcekeys)}
 odd=[x for x in range(32) if x.bit_count()%2]
 residual=collections.Counter();total=0
 for I in itertools.combinations([x for x in odd if x.bit_count()>1],3):
  for Y in itertools.combinations([x for x in odd if x not in I],2):
   total+=1;s,sa,c=tests(Y,I)
   if not s and not sa:residual[canonical(Y,I)]+=1
 assert total==analytic['normalized_configurations']
 assert residual==collections.Counter({key:source[i]['count'] for i,key in enumerate(sourcekeys)})
 author=json.loads((ROOT/'eight_t15_core_map.json').read_text())
 coverage=json.loads((ROOT/'eight_t15_geometric_coverage.json').read_text())
 expected={rowkey(row):row for row in author['targets']}
 no21={rowkey(row):row for row in author['without_a2b1_geometries']}
 assert len(expected)==len(author['targets']) and len(no21)==len(author['without_a2b1_geometries'])
 rawkeys=set();freq=collections.Counter();summaries=[];choices=[];cuts=0;geometry_tests=0
 no_good=0
 for v in (1,7,31):
  raw=(ROOT/f'covered_eight_residual_{v}.bin').read_bytes();assert len(raw)%7==0
  have=without=closed=0
  for offset in range(0,len(raw),7):
   Z=tuple(raw[offset:offset+3]);W=tuple(raw[offset+3:offset+7]);k=(v,Z,W)
   assert k not in rawkeys;rawkeys.add(k)
   H={0,*Z,*W}
   assert len(H)==8 and v not in H
   assert all(x.bit_count()%2==0 and x!=0 for x in Z) and all(x.bit_count()%2 for x in W)
   assert all((z^w).bit_count()!=1 for z in Z for w in W)
   witnesses=[];ch=set();localclose=False
   for i in range(6):
    face=lambda x:((x>>i)&1)==((v>>i)&1)
    za=[z for z in Z if face(z)];wa=[w for w in W if face(w)]
    if len(za)!=2 or len(wa)!=1:continue
    cuts+=1
    q=next(z for z in Z if not face(z));Y=[z^(1<<i) for z in za];I=[w for w in W if not face(w)]
    assert len(set((q,*Y,*I)))==6 and len(I)==3
    assert all(not face(x) for x in (q,*Y,*I))
    assert q.bit_count()%2==0 and all(x.bit_count()%2 for x in (*Y,*I))
    # Use coordinate lists, rather than author's shift-mask projection formula.
    coords=[j for j in range(6) if j!=i]
    def project(x):return sum((((x>>j)&1)^((q>>j)&1))<<k for k,j in enumerate(coords))
    assert project(q)==0
    Yp=tuple(sorted(map(project,Y)));Ip=tuple(sorted(map(project,I)))
    assert all(x.bit_count()%2 for x in (*Yp,*Ip))
    assert all(x.bit_count()>1 for x in Ip)
    split,same,cell=tests(Yp,Ip);geometry_tests+=1
    localclose|=bool(split or cell)
    assert not split and not same # every actual image has NO direct good cut
    no_good+=1
    key=canonical(Yp,Ip);assert key in ids
    core=ids[key];ch.add(core);witnesses.append({'cut':i,'core':core})
   if ch:
    have+=1;assert k in expected and k not in no21
    assert expected[k]['core_choices']==sorted(ch) and expected[k]['cut_witnesses']==witnesses
    choices.append(ch);freq.update(ch)
   else:
    without+=1;assert k in no21 and k not in expected
    assert not no21[k]['core_choices'] and not no21[k]['cut_witnesses']
   if localclose:closed+=1
  summaries.append({'target':v,'total':len(raw)//7,'with_a2b1':have,'without_a2b1':without,'closed_by_split_or_cell':closed})
 assert rawkeys==set(expected)|set(no21)
 assert set(expected).isdisjoint(no21)
 assert not coverage['closed'] and coverage['closed_count']==0
 assert coverage['remaining_count']==len(rawkeys)==66127
 assert len(coverage['remaining'])==len(rawkeys) and {rowkey(r) for r in coverage['remaining']}==rawkeys
 for own,stored in zip(summaries,coverage['summary']):
  assert stored=={'target':own['target'],'total':own['total'],'remaining_with_a2b1':own['with_a2b1'],'remaining_without_a2b1':own['without_a2b1']}
 actualused={r['core']:r for r in author['used_cores']}
 assert set(actualused)==set(freq) and len(freq)==41
 for core,n in freq.items():
  assert actualused[core]=={'core':core,**source[core],'parent_geometries':n}
 uncovered=set(range(len(choices)));greedy=[]
 while uncovered:
  gains={i:sum(i in choices[t] for t in uncovered) for i in freq}
  core=min(gains,key=lambda i:(-gains[i],i));gain=gains[core]
  assert gain>0
  greedy.append({'core':core,'newly_covered_geometries':gain})
  uncovered.difference_update(t for t in list(uncovered) if core in choices[t])
 assert greedy==author['greedy_sufficient_core_cover'] and len(greedy)==23
 assert sum(x['newly_covered_geometries'] for x in greedy)==len(expected)==65920
 assert (author['total_R8_geometries'],author['with_a2b1'],author['without_a2b1'],author['distinct_T15_core_orbits'],author['greedy_cover_size'])==(66127,65920,207,41,23)
 assert not author['greedy_cover_optimality_claimed']
 assert author['without_a2b1_by_target']=={str(r['target']):r['without_a2b1'] for r in summaries}
 filenames=['eight_t15_geometric_coverage.py','eight_t15_geometric_coverage.json','eight_t15_core_map.py','eight_t15_core_map.json','t15_analytic_geometry.py','t15_analytic_geometry.json',*[f'covered_eight_residual_{v}.bin' for v in (1,7,31)]]
 result={'status':'PASS','summaries':summaries,'total':len(rawkeys),'with_a2b1':len(expected),'without_a2b1':len(no21),'a2b1_cuts_checked':cuts,'projected_T15_criterion_checks':geometry_tests,'all_projected_geometries_without_any_direct_good_cut':no_good==cuts,'closed_by_split_or_cell':0,'normalized_T15_domain_enumerated':total,'residual_T15_orbits':len(residual),'used_T15_orbits':len(freq),'greedy_cover_size':len(greedy),'greedy_cover':greedy,'optimality_claimed':False,'source_hashes':{n:'sha256:'+hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in filenames},'matching_realizability_checked':False,'any_new_T15_core_proved':False,'R8_covered_proved':False,'full_P6_proved':False}
 (ROOT/'EIGHT_T15_CORE_MAP_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','greedy_cover')}))

if __name__=='__main__':main()

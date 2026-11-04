"""Exact hole-geometry coverage by a2b1 -> proved T15 split/cell criteria.

Does not enumerate realizing matchings or prove residual cases.
"""
import collections,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def pc(x):return x.bit_count()
def t15_check(minority,odd,avoid,coords,side_vertices):
 split=[];same=[]
 for j in coords:
  # The face containing avoid[0] is the first face.
  a=[x for x in [minority,*odd] if (x>>j&1)==(avoid[0]>>j&1)]
  hE=int(minority in a);hO=sum(x in a for x in odd)
  if (avoid[1]>>j&1)!=(avoid[0]>>j&1) and hO-hE==2:split.append(j)
  if (avoid[1]>>j&1)==(avoid[0]>>j&1) and hE==0 and hO==4:same.append(j)
 if split:return {'reason':'split','inner_cut':split[0]}
 good=split+same
 if not good:return None
 covered=set(side_vertices)-{minority,*odd}
 cells=collections.Counter(tuple(x>>j&1 for j in good) for x in covered)
 odd_cells=[list(k) for k,v in cells.items() if v%2]
 if odd_cells:return {'reason':'cell_parity','cuts':good,'odd_cells':odd_cells}
 return None
def main():
 summary=[];closed=[];remaining=[]
 for v in (1,7,31):
  data=(ROOT/f'covered_eight_residual_{v}.bin').read_bytes();assert len(data)%7==0
  counts=collections.Counter()
  for off in range(0,len(data),7):
   Z=list(data[off:off+3]);W=list(data[off+3:off+7]);found=None;has21=False
   for i in range(6):
    za=[z for z in Z if (z>>i&1)==(v>>i&1)];wa=[w for w in W if (w>>i&1)==(v>>i&1)]
    if len(za)!=2 or len(wa)!=1:continue
    has21=True;q=next(z for z in Z if z not in za);Y=[z^(1<<i) for z in za]
    localodd=[w for w in W if w not in wa]+Y
    assert len(set(localodd))==5 and all(pc(w)%2 for w in localodd)
    B=[x for x in range(64) if (x>>i&1)!=(v>>i&1)]
    result=t15_check(q,localodd,Y,[j for j in range(6) if j!=i],B)
    if result is not None:found={'outer_cut':i,'minority':q,'odd_holes':localodd,'avoided':Y,**result};break
   row={'target':v,'Z':Z,'W':W}
   if found is not None:counts[found['reason']]+=1;closed.append(dict(row,certificate=found))
   else:counts['remaining_with_a2b1' if has21 else 'remaining_without_a2b1']+=1;remaining.append(row)
  summary.append({'target':v,'total':len(data)//7,**counts})
 result={'scope':'R8-covered geometry accounting via a2b1/T15 split; semantic acceptance requires cited audits',
 'summary':summary,'closed_count':len(closed),'remaining_count':len(remaining),'closed':closed,'remaining':remaining,
 'full_eight_hole_proved':False,'full_p6_proved':False}
 (ROOT/'eight_t15_geometric_coverage.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('closed','remaining')}))
if __name__=='__main__':main()

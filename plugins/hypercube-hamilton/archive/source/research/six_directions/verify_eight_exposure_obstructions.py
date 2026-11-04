"""Verify explicit matchings and no-exposure Hall obstructions without a solver."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def pc(x):return x.bit_count()
def crossing_odd_port(edge,v,i):
 a,b=edge
 if (a>>i&1)==(b>>i&1):return None
 q=a if (a>>i&1)==(v>>i&1) else b
 return q if pc(q)%2 else None
def main():
 src=ROOT/'eight_hole_covered_next_probe.json';data=json.loads(src.read_text(encoding='utf-8-sig'))
 n=0
 for row in data['results']:
  assert row['no_exposure_matching_found'];v=row['target'];i=row['cut'];M=row['matching']
  H={0,*row['Z'],*row['W']};covered={x for e in M for x in e}
  assert len(M)==28 and len(covered)==56 and covered==set(range(64))-H
  assert v in covered and all(pc(a^b)==1 for a,b in M)
  assert sum((x>>i&1)==(v>>i&1) for x in row['Z'])==2
  assert all((x>>i&1)!=(v>>i&1) for x in row['W'])
  S={w^(1<<i) for w in row['W']}
  ports={q for e in M if (q:=crossing_odd_port(e,v,i)) is not None}
  assert ports==set(row['odd_ports']) and S==set(row['mirror_holes'])
  assert not any(pc(q^s)==1 for q in ports for s in S)
  n+=1
 hall=[]
 for row in data['joint_results']:
  v=row['target'];H={0,*row['Z'],*row['W']};V=set(range(64))-H
  E=[]
  for a in V:
   if pc(a)%2:continue
   for j in range(6):
    b=a^(1<<j)
    if b not in V:continue
    legal=True
    for i in row['cuts']:
     q=crossing_odd_port((a,b),v,i)
     if q is not None and any(pc(q^(w^(1<<i)))==1 for w in row['W']):legal=False
    if legal:E.append((a,b))
  U=set(row['hall_even_subset']);assert U<=V and all(pc(u)%2==0 for u in U)
  N={b for a,b in E if a in U}
  assert N==set(row['hall_odd_neighbours']) and len(U)-len(N)==row['hall_deficiency']>0
  hall.append({'target':v,'Z':row['Z'],'W':row['W'],'hall_deficiency':len(U)-len(N)})
 assert n==21 and len(hall)==7
 result={'status':'PASS','individual_cut_counterexamples':n,'simultaneous_no_exposure_impossible_orbits':7,'hall_certificates':hall,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'scope':'Exposure adjacency only; no prescribed-edge Hamilton-path claim','full_eight_hole_proved':False,'full_p6_proved':False}
 (ROOT/'eight_exposure_obstructions_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:result[k] for k in ('status','individual_cut_counterexamples','simultaneous_no_exposure_impossible_orbits')}))
if __name__=='__main__':main()

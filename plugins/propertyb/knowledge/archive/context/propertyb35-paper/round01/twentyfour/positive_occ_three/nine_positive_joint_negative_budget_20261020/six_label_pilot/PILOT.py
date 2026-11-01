"""Bounded six-label graph gate diagnostic, not negative-layout or H search."""
from itertools import combinations,permutations,product
from collections import Counter
from pathlib import Path
from math import comb
import json,time,argparse
HERE=Path(__file__).resolve().parent
EDGES=tuple(combinations(range(6),2));IDX={e:k for k,e in enumerate(EDGES)}
PERM_MAPS=tuple(tuple(IDX[tuple(sorted((p[a],p[b])))] for a,b in EDGES) for p in permutations(range(6)))
def matching_partitions(v):
 if not v:return [()]
 a=v[0];out=[]
 for b in v[1:]:
  for rest in matching_partitions(tuple(x for x in v[1:] if x!=b)):out.append((IDX[tuple(sorted((a,b)))],)+rest)
 return out
MATCH=matching_partitions(tuple(range(6)))
assert len(MATCH)==15

def m3(g):return sum(g[a]*g[b]*g[c] for a,b,c in MATCH)
def orbit(g):
 out=set()
 for mp in PERM_MAPS:
  h=[0]*15
  for k,v in enumerate(g):h[mp[k]]=v
  out.add(tuple(h))
 return out
PARAMS=tuple((u,t,v,20-t) for u in range(4) for t in range(u,4) for v in range(5-u))
assert len(PARAMS)==40

def analyse(g):
 deg=[sum(v for e,v in zip(EDGES,g) if a in e) for a in range(6)]
 masks=[]
 for (a,b),v in zip(EDGES,g):masks += [(1<<a)|(1<<b)]*v
 for a in range(6):masks += [1<<a]*(4-deg[a])
 n=len(masks);assert n==24-sum(g)<=17
 sets=[tuple(i for i,m in enumerate(masks) if m>>a&1) for a in range(6)]
 assert all(len(a)==4 for a in sets)
 def hits(c):
  u=0
  for i in c:u|=masks[i]
  return u==63
 cand3=[c for c in combinations(range(n),3) if hits(c)]
 cand4=[c for c in combinations(range(n),4) if hits(c)]
 assert len(cand3)==m3(g)
 IE=[]
 for k in (3,4):
  ans=0
  for S in range(64):
   left=sum(not(m&S) for m in masks)
   ans+=(-1)**S.bit_count()*(comb(left,k) if left>=k else 0)
  IE.append(ans)
 assert IE==[len(cand3),len(cand4)]
 pair3=Counter(q for c in cand3 for q in combinations(c,2))
 pair4=Counter(q for c in cand4 for q in combinations(c,2))
 triple4=Counter(q for c in cand4 for q in combinations(c,3))
 top3=sorted(pair3.values(),reverse=True)+[0]*3
 top4=sorted(pair4.values(),reverse=True)+[0]*3
 S3=[sum(top3[:u]) for u in range(4)];S4=[sum(top4[:u]) for u in range(4)]
 h3=max(triple4.values(),default=0)
 rows=[];failed=[]
 for u,t,v,b in PARAMS:
  bound3=S3[u]+t-u+v
  bound4=S4[u]+(t-u+v)*h3+(b-v)
  row={'u':u,'t':t,'v':v,'b':b,'C3_blocker':bound3,'C4_blocker':bound4,
       'C3_margin':len(cand3)-bound3,'C4_margin':len(cand4)-bound4}
  rows.append(row)
  if len(cand3)<=bound3 and len(cand4)<=bound4:failed.append(row)
 return {'vector':g,'E':sum(g),'degrees':deg,'M3':m3(g),'union_size':n,'sets':sets,
         'C3':len(cand3),'C4':len(cand4),'C3_IE':IE[0],'C4_IE':IE[1],
         'C3_pair_top_counts':top3[:3],'C4_pair_top_counts':top4[:3],
         'C3_pair_prefix_sums':S3,'C4_pair_prefix_sums':S4,'C4_max_triple_extension':h3,
         'maximal_b_parameter_rows':rows,'nongated_maximal_b_rows':failed}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cpu-limit',type=float,default=10);ap.add_argument('--prefix',default='PROFILE');args=ap.parse_args()
 start=time.process_time();g=[0]*15;incoming=[0]*6;seen=set();rows=[];failure=None;stop=None;labelled=0;rawleaves=0
 def rec(a):
  nonlocal failure,stop,labelled,rawleaves
  if failure is not None or stop is not None:return
  if a==5:
   rawleaves+=1;e=sum(g)
   if not(7<=e<=12) or m3(g)>13:return
   labelled+=1;key=tuple(g)
   if key in seen:return
   orb=orbit(key);seen.update(orb)
   row=analyse(key);row['orbit_size']=len(orb);rows.append(row)
   if row['nongated_maximal_b_rows']:failure=row;return
   if time.process_time()-start>args.cpu_limit:stop={'last_vector':key,'completed_representatives':len(rows)}
   return
  js=tuple(range(a+1,6))
  for vals in product(*(range(min(4-incoming[a],4-incoming[b])+1) for b in js)):
   if sum(vals)+incoming[a]>4 or sum(g)+sum(vals)>12:continue
   for b,v in zip(js,vals):g[IDX[a,b]]=v;incoming[b]+=v
   # Completed partial matching products never decrease.
   if m3(g)<=13:rec(a+1)
   for b,v in zip(js,vals):g[IDX[a,b]]=0;incoming[b]-=v
   if failure is not None or stop is not None:return
 rec(0)
 out={'status':'FIRST_NONGATED_GRAPH' if failure else 'CPU_PREFIX' if stop else 'COMPLETE_STRICT',
      'scope':__doc__,'domain':'six labels, nonnegative unordered edge multiplicities, maxdegree4, 7<=E<=12, M3<=13; S6 transport',
      'edge_order':EDGES,'perfect_matchings':MATCH,'cpu_seconds':time.process_time()-start,
      'labelled_eligible_scanned':labelled,'raw_leaves_scanned':rawleaves,'representatives_checked':len(rows),
      'labelled_graphs_in_processed_orbits':len(seen),'rows':rows,'first_nongated':failure,'stop':stop,
      'parameter_reduction':'Only b=20-t checked: both bounds nondecreasing in b, and v<=4-u<=4<=20-t. Strict for these 40 rows implies every legal b.',
      'no_negative_layout_enumeration':True}
 (HERE/(args.prefix+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('rows','first_nongated')},indent=2))
 if failure:print('FAILURE',json.dumps(failure,indent=2))
if __name__=='__main__':main()

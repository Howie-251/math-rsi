"""Exactly four 1-inverse-pair-per-fiber prunings of each of two saved lifts."""
from pathlib import Path
from collections import Counter,deque
from itertools import product
import subprocess,json
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
cases=[('D7_Meta_13_27_3',13,27,3),('D7_Meta_15_24_2',15,24,2)]
results=[]
for name,m,k,r in cases:
 q=m*k;n=2*q
 source=ROOT/'computations/ddp/m1/d7_profile'/name
 spec=json.loads(source.with_suffix('.json').read_text())
 def mul(x,y):
  a,b=divmod(x,k);c,d=divmod(y,k)
  return ((a+pow(r,b,m)*c)%m)*k+(b+d)%k
 def inv(x):
  a,b=divmod(x,k);return ((-pow(r,(-b)%k,m)*a)%m)*k+(-b)%k
 def pairs(xs):
  out=sorted({tuple(sorted((x,inv(x)))) for x in xs})
  assert len(out)==2 and all(len(set(p))==2 and set(p)<=set(xs) for p in out)
  return out
 pa,pb=pairs(spec['A']),pairs(spec['B']);S=spec['S']
 def expand(A,B):
  E=set()
  for g in range(q):
   for x in A:E.add(tuple(sorted((g,mul(g,x)))))
   for x in B:E.add(tuple(sorted((q+g,q+mul(g,x)))))
   for x in S:E.add((g,q+mul(g,x)))
  return E
 original_lines=source.with_suffix('.edges').read_text().splitlines()
 assert tuple(map(int,original_lines[0].split()))==(n,7*n//2)
 original={tuple(map(int,l.split())) for l in original_lines[1:]}
 assert expand(spec['A'],spec['B'])==original
 for ia,ib in product(range(2),repeat=2):
  A,B=pa[ia],pb[ib];E=expand(A,B)
  assert E<=original and len(E)==5*n//2
  adj=[[] for _ in range(n)]
  for u,v in E:assert u<v;adj[u].append(v);adj[v].append(u)
  assert {len(x) for x in adj}=={5}
  reps=[]
  for root in [0,q]:
   d=[-1]*n;d[root]=0;todo=deque([root])
   while todo:
    u=todo.popleft()
    for v in adj[u]:
     if d[v]==-1:d[v]=d[u]+1;todo.append(v)
   reps.append({'root':root,'eccentricity':max(d) if min(d)>=0 else -1,'missing_gt5':sum(x<0 or x>5 for x in d),'distance_histogram':dict(sorted(Counter(d).items()))})
  label=f'n{n}_a{ia}_b{ib}';edgefile=OUT/(label+'.edges')
  edgefile.write_text(f'{n} {len(E)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(E)))
  completed=subprocess.run([str(ROOT/'computations/ddp/verify_graph'),str(edgefile),'5','5'],capture_output=True,text=True)
  assert completed.returncode in [0,1],completed.stderr
  check=json.loads(completed.stdout)
  assert check['roots_checked']==n and check['max_degree']==5 and check['min_degree']==5
  implied_bad=q*sum(x['missing_gt5'] for x in reps)//2
  assert check['bad_unordered_pairs']==implied_bad
  total=Counter()
  for rep in reps:
   for d,count in rep['distance_histogram'].items():total[int(d)]+=q*count
  assert dict(total)=={int(d):count for d,count in check['ordered_distance_histogram'].items()}
  rec={'source_group':name,'source_parameters':str(source.with_suffix('.json').relative_to(ROOT)),'source_reconstruction_matches_entire_edge_list':True,'group_parameters':{'m':m,'k':k,'r':r},'multiplication':'(a,b)*(c,d)=(a+r^b*c mod m,b+d mod k)','vertex_label':'type*m*k + a*k+b','A':list(A),'B':list(B),'S':S,'order':n,'degree':5,'target_diameter':5,'subset_of_saved_parent_edges':True,'representative_BFS':reps,'independent_all_source_BFS':check,'independent_checker_exit_code':completed.returncode}
  (OUT/(label+'.json')).write_text(json.dumps(rec,indent=2)+'\n');results.append(rec)
  print(label,'diameter',check['diameter'],'bad_unordered',check['bad_unordered_pairs'],'root_missing',[x['missing_gt5'] for x in reps],'valid',check['valid'],flush=True)
(OUT/'results.json').write_text(json.dumps(results,indent=2)+'\n')

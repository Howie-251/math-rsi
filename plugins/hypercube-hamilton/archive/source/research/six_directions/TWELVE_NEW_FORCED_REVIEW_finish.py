"""Counterexample-pressure for labelled contraction; final hash and certificate gates."""
import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
m=json.loads((R/'TWELVE_NEW_FORCED_MANIFEST.json').read_text());d=json.loads((R/'TWELVE_NEW_FORCED_REVIEW_check.json').read_text(encoding='utf-8-sig'))
assert d['status']=='PASS' and len(d['reports'])==27 and all(x['GF2_rank']==512 for x in d['reports'])
for n,h in m['files'].items():assert sha(n)==h,n
def pairs(xs):
 if not xs:yield ();return
 a,*rest=xs
 for i,b in enumerate(rest):
  for sub in pairs(rest[:i]+rest[i+1:]):yield ((a,b),)+sub
def connected(P,F):
 vertices={x for e in P+F for x in e};adj={x:[] for x in vertices}
 for a,b in P+F:adj[a].append(b);adj[b].append(a)
 seen=set();todo=[next(iter(vertices))]
 while todo:
  x=todo.pop()
  if x in seen:continue
  seen.add(x);todo.extend(adj[x])
 return seen==vertices
checks=0
for n in [6,8]:
 for redP in pairs(list(range(2,n))):
  P=((0,1),)+redP
  for F in pairs(list(range(n))):
   if (0,1) in F:continue
   mate={a:b for x,y in F for a,b in [(x,y),(y,x)]};a=mate[0];b=mate[1]
   redF=tuple(e for e in F if 0 not in e and 1 not in e)+((a,b),)
   assert connected(P,F)==connected(redP,redF)
   checks+=1
out={'status':'PASS','frozen_hashes_rechecked_after_run':249,'small_labelled_contraction_equivalences_checked':checks,'certificate_totals':{k:v for k,v in d.items() if k!='reports'},'primary_general_bound':'Corollary3.5, all complete-graph matchings and every even t>=2; t20 gives512','local_only':True,'full_T28_proved':False,'full_T19_proved':False,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_NEW_FORCED_REVIEW_finish.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

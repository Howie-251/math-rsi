"""Finite completion accounting for the two residual T44_5 geometries.

Uses the full Q4 avoided-vertex negative tables. A proof of the occupied
endpoint transfer and an independent audit are required for global closure.
"""
import itertools,json,math
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def main():
 sources={k:json.loads((ROOT/f'q4_distance{k}_avoided_table_verification.json').read_text()) for k in (1,3)}
 odd=[x for x in range(16) if x.bit_count()%2];bad={}
 for y in odd:
  p=[i for i in range(4) if y>>i&1]+[i for i in range(4) if not y>>i&1]
  def tr(x):return sum(((x>>i)&1)<<p[i] for i in range(4))
  values=set()
  for row in sources[y.bit_count()]['exceptions']:
   F=frozenset(edge(tr(a),tr(b)) for a,b in row['matching'])
   for a,b in F:
    for d,k in ((a,b),(b,a)):
     L=frozenset(F-{edge(d,k)}|{edge(y,k)})
     values.add((d,L))
  bad[y]=values
 results=[]
 for targets in ((7,11),(2,14)):
  candidates=bad[targets[0]]|bad[targets[1]]
  failures={(d,F) for d,F in candidates if all(d==y or (d,F) in bad[y] for y in targets)}
  levels=[]
  for c in (1,3,5,7,9,11,13):
   m=(15-c)//2;totalroot=math.prod(range(1,c-1,2));total=c*totalroot
   counts=Counter(tuple(sorted(sub)) for d,F in failures for sub in itertools.combinations(sorted(F),m))
   stalls=[frozenset(f) for f,k in counts.items() if k==total]
   items=[];unresolved=[]
   for f in stalls:
    ports=sorted(set(range(1,16))-{x for e in f for x in e});assert len(ports)==c
    goodroots={};badcounts={}
    for y in odd:
     countsroot=Counter(d for d,L in bad[y] if f<=L)
     assert all(countsroot[d]<=totalroot for d in ports)
     goodroots[y]=[d for d in ports if d!=y and countsroot[d]<totalroot]
     badcounts[y]={d:totalroot if d==y else countsroot[d] for d in ports}
    G=[y for y in odd if y!=1 and goodroots[y]]
    badroots={y:[d for d in ports if d not in goodroots[y]] for y in G}
    def bad_injection(todo,used):
     if not todo:return {}
     y=todo[0]
     for d in badroots[y]:
      if d not in used:
       rest=bad_injection(todo[1:],used|{d})
       if rest is not None:return {y:d,**rest}
     return None
    injection=None if len(G)>c else bad_injection(sorted(G,key=lambda y:len(badroots[y])),set())
    guaranteed=len(G)>c or (c>=3 and injection is None)
    item={'matching':sorted(f),'ports':ports,'good_endpoints_excluding_forbidden':G,'good_roots':goodroots,'bad_counts':badcounts,'guaranteed_safe_or_occupied':guaranteed,'bad_injection':injection}
    items.append(item)
    if not guaranteed:unresolved.append(item)
   levels.append({'crossings':c,'all_fixed_target_failure_partials':len(stalls),'unresolved':len(unresolved),'items':items})
  results.append({'free_targets':targets,'other_forbidden':1,'near_perfect_failures':len(failures),'levels':levels})
 out={'scope':'canonical local completion/root availability; occupied gluing proof and independent audit pending','results':results,'T44_5_proved':False,'full_p6_proved':False}
 (ROOT/'t44_canonical_completion_probe.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps([{'free_targets':r['free_targets'],'near_perfect_failures':r['near_perfect_failures'],'levels':[{k:l[k] for k in ('crossings','all_fixed_target_failure_partials','unresolved')} for l in r['levels']]} for r in results]))
if __name__=='__main__':main()

"""Literal graph test of a necessary critical-core constraint; not an H search."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
src=P.parent/'a1_rank_component_wedge_budget_20261020/VERIFY.json'
j=json.loads(src.read_text());edges={tuple(e) for e in j['graph_edges']};assert len(edges)==76
N=35
def deg(E):
 d=[0]*N
 for a,b in E:assert 0<=a<b<N;d[a]+=1;d[b]+=1
 return d
def f(s):
 a,b=divmod(s,5);return (s*s-(5-b)*a*a-b*(a+1)**2)//2
def Pval(E):return sum(f(34-q) for q in deg(E))
d0=deg(edges);assert Pval(edges)==13074
u,v=[i for i,d in enumerate(d0) if d==34];w=next(i for i,d in enumerate(d0) if d==11)
leaf=[i for i,d in enumerate(d0) if d==2 and tuple(sorted((w,i))) not in edges]
assert len(leaf)==23
moves=[]
for z in leaf[:5]:
 old=tuple(sorted((u,z)));new=tuple(sorted((w,z)))
 assert old in edges and new not in edges
 edges.remove(old);edges.add(new);moves.append({'remove':old,'add':new})
d=deg(edges);assert len(edges)==76 and d[u]==29 and d[v]==34 and d[w]==16
assert Counter(d)==Counter({34:1,29:1,16:1,3:9,2:23})
assert sum(q>29 for q in d)==1
sing=[34-q for q in d];assert Counter(sing)==Counter({0:1,5:1,18:1,31:9,32:23})
core=[z for z in range(N) if z!=v]
# Stronger form: there is an induced34-vertex singleton graph of min degree>=5.
induced_sing={i:sum(tuple(sorted((i,k))) not in edges for k in core if k!=i) for i in core}
assert min(induced_sing.values())==5
assert Pval(edges)==13002
assert f(23)==211 and f(18)==129 and f(5)==10
assert 13074-13002==f(23)-f(18)-f(5)==72
# Saved actual-H moment relaxation: only the joint P budget is reduced.
n=[34,519,5,29,8];tau=0;budget=Fraction(13002)
cap=[33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4]];C=[Fraction(0)]*5
for k in range(4,-1,-1):C[k]=min(budget,cap[k]);budget-=C[k]
L=sum(a*b for a,b in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
assert C==[0,12473,120,377,32] and L==2726136 and L-2722720==3416
out={'status':'PASS_RELAXATION_WITNESS_ONLY','scope':'explicit76-edge graph, not a5-uniform H or a Gram realization; necessary critical-core test only','source':str(src),'N':N,'e':len(edges),'u':u,'v_exception':v,'w':w,'moves':moves,'graph_edges':sorted(edges),'Gamma_degree_histogram':dict(Counter(d)),'singleton_degree_histogram':dict(Counter(sing)),'singleton_induced_core':core,'induced_core_min_degree':min(induced_sing.values()),'P':Pval(edges),'P_drop':72,'moment_profile':n,'tau':tau,'C':[str(x) for x in C],'L':str(L),'threshold':2722720,'surviving_margin':3416,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('graph_edges','singleton_induced_core','moves')})

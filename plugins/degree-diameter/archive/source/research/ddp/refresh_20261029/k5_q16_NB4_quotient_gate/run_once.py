"""One complete K5/Q16->V4 necessary gate, no controller or field graph search."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json
import resource
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(9,10))
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
assert not (HERE/'RESULT.json').exists(),'Single complete gate already recorded.'
source=ROOT/'research/ddp/breadth_20261027_wave5/chart4_quotient_probe/RESULT.json'
chart=json.loads(source.read_text())
assert chart['status']=='UNIVERSAL_QUOTIENT_CHART_FOUND'
assert chart['field']==3 and chart['dimension']==4 and chart['rank_histogram']=={'4':108}
M=chart['matrices'];V=chart['vectors'];I=[[int(i==j) for j in range(4)]for i in range(4)]
def mm(A,B):return [[sum(A[i][k]*B[k][j]for k in range(4))%3 for j in range(4)]for i in range(4)]
def mv(A,x):return [sum(A[i][j]*x[j]for j in range(4))%3 for i in range(4)]
def line(x,b):return any(all(x[i]%3==t*b[i]%3 for i in range(4))for t in range(3))
def inverse_relation(p,q):
 P=mm(M[q],M[p])
 return all(line([(P[i][j]-I[i][j])%3 for i in range(4)],V[q])for j in range(4)) and line(mv(M[q],V[p]),V[q])
candidates=[[q for q in range(4)if inverse_relation(p,q) and inverse_relation(q,p)]for p in range(4)]
assert all(len(x)==1 for x in candidates),candidates
inv=[x[0]for x in candidates]
assert all(inv[p]!=p and inv[inv[p]]==p for p in range(4)),inv
def rank(columns):
 A=[[columns[j][i]%3 for j in range(len(columns))]for i in range(4)]
 r=0
 for c in range(len(columns)):
  pivot=next((i for i in range(r,4)if A[i][c]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r]
  t=pow(A[r][c],-1,3);A[r]=[(t*x)%3 for x in A[r]]
  for i in range(4):
   if i!=r:
    t=A[i][c];A[i]=[(A[i][j]-t*A[r][j])%3 for j in range(len(columns))]
  r+=1
 return r
def noises(word):
 acc=I;cols=[]
 for p in reversed(word):
  cols.append(mv(acc,V[p]));acc=mm(acc,M[p])
 return cols
words_labels=[]
def labels(prefix):
 if len(prefix)==4:words_labels.append(prefix);return
 for p in range(4):
  if not prefix or p!=inv[prefix[-1]]:labels(prefix+[p])
labels([])
ranks=Counter(rank(noises(w))for w in words_labels)
assert len(words_labels)==108 and ranks=={4:108},ranks
pairs=[(p,inv[p])for p in range(4)if p<inv[p]]
assert len(pairs)==2
cycles=[[0,1,2,3,4],[0,2,4,1,3]]
adj=[[-1]*4 for _ in range(5)]
for cyc,(p,q)in zip(cycles,pairs):
 for i,u in enumerate(cyc):
  v=cyc[(i+1)%5];adj[u][p]=v;adj[v][q]=u
assert all(set(adj[u])==set(range(5))-{u} for u in range(5))
assert all(adj[adj[u][p]][inv[p]]==u for u in range(5)for p in range(4))
tree=[[0,i]for i in range(1,5)]
chords=[[u,v]for u in range(1,5)for v in range(u+1,5)]
chord_index={tuple(e):j for j,e in enumerate(chords)}
def oriented_chord(u,v):
 e=tuple(sorted((u,v)))
 return (1 if u<v else -1)*(chord_index[e]+1)if e in chord_index else 0
records=[];forms={(u,v):Counter()for u in range(5)for v in range(5)}
for root in range(5):
 for word in words_labels:
  path=[root];signed=[];mask=0
  for p in word:
   u=path[-1];v=adj[u][p];code=oriented_chord(u,v)
   if code:signed.append(code);mask^=1<<(abs(code)-1)
   path.append(v)
  records.append(dict(source=root,target=path[-1],ports=word,base_path=path,
      signed_chord_word=signed,V4paritymask=mask))
  forms[root,path[-1]][mask]+=1
raw_counts=[[sum(forms[u,v].values())for v in range(5)]for u in range(5)]
assert all(raw_counts[u][v]==(24 if u==v else 21)for u in range(5)for v in range(5))
def mul(x,y):
 i,j=x%8,x//8;k,l=y%8,y//8
 return (i+(-1 if j else 1)*k+4*j*l)%8+8*(j^l)
def inverse(x):return (-x)%8 if x<8 else (x%8+4)%8+8
assert mul(8,8)==4 and all(mul(x,inverse(x))==0 for x in range(16))
q16_involutions=[x for x in range(16)if inverse(x)==x]
assert q16_involutions==[0,4]
parity=[[((a&mask).bit_count()&1)for mask in range(64)]for a in range(64)]
passes=[];failure_hist=Counter();first_failure=None
ordered_slots=[(u,v,list(forms[u,v].items()))for u in range(5)for v in range(5)]
for a in range(64):
 for b in range(64):
  worst=None;bad=None
  for u,v,terms in ordered_slots:
   counts=[0]*4
   for mask,n in terms:counts[parity[a][mask]+2*parity[b][mask]]+=n
   required=[6,4,4,4]if u==v else [4,4,4,4]
   slack=min(counts[c]-required[c]for c in range(4))
   slot=dict(source=u,target=v,counts=counts,required=required,slack=slack)
   if worst is None or slack<worst['slack']:worst=slot
   if slack<0:
    bad=slot;break
  projection=[((a>>j)&1)+2*((b>>j)&1)for j in range(6)]
  if bad is None:passes.append(dict(chord_V4_values=projection,component_masks=[a,b],minimum_slot=worst))
  else:
   failure_hist[f'{bad["source"]}->{bad["target"]}']+=1
   if first_failure is None:first_failure=dict(chord_V4_values=projection,slot=bad)
data=dict(base='K5',base_vertices=5,oriented_C5_factors=cycles,
    inverse_ports=inv,port_neighbors=adj,star_tree=tree,chords_low_to_high=chords,
    chart_source=str(source.relative_to(ROOT)),chart_column_vector_action=True,
    matrices=M,noise_vectors=V,verified_inverse_port_candidates=candidates,
    reduced4_rank_histogram={str(k):v for k,v in ranks.items()},
    raw_NB4_slot_word_counts=raw_counts,
    field_graph_conditional_order=6480,field_graph_conditional_degree=12)
(HERE/'BASE_INPUT.json').write_text(json.dumps(data,indent=2)+'\n')
(HERE/'WORDS.json').write_text(json.dumps(records,indent=2)+'\n')
(HERE/'PASS_ASSIGNMENTS.json').write_text(json.dumps(passes,indent=2)+'\n')
(HERE/'FIRST_FAILURE.json').write_text(json.dumps(first_failure,indent=2)+'\n')
representative=None
if passes:
 representative=dict(passes[0])
 u=representative['minimum_slot']['source'];v=representative['minimum_slot']['target']
 a,b=representative['component_masks']
 representative['minimum_slot_words_by_coset']={str(c):[w for w in records if w['source']==u and w['target']==v and parity[a][w['V4paritymask']]+2*parity[b][w['V4paritymask']]==c]for c in range(4)}
 (HERE/'REPRESENTATIVE_PASS.json').write_text(json.dumps(representative,indent=2)+'\n')
 prep=dict(status='Q16_FULL_COMMON_COVER_INPUT_PREPARED_NOT_SOLVED',
    Q16_encoding='i+8*j represents r^i*s^j; r^8=1,s^2=r^4,s*r*s^-1=r^-1',
    multiplication=[[mul(x,y)for y in range(16)]for x in range(16)],
    inverse=[inverse(x)for x in range(16)],quotient=[(x%2)+2*(x//8)for x in range(16)],
    lifts_by_V4_coset=[[x for x in range(16)if (x%2)+2*(x//8)==c]for c in range(4)],
    variable_count=6,variables=chords,unfiltered_assignments=16**6,
    passed_projection_assignments=len(passes),remaining_full_assignments=len(passes)*4**6,
    necessary_quotient_prefilter_lossless=True,
    all_full_constraints='For each ordered basepair, exact NB4 ordered chord products cover every Q16 element.',
    BASE_INPUT='BASE_INPUT.json',WORDS='WORDS.json',PASS_ASSIGNMENTS='PASS_ASSIGNMENTS.json',
    full_common_search_calls=0,controller80_graphs_generated=0,field6480_graphs_generated=0)
 (HERE/'Q16_PREPARE.json').write_text(json.dumps(prep,indent=2)+'\n')
elapsed=time.process_time()-START
assert elapsed<10,elapsed
result=dict(status='COMPLETE_Q16_V4_GATE_HAS_PASS'if passes else 'COMPLETE_ALL4096_Q16_V4_ASSIGNMENTS_REJECTED',
    completed_UTC=datetime.now(timezone.utc).isoformat(),
    prediction_at_least_one_projection_pass='SUPPORTED'if passes else 'REFUTED',
    chart_binding=dict(inverse_ports=inv,reduced4_rank_histogram={str(k):v for k,v in ranks.items()}),
    group='Q16 only',quotient='V4',tree_identity_edges=4,chord_variables=6,
    complete_projection_assignments=4096,passed_assignments=len(passes),failed_assignments=4096-len(passes),
    diagonal_identity_coset_word_threshold=6,other_coset_word_threshold=4,
    first_failure_slot_histogram=dict(failure_hist),
    raw_NB4_slot_counts=raw_counts,
    representative_pass_chord_values=passes[0]['chord_V4_values']if passes else None,
    representative_minimum_slot=passes[0]['minimum_slot']if passes else None,
    Q16_controller_existence_claimed=False,D16_paper_cancelled_before_numeric=True,
    scope='Only the exact-NB4 sufficient controller certificate; not actual D4 lift existence.',
    actual_D4_lift_family_excluded=False,
    CPU_seconds=elapsed,CPU_budget_seconds=10,workers=1,
    solver_calls=0,BFS_runs=0,source_record_graph_reads=0,
    controller80_graphs_generated=0,field6480_graphs_generated=0,
    full_common_Q16_search_calls=0,running=False,pending=[])
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'REPORT.md').write_text(
 '# K5/Q16固定V4必要门终态\n\n'
 f'完整4096投影中{len(passes)}通过、{4096-len(passes)}失败；CPU{elapsed:.9f}秒，预算10。\n\n'
 f'真实chart列向量关系核得inverseports={inv}，108个约化四字全rank4。'
 'K5原slot词数对角24、非对角21；V4每coset至少4，对角identity至少6。'
 '全部通过者在PASS_ASSIGNMENTS.json，完整540词及有序chord乘积在WORDS.json，例子及最小槽另存。'
 '通过仅必要，不声称全Q16电压解、80控制器或6480点图。D16在任何数值前以12反向词对不足13逆轨道取消。\n\n'
 'Q16_PREPARE.json（若有pass）给完整共同覆盖的6变量输入和精确乘法/逆表；没有运行后续共同搜索。'
 '原树规范覆盖全部ordinaryvoltage赋值，因为逐顶点fiber重标号可置tree电压为identity；商门没有添加对称或LP限制。'
 '本门只针对exact-NB4充分证书，不把失败或D16纸面门外推为所有K5×G实际D4提升不可能；短路并集仍可能补偿。'
 '0旧源读/BFS/solver/大图，Wiki/root/专家文件未改。\n')
print(json.dumps(dict(status=result['status'],passes=len(passes),CPU_seconds=elapsed,
    inverse_ports=inv,result=str((HERE/'RESULT.json').relative_to(ROOT)))))

"""Natural H3 host binding and one-vertex R4-cover decision.
Only28 eligibleport depth4 masks are built once, including R2/R3 snapshots
for the same-host cooperative producer. No fullsource BFS is performed.
"""
from array import array
from collections import Counter
from itertools import combinations
from pathlib import Path
import json,math,resource,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(29,30))

def save(name,data):(P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
save('PREDICTION.json',{'prediction_id':'P_H3_PORT_OVOID_R4','frozen_before_host_extraction_and_portmask_calculation':True,
 'target_Delta':4,'target_D':5,'savedL':364,'n':{'actual':None,'hypothetical':365},
 'host_hypothesis':'NaturalH3polarity graph has364vertices,714edges,28degree3absoluteports and336degree4vertices;publicDelorme364regularmatchedgraph isdifferent.',
 'falsifiable_prediction':'Each absoluteport closedR4 contains itself and none oftheother27ports. Thus no four distinctspareports canR4-coverthehost, and onevertexmonotone365extension failsuniformly.',
 'intuition':'Absoluteovoidpoints ofthepolar hexagon haveincidencedistance6;afterpolarityfold theyare mutuallydistance5. TheirR4 balls cannot helpcoveroneanother. Capacity ofwalksdoesnotremove thisfreeportclass constraint.',
 'scope':'Only add one newvertex adjacenttoatmost4old degree<4pins,keepalloldedges; no randomedge deletions,otherhostsoroldH9search.',
 'shared_prep':'Compute28R3/R4masks oncehere andhandoffto thecooperative producer. Notall364sourceBFS.'})
(P/'PLAN.md').write_text('''# 自然H3极性图：端口绑定与单点365判定

先区分公开364/728全4regular图与Q_data的自然364/714图。直接导出后者，不从公开图随机删matching。D≤5继承广义六边形polarity投影：point p至polarline pi(q)的奇距离≤5，投影为p到q的≤5walk；删除loop不增距。因Moore(4,4)=161<364，源恰D5。

全部新邻点只能选实际degree<4点。一次构造所有ports闭R2/R3/R4并供同源两点任务复用，先查portclass覆盖障碍；若无统一障碍，完整枚举四pins的有限bitsetunion，首hit导365边表供root独立验收。单核30CPU，无全源BFS、新依赖、solver或随机seed。
''')
qpath=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json'
q=json.load(open(qpath));raw=q['H3_graph'];n=len(raw)
edges=sorted({tuple(sorted((u,v)))for u,row in enumerate(raw)for v in row if u!=v})
adj=[set()for _ in range(n)]
for u,v in edges:adj[u].add(v);adj[v].add(u)
deg=[len(row)for row in adj];ports=[u for u,d in enumerate(deg)if d<4]
assert n==364 and len(edges)==714 and Counter(deg)==Counter({4:336,3:28})
(P/'source364.edges').write_text('364 714\n'+''.join(f'{u} {v}\n'for u,v in edges))
binding={'status':'BOUND_NATURAL_H3_POLARITY_HOST','source_file':str((P/'source364.edges').relative_to(ROOT)),'source_n':364,'source_m':714,'degree_cap':4,
 'degree_histogram':dict(sorted(Counter(deg).items())),'eligible_ports':ports,'eligible_port_count':28,'eligible_port_degrees':[3]*28,'all_port_deficits':1,
 'source_definition':str(qpath.relative_to(ROOT))+"['H3_graph']; remove polarityloops onlyifpresent, otherwise preserveedges exactly. No public364edge deletion.",
 'source_local_existing_evidence':'research/ddp/breadth_20261027_wave4/controller364_quotient/source_local_check.json',
 'source_D5_proof':'NaturalH3 incidencegraph hasdiameter6 andpolarity sigma. Forpointsp,q, pointp->linesigma(q)hasodd distance<=5; polarityquotient mapsit toa<=5walkp->q. Removingloopsteps cannotincreasedistance. Moore4,4=161<364 givesexactD5.',
 'public_regular_source_not_used':'research/ddp/breadth_20261027_wave3/binary_branch364/source.edges:364/728/all4regular,eligible0.',
 'source_all_BFS_repeated':False,'port_order':'ascendingactualnaturalH3labels',
 'R3_binary_file':'R3.u64le.bin','R4_binary_file':'R4.u64le.bin','binary_layout':'port-major28rows,each6littleendianuint64,lowbitsfirst,vertex0bit0;bits364..383zero.',
 'masks_json':'PORT_BALLS.json'}
save('PORT_BINDING.json',binding);print('HOST',n,len(edges),dict(Counter(deg)),'PORTS',ports,flush=True)
# Exactly28 depth4 neighborhood preparations, shared with the cooperative task.
neigh=[sum(1<<v for v in row)for row in adj];R2=[];R3=[];R4=[]
for root in ports:
 seen=front=1<<root
 for depth in range(1,5):
  nxt=0
  while front:
   bit=front&-front;front-=bit;nxt|=neigh[bit.bit_length()-1]
  front=nxt&~seen;seen|=front
  if depth==2:R2.append(seen)
  if depth==3:R3.append(seen)
  if depth==4:R4.append(seen)
allports=sum(1<<v for v in ports);full=(1<<364)-1
porthits=[[(mask>>v)&1 for v in ports]for mask in R4]
diagonal=all(porthits[i][j]==int(i==j)for i in range(28)for j in range(28))
words={k:[[(mask>>(64*j))&((1<<64)-1)for j in range(6)]for mask in vals]for k,vals in [('R3',R3),('R4',R4)]}
for name in ['R3','R4']:
 import struct
 (P/(name+'.u64le.bin')).write_bytes(b''.join(struct.pack('<6Q',*row)for row in words[name]))
save('PORT_BALLS.json',{'source_file':binding['source_file'],'source_n':364,'source_m':714,'ports':ports,'rows_port_order':ports,'words_per_row':6,'vertexbit_layout':'low64first,vertex0bit0',
 'R3_words_u64':words['R3'],'R4_words_u64':words['R4'],'radius3_sizes':[m.bit_count()for m in R3],'radius4_sizes':[m.bit_count()for m in R4],
 'radius4_intersection_with_ports':[[v for v in ports if(mask>>v)&1]for mask in R4],'depth4_port_preparations':28,'source_full_BFS':0})
unionR2=0;totalR2=0
for mask in R2:unionR2|=mask;totalR2+=mask.bit_count()
partition=totalR2==364 and unionR2==full
save('PORT_CLASSES.json',{'R2_class_sizes':[m.bit_count()for m in R2],'R2_classes_partition_all364':partition,'R2_class_members':[[v for v in range(364)if(mask>>v)&1]for mask in R2],
 'R4_port_incidence_is_identity':diagonal,'R3_port_incidence_is_identity':all((mask&allports)==(1<<ports[i])for i,mask in enumerate(R3)),
 'interpretation':'The28absoluteports areseparateR4coverrequirements;R2perfect-code classes ifpartitionflagtrue. These areactualsharedmaskfacts,notassumedfrompublicregularlabeling.'})
unionR4=0
for m in R4:unionR4|=m
hit=None;tested=0;scope=math.comb(len(ports),4)
if not diagonal:
 for pick in combinations(range(28),4):
  tested+=1;cover=R4[pick[0]]|R4[pick[1]]|R4[pick[2]]|R4[pick[3]]
  if cover==full:hit=[ports[i]for i in pick];break
if hit is not None:
 newedges=edges+[(v,364)for v in hit]
 (P/'candidate365.edges').write_text(f'365 {len(newedges)}\n'+''.join(f'{u} {v}\n'for u,v in sorted(newedges)))
 save('first_hit.json',{'source_file':binding['source_file'],'n':365,'m':len(newedges),'degree_cap':4,'target_D':5,'old_pins':hit,'new_vertex':364,'full_old_R4_covered':364,'source_oldedges_preserved':True,'pending':['root-independent-new-parameter-check']})
result={'status':'CLOSED_SINGLE_VERTEX_BY28_INDEPENDENT_PORT_REQUIREMENTS'if diagonal else'FIRST_COMPLETE365_CANDIDATE'if hit else'COMPLETE_FIXED_HOST_ALL_S4_NO_HIT',
 'prediction_id':'P_H3_PORT_OVOID_R4','prediction_verdict':'SUPPORTED'if diagonal else'REFUTED','source_file':binding['source_file'],'source_n':364,'source_m':714,'target_Delta':4,'target_D':5,'savedL':364,
 'n':{'actual':365 if hit else None,'hypothetical':365},'actual_D':None,'ordinary_bad_unordered_pairs':None,'eligible_ports':ports,'port_count':28,
 'R4_port_incidence_is_identity':diagonal,'all28_R4_union_covers_allsource':unionR4==full,'minimum_port_cover_lower_bound':28 if diagonal else None,'minimum_port_cover_exact':28 if diagonal and unionR4==full else None,
 'four_pin_scope':scope,'four_pin_sets_explicitly_evaluated':tested,'four_pin_sets_excluded_by_uniform_obstruction':scope if diagonal else 0,
 'R2_classes_partition_all364':partition,'port_radius4_preparations':28,'source_full_BFS':0,'old_regular_source_rerun':False,'new_graphs_generated':int(hit is not None),'complete_hits':int(hit is not None),
 'CPU_seconds':time.process_time()-START,'scope':'Onlyfixednatural364host,one newvertex,oldedgesretained,atmost4actualsparepins. Notgeneral365graphs,notedge-rewiringorotherhosts.',
 'shared_mask_handoff':'PORT_BINDING.json,PORT_BALLS.json,R3.u64le.bin,R4.u64le.bin','pending':['root-independent-new-parameter-check']if hit else[]}
save('RESULT.json',result);save('terminal.json',result)
print('PORTFACTS R2partition',partition,'R4portidentity',diagonal,'R4unionall',unionR4==full,'S4tested',tested,'scope',scope,'hit',hit,'CPU',result['CPU_seconds'],flush=True)

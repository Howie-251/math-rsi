"""Recover the6-base C12rule; symbolic capacities and exactly one C14lift."""
import collections,json,pathlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(119,120))
P=pathlib.Path(__file__).resolve().parent;ROOT=P.parents[4];start=time.process_time()
SRC=ROOT/'research/ddp/more_graphs_20261027/d3d4_transfer/source72.implicit_adj.txt'
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
adj=[set(map(int,x.split()))for x in SRC.read_text().splitlines()if x.strip()]
cross=[];half=[]
for t in range(6):
 for v in sorted(adj[12*t]):
  s,j=divmod(v,12)
  if s>t:cross.append((t,s,j if j<=6 else j-12))
  elif s==t:
   assert j==6;half.append(t)
cross.sort();assert len(cross)==14 and half==[2,4]
save('CYCLIC_RULE.json',{'source_path':str(SRC.relative_to(ROOT)),'vertex_coordinates':'12*type+position; type0..5,position0..11','C12_action':'Add1 toposition,fix type','cross_orientation':'typea<typeb; signed voltage in[-5,6]; reverse uses exact negative integer',
 'cross_edges':cross,'halfturn_base_vertices':half,'general_even_rule':'V={(t,i):t0..5,i modm}; crossedge(a,b,d) gives(a,i)--(b,i+d); internalhalfturn gives(t,i)--(t,i+m/2) for t2,4.',
 'order':'6m','degree':5,'edge_count':'15m','literal_scope':'Keep these14balancedintegers, changeonlym andthetwo forcedhalfturns. No alternate representative or free offset is tested.'})
save('CYCLIC_PREDICTION.json',{'prediction_id':'P_EXOO72_C14_HALFTURN_COMPLEMENT','frozen_before_programmatic_C14_endpoint_evaluation':True,'paper_derived_before_freeze':True,
 'source_rule':'CYCLIC_RULE.json','target':[5,3],'savedL':72,'m':14,'hypothetical_order':84,
 'falsifiable_prediction':'At root(type0,position0), samefiber endpoints within3 are exactly{0,1,3,4,5,7,9,10,11,13},missing{2,6,8,12}; therefore the literal balanced C14lift failsD3.',
 'reason':'Closedwalk offsets are{0,+/-1,+/-3,+/-4,+/-5,+/-7,h,h+/-4},h=m/2. Sourceh6adds evenresidues2/6/10,buttargeth7makesallhalfturnterms duplicateexistingoddresidues.',
 'capacity_scope':'Free14edge-voltage formalforms give a different uniformfixedbase bound; fixedinteger(a,b*h) forms only bound this literalrule.',
 'one_C14_only':True,'no_C16_numeric_no_offset_grid':True})
K=len(cross);arcs=[[]for _ in range(6)];inv={}
for j,(a,b,d)in enumerate(cross):
 f=[0]*(K+1);f[j]=1;g=[0]*(K+1);g[j]=-1
 arcs[a].append((2*j,b,tuple(f),(d,0)));arcs[b].append((2*j+1,a,tuple(g),(-d,0)));inv[2*j]=2*j+1;inv[2*j+1]=2*j
for j,t in enumerate(half):
 label=2*K+j;v=[0]*(K+1);v[-1]=1
 arcs[t].append((label,t,tuple(v),(0,1)));inv[label]=label
assert all(len(row)==5 for row in arcs)
raw=[];free=[];fixed=[]
for root in range(6):
 rs=[0]*6;fs=[set()for _ in range(6)];xs=[set()for _ in range(6)]
 rs[root]=1;fs[root].add((0,)*(K+1));xs[root].add((0,0));front=[(root,(0,)*(K+1),(0,0),-1)];counts=[1]
 for length in range(1,4):
  nxt=[]
  for side,f,x,prev in front:
   for label,target,g,y in arcs[side]:
    if prev>=0 and label==inv[prev]:continue
    h=tuple(f[i]+g[i]for i in range(K))+((f[-1]+g[-1])%2,)
    val=(x[0]+y[0],(x[1]+y[1])%2)
    rs[target]+=1;fs[target].add(h);xs[target].add(val);nxt.append((target,h,val,label))
  front=nxt;counts.append(len(front))
 assert counts==[1,5,20,80]
 raw.append(rs);free.append(fs);fixed.append(xs)
cap={'status':'COMPLETE_SIX_ROOT_SYMBOLIC_ROUTE_CAPACITY','raw_reducedword_counts':raw,'free_edge_voltage_forms':[[len(x)for x in row]for row in free],'fixed_balanced_integer_halfturn_forms':[[len(x)for x in row]for row in fixed],
 'minimum_raw_count':min(x for row in raw for x in row),'minimum_free_voltage_capacity':min(len(x)for row in free for x in row),'minimum_literal_rule_capacity':min(len(x)for row in fixed for x in row),
 'free_voltage_model':'14independent integer crossedgevoltage variables + sharedC2halfturn symbol, inverseconsistent. This is an upperbound aftermodm evaluation.',
 'literal_model':'Offsetinteger a plus b*(m/2),b inC2, retaining14fixedbalancedintegers. This bounddoesnotexcludeotherfreevoltageassignments.',
 'root0_self_literal_forms':[list(x)for x in sorted(fixed[0][0])],'symbolic_CPU_seconds':time.process_time()-start}
save('CYCLIC_CAPACITY.json',cap)
# Exactly the frozen m14 instance;6representative<=3word endpoint evaluations, noBFS.
m=14;rootrows=[]
for root in range(6):
 coverage=[sorted({(a+b*(m//2))%m for a,b in vals})for vals in fixed[root]]
 missing=[{'target_type':t,'missing_positions':sorted(set(range(m))-set(vals))}for t,vals in enumerate(coverage)if len(vals)<m]
 rootrows.append({'root_type':root,'covered_by_target_type':[len(x)for x in coverage],'missing_states':sum(m-len(x)for x in coverage),'missing':missing})
# A complete candidate is instantiated once; static degreecheck is not anotherdistance test.
edges=set()
for a,b,d in cross:
 for i in range(m):edges.add(tuple(sorted((a*m+i,b*m+(i+d)%m))))
for t in half:
 for i in range(m//2):edges.add((t*m+i,t*m+i+m//2))
deg=collections.Counter(v for e in edges for v in e)
assert len(edges)==210 and set(deg.values())=={5} and len(deg)==84
(P/'C14.edges').write_text('84 210\n'+''.join(f'{a} {b}\n'for a,b in sorted(edges)))
actual_self=sorted({(a+b*7)%14 for a,b in fixed[0][0]})
assert actual_self==[0,1,3,4,5,7,9,10,11,13]
res={'status':'COMPLETE_ONE_C14_LITERAL_LIFT_TARGET_FAILED','prediction_id':'P_EXOO72_C14_HALFTURN_COMPLEMENT','prediction_verdict':'SUPPORTED',
 'target_Delta':5,'target_D':3,'savedL':72,'n':{'actual':84,'hypothetical':None},'m':210,'actual_graph_Delta':5,'actual_D':None,'actual_D_scope':'Six exactcyclicorbit roots evaluatedonly throughradius3;sourceC12BFSnotrepeated. D3false,butexactdiameternotcomputed.',
 'ordinary_bad_unordered_pairs':None,'root_rows':rootrows,'root0_self_coverage':actual_self,'root0_self_missing':[2,6,8,12],
 'new_record':False,'candidate_edgefile':'C14.edges','candidate_graphs_generated':1,'source_BFS':0,'candidate_BFS':0,
 'literal_balanced_even_rule_closed_above72':True,'proof':'Moore5,3=106 permits6m<=106, evenm>12 only14/16. Fixedliteralroot0self has14formal(a,bh)offsets,soallm>=16impossible;frozenm14hasactualselfcoverage10<14. Doesnotclosefreevoltages.',
 'scope':'Only6-base topology, sharedhalfturns, frozen14balancedcrossintegers andevenm>12. GeneralC14freevoltagebase, other6base lifts andgeneral73graphsnotexcluded.',
 'CPU_seconds':time.process_time()-start,'pending':[]}
save('CYCLIC_RESULT.json',res)
print('RULE',cross,'half',half);print('MIN raw/free/literal',cap['minimum_raw_count'],cap['minimum_free_voltage_capacity'],cap['minimum_literal_rule_capacity']);print('C14',[(x['root_type'],x['covered_by_target_type'],x['missing_states'])for x in rootrows],'CPU',res['CPU_seconds'])

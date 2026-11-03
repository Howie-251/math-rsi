from pathlib import Path
from collections import Counter
import json,time,resource,sys,itertools
D=Path(__file__).resolve().parent;G=D.parent;S=G.parent
sys.path.insert(0,str(G))
from analyze_g import inverse,mv,dot,equation,holds,RVALUES
T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(45,46))
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def code(v):return sum(a*3**i for i,a in enumerate(v))
V=[tuple((k//3**i)%3 for i in range(5)) for k in range(243)]
W={v for v in V if v[2:]==(0,0,0)}
def reduce_rows(A,n=5):
    A=[list(r) for r in A];piv=[];r=0
    for j in range(n):
        k=next((i for i in range(r,len(A)) if A[i][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r];z=pow(A[r][j],-1,3);A[r]=[a*z%3 for a in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                z=A[i][j];A[i]=[(a-z*b)%3 for a,b in zip(A[i],A[r])]
        piv.append(j);r+=1
        if r==len(A):break
    return A[:r],piv
def span(B):return {tuple(sum(t[j]*B[j][i] for j in range(len(B)))%3 for i in range(5)) for t in itertools.product(range(3),repeat=len(B))}
def normal(B):
    A,piv=reduce_rows(B);free=[j for j in range(5) if j not in piv];assert len(free)==1
    f=[0]*5;f[free[0]]=1
    for row,j in zip(A,piv):f[j]=-row[free[0]]%3
    z=pow(next(a for a in f if a),-1,3);return [a*z%3 for a in f]
C=json.loads((S/'LINE_KERNELS.json').read_text())['chart'];M=json.loads((S/'MAPPING_DATA.json').read_text());St=json.loads((S/'STRUCTURE.json').read_text());P=json.loads((G/'PREPARED_GEOMETRY.json').read_text());old=json.loads((G/'RESULT.json').read_text())
regular={r['source'] for r in P['source_bindings']};exceptional=sorted(set(range(364))-regular);assert len(exceptional)==49
mt=M['main_fiber_target'];assert all(mt[mt[a]]==a and mt[a]!=a and mt[a] in [e['target'] for e in C[a]] for a in range(364))
assert P['all_target_incoming_directions_verified_distinct_W_lines']==364
loop=[]
for rec in St['self_ports']:
    a=rec['controller'];p=rec['port'];L={V[k] for k in rec['self_loop_vectors']};B,_=reduce_rows(L);LW=L&W;WB,_=reduce_rows(LW)
    assert len(L)==27 and len(B)==3 and span(B)==L and len(LW)==3 and len(WB)==1
    ell=C[a][p]['source_line_kernel'];assert tuple(ell) in LW and any(ell)
    loop.append({'source':a,'port':p,'loop_locus_basis':B,'loop_locus_dimension':3,'loop_locus_size':27,'loop_locus_intersection_W':sorted(LW),'loop_locus_intersection_W_dimension':1,'input_noise_line':ell,'all_affine_W_transverse_H_loop_intersection_upper':9})
assert len(loop)==28 and {r['source'] for r in loop}=={a for a in range(364) if M['self_loop_masks'][a]}
loopCPU=time.process_time()-T
save('LOOP_GEOMETRY.json',{'status':'ALL28_LOOP_LOCI_LINEAR3_WITH_W_LINE','records':loop,'target_incoming_four_W_lines_verified':364,'M_fiber_permutation_involutive_no_fixed_and_target_also_ordinary':True,'self_ordinary_output_deletion_upper_per_affine_full27_block':9,'different_normal_hyperplane_intersection':27,'ordinary_row_necessary_inequality':'s_b+x_mate(b)<=3','all364_normal_exclusivity_preserved':True,'scope':'One affine full27 W-transverse block per selected source. P adds load. No claim for arbitrary nonlinear27 transversals.','preparation_CPU_seconds':loopCPU})
# Reduce already fixed regular equation geometry, retaining the matching-port mask.
maskcache={}
for typ in P['geometry_types']:
    vals=[]
    for k,R in enumerate(RVALUES):
        if holds(typ['M_zero_equation'],R):continue
        truths=tuple(holds(eq,R) for eq in typ['g_equations']);vals.append((k,truths,sum(truths)))
    maskcache[typ['type_id']]=vals
reg=[]
for bind in P['source_bindings']:
    typ=P['geometry_types'][bind['type_id']];mp=bind['M_ordinary_port'];meq=bind['g_port_equations'][mp]['g_equation'];j=typ['g_equations'].index(meq)
    best=min((13-2*g-int(not truths[j]),k,g,not truths[j]) for k,truths,g in maskcache[bind['type_id']])
    gmax=max(g for k,t,g in maskcache[bind['type_id']]);assert gmax==old['source_gmax'][str(bind['source'])]
    reg.append({'source':bind['source'],'gmax':gmax,'minimum_cost':best[0],'first_min_cost_R_code':best[1],'witness_g':best[2],'matching_port_bad':best[3]})
regcost=Counter(r['minimum_cost'] for r in reg)
save('REGULAR_STRONG_COST.json',{'source_count':315,'cost_formula':'13-2*g(H)-1_{matching_port_bad}','source_minimum_cost_histogram':dict(sorted(regcost.items())),'records':reg,'scope':'Exact reduction of the same previously completed729-slope regular315 domain; no new matrices or phases.','CPU_seconds_counted_in':'RESULT.json'})
# Build only the49*243 required local center-neighborhood records.
neigh={};prep_counts=[]
for a in exceptional:
    rows=[];nloops=0;np=0
    for k,x in enumerate(V):
        parts=[]
        for e in C[a]:
            y=mv(e['A'],x)
            raw={243*e['target']+code([(z+t*b)%3 for z,b in zip(y,e['b'])]) for t in range(3)}
            own=243*a+k;nloops+=int(own in raw);raw.discard(own);parts.extend(raw)
        parts.append(243*mt[a]+M['main_fiber_coordinate_maps'][a][k])
        pv=M['spare_vertex_map'][243*a+k]
        if pv>=0:parts.append(pv);np+=1
        assert len(parts)==13 and len(set(parts))==13
        rows.append(tuple(parts))
    neigh[a]=rows;prep_counts.append({'source':a,'centers_precomputed':243,'old_degree':13,'loop_centers':nloops,'P_centers':np})
preparedCPU=time.process_time()-T
save('LOCAL_NEIGHBORHOOD_SCOPE.json',{'sources':exceptional,'source_count':49,'center_records':49*243,'degree_histogram':{'13':49*243},'by_source':prep_counts,'complete_graph_constructed':False,'CPU_preparation_seconds':preparedCPU})
# For each exceptional source, only four-linearly-constrained g4 slopes and their9 phases.
cache={};results=[];stopped=False
for a in exceptional:
    if time.process_time()-T>43:stopped=True;break
    eqs=[]
    for e in C[a]:
        key=tuple(map(tuple,e['A']))
        if key not in cache:cache[key]=inverse(e['A'])
        Ai=cache[key];ell=mv(Ai,e['b']);assert ell[2:]==[0,0,0] and any(ell[:2]);L=[-ell[1]%3,ell[0]]
        j=0 if e['b'][1] else 1;v=mv(Ai,[int(i==j) for i in range(5)]);eqs.append(equation(L,v))
    slopes=[k for k,R in enumerate(RVALUES) if all(holds(eq,R) for eq in eqs)]
    tested=0;witness=None;first_failure=None
    for k in slopes:
        R=RVALUES[k];B=[[R[j],R[3+j]]+[int(i==j) for i in range(3)] for j in range(3)];HV=span(B);assert len(HV)==27 and HV&W=={(0,0,0,0,0)}
        for phase in range(9):
            tested+=1;c=[phase%3,phase//3,0,0,0];centers=sorted(code([(u+v)%3 for u,v in zip(x,c)]) for x in HV)
            seen=set();collision=None
            for center in centers:
                for v in neigh[a][center]:
                    if v in seen:collision=v;break
                    seen.add(v)
                if collision is not None:break
            if collision is not None:
                if first_failure is None:first_failure={'R_code':k,'phase':phase,'shared_old_vertex':collision}
                continue
            assert len(seen)==351
            ports=[];removed=0
            for p,e in enumerate(C[a]):
                outbasis=[mv(e['A'],z) for z in B]+[e['b']];n=normal(outbasis);assert n[:2]==[0,0]
                const=dot(n,mv(e['A'],c));raw=set()
                for center in centers:
                    y=mv(e['A'],V[center]);raw.update(code([(u+t*v)%3 for u,v in zip(y,e['b'])]) for t in range(3))
                assert len(raw)==81 and all(dot(n,V[v])==const for v in raw)
                # Literal self-loop domain gives exactly which raw incidences were removed.
                deleted=[k for k in centers if e['target']==a and M['self_loop_masks'][a]>>k&1]
                assert len(deleted)<=9;removed+=len(deleted)
                ports.append({'port':p,'target':e['target'],'normal':n,'affine_constant':const,'raw_size':81,'deleted_loop_count':len(deleted)})
            witness={'R_code':k,'R_rows':[list(R[:3]),list(R[3:])],'H_basis':B,'phase_code':phase,'phase_vector':c,'center_local_labels':centers,'center_global_labels':[243*a+x for x in centers],'g':4,'ordinary_ports':ports,'ordinary_raw_count':324,'deleted_loops':removed,'P_neighbor_count':sum(M['spare_vertex_map'][243*a+x]>=0 for x in centers),'M_neighbor_count':27,'full_old_N_union_size':351,'max_old_load':1}
            break
        if witness:break
    results.append({'source':a,'kind':'self/P' if M['self_loop_masks'][a] else 'nonself_nonaffine_M','all729_slopes_filtered':True,'g4_slope_count':len(slopes),'g4_possible_phase_blocks':9*len(slopes),'phase_blocks_checked':tested,'has_local_g4':witness is not None,'complete_domain_checked_if_no_witness':witness is None,'first_failure':first_failure,'witness':witness})
    save('EXCEPTIONAL_SOURCE_RESULTS.json',{'status':'RUNNING_FINITE49_GATE','source_records':results,'unprocessed_sources':[b for b in exceptional if b not in {r['source'] for r in results}],'CPU_seconds':time.process_time()-T})
if stopped:
    status='UNKNOWN_BUDGET_STOP';available=None;combined_upper=None
else:
    assert len(results)==49
    available=sum(r['has_local_g4'] for r in results)
    # Nong4 exceptions receive optimistic cost6; no need to check theirg3 domains.
    costs=sorted([r['minimum_cost'] for r in reg]+[5 if r['has_local_g4'] else 6 for r in results]);used=0;combined_upper=0
    for cost in costs:
        if used+cost>1092:break
        used+=cost;combined_upper+=1
    status='ALL364_AFFINE_FULL27_RULE_EXCLUDED_BY_COST_GATE' if combined_upper<213 else 'EXCEPTIONAL_G4_RESOURCE_GATE_PASSES_GLOBAL_PACKING_OPEN'
res={'status':status,'source_count':49,'completed_sources':len(results),'exceptions_with_local_g4':available,'regular_g4_sources':175,'needed_g4_sources_for213_fullblocks':186,'needed_exceptional_g4_sources':11,'regular_minimum_cost_histogram':dict(sorted(regcost.items())),'optimistic_exception_costs':'5 for witnessedg4;6 for completeg4-negative (g3 remains optimistic)','all364_optimistic_fullblock_upper':combined_upper,'capacity_budget':1092,'necessary_cost_inequality':'sum_selected min_H(13-2g(H)-1_matching_bad)<=1092','loop_gate_verified':True,'loop_deletion_upper':9,'source_results':'EXCEPTIONAL_SOURCE_RESULTS.json','loop_geometry':'LOOP_GEOMETRY.json','regular_costs':'REGULAR_STRONG_COST.json','CPU_seconds':time.process_time()-T,'CPU_budget_seconds':45,'worker_count':1,'solver_calls':0,'BFS_runs':0,'complete_graphs':0,'new_cloned_graphs':0,'running':False,'pending':[],'scope':'One full27 affine W-transverse block per chosen original fiber, cap14 full-old-N clones. Necessary global resource gate only. Does not cover nonlinear or partial blocks.'}
if not stopped:res['all364_optimistic_cost_used_by_cheapest_blocks']=used
save('RESULT.json',res);save('EXCEPTIONAL_SOURCE_RESULTS.json',{'status':'COMPLETE' if not stopped else status,'source_records':results,'unprocessed_sources':[b for b in exceptional if b not in {r['source'] for r in results}],'CPU_seconds_counted_in':'RESULT.json'})
print(json.dumps(res))
print('source_g4_witnesses',[r['source'] for r in results if r['has_local_g4']])
print('source_g4_negative',[r['source'] for r in results if not r['has_local_g4']])

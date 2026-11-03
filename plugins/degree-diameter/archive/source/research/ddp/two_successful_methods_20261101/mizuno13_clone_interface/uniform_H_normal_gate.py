from pathlib import Path
from collections import Counter,defaultdict
import json,time,resource

D=Path(__file__).resolve().parent
T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(30,31))
L=json.loads((D/'LINE_KERNELS.json').read_text());C=L['chart'];M=json.loads((D/'MAPPING_DATA.json').read_text());F=json.loads((D/'INVARIANT_FUNCTIONAL_RESULT.json').read_text());H=F['H_basis']
V=[tuple((x//3**j)%3 for j in range(5)) for x in range(243)];normals=L['projective_normals'];normal_index={tuple(v):i for i,v in enumerate(normals)};normal_masks=L['normal_fiber_masks']
def dot(x,y):return sum(a*b for a,b in zip(x,y))%3
def mv(A,x):return [dot(row,x) for row in A]
def enc(x):return sum(a*3**j for j,a in enumerate(x))
def nullvector(A):
    A=[list(row) for row in A];piv=[];r=0
    for c in range(5):
        k=next((i for i in range(r,len(A)) if A[i][c]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r];z=pow(A[r][c],-1,3);A[r]=[x*z%3 for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                z=A[i][c];A[i]=[(x-z*y)%3 for x,y in zip(A[i],A[r])]
        piv.append(c);r+=1
        if r==len(A):break
    free=[j for j in range(5) if j not in piv];assert len(free)==1
    z=[0]*5;z[free[0]]=1
    for row,c in zip(A,piv):z[c]=-row[free[0]]%3
    scale=pow(next(x for x in z if x),-1,3)
    return [x*scale%3 for x in z]
phase_vectors=[[a,b,0,0,0] for b in range(3) for a in range(3)]
phase_centers=[sorted(enc([(a+b)%3 for a,b in zip(V[x],c)]) for x in F['center_local_labels']) for c in phase_vectors]
records=[];nonself=[];nonaffine=[];no_local_phase=[]
for u,row in enumerate(C):
    if any(e['target']==u for e in row):continue
    assert all(M['spare_vertex_map'][243*u+x]<0 for x in range(243))
    nonself.append(u);coords=M['main_fiber_coordinate_maps'][u];translation=V[coords[0]]
    cols=[[(a-b)%3 for a,b in zip(V[coords[3**j]],translation)] for j in range(5)];matrix=[list(x) for x in zip(*cols)]
    affine=all(tuple((a+b)%3 for a,b in zip(mv(matrix,x),translation))==V[coords[code]] for code,x in enumerate(V))
    if not affine:nonaffine.append(u);continue
    matching_target=M['main_fiber_target'][u];mp=next(p for p,e in enumerate(row) if e['target']==matching_target)
    portdata=[]
    for p,e in enumerate(row):
        n=nullvector([mv(e['A'],h) for h in H]+[e['b']]);j=normal_index[tuple(n)]
        assert all(dot(n,mv(e['A'],h))==0 for h in H) and dot(n,e['b'])==0
        portdata.append({'port':p,'target':e['target'],'normal':n,'normal_index':j})
    phases=[];valid=[]
    for phase,(c,centers) in enumerate(zip(phase_vectors,phase_centers)):
        constants=[dot(z['normal'],mv(e['A'],c)) for z,e in zip(portdata,row)]
        ordinary_M_mask=normal_masks[portdata[mp]['normal_index']][constants[mp]]
        actual_M_mask=sum(1<<coords[x] for x in centers)
        assert actual_M_mask.bit_count()==27
        overlap=(actual_M_mask&ordinary_M_mask).bit_count()
        if not overlap:valid.append(phase)
        phases.append({'phase':phase,'ordinary_hyperplane_constants':constants,'M_ordinary_overlap':overlap,'local_cap14_feasible':not overlap})
    if not valid:no_local_phase.append(u)
    records.append({'source':u,'M_affine_matrix':matrix,'M_affine_translation':translation,'M_matches_ordinary_matrix':matrix==row[mp]['A'],'M_target':matching_target,'M_ordinary_port':mp,'ordinary_ports':portdata,'valid_phase_codes':valid,'phase_checks':phases})
assert len(nonself)==336
available=[x for x in records if x['valid_phase_codes']]
targets=[defaultdict(list) for _ in range(364)]
for source in available:
    for p in source['ordinary_ports']:targets[p['target']][tuple(p['normal'])].append(source['source'])
targetdata=[]
for b,groups in enumerate(targets):
    h=max(map(len,groups.values()),default=0);bound=min(3,h)
    targetdata.append({'target':b,'normal_groups':[{'normal':list(n),'sources':sorted(set(a)),'source_count':len(set(a))} for n,a in sorted(groups.items())],'h_b':h,'ordinary_block_upper':bound})
right=sum(x['ordinary_block_upper'] for x in targetdata);upper=right//4
result={'status':'UNIFORM_H_AFFINE_PHASE_DOMAIN_EXCLUDED_BY_NORMAL_BOUND' if upper<213 else 'NORMAL_BOUND_PASSES_GLOBAL_PACKING_NOT_CHECKED','H_basis':H,'H_rule':'{(-z,0,a,b,z)}','phases':phase_vectors,'nonself_noP_sources_checked':len(nonself),'nonaffine_M_source_count_excluded':len(nonaffine),'nonaffine_M_sources_excluded':nonaffine,'affine_sources_probed':len(records),'M_equals_matching_ordinary_matrix_count':sum(x['M_matches_ordinary_matrix'] for x in records),'valid_phase_count_histogram':dict(sorted(Counter(len(x['valid_phase_codes']) for x in records).items())),'sources_with_some_local_phase':len(available),'sources_with_no_local_phase':no_local_phase,'h_b_histogram':dict(sorted(Counter(x['h_b'] for x in targetdata).items())),'ordinary_target_bound_histogram':dict(sorted(Counter(x['ordinary_block_upper'] for x in targetdata).items())),'normal_gate_RHS_sum':right,'block_count_upper':upper,'full27_clone_count_upper':27*upper,'final_n_upper':88452+27*upper,'needed_full27_blocks':213,'source_target_incidence_count':sum(sum(len(a) for a in groups.values()) for groups in targets),'expected_source_target_incidence_count':4*len(available),'CPU_seconds':time.process_time()-T,'CPU_budget_seconds':30,'scope':'Fixed common H, all nine W-affine cosets, at most one full27 block in each nonself/noP fiber with affine M and at least one locally legal coset. Other H/nonlinear transversals, nonaffine M and partial blocks remain open.','proof':'At each target, any two nonparallel affine81 hyperplanes intersect in27 points, so all chosen ordinary providers must share one projective normal. A parallel class has only3 disjoint affine levels; therefore ordinary providers <=min(3,h_b). Sum over364 targets, each selected block contributes4.','solver_calls':0,'BFS_runs':0,'new_graphs':0,'global_packing_checked':False,'running':False,'pending':[]}
assert result['source_target_incidence_count']==result['expected_source_target_incidence_count']
(D/'UNIFORM_H_SOURCE_PHASES.json').write_text(json.dumps({'source_records':records,'nonaffine_M_sources_excluded':nonaffine,'H_basis':H,'phase_vectors':phase_vectors},indent=2)+'\n')
(D/'UNIFORM_H_TARGET_NORMAL_GROUPS.json').write_text(json.dumps({'targets':targetdata,'ordinary_incoming_source_incidence_count':result['source_target_incidence_count']},indent=2)+'\n')
(D/'UNIFORM_H_NORMAL_GATE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

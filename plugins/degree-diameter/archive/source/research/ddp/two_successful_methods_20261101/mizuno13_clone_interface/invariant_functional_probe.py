from pathlib import Path
from collections import defaultdict,Counter
import json,time,resource

D=Path(__file__).resolve().parent
T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(20,21))
C=json.loads((D/'LINE_KERNELS.json').read_text())['chart']
data=json.loads((D/'MAPPING_DATA.json').read_text())
V=[tuple((x//3**j)%3 for j in range(5)) for x in range(243)]
def dot(x,y):return sum(a*b for a,b in zip(x,y))%3
def mv(A,x):return [dot(r,x) for r in A]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(5))%3 for j in range(5)] for i in range(5)]
def rank(vectors):
    if not vectors:return 0
    A=[list(x) for x in vectors];r=0
    for j in range(5):
        k=next((i for i in range(r,len(A)) if A[i][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r];z=pow(A[r][j],-1,3);A[r]=[x*z%3 for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                z=A[i][j];A[i]=[(a-z*b)%3 for a,b in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r
def inverse(B):
    A=[list(row)+[int(i==j) for j in range(5)] for i,row in enumerate(B)]
    for j in range(5):
        k=next(i for i in range(j,5) if A[i][j]);A[j],A[k]=A[k],A[j];z=pow(A[j][j],-1,3);A[j]=[x*z%3 for x in A[j]]
        for i in range(5):
            if i!=j and A[i][j]:
                z=A[i][j];A[i]=[(a-z*b)%3 for a,b in zip(A[i],A[j])]
    return [row[5:] for row in A]
def enc(x):return sum(a*3**j for j,a in enumerate(x))
u=0;target=data['main_fiber_target'][u];p=next(i for i,e in enumerate(C[u]) if e['target']==target)
assert p==3 and all(e['target']!=u for e in C[u]) and all(data['spare_vertex_map'][x]<0 for x in range(243))
m=data['main_fiber_coordinate_maps'][u];d=V[m[0]];Fcols=[[(a-b)%3 for a,b in zip(V[m[3**j]],d)] for j in range(5)];F=[list(x) for x in zip(*Fcols)]
assert all(tuple((a+b)%3 for a,b in zip(mv(F,x),d))==V[m[code]] for code,x in enumerate(V))
Ai=inverse(C[u][p]['A']);K=mm(Ai,F);dp=mv(Ai,d);ell=mv(Ai,C[u][p]['b'])
normals=[x for x in V[1:] if next(a for a in x if a)==1]
stage=Counter();solutions=[]
for f in normals:
    if dot(f,ell):continue
    stage['annihilate_ell']+=1
    if [sum(f[i]*K[i][j] for i in range(5))%3 for j in range(5)]!=list(f):continue
    stage['also_invariant']+=1
    if not dot(f,dp):continue
    stage['also_detect_translation']+=1
    if not (f[0] or f[1]):continue
    stage['also_nonzero_on_W']+=1;solutions.append(list(f))
result={'status':'INVARIANT_FUNCTIONAL_REPAIR_FOUND' if solutions else 'NO_FUNCTIONAL_IN_SPECIFIED_SUFFICIENT_CLASS','controller':u,'matching_target_fiber':target,'matching_ordinary_port':p,'M_affine_matrix_F':F,'M_affine_translation_d':d,'ordinary_matrix_A':C[u][p]['A'],'A_inverse':Ai,'K_AinverseF':K,'dprime_Ainversed':dp,'ell_Ainverseb':ell,'projective_functionals_checked':121,'successive_filter_counts':dict(stage),'all_valid_functionals':solutions,'CPU_budget_seconds':20,'full_source_BFS_runs':0,'full_graph_generated':False,'solver_calls':0,'scope':'This one invariant-functional sufficient repair on fiber0; not all linear complements, nonlinear W-transversals, other fibers or global clone packing'}
if solutions:
    f=solutions[0];Wbasis=[[1,0,0,0,0],[0,1,0,0,0]];H=[]
    for x in V[1:]:
        if dot(f,x)==0 and rank(Wbasis+H+[list(x)])>2+len(H):H.append(list(x))
        if len(H)==3:break
    assert len(H)==3 and rank(Wbasis+H)==5 and all(dot(f,x)==0 for x in H)
    centers=sorted({enc([(a*H[0][j]+b*H[1][j]+c*H[2][j])%3 for j in range(5)]) for a in range(3) for b in range(3) for c in range(3)})
    assert len(centers)==27
    providers=defaultdict(list);ordinary=set();mimages=set()
    for code in centers:
        x=V[code]
        for port,e in enumerate(C[u]):
            y=mv(e['A'],x)
            for t in range(3):
                v=243*e['target']+enc([(a+t*b)%3 for a,b in zip(y,e['b'])]);assert v!=code
                providers[v].append({'center':code,'kind':'ordinary','port':port,'noise':t});ordinary.add(v)
        v=243*target+m[code];providers[v].append({'center':code,'kind':'M'});mimages.add(v)
    collision=[{'old_vertex':v,'providers':p} for v,p in providers.items() if len(p)>1]
    transformed_ordinary={dot(f,mv(Ai,V[v%243])) for v in ordinary if v//243==target}
    transformed_M={dot(f,mv(Ai,V[v%243])) for v in mimages}
    assert not collision and len(providers)==351 and len(ordinary)==324 and len(mimages)==27
    assert transformed_ordinary=={0} and transformed_M=={dot(f,dp)} and dot(f,dp)!=0
    result.update({'chosen_f':f,'f_dprime':dot(f,dp),'H_basis':H,'H_dimension':3,'H_intersection_W_trivial':True,'H_subset_ker_f':True,'center_local_labels':centers,'full_old_neighbor_union_size':len(providers),'ordinary_union_size':len(ordinary),'M_union_size':len(mimages),'P_image_count':0,'ordinary_M_overlap':0,'max_old_load':max(map(len,providers.values())),'target_fiber_Ainverse_ordinary_f_values':sorted(transformed_ordinary),'target_fiber_Ainverse_M_f_values':sorted(transformed_M),'old_target_counts_by_fiber':dict(sorted(Counter(v//243 for v in providers).items())),'local_capacity_feasible':True,'global_block_packing_examined':False})
result['CPU_seconds']=time.process_time()-T
(D/'INVARIANT_FUNCTIONAL_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

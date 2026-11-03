from pathlib import Path
from collections import defaultdict,Counter
import json,time,resource

D=Path(__file__).resolve().parent
T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(20,21))
C=json.loads((D/'LINE_KERNELS.json').read_text())['chart'][0]
M=json.loads((D/'MAPPING_DATA.json').read_text())
F=json.loads((D/'INVARIANT_FUNCTIONAL_RESULT.json').read_text())
H=F['H_basis'];Hcodes=F['center_local_labels'];V=[tuple((x//3**j)%3 for j in range(5)) for x in range(243)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))%3
def mv(A,x):return [dot(row,x) for row in A]
def enc(x):return sum(a*3**j for j,a in enumerate(x))
def nullvector(A):
    A=[list(row) for row in A];piv=[];r=0
    for c in range(5):
        q=next((i for i in range(r,len(A)) if A[i][c]),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r];z=pow(A[r][c],-1,3);A[r]=[x*z%3 for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                z=A[i][c];A[i]=[(x-z*y)%3 for x,y in zip(A[i],A[r])]
        piv.append(c);r+=1
        if r==len(A):break
    free=[j for j in range(5) if j not in piv];assert len(free)==1
    n=[0]*5;n[free[0]]=1
    for row,c in zip(A,piv):n[c]=-row[free[0]]%3
    scale=pow(next(x for x in n if x),-1,3)
    return [x*scale%3 for x in n]
normals=[]
for e in C:
    cols=[mv(e['A'],h) for h in H]+[e['b']]
    normals.append(nullvector(cols))
phases=[]
for code in range(9):
    c=[code%3,code//3,0,0,0]
    centers=sorted(enc([(x+y)%3 for x,y in zip(V[h],c)]) for h in Hcodes)
    providers=defaultdict(list);O=set();MM=set();P=set();byport=[]
    for p,e in enumerate(C):
        image=set()
        for x in centers:
            y=mv(e['A'],V[x])
            for t in range(3):
                v=243*e['target']+enc([(a+t*b)%3 for a,b in zip(y,e['b'])]);assert v!=x
                providers[v].append({'center':x,'kind':'ordinary','port':p});image.add(v);O.add(v)
        offset=dot(normals[p],mv(e['A'],c))
        assert len(image)==81 and all(dot(normals[p],V[v%243])==offset for v in image)
        byport.append({'port':p,'target_fiber':e['target'],'size':81,'target_hyperplane_normal':normals[p],'target_hyperplane_constant':offset,'contains_target_zero':243*e['target'] in image})
    for x in centers:
        v=243*M['main_fiber_target'][0]+M['main_fiber_coordinate_maps'][0][x];providers[v].append({'center':x,'kind':'M'});MM.add(v)
        v=M['spare_vertex_map'][x]
        if v>=0:providers[v].append({'center':x,'kind':'P'});P.add(v)
    assert len(providers)==351 and len(O)==324 and len(MM)==27 and not O&MM and not P and max(map(len,providers.values()))==1
    ordinary_zeros=sorted(v for v in O if v%243==0);Mzeros=sorted(v for v in MM if v%243==0)
    if code==0:assert len(ordinary_zeros)==4
    else:assert len(ordinary_zeros)==1
    assert bool(Mzeros)==(code==2)
    phases.append({'phase_code':code,'phase_vector':c,'center_local_labels':centers,'old_union_size':351,'max_old_load':1,'ordinary_M_overlap':0,'P_image_count':0,'ordinary_zero_labels':ordinary_zeros,'ordinary_zero_target_fibers':[v//243 for v in ordinary_zeros],'M_zero_labels':Mzeros,'total_distinct_zero_targets':len(ordinary_zeros+Mzeros),'ordinary_target_hyperplanes':byport,'local_capacity_feasible':True})
result={'status':'ALL9_LOCAL_AFFINE_PHASES_VERIFIED','controller':0,'existing_H_basis':H,'phase_rule':'H+(c0,c1,0,0,0), c0,c1 inF3, phase_code=c0+3*c1','all_local_feasible_phases':9,'M_zero_phase_codes':[2],'M_zero_phase_locally_illegal':False,'phases_after_optional_M_zero_exclusion':[0,1,3,4,5,6,7,8],'nonzero_single_zero_preferred_phases':[1,3,4,5,6,7,8],'preferred_phase_count':7,'target_hyperplane_normals':normals,'phases':phases,'cross_source_necessary_condition':'At a shared target fiber, two ordinary81-point affine hyperplanes must have the same projective normal and different constants to be disjoint. Nonparallel normals force intersection of27 points. M27-point affine subsets and P exceptions additionally need exact capacity checks.','global_packings_checked':0,'other_fibers_checked':0,'source_BFS_runs':0,'new_graphs_generated':0,'solver_calls':0,'CPU_seconds':time.process_time()-T}
(D/'AFFINE_PHASE9_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='phases'}))
print('zero_table',json.dumps([{k:p[k] for k in ['phase_code','ordinary_zero_target_fibers','M_zero_labels','total_distinct_zero_targets']} for p in phases]))

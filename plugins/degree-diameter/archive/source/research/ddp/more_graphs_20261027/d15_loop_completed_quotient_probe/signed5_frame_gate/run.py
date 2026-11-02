"""One actual-source signed5-frame gate, with no target graph generation."""
from pathlib import Path
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(5,5))
START=time.process_time()
P=Path(__file__).resolve().parent
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_kernel_frame_or_signed_arc_numeric_tests']
assert not (P/'RESULT.json').exists()
table=json.loads((P.parent/'affine_relation_recovery/source15552_AFFINE_RELATIONS.json').read_text())
assert table['complete'] and (table['n'],table['dimension'],table['bin_size'])==(15552,4,81)
assert len(table['arcs'])==960 and all(not any(a['c']) for a in table['arcs'])

def rref(matrix,ncols):
    rows=[[x%3 for x in row] for row in matrix]
    pivots=[]
    at=0
    for column in range(ncols):
        pivot=next((i for i in range(at,len(rows)) if rows[i][column]),None)
        if pivot is None:
            continue
        rows[at],rows[pivot]=rows[pivot],rows[at]
        inverse=rows[at][column]
        rows[at]=[(inverse*x)%3 for x in rows[at]]
        for i in range(len(rows)):
            if i!=at and rows[i][column]:
                scale=rows[i][column]
                rows[i]=[(x-scale*y)%3 for x,y in zip(rows[i],rows[at])]
        pivots.append(column)
        at+=1
    return rows,pivots

def nullspace(matrix,ncols):
    reduced,pivots=rref(matrix,ncols)
    basis=[]
    for free in [i for i in range(ncols) if i not in pivots]:
        v=[0]*ncols
        v[free]=1
        for i,pivot in enumerate(pivots):
            v[pivot]=-reduced[i][free]%3
        basis.append(v)
    return reduced,pivots,basis

def normalized(v):
    inverse=next(x for x in v if x)
    return tuple(inverse*x%3 for x in v)

def rank_columns(columns):
    rows=[[column[i] for column in columns] for i in range(4)]
    return len(rref(rows,len(columns))[1])

def matvec(B,v):
    return tuple(sum(x*y for x,y in zip(row,v))%3 for row in B)

def invert4(matrix):
    rows=[row+[int(i==j) for j in range(4)] for i,row in enumerate(matrix)]
    for j in range(4):
        pivot=next(i for i in range(j,4) if rows[i][j])
        rows[j],rows[pivot]=rows[pivot],rows[j]
        inverse=rows[j][j]
        rows[j]=[x*inverse%3 for x in rows[j]]
        for i in range(4):
            if i!=j and rows[i][j]:
                scale=rows[i][j]
                rows[i]=[(x-scale*y)%3 for x,y in zip(rows[i],rows[j])]
    assert [row[:4] for row in rows]==[[int(i==j) for j in range(4)] for i in range(4)]
    return [row[4:] for row in rows]

by={a:[] for a in range(192)}
lookup={}
for arc_id,arc in enumerate(table['arcs']):
    by[arc['from']].append((arc_id,arc))
    lookup[(arc['from'],arc['to'])]=(arc_id,arc)
for arcs in by.values():
    arcs.sort(key=lambda x:x[1]['to'])
    assert len(arcs)==5
local_index={(a,arc['to']):i for a,arcs in by.items() for i,(_,arc) in enumerate(arcs)}
controllers=[]
failure=None
kernel_checks=0
frame_checks=0
arc_checks=0
signed=[]

for a in range(192):
    kernels=[]
    for i,(arc_id,arc) in enumerate(by[a]):
        reduced,pivots,basis=nullspace(arc['B'],4)
        kernel_checks+=1
        if len(pivots)!=3 or len(basis)!=1:
            failure={'gate':'INPUT_KERNEL_NOT_A_LINE','controller':a,'input_index':i,
                     'arc_id':arc_id,'target_controller':arc['to'],'B':arc['B'],
                     'rank':len(pivots),'kernel_basis':basis}
            break
        u=normalized(basis[0])
        reverse=lookup.get((arc['to'],a))
        if reverse is None or u!=normalized(reverse[1]['v']):
            failure={'gate':'INPUT_KERNEL_REVERSE_OUTPUT_DIRECTION_MISMATCH','controller':a,
                     'input_index':i,'arc_id':arc_id,'target_controller':arc['to'],
                     'B':arc['B'],'input_kernel':list(u),
                     'reverse_arc_output_v':None if reverse is None else reverse[1]['v']}
            break
        kernels.append(u)
    if failure:
        break
    for subset in itertools.combinations(range(5),4):
        rank=rank_columns([kernels[i] for i in subset])
        frame_checks+=1
        if rank!=4:
            failure={'gate':'FIVE_KERNEL_LINES_NOT_PROJECTIVE_FRAME','controller':a,
                     'targets_in_input_order':[arc['to'] for _,arc in by[a]],
                     'kernel_representatives':[list(u) for u in kernels],
                     'dependent_four_indices':list(subset),'dependent_four_rank':rank}
            break
    if failure:
        break
    kernel_matrix=[[u[row] for u in kernels] for row in range(4)]
    _,relation_pivots,relations=nullspace(kernel_matrix,5)
    assert len(relation_pivots)==4 and len(relations)==1
    alpha=list(normalized(relations[0]))
    assert all(alpha)
    frame=[tuple(alpha[i]*x%3 for x in kernels[i]) for i in range(5)]
    assert all(sum(f[row] for f in frame)%3==0 for row in range(4))
    T=[[f[row] for f in frame] for row in range(4)]
    first4=[row[:4] for row in T]
    controllers.append({'controller':a,'outgoing_target_order':[arc['to'] for _,arc in by[a]],
                        'input_kernel_lines':[list(u) for u in kernels],
                        'relation_alpha':alpha,'normalized_frame_columns':[list(v) for v in frame],
                        'T_4x5':T,'T_first4_inverse':invert4(first4)})

if failure is None:
    for a in range(192):
        fa=controllers[a]['normalized_frame_columns']
        for i,(arc_id,arc) in enumerate(by[a]):
            b=arc['to']
            j=local_index[(b,a)]
            fb=controllers[b]['normalized_frame_columns']
            v,pivot=arc['v'],arc['pivot']
            assert normalized(v)==normalized(controllers[b]['input_kernel_lines'][j])
            quotient=lambda y:tuple((y[h]-y[pivot]*v[h])%3 for h in range(4))
            target={}
            for ell in range(5):
                if ell==j:
                    continue
                y=quotient(fb[ell])
                assert any(y)
                key=normalized(y)
                assert key not in target
                target[key]=(ell,y)
            permutation=[None]*5
            permutation[i]=j
            scalars=[]
            pairs=[]
            for h in range(5):
                if h==i:
                    assert not any(matvec(arc['B'],fa[h]))
                    continue
                image=matvec(arc['B'],fa[h])
                key=normalized(image)
                if key not in target:
                    failure={'gate':'QUOTIENT_FRAME_PROJECTIVE_POINT_NOT_MATCHED',
                             'arc_id':arc_id,'from':a,'to':b,'input_index':i,'output_index':j,
                             'source_other_frame_index':h,'source_frame_vector':fa[h],
                             'B':arc['B'],'v':v,'B_source_frame_vector':list(image),
                             'target_quotient_frame_points':[
                                 {'target_index':ell,'vector':list(y)} for ell,y in target.values()]}
                    break
                ell,y=target[key]
                permutation[h]=ell
                component=next(z for z,x in enumerate(y) if x)
                mu=image[component]*y[component]%3
                assert mu in (1,2) and tuple(mu*x%3 for x in y)==image
                scalars.append(mu)
                pairs.append({'source_index':h,'target_index':ell,'mu':mu})
            if failure:
                break
            if len(set(permutation))!=5 or len(set(scalars))!=1:
                failure={'gate':'NO_BIJECTIVE_COMMON_SIGNED_FRAME_PERMUTATION',
                         'arc_id':arc_id,'from':a,'to':b,'input_index':i,'output_index':j,
                         'permutation':permutation,'scalar_checks':pairs}
                break
            arc_checks+=1
            signed.append({'arc_id':arc_id,'from':a,'to':b,'input_index':i,
                           'output_index':j,'permutation':permutation,
                           'mu_F3':scalars[0],'mu_sign':1 if scalars[0]==1 else -1})
        if failure:
            break

passed=failure is None
if passed:
    assert len(controllers)==192 and len(signed)==960
    recipe={'status':'COMPLETE_SIGNED5_FRAME_SOURCE_RECIPE','source_n':15552,
            'source_m':table['m'],'source_dimension':4,'controller_count':192,
            'frame_convention':'T_a maps e_i to f_ai; its kernel is the all-ones line inF3^5.',
            'arc_convention':'permutation maps input local frame index to output local frame index. B_ab*f_ai=mu*Q_v*f_b,pi(i), including the zero equality at the killed input index.',
            'controllers':controllers,'arcs':signed,
            'new_binary_graph_generated':False}
    (P/'SIGNED5_FRAME_RECIPE.json').write_text(json.dumps(recipe,ensure_ascii=False,indent=2)+'\n')
result={'status':'COMPLETE_SIGNED5_FRAME_PASS' if passed else 'FIRST_LITERAL_SIGNED5_FRAME_GATE_FAILURE',
        'prediction_status':'SUPPORTED' if passed else 'REFUTED',
        'source_n':15552,'source_m':table['m'],'kernel_arcs_checked':kernel_checks,
        'four_subset_frame_checks':frame_checks,'controllers_completed':len(controllers),
        'signed_arcs_checked':arc_checks,'first_failure':failure,
        'recipe_file':'SIGNED5_FRAME_RECIPE.json' if passed else None,
        'CPU_seconds':time.process_time()-START,'BFS':0,'solver_calls':0,'new_graphs':0,
        'scope':'Only the fixed actual15552 source and the unique prescribed frame normalization; no basis/frame search or binary target construction.'}
(P/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))

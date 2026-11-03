"""Profile all input-kernel matroids and, only on PASS, save intrinsic labels."""
from pathlib import Path
from collections import Counter
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(5,5))
START=time.process_time()
P=Path(__file__).resolve().parent
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_full_controller_matroid_profile']
assert not (P/'RESULT.json').exists()
table=json.loads((P.parent/'affine_relation_recovery/source15552_AFFINE_RELATIONS.json').read_text())
assert table['complete'] and (table['n'],table['bin_size'],table['dimension'])==(15552,81,4)

def rref(matrix,ncols):
    rows=[[x%3 for x in row] for row in matrix]
    pivots=[]
    at=0
    for j in range(ncols):
        pivot=next((i for i in range(at,len(rows)) if rows[i][j]),None)
        if pivot is None:
            continue
        rows[at],rows[pivot]=rows[pivot],rows[at]
        inv=rows[at][j]
        rows[at]=[x*inv%3 for x in rows[at]]
        for i in range(len(rows)):
            if i!=at and rows[i][j]:
                scalar=rows[i][j]
                rows[i]=[(x-scalar*y)%3 for x,y in zip(rows[i],rows[at])]
        pivots.append(j)
        at+=1
    basis=[]
    for free in (i for i in range(ncols) if i not in pivots):
        v=[0]*ncols
        v[free]=1
        for i,pivot in enumerate(pivots):
            v[pivot]=-rows[i][free]%3
        basis.append(v)
    return rows,pivots,basis

def normalized(v):
    scale=next(x for x in v if x)
    return tuple(scale*x%3 for x in v)

def columns_rank(columns):
    return len(rref([[c[i] for c in columns] for i in range(4)],len(columns))[1])

def encode(v):
    return sum(t*3**i for i,t in enumerate(v))

by={a:[] for a in range(192)}
lookup={}
for index,arc in enumerate(table['arcs']):
    by[arc['from']].append((index,arc))
    lookup[(arc['from'],arc['to'])]=(index,arc)
for arcs in by.values():
    arcs.sort(key=lambda item:item[1]['to'])
    assert len(arcs)==5
local_index={(a,arc['to']):i for a,arcs in by.items() for i,(_,arc) in enumerate(arcs)}
profile=[]
rank_hist=Counter()
support_hist=Counter()
first_failure=None
kernel_checks=0
for a in range(192):
    kernels=[]
    for i,(arc_id,arc) in enumerate(by[a]):
        _,pivots,basis=rref(arc['B'],4)
        kernel_checks+=1
        if len(pivots)!=3 or len(basis)!=1:
            first_failure={'gate':'INPUT_KERNEL_NOT_ONE_DIMENSIONAL','controller':a,
                           'arc_id':arc_id,'input_port_index':i,'B':arc['B'],
                           'B_rank':len(pivots),'kernel_basis':basis}
            break
        u=normalized(basis[0])
        reverse=lookup[(arc['to'],a)][1]
        assert u==normalized(reverse['v'])
        kernels.append(u)
    if len(kernels)!=5:
        break
    matrix=[[u[i] for u in kernels] for i in range(4)]
    reduced,pivots,relations=rref(matrix,5)
    rank=len(pivots)
    rank_hist[rank]+=1
    alpha=list(normalized(relations[0])) if len(relations)==1 else None
    support=[i for i,x in enumerate(alpha) if x] if alpha is not None else None
    support_hist[len(support) if support is not None else 'nonunique']+=1
    rec={'controller':a,'outgoing_target_order':[arc['to'] for _,arc in by[a]],
         'kernel_representatives':[list(u) for u in kernels],'kernel_span_rank':rank,
         'unique_relation':alpha,'dependence_support':support,
         'dependence_support_size':None if support is None else len(support)}
    profile.append(rec)
    if (rank!=4 or support is None or len(support)!=3) and first_failure is None:
        first_failure={'gate':'NOT_RANK4_WITH_UNIQUE_SUPPORT3_RELATION',**rec}

complete=len(profile)==192
passed=complete and first_failure is None
labels=[]
typed_arcs=[]
type_hist=Counter()
if passed:
    for rec in profile:
        a=rec['controller']
        kernels=rec['kernel_representatives']
        support=rec['dependence_support']
        axis=[i for i in range(5) if i not in support]
        p_basis=[kernels[support[0]],kernels[support[1]]]
        axes=[kernels[i] for i in axis]
        assert columns_rank(p_basis)==2
        assert columns_rank(p_basis+axes)==4
        assert columns_rank([kernels[i] for i in support])==2
        points={tuple((s*p_basis[0][j]+t*p_basis[1][j]+epsilon1*axes[0][j]+epsilon2*axes[1][j])%3 for j in range(4))
                for s,t in itertools.product(range(3),repeat=2)
                for epsilon1,epsilon2 in itertools.product((1,2),repeat=2)}
        assert len(points)==36
        offsets=sorted(encode(x) for x in points)
        original_labels=[81*a+x for x in offsets]
        labels.extend(original_labels)
        rec.update({'ternary_port_indices':support,'axis_port_indices':axis,
                    'port_types':['ternary' if i in support else 'axis' for i in range(5)],
                    'P_basis':p_basis,'axis_representatives':axes,
                    'direct_sum_basis_columns':p_basis+axes,
                    'local_offsets36':offsets,'original_labels36':original_labels})
    assert len(labels)==len(set(labels))==6912 and labels==sorted(labels)
    for a in range(192):
        for i,(arc_id,arc) in enumerate(by[a]):
            b=arc['to']
            j=local_index[(b,a)]
            left=profile[a]['port_types'][i]
            right=profile[b]['port_types'][j]
            type_hist[left+'->'+right]+=1
            typed_arcs.append({'arc_id':arc_id,'from':a,'to':b,
                               'input_port_index':i,'reverse_port_index':j,
                               'source_port_type':left,'target_reverse_port_type':right,
                               'types_match':left==right})
    pool={'status':'COMPLETE_INTRINSIC_MATROID36_ORIGINAL_LABEL_POOL',
          'source_n':15552,'source_m':table['m'],'source_bin_size':81,
          'controller_count':192,'points_per_controller':36,
          'hypothetical_induced_n':6912,'target_Delta':13,'target_D':4,
          'source_vertex_ids':labels,'new_label_order':'Ascending original vertex labels, zero-based position in source_vertex_ids.',
          'definition':'C_a=P_a+{+e1,-e1}+{+e2,-e2} in the original F3 coordinates; P_a is the rank2 span of the unique support3 dependence.',
          'controllers':profile,'typed_directed_quotient_arcs':typed_arcs,
          'type_pair_histogram':dict(type_hist),
          'induced_graph_generated':False,'actual_induced_max_degree':None,'actual_induced_D':None}
    (P/'LABEL_POOL.json').write_text(json.dumps(pool,ensure_ascii=False,indent=2)+'\n')
    (P/'source_vertex_ids.txt').write_text(' '.join(map(str,labels))+'\n')

result={'status':'COMPLETE_UNIFORM_SUPPORT3_LABEL_POOL' if passed else 'MATROID_PREDICTION_FAILED_NO_LABEL_POOL',
        'prediction_status':'SUPPORTED' if passed else 'REFUTED',
        'source_n':15552,'source_m':table['m'],'kernel_B_matrices_checked':kernel_checks,
        'controllers_profiled':len(profile),'complete_controller_profile':complete,
        'kernel_span_rank_histogram':dict(rank_hist),
        'unique_dependence_support_histogram':dict(support_hist),
        'first_failure':first_failure,'original_labels_selected':len(labels),
        'typed_directed_quotient_arc_histogram':dict(type_hist),
        'all_arc_end_types_match':all(a['types_match'] for a in typed_arcs) if passed else None,
        'label_pool':'LABEL_POOL.json' if passed else None,
        'actual_new_graph_n':None,'actual_new_graph_D':None,'actual_new_graph_max_degree':None,
        'CPU_seconds':time.process_time()-START,'BFS':0,'solver_calls':0,'new_graphs':0,
        'scope':'Only actual-source matroid profile and intrinsic original-label selection; degree and distance require a separate induced-graph computation.'}
(P/'PROFILE.json').write_text(json.dumps({'controllers':profile},ensure_ascii=False,indent=2)+'\n')
(P/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))

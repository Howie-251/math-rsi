"""Actual free fixedspaces and inversion groups; no balls or graph traversal."""
from pathlib import Path
import itertools
import json
import resource
import struct
import time

resource.setrlimit(resource.RLIMIT_CPU,(10,10))
START=time.process_time()
P=Path(__file__).resolve().parent
BASE=P.parent.parent
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_fixedspace_or_direction_numeric_check']

def rref_and_kernel(matrix,k):
    rows=[[v%3 for v in row] for row in matrix]
    pivots=[]
    at=0
    for column in range(k):
        pivot=next((i for i in range(at,len(rows)) if rows[i][column]),None)
        if pivot is None:
            continue
        rows[at],rows[pivot]=rows[pivot],rows[at]
        inv=rows[at][column]  # 1^-1=1 and 2^-1=2 in F3
        rows[at]=[(inv*x)%3 for x in rows[at]]
        for i in range(len(rows)):
            if i!=at and rows[i][column]:
                scale=rows[i][column]
                rows[i]=[(x-scale*y)%3 for x,y in zip(rows[i],rows[at])]
        pivots.append(column)
        at+=1
    free=[i for i in range(k) if i not in pivots]
    basis=[]
    for column in free:
        v=[0]*k
        v[column]=1
        for i,pivot in enumerate(pivots):
            v[pivot]=-rows[i][column]%3
        basis.append(v)
    return rows,pivots,basis

def encode(v):
    return sum(x*3**i for i,x in enumerate(v))

def normalized(v):
    scale=next(x for x in v if x)
    return tuple((scale*x)%3 for x in v)

def matvec(matrix,v):
    return [sum(a*b for a,b in zip(row,v))%3 for row in matrix]

def free_cache_labels(n):
    if n==15552:
        folder=BASE/'d15_D4_current15552/single_vertex_R3_cover'
        path=folder/'R3_MASKS.bin'
        labels=[]
        with path.open('rb') as stream:
            count,stored_n,words=struct.unpack('<III',stream.read(12))
            assert (count,stored_n,words)==(648,15552,243)
            for _ in range(count):
                labels.append(struct.unpack('<I',stream.read(4))[0])
                stream.seek(8*words,1)  # Skip ball contents; read only row labels.
            assert stream.tell()==path.stat().st_size
        meta={'file':str(path.relative_to(BASE)),'format':'12-byte LEu32 header648,15552,243; each row labelLEu32 then243LEu64 words',
              'radius':3,'words_per_ball':243,'row_stride_bytes':1948,'first_ball_word_byte_offset':16}
    else:
        assert n==102060
        folder=BASE/'d15_D5_current102060_source/monotone_R4_cover'
        labels=[int(x) for x in (folder/'eligible.txt').read_text().split()]
        assert len(labels)==810
        pre=json.loads((folder/'PREFLIGHT.json').read_text())
        assert labels==pre['eligible_labels']
        meta={'file':str((folder/'radius4.u64le.bin').relative_to(BASE)),
              'row_labels':str((folder/'eligible.txt').relative_to(BASE)),
              'format':'810 rows1595LEu64; bit t is old vertex t;44 meaningful bits in last word',
              'radius':4,'words_per_ball':1595,'row_stride_bytes':12760,'first_ball_word_byte_offset':0}
    assert len(labels)==len(set(labels))
    return labels,meta

summaries=[]
merge={}
for label,n,diameter,expected_controllers in [('source15552',15552,4,24),('source102060',102060,5,30)]:
    began=time.process_time()
    table=json.loads((P.parent/'affine_relation_recovery'/f'{label}_AFFINE_RELATIONS.json').read_text())
    assert table['complete'] and table['n']==n
    assert all(not any(arc['c']) for arc in table['arcs'])
    k,q=table['dimension'],table['bin_size']
    labels,cache=free_cache_labels(n)
    label_to_row={vertex:i for i,vertex in enumerate(labels)}
    digits=[[x//3**i%3 for i in range(k)] for x in range(q)]
    neg=[encode([(-t)%3 for t in v]) for v in digits]
    arcs=sorted((a for a in table['arcs'] if a['from']==a['to']),key=lambda a:a['from'])
    assert len(arcs)==expected_controllers
    controllers=[]
    groups=[]
    all_free=set()
    for arc in arcs:
        a=arc['from']
        B,v,j=arc['B'],arc['v'],arc['pivot']
        assert v[j]==1 and all(row==0 for row in B[j])
        Q=[[(int(i==ell)-v[i]*int(ell==j))%3 for ell in range(k)] for i in range(k)]
        minusI=[[(B[i][ell]-int(i==ell))%3 for ell in range(k)] for i in range(k)]
        equation=[[sum(Q[i][h]*minusI[h][ell] for h in range(k))%3 for ell in range(k)] for i in range(k)]
        assert equation==[[(B[i][ell]-Q[i][ell])%3 for ell in range(k)] for i in range(k)]
        reduced,pivots,basis=rref_and_kernel(equation,k)
        dimension=len(basis)
        assert dimension==3
        points={tuple(sum(coeff[h]*basis[h][i] for h in range(dimension))%3 for i in range(k))
                for coeff in itertools.product(range(3),repeat=dimension)}
        assert len(points)==27 and all(not any(matvec(equation,x)) for x in points)
        actual_free={vertex for vertex in labels if vertex//q==a}
        predicted_free={a*q+encode(x) for x in points}
        assert predicted_free==actual_free and len(actual_free)==27
        assert not (all_free&predicted_free)
        all_free.update(predicted_free)
        directions=sorted({normalized(x) for x in points if any(x)})
        assert len(directions)==13
        canonical=normalized(v)
        assert canonical in directions
        canonical_index=directions.index(canonical)
        controller_groups=[]
        zero=a*q
        singleton={'variable':len(groups)+1,'group_index0':len(groups),'controller':a,
                   'kind':'zero_singleton','pins':[zero],'cost':1,
                   'ball_row_indices':[label_to_row[zero]],'in_old_canonical_selfline_domain':True}
        groups.append(singleton)
        controller_groups.append(singleton['variable'])
        records=[]
        for di,d in enumerate(directions):
            offset=encode(d)
            partner=neg[offset]
            pins=[a*q+offset,a*q+partner]
            iscanonical=di==canonical_index
            group={'variable':len(groups)+1,'group_index0':len(groups),'controller':a,
                   'kind':'nonzero_inversion_pair','direction_index':di,'direction':list(d),
                   'pins':pins,'cost':2,'ball_row_indices':[label_to_row[p] for p in pins],
                   'in_old_canonical_selfline_domain':iscanonical}
            groups.append(group)
            controller_groups.append(group['variable'])
            records.append({'direction_index':di,'normalized_vector':list(d),'local_offsets':[offset,partner],
                            'pins':pins,'ball_row_indices':group['ball_row_indices'],
                            'group_variable':group['variable'],'is_old_canonical_direction':iscanonical})
        controllers.append({'controller':a,'self_arc_B':B,'self_arc_v':v,'pivot':j,
                            'Q_v':Q,'fixedspace_equation':equation,'fixedspace_RREF':reduced,
                            'equation_rank':len(pivots),'fixedspace_dimension':dimension,
                            'fixedspace_basis':basis,'local_free_offsets27':sorted(encode(x) for x in points),
                            'actual_free_pins27':sorted(predicted_free),
                            'direction_count':13,'canonical_direction_index':canonical_index,
                            'directions':records,'group_variables':controller_groups})
    assert all_free==set(labels)
    flatten=[pin for group in groups for pin in group['pins']]
    assert len(flatten)==len(set(flatten))==len(labels) and set(flatten)==set(labels)
    assert len(groups)==14*len(arcs) and sum(g['cost'] for g in groups)==len(labels)
    interface={'status':'COMPLETE_LITERAL_FREE_FIXEDSPACE_AND_INVERSION_PARTITION',
               'source':label,'n':n,'m':table['m'],'D':diameter,'Delta':15,'bin_size':q,'dimension':k,
               'controller_count':table['controller_count'],'loop_controller_count':len(arcs),
               'free_pin_count':len(labels),'group_count':len(groups),
               'group_variable_base':1,'group_index0_base':0,'ball_row_indices_base':0,
               'groups_partition_all_actual_free':True,
               'literal_free_ball_row_order':labels,'cache':cache,
               'global_inversion':'vertex a*q+x maps to a*q+neg_local_offsets[x]',
               'neg_local_offsets':neg,
               'inversion_automorphism_reason':'Every certified directed relation has c=0, so simultaneous input/output negation preserves it. Removing its virtual diagonal loops commutes with negation.',
               'controllers':controllers,'groups':groups,
               'coverage_computed':False,'BFS_ball_OR_solver_or_graph_runs':0,
               'CPU_seconds':time.process_time()-began}
    outname=f'{label}_FREE_DIRECTION_GROUPS.json'
    (P/outname).write_text(json.dumps(interface,ensure_ascii=False,indent=2)+'\n')
    summary={key:interface[key] for key in ['source','n','m','D','bin_size','dimension','loop_controller_count','free_pin_count','group_count','groups_partition_all_actual_free','CPU_seconds']}
    summary.update({'fixedspace_dimension_per_controller':3,'free_points_per_controller':27,
                    'projective_directions_per_controller':13,'canonical_directions_per_controller':1,
                    'new_directions_per_controller':12,'new_noncanonical_free_pins':len(arcs)*24,
                    'singleton_groups':len(arcs),'pair_groups':len(arcs)*13,'interface_file':outname})
    summaries.append(summary)
    merge[label]={
        'scope':'Fixed-coordinate free-space recovery on every self-controller arc of the already certified actual source; exact partition of all actual free-cache labels.',
        'failure_or_result':f"SUPPORTED: {len(arcs)} selfarcs each have a3-dimensional27-point free kernel and13 projective directions; all{len(labels)} actual free labels match; one old canonical direction and12 new directions per controller.",
        'lesson_and_restart_condition':'The old canonical selfline domain is only one direction per free kernel. The expanded inversion-group interface is complete for all free ports, but target coverage or construction existence is not tested by this recovery.',
        'unclosed_gap':'A degree-budget15 inversion-invariant all-target cover is a separate producer problem; no numerical coverage prediction is certified here.',
        'other_metrics':summary,
        'report_paths':[str(P.relative_to(BASE.parent.parent.parent)/'PREDICTION.json'),
                        str(P.relative_to(BASE.parent.parent.parent)/'run.py'),
                        str(P.relative_to(BASE.parent.parent.parent)/outname)]
    }
result={'status':'COMPLETE_TWO_SOURCE_FREE_DIRECTION_RECOVERY','primary_prediction_status':'SUPPORTED',
        'coverage_prediction_status':'NOT_TESTED_HERE_PRODUCER_OWNED',
        'sources':summaries,'CPU_seconds':time.process_time()-START,
        'new_balls':0,'source_BFS':0,'cached_ball_OR':0,'solver_calls':0,'new_graphs':0}
(P/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(P/'RAW_ANALYSIS_FIELDS.json').write_text(json.dumps(merge,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))

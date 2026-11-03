"""Recover only the fixed-coordinate affine relations; no graph traversal."""
from array import array
from pathlib import Path
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU,(10,10))
START=time.process_time()
P=Path(__file__).resolve().parent
BASE=P.parent.parent
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_numeric_affine_relation_recovery']
previous=json.loads((P.parent/'RESULT.json').read_text())
assert all(s['complete_equitable'] for s in previous['sources'])
assert sys.byteorder=='little'

def recover(label,n,m,k,row,input_path):
    began=time.process_time()
    q=3**k
    digits=[[(x//(3**i))%3 for i in range(k)] for x in range(q)]
    powers=[3**i for i in range(k)]
    add=[[sum(((digits[x][i]+digits[y][i])%3)*powers[i] for i in range(k)) for y in range(q)] for x in range(q)]
    neg=[sum(((-digits[x][i])%3)*powers[i] for i in range(k)) for x in range(q)]
    sub=[[add[x][neg[y]] for y in range(q)] for x in range(q)]
    scalar=[[0]*q,list(range(q)),neg]
    previous_input=[0]*q
    input_column=[0]*q
    for x in range(1,q):
        i=next(i for i,t in enumerate(digits[x]) if t)
        previous_input[x]=x-powers[i]
        input_column[x]=i
    arcs=[]
    failure=None
    rows_compared=0
    loops=0
    completed_controllers=0
    for a in range(n//q):
        groups=[]
        for x in range(q):
            vertex=a*q+x
            neighbors=row(vertex)
            bybin={}
            for w in neighbors:
                b,y=divmod(w,q)
                bybin.setdefault(b,[]).append(y)
            if len(neighbors)==14:
                bybin.setdefault(a,[]).append(x)
                loops+=1
            assert len(bybin)==5 and all(len(ys)==3 for ys in bybin.values())
            groups.append({b:tuple(sorted(ys)) for b,ys in bybin.items()})
        targets=sorted(groups[0])
        assert all(sorted(g)==targets for g in groups)
        for b in targets:
            origin=groups[0][b]
            direction=sub[origin[1]][origin[0]]
            assert direction
            pivot=next(i for i,t in enumerate(digits[direction]) if t)
            # 1 and 2 are their own inverses in F3.
            v=scalar[digits[direction][pivot]][direction]
            assert digits[v][pivot]==1
            quotient=[sub[y][scalar[digits[y][pivot]][v]] for y in range(q)]
            c=quotient[origin[0]]
            columns=[sub[quotient[groups[powers[i]][b][0]]][c] for i in range(k)]
            expected=[c]*q
            for x in range(1,q):
                expected[x]=add[expected[previous_input[x]]][columns[input_column[x]]]
            twice=neg[v]
            for x in range(q):
                fit=tuple(sorted((expected[x],add[expected[x]][v],add[expected[x]][twice])))
                actual=groups[x][b]
                rows_compared+=1
                if fit!=actual:
                    local_line=tuple(sorted((actual[0],add[actual[0]][v],add[actual[0]][twice])))
                    failure={
                        'source_controller':a,'target_controller':b,'local_input':x,
                        'input_digits':digits[x],'source_vertex':a*q+x,
                        'kind':'PARALLEL_LINE_FAILURE' if local_line!=actual else 'AFFINE_INPUT_MAP_FAILURE',
                        'row0_outputs':origin,'actual_local_outputs':actual,'candidate_local_outputs':fit,
                        'direction_v':digits[v],'pivot':pivot,'constant_c':digits[c],
                        'B_rows':[[digits[columns[i]][j] for i in range(k)] for j in range(k)]
                    }
                    break
            if failure:
                break
            assert all(digits[c][pivot]==0 and digits[col][pivot]==0 for col in columns)
            arcs.append({'from':a,'to':b,'pivot':pivot,'v':digits[v],'c':digits[c],
                         'B':[[digits[columns[i]][j] for i in range(k)] for j in range(k)],
                         'v_offset':v,'c_offset':c,'column_offsets':columns})
        if failure:
            break
        completed_controllers+=1
    success=failure is None
    if success:
        assert len(arcs)==5*(n//q) and rows_compared==5*n
    table={'source':label,'n':n,'m':m,'dimension':k,'bin_size':q,'controller_count':n//q,
           'coordinate_convention':'Local offset=sum_i digit_i*3^i, arithmetic in F3.',
           'relation':'(a,x) has directed completed neighbors (b,B*x+c+t*v) for t=0,1,2.',
           'remove_virtual_loops':'Remove an output only when its entire vertex label equals the input label (same controller and local offset).',
           'complete':success,'arcs':arcs}
    filename=f'{label}_AFFINE_RELATIONS.json'
    (P/filename).write_text(json.dumps(table,ensure_ascii=False,separators=(',',':'))+'\n')
    return {'source':label,'n':n,'m':m,'dimension':k,'bin_size':q,'controller_count':n//q,
            'input':input_path,'complete_affine_relation_certificate':success,
            'status':'ALL_LITERAL_ROWS_MATCH_AFFINE_LINE_RELATIONS' if success else 'FIRST_FIXED_COORDINATE_ARC_COUNTEREXAMPLE',
            'directed_arcs_verified':len(arcs),'arc_rows_compared':rows_compared,
            'controllers_completed':completed_controllers,'virtual_selfloops_seen':loops,
            'original_graph_exactly_reconstructible':success,'first_counterexample':failure,
            'relation_table':filename,'CPU_seconds':time.process_time()-began}

out=[]
source=BASE/'d15_D4_current15552/source15552.header.edges'
g=[[] for _ in range(15552)]
with source.open() as f:
    n,m=map(int,next(f).split())
    assert (n,m)==(15552,116316)
    for line in f:
        a,b=map(int,line.split())
        g[a].append(b)
        g[b].append(a)
assert sum(map(len,g))==2*m
out.append(recover('source15552',n,m,4,lambda v:g[v],str(source.relative_to(BASE))))
del g
source=BASE/'d15_D5_current102060_source/monotone_R4_cover/source.csr.u32le.bin'
data=array('I');data.frombytes(source.read_bytes())
n,nadj=data[0],data[1]
assert (n,nadj)==(102060,1530090) and len(data)==n+3+nadj
begin=n+3
def row(v):
    return data[begin+data[2+v]:begin+data[3+v]]
out.append(recover('source102060',n,nadj//2,5,row,str(source.relative_to(BASE))))
result={'status':'COMPLETE_TWO_FIXED_COORDINATE_RECOVERY_CHECKS',
        'prediction_status':'SUPPORTED' if all(s['complete_affine_relation_certificate'] for s in out) else 'REFUTED_FOR_AT_LEAST_ONE_SOURCE',
        'sources':out,'source_adjacency_modified':False,
        'scope':'Exact literal affine relations for the prescribed local coordinates and virtual-loop completion. Reported source diameter remains inherited; no new graph or distance claim.',
        'graph_distance_ball_or_solver_runs':0,'source_reads_per_input':1,
        'CPU_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))

#!/usr/bin/env python3
"""Prepare strengthened shared-route CNF; never invoke its main solver."""
from pathlib import Path
from array import array
import argparse
import json
import shutil
import time

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'f5_induced_retention_closure'
SUPPORT=HERE.parent/'f5_induced_support_closure'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--prepare-only',action='store_true',required=True)
    parser.parse_args()
    assert not (HERE/'MODEL.json').exists(), 'This preparation has already completed.'
    start=time.process_time()
    support_check=json.loads((HERE/'SUPPORT_CHECK_RESULT.json').read_text())
    assert support_check['status']=='RAW_UNSAT_COUNTEREXAMPLE_ATTACK_PASS'
    old_model=json.loads((OLD/'MODEL.json').read_text())
    assert (old_model['variables'],old_model['clauses'])==(300221,1170873)
    paths=json.loads((OLD/'CONTROLLER_UNIQUE_WORDS.json').read_text())
    assert len(paths)==258
    params=json.loads((HERE.parent/'f5_full_d20_D3/PARAMETERS.json').read_text())
    ctl=params['controller']
    raw=array('H')
    with (HERE.parent/'f5_induced_hyperplane3000/source_adjacency.u16.bin').open('rb') as f:
        raw.fromfile(f,3750*20)
    adj=[list(raw[20*v:20*v+20]) for v in range(3750)]
    # Restore, rather than regenerate, all original OR flag IDs. Order must
    # match the old loop: saved word order, z increasing, left flag then right.
    old_flags={};nextvar=3750+273750+18731
    assert nextvar==296231
    def restore(ids):
        nonlocal nextvar
        key=tuple(sorted(ids))
        if key not in old_flags:
            nextvar+=1;old_flags[key]=nextvar
        return old_flags[key]
    for path in paths:
        u,a,b,v=path['vertices']
        for z in range(125*a,125*(a+1)):
            left=[x for x in adj[z] if x//125==u]
            mids=[x for x in adj[z] if x//125==b]
            right={y for w in mids for y in adj[w] if y//125==v}
            assert len(left)==5 and len(right)==25
            restore(left);restore(right)
    assert nextvar==300221 and len(old_flags)==3990
    assert sum(len(k)==5 for k in old_flags)==3000
    assert sum(len(k)==25 for k in old_flags)==990
    witness=old_model['literal_controlled_counterexample_clause']
    assert old_flags[tuple(witness['left_old_ids'])]==witness['left_OR_variable']==296262
    assert old_flags[tuple(witness['right_old_ids'])]==witness['right_OR_variable']==296263
    (HERE/'RESTORED_OR_FLAGS.json').write_text(json.dumps([
        {'old_ids':list(key),'flag':flag} for key,flag in old_flags.items()
    ],separators=(',',':'))+'\n')
    restored_cpu=time.process_time()-start
    external=[]
    for u in range(30):
        for p,v in enumerate(ctl[u]):
            if not set(ctl[u]).intersection(ctl[v]):external.append((u,v,p))
    assert len(external)==60
    new_flags={};extra_clauses=0;groups=0;literal_example=None
    tail=HERE/'shared_routes.added.cnf'
    with tail.open('w') as out,(HERE/'SHARED_ROUTE_GROUPS.jsonl').open('w') as records:
        def emit(literals):
            nonlocal extra_clauses
            out.write(' '.join(map(str,literals))+' 0\n');extra_clauses+=1
        def or4(ids):
            nonlocal nextvar
            key=tuple(sorted(ids));assert len(key)==4
            if key not in new_flags:
                nextvar+=1;new_flags[key]=nextvar
                for x in key:emit([-(x+1),nextvar])
                emit([-nextvar,*[x+1 for x in key]])
            return new_flags[key]
        for u,v,p in external:
            for q in range(4):
                if q==p:continue
                a=ctl[u][q]
                for w in range(125*u,125*(u+1)):
                    Y=tuple(x for x in adj[w] if x//125==v)
                    Z=tuple(x for x in adj[w] if x//125==a)
                    assert len(Y)==len(Z)==5
                    # Literal inverse q-neighborhood is the complete source pencil line.
                    line=tuple(x for x in adj[Z[0]] if x//125==u)
                    assert len(line)==5 and w in line
                    L=tuple(x for x in line if x!=w)
                    assert Y in old_flags and Z in old_flags
                    lf,yf,zf=or4(L),old_flags[Y],old_flags[Z]
                    clause1=[w+1,-lf,-yf];clause2=[zf,-lf,-yf]
                    emit(clause1);emit(clause2);groups+=1
                    records.write(json.dumps({'u':u,'v':v,'p':p,'q':q,'w':w,
                                              'L_flag':lf,'Y_flag':yf,'Z_flag':zf},separators=(',',':'))+'\n')
                    if (u,v,p,q,w)==(0,20,1,0,0):
                        assert L==(1,2,3,4) and Y==tuple(range(2500,2505))
                        assert Z==(2250,2255,2260,2265,2270)
                        literal_example={'u':u,'v':v,'p':p,'q':q,'w':w,
                            'L':L,'Y':Y,'Z':Z,'L_flag':lf,'Y_flag':yf,'Z_flag':zf,
                            'clauses':[clause1,clause2]}
        assert groups==22500 and len(new_flags)==15000
        assert nextvar==315221 and extra_clauses==120000
        # Primary justification is the complete closure enumeration + projection
        # and density proofs. The small SAT check is only a separate attack.
        for u in range(30):emit(list(range(125*u+1,125*(u+1)+1)))
    assert extra_clauses==120030 and literal_example is not None
    (HERE/'NEW_OR4_FLAGS.json').write_text(json.dumps([
        {'old_ids':list(key),'flag':flag} for key,flag in new_flags.items()
    ],separators=(',',':'))+'\n')
    with (HERE/'model.cnf').open('w') as out,(OLD/'model.cnf').open() as base,tail.open() as additions:
        assert base.readline().split()==['p','cnf','300221','1170873']
        out.write(f'p cnf {nextvar} {old_model["clauses"]+extra_clauses}\n')
        shutil.copyfileobj(base,out);shutil.copyfileobj(additions,out)
    model={'status':'PREPARED_NOT_SOLVED','variables':nextvar,
        'clauses':old_model['clauses']+extra_clauses,
        'keep_variables':3750,'keep_variable_rule':'old vertex v has DIMACS variable v+1',
        'n_at_least':1921,'n_exactly_fixed':False,'max_degree':16,
        'parent_base_variables':300221,'parent_base_clauses':1170873,
        'parent_base_rebuilt':False,'parent_base_path':str(OLD/'model.cnf'),
        'old_OR_flag_previous_variable':296231,'old_OR_flag_final_variable':300221,
        'restored_OR5_count':3000,'restored_OR25_count':990,
        'old_literal_flag_calibration':[296262,296263],
        'external_directed_controller_edges':external,
        'shared_route_groups':groups,'shared_route_clauses':45000,
        'new_exact_OR4_flags':len(new_flags),'new_exact_OR4_binding_clauses':75000,
        'all_nonempty_fiber_clauses':30,
        'all_nonempty_fiber_basis':{
            'closed_support_enumeration':str(SUPPORT/'REPORT.md'),
            'six_large_proper_supports':str(SUPPORT/'LARGE_PROPER_SUPPORTS.json'),
            'size16_projection_exclusion':str(SUPPORT/'PROJECTION_RESULT.json'),
            'size19_density_matching_bound':str(SUPPORT/'DENSITY_RESULT.json'),
            'density_lemma':str(SUPPORT/'DENSITY_LEMMA.md'),
            'review_status':'Root and degree5 paper PASS; raw SAT attack is supplementary only'},
        'literal_shared_route_example':literal_example,
        'necessary_only':True,'SAT_requires_actual_induced_D3_check':True,
        'restoration_CPU_seconds':restored_cpu,'CPU_seconds':time.process_time()-start,
        'prior_stage_CPU_seconds':support_check['aggregate_CPU_seconds'],
        'source_cache_reads':1,'source_edge_text_reads':0,'BFS_runs':0,
        'main_solver_calls':0,'graphs_generated':0,
        'main_solver_CPU_budget':120,'main_whole_CPU_budget':150,
        'main_max_calls':4,'main_first_window':60,'pending':['root_code_review_before_main_solver']}
    assert model['clauses']==1290903
    (HERE/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
    print(json.dumps({k:model[k] for k in ['status','variables','clauses','shared_route_groups',
        'new_exact_OR4_flags','all_nonempty_fiber_clauses','CPU_seconds']}),flush=True)

if __name__=='__main__':main()

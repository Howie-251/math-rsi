#!/usr/bin/env python3
"""Prepare-only C25 motif completion with exact NB2/NB3 multiplicity gates."""
import argparse
import itertools
import json
import os
from pathlib import Path
import resource
import shutil
import time

HERE=Path(__file__).resolve().parent
START=time.process_time()
WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(20,21))
N=25

def save(name,value):
    (HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only',required=True,action='store_true')
    parser.parse_args()
    assert not (HERE/'PREPARE_HANDLE.json').exists(),'This preparation has already started.'
    save('PREPARE_HANDLE.json',dict(status='PREPARING_ONLY',pid=os.getpid(),running=True,CPU_budget=20))
    print(json.dumps(dict(status='PREPARING_ONLY',pid=os.getpid())),flush=True)
    triangles=[(0,1,2),(2,3,4),(4,5,6)]+[tuple(range(7+3*b,10+3*b)) for b in range(6)]
    fixed={tuple(sorted(e)) for tri in triangles for e in itertools.combinations(tri,2)}
    fixed_degrees=[sum(v in e for e in fixed) for v in range(N)]
    free=[v for v in range(N) if fixed_degrees[v]==2]
    assert len(fixed)==27 and len(free)==23
    assert [v for v in range(N) if fixed_degrees[v]==4]==[2,4]
    scope=dict(controller_order=N,triangles=triangles,fixed_edges=sorted(fixed),
        fixed_degrees=fixed_degrees,free_vertices=free,centers_without_extra_edges=[2,4],
        additional_degree={str(v):2 for v in free},required_extra_edges=23,required_total_edges=50,
        fiber={'field':5,'dimension':3,'kept':'z != 0 and x-y != 0','size':80},
        target_order=2000,target_max_degree=16,target_diameter=3,
        target_graph_generated=False,charts_constructed=False,
        necessary_controller_conditions_only=True,canonicalization=None,
        local_triangle_fourcycle_cuts=False,nontriangle_edge_fourcycle_cut=True)
    save('INPUT_SCOPE.json',scope)

    variables=clauses=literals=0
    and_cache={}
    or_cache={}
    body=HERE/'clauses.body'
    with body.open('w') as stream:
        def fresh():
            nonlocal variables
            variables+=1
            return variables
        def neg(x):
            return not x if isinstance(x,bool) else -x
        def clause(xs):
            nonlocal clauses,literals
            if any(x is True for x in xs):return
            xs=[x for x in xs if x is not False]
            stream.write(' '.join(map(str,xs))+' 0\n')
            clauses+=1
            literals+=len(xs)
        def conjunction(xs):
            if any(x is False for x in xs):return False
            key=tuple(sorted(set(x for x in xs if x is not True)))
            if not key:return True
            if len(key)==1:return key[0]
            if key not in and_cache:
                z=fresh()
                and_cache[key]=z
                for x in key:clause([-z,x])
                clause([z]+[-x for x in key])
            return and_cache[key]
        def disjunction(xs):
            if any(x is True for x in xs):return True
            key=tuple(sorted(set(x for x in xs if x is not False)))
            if not key:return False
            if len(key)==1:return key[0]
            if key not in or_cache:
                z=fresh()
                or_cache[key]=z
                clause([-z]+list(key))
                for x in key:clause([z,-x])
            return or_cache[key]
        def one_and_two(xs):
            # Count distinct word occurrences, not distinct gate literals.
            # Saturated counts of disjoint word lists combine exactly:
            # one=L1 OR R1; two=L2 OR R2 OR (L1 AND R1).
            stage=[(x,False) for x in xs if x is not False]
            if not stage:return False,False
            while len(stage)>1:
                next_stage=[]
                for j in range(0,len(stage),2):
                    if j+1==len(stage):next_stage.append(stage[j]);continue
                    l1,l2=stage[j];r1,r2=stage[j+1]
                    one=disjunction([l1,r1])
                    two=disjunction([l2,r2,conjunction([l1,r1])])
                    next_stage.append((one,two))
                stage=next_stage
            return stage[0]

        edge_variables={e:fresh() for e in itertools.combinations(free,2) if e not in fixed}
        assert len(edge_variables)==233
        def adj(u,v):
            if u==v:return False
            e=tuple(sorted((u,v)))
            return True if e in fixed else edge_variables.get(e,False)
        save('EDGE_VARIABLES.json',[dict(edge=e,var=v) for e,v in edge_variables.items()])

        for u in free:
            xs=[var for edge,var in edge_variables.items() if u in edge]
            # At least two: at least one, and each chosen literal requires another.
            clause(xs)
            for j,x in enumerate(xs):clause([-x]+xs[:j]+xs[j+1:])
            # At most two: the same forward threshold encoding as the C31 model.
            previous=None
            for x in xs:
                one,two=fresh(),fresh()
                clause([-x,one])
                if previous is None:clause([-two])
                else:
                    p1,p2=previous
                    clause([-p1,one]);clause([-p2,two])
                    clause([-x,-p1,two]);clause([-x,-p2])
                previous=one,two
        degree_variables=variables
        degree_clauses=clauses

        pair_records=[]
        total_possible_nb3=0
        total_nb2_terms=0
        for u,v in itertools.combinations(range(N),2):
            adjacency=adj(u,v)
            if adjacency is True:
                pair_records.append(dict(u=u,v=v,fixed_adjacent=True,route_clauses_vacuous=True))
                continue
            twos=[]
            for a in range(N):
                if a in (u,v):continue
                term=conjunction([adj(u,a),adj(a,v)])
                if term is not False:twos.append([a,term])
            nb2=disjunction([term for a,term in twos])
            words=[]
            for a in range(N):
                if a in (u,v) or adj(u,a) is False:continue
                for b in range(N):
                    if b in (u,v,a):continue
                    term=conjunction([adj(u,a),adj(a,b),adj(b,v)])
                    if term is not False:words.append([a,b,term])
            nb3_one,nb3_two=one_and_two([term for a,b,term in words])
            clause([adjacency,nb3_one])
            clause([adjacency,nb2,nb3_two])
            # Together with the first clause, this is edge -> (triangle or C4).
            # NB3 words have four distinct vertices, so an adjacent endpoint pair
            # plus such a path is an actual C4, not a backtracking walk.
            clause([nb2,nb3_one])
            total_possible_nb3+=len(words)
            total_nb2_terms+=len(twos)
            pair_records.append(dict(u=u,v=v,fixed_adjacent=False,adjacency_literal=adjacency,
                NB2_flag=nb2,NB3_atleast1_flag=nb3_one,NB3_atleast2_flag=nb3_two,
                NB2_terms=twos,NB3_words=words))

    with (HERE/'model.cnf').open('w') as out:
        out.write(f'p cnf {variables} {clauses}\n')
        with body.open() as inp:shutil.copyfileobj(inp,out,1024*1024)
    save('PAIR_ROUTE_GATES.json',dict(path_encoding='u,a,b,v all distinct; each term iff all three edges',
        threshold_encoding='balanced exact saturated count of distinct path occurrences',pairs=pair_records))
    elapsed=time.process_time()-START
    model=dict(status='C25_FIXED_MOTIF_NB2_NB3_CAPACITY_CNF_PREPARED_NOT_SOLVED',pid=os.getpid(),
        controller_order=N,fixed_edges=27,free_vertices=23,extra_edge_variables=233,
        selected_extra_edges=23,expected_total_edges=50,degree=4,
        all_variables=variables,clauses=clauses,literal_occurrences=literals,
        degree_stage_variables=degree_variables,degree_stage_clauses=degree_clauses,
        distinct_AND_gates=len(and_cache),distinct_OR_gates=len(or_cache),
        unordered_pairs=300,fixed_adjacent_pairs_skipped=27,pairs_with_route_conditions=273,
        symbolic_NB2_terms=total_nb2_terms,symbolic_NB3_path_occurrences=total_possible_nb3,
        conditions=['adj(u,v) OR NB3count(u,v)>=1','adj(u,v) OR NB2exists(u,v) OR NB3count(u,v)>=2',
                    'NB2exists(u,v) OR NB3count(u,v)>=1'],
        same_vertex_triangle_condition='Every vertex lies in a fixed motif triangle',
        complete_fixed_motif_completions=True,canonicalization=False,
        local_cycle_cuts=False,nontriangle_edge_C4_cut=True,
        controller_conditions_are_necessary_not_sufficient_for_fiber80=True,
        source_module='controller31_chain_full/run_once.py: motif/adj/Tseitin/exact-extra2 logic only',
        formula='model.cnf',edge_variable_map='EDGE_VARIABLES.json',scope='INPUT_SCOPE.json',
        route_gate_metadata='PAIR_ROUTE_GATES.json',
        prepare_CPU_seconds=elapsed,prepare_wall_seconds=time.monotonic()-WALL,prepare_CPU_budget=20,
        solver_calls=0,graphs_generated=0,large_graph_BFS=0,charts_constructed=False,
        planned_control_solver_CPU_seconds=60,max_planned_solver_calls=1,UNKNOWN_policy='stop',
        running=False,pending=['Root mathematical and code review before any solver call'])
    assert elapsed<20
    save('MODEL.json',model);save('PREPARE_TERMINAL.json',model);save('PREPARE_HANDLE.json',model)
    print(json.dumps(model),flush=True)

if __name__=='__main__':main()

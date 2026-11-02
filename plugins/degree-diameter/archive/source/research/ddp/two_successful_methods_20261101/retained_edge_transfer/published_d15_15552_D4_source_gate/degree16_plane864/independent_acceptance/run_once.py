"""One fresh final16416 acceptance suite; no retry or source-D4 suite."""
import time
START=time.process_time();WALL=time.time()
import json,math,os,resource,subprocess
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
assert not (D/'TERMINAL.json').exists(), 'Acceptance is already terminal; no restart.'
BUDGET=120.
PREP=json.loads((D/'PREPARATION.json').read_text())['CPU_seconds']
INITIAL=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return PREP+time.process_time()-START+r.ru_utime+r.ru_stime-INITIAL.ru_utime-INITIAL.ru_stime
def save(name,value):(D/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
source=ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
candidate=D.parent/'graph_d16_D4_n16416.edges'
steps=[];phase='producer_preflight'
try:
    assert source.is_file() and candidate.is_file(), 'Await actual graph; do not start missing-input suite'
    term=json.loads((D.parent/'TERMINAL.json').read_text())
    prod=json.loads((D.parent/'RESULT.json').read_text())
    assert term['graph_closed'] and not term['running'] and term['status'].startswith('PRODUCER_COMPLETE')
    assert prod['n']==16416 and prod['fullN_role_bindings']==864
    frozen=json.loads((D/'FROZEN_I32_INPUT.json').read_text())
    interface=json.loads((D.parent.parent/'controller_pack32_gate/SELECTED_BLOCKS.json').read_text())
    assert interface['selected_controllers']==frozen['selected_controllers']
    assert interface['whole_plane']==frozen['whole_plane']
    save('ACTUAL_PRODUCER_GATE.json',dict(status='SUCCESSFUL_CLOSED_PRODUCER_SEEN',
        producer_status=term['status'],producer_graph_closed=True,actual_graph=str(candidate.relative_to(ROOT)),
        frozen_I32_matches_selected_interface=True,old16389_acceptance_inherited=False))
    for phase,command in [('compile',['g++','-O3','-std=c++17','verify.cpp','-o','verify']),
                          ('validate',['./verify',str(source),str(candidate)])]:
        remaining=max(1,math.floor(BUDGET-cpu()-1))
        if phase=='validate':command.append(str(remaining-1))
        def limit():resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining+1))
        before=cpu()
        with (D/(phase+'.stdout')).open('w') as out,(D/(phase+'.stderr')).open('w') as err:
            process=subprocess.Popen(command,cwd=D,stdout=out,stderr=err,preexec_fn=limit)
            save('HANDLE.json',dict(status='RUNNING',running=True,pid=process.pid,phase=phase,
                total_CPU_budget_seconds=BUDGET,single_worker=True,one_all16416_final_root_batch=True,
                actual_producer_success_seen=True,charged_CPU_before_phase=before))
            code=process.wait()
        steps.append(dict(phase=phase,exit_code=code,CPU_seconds=cpu()-before))
        assert code==0,(phase,code)
        assert cpu()<BUDGET
    result=json.loads((D/'RESULT.json').read_text())
    assert result['status']=='PASS_COMPLETE_LITERAL_AND_ALL16416_FINAL_ROOTS_EXACT_D4'
    assert result['ordinary_final_graph_BFS_roots']==16416 and result['source_only_BFS_roots']==0
    result.update(total_suite_CPU_seconds=cpu(),CPU_budget_seconds=BUDGET,
        selected_I32_controllers=frozen['selected_controllers'],old16389_PASS_inherited=False)
    save('RESULT.json',result)
    note=f'''# Fresh literal16416 acceptance

Actual status:{result['status']}. The successful closed new producer was checked
before either graph was read. Old16389 PASS was not an acceptance premise.

This independent suite parsed the original15552/116316 author source once as
literal binding and the new16416 candidate once. It independently formed864
ordered centers from the frozen I32 and27 offsets of W={{x1=0}}, then bound the
candidate to every oldsource edge and every complete actual simpleN. No producer
neighborhood cache, virtual oldself or completed-loop adjacency was substituted.
Actual m:{result['m']}; newedges:{result['new_edges']}; sourceedges retained:
{result['all_source_edges_retained_exact']}; newnew:{result['new_new_edges']}.
Actual final degree histogram:{json.dumps(result['degree_histogram'])}.
Actual center degree histogram:{json.dumps(result['center_degree_histogram'])}.

Exactly16416 ordinary BFS roots were run once on this NEW graph,15552 oldlabels
and864 newlabels. All roots reached16416 vertices and had eccentricity exactly4.
The minimum observed number of OLD targets at distance4 was
{result['actual_min_old_R4']} (prediction>=6966),maximum{result['actual_max_old_R4']}.
All864 newroots have their ownoldcenter at distance2 and their other863 new
vertices at distance3 or4. There was no preliminary864-root batch or separate
source/controller BFS. Complete per-root histograms and the first actual
distance4 predecessor path are saved from the same unique full suite.

Every final edge projects to a bound actual source controller edge or holding
step under the192 labels,loopless maximumdegree{result['actual_loopless_controller_maxdegree']}.
The controller B3 bound106 leaves86*81=6966 oldtargets beyond3. This gives the
concrete prediction a structural basis without a controller distance run.
FullN copying gives a retraction from the new graph to its original source,
and complete finalBFS supplies sourceD4 as a consequence,without sourceBFS.

This is mathematical acceptance of one exact new literal. Global priority,
fresh public comparisons,Lean and final review remain separate. No global
counts,root STATE/HTML/Wiki,oldsource or oldgraph files were changed. Total suite
CPU is inTERMINAL,within120 including preparation/compile/run/aggregation.
No retries,field/rank/kernel regeneration,solver,Lean,ARIS,paidreview,install orhash.
'''
    (D/'NOTE.md').write_text(note)
    terminal=dict(status=result['status'],all_processes_terminal=True,running=False,single_worker=True,
        CPU_seconds=cpu(),CPU_budget_seconds=BUDGET,wall_seconds=time.time()-WALL,steps=steps,
        source_raw_parses=1,candidate_parses=1,final_graph_BFS_roots=16416,
        final_old_labelled_roots=15552,final_new_labelled_roots=864,separate_source_BFS_roots=0,
        preliminary_newroot_BFS=0,root_prediction_mismatches=0,no_automatic_continuation=True,
        measurement_boundary='Conservative metadata preparation plus recorded code preparation,onecompile,one source literal input binding,one candidate stream,independent I32/fullN/projection binding,one all16416root BFS,aggregation')
    save('TERMINAL.json',terminal)
    save('HANDLE.json',dict(status='TERMINAL',running=False,all_processes_terminal=True,
        result=result['status'],CPU_seconds=terminal['CPU_seconds']))
    print(json.dumps(terminal,indent=2))
except Exception as exc:
    failure=json.loads((D/'FAILURE.json').read_text()) if (D/'FAILURE.json').is_file() else {}
    save('TERMINAL.json',dict(status='FAIL_OR_BUDGET_UNKNOWN',phase=phase,error=str(exc),
        CPU_seconds=cpu(),CPU_budget_seconds=BUDGET,steps=steps,all_processes_terminal=True,running=False,
        actual_validator_failure=failure,no_automatic_continuation=True))
    save('HANDLE.json',dict(status='TERMINAL_FAILURE',running=False,all_processes_terminal=True))
    raise

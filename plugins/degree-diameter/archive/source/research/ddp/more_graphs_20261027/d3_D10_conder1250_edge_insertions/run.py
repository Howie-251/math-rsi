import json
import pathlib
import resource
import subprocess
import time

D=pathlib.Path(__file__).resolve().parent
SOURCE=D.parent/'d3_D10_current1250_source/source1250.edges'
with SOURCE.open() as f:
    assert list(map(int,f.readline().split()))==[1250,1875]
    assert list(map(int,f.readline().split()))==[0,1]
(D/'SOURCE_BINDING.json').write_text(json.dumps({'source_file':str(SOURCE),'source_header':[1250,1875],'anchor':[0,1],'source_label_recipe':'Officialraw1..1250minus1,asboundbydebruijn;notSagealternate-labelartifact','source_D10':'InheritedpublishedConderC1250.2/officialdescription','edge_VT':'Inheritedpublished3arc-regular/Aut15000','source_BFS':0},indent=2)+'\n')
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
wall=time.monotonic()
(D/'checkpoint.json').write_text(json.dumps({'status':'COMPILING_SINGLE_A_THEN_FINITE_B5614_BATCH','source_BFS':0,'modified_graphs_not_yet_run':True},indent=2)+'\n')
c=subprocess.run(['g++','-O3','-std=c++17',str(D/'probe.cpp'),'-o',str(D/'probe')],text=True,capture_output=True)
(D/'compile.log').write_text(c.stdout+c.stderr)
c.check_returncode()
compile_cpu=cpu()-start
(D/'checkpoint.json').write_text(json.dumps({'status':'NATIVE_A_B_MODIFIED_GRAPH_R10_RUNNING','native_aggregate_CPU_hard_limit':10,'source_BFS':0},indent=2)+'\n')
run=subprocess.run([str(D/'probe'),str(D),str(SOURCE)],text=True,capture_output=True)
native_process_cpu=cpu()-start-compile_cpu
(D/'native.log').write_text(run.stdout+run.stderr)
if run.returncode:
    r={'status':'UNKNOWN_OR_INVALID_NATIVE_EXIT','returncode':run.returncode}
    if (D/'cursor.json').exists():
        try:r['last_cursor']=json.loads((D/'cursor.json').read_text())
        except ValueError:r['last_cursor']='Partialcursor;useB_CASES.jsonl'
    if (D/'B_CASES.jsonl').exists():r['completed_case_lines']=sum(bool(line.strip()) for line in (D/'B_CASES.jsonl').read_text().splitlines())
else:r=json.loads((D/'NATIVE_RESULT.json').read_text())
r.update(target_Delta=3,target_D=10,savedL=1250,compile_CPU_seconds=compile_cpu,native_process_CPU_seconds=native_process_cpu,total_parent_children_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,source_old_BFS=0,new_lower_bounds=0)
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
term={'status':r['status'],'running':False,'pending':[],'result':'RESULT.json','new_lower_bounds':0}
(D/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','A_actual_D','B_objects_touched','B_objects_failed','B_objects_unknown','B_objects_unattempted','B_new_x_failures','B_new_y_failures','B_old_old_failures','hit_n','hit_object_id','native_CPU_seconds','total_parent_children_CPU_seconds'] if k in r}))

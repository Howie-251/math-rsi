import json,os,resource,subprocess,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'research/ddp/more_graphs_20261027').is_dir())
child_CPU=0.;attempts=[]
def save(name,value):(D/name).write_text(json.dumps(value,indent=2)+'\n')
def cost():return child_CPU+time.process_time()-started
def run(command,limit,stem):
    global child_CPU
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit))
    with (D/(stem+'.stdout')).open('w')as out,(D/(stem+'.stderr')).open('w')as err:
        p=subprocess.Popen(command,stdout=out,stderr=err,preexec_fn=limits)
        save('CONTROL_PACKING_HANDLE.json',dict(pid=p.pid,command=command,running=True,CPU_seconds=cost()))
        _,status,u=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    c=u.ru_utime+u.ru_stime;child_CPU+=c
    receipt=dict(command=command,exit_code=p.returncode,CPU_seconds=c,CPU_hard_limit=limit)
    attempts.append(receipt);return receipt
recipe=R/'research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json'
table=json.loads(recipe.read_text());arcs=[a for a in table['arcs']if a['from']==0]
centers=[x0+9*x2+27*x3 for x3 in range(3)for x2 in range(3)for x0 in range(3)]
literal={}
source=R/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
with source.open()as f:
    for lineno,line in enumerate(f):
        row=list(map(int,line.split()));label=row[0]
        if label in centers:literal[label]=set(row[1:])
        if label>=max(centers):break
loads={};details=[];all_equal=True
for x in centers:
    digits=[x//3**i%3 for i in range(4)];neighbors=set();virtual=[]
    for a in arcs:
        z=[(a['c'][j]+sum(a['B'][j][i]*digits[i]for i in range(4)))%3 for j in range(4)]
        for t in range(3):
            y=a['to']*81+sum(((z[j]+t*a['v'][j])%3)*3**j for j in range(4))
            if y==x:virtual.append(y)
            else:neighbors.add(y)
    equal=neighbors==literal[x];all_equal&=equal
    for y in neighbors:loads[y]=loads.get(y,0)+1
    details.append(dict(center=x,degree=len(neighbors),literal_equal=equal,deleted_virtual_self_entries=virtual,
                        literal_neighbors=sorted(literal[x])))
target0=sorted(a['to']for a in arcs)
normalization=all(a['v'][a['pivot']]==1 and all(x==0 for x in a['B'][a['pivot']])for a in arcs)
local_pass=all_equal and all(d['degree']in[14,15]for d in details)and max(loads.values())==1 and sorted({y//81 for y in loads})==target0 and target0==[0,11,59,79,180] and normalization
local=dict(status='PASS'if local_pass else'REFUTED_STOP',center_count=27,ordered_centers=centers,
    full_literal_rows_equal=all_equal,actual_degree_histogram={str(d):sum(r['degree']==d for r in details)for d in sorted({r['degree']for r in details})},
    actual_distinct_pin_count=len(loads),actual_max_pin_load=max(loads.values()),actual_target_controllers=sorted({y//81 for y in loads}),
    actual_deleted_virtual_self_entries=sum(len(r['deleted_virtual_self_entries'])for r in details),
    five_Qv_normalization_pivot_one_Bpivotzero=normalization,
    inherited_kernel_normal_second_coordinate_nonzero=True,kernel_rank_or_fieldlaws_recomputed=False,
    source_rows_parsed=lineno+1,source_rows_compared=27,details=details,CPU_seconds=cost())
save('LOCAL27_RESULT.json',local)
if not local_pass:
    result=dict(status='LOCAL27_REFUTED_NO_PACKING',local=local,CPU_seconds=cost(),attempts=attempts)
else:
    targets=[[]for _ in range(192)]
    for a in table['arcs']:targets[a['from']].append(a['to'])
    assert all(len(set(t))==5 for t in targets)
    assert sum(a in targets[a]for a in range(192))==24
    with (D/'ACTUAL_CONTROLLER_TARGETS.txt').open('w')as f:
        f.write('192 5\n')
        for a,t in enumerate(targets):f.write(str(a)+' '+' '.join(map(str,sorted(t)))+'\n')
    compile_receipt=run(['g++','-O3','-std=c++17',str(D/'control_packing.cpp'),'-o',str(D/'control_packing')],min(5,int(30-cost())),'COMPILE')
    if compile_receipt['exit_code']:
        result=dict(status='COMPILE_FAILURE_NO_SEARCH',CPU_seconds=cost(),attempts=attempts)
    else:
        remaining=min(25.,30-cost()-0.4)
        assert remaining>0
        save('CONTROL_PACKING_CHECKPOINT.json',dict(status='LOCAL27_PASS_ONE_SEARCH_STARTING',CPU_seconds=cost(),search_budget=remaining,running=True))
        search_receipt=run([str(D/'control_packing'),str(D/'ACTUAL_CONTROLLER_TARGETS.txt'),str(remaining)],min(26,int(30-cost())),'SEARCH')
        if search_receipt['exit_code']:
            result=dict(status='UNKNOWN_SEARCH_PROCESS_LIMIT_OR_FAILURE',CPU_seconds=cost(),attempts=attempts)
        else:
            search=json.loads((D/'SEARCH.stdout').read_text());selected=search['selected_controllers'];union=[]
            for a in selected:union+=targets[a]
            assert len(set(union))==5*len(selected)
            result=dict(status=search['status'],search=search,local27='LOCAL27_RESULT.json',
                fixed_rule='whole27 W{x1=0}, completed five-target disjoint controller blocks',
                complete_target_set_count=192,loop_controller_memberships_kept=24,
                selected_controller_labels=selected,selected_target_sets=[sorted(targets[a])for a in selected],
                selected_original_center_labels=[81*a+x for a in selected for x in centers],
                conditional_n_if_incumbent_used=15552+27*len(selected),conditional_competitive_threshold31=16389,
                CPU_seconds=cost(),CPU_budget_seconds=30,attempts=attempts)
result.update(running=False,graph_generation=0,BFS=0,old_field_rank_checks=0,Lean=0,new_graph_parameter_count=0,
              root_files_changed=False,packing_search_count=sum('control_packing'==Path(a['command'][0]).name for a in attempts))
save('CONTROL_PACKING_RESULT.json',result)
save('CONTROL_PACKING_TERMINAL.json',dict(status=result['status'],running=False,CPU_seconds=cost(),CPU_budget_seconds=30,
     unique_search_count=result['packing_search_count'],new_graphs=0,new_parameters=0,Lean=0))
save('CONTROL_PACKING_HANDLE.json',dict(status=result['status'],running=False,CPU_seconds=cost()))
print(json.dumps({k:result[k]for k in ['status','CPU_seconds','packing_search_count']}))

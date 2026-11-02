"""One bounded same-fiber literal route enumeration; no graph construction."""
from pathlib import Path
from datetime import datetime,timezone
import json
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
START=time.process_time()
BASE_CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
assert not (HERE/'RESULT.json').exists(),'This single bounded gate already has a result.'
assert sys.byteorder=='little'
params_path=ROOT/'research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json'
params=json.loads(params_path.read_text())
assert params['field']==5 and len(params['controller'])==30
cache=ROOT/'research/ddp/refresh_20261029/f5_induced_hyperplane3000/source_adjacency.u16.bin'
assert cache.stat().st_size==3750*20*2
def literal_array(xs):
    return '{'+','.join(literal_array(x) if isinstance(x,list) else str(x) for x in xs)+'}'
(HERE/'literal_parameters.h').write_text(
    'constexpr int DIRECTIONS[4][3]='+literal_array(params['directions'])+';\n'
    'constexpr int CONTROLLER[30][4]='+literal_array(params['controller'])+';\n')
(HERE/'PARAMETER_BINDING.json').write_text(json.dumps(dict(
    source_parameters=str(params_path.relative_to(ROOT)),
    source_cache=str(cache.relative_to(ROOT)),
    field=5,vertex_label=params['vertex_label'],fiber=0,
    directions=params['directions'],controller=params['controller'],
    byteorder=sys.byteorder,source_cache_bytes=cache.stat().st_size),indent=2)+'\n')
compile_start=resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++','-O2','-std=c++17',str(HERE/'check.cpp'),'-o',str(HERE/'check')],
    cwd=HERE,check=True,timeout=30)
compile_end=resource.getrusage(resource.RUSAGE_CHILDREN)
compile_cpu=(compile_end.ru_utime+compile_end.ru_stime-
             compile_start.ru_utime-compile_start.ru_stime)
assert compile_cpu<8,'No gate execution with insufficient original10CPU budget.'
subprocess.run([str(HERE/'check'),str(cache),str(HERE)],cwd=HERE,check=True,timeout=10)
usage=resource.getrusage(resource.RUSAGE_CHILDREN)
total=time.process_time()-START+usage.ru_utime+usage.ru_stime-BASE_CHILD.ru_utime-BASE_CHILD.ru_stime
native=json.loads((HERE/'NATIVE_RESULT.json').read_text())
assert native['pairs_checked']==7750
supported=native['prediction_failures']==0 and native['nontriangle_three_step_walks']==0
result=dict(native,status='COMPLETE_ALL_PREDICTIONS_SUPPORTED' if supported else 'PREDICTION_REFUTED',
    completed_UTC=datetime.now(timezone.utc).isoformat(),
    compile_CPU_seconds=compile_cpu,aggregate_compile_run_driver_CPU_seconds=total,
    CPU_budget_seconds=10,all7750_pairs_complete=True,
    endpoint_order='x<y, both old labels0..124 in fiber0',
    directed_walk_vs_AND_scope='Each ordered internal pair is a fixed-endpoint-direction walk; internal AND terms are sorted and deduplicated separately. Reverse endpoint direction is not counted again.',
    exact_no_two_step_condition='For retained endpoints in the6750 no-two-step pairs, D<=3 iff at least one of the two saved internal-vertex pair AND terms is wholly retained.',
    source_edge_text_reads=0,source_old_graph_full_revalidation=False,
    new_record=False,main_Wiki_changed=False,running=False,pending=[])
assert total<=10,total
(HERE/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(HERE/'REPORT.md').write_text(
    '# 固定fiber0全部二／三步路线：一次实测终态\n\n'
    f'完成7750个无序不同端点对，预测结果为{result["status"]}。'
    '每对以旧标签x<y固定端点方向，直接枚举全部二步中点及20×20三步内部有序点对；没有BFS。\n\n'
    f'二步中点数分布{native["two_step_midpoint_count_histogram"]}；'
    f'有向三步walk数分布{native["directed_three_step_walk_count_histogram_fixed_x_less_y"]}；'
    f'内部点去序AND项数分布{native["distinct_unordered_internal_AND_terms_histogram"]}。'
    f'两条三步路内部交点数分布{native["two_three_walks_internal_vertex_overlap_histogram"]}。\n\n'
    '1000对差在四方向之一，各方向250对；其它6750对没有二步路线。'
    '对后一类，保留端点时D≤3精确等价于两条三步路线中至少一条的两个内部点全部保留。'
    '这不是把两条有向walk机械计成两个不同AND：代码单独去序去重并检查，三例完整路线见EXAMPLES.json。\n\n'
    f'只读取现成cache一次和PARAMETERS；编译CPU{compile_cpu:.9f}秒，'
    f'编译/执行/driver合计{total:.9f}CPU秒，预算10。0原边表读、0BFS、0solver、0新图、0旧成果复验。'
    '未写Wiki/root/专家文件；单门已完成，无待运行项。\n')
print(json.dumps(dict(status=result['status'],pairs=7750,
    aggregate_CPU_seconds=total,RESULT=str((HERE/'RESULT.json').relative_to(ROOT))),ensure_ascii=False))

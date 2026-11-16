"""Final fixed literal graph check,3CPU total, reusing the compiled checker."""
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
RUN=HERE.parent
FINAL=RUN/'h9_n37632'
OLD=RUN/'h9_other_orientation'
OUT=FINAL/'independent'


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(3,3))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    start=time.process_time();wall=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    def used():
        r=resource.getrusage(resource.RUSAGE_CHILDREN)
        return time.process_time()-start+r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
    OUT.mkdir(exist_ok=False)
    def read(path,expected_m):
        with path.open()as f:
            n,m=map(int,next(f).split());assert(n,m)==(37632,expected_m)
            edges=set();count=0
            for row in f:
                u,v=map(int,row.split());assert 0<=u<v<n
                count+=1;edges.add((u,v))
            assert count==len(edges)==m
        return edges
    oldedges=read(OLD/'candidate37632.edges',205365)
    edges=read(FINAL/'graph_d11_D5_n37632.edges',205366)
    assert oldedges<=edges and edges-oldedges=={(31,37631)}
    oldc=json.loads((OLD/'CANDIDATE.json').read_text())
    params=json.loads((FINAL/'PARAMETERS.json').read_text())
    assert params['colors']==oldc['colors']
    assert params['pins']==sorted(oldc['pins']+[31])
    assert params['anchor']==31 and params['plane_id']==oldc['plane_id']==605
    prior=json.loads((HERE/'other37632/BINDING.json').read_text())
    assert prior['status']=='INDEPENDENT_CACHED_TRUE_GEOMETRY_SIGMA_LITERAL_BINDING_PASS'
    assert prior['actual_core_exact_match'] and prior['sigma_bijection'] and prior['eps_phi_constant']
    core_unchanged={e for e in edges if e[1]<37471}=={e for e in oldedges if e[1]<37471}
    outer_unchanged={e for e in edges if 37471<=e[1]<37631}=={e for e in oldedges if 37471<=e[1]<37631}
    assert core_unchanged and outer_unchanged
    (OUT/'PINS.txt').write_text('11\n'+' '.join(map(str,params['pins']))+'\n')
    rem=3-used();assert rem>0.2
    def limits():
        sec=max(1,math.ceil(rem));resource.setrlimit(resource.RLIMIT_CPU,(sec,sec))
        resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
        resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    with(OUT/'CHECK.log').open('w')as log:
        subprocess.run([str(HERE/'canonical37632/check'),str(FINAL/'graph_d11_D5_n37632.edges'),str(OUT),str(OUT/'PINS.txt'),str(rem-0.2)],check=True,
                       stdout=log,stderr=subprocess.STDOUT,timeout=30,preexec_fn=limits)
    raw=json.loads((OUT/'RAW_CHECK_RESULT.json').read_text())
    assert raw['status']=='ALL161_ROOTS_PASS' and raw['roots_complete']
    assert raw['roots_checked']==161 and raw['unique_bad_pairs_touching_checked_roots']==0
    assert raw['maximum_degree']==11 and raw['simple']
    rows=[json.loads(s)for s in(OUT/'ROOT_RESULTS.jsonl').read_text().splitlines()]
    assert len(rows)==161 and all(r['eccentricity']<=5 and r['unreachable_count']==0 for r in rows)
    result=dict(status='PASS_COMPLETE_LEGAL_GRAPH_BY_BOUND_CORE_AND_ALL161_REMAINING_ROOTS',
                n=37632,m=205366,maximum_degree=11,simple=True,diameter_upper_bound=5,diameter_exact=5,
                roots_checked=161,required_roots=161,unreachable_count=0,remaining_bad_pairs=0,
                core_roots_repeated=0,
                literal_binding=dict(retained_all_pre_anchor_candidate_edges=True,
                                     compared_pre_anchor_graph=str(OLD/"candidate37632.edges"),
                                     original37631_core_edges_all_preserved=False,only_added_edge=[31,37631],
                                     core_unchanged=core_unchanged,exterior_edges_unchanged=outer_unchanged,
                                     pins_exact=params['pins'],colors_exact=True),
                core_pair_proof=dict(evidence=str(HERE/'other37632/BINDING.json'),
                    justification='Actual core exactly unchanged from independently reconstructed trueH9/sigma/pi core. Arbitrarysigma and partialfold theorem gives allcore pairs<=5. Each of160old exterior and the newroot has now fullBFS on the finalactualgraph.'),
                diameter_lower_bound=dict(Moore_degree11_diameter4=1+11+11*10+11*100+11*1000,
                                          actual_order=37632,argument='37632>12222; no maximumdegree11graph of diameter<=4 can have this order.'),
                graph=str(FINAL/'graph_d11_D5_n37632.edges'),
                concrete_Lean_complete=False,requested_Gemini_final_review='PENDING_NOT_REPLACED',
                compiler_runs=0,whole_CPU=used(),whole_wall=time.monotonic()-wall,whole_CPU_cap=3,
                source_Lean_boundary='Concrete source/formal certification stillopen; mathematical graph verification is separately complete.')
    assert result['whole_CPU']<=3
    (OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    report='''H9最终37632图独立核验PASS
实际最终图37632顶点、205366边，简单、最大度11、直径恰5。
逐边比对先前独立绑定的另一方向图，所有core和旧外围边完全保留，唯一新增边为(31,37631)；颜色和全部11pins与PARAMETERS准确一致。
固定core与独立缓存真H9/sigma/pi重建结果全等，其core-core距离由任意sigma/partialfold定理保证。本次又在最终实际图运行完整160旧外围根+新根，共161次BFS，全部到全图<=5，未达点和坏对均0；没有重复37471个核心根。
最大度11的直径4 Moore界为12222，小于本图37632，因此D不能<=4，结合上界得到D恰5。
ROOT_RESULTS.jsonl保存每个根的完整ecc和未达目标列表（全部为空）；RAW_CHECK_RESULT保存实际独立原边checker结果。
本次仅固定最终图验证，未新搜颜色/plane/anchor，未重编checker。具体Lean及指定Gemini最终review仍pending，不因数学独验而升格。未改STATE/Wiki/catalog。
'''
    report+='Resources: '+json.dumps({k:result[k]for k in['whole_CPU','whole_wall','whole_CPU_cap','compiler_runs']})+'\n'
    (OUT/'REPORT.txt').write_text(report)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Check the prescribed old-core obligations, then run one finite repair."""
from pathlib import Path
import json,os,resource,subprocess,time
from twin59_to_58_deflation_verify import read_edges
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin58_old_core_unwind_run'
SOURCE=HERE/'twin59_to_58_deflation_run/component.path1.edges'
def precheck():
    n,edges58=read_edges(SOURCE);assert n==58
    label=lambda v:v if v<41 else v+2
    edges={tuple(sorted((label(u),label(v)))) for u,v in edges58}
    old=set(range(40))|set(range(50,60));aux=set(range(60))-old-{41,42}
    undo={(3,12),(9,14),(28,29)};assert undo<=edges;edges-=undo
    adj={u:set() for u in old|aux}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    ports={u:8-len(adj[u]&old) for u in old};checks=[]
    for u in sorted(old):
        if ports[u]:continue
        missing=[[u,v] for v in sorted(old) if v!=u and v not in adj[u] and not adj[u]&adj[v]&old]
        capacity=sum(ports[w] for w in adj[u]&old)
        checks.append({'old_vertex':u,'missing_old_pairs':missing,'old_neighbors':sorted(adj[u]&old),
          'neighbor_port_sum':capacity,'auxiliary_vertices':8,'passes':not missing and capacity>=8})
    result={'source':str(SOURCE),'old_edges_removed':sorted(undo),
      'label_convention':'original order60 labels;41,42 absent','zero_port_checks':checks,
      'passes_all_required_zero_port_conditions':all(c['passes'] for c in checks)}
    (OUT/'precheck.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(11,12))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def main():
    OUT.mkdir(exist_ok=True)
    check=precheck();print(json.dumps(check,indent=2))
    if not check['passes_all_required_zero_port_conditions']:
        print('Stopped at failed old-core obligation; no repair enumeration.')
        return
    command=[str(HERE/'twin58_old_core_unwind.bin'),str(SOURCE),str(OUT/'repair')];start=time.monotonic()
    with (OUT/'repair.log').open('w') as out:
        p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    resources={'command':command,'exit_code':p.returncode,'wall_seconds':time.monotonic()-start,
      'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,'max_rss_kib':usage.ru_maxrss,
      'threads':1,'internal_cpu_budget_seconds':10,'rlimit_cpu_soft_seconds':11,'rlimit_cpu_hard_seconds':12}
    (OUT/'repair.resources.json').write_text(json.dumps(resources,indent=2)+'\n')
    assert p.returncode==0;print((OUT/'repair.log').read_text().strip())
if __name__=='__main__':main()

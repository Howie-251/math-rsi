#!/usr/bin/env python3
"""One exact existence check per catalog local state; verify saved witnesses."""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'variable_hub_local_run'

def dump(path,data):
    path.write_text(json.dumps(data,indent=2)+'\n')

def limits():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(12,12))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))

def main():
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'resources.json').exists(),'This bounded run is not repeated.'
    catalog=json.loads((HERE/'d1_10_3_catalog/local_interfaces.json').read_text())
    states=[]
    for item in catalog['configurations']:
        primal=item['primal']
        zcols=[[i for i,row in enumerate(primal['Z_row_supports']) if j in row] for j in range(10)]
        for index,choice in enumerate(primal['choices']):
            mate=[-1]*10
            for u,v in choice['matching']:mate[u]=v;mate[v]=u
            states.append(dict(configuration=item['grunbaum_number'],matching_index=index,
                mate=mate,Z_columns=zcols,Y_columns=choice['factor_edges']))
    assert len(states)==71
    dump(OUT/'states.json',states)
    rows=[str(len(states))]
    for s in states:
        vals=[s['configuration'],s['matching_index']]+s['mate']
        vals += [sum(1<<u for u in col) for col in s['Z_columns']]
        vals += [sum(1<<u for u in col) for col in s['Y_columns']]
        rows.append(' '.join(map(str,vals)))
    (OUT/'input.txt').write_text('\n'.join(rows)+'\n')
    command=[str(HERE/'variable_hub_local_search.bin'),str(OUT/'input.txt'),str(OUT/'states.results.jsonl')]
    began=time.monotonic()
    with (OUT/'search.json').open('w') as out:
        p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    dump(OUT/'resources.json',dict(command=command,exit_code=p.returncode,
        wall_seconds=time.monotonic()-began,process_cpu_seconds=usage.ru_utime+usage.ru_stime,
        max_rss_kib=usage.ru_maxrss,threads=1,internal_cpu_limit_seconds=10,
        process_cpu_limit_seconds=12))
    assert p.returncode==0
    results=[json.loads(line) for line in (OUT/'states.results.jsonl').read_text().splitlines()]
    assert len(results)==71
    checked=[]
    for s,r in zip(states,results):
        assert (s['configuration'],s['matching_index'])==(r['configuration'],r['matching_index'])
        if r['status']!='witness':continue
        zperm=r['Z_column_for_target'];yperm=r['Y_column_for_target']
        assert sorted(zperm)==sorted(yperm)==list(range(10))
        c=[[int(r['C_column_masks'][v]>>u&1) for v in range(10)] for u in range(10)]
        z=[[int(u in s['Z_columns'][zperm[v]]) for v in range(10)] for u in range(10)]
        y=[[int(u in s['Y_columns'][yperm[v]]) for v in range(10)] for u in range(10)]
        assert all(sum(row)==3 for row in c)
        assert all(c[u][v]==c[v][u] for u in range(10) for v in range(10))
        assert all(c[u][u]==0 for u in range(10))
        assert all(int(u==v)+int(s['mate'][u]==v)+c[u][v]+z[u][v]+y[u][v]==1
            for u in range(10) for v in range(10))
        assert all(int(s['mate'][u]==v)+sum(y[u][k]*y[v][k]+z[u][k]*z[v][k] for k in range(10))
            ==1+4*int(u==v) for u in range(10) for v in range(10))
        seen={0};todo=[0]
        while todo:
            u=todo.pop()
            for v in range(10):
                if c[u][v] and v not in seen:seen.add(v);todo.append(v)
        assert len(seen)==10
        checked.append(dict(configuration=s['configuration'],matching_index=s['matching_index'],
            C=c,Z_relabelled=z,Y_relabelled=y,mate=s['mate']))
    dump(OUT/'verified_witnesses.json',checked)
    print((OUT/'search.json').read_text())
    print('Independently verified local hub witnesses:',len(checked))

if __name__=='__main__':main()

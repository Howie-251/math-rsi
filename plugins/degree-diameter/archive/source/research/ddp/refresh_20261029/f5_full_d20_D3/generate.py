#!/usr/bin/env python3
"""Deterministic full F5 graph; standard-library only, no search or BFS."""
import argparse,json,time
from pathlib import Path

HERE=Path(__file__).resolve().parent


def generate(output, parameters_path, compare):
    start=time.process_time()
    source='research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
    if parameters_path.exists():
        saved=json.loads(parameters_path.read_text())
        C=saved['controller'];Ts=saved['matrices']
        directions=saved['directions'];inverse_ports=saved['inverse_ports']
    else:
        project=HERE.parents[3]
        C=json.loads((project/source).read_text())['controller']
        local=json.loads((HERE.parent/'f5_complementary_triples/MATRICES_AND_PENCILS.json').read_text())
        Ts=[p['T'] for p in local['ports']]
        directions=local['directions'];inverse_ports=local['inverse_ports']
    n=len(C)*125;G=[set() for _ in range(n)]
    for a in range(30):
        for code in range(125):
            x=(code%5,code//5%5,code//25)
            for p,b in enumerate(C[a]):
                T=Ts[p];v=directions[inverse_ports[p]]
                y=[sum(T[i][j]*x[j] for j in range(3))%5 for i in range(3)]
                for t in range(5):
                    z=[(y[i]+t*v[i])%5 for i in range(3)]
                    G[a*125+code].add(b*125+z[0]+5*z[1]+25*z[2])
    assert n==3750
    assert all(len(row)==20 and u not in row for u,row in enumerate(G))
    assert all(u in G[v] for u,row in enumerate(G) for v in row)
    edges=[(u,v) for u,row in enumerate(G) for v in sorted(row) if u<v]
    assert len(edges)==37500
    comparison=None
    if compare:
        with compare.open() as f:
            header=tuple(map(int,f.readline().split()))
            rows=[tuple(map(int,line.split())) for line in f if line.strip()]
        comparison=dict(header=header,edge_set_matches=set(rows)==set(edges),repeated_rows=len(rows)-len(set(rows)))
        assert header==(3750,37500) and comparison['edge_set_matches'] and not comparison['repeated_rows']
    if output:
        with output.open('w') as f:
            f.write('3750 37500\n')
            for u,v in edges:f.write(f'{u} {v}\n')
    parameters=dict(field=5,controller=C,directions=directions,matrices=Ts,inverse_ports=inverse_ports,
        coefficient_sets=[[0,1,2,3,4] for _ in range(4)],vertex_label='a*125+x0+5*x1+25*x2',
        source_controller=source,base_author='Ryosuke Mizuno; original F4 source and controller',
        change='F5 complementary direction matrices and full F5 line relations',
        historical_comparison=dict(degree=20,diameter=3,verified_published_lower_bound=2783,
            source='Rajiv primary Sept2026 source23052995; current overall best not yet concluded'))
    if not compare:
        (HERE/'PARAMETERS.json').write_text(json.dumps(parameters,indent=2)+'\n')
    result=dict(status='DETERMINISTIC_REPRODUCTION_PASS' if compare else 'FULL_EDGE_LIST_GENERATED',n=n,m=len(edges),min_degree=20,max_degree=20,
        simple=True,undirected=True,output=str(output) if output else None,BFS_performed=False,
        diameter_status='F5 route proof; see separate INDEPENDENT_VALIDATION.json when available',
        CPU_seconds=time.process_time()-start,comparison=comparison)
    result_name='REPRODUCTION_CHECK.json' if compare else 'GENERATION_RESULT.json'
    (HERE/result_name).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'graph_d20_D3_n3750.edges')
    parser.add_argument('--parameters',type=Path,default=HERE/'PARAMETERS.json')
    parser.add_argument('--compare',type=Path)
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args();generate(None if args.dry_run else args.output,args.parameters,args.compare)

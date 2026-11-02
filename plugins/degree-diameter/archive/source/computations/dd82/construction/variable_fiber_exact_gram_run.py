#!/usr/bin/env python3
"""Five explicit exact-Gram cores; one combined bounded construction run."""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import json
import os
import random
import resource
import subprocess
import time

from d1_homogeneous_configuration_prepare import alignments

HERE = Path(__file__).resolve().parent
OUT = HERE / 'variable_fiber_exact_gram_run'
Q = [[0,0,1,3,1,2], [0,0,3,1,2,1], [1,3,0,2,0,1],
     [3,1,2,0,1,0], [1,2,0,1,0,1], [2,1,1,0,1,0]]
D = [1,1,1,1,3,3]
R = [[Q[i][j] + (D[i] if i == j else 0) for j in range(6)] for i in range(6)]
BQ = [[sum(R[i][k]*R[k][j] for k in range(6)) + R[i][j]
       - 7*(i == j) - 10 for j in range(6)] for i in range(6)]


def dump(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def matrix_from_supports(supports):
    return [[int(v in row) for v in range(10)] for row in supports]


def matrix_from_edges(edges):
    result = [[0]*10 for _ in range(10)]
    for u,v in edges:
        result[u][v] = result[v][u] = 1
    return result


def verify(path, core):
    lines = path.read_text().splitlines()
    assert tuple(map(int, lines[0].split())) == (60,240)
    edges = [tuple(map(int,line.split())) for line in lines[1:]]
    assert len(edges) == len(set(edges)) == 240
    ns = [set() for _ in range(60)]
    for u,v in edges:
        assert 0 <= u < v < 60
        ns[u].add(v); ns[v].add(u)
    assert all(len(row) == 8 for row in ns)
    for u in range(60):
        assert [sum(v//10 == j for v in ns[u]) for j in range(6)] == [
            D[j] if u//10 == j else Q[u//10][j] for j in range(6)]
    def block(i,j):
        return [[int(10*j+y in ns[10*i+x]) for y in range(10)] for x in range(10)]
    fixed = core['fixed_blocks']
    for key,a in fixed.items():
        assert block(int(key[0]),int(key[1])) == a
    gram_records = []
    for i,low,high in [(0,5,3),(1,4,2),(2,3,1),(3,2,0)]:
        s,x,z = block(i,i),block(i,low),block(i,high)
        xx,zz = matmul(x,transpose(x)),matmul(z,transpose(z))
        lhs = [[s[u][v]+xx[u][v]+zz[u][v] for v in range(10)] for u in range(10)]
        assert lhs == [[1+4*(u == v) for v in range(10)] for u in range(10)]
        gram_records.append(dict(fiber=i,degree_two_neighbor=low,degree_three_neighbor=high,
                                 lhs_integer_matrix=lhs,equals_J_plus_4I=True))
    # A saved Y/V must also be a column permutation of its fixed core incidence.
    for key in ('05','14'):
        a = block(int(key[0]),int(key[1]))
        assert sorted(map(tuple,transpose(a))) == sorted(map(tuple,transpose(core['initial_blocks'][key])))
    bad, distance_histogram = [],Counter()
    diameter = 0
    for u in range(60):
        dist = {u:0}; queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in ns[x]:
                if y not in dist:
                    dist[y] = dist[x]+1; queue.append(y)
        assert len(dist) == 60
        diameter = max(diameter,max(dist.values()))
        for v in range(u+1,60):
            distance_histogram[dist[v]] += 1
            if dist[v] > 2:
                bad.append(dict(pair=[u,v],fibers=[u//10,v//10],distance=dist[v],
                    zero_defect_block=BQ[u//10][v//10] == 0,common_neighbors=sorted(ns[u]&ns[v]),
                    neighbors_u=sorted(ns[u]),neighbors_v=sorted(ns[v])))
    defect = [[len(ns[u]&ns[v])+int(v in ns[u])-7*(u == v)-1 for v in range(60)] for u in range(60)]
    assert all(sum(row) == 5 for row in defect)
    for u in range(60):
        assert [sum(defect[u][10*j:10*j+10]) for j in range(6)] == BQ[u//10]
    blocks,exact_zero = [],[]
    for i in range(6):
        for j in range(i,6):
            vals = [defect[u][v] for u in range(10*i,10*i+10) for v in range(10*j,10*j+10) if u<v]
            missing = vals.count(-1); excess = sum(max(0,x) for x in vals)
            assert excess-missing == (5 if i == j else 10)*BQ[i][j]
            item = dict(fibers=[i,j],defect_quotient_entry=BQ[i][j],missing_pairs=missing,
                        positive_route_excess=excess,defect_histogram=dict(sorted(Counter(vals).items())))
            blocks.append(item)
            if BQ[i][j] == 0:
                exact_zero.append(dict(**item,zero_matrix=all(x == 0 for x in vals),
                    matrix=[row[10*j:10*j+10] for row in defect[10*i:10*i+10]]))
    assert all(exact_zero[k]['zero_matrix'] for k in range(len(exact_zero)) if exact_zero[k]['fibers'][0] == exact_zero[k]['fibers'][1])
    result = dict(graph=path.name,core_id=core['core_id'],n=60,edges=240,
        degree_histogram=dict(Counter(map(len,ns))),equitable_degrees_verified=True,
        fixed_core_verified=True,Y_V_column_permutations_verified=True,
        four_integer_Gram_equalities=gram_records,diameter=diameter,
        distance_histogram=dict(sorted(distance_histogram.items())),bad_pair_count=len(bad),
        zero_defect_block_bad_pairs=sum(x['zero_defect_block'] for x in bad),bad_pairs=bad,
        route_defect=defect,route_defect_row_sums=[sum(row) for row in defect],
        block_statistics=blocks,all_zero_blocks=exact_zero)
    dump(path.with_suffix('.verification.json'),result)
    return {k:result[k] for k in ('graph','core_id','n','edges','degree_histogram','diameter',
            'bad_pair_count','zero_defect_block_bad_pairs','block_statistics')}


def prepare():
    start = time.process_time()
    catalog = json.loads((HERE/'d1_10_3_catalog/local_interfaces.json').read_text())['configurations']
    configs = {c['grunbaum_number']:c for c in catalog}
    specs = [(1,4,[5,5]),(2,3,[10]),(5,8,[4,6]),(6,7,[3,7]),(9,9,[3,3,4])]
    cores,checks = [],{}
    for core_id,(zn,wn,cycle_type) in enumerate(specs):
        zc,wc = configs[zn],configs[wn]
        zd = next(i for i,c in enumerate(zc['dual']['choices']) if c['factor_cycle_type'] == cycle_type)
        wd = next(i for i,c in enumerate(wc['dual']['choices']) if c['factor_cycle_type'] == cycle_type)
        zp,wp = zc['primal']['choices'][0],wc['primal']['choices'][0]
        zr,wr = zc['dual']['choices'][zd],wc['dual']['choices'][wd]
        t_rows = next(alignments(wr,zr))
        blocks = {'03':matrix_from_supports(zc['primal']['Z_row_supports']),
                  '12':matrix_from_supports(wc['primal']['Z_row_supports']),
                  '23':[[int(row>>v&1) for v in range(10)] for row in t_rows],
                  '00':matrix_from_edges(zp['matching']), '11':matrix_from_edges(wp['matching']),
                  '22':matrix_from_edges(wr['matching']), '33':matrix_from_edges(zr['matching'])}
        fixed = dict(blocks)
        blocks['05'] = matrix_from_supports(zp['Y_row_supports'])
        blocks['14'] = matrix_from_supports(wp['Y_row_supports'])
        initial = {key:blocks[key] for key in ('05','14')}
        rng = random.Random(2026101200+core_id)
        column_labels = {}
        for key in ('05','14'):
            p = list(range(10)); rng.shuffle(p); column_labels[key] = p
            blocks[key] = [[row[p[j]] for j in range(10)] for row in blocks[key]]
        matchings = {}
        for i,j in combinations(range(6),2):
            if Q[i][j] != 1: continue
            p = list(range(10)); rng.shuffle(p); matchings[f'{i}{j}'] = p
            blocks[f'{i}{j}'] = [[int(p[u] == v) for v in range(10)] for u in range(10)]
        pe = {(x,x+5) for x in range(5)}
        pe |= {tuple(sorted((x,(x+1)%5))) for x in range(5)}
        pe |= {tuple(sorted((x+5,(x+2)%5+5))) for x in range(5)}
        blocks['44'] = blocks['55'] = matrix_from_edges(pe)
        edges = []
        for key,a in blocks.items():
            i,j = map(int,key)
            edges.extend((10*i+x,10*j+y) for x in range(10) for y in range(10) if a[x][y] and (i != j or x<y))
        assert len(edges) == len(set(edges)) == 240
        path = OUT/f'core{core_id}.seed.edges'
        path.write_text('60 240\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
        core = dict(core_id=core_id,Z_configuration=zn,W_configuration=wn,
                    Z_primal_choice=0,W_primal_choice=0,Z_dual_choice=zd,W_dual_choice=wd,
                    T_cycle_type=cycle_type,T_alignment='first generated alignment of W dual factor to Z dual factor',
                    fixed_blocks=fixed,initial_blocks=initial,seed_blocks=blocks,
                    Y_V_seed_column_labels=column_labels,q1_seed_permutations=matchings,
                    seed_random_seed=2026101200+core_id)
        cores.append(core);dump(OUT/f'core{core_id}.json',core)
        checks[f'core{core_id}_seed'] = verify(path,core)
    dump(OUT/'cores.json',cores)
    dump(OUT/'preparation.json',dict(core_count=len(cores),d=D,Q=Q,defect_quotient=BQ,
        scope='Five specified fixed catalogue cores; no catalogue completeness claim for this experiment.',
        cpu_seconds=time.process_time()-start))
    (OUT/'domain.txt').write_text(' '.join(map(str,[len(cores)]+D+[x for row in Q for x in row]+[x for row in BQ for x in row]))+'\n')
    return cores,checks


def limits():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))


def record_hub_failures():
    """Decompose block 04 of the already generated seeds; no graph search."""
    records = []
    identity = [[int(i == j) for j in range(10)] for i in range(10)]
    for core in json.loads((OUT/'cores.json').read_text()):
        cid = core['core_id']
        ns = [set() for _ in range(60)]
        for line in (OUT/f'core{cid}.seed.edges').read_text().splitlines()[1:]:
            u,v = map(int,line.split()); ns[u].add(v); ns[v].add(u)
        def block(i,j):
            return [[int(10*j+y in ns[10*i+x]) for y in range(10)] for x in range(10)]
        a,s,c,z,y = block(0,4),block(0,0),block(4,4),block(0,3),block(0,5)
        at = transpose(a)
        n,p = matmul(block(3,4),at),matmul(block(5,4),at)
        cnew = matmul(matmul(a,c),at)
        zn,yp = matmul(z,n),matmul(y,p)
        normalized = [[sum(m[u][v] for m in (identity,s,cnew,zn,yp)) for v in range(10)] for u in range(10)]
        original = matmul(normalized,a)
        direct = [[int(40+v in ns[u])+len(ns[u]&ns[40+v]) for v in range(10)] for u in range(10)]
        assert original == direct
        assert cnew == transpose(cnew) and all(sum(row)==3 for row in cnew)
        missing,overlaps = [],[]
        for u in range(10):
            for v in range(10):
                value = direct[u][v]
                if value == 0:
                    missing.append(dict(pair=[u,40+v],neighbors_source=sorted(ns[u]),
                                        neighbors_target=sorted(ns[40+v])))
                elif value > 1:
                    overlaps.append(dict(pair=[u,40+v],route_count=value,
                                         direct_edge=40+v in ns[u],common_neighbors=sorted(ns[u]&ns[40+v])))
        assert all(sum(row)==10 for row in direct)
        assert sum(x['route_count']-1 for x in overlaps) == len(missing)
        records.append(dict(core_id=cid,original_equation='F04+S0*F04+F04*C4+Z*F34+Y*F54=J',
            normalized_equation='I+S0+Cprime+Z*N+Y*P=J',
            normalization='Right multiply by F40; Cprime=F04*C4*F40, N=F34*F40, P=F54*F40',
            S0=s,Z=z,Y=y,Cprime=cnew,N=n,P=p,Z_N=zn,Y_P=yp,
            original_route_matrix=direct,normalized_route_matrix=normalized,
            missing_count=len(missing),missing_pairs=missing,overlap_pairs=overlaps))
    dump(OUT/'hub04_failures.json',records)
    return [{k:record[k] for k in ('core_id','missing_count')} for record in records]


def main():
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'resources.json').exists(),'No unchanged bounded-search repeat.'
    assert not (OUT/'launch_status.json').exists(),'Experiment already completed without optimization.'
    cores,checks = prepare()
    print(json.dumps({'complete_seeds':{key:(v['bad_pair_count'],v['zero_defect_block_bad_pairs']) for key,v in checks.items()}}),flush=True)
    cmd = [str(HERE/'variable_fiber_exact_gram_search.bin'),str(OUT)]
    began = time.monotonic()
    with (OUT/'search.log').open('w') as out:
        p = subprocess.Popen(cmd,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        _,status,usage = os.wait4(p.pid,0); p.returncode = os.waitstatus_to_exitcode(status)
    resources = dict(command=cmd,exit_code=p.returncode,wall_seconds=time.monotonic()-began,
        user_cpu_seconds=usage.ru_utime,system_cpu_seconds=usage.ru_stime,
        total_cpu_seconds=usage.ru_utime+usage.ru_stime,max_rss_kib=usage.ru_maxrss,
        threads=1,process_cpu_limit_seconds=30,internal_combined_optimization_budget_seconds=27,
        optimization_processes=1,cores=len(cores))
    dump(OUT/'resources.json',resources); assert p.returncode == 0
    stats = json.loads((OUT/'search.json').read_text())
    for core in cores:
        cid = core['core_id']
        for name in ('best_bad','best_zero','best_energy'):
            key = f'core{cid}_{name}'
            checks[key] = verify(OUT/f'core{cid}.{name}.edges',core)
            expected = stats['cores'][cid][name]
            assert checks[key]['bad_pair_count'] == expected['bad_pairs']
            assert checks[key]['zero_defect_block_bad_pairs'] == expected['zero_block_bad_pairs']
    dump(OUT/'verification.json',checks)
    print(json.dumps(dict(resources=resources,graphs={key:{k:v[k] for k in ('bad_pair_count','zero_defect_block_bad_pairs','diameter')} for key,v in checks.items()}),indent=2))


if __name__ == '__main__':
    main()

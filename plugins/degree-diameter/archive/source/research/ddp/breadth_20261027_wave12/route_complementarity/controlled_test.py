"""One controlled edge-direction change, checked by one independent all-root BFS."""
from pathlib import Path
from collections import deque, Counter, defaultdict
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent/'controlled_edge_change'
SOURCE = ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words'

def action(columns,x):
    y = 0
    for i in range(4):
        if x&(1<<i):
            y ^= columns[i]
    return y

def run(new_b,second_b=None,shear=False):
    assert 0<new_b<16
    if second_b is not None:
        assert 0<second_b<16
    prefix = 'matrix_shear' if shear else 'coordinated' if second_b is not None else 'controlled'
    output = OUT/('matrix_prediction_check.json' if shear else 'coordinated_prediction_check.json' if second_b is not None else 'actual_prediction_check.json')
    if output.exists():
        raise RuntimeError('Controlled graph has already been checked; reuse its saved distances')
    started = time.process_time()
    data = json.loads((SOURCE/'best_parameters.json').read_text())
    gp = data['global_label_parameters']
    mats,bs,inv = gp['matrix_columns'],gp['b_codes'],data['inverse_labels']
    controller = data['controller_out']
    changed = (0,18)
    edges,parameters = set(),[]
    for u,row in enumerate(controller):
        for t in (0,1):
            v = row[t]
            b = new_b if (u,v)==changed else second_b if second_b is not None and (u,v)==(36,0) else bs[t]
            T,Ti = mats[t],mats[inv[t]]
            if shear and (u,v)==changed:
                assert new_b==3
                T = [column^(2 if column&1 else 0) for column in T]
                inverse_map = {action(T,x):x for x in range(16)}
                assert len(inverse_map)==16
                Ti = [inverse_map[1<<i] for i in range(4)]
            assert all(action(Ti,action(T,x))==x for x in range(16))
            parameters.append(dict(u=u,v=v,label=t,T_columns=T,b=b,c=0,
                Tinv_columns=Ti,reverse_b=action(Ti,b),reverse_c=0))
            for x in range(16):
                for lam in range(2):
                    y = action(T,x)^(lam*b)
                    edges.add(tuple(sorted((16*u+x,16*v+y))))
    assert len(edges)==4608
    oldlines = (SOURCE/'best.edges').read_text().splitlines()
    oldedges = {tuple(map(int,line.split())) for line in oldlines[1:]}
    delta = edges.symmetric_difference(oldedges)
    allowed_changes = {frozenset(changed)}
    if second_b is not None:
        allowed_changes.add(frozenset((36,0)))
    assert delta and all(frozenset((u//16,v//16)) in allowed_changes for u,v in delta)
    adjacency = [[] for _ in range(1152)]
    for u,v in edges:
        assert u<v
        adjacency[u].append(v)
        adjacency[v].append(u)
    assert all(len(row)==8 and len(set(row))==8 for row in adjacency)
    (OUT/(prefix+'.edges')).write_text('1152 4608\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
    (OUT/(prefix+'_parameters.json')).write_text(json.dumps(dict(changed_edge=changed,
        changed_b=new_b,second_edge=(36,0) if second_b is not None else None,
        second_b=second_b,global_source=str(SOURCE.relative_to(ROOT)),edges=parameters),indent=2)+'\n')
    tight = json.loads((ROOT/'research/ddp/breadth_20261027_wave10/binary1152_edge_local/unique4_controller_slots.json').read_text())['slots']
    tight_pairs = {(r['source'],r['target']) for r in tight}
    missing_tight = Counter()
    histogram = Counter()
    ecc = Counter()
    target_missing = 0
    bad = 0
    unreachable = 0
    with (OUT/(prefix+'_distances.u8.bin')).open('wb') as file:
        for root in range(1152):
            distance = [-1]*1152
            distance[root] = 0
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v in adjacency[u]:
                    if distance[v]<0:
                        distance[v] = distance[u]+1
                        queue.append(v)
            file.write(bytes(d if d>=0 else 255 for d in distance))
            ecc[max(distance) if -1 not in distance else -1] += 1
            source_base = root//16
            if source_base==0:
                target_missing += sum(distance[v]<0 or distance[v]>4 for v in range(160,176))
            for v,d in enumerate(distance):
                if d<0 or d>4:
                    pair = (source_base,v//16)
                    if pair in tight_pairs:
                        missing_tight[pair] += 1
                if v>root:
                    histogram[d] += 1
                    bad += d<0 or d>4
                    unreachable += d<0
    result = dict(status='ONE_MATRIX_DIRECTION_GRAPH_MEASURED' if shear else 'ONE_COORDINATED_GRAPH_MEASURED' if second_b is not None else 'ONE_CONTROLLED_GRAPH_MEASURED',n=1152,m=4608,degree=8,
        simple=True,connected=unreachable==0,diameter=max(histogram) if unreachable==0 else None,
        target_D=4,ordinary_bad_unordered_pairs=bad,
        unordered_distance_histogram=dict(sorted(histogram.items())),
        eccentricity_histogram=dict(sorted(ecc.items())),
        changed_edge=changed,new_b=new_b,old_b=bs[0],
        second_edge=(36,0) if second_b is not None else None,second_b=second_b,
        one_edge_output_shear_applied=shear,
        all_other_control_edge_relations_unchanged=True,
        symmetric_difference_edges=len(delta),critical_slot_0_to_10_missing=target_missing,
        tight_slot_missing=[dict(source=u,target=v,missing_ordered_fiber_pairs=count)
                            for (u,v),count in sorted(missing_tight.items())],
        roots_checked=1152,old_graph_BFS_repeated=False,source_graph_bad_count_reused=12384,
        critical_repair_prediction_supported=target_missing==0,
        full_distance_cache=prefix+'_distances.u8.bin',CPU_seconds=time.process_time()-started,
        new_lower_bound=False)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='tight_slot_missing'},ensure_ascii=False))

if __name__=='__main__':
    run(int(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 and sys.argv[2]!='shear' else None,
        shear=len(sys.argv)>2 and sys.argv[2]=='shear')

#!/usr/bin/env python3
"""Only enumerate cycle slopes and necessary line counts; no translations/graphs."""
import itertools
import json
import time
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parent
PAIRS = list(itertools.combinations(range(4), 2))


def analyze(q, mults):
    start = time.process_time()
    mult = [[0] * 4 for _ in range(4)]
    for (i,j), n in zip(PAIRS,mults):
        mult[i][j] = mult[j][i] = n
    data = []
    for i,j in PAIRS:
        h,k = [v for v in range(4) if v not in (i,j)]
        n = mult[i][j]
        direct = n + n*n*(n-1)//2 + n*sum(
            mult[i][v]*(mult[i][v]-1)+mult[j][v]*(mult[j][v]-1)
            for v in (h,k))
        paths = [(i,h,j), (i,k,j), (i,h,k,j), (i,k,h,j)]
        weights = []
        for path in paths:
            weight = 1
            for a,b in zip(path,path[1:]):
                weight *= mult[a][b]
            weights.append(weight)
        assert sum(weights) < q
        data.append({'pair':[i,j], 'direct_capacity':direct,
                     'other_base_paths':paths, 'path_weights':weights,
                     'maximum_other_direction_lines':sum(weights),
                     'total_form_capacity':direct+sum(weights)})
    inv = [0] + [pow(x,-1,q) for x in range(1,q)]
    survivors = []
    passes_hist = Counter()
    min_capacity_hist = Counter()
    completed = 0
    for u,v,w in itertools.product(range(1,q), repeat=3):
        slopes = [[1]*4 for _ in range(4)]
        for a,b,x in [(1,2,u),(1,3,v),(2,3,w)]:
            slopes[a][b]=x
            slopes[b][a]=inv[x]
        caps = []
        for datum in data:
            i,j=datum['pair']
            cap=datum['direct_capacity']
            for path,weight in zip(datum['other_base_paths'],datum['path_weights']):
                s=1
                for a,b in zip(path,path[1:]):
                    s=s*slopes[a][b] % q
                if s == slopes[i][j]:
                    cap += weight
            caps.append(cap)
        completed += 1
        passes_hist[sum(c>=q for c in caps)] += 1
        min_capacity_hist[min(caps)] += 1
        if min(caps)>=q:
            survivors.append({'cycle_slopes_12_13_23':[u,v,w],
                              'direct_direction_capacity_by_unordered_pair':caps})
    return {'field_order':q, 'cross_multiplicities':mults,
            'tree_slope_classes':[[0,1],[0,2],[0,3]],
            'cycle_slope_classes':[[1,2],[1,3],[2,3]],
            'unordered_pair_order':[list(p) for p in PAIRS],
            'path_type_data':data, 'expected_slope_inputs':(q-1)**3,
            'completed_slope_inputs':completed,
            'survivor_count':len(survivors), 'survivors':survivors,
            'number_of_passing_pairs_histogram':dict(sorted(passes_hist.items())),
            'minimum_direct_capacity_histogram':dict(sorted(min_capacity_hist.items())),
            'CPU_seconds':time.process_time()-start}


def main():
    start=time.process_time()
    results=[analyze(31,[2,2,2,2,2,2]),analyze(43,[3,2,2,2,2,3])]
    output={'status':'COMPLETE','running':False,
            'scope':'necessary cycle-slope line capacity only for the two fixed bases',
            'results':results,'CPU_seconds':time.process_time()-start,
            'translation_assignments':0,'generated_graphs':0,'BFS_roots':0}
    (OUT/'SLOPE_CAPACITY.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({**{k:output[k] for k in ['status','CPU_seconds','translation_assignments','generated_graphs','BFS_roots']},
                     'results':[{k:r[k] for k in ['field_order','completed_slope_inputs','survivor_count','CPU_seconds']} for r in results]},indent=2))


if __name__=='__main__':
    main()

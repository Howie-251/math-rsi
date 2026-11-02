"""Fixed-bin virtual-loop statistics only; no graph traversal or modification."""
from array import array
from collections import Counter
from pathlib import Path
import json
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
START = time.process_time()
P = Path(__file__).resolve().parent
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_numeric_loop_completed_partition_check']
assert sys.byteorder == 'little'

def inspect(label, n, m, binsize, row, source):
    before = time.process_time()
    representatives = {}
    virtual_loops = []
    degree_hist = Counter()
    error = None
    tested = 0
    for v in range(n):
        neighbors = row(v)
        deg = len(neighbors)
        degree_hist[deg] += 1
        counts = Counter(w//binsize for w in neighbors)
        original = sorted(counts.items())
        added = deg == 14
        if added:
            counts[v//binsize] += 1
            virtual_loops.append(v)
        signature = tuple(sorted(counts.items()))
        tested += 1
        if len(signature) != 5 or any(k != 3 for _, k in signature):
            error = {'kind':'ROW_NOT_FIVE_BINS_TIMES_THREE','vertex':v,'source_bin':v//binsize,
                     'original_degree':deg,'virtual_loop_added':added,
                     'original_target_bin_counts':original,'loop_completed_target_bin_counts':signature}
            break
        sourcebin = v//binsize
        if sourcebin in representatives and representatives[sourcebin]['signature'] != signature:
            error = {'kind':'WITHIN_SOURCE_BIN_SIGNATURE_MISMATCH','vertex':v,'source_bin':sourcebin,
                     'original_degree':deg,'virtual_loop_added':added,
                     'original_target_bin_counts':original,'loop_completed_target_bin_counts':signature,
                     'earlier_vertex':representatives[sourcebin]['vertex'],
                     'earlier_loop_completed_signature':representatives[sourcebin]['signature']}
            break
        representatives.setdefault(sourcebin, {'vertex':v,'signature':signature})
    success = error is None
    result = {'source':label,'n':n,'m':m,'input':source,'bin_size':binsize,'bin_count':n//binsize,
              'status':'COMPLETE_EQUITABLE_LOOP_COMPLETED_RELATION' if success else 'FIXED_PARTITION_COUNTEREXAMPLE',
              'complete_equitable':success,'rows_tested':tested,'first_counterexample':error,
              'degree_histogram_among_tested_rows':dict(sorted(degree_hist.items())),
              'CPU_seconds_partition_test':time.process_time()-before}
    if success:
        assert len(representatives) == n//binsize
        result['virtual_selfloop_count'] = len(virtual_loops)
        result['loop_controller_counts'] = dict(sorted(Counter(v//binsize for v in virtual_loops).items()))
        result['loop_controllers'] = sorted({v//binsize for v in virtual_loops})
        result['virtual_selfloop_vertex_labels'] = virtual_loops
        result['quotient_relations'] = [
            {'source_bin':b,'representative_vertex':representatives[b]['vertex'],
             'target_bin_counts':representatives[b]['signature']}
            for b in range(n//binsize)]
    return result

sources = []
source = P.parent/'d15_D4_current15552/source15552.header.edges'
g = [[] for _ in range(15552)]
with source.open() as f:
    n, m = map(int, next(f).split())
    assert (n,m) == (15552,116316)
    for line in f:
        u,v = map(int,line.split())
        g[u].append(v)
        g[v].append(u)
assert sum(map(len,g)) == 2*m
sources.append(inspect('actual (15,4) 15552',n,m,81,lambda v:g[v],str(source.relative_to(P.parent))))
del g

source = P.parent/'d15_D5_current102060_source/monotone_R4_cover/source.csr.u32le.bin'
data = array('I')
data.frombytes(source.read_bytes())
n, nadj = data[0], data[1]
assert (n,nadj) == (102060,1530090)
assert len(data) == 2+(n+1)+nadj
start = n+3
assert data[2] == 0 and data[n+2] == nadj
def csr_row(v):
    return data[start+data[2+v]:start+data[3+v]]
sources.append(inspect('actual (15,5) 102060',n,nadj//2,243,csr_row,str(source.relative_to(P.parent))))
result = {'status':'COMPLETE_TWO_FIXED_LOOP_COMPLETION_PREDICTION_CHECKS',
          'prediction_status':'SUPPORTED' if all(s['complete_equitable'] for s in sources) else 'REFUTED_FOR_AT_LEAST_ONE_FIXED_SOURCE_PARTITION',
          'sources':sources,'source_adjacency_modified':False,
          'source_reads_per_input':1,'graph_or_ball_or_solver_runs':0,
          'CPU_seconds':time.process_time()-START,
          'scope':'Only specified 81 and 243 label bins with one virtual selfloop statistic per degree-14 point. No coordinate relabeling, affine chart proof, distance or new graph claim.'}
(P/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'CPU_seconds':result['CPU_seconds'],
                  'sources':[{k:s[k] for k in ['source','status','rows_tested','complete_equitable','first_counterexample']} for s in sources]}))

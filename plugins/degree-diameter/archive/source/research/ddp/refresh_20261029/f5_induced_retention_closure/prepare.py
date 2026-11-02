#!/usr/bin/env python3
"""Exact necessary retention CNF; this file never starts a solver."""
from pathlib import Path
from collections import defaultdict
from array import array
import argparse
import json
import shutil
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

class CNF:
    def __init__(self, path):
        self.nv = 3750
        self.nc = 0
        self.f = path.open('w')
    def var(self):
        self.nv += 1
        return self.nv
    @staticmethod
    def neg(x):
        return not x if isinstance(x, bool) else -x
    def add(self, *xs):
        if any(x is True for x in xs):
            return
        ys = list(dict.fromkeys(x for x in xs if x is not False))
        if any(-x in ys for x in ys):
            return
        self.f.write(' '.join(map(str, ys)) + ' 0\n')
        self.nc += 1
    def both(self, a, b):
        if a is False or b is False: return False
        if a is True: return b
        if b is True: return a
        if a == b: return a
        if a == -b: return False
        z = self.var()
        self.add(-z, a); self.add(-z, b); self.add(z, -a, -b)
        return z
    def either(self, a, b):
        if a is True or b is True: return True
        if a is False: return b
        if b is False: return a
        if a == b: return a
        if a == -b: return True
        z = self.var()
        self.add(z, -a); self.add(z, -b); self.add(-z, a, b)
        return z
    def xor(self, a, b):
        if a is False: return b
        if b is False: return a
        if a is True: return self.neg(b)
        if b is True: return self.neg(a)
        if a == b: return False
        if a == -b: return True
        z = self.var()
        self.add(a, b, -z); self.add(a, -b, z)
        self.add(-a, b, z); self.add(-a, -b, -z)
        return z
    def majority(self, a, b, c):
        if isinstance(a, bool): return self.either(b,c) if a else self.both(b,c)
        if isinstance(b, bool): return self.either(a,c) if b else self.both(a,c)
        if isinstance(c, bool): return self.either(a,b) if c else self.both(a,b)
        z = self.var()
        self.add(-a,-b,z); self.add(-a,-c,z); self.add(-b,-c,z)
        self.add(a,b,-z); self.add(a,c,-z); self.add(b,c,-z)
        return z
    def threshold_step(self, a, b, y):
        # z iff a OR (b AND y); exact, including the reverse implication.
        if a is True: return True
        if a is False: return self.both(b,y)
        if b is False: return a
        if b is True: return self.either(a,y)
        z = self.var()
        self.add(-a,z); self.add(-b,-y,z)
        self.add(-z,a,b); self.add(-z,a,y)
        return z
    def or_many(self, lits):
        if len(lits) == 1: return lits[0]
        z = self.var()
        for x in lits: self.add(-x,z)
        self.add(-z,*lits)
        return z
    def add_bits(self, aa, bb):
        result = []
        carry = False
        for i in range(max(len(aa),len(bb))):
            a = aa[i] if i < len(aa) else False
            b = bb[i] if i < len(bb) else False
            result.append(self.xor(self.xor(a,b),carry))
            carry = self.majority(a,b,carry)
        if carry is not False: result.append(carry)
        return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare-only', action='store_true', required=True)
    parser.parse_args()
    start = time.process_time()
    params = json.loads((BASE/'f5_full_d20_D3/PARAMETERS.json').read_text())
    cert = json.loads((BASE/'f5_d20_edge_criticality_20261029/CONTROLLER_CERTIFICATE.json').read_text())
    ctl = params['controller']
    raw = array('H')
    with (BASE/'f5_induced_hyperplane3000/source_adjacency.u16.bin').open('rb') as f:
        raw.fromfile(f, 3750*20)
    adj = [list(raw[20*v:20*v+20]) for v in range(3750)]
    paths = []
    for u in range(30):
        by_target = defaultdict(list)
        for p,a in enumerate(ctl[u]):
            for q,b in enumerate(ctl[a]):
                for r,v in enumerate(ctl[b]):
                    by_target[v].append(([u,a,b,v],[p,q,r]))
        for v, words in sorted(by_target.items()):
            if v == u or v in ctl[u] or set(ctl[u]).intersection(ctl[v]):
                continue
            if len(words) == 1:
                vv, pp = words[0]
                paths.append({'vertices':vv,'ports':pp})
    assert len(paths) == 258 == cert['unique_controller_distance3_ordered_pairs']
    path_tuples = {tuple(p['vertices']) for p in paths}
    assert all(tuple(reversed(p)) in path_tuples for p in path_tuples)
    (HERE/'CONTROLLER_UNIQUE_WORDS.json').write_text(json.dumps(paths,indent=2)+'\n')
    body = HERE/'model.body.tmp'
    cnf = CNF(body)
    stages = []
    def stage(name, before):
        stages.append({'name':name,'new_variables':cnf.nv-before[0],
                       'new_clauses':cnf.nc-before[1]})
    before = (cnf.nv,cnf.nc)
    for v in range(3750):
        prev = [True,False,False,False,False]
        for i,w in enumerate(adj[v],1):
            cur = [True,False,False,False,False]
            for j in range(1,min(i,4)+1):
                cur[j] = cnf.threshold_step(prev[j],prev[j-1],-(w+1))
            prev = cur
        cnf.add(-(v+1),prev[4])
    stage('conditional_retained_degree_at_most16',before)
    before = (cnf.nv,cnf.nc)
    vectors = [[v+1] for v in range(3750)]
    while len(vectors)>1:
        vectors = [cnf.add_bits(vectors[i],vectors[i+1]) if i+1<len(vectors)
                   else vectors[i] for i in range(0,len(vectors),2)]
    sum_bits = vectors[0]
    ge = True
    for i,bit in enumerate(sum_bits):
        ge = cnf.both(bit,ge) if (1921>>i)&1 else cnf.either(bit,ge)
    cnf.add(ge)
    stage('exact_binary_sum_at_least1921',before)
    before = (cnf.nv,cnf.nc)
    cache = {}
    cache_sizes = defaultdict(int)
    def flag(old_ids):
        key = tuple(sorted(old_ids))
        if key not in cache:
            cache[key] = cnf.or_many([v+1 for v in key])
            cache_sizes[len(key)] += 1
        return cache[key]
    closure_count = 0
    literal_witness = None
    for path in paths:
        u,a,b,v = path['vertices']
        for z in range(125*a,125*(a+1)):
            left = [x for x in adj[z] if x//125 == u]
            mids = [x for x in adj[z] if x//125 == b]
            right = {y for w in mids for y in adj[w] if y//125 == v}
            assert len(left)==5 and len(mids)==5 and len(right)==25
            lf,rf = flag(left),flag(right)
            clause = [z+1,-lf,-rf]
            cnf.add(*clause)
            closure_count += 1
            if [u,a,b,v] == [0,18,29,5] and z == 2250:
                assert 1 in left and 626 in right
                literal_witness = {'controller_path':[u,a,b,v],'middle_old_id':z,
                    'left_old_ids':sorted(left),'right_old_ids':sorted(right),
                    'left_OR_variable':lf,'right_OR_variable':rf,'clause':clause,
                    'controlled_rule_violation_endpoints':[1,626]}
    assert closure_count==32250 and literal_witness is not None
    stage('unique_control_geodesic_closure_including_cached_OR_gates',before)
    cnf.f.close()
    with (HERE/'model.cnf').open('w') as out, body.open() as inp:
        out.write(f'p cnf {cnf.nv} {cnf.nc}\n')
        shutil.copyfileobj(inp,out)
    body.unlink()
    metadata = {
        'status':'PREPARED_NOT_SOLVED','variables':cnf.nv,'clauses':cnf.nc,
        'keep_variables':3750,'keep_variable_rule':'old vertex v corresponds to DIMACS v+1',
        'n_at_least':1921,'n_exactly_fixed':False,'max_degree':16,
        'conditional_degree_counter':'exact at-least-four-deleted threshold; only selected centers require it',
        'global_cardinality':'balanced exact binary addition and constant comparator',
        'sum_bits_little_endian':sum_bits,
        'controller_unique_distance3_pairs_ordered':len(paths),
        'closure_clauses':closure_count,
        'equivalent_uncompressed_intermediate_implications':closure_count*125,
        'unique_OR_sets_by_size':dict(sorted(cache_sizes.items())),
        'stages':stages,'literal_controlled_counterexample_clause':literal_witness,
        'source_edge_table_reads':0,'source_adjacency_cache_reads':1,
        'BFS_runs':0,'solver_calls':0,'new_graphs_generated':0,
        'necessary_only':True,
        'SAT_requires_actual_induced_D3_check':True,
        'CPU_seconds':time.process_time()-start,
        'byteorder':sys.byteorder,
    }
    (HERE/'MODEL.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps({k:metadata[k] for k in ['status','variables','clauses','closure_clauses',
          'unique_OR_sets_by_size','stages','CPU_seconds']}))

if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Read one saved graph; diagnose pairwise cycle budgets. No BFS or search."""
from pathlib import Path
from itertools import combinations
from math import comb
from collections import Counter
import json, time

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'petersen_all_matchings_run/candidate.best.edges'

def main():
    started = time.process_time()
    lines = [list(map(int, line.split())) for line in SOURCE.read_text().splitlines() if line.strip()]
    assert lines[0] == [60, 240] and len(lines[1:]) == 240
    adj = [set() for _ in range(60)]
    for u, v in lines[1:]:
        assert u != v and v not in adj[u]
        adj[u].add(v); adj[v].add(u)
    assert all(len(row) == 8 for row in adj)
    internal = [[{v % 10 for v in adj[10*i+u] if v//10 == i} for u in range(10)] for i in range(6)]
    matching = {}
    for i in range(6):
        for u in range(10):
            assert len(internal[i][u]) == 3
            for v in range(u+1, 10):
                assert len(internal[i][u] & internal[i][v]) == (0 if v in internal[i][u] else 1)
        for j in range(6):
            if i == j: continue
            image = []
            for u in range(10):
                targets = [v % 10 for v in adj[10*i+u] if v//10 == j]
                assert len(targets) == 1
                image.append(targets[0])
            assert sorted(image) == list(range(10))
            matching[i,j] = image

    def walk(fibers, u):
        for a, b in zip(fibers, fibers[1:]):
            u = matching[a,b][u]
        return u

    triples = {}
    for i, j, k in combinations(range(6), 3):
        t = sum(walk([i,j,k,i],u) == u for u in range(10))
        a = {}
        for x, y, z in [(i,j,k),(j,k,i),(k,i,j)]:
            a[x] = sum(walk([x,y,z,x],u) in internal[x][u] for u in range(10))
        triples[i,j,k] = {'fibers':[i,j,k], 'triangles':t, 'three_fiber_squares_by_internal_fiber':a}

    opposite = {}
    for a,b,c,d in combinations(range(6), 4):
        for i,j,k,l in [(a,b,c,d),(a,c,b,d),(a,d,b,c)]:
            opposite[(i,j),(k,l)] = sum(walk([i,k,j,l,i],u) == u for u in range(10))

    rows=[]; qsum=0
    for i,j in combinations(range(6),2):
        m=matching[i,j]
        q=sum(m[v] in internal[j][m[u]] for u in range(10) for v in internal[i][u] if u<v)
        t=0; a=0
        for k in range(6):
            if k in (i,j):continue
            triple=triples[tuple(sorted((i,j,k)))];t+=triple['triangles']
            a+=triple['three_fiber_squares_by_internal_fiber'][i]+triple['three_fiber_squares_by_internal_fiber'][j]
        required=10-2*q-t-a
        actual=sum(count for pair,count in opposite.items() if (i,j) in pair)
        bad=[];crowded=[];slot_histogram=Counter();direct_energy=0
        for u in range(10*i,10*i+10):
            for v in range(10*j,10*j+10):
                common=sorted(adj[u]&adj[v]); edge=int(v in adj[u]);slots=len(common)+edge
                slot_histogram[slots]+=1
                direct_energy+=comb(len(common),2)+edge*len(common)
                if slots==0:bad.append([u,v])
                if slots>=3:crowded.append({'pair':[u,v],'route_slots':slots,'common_neighbors':common,
                                           'penalty':comb(slots-1,2)})
        direct_energy-=10
        assert direct_energy==actual-required==len(bad)+sum(x['penalty'] for x in crowded)
        assert direct_energy>=0
        rows.append({'fibers':[i,j],'q':q,'triangles_using_interface':t,
                     'three_fiber_square_opposites':a,'required_four_fiber_opposites_r':required,
                     'actual_four_fiber_opposites':actual,'pair_energy':direct_energy,
                     'route_slot_histogram':dict(sorted(slot_histogram.items())),
                     'bad_pairs':bad,'crowded_pairs':crowded})
        qsum+=q

    triangle_total=sum(t['triangles'] for t in triples.values())
    square3=sum(sum(t['three_fiber_squares_by_internal_fiber'].values()) for t in triples.values())
    square4=sum(opposite.values());square_total=qsum+square3+square4
    assert triangle_total==sum(len(adj[u]&adj[v]) for u in range(60) for v in adj[u] if u<v)//3
    assert 2*square_total==sum(comb(len(adj[u]&adj[v]),2) for u,v in combinations(range(60),2))
    r={tuple(row['fibers']):row['required_four_fiber_opposites_r'] for row in rows}
    total=sum(r.values());tests=[]
    tests.append({'condition':'all_r_nonnegative','passes':min(r.values())>=0})
    tests.append({'condition':'sum_r_even','passes':total%2==0,'sum_r':total})
    for e,value in r.items():
        partners=sum(v for f,v in r.items() if not set(e)&set(f))
        tests.append({'condition':'single_pair_disjoint_partner_capacity','fibers':e,
                      'lhs':value,'rhs':partners,'passes':value<=partners})
    for i in range(6):
        value=sum(v for e,v in r.items() if i in e)
        tests.append({'condition':'star_independent_set','fiber':i,'twice_lhs':2*value,
                      'rhs':total,'passes':2*value<=total})
    for triple in combinations(range(6),3):
        value=sum(r[e] for e in combinations(triple,2))
        tests.append({'condition':'triangle_independent_set','fibers':triple,'twice_lhs':2*value,
                      'rhs':total,'passes':2*value<=total})
    report={'source':str(SOURCE),'scope':'Single saved graph diagnostic; no BFS, move search, or solver',
      'triangles':triangle_total,'two_fiber_squares':qsum,'three_fiber_squares':square3,
      'four_fiber_squares':square4,'total_squares':square_total,
      'total_pair_energy':sum(row['pair_energy'] for row in rows),
      'bad_pairs':sum(len(row['bad_pairs']) for row in rows),
      'pair_budgets':rows,'triple_counts':list(triples.values()),
      'four_fiber_counts':[{'opposite_fiber_pairs':pair,'count':count} for pair,count in opposite.items()],
      'simple_KG_checks':tests,'all_simple_KG_checks_pass':all(x['passes'] for x in tests),
      'cpu_seconds':time.process_time()-started}
    (HERE/'petersen_pair_cycle_budget.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('triangles','two_fiber_squares','three_fiber_squares',
          'four_fiber_squares','total_pair_energy','bad_pairs','all_simple_KG_checks_pass','cpu_seconds')},indent=2))
    for row in rows:
        print(row['fibers'],'q',row['q'],'t',row['triangles_using_interface'],'a',row['three_fiber_square_opposites'],
              'r',row['required_four_fiber_opposites_r'],'actual',row['actual_four_fiber_opposites'],'E',row['pair_energy'])

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact affine-composition coefficients for saved slope-only survivors.

All intercepts remain formal. No field assignment, graph, or BFS is used.
"""
import json
import time
from pathlib import Path
from collections import Counter

OUT=Path(__file__).resolve().parent
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


def forms(q,mults,uvw):
    slopes=[[1]*4 for _ in range(4)]
    for (u,v),s in zip([(1,2),(1,3),(2,3)],uvw):
        slopes[u][v]=s
        slopes[v][u]=pow(s,-1,q)
    edges=[]
    for pair,n in zip(PAIRS,mults):
        edges.extend([pair]*n)
    E=len(edges)
    tree=[]
    for pair in [(0,1),(0,2),(0,3)]:
        tree.append(edges.index(pair))
    free=[e for e in range(E) if e not in tree]
    adj=[[] for _ in range(4)]
    for e,(u,v) in enumerate(edges):
        a=slopes[u][v]
        ai=pow(a,-1,q)
        adj[u].append((2*e,v,e,a,1))
        adj[v].append((2*e+1,u,e,ai,-ai % q))
    roots=[]
    for source in range(4):
        raw=[{} for _ in range(4)]
        gauged=[{} for _ in range(4)]
        depths=[0]*4
        def visit(vertex,A,B,depth,last):
            depths[depth]+=1
            raw[vertex].setdefault(A,set()).add(B)
            gauged[vertex].setdefault(A,set()).add(tuple(B[e] for e in free))
            if depth==3:
                return
            for dart,target,e,a,bcoef in adj[vertex]:
                if last>=0 and dart==(last^1):
                    continue
                Bnext=[a*c % q for c in B]
                Bnext[e]=(Bnext[e]+bcoef)%q
                visit(target,a*A%q,tuple(Bnext),depth+1,dart)
        visit(source,1,(0,)*E,0,-1)
        d=len(adj[source])
        assert depths==[1,d,d*(d-1),d*(d-1)**2]
        counts=[{a:len(ff) for a,ff in rr.items()} for rr in raw]
        gcounts=[{a:len(ff) for a,ff in rr.items()} for rr in gauged]
        assert counts==gcounts
        roots.append(counts)
    return roots


def main():
    start=time.process_time()
    data=json.loads((OUT/'SLOPE_CAPACITY.json').read_text())
    families=[]
    for result in data['results']:
        q=result['field_order']
        mults=result['cross_multiplicities']
        rows=[]
        for survivor in result['survivors']:
            uvw=survivor['cycle_slopes_12_13_23']
            exact=forms(q,mults,uvw)
            for k,(i,j) in enumerate(PAIRS):
                direct=1 if i==0 else uvw[[(1,2),(1,3),(2,3)].index((i,j))]
                assert exact[i][j][direct]==survivor['direct_direction_capacity_by_unordered_pair'][k]
            self_counts=[exact[i][i] for i in range(4)]
            if uvw==[1,1,1]:
                category='FLAT_NOT_EXCLUDED'
                expected_self={1:55 if q==31 else 83}
            elif uvw==[q-1,q-1,q-1]:
                category='EXCLUDED_TWO_INCOMPLETE_DIRECTIONS'
                expected_self={1:7 if q==31 else 11,q-1:24 if q==31 else 36}
            else:
                assert q==43
                t=uvw[0]
                assert uvw in [[t,t,t],[t,t,pow(t,-1,q)],[t,pow(t,-1,q),pow(t,-1,q)]]
                category='EXCLUDED_7_BY_7_INTERPOLATION'
                expected_self={1:11,t:36,pow(t,-1,q):36}
            assert all(c==expected_self for c in self_counts)
            rows.append({'cycle_slopes_12_13_23':uvw,'category':category,
                         'self_direction_form_counts_by_root':self_counts,
                         'all_root_target_direction_form_counts':exact})
        families.append({'field_order':q,'cross_multiplicities':mults,
                         'saved_slope_survivors_checked':len(rows),
                         'categories':dict(Counter(r['category'] for r in rows)),
                         'survivors':rows})
    output={'status':'COMPLETE','running':False,'families':families,
            'all_raw_and_tree_gauge_counts_equal':True,
            'all_offdiagonal_direct_counts_match_path_type_formula':True,
            'CPU_seconds':time.process_time()-start,
            'translation_assignments':0,'generated_graphs':0,'BFS_roots':0}
    (OUT/'SURVIVOR_FORM_CHECK.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'CPU_seconds':output['CPU_seconds'],
                     'families':[{k:f[k] for k in ['field_order','saved_slope_survivors_checked','categories']} for f in families]},indent=2))


if __name__=='__main__':
    main()

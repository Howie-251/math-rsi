"""All actual h6 distinct-W-port graphs modulo two genuine W matchings.

Build/prepare only; no solver call. No fixed third permutation or parent colors.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('reviewed_nonadj_cnf', HERE.parent/'nonadjacent_double46_full61_run'/'encode.py')
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)
CNF, neg, truth = lib.CNF, lib.neg, lib.truth
pair, count_thresholds, lex_nonincreasing = lib.pair, lib.count_thresholds, lib.lex_nonincreasing
N=61
S=list(range(2,5)); U=list(range(5,10)); V=list(range(10,15))
W=[list(range(15+6*i,21+6*i)) for i in range(3)]
WW=sum(W,[]); C=list(range(33,61))
UV={(5,11),(5,12),(6,10),(7,10),(8,13),(9,14)}
SCOPE=('All actual61 graphs in the triangle-free isolated nonadjacent double-root '
       'h6 distinct-R-port branch: W perfect matchings and UV=2P3+2K2 inherited '
       'from local paper proofs; all third matchings, port locations, parent colors '
       'and actual C-W/C-C edges jointly free. Other n61 branches remain open.')


def build():
    em=CNF()
    fixed=({(0,x) for x in S+U}|{(1,x) for x in S+V}|UV
           |{(s,w) for s,group in zip(S,W) for w in group}
           |{(W[0][i],W[j][i]) for i in range(6) for j in (1,2)})
    allowed=({(p,r) for p in U+V for r in WW+C}
             |{(a,b) for a in W[1] for b in W[2]}
             |{(w,c) for w in WW for c in C}|set(combinations(C,2)))
    free={ab:em.var() for ab in sorted(allowed)}
    primary_count=em.nv
    assert primary_count==1378 and len(fixed)==52
    def edge(a,b):
        if a==b: return False
        ab=pair(a,b)
        return True if ab in fixed else free.get(ab,False)
    full_edges={ab:edge(*ab) for ab in combinations(range(N),2)}
    def front():
        for a in W[1]: em.exact([edge(a,b) for b in W[2]],1)
        for b in W[2]: em.exact([edge(a,b) for a in W[1]],1)
        for parents in (U,V):
            em.exact([edge(p,w) for p in parents for w in WW],1)
            for c in C: em.exact([edge(p,c) for p in parents],1)
        for w in WW: em.at_most([edge(p,w) for p in U+V],1)
        for c in C:
            for group in W: em.at_least([edge(w,c) for w in group],1)
            em.at_most([edge(w,c) for w in WW],5)
    em.section('complete_h6_frontend',front)
    em.section('all_original_degrees_8',lambda:[em.exact([edge(a,b) for b in range(N) if b!=a],8) for a in range(N)])
    common_terms={};thresholds={};covered={}
    def definitions():
        for a,b in combinations(range(N),2):
            terms=[em.gate('and',[edge(a,w),edge(b,w)]) for w in range(N) if w not in (a,b)]
            common_terms[a,b]=terms
            thresholds[a,b]=count_thresholds(em,terms,4)
            covered[a,b]=em.gate('or',[edge(a,b),thresholds[a,b][1]])
    em.section('exact_common_and_coverage_definitions',definitions)
    em.section('all_1830_original_pairs_covered',lambda:[em.add(lit) for lit in covered.values()])
    em.section('global_common_at_most_3',lambda:[em.add(neg(t[4])) for t in thresholds.values()])
    em.section('adjacent_common_at_most_1',lambda:[em.add(neg(full_edges[ab]),neg(t[2])) for ab,t in thresholds.items()])
    em.section('selected_roots_no_other_double',lambda:[em.add(neg(t[3])) for ab,t in thresholds.items() if (0 in ab or 1 in ab) and ab!=(0,1)])
    em.section('C_parent_vectors_nonincreasing_lex',lambda:[lex_nonincreasing(em,[edge(p,a) for p in U+V],[edge(p,b) for p in U+V]) for a,b in zip(C,C[1:])])
    return dict(em=em,fixed=fixed,free=free,primary_count=primary_count,full_edges=full_edges,
                common_terms=common_terms,thresholds=thresholds,covered=covered)

assignment=lib.assignment
rejected_groups=lib.rejected_groups
save=lib.save

def prepare():
    assert not any((HERE/name).exists() for name in ('input.cnf','encoding.json','variable_map.json'))
    model=build();em=model['em']
    with (HERE/'input.cnf').open('w') as f:
        f.write(f'p cnf {em.nv} {len(em.clauses)}\n')
        for row in em.clauses: f.write(' '.join(map(str,row))+' 0\n')
    save(HERE/'variable_map.json',dict(n=N,fixed_edges=sorted(model['fixed']),free_edges=[[a,b,v] for (a,b),v in model['free'].items()]))
    info=dict(status='PREPARED_NOT_RUN',scope=SCOPE,variables=em.nv,clauses=len(em.clauses),primary_edge_variables=model['primary_count'],fixed_original_edges=len(model['fixed']),covered_original_pairs=1830,groups={name:dict(start=a,stop=b,clauses=b-a) for name,(a,b) in em.groups.items()},solver_calls=0,proof_logging=False,symmetry='Two actual W matchings transported to identity; all 720 third permutations retained; C-only parent lex',forbidden_extra_restrictions='No fixed a/b positions or parents, no W father-color sorting, no regular-color-extraction assumption')
    save(HERE/'encoding.json',info);print(json.dumps(info,indent=2))

def decode():
    # The reused decoder reads only saved CNF/edge maps and uses no old geometry.
    old=lib.HERE
    try:
        lib.HERE=HERE
        lib.decode()
    finally:
        lib.HERE=old

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('prepare','decode'))
    args=parser.parse_args()
    prepare() if args.action=='prepare' else decode()

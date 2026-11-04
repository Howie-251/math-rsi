"""Independent raw-geometry appendix; never imports a producer/checker.
Writes only its own check JSON. Theorems are imported from scoped reviews.
"""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
from datetime import datetime,timezone
import hashlib,json

R=Path(__file__).resolve().parent
OLD={13,14,19,31,32,35,37,38}
NEW={2,7,10,44}
def load(n): return json.loads((R/n).read_text(encoding='utf-8'))
def sha(n): return 'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
def require(p,m):
    if not p: raise ValueError(m)
def main():
    core_report=load('T15_BALANCED_BRIDGE_REVIEW.json')
    require(core_report['verdict']=='PASS','four-core semantic review')
    for n,h in core_report['audited_input_hashes'].items():
        require(sha(n)==h,'core input became stale: '+n)
    protected={n:sha(n) for n in ['T15_BALANCED_BRIDGE_FOUR_CORES.md','T15_BALANCED_BRIDGE_REVIEW.md','T15_BALANCED_BRIDGE_REVIEW.json','T15_BALANCED_BRIDGE_independent_check.py','T15_BALANCED_BRIDGE_independent_check.json']}
    geometry=load('t15_analytic_geometry.json')['T15']['residual_orbits']
    lookup={}
    for core,row in enumerate(geometry):
        require(len({0,*row['avoided'],*row['included']})==6,'core six distinct holes')
        for perm in permutations(range(5)):
            # Destination-to-source coordinates; inverse convention to producer.
            def tr(v): return sum(((v>>p)&1)<<k for k,p in enumerate(perm))
            key=(tuple(sorted(tr(v) for v in row['avoided'])),tuple(sorted(tr(v) for v in row['included'])))
            require(key not in lookup or lookup[key]==core,'overlapping core orbit')
            lookup[key]=core
    patterns=Counter(); projected_hist=Counter(); source_count=Counter(); covered_count=Counter(); leftover_count=Counter(); nochoices=Counter()
    retained_rows=[]; hashes={}; total_projections=0
    for target in (1,7,31):
        n=f'remaining_eight_after_single_face_{target}.bin'; hashes[n]=sha(n)
        raw=(R/n).read_bytes(); require(len(raw)%7==0,'source alignment')
        seen=set(); expected_bin=[]
        for off in range(0,len(raw),7):
            rec=raw[off:off+7]; z=tuple(rec[:3]); w=tuple(rec[3:])
            require(rec not in seen,'source duplicate'); seen.add(rec)
            require(z==tuple(sorted(z)) and w==tuple(sorted(w)),'source canonical order')
            require(len({0,*z,*w})==8 and target not in {0,*z,*w},'source/target distinct')
            require(all(v<64 and v.bit_count()%2==0 for v in z),'even Z')
            require(all(v<64 and v.bit_count()%2==1 for v in w),'odd W')
            require(all((a^b).bit_count()!=1 for a in z for b in w),'source preprocessing')
            choices=set()
            for cut in range(6):
                same=lambda v: ((v^target)>>cut)&1==0
                za=[v for v in z if same(v)]; wa=[v for v in w if same(v)]
                require((len(za),len(wa))!=(1,4),'a1b4 should already close')
                if (len(za),len(wa))!=(2,1): continue
                total_projections+=1
                root=next(v for v in z if not same(v))
                coords=[i for i in range(6) if i!=cut]
                def project(v): return sum((((v^root)>>coord)&1)<<k for k,coord in enumerate(coords))
                # Translate within opposite face; avoid holes have been mirrored.
                forbidden=tuple(sorted(project(v^(1<<cut)) for v in za))
                retained=tuple(sorted(project(v) for v in w if not same(v)))
                require(all(v.bit_count()%2==1 for v in forbidden+retained),'T15 majority parity')
                require((forbidden,retained) in lookup,'residual T15 lookup')
                core=lookup[forbidden,retained]; choices.add(core); projected_hist[core]+=1
            require(not choices&OLD,'previously closed core in source')
            source_count[target]+=1
            if choices&NEW: covered_count[target]+=1
            else:
                expected_bin.append(rec); leftover_count[target]+=1
                retained_rows.append(dict(target=target,Z=list(z),W=list(w),core_choices=sorted(choices)))
                if choices: patterns[tuple(sorted(choices))]+=1
                else: nochoices[target]+=1
        n=f'remaining_eight_after_balanced_bridge_{target}.bin'; hashes[n]=sha(n)
        saved=(R/n).read_bytes()
        require(saved==b''.join(expected_bin),'new binary differs from independently filtered raw sequence')
    forced={p[0] for p in patterns if len(p)==1}
    residual={frozenset(p) for p in patterns if not forced.intersection(p)}
    groups=[]
    while residual:
        constraints={residual.pop()}; vertices=set(next(iter(constraints)))
        while True:
            adjacent={s for s in residual if s&vertices}
            if not adjacent: break
            constraints|=adjacent; residual-=adjacent
            vertices|=set.union(*(set(s) for s in adjacent))
        common=set.intersection(*(set(s) for s in constraints))
        require(bool(common),'group cannot be covered by one extra core')
        groups.append(dict(vertices=sorted(vertices),constraints=sorted(map(sorted,constraints)),common=sorted(common)))
    require(all(not forced.intersection(g['vertices']) for g in groups),'forced/group disjoint')
    require(all(not set(a['vertices'])&set(b['vertices']) for a,b in combinations(groups,2)),'group disjoint')
    selected=forced|{min(g['common']) for g in groups}
    require(all(selected.intersection(p) for p in patterns),'upper bound cover')
    result=dict(previous_remaining=sum(source_count.values()),newly_covered=sum(covered_count.values()),
        newly_by_target={str(v):covered_count[v] for v in (1,7,31)},remaining=sum(leftover_count.values()),
        remaining_by_target={str(v):leftover_count[v] for v in (1,7,31)},remaining_with_a2b1=sum(patterns.values()),
        remaining_without_a2b1=sum(nochoices.values()),coordinate_projections=total_projections,
        proved_T15_core_orbits=sorted(OLD|NEW),additional_sufficient_cores=sorted(selected),
        minimum_additional_whole_orbit_cover=len(forced)+len(groups),remaining_choice_patterns=[list(p) for p in sorted(patterns)])
    producer=load('eight_after_balanced_bridge_check.json')
    for k,v in result.items(): require(producer[k]==v,'producer numerical mismatch: '+k)
    for n,h in producer['source_hashes'].items(): require(sha(n)=='sha256:'+h,'producer stale source hash')
    candidates=load('eight_after_balanced_bridge_candidates.json')
    require(candidates['rows']==retained_rows,'producer candidate row mismatch')
    for k,v in result.items(): require(candidates[k]==v,'candidate metadata mismatch')
    require(result['previous_remaining']==33638 and result['coordinate_projections']==94779,'recomputed source/projection counts')
    require(result['newly_covered']==12288 and result['remaining']==21350,'recomputed filter count')
    for n in ['t15_analytic_geometry.json','eight_after_balanced_bridge_check.py','eight_after_balanced_bridge_check.json','eight_after_balanced_bridge_candidates.json',Path(__file__).name]: hashes[n]=sha(n)
    for n,h in protected.items(): require(sha(n)==h,'protected four-core file changed')
    out=dict(status='PASS',audit_skill='proof-checker',reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',fork_turns='none',
        review_independence='same-family',acceptance_status='provisional',generated_at=datetime.now(timezone.utc).isoformat(),
        source='Three raw after_single_face binaries; no saved core-map used',numbers=result,
        forced_singleton_cores=sorted(forced),remaining_constraint_groups=groups,choice_pattern_multiplicities={','.join(map(str,p)):n for p,n in sorted(patterns.items())},
        without_a2b1_by_target={str(v):nochoices[v] for v in (1,7,31)},projected_core_histogram=dict(sorted(projected_hist.items())),
        binary_comparison='exact byte equality in all three output binaries',candidate_rows_compared=len(retained_rows),
        mathematical_scope='Normalized marked hole geometries; conditional on previously imported eight-core theorem, plus separately audited four-core theorem. Not counts of arbitrary matchings or realizability.',
        full_T15_proved=False,full_eight_hole_proved=False,full_P6_proved=False,
        audited_input_hashes=hashes,protected_core_hashes=protected,author_checker_imported=False)
    (R/'T15_BALANCED_BRIDGE_CONSEQUENCES_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status=out['status'],numbers=result,forced=sorted(forced),groups=groups)))
if __name__=='__main__': main()

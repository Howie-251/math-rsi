"""Scoped independent audit. Does not import producers or other checkers.

Geometry is regenerated from raw after-a1b4 inputs, not core_map.json.
Q4 certificates are parsed and checked directly. Writes only its own JSON.
"""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json

R = Path(__file__).resolve().parent
CORES = {13, 14, 19, 31, 32, 35, 37, 38}
ODD = {x for x in range(16) if x.bit_count() % 2}
N = {1, 2, 4, 8}
D3 = ODD - N


def require(x, message):
    if not x:
        raise ValueError(message)


def sha(name):
    return hashlib.sha256((R / name).read_bytes()).hexdigest()


def load(name):
    return json.loads((R / name).read_text(encoding='utf-8'))


def edge(a, b):
    return tuple(sorted((a, b)))


def mate_edges(mate, holes):
    require(len(mate) == 16, 'mate array length')
    require({x for x in range(16) if mate[x] == 255} == holes, 'mate holes')
    support = set(range(16)) - holes
    require(all(mate[x] in support and mate[x] != x and mate[mate[x]] == x
                for x in support), 'mate involution')
    return tuple((x, mate[x]) for x in sorted(support) if x < mate[x])


def walk_ok(w, matching, support, closed):
    require(len(w) == len(support) and set(w) == support, 'walk exact distinct support')
    es = {edge(w[i], w[(i + 1) % len(w)]) for i in range(len(w) if closed else len(w)-1)}
    require(set(matching) <= es, 'mandatory edges')
    require(all((a ^ b).bit_count() == 1 for a, b in es - set(matching)), 'optional shortness')


def no_short_completion(m, support):
    """Enumerate disjoint short perfect complements by smallest unmatched vertex."""
    forbidden = set(m)
    hist = Counter()

    def visit(left, added):
        if left:
            a = min(left)
            for j in range(4):
                b = a ^ (1 << j)
                if b in left and edge(a, b) not in forbidden:
                    visit(left - {a, b}, added + [(a, b)])
            return
        graph = {x: [] for x in support}
        for a, b in list(m) + added:
            graph[a].append(b)
            graph[b].append(a)
        require(all(len(v) == 2 for v in graph.values()), 'complement degrees')
        unseen = set(support)
        count = 0
        while unseen:
            count += 1
            pending = [unseen.pop()]
            while pending:
                for b in graph[pending.pop()]:
                    if b in unseen:
                        unseen.remove(b)
                        pending.append(b)
        require(count > 1, 'negative table counterexample')
        hist[count] += 1

    visit(set(support), [])
    return dict(sorted(hist.items()))


def q4_certificates():
    negative = {}
    negative_details = []
    positive_count = 0
    for y in (1, 7):
        name = f'q4_distance{y.bit_count()}_avoided_table.bin'
        raw = (R / name).read_bytes()
        require(len(raw) == 135135 * 30, 'circle table length')
        seen = set()
        negative[y] = set()
        for off in range(0, len(raw), 30):
            m = mate_edges(raw[off:off+16], {0, y})
            require(m not in seen, 'circle duplicate')
            seen.add(m)
            w = raw[off+16:off+30]
            if w == bytes([255])*14:
                negative[y].add(m)
                negative_details.append(dict(y=y, matching=m,
                    complement_component_counts=no_short_completion(m, set(range(16))-{0,y})))
            else:
                walk_ok(w, m, set(range(16))-{0,y}, True)
                positive_count += 1
        # Exactly 13!! possible matchings on this 14-vertex support.
        require(len(seen) == 135135, 'complete circle universe')
    require([len(negative[y]) for y in (1, 7)] == [51, 53], 'negative counts')

    p4 = list(permutations(range(4)))
    maps = [tuple(sum(((x >> j)&1) << p[j] for j in range(4)) for x in range(16)) for p in p4]
    badtables = {}
    for y in ODD:
        base = 1 if y in N else 7
        tr = next(tr for tr in maps if tr[base] == y)
        badtables[y] = {tuple(sorted(edge(tr[a],tr[b]) for a,b in m)) for m in negative[base]}
    candidates = set()
    inverse_instances = 0
    for y, rows in badtables.items():
        for m in rows:
            for e in m:
                for a,b in (e,e[::-1]):
                    candidates.add(tuple(sorted((set(m)-{e})|{edge(0,a),edge(y,b)})))
                    inverse_instances += 1
    badhist, d3hist = Counter(), Counter()
    for m in candidates:
        mate = {a:b for u,v in m for a,b in ((u,v),(v,u))}
        bad = set()
        for y in ODD:
            if mate[0] == y:
                bad.add(y)
            else:
                a,b = mate[0],mate[y]
                reduced = tuple(sorted((set(m)-{edge(0,a),edge(y,b)})|{edge(a,b)}))
                if reduced in badtables[y]:
                    bad.add(y)
        require(len(ODD-bad) >= 4 and (D3-bad), 'universal endpoint bound on exceptional universe')
        badhist[len(bad)] += 1
        d3hist[len(D3-bad)] += 1

    families = []
    reps = ((1,2),(2,4),(1,14),(2,14))
    for v,w in reps:
        raw = (R/f'q4_t15_path_abundance_{v}_{w}.bin').read_bytes()
        seen, hist = set(), Counter()
        off = paths = triangle = 0
        holes = {0,7,11,13,v,w}
        while off < len(raw):
            require(off+17 <= len(raw), 'A row header')
            m = mate_edges(raw[off:off+16], holes)
            require(m not in seen, 'A duplicate')
            seen.add(m)
            k = raw[off+16]
            off += 17
            require(off+14*k <= len(raw), 'A row payload')
            endpoints = set()
            for _ in range(k):
                walk = raw[off:off+14]
                off += 14
                walk_ok(walk,m,set(range(16))-{v,w},False)
                require(walk[0] == 0 and walk[-1] in ODD-{v,w}, 'A endpoints')
                require(walk[-1] not in endpoints, 'A distinct endpoints')
                endpoints.add(walk[-1])
                paths += 1
            is_triangle = {v,w} <= N and tuple(sorted(N-{v,w})) in m
            if is_triangle:
                require(D3 <= endpoints, 'A triangle endpoint lower bound')
                triangle += 1
            else:
                require(endpoints == ODD-{v,w}, 'A nontriangle endpoint lower bound')
            hist[k] += 1
        # Every row is a distinct matching on the same ten vertices; 9!!=945.
        require(off == len(raw) and len(seen) == 945, 'complete A universe')
        families.append(dict(avoid=[v,w],records=len(seen),paths=paths,
                             triangular=triangle,endpoint_histogram=dict(hist)))
    orbits = [{(frozenset(tr[x] for x in (7,11,13)),frozenset(tr[x] for x in rep))
               for tr in maps} for rep in reps]
    geom = Counter()
    for holes in combinations(ODD,5):
        for pair in combinations(holes,2):
            available = frozenset(holes)-set(pair)
            if available & N:
                geom['adjacent'] += 1
            else:
                hits = [i for i,o in enumerate(orbits) if (available,frozenset(pair)) in o]
                require(len(hits)==1,'complete unique residual geometry orbit')
                geom[str(reps[hits[0]])] += 1
    # Directly verify the endpoint intersection implications on all lower-bound sets.
    for good in combinations(ODD,4):
        if set(good)&D3:
            require(set(good)&D3,'triangle intersection')
            for omitted in combinations(ODD,2):
                require(len(set(good)&(ODD-set(omitted)))>=2,'nontriangle intersection')
    return dict(circle_positives=positive_count,negative_count=len(negative_details),
                negative_details=negative_details,inverse_instances=inverse_instances,
                exceptional_perfect_matchings=len(candidates),bad_histogram=dict(badhist),
                good_d3_histogram=dict(d3hist),path_families=families,geometry=dict(geom),
                outside_candidate_bound='Only possible bad endpoint is root partner; >=7 good, >=3 distance-three')


def geometry_consequences():
    source = load('t15_analytic_geometry.json')['T15']['residual_orbits']
    lookup = {}
    for core,row in enumerate(source):
        require(len(set(row['avoided']+row['included']+[0])) == 6,'source holes distinct')
        for perm in permutations(range(5)):
            tr = lambda x: sum(((x >> perm[j])&1) << j for j in range(5))
            key = (tuple(sorted(tr(x) for x in row['avoided'])),
                   tuple(sorted(tr(x) for x in row['included'])))
            require(key not in lookup or lookup[key]==core,'source orbit overlap')
            lookup[key] = core
    patterns, newly, after, exceptions = Counter(), Counter(), Counter(), Counter()
    all_keys = set()
    cuts = 0
    for target in (1,7,31):
        raw = (R/f'remaining_eight_after_a1b4_{target}.bin').read_bytes()
        require(len(raw)%7==0,'raw length')
        retained = set()
        for off in range(0,len(raw),7):
            record = raw[off:off+7]
            z,w = tuple(record[:3]),tuple(record[3:])
            key = (target,tuple(sorted(z)),tuple(sorted(w)))
            require(key not in all_keys,'raw duplicate')
            all_keys.add(key)
            require(len({0,*z,*w})==8 and target not in {0,*z,*w},'raw holes distinct from target')
            require(all(x<64 and x.bit_count()%2==0 for x in z),'Z parity/range')
            require(all(x<64 and x.bit_count()%2 for x in w),'W parity/range')
            require(all((a^b).bit_count()!=1 for a in z for b in w),'preprocessed Z-W nonadjacency')
            choices = set()
            for cut in range(6):
                inface = lambda x: ((x^target)>>cut)&1 == 0
                za,wa = [x for x in z if inface(x)],[x for x in w if inface(x)]
                require(not(len(za)==1 and len(wa)==4),'raw excludes a1b4')
                if (len(za),len(wa)) != (2,1):
                    continue
                cuts += 1
                root = next(x for x in z if not inface(x))
                coords = [j for j in range(6) if j!=cut]
                # First move two avoided holes to root's face; then drop coordinate
                # using explicit coordinate lists and translate by minority root.
                project = lambda x: sum((((x^root)>>j)&1) << k for k,j in enumerate(coords))
                avoided = tuple(sorted(project(x^(1<<cut)) for x in za))
                included = tuple(sorted(project(x) for x in w if not inface(x)))
                require(all(x.bit_count()%2 for x in avoided+included),'projected parity')
                require((avoided,included) in lookup,'projected core missing')
                choices.add(lookup[(avoided,included)])
            if choices & CORES:
                newly[target] += 1
            else:
                retained.add((tuple(sorted(z)),tuple(sorted(w))))
                if choices:
                    after[target] += 1
                    patterns[tuple(sorted(choices))] += 1
                else:
                    exceptions[target] += 1
        saved = (R/f'remaining_eight_after_single_face_{target}.bin').read_bytes()
        require(len(saved)%7==0,'new bin length')
        saved_keys = [(tuple(sorted(saved[o:o+3])),tuple(sorted(saved[o+3:o+7])))
                      for o in range(0,len(saved),7)]
        require(len(saved_keys)==len(set(saved_keys)),'new bin duplicates')
        require(set(saved_keys)==retained,'new bin exact set equality')
    forced = {p[0] for p in patterns if len(p)==1}
    todo = {frozenset(p) for p in patterns if not forced.intersection(p)}
    groups = []
    while todo:
        edges = {todo.pop()}
        vertices = set(next(iter(edges)))
        while True:
            adjacent = {e for e in todo if e & vertices}
            if not adjacent:
                break
            edges |= adjacent
            todo -= adjacent
            vertices |= set.union(*(set(e) for e in adjacent))
        common = set.intersection(*(set(e) for e in edges))
        require(common,'one selected core per connected constraint group suffices')
        groups.append(dict(vertices=sorted(vertices),constraints=sorted(map(sorted,edges)),
                           common_choices=sorted(common),selected=min(common)))
    selected = forced | {g['selected'] for g in groups}
    require(all(selected.intersection(p) for p in patterns),'upper-bound cover')
    require(all(not forced.intersection(g['vertices']) for g in groups),'forced/group disjoint')
    require(all(not set(a['vertices'])&set(b['vertices']) for a,b in combinations(groups,2)),
            'group pairwise disjoint')
    actual = dict(previous_remaining=len(all_keys),newly_covered=sum(newly.values()),
                  remaining=sum(after.values())+sum(exceptions.values()),
                  remaining_with_a2b1=sum(after.values()),remaining_without_a2b1=sum(exceptions.values()),
                  newly_by_target={str(k):v for k,v in newly.items()},
                  remaining_by_target={str(k):after[k]+exceptions[k] for k in (1,7,31)},
                  remaining_choice_patterns=[list(p) for p in sorted(patterns)],
                  forced_remaining_cores=sorted(forced),minimum_additional_core_cover=len(forced)+len(groups),
                  selected_additional_cores=sorted(selected))
    producer = load('eight_after_single_face_cores.json')
    for k,v in actual.items():
        require(producer[k]==v,'producer mismatch: '+k)
    require(set(producer['closed_core_candidates'])==CORES,'candidate core set')
    for n,h in producer['source_hashes'].items():
        require(sha(n)==h,'producer source hash stale: '+n)
    actual.update(a2b1_cuts_checked=cuts,disjoint_groups=groups,
                  candidate_cores=sorted(CORES),raw_new_bin_sets_equal=True,
                  without_a2b1_by_target=dict(exceptions),
                  core_map_used_to_generate_choices=False,matching_realizability_checked=False)
    return actual


def main():
    prior = load('T15_SAMEFACE_ZERO_CROSSING_check.json')
    for name,h in prior['input_hashes'].items():
        require('sha256:'+sha(name)==h,'sameface saved input hash stale: '+name)
    require(sha('T15_SAMEFACE_ZERO_CROSSING_check.py')==prior['checker_sha256'], 'saved checker hash')
    t44 = load('T44_Q5_CLOSURE_REVIEW.json')
    require(t44['verdict']=='PASS','T44 import provenance')
    require(t44['audited_input_hashes']['T44_Q5_CLOSURE_DRAFT.md']=='sha256:'+sha('T44_Q5_CLOSURE_DRAFT.md'),
            'T44 theorem current hash')
    cf1 = load('A4_FACTOR_REVIEW.json')
    require(cf1['verdict']=='PASS', 'CF1 import provenance')
    require(cf1['audited_input_hashes']['A4_SPANNING_FACTOR.md']=='sha256:'+sha('A4_SPANNING_FACTOR.md'),
            'CF1 theorem current hash')
    q4 = q4_certificates()
    require(q4['bad_histogram']=={int(k):v for k,v in prior['perfect']['exceptional_bad_endpoint_histogram'].items()},
            'saved B census agreement')
    require(q4['good_d3_histogram']=={int(k):v for k,v in prior['perfect']['exceptional_good_distance_three_histogram'].items()},
            'saved B D3 agreement')
    require(q4['exceptional_perfect_matchings']==4708 and q4['inverse_instances']==5824,'B census totals')
    for own,saved in zip(q4['path_families'],prior['paths']):
        require(own['records']==saved['records'] and own['paths']==saved['paths']
                and own['triangular']==saved['triangular_records']
                and own['endpoint_histogram']=={int(k):v for k,v in saved['histogram'].items()},
                'saved A family census agreement')
    require(q4['geometry']==prior['geometry']['at_root_zero'],'saved geometry agreement')
    consequences = geometry_consequences()
    names = ['T15_SAMEFACE_ZERO_CROSSING.md','T15_SAMEFACE_ZERO_CROSSING_check.py',
             'T15_SAMEFACE_ZERO_CROSSING_check.json','T15_PRESCRIPTION_ANALYSIS.md',
             'T15_EDGE_PRESCRIPTION_REDUCTION.md','A4_SPANNING_FACTOR.md','A4_FACTOR_REVIEW.md',
             'A4_FACTOR_REVIEW.json',
             'eight_after_single_face_cores.py','eight_after_single_face_cores.json',
             't15_analytic_geometry.json',*[f'remaining_eight_after_{kind}_{v}.bin'
             for kind in ('a1b4','single_face') for v in (1,7,31)],*prior['input_hashes']]
    result = dict(status='PASS',generated_at=datetime.now(timezone.utc).isoformat(),
                  review_independence='same-family',acceptance_status='provisional',
                  semantic_scope='Sound modulo imported T44_5 and CF1; eight-core coverage conditional on separate core theorem audit',
                  q4=q4,geometry_consequences=consequences,
                  audited_input_hashes={n:'sha256:'+sha(n) for n in dict.fromkeys(names)},
                  checker_sha256=sha(Path(__file__).name),
                  full_T15_proved=False,full_eight_hole_proved=False,full_P6_proved=False)
    (R/'T15_NEW_CONSEQUENCES_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(status=result['status'],q4_positive_circles=q4['circle_positives'],
                         q4_positive_paths=sum(f['paths'] for f in q4['path_families']),
                         geometry=consequences),indent=2))


if __name__=='__main__':
    main()

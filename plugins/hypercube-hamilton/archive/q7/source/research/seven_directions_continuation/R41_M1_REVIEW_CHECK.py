"""Independent finite audit of the frozen R41 m=1 proof and data."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations
from math import comb
from pathlib import Path
from time import process_time
import json

HERE = Path(__file__).resolve().parent
PREFIX = 'R7_E16_MU3_R41_M1_'
PROOF = PREFIX + 'CLOSURE.md'
MANIFEST = PREFIX + 'CLOSURE_INPUTS.json'
PROOF_HASH = 'a94b638bd3fb09e21628dc83602ff8e78d53739bb4286f1472abc473d5ff4f29'
MANIFEST_HASH = 'f5ce8cfce2d01e0b613346c95a8c99f3aa1536266c452fa18d084ff3c73eceec'
START = process_time()
BITS = tuple(1 << i for i in range(6))
ODD = tuple(v for v in range(64) if v.bit_count() % 2)
EVEN = tuple(v for v in range(1,64) if not v.bit_count() % 2)
LOAD_KEY = tuple(sum(((v >> i)&1) << (3*i) for i in range(6)) for v in range(64))
POWERS = tuple(5**i for i in range(6))
COEFF_KEY = tuple(sum(((v >> i)&1) * POWERS[i] for i in range(6)) for v in range(64))
NEIGHBORS = {v: sum(1 << (v ^ bit) for bit in BITS) for v in ODD}
EVEN_MASK = sum(1 << v for v in EVEN)


def guard():
    assert process_time()-START < 45, '45 CPU seconds for final checker run'


def read(name):
    return json.loads((HERE / name).read_bytes())


def digest(name):
    return sha256((HERE / name).read_bytes()).hexdigest()


def loads(points):
    key = sum(LOAD_KEY[v] for v in points)
    return tuple((key >> (3*i)) & 7 for i in range(6))


def move(points, mapping):
    return tuple(sorted(mapping[v] for v in points))


def coefficient(pool, allowed, sparse):
    # In base five every load in degrees 0 to 4 is a single digit.
    layers = [Counter({0:1}),Counter(),Counter(),Counter(),Counter()]
    for v in pool:
        add = COEFF_KEY[v]
        for degree in (4,3,2,1):
            for key, number in layers[degree-1].items():
                layers[degree][key+add] += number
    assert sum(layers[4].values()) == comb(len(pool),4)
    result = [0]*5
    for key, number in layers[4].items():
        if all((key//p)%5 in a for p,a in zip(POWERS,allowed)):
            result[(key//POWERS[sparse])%5] += number
    return result


def source_check():
    from R7_E16_MU3_R41_M_GE3_REVIEW_CHECK import scalar_table

    relation = defaultdict(set)
    for a,b,c,d in scalar_table():
        if d==0 and abs(a+c-b)<=6:
            relation[c,b].add(a)
    assert sum(map(len,relation.values()))==65
    projection={c:{b for cc,b in relation if cc==c} for c in range(5)}
    assert projection[1]=={0,6,7} and projection[2]=={0,1,7}
    maps=tuple(tuple(sum(((v>>i)&1)<<j for i,j in enumerate(p)) for v in range(64))
               for p in permutations(range(6)))
    data=read(PREFIX+'PREFLIGHT.json')
    assert data['status']=='complete'
    assert all(data[k]==0 for k in ('complete_U_generated','complete_geometries_generated','plans',
                                  'original_matchings_enumerated','solver_calls','rank_runs'))
    domain={w for w in combinations(tuple(v for v in ODD if v not in BITS),4)
            if sum(c in (1,2) for c in loads(w))==1}
    covered=set()
    totals=Counter()
    groups={}
    sources={}
    details=[]
    for wi,row in enumerate(data['rows']):
        guard()
        w=tuple(row['W'])
        c=loads(w)
        assert c==tuple(row['c']) and w in domain
        orbit={move(w,g) for g in maps}
        assert not orbit&covered and orbit<=domain
        covered.update(orbit)
        stab=tuple(g for g in maps if move(w,g)==w)
        assert len(stab)==row['stabilizer_size']
        sparse,=tuple(i for i,value in enumerate(c) if value in (1,2))
        bit=BITS[sparse]
        assert sparse==row['sparse_axis'] and all(g[bit]==bit for g in stab)
        fiber={s:tuple(v for v in ODD if v not in w and bool(v & bit)==s) for s in (0,1)}
        expected={}
        raw={}
        for b_s in sorted(projection[c[sparse]]):
            sides=(combinations(fiber[0],7-b_s),tuple(combinations(fiber[1],b_s)))
            bucket=set()
            raw[str(b_s)]=comb(len(fiber[0]),7-b_s)*comb(len(fiber[1]),b_s)
            for zero in sides[0]:
                for one in sides[1]:
                    y=tuple(sorted(zero+one))
                    assert len(y)==7
                    if all(u in y for u in BITS):
                        continue
                    b=loads(y)
                    if all(bi in projection[ci] for ci,bi in zip(c,b)):
                        bucket.add(y)
            expected[b_s]=bucket
        assert raw==row['fiber_bounds_by_b'] and sum(raw.values())==row['fiber_bound']
        assert {str(k):len(v) for k,v in expected.items()}==row['labeled_Y_by_b']
        seen=defaultdict(set)
        local=Counter()
        source_b=Counter()
        coef_buckets=defaultdict(Counter)
        for yi,source in enumerate(row['source_representatives']):
            guard()
            y=tuple(source['Y'])
            b=loads(y)
            b_s=b[sparse]
            assert list(b)==source['b']
            y_orbit={move(y,g) for g in stab}
            assert y==min(y_orbit) and y_orbit<=expected[b_s] and not y_orbit&seen[b_s]
            seen[b_s].update(y_orbit)
            multiplicity=len(y_orbit)
            assert multiplicity==source['orbit_size']
            source_b[str(b_s)]+=1
            allowed=tuple(frozenset(relation[ci,bi]) for ci,bi in zip(c,b))
            assert tuple(tuple(sorted(a)) for a in allowed)==tuple(map(tuple,source['allowed_a']))
            blocked=0
            for v in y:
                blocked |= NEIGHBORS[v]
            mask=EVEN_MASK & ~blocked
            pool=tuple(v for v in EVEN if mask & (1<<v))
            assert tuple(source['U_pool'])==pool
            vector=coefficient(pool,allowed,sparse)
            assert vector==source['U_coefficients_by_a']
            number=sum(vector)
            for a in allowed[sparse]:
                coef_buckets[c[sparse],b_s,a].update(exact_U_on_source_reps=vector[a],
                    exact_labeled_Y_U=multiplicity*vector[a],source_orbits_with_U=bool(vector[a]))
            groups[wi,yi]=tuple(g for g in stab if move(y,g)==y)
            sources[wi,yi]=(w,y,pool,allowed,number)
            local.update(source_orbits=1,labeled_Y=multiplicity,exact_U_on_source_reps=number,
                         exact_labeled_Y_U=multiplicity*number,source_orbits_with_U=bool(number),
                         labeled_Y_with_U=multiplicity*bool(number))
        assert dict(seen)==expected
        assert source_b==row['source_orbits_by_b'] and set(row['completed_coefficient_buckets'])==set(expected)
        for field in ('labeled_Y','source_orbits'):
            local[field+'_counted']=local[field]
        assert all(row[field]==count for field,count in local.items())
        saved_buckets={(r['c'],r['b'],r['a']):{k:v for k,v in r.items() if k not in ('c','b','a')}
                       for r in row['sparse_coefficient_buckets']}
        assert len(saved_buckets)==len(row['sparse_coefficient_buckets']) and saved_buckets==coef_buckets
        same_root=coef_buckets[c[sparse],7,4-c[sparse]]
        details.append(dict(W=w,sparse_axis=sparse,fiber_bound=sum(raw.values()),
                            co_root=dict(same_root),**local))
        totals.update(local)
        totals['fiber_bound']+=sum(raw.values())
    assert covered==domain and len(details)==4
    assert [r['fiber_bound'] for r in details]==[73216,48906,73216,48906]
    assert [r['co_root']['exact_U_on_source_reps'] for r in details]==[0,9,0,45]
    assert [r['co_root']['exact_labeled_Y_U'] for r in details]==[0,24,0,92]
    assert [totals[k] for k in ('fiber_bound','labeled_Y','source_orbits','source_orbits_with_U',
                               'exact_U_on_source_reps','exact_labeled_Y_U')]==[
                               244244,116488,23830,4372,55119,234265]
    assert data['fiber_bound']==totals['fiber_bound']
    assert data['totals']=={k:totals[k] for k in data['totals']}
    return sources,groups,dict(totals=totals,templates=details,labeled_W=len(domain),scalar_rows=65)


def base_check(sources,groups):
    data=read(PREFIX+'BASE.json'); rows=data['records']
    assert data['status']=='complete' and data['source_sha256']==digest(PREFIX+'PREFLIGHT.json')
    assert all(data[k]==0 for k in ('original_matchings_enumerated','solver_calls','rank_runs'))
    assert len(rows)==data['record_count']==47919
    seen=defaultdict(set); hits=set(); unique=set(); spectrum=Counter(); by_template=Counter()
    for t in data['U_transports']:
        guard(); i=t['representative']; assert i in range(len(rows)); row=rows[i]; key=row['receiver_index'],row['source_index']
        w,y,pool,allowed,number=sources[key]; u=tuple(t['U']); g=tuple(t['coordinate_image'])
        assert len(u)==len(set(u))==4 and u==tuple(sorted(u)) and set(u)<=set(pool)
        assert all(v in a for v,a in zip(loads(u),allowed)) and u not in seen[key]
        assert g in groups[key] and move(u,g)==tuple(row['U'])
        assert tuple(row['U'])==min(move(u,h) for h in groups[key])
        seen[key].add(u); hits.add(i)
    assert hits==set(range(len(rows)))
    for key,source in sources.items(): assert len(seen[key])==source[-1]
    for row in rows:
        guard(); key=row['receiver_index'],row['source_index']; w,y,pool,allowed,number=sources[key]
        u=tuple(row['U']); ident=key,u; by_template[key[0]]+=1
        assert ident not in unique; unique.add(ident)
        assert tuple(row['W'])==w and tuple(row['Y'])==y
        orbit={move(u,g) for g in groups[key]}
        assert len(groups[key])==row['common_stabilizer_size'] and len(orbit)==row['U_orbit_size']
        even=(0,)+tuple(64^v for v in y); odd=w+tuple(64^v for v in u)
        assert even==tuple(row['even_holes']) and odd==tuple(row['odd_holes'])
        assert len(set(even))==len(set(odd))==8
        assert all(v.bit_count()%2==p for p,group in enumerate((even,odd)) for v in group)
        assert all((v^q).bit_count()!=1 for v in even for q in odd)
        gaps=tuple(sum((v>>i)&1 for v in even)-sum((v>>i)&1 for v in odd) for i in range(7))
        assert gaps==tuple(row['signed_gaps']) and gaps[6]==3 and all(3<=abs(d)<=6 for d in gaps)
        spectrum[tuple(sorted(map(abs,gaps)))]+=1
    assert len(data['U_transports'])==sum(len(v) for v in seen.values())==55119
    assert list(by_template.values())==[11936,15028,8017,12938]
    assert len(data['summaries']) == len(by_template)
    for i, item in enumerate(data['summaries']):
        items=[s for (wi,_),s in sources.items() if wi==i]
        assert item==dict(W=list(items[0][0]),generated_U=sum(s[-1] for s in items),
                          representatives=by_template[i],sources_with_U=sum(s[-1]>0 for s in items))
    assert data['counters']['generated_U']==55119
    return rows,dict(representatives=len(rows),completions=55119,by_template=by_template,
                     spectrum={str(k):v for k,v in sorted(spectrum.items())})

def registered(plan,j,a,b,old63,new63,stats,ranks):
    from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import face
    from R7_E16_MU3_R41_M_GE3_REVIEW_CHECK import permute,project
    source_list=plan['sources']
    x=set(source_list); y={v^(1<<j) for v in x}
    r,k=plan['r'],plan['k']
    assert (r,k) in ((3,3),(3,4),(4,3),(4,4)) and list(map(len,a))==[r,r+k]
    assert len(b[0])-len(b[1])==len(x)==len(source_list)==k and x<=a[1]
    assert not y&set.union(*a,*b)
    assert sorted(y)==plan['marks'] and list(map(sorted,(b[1],b[0])))==[plan['receiver_minority'],plan['receiver_majority']]
    if plan['gate']=='universal_delta3':
        i,root,w=plan['inner'],plan['root'],plan['mirror']
        assert i in range(7) and i!=j and (r,k)==(4,3) and list(map(len,b))==[4,1]
        assert b[1]=={root} and w==root^(1<<i) and w not in set.union(*a,*b)|y
        z=(root>>i)&1
        assert [[len(face(g,i,s)) for g in (b[1],b[0])] for s in (z,1-z)]==[[1,2],[0,2]]
        assert [len(face(y,i,s)) for s in (z,1-z)]==[2,1]
        return
    spec=plan['receiver']; i=spec['inner']
    assert i in range(7) and i!=j
    axes=[v for v in range(7) if v not in (i,j)]
    assert spec['projected_axes']==axes and len(spec['faces'])==2
    used=[]
    assert plan['gate']=='controlled_cycle_registered_split'
    for side,f in enumerate(spec['faces']):
        n,m,z=({project(v,axes) for v in face(g,i,side)} for g in (b[1],b[0]|y,y))
        assert list(map(sorted,(n,m,z)))==[f['minority'],f['majority'],f['marks']]
        iface=f['interface']; kind=iface['kind']; used.append(kind); stats[kind]+=1
        assert z<=m and len(m)-len(n)==2*len(z)
        if kind=='Q5_A_ALL': assert len(z)==1 and len(n)<=14; continue
        rank=iface.get('rank')
        if kind!='Q5_A_ALL':
            assert list(map(len,(n,m,z)))==[0,6,3]
            if kind=='T63_split':
                inner=iface['local_inner']; assert inner in range(5)
                assert sum((v>>inner)&1 for v in m-z)==sum((v>>inner)&1 for v in z) in (1,2)
                continue
            if kind=='T63_old':
                p,shift=iface['rank_to_local_permutation'],iface['rank_to_local_xor']
                source,target=old63[rank],(m,z)
            else:
                assert kind=='T63_new'
                p,shift0=iface['local_to_rank_permutation'],iface['local_to_rank_xor']
                assert shift0 in range(32); shift=permute(shift0,p)
                source,target=(m,z),new63[rank]
            assert sorted(p)==list(range(5)) and shift in range(32)
            assert tuple({permute(v,p)^shift for v in g} for g in source)==target
            ranks[kind][rank]+=1
    assert used.count('Q5_A_ALL')==1



def verify_original_cut(a, b, witness, expected):
    from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import shape

    assert shape(a,b)==witness['shape']==expected
    assert list(map(sorted,a))==witness['original_A_by_alpha_beta']
    assert list(map(sorted,b))==witness['original_B_by_alpha_beta']


def check_r41(colors, witness):
    from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import directed_cut

    j,a,b=directed_cut(colors,witness,'donor_side')
    verify_original_cut(a,b,witness,[[4,7],[4,1]])
    root,=b[1]
    assert root==witness['root']
    loads_by_axis=[[i,sum(((root^v)>>i)&1 for v in b[0])] for i in range(7) if i!=j]
    usable=[i for i,c in loads_by_axis if c in (1,2)]
    assert loads_by_axis==witness['inner_loads'] and usable==witness['usable']
    assert len(usable)>=2
    return len(usable)


def check_k5(plan, j, a, b, registry, cores, kinds):
    from R7_E16_MU3_GAP7_ODD_REVIEW_CHECK import actual_returns,double_omit,projected_split

    assert plan['required_forced_edge'] is None and plan['k']==5
    retained,v,rb,y=actual_returns(plan,j,a,b,5)
    for key,group in (('donor_minority',a[0]),('donor_retained',retained),('donor_marks',v),
                      ('receiver_minority',b[1]),('receiver_retained',rb),('receiver_marks',y)):
        assert sorted(group)==plan[key]
    donor=plan['donor']
    assert donor['kind']=='T15_exact_core' and donor['index']==117
    double_omit(donor,a[0],retained|v,v,j,registry,cores)
    receiver=plan['receiver']
    assert receiver['kind']=='positive_split_Q5'
    projected_split(receiver,j,b[1],rb|y,y)
    face_kinds=[f['interface']['kind'] for f in receiver['faces']]
    assert face_kinds==['T15','avoid_one']
    kinds.update([donor['kind'],receiver['kind'],*face_kinds])


def plan_check(rows, manifest):
    from R7_E16_MU3_CENTRAL_ANTIPODAL_REVIEW_CHECK import high_m
    from R7_E16_MU3_CENTRAL_M3_REVIEW_CHECK import exact_registry,forbid_edge_assumption
    from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import directed_cut,face,one_send
    from R7_E16_MU3_GAP6_EVEN_02_REVIEW_CHECK import whole_receiver_k3
    from R7_E16_MU3_GAP7_ODD_REVIEW_CHECK import k4
    from R7_E16_MU3_R41_M_GE3_REVIEW_CHECK import ranked_targets,SIX

    data=read(PREFIX+'FIXED_PLANS.json')
    assert data['status']=='complete' and data['first_failure'] is None
    assert data['base_sha256']==digest(PREFIX+'BASE.json')
    assert len(data['positives'])==data['visited']==data['input_representatives']==len(rows)
    assert all(data[k]==0 for k in ('unvisited','new_geometries','original_matchings_enumerated','solver_calls','rank_runs'))
    old63=ranked_targets(SIX/'Q5_T63_RANK_PROOF.md',r'^\|(\d+)\|([\d,]+)\|([\d,]+)\|$')
    new63=ranked_targets(HERE/'R7_MU3_T63_NEW_RANK.md',r'^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| [\d,]+ \|')
    assert set(old63)==set(range(7)) and set(new63)==set(range(1,7))
    registry=exact_registry()
    seen=set()
    counts,local,cores,k5_cores,k4_details,rk=(Counter() for _ in range(6))
    kinds=defaultdict(Counter)
    ranks=defaultdict(Counter)
    high=defaultdict(Counter)
    k5_witnesses=[]
    for entry in data['positives']:
        guard()
        index=entry['index']
        p=entry['plan']
        gate=p['gate']
        assert index in range(len(rows)) and index not in seen
        seen.add(index)
        colors=tuple(set(rows[index][k]) for k in ('even_holes','odd_holes'))
        holes=set.union(*colors)
        forbid_edge_assumption(p)
        counts[gate]+=1
        try:
            if gate=='accepted_R41_m_ge2':
                high[gate][str(check_r41(colors,p['witness']))]+=1
                continue
            if gate=='accepted_central_m_ge3':
                high_m(colors,{'R32':p['witness']})
                high[gate][str(len(p['witness']['usable']))]+=1
                continue
            if gate=='registry_two_return':
                p=dict(p,alpha_parity=1-p['donor_majority_parity'])
            j,a,b=directed_cut(colors,p,'donor_side' if 'donor_side' in p else 'A_side')
            if gate=='accepted_central_antipodal_h6':
                verify_original_cut(a,b,p,[[3,6],[5,2]])
                u,v=sorted(b[1])
                assert (u^v).bit_count()==p['h']==6
            elif gate=='controlled_cycle_count':
                one_send(p,j,a,b,local)
                rk[f"{p['r']},{p['k']}"]+=1
            elif gate=='k3_whole_receiver':
                whole_receiver_k3(p,j,a,b,registry,cores)
                kinds[gate][p['donor']['kind']]+=1
            elif gate=='k4_two_return':
                supplier,mode,receiver=k4(p,j,a,b,registry,k4_details)
                kinds[gate][supplier]+=1
                if receiver is not None:
                    kinds[gate][receiver]+=1
                if mode=='controlled_single_root':
                    assert p['receiver']['a'] in b[1] and p['receiver']['w'] not in holes|set(p['Y'])
            elif gate=='four_mono_capacity':
                verify_original_cut(a,b,p,[[4,8],[4,0]])
                axes=[i for i in range(7) if i!=j and len(face(b[0],i,1))==2]
                assert axes==p['split_axes'] and len(axes) in (3,4,5,6)
                assert len(a[1])>{3:7,4:6,5:6,6:7}[len(axes)]
            elif gate=='registry_two_return':
                check_k5(p,j,a,b,registry,k5_cores,kinds[gate])
                k5_witnesses.append(entry)
            else:
                assert gate in ('universal_delta3','controlled_cycle_registered_split')
                registered(p,j,a,b,old63,new63,kinds[gate],ranks)
        except (AssertionError,KeyError,ValueError) as exc:
            raise AssertionError((index,gate)) from exc

    assert seen==set(range(len(rows))) and counts==data['plan_counts']==manifest['plan_counts']
    assert high==manifest['high_m_actual']
    kinds={k:v for k,v in kinds.items() if v}
    assert kinds==manifest['actual_interface_kinds_by_gate']
    assert local==manifest['count_receiver_interfaces'] and rk==manifest['controlled_rk_counts']
    assert k5_cores=={117:2}
    assert [e['index'] for e in k5_witnesses]==[3125,3161]
    assert k5_witnesses==manifest['registry_two_return_witnesses']
    ranks['T15_exact_core']=cores+k5_cores
    targets={kind:{str(k):v for k,v in sorted(hist.items())} for kind,hist in ranks.items()}
    assert targets==manifest['exact_marked_target_counts']
    return dict(plan_counts=counts,high_m=high,controlled_interfaces=local,controlled_rk=rk,
                exact_marked_targets=targets,interface_kinds=kinds,k4_details={':'.join(k):v for k,v in k4_details.items()},
                k4_exact_core117=k4_details['core117','positive_split'],k5_indices=[e['index'] for e in k5_witnesses])


def verify_imports(bound):
    from R7_E16_MU3_R41_M_GE3_REVIEW_CHECK import SIX

    receipts=(
        'R41_M2_REVIEW.json','R7_E16_MU3_CENTRAL_ANTIPODAL_REVIEW.json',
        'R7_E16_MU3_CENTRAL_M3_REVIEW.json','R7_E16_MU3_R41_M_GE3_REVIEW.json',
        'R7_MU1_CENTRAL_T1_AND_E14_REVIEW.json','R7_E16_MU3_GAP7_ODD_REVIEW.json',
        'R7_MU3_THREE_BRIDGE_FULL_REVIEW.json','R7_MU3_CONTROLLED_AND_T63_REVIEW.json',
        'R7_MU3_THREE_BRIDGE_REVIEW.json','R7_CYCLE_DONOR_THREE_BRIDGE_UNIVERSAL_REVIEW.json',
        'R7_FOUR_MONO_BALANCED_COORDINATES_REVIEW.json','R7_E16_ODD_22_COMPLETE_COVERAGE_REVIEW.json',
        'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT_REVIEW.json','R7_DELTA2_DISTANCE2_REVIEW.json',
        'R7_E16_DISTANCE2_TWO_RETURN_PLAN_REVIEW.json','R7_E16_MU2_FULL_REVIEW.json',
    )
    for name in receipts:
        assert read(name)['verdict']=='PASS',name
    receipt=read('R41_M2_REVIEW.json')
    assert receipt['soundness']=='sound-modulo-imports'
    for name in ('R7_E16_MU3_R41_M2_CLOSURE.md','R7_E16_MU3_R41_M2_CLOSURE_INPUTS.json'):
        assert receipt['audited_input_hashes'][name].removeprefix('sha256:')==digest(name)
    six_receipts=('Q5_A10_FULL_REVIEW.json','Q5_T63_RANK_REVIEW.json')
    seven_receipts=('Q5_T15_FULL_REVIEW.json','Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
    extras=tuple(SIX/name for name in six_receipts) + tuple(SIX.parent/'seven_directions'/name for name in seven_receipts)
    for path in extras:
        assert read(path)['verdict']=='PASS',path
    modules=(
        'R7_E16_MU3_R41_M_GE3_REVIEW_CHECK.py','R7_E16_MU3_CENTRAL_ANTIPODAL_REVIEW_CHECK.py',
        'R7_E16_MU3_CENTRAL_M3_REVIEW_CHECK.py','R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK.py',
        'R7_E16_MU3_GAP7_EVEN_D30_REVIEW_CHECK.py','R7_E16_MU3_GAP7_ODD_REVIEW_CHECK.py',
        'R7_E16_MU3_GAP6_EVEN_02_REVIEW_CHECK.py','R7_MU3_T63_NEW_RANK.md',
    )
    tables=(SIX/'Q5_T63_RANK_PROOF.md',SIX.parent/'seven_directions'/'Q6_T15_ACTUAL_PROFILE.json')
    table_receipts=tuple(SIX.parent/'seven_directions'/name for name in (
        'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json','Q6_T15_CORE85_MARKED_REVIEW.json',
        'Q6_T15_CORE1054_MARKED_REVIEW.json','Q6_T15_CORE85_MARKED_CLOSURE.md','Q6_T15_CORE1054_MARKED_CLOSURE.md'))
    additional={}
    for path in (*map(HERE.joinpath, modules),*tables,*table_receipts,*extras):
        name=path.as_posix()
        additional[name]=digest(path)
        if name in bound:
            assert additional[name]==bound[name].removeprefix('sha256:')
    return additional


def main():
    assert __debug__
    assert digest(PROOF)==PROOF_HASH and digest(MANIFEST)==MANIFEST_HASH
    manifest=read(MANIFEST)
    bound=manifest['sha256']
    assert len(bound)==195
    for name,expected in bound.items():
        guard()
        assert digest(name)==expected.removeprefix('sha256:'),name
    extra=verify_imports(bound)
    sources,groups,source_result=source_check()
    print('Verified four W orbits, 23,830 source orbits and all exact U coefficients',flush=True)
    rows,base_result=base_check(sources,groups)
    print('Verified 55,119 transports to 47,919 representatives',flush=True)
    plans=plan_check(rows,manifest)
    guard()
    result=dict(status='complete',proof_sha256=PROOF_HASH,manifest_sha256=MANIFEST_HASH,
                bindings=len(bound),checker_inputs_sha256=extra,sources=source_result,basis=base_result,plans=plans,
                cpu_seconds=process_time()-START,cpu_budget=45,cumulative_cpu_budget=60,
                earlier_attempt_cpu_seconds=14.375,
                earlier_exit='k4 interface histogram needed to include whole-face receiver kinds',
                producer_runs=0,plan_searches=0,matching_enumerations=0,solver_calls=0,rank_runs=0,old_certificate_replays=0)
    with (HERE/'R41_M1_REVIEW_CHECK.json').open('x',encoding='utf-8') as handle:
        json.dump(result,handle,indent=2,ensure_ascii=False)
        handle.write('\n')
    print(f"Verified {len(rows):,} fixed plans in {result['cpu_seconds']:.6f} CPU seconds",flush=True)


if __name__=='__main__':
    try:
        main()
    finally:
        print(f'Checker CPU seconds including output: {process_time()-START:.6f}',flush=True)

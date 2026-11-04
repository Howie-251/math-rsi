"""Independent bit geometry and choice-quantifier checks; zero F enumeration."""
from pathlib import Path
from itertools import combinations
import hashlib,json
R=Path(__file__).resolve().parent
V=set(range(32));E={x for x in V if x.bit_count()%2==0}
N={x:{y for y in V if (x^y).bit_count()==1} for x in V}
def sha(n):return 'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def swap(x,d):return x^(3<<d) if ((x>>d)^(x>>(d+1)))&1 else x
def orbit(z,w):
    seed=(tuple(sorted(z)),tuple(sorted(w)));seen={seed};todo=[seed]
    while todo:
        a,b=todo.pop()
        for d in range(4):
            g=(tuple(sorted(swap(x,d) for x in a)),tuple(sorted(swap(x,d) for x in b)))
            if g not in seen:seen.add(g);todo.append(g)
    return seen
source=['A8_ORBITS2_3_ANALYTIC_CLOSURE.md','A8_orbits2_3_geometry_check.py','A8_orbits2_3_geometry_check.json']
given=load(source[2]);assert given['status']=='PASS'
assert given['checker_sha256']==sha(source[1]).removeprefix('sha256:')
Hsets=[{0,3,5,6,15,25,26,28},{0,3,5,15,23,25,26,28}]
I={24,27,29,30};D8={8,9,10,12};D16={16,17,18,20};U=I|D8|D16
results=[];choice_count=0;choice_deletion_checks=0;parity_checks=0
for index,H in enumerate(Hsets):
    major=H&E;minor=H-E;Z=major-{0};covered=V-H
    assert len(major)==5 and len(minor)==3
    assert all(not(N[x]&minor) for x in Z)
    row=given['rows'][index];assert row['Z']==sorted(Z) and row['W']==sorted(minor)
    cuts=[];closed=[]
    for bit in (8,16):
        A={x for x in V if not x&bit};B=V-A
        delta=len(major&A)-len(minor&A);k=delta-2
        candidates={x^bit for x in Z&A}
        assert len(candidates)==k+1 and k in (2,3) and candidates<=covered&B
        choices=[];S=None
        for Yt in combinations(sorted(candidates),k):
            Y=set(Yt);final_holes=(H&B)|Y
            # Derive obstruction from exact imported classification, not table.
            if k==2:
                singleton=final_holes&E
                assert len(singleton)==1 and len(final_holes-E)==5
                a=next(iter(singleton));neigh=N[a]&B
                assert Y<=neigh
                obstruction=neigh-Y;assert len(obstruction)==2
            else:
                assert len(final_holes)==6 and len(final_holes&E)==0
                potential=[]
                for a in (B&E)-final_holes:
                    available=(N[a]&B)-Y
                    if len(available)==1:potential.append({a,next(iter(available))})
                assert len(potential)==1;obstruction=potential[0]
            assert obstruction<=covered and not obstruction&Y
            special=Y|obstruction
            if S is None:S=special
            else:assert S==special
            choices.append({'Y':sorted(Y),'obstruction':sorted(obstruction)})
            choice_count+=1
        special_vertex=set.intersection(*(set(c['obstruction']) for c in choices))
        assert len(special_vertex)==1 and S==candidates|special_vertex
        assert all(len(set(c['obstruction'])&candidates)==1 for c in choices)
        for fixed in [-1]+list(range(len(choices))):
            active=[set(c['Y']) for i,c in enumerate(choices) if i!=fixed]
            assert set().union(*active)==candidates
            choice_deletion_checks+=1
        # Every possible set of c crossing ports inside S with correct parity.
        for c in range(len(S)+1):
            if c%2!=(16-len(H&A))%2:continue
            for ports in combinations(sorted(S),c):
                assert (len(S)-c)%2==0
                r=next(iter(special_vertex))
                if r not in ports:assert (len(S)-c-1)%2==1
                parity_checks+=1
        C=(covered&B)-S;closed.append(C)
        g=next(q for q in row['cuts'] if q['bit']==bit)
        assert g['bridges_per_choice']==k and g['candidates']==sorted(candidates)
        assert g['special']==sorted(S) and g['closed_outside']==sorted(C)
        assert g['A_hole_counts']==[len(minor&A),len(major&A)]
        assert g['obstruction_edges']==[c['obstruction'] for c in choices]
        cuts.append({'bit':bit,'k':k,'candidate_mirrors':sorted(candidates),'S':sorted(S),'choices':choices,'closed_set':sorted(C)})
    assert closed[0]&closed[1]==I and closed[0]-closed[1]==D8 and closed[1]-closed[0]==D16
    rem=covered-U;assert len(rem)==12 and sorted(rem)==row['remaining_closed_set']
    zero=[]
    for d in range(5):
        bit=1<<d;A={x for x in V if not x&bit};B=V-A
        if len(major&A)!=2 or len(minor&A)!=2:continue
        Y={x^bit for x in minor&A};singleton=minor&B;assert len(singleton)==1
        a=next(iter(singleton));special=N[a]&B;pair=special-Y
        assert Y<=special and Y<=covered and len(pair)==2
        assert len(pair&D8)==len(pair&D16)==1 and special<=U
        zero.append({'bit':bit,'Y':sorted(Y),'singleton':a,'obstruction':sorted(pair),'S':sorted(special)})
        g=next(q for q in row['delta0'] if q['bit']==bit)
        assert g['bridge_vertices']==sorted(Y) and g['singleton']==a and g['obstruction_edge']==sorted(pair) and g['special']==sorted(special)
    assert len(zero)==len(row['delta0'])
    preserved=sum(c['bit'] for c in zero)
    assert preserved==row['preserved_bitmask']
    assert {x for x in rem if (x&preserved)==(1&preserved)}=={1}
    images=orbit(Z,minor);assert len(images)==[20,30][index]==row['orbit_size']
    results.append({'H':sorted(H),'cuts':cuts,'zero_cuts':zero,'R':sorted(rem),'preserved_mask':preserved,'orbit_size':len(images)})

# Construct all five residual orbits and check exact member sets and disjointness.
old=load('A8_geometry_census.json');all_images=[]
for r in old['residual_orbits']:
    images=orbit(r['Z'],r['W']);assert len(images)==r['size']
    assert images=={(tuple(g['Z']),tuple(g['W'])) for g in r['members']}
    assert all(not images&p for p in all_images);all_images.append(images)
assert sum(map(len,all_images))==160
assert orbit(Hsets[0]&E-{0},Hsets[0]-E)==all_images[1]
assert orbit(Hsets[1]&E-{0},Hsets[1]-E)==all_images[2]
assert len(all_images[1]|all_images[2])==50
assert not (all_images[1]|all_images[2])&(all_images[0]|all_images[3]|all_images[4])

# The terminal-excess arithmetic for every possible endpoint population up to
# seven D edges, including the d=1 multigraph boundary. No original matching.
terminal_cases=0
for d in range(1,8):
    for p in range(d+1):
        terminals=2*d-2*p
        for e in (0,1):
            if terminals>=2*e+1:
                assert terminals>2*e and d>p+e
                terminal_cases+=1
deps=['Q4_GENERAL_AUGMENTATION.md','Q4_T15_CLASSIFICATION.md','Q4_T15_CLASSIFICATION_REVIEW.json',
      'A8_Q4_T63_CLASSIFICATION.md','A8_BRIDGE_INPUTS_REVIEW.md','A8_BRIDGE_INPUTS_REVIEW.json',
      'A8_geometry_census.json','A8_PARTIAL_REVIEW.json','A8_DELTA4_FIRST_ORBIT_REVIEW.json']
for n in deps:
    if n.endswith('_REVIEW.json'):assert load(n)['verdict']=='PASS'
checks=0
for report in ['A8_BRIDGE_INPUTS_REVIEW.json','Q4_T15_CLASSIFICATION_REVIEW.json','A8_PARTIAL_REVIEW.json']:
    data=load(report)
    for key in ['audited_input_hashes','imported_dependency_hashes']:
        for n,h in data.get(key,{}).items():
            if n in deps:
                assert sha(n).removeprefix('sha256:')==h.removeprefix('sha256:')
                checks+=1
out={'status':'PASS','audited_input_hashes':{n:sha(n) for n in source},
     'imported_dependency_hashes':{n:sha(n) for n in deps},'imported_source_hash_comparisons':checks,
     'rows':results,'bridge_choices_checked':choice_count,'possible_fixed_choice_removal_checks':choice_deletion_checks,
     'covered_S_port_parity_cases':parity_checks,'terminal_excess_cases':terminal_cases,
     'new_geometry_count':50,'new_orbit_sizes':[20,30],'all_five_residual_orbits':[len(x) for x in all_images],
     'no_overlap_with_first_fourth_fifth_orbits':True,'matching_instances_enumerated':0,
     'full_A8_proved':False,'full_P6_proved':False,'producer_code_imported_or_executed':False}
(R/'A8_ORBITS2_3_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','imported_dependency_hashes']},indent=2))

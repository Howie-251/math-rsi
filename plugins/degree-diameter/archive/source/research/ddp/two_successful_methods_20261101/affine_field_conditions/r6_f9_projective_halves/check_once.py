#!/usr/bin/env python3
"""One bounded, single-worker complete PGL2(F9) half-set gate; no graph."""
import itertools, json, os, resource, time
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
if hasattr(os, 'sched_getaffinity'):
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
t0 = time.process_time()
HERE = Path(__file__).resolve().parent
STAGE = HERE.parents[1]
SOURCE = STAGE / 'd2_spare_dominating_fill/brown91_cap11_interface/pin_profiles/GEOMETRY.json'
raw = json.loads(SOURCE.read_text())
M = raw['field_multiplication']
INV = raw['field_inverses']
F = range(9)
INF = 9
PG = (INF,) + tuple(F)
S = (INF, 0, 1, 2, 3, 6)

def add(x, y):
    return (x % 3 + y % 3) % 3 + 3 * ((x // 3 + y // 3) % 3)
def neg(x): return (-x % 3) % 3 + 3 * ((- (x // 3)) % 3)
def sub(x, y): return add(x, neg(y))
def mul(x, y): return M[x][y]
def fs(xs):
    z = 0
    for x in xs: z = add(z, x)
    return z
def normalize(v):
    z = next((x for x in v if x), 0)
    assert z
    return tuple(mul(INV[z], x) for x in v)
def mv(A, x): return tuple(fs(mul(a,b) for a,b in zip(row,x)) for row in A)
def mm(A, B):
    return tuple(tuple(fs(mul(A[i][k], B[k][j]) for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))
def eye(n): return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mi(A):
    n = len(A)
    a = [list(A[i]) + list(eye(n)[i]) for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j,n) if a[i][j])
        a[j],a[p] = a[p],a[j]
        z = INV[a[j][j]]
        a[j] = [mul(z,x) for x in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [sub(x,mul(z,y)) for x,y in zip(a[i],a[j])]
    assert tuple(tuple(row[:n]) for row in a) == eye(n)
    return tuple(tuple(row[n:]) for row in a)
def det3cols(x,y,z):
    return sub(add(mul(x[0],sub(mul(y[1],z[2]),mul(y[2],z[1]))),
                   mul(x[2],sub(mul(y[0],z[1]),mul(y[1],z[0])))),
               mul(x[1],sub(mul(y[0],z[2]),mul(y[2],z[0]))))
def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))
def ell(t): return (0,0,1) if t==INF else (1,t,mul(t,t))
def H(t):
    return ((0,0,1),(1,0,0),(0,1,0)) if t==INF else ((1,0,0),(neg(t),1,0),(0,neg(t),1))
def canon_z(u,v): return INF if not u else mul(v,INV[u])
def image_z(g,z):
    a,b,c,d=g
    num,den = (a,c) if z==INF else (add(mul(a,z),b),add(mul(c,z),d))
    assert num or den
    return canon_z(den,num)
def jpoint(x): return 'inf' if x==INF else x
def jset(B): return [jpoint(z) for z in PG if z in B]
def dump(name,obj): (HERE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

# Verify that the inherited table realizes exactly the requested field presentation.
assert len(M)==9 and all(len(r)==9 for r in M) and len(INV)==9
for x,y in itertools.product(F,repeat=2):
    a,b=x%3,x//3; c,d=y%3,y//3
    polynomial_product = (a*c-b*d)%3 + 3*((a*d+b*c)%3)
    assert mul(x,y)==polynomial_product
    assert add(x,y)==add(y,x) and mul(x,y)==mul(y,x)
    assert add(x,neg(x))==0
    for z in F:
        assert mul(mul(x,y),z)==mul(x,mul(y,z))
        assert mul(x,add(y,z))==add(mul(x,y),mul(x,z))
for x in range(1,9): assert mul(x,INV[x])==1
assert mul(3,3)==2 and neg(3)==6
field_cpu = time.process_time()-t0

# Enumerate all normalized projective linear matrices, and only linear matrices.
group=[]
for g in itertools.product(F,repeat=4):
    if not any(g) or next(x for x in g if x)!=1: continue
    a,b,c,d=g
    if sub(mul(a,d),mul(b,c))==0: continue
    perm=tuple(image_z(g,z) for z in PG)
    assert set(perm)==set(PG)
    group.append((g,perm))
assert len(group)==720 and len({p for _,p in group})==720
assert [g for g,_ in group]==sorted(g for g,_ in group)
perm_by_g=dict(group)
def act(g,B): return frozenset(image_z(g,z) for z in B)
subsets=[frozenset(c) for c in itertools.combinations(PG,5)]
assert len(subsets)==252
unseen=set(subsets)
orbits=[]
for rep in subsets:
    if rep not in unseen: continue
    witnesses={}
    for g,_ in group: witnesses.setdefault(act(g,rep),g)
    members=set(witnesses)
    assert members <= unseen
    unseen -= members
    orbits.append((rep,witnesses))
assert not unseen
orbit_id={B:i for i,(_,ws) in enumerate(orbits) for B in ws}
all_points=frozenset(PG)
records=[]
for B in subsets:
    C=all_points-B
    maps=[g for g,_ in group if act(g,B)==C]
    oi=orbit_id[B]
    records.append({'subset':jset(B),'orbit_id':oi,
                    'representative_to_subset':list(orbits[oi][1][B]),
                    'complement_orbit_id':orbit_id[C],
                    'complement_maps_count':len(maps),
                    'lex_first_to_complement':list(maps[0]) if maps else None})
summary=[]
for i,(rep,ws) in enumerate(orbits):
    C=all_points-rep
    maps=[g for g,_ in group if act(g,rep)==C]
    summary.append({'orbit_id':i,'representative':jset(rep),'size':len(ws),
                    'stabilizer_order':720//len(ws),
                    'complement_orbit_ids':sorted({orbit_id[all_points-B] for B in ws}),
                    'lex_first_representative_to_complement':list(maps[0]) if maps else None,
                    'representative_complement':jset(C)})
orbit_cpu=time.process_time()-t0-field_cpu
dump('ORBIT_WITNESSES.json',{'field':'F3[w]/(w^2+1), code a+3b',
     'PG_point_order':[jpoint(z) for z in PG],
     'coefficient_convention':'(a,b,c,d), (az+b)/(cz+d); normalized first nonzero=1, lex code order',
     'group_order':720,'group_coefficients':[list(g) for g,_ in group],
     'subset_count':252,'orbits':summary,'subsets':records})

# Fixed S only: stop immediately if its required local complement map is absent.
record_by_B={B:r for B,r in zip(subsets,records)}
charts=[]
chart_checks=[]
triples=[]
for ids in itertools.combinations(range(6),3):
    det=det3cols(*(ell(S[i]) for i in ids))
    assert det
    triples.append({'port_indices':ids,'determinant':det})
for p,t in enumerate(S):
    B=frozenset(S)-{t}
    g=record_by_B[B]['lex_first_to_complement']
    if g is None:
        dump('COUNTEREXAMPLE.json',{'port_index':p,'port_parameter':jpoint(t),'B':jset(B),
             'complement':jset(all_points-B),'reason':'No PGL2(F9) map to complement among all720'})
        raise SystemExit('Fixed S fails; chart gate stopped without variant')
    a,b,c,d=g
    Q=((d,c),(b,a))
    D=((1,0,0),(0,d,c),(0,b,a))
    Hp=H(t); Hip=mi(Hp)
    Tp=mm(mm(Hip,D),Hp); Tm=mi(Tp)
    assert mm(Tp,Tm)==eye(3) and mm(Tm,Tp)==eye(3)
    assert mv(Tp,ell(t))==ell(t) and mv(Tm,ell(t))==ell(t)
    # Check all q possible noise values; this is the exact inverse edge relation.
    for noise in F:
        assert mv(Tm,tuple(mul(noise,x) for x in ell(t))) == tuple(mul(noise,x) for x in ell(t))
    charts.append({'port_index':p,'port_parameter':jpoint(t),'B':jset(B),
          'complement':jset(all_points-B),'halfset_orbit_id':record_by_B[B]['orbit_id'],
          'f_plus_coefficients':g,'f_plus_images_in_B_order':[jpoint(image_z(g,z)) for z in PG if z in B],
          'Q_plus':Q,'H':Hp,'H_inverse':Hip,'T_plus':Tp,'T_minus_exact_inverse':Tm,
          'T_plus_squared':mm(Tp,Tp),'T_plus_squared_is_identity':mm(Tp,Tp)==eye(3)})
    for sign,T in [('+',Tp),('-',Tm)]:
        dets=[]
        for i in range(6):
            if i==p: continue
            for j in range(6):
                if j==p: continue
                v=det3cols(mv(T,ell(S[i])),ell(t),ell(S[j]))
                assert v
                dets.append({'source_other_port':i,'target_other_port':j,'determinant':v})
        pre=[mv(T,ell(S[i])) for i in range(6) if i!=p]
        post=[ell(S[j]) for j in range(6) if j!=p]
        pre_rays=[canon_z(*mv(Hp,v)[1:]) for v in pre]
        post_rays=[canon_z(*mv(Hp,v)[1:]) for v in post]
        assert set(pre_rays).isdisjoint(post_rays)
        assert set(pre_rays+post_rays)==set(PG)
        normals=[normalize(cross(ell(t),v)) for v in pre+post]
        assert len(set(normals))==10
        covered=sum(any(fs(mul(n[k],x[k]) for k in range(3))==0 for n in normals)
                    for x in itertools.product(F,repeat=3))
        assert covered==729
        chart_checks.append({'port_index':p,'sign':sign,'turn_count':len(dets),'rank3_count':len(dets),
                  'turn_determinants':dets,'pre_plane_rays':[jpoint(z) for z in pre_rays],
                  'post_plane_rays':[jpoint(z) for z in post_rays],
                  'distinct_plane_count':len(set(normals)),'normalized_plane_normals':normals,
                  'pencil_union_cardinality':covered,'own_port_vector_preserved_exactly':True})
chart_cpu=time.process_time()-t0-field_cpu-orbit_cpu
cpu=time.process_time()-t0
assert cpu<20
params={'field':{'characteristic':3,'order':9,'presentation':'F3[w]/(w^2+1)',
                 'encoding':'a+3b represents a+bw, a,b in0..2',
                 'multiplication':M,'inverses':INV},
        'port_parameters':['inf',0,1,2,3,6],'port_vectors':[ell(t) for t in S],
        'forward_edge_relation':'y=T_plus[p] x + noise ell_p; reverse uses T_minus_exact_inverse[p]',
        'orientation_convention':'For each edge of each self-inverse matching port, choose one direction; positive usesT_plus, negative usesT_minus_exact_inverse.',
        'charts':charts}
dump('PARAMETERS.json',params)
dump('CHART_CHECKS.json',{'chart_count':12,'central_turns':300,'rank3_turns':300,
                        'conic_triples':triples,'checks':chart_checks})
result={'status':'PASS_COMPLETE_PGL2_F9_HALFSET_CLASSIFICATION_AND_FIXED_S_LOCAL_GATE',
        'prediction_orbit_sizes':[72,180],'actual_orbit_sizes':[x['size'] for x in summary],
        'orbits':summary,'all252_halves_projectively_self_complementary':all(r['lex_first_to_complement'] is not None for r in records),
        'fixed_S':['inf',0,1,2,3,6],'fixed_S_all_six_halves_pass':True,
        'group_permutations':720,'subsets':252,'actual_charts':12,'central_turns':300,'rank3_turns':300,
        'per_chart_plane_rays':10,'per_chart_pencil_coverage':729,
        'own_port_vector_and_true_inverse_checks':True,
        'positive_square_identity_by_port':[r['T_plus_squared_is_identity'] for r in charts],
        'CPU_seconds':cpu,'CPU_phases_seconds':{'field_check':field_cpu,'orbit_classification':orbit_cpu,'charts':chart_cpu},
        'CPU_limit_seconds':20,'workers':1,'pid':os.getpid(),
        'controller_generated':False,'fiber_graph_generated':False,'BFS_calls':0,'solver_calls':0,'Lean_calls':0,
        'semilinear_Frobenius_maps_used':False,'alternative_S_used':False,
        'complete_graph_or_record_claim':False,
        'source_field_table':str(SOURCE.relative_to(STAGE)),
        'inherited_derivation':'../general_ports/DERIVATION_PACKAGE.md'}
dump('RESULT.json',result)
dump('TERMINAL.json',{'status':'COMPLETE_PASS_LOCAL_GATE_ONLY','pid':os.getpid(),'CPU_seconds':cpu,
                      'live_handle':None,'jobs_running':False,'scope':'onePGL2F9 classification; onefixedS; twelveactualcharts; nofullgraph'})
print(json.dumps(result,ensure_ascii=False,indent=2))

#!/usr/bin/env python3
"""Fixed-S cross-port extension only; reuse completed group and self-chart data."""
import itertools, json, os, resource, time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
if hasattr(os,'sched_getaffinity'):
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
t0=time.process_time()
HERE=Path(__file__).resolve().parent
OLD=HERE.parent
oldparams=json.loads((OLD/'PARAMETERS.json').read_text())
oldresult=json.loads((OLD/'RESULT.json').read_text())
oldchecks=json.loads((OLD/'CHART_CHECKS.json').read_text())
orbitdata=json.loads((OLD/'ORBIT_WITNESSES.json').read_text())
assert oldresult['status']=='PASS_COMPLETE_PGL2_F9_HALFSET_CLASSIFICATION_AND_FIXED_S_LOCAL_GATE'
assert oldresult['rank3_turns']==300 and oldchecks['chart_count']==12
# These saved720 coefficients are reused; group and252-subset classification are not rerun.
group=[tuple(g) for g in orbitdata['group_coefficients']]
assert len(group)==720
M=oldparams['field']['multiplication']; INV=oldparams['field']['inverses']
S=tuple(9 if t=='inf' else t for t in oldparams['port_parameters'])
assert S==(9,0,1,2,3,6)
PG=(9,)+tuple(range(9)); ALL=frozenset(PG)
ells=[tuple(v) for v in oldparams['port_vectors']]
Hs=[tuple(tuple(row) for row in c['H']) for c in oldparams['charts']]
His=[tuple(tuple(row) for row in c['H_inverse']) for c in oldparams['charts']]

def add(x,y): return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x): return (-x)%3+3*((-(x//3))%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y): return M[x][y]
def fs(xs):
    out=0
    for x in xs: out=add(out,x)
    return out
def mv(A,x): return tuple(fs(mul(a,b) for a,b in zip(row,x)) for row in A)
def mm(A,B): return tuple(tuple(fs(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def eye(n): return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mi(A):
    n=len(A); a=[list(A[i])+list(eye(n)[i]) for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j]); a[j],a[p]=a[p],a[j]
        z=INV[a[j][j]]; a[j]=[mul(z,x) for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j]; a[i]=[sub(x,mul(z,y)) for x,y in zip(a[i],a[j])]
    return tuple(tuple(row[n:]) for row in a)
def norm(v):
    c=INV[next(x for x in v if x)]
    return tuple(mul(c,x) for x in v)
def cross(x,y): return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def det(x,y,z): return fs(mul(x[k],cross(y,z)[k]) for k in range(3))
def cz(u,v): return 9 if not u else mul(v,INV[u])
def f(g,z):
    a,b,c,d=g
    nu,de=(a,c) if z==9 else (add(mul(a,z),b),add(mul(c,z),d))
    return cz(de,nu)
def jp(t): return 'inf' if t==9 else t
def js(B): return [jp(t) for t in PG if t in B]
def dump(n,x): (HERE/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
Bs=[frozenset(S)-{t} for t in S]
charts=[]
# Merely copy the old12 actual matrices; no old rank, field or pencil check is run.
for p,rec in enumerate(oldparams['charts']):
    for sign,key in [('+','T_plus'),('-','T_minus_exact_inverse')]:
        charts.append({'chart_id':f'self_{p}_{"plus" if sign=="+" else "minus"}',
          'source_port':p,'target_port':p,'matrix':rec[key],
          'inverse_chart_id':f'self_{p}_{"minus" if sign=="+" else "plus"}',
          'validation':'inherited_from_../CHART_CHECKS.json','inherited_turn_count':25})
pairs=[]; checks=[]; dart_lookup={}; newmat={}
for p,q in itertools.combinations(range(6),2):
    target=ALL-Bs[q]
    g=next((g for g in group if frozenset(f(g,z) for z in Bs[p])==target),None)
    if g is None:
        dump('COUNTEREXAMPLE.json',{'source_port':p,'target_port':q,'B_source':js(Bs[p]),'complement_B_target':js(target)})
        raise SystemExit('Fixed-S cross-port map missing; stopped')
    a,b,c,d=g
    D=((1,0,0),(0,d,c),(0,b,a))
    T=mm(mm(His[q],D),Hs[p]); Ti=mi(T)
    assert mm(T,Ti)==eye(3) and mm(Ti,T)==eye(3)
    assert mv(T,ells[p])==ells[q] and mv(Ti,ells[q])==ells[p]
    ids=(f'cross_{p}_{q}_forward',f'cross_{p}_{q}_reverse')
    pairs.append({'source_port':p,'target_port':q,'f_coefficients':g,'B_source':js(Bs[p]),
                  'complement_B_target':js(target),'f_images_in_source_B_order':[jp(f(g,z)) for z in PG if z in Bs[p]],
                  'Q':((d,c),(b,a)),'T_forward':T,'T_reverse_literal_inverse':Ti,
                  'forward_chart_id':ids[0],'reverse_chart_id':ids[1]})
    for s,t,A,cid,icid in [(p,q,T,ids[0],ids[1]),(q,p,Ti,ids[1],ids[0])]:
        # Exact noise-direction transport required by the reverse line relation.
        for k in range(9):
            assert mv(A,tuple(mul(k,x) for x in ells[s]))==tuple(mul(k,x) for x in ells[t])
        ds=[]
        for i in range(6):
            if i==s: continue
            for j in range(6):
                if j==t: continue
                v=det(mv(A,ells[i]),ells[t],ells[j]); assert v
                ds.append({'source_other_port':i,'target_other_port':j,'determinant':v})
        pre=[mv(A,ells[i]) for i in range(6) if i!=s]
        post=[ells[j] for j in range(6) if j!=t]
        prerays=[cz(*mv(Hs[t],v)[1:]) for v in pre]
        postrays=[cz(*mv(Hs[t],v)[1:]) for v in post]
        assert set(prerays).isdisjoint(postrays) and set(prerays+postrays)==set(PG)
        normals=[norm(cross(ells[t],v)) for v in pre+post]
        assert len(set(normals))==10
        covered=sum(any(fs(mul(n[k],x[k]) for k in range(3))==0 for n in normals) for x in itertools.product(range(9),repeat=3))
        assert covered==729
        checks.append({'chart_id':cid,'source_port':s,'target_port':t,'turn_count':25,'rank3_count':25,
             'turn_determinants':ds,'pre_plane_rays':[jp(z) for z in prerays],
             'post_plane_rays':[jp(z) for z in postrays],'normalized_plane_normals':normals,
             'distinct_plane_count':10,'pencil_coverage':covered,'source_to_target_vector_exact':True,
             'all9_noise_values_direction_transport':True})
        charts.append({'chart_id':cid,'source_port':s,'target_port':t,'matrix':A,'inverse_chart_id':icid,
                       'validation':'CHART_CHECKS.json','new_turn_count':25})
        dart_lookup[f'{s},{t}']=cid; newmat[f'{s},{t}']=A
assert len(pairs)==15 and len(checks)==30 and len(charts)==42
assert sum(c['rank3_count'] for c in checks)==750
params={'field':oldparams['field'],'port_parameters':oldparams['port_parameters'],'port_vectors':oldparams['port_vectors'],
        'fixed_S_only':True,'H':Hs,'H_inverse':His,'canonical_cross_pairs':pairs,'charts':charts,
        'cross_port_matrix_by_source_target':newmat,'cross_port_chart_by_source_target':dart_lookup,
        'self_port_plus':[r['T_plus'] for r in oldparams['charts']],
        'self_port_minus':[r['T_minus_exact_inverse'] for r in oldparams['charts']],
        'dart_rule':{'p<q':'cross_(p,q)_forward','p>q':'cross_(q,p)_reverse',
                     'p=q and u<v':'self_p_plus','p=q and u>v':'self_p_minus'},
        'edge_relation':'For dart u->v, with local sourceport p and targetport q: y=T_dart*x+noise*ell_q, noise inF9.',
        'controller_port_assumption':'At each simple6-regular controller vertex, ports0..5 bijectively label its six incident edges. Independent sorted-neighbor labels are allowed; no6-edge-coloring is required.',
        'inherited_self_chart_source':'../PARAMETERS.json','inherited_self_validation':'../CHART_CHECKS.json'}
dump('PARAMETERS.json',params)
dump('CHART_CHECKS.json',{'new_cross_chart_count':30,'new_turn_count':750,'new_rank3_count':750,
      'inherited_self_chart_count':12,'inherited_self_turn_count':300,
      'combined_chart_count':42,'combined_turn_count':1050,'checks':checks})
cpu=time.process_time()-t0
assert cpu<5
result={'status':'PASS_FIXED_S_COMPLETE_CROSS_PORT_LOCAL_GLUE','new_unordered_cross_pairs':15,
 'new_cross_charts':30,'new_actual_turn_checks':750,'new_rank3_turns':750,'inherited_self_charts':12,
 'inherited_self_turn_checks':300,'combined_actual_charts':42,'combined_rank3_turns':1050,
 'per_new_chart_plane_rays':10,'per_new_chart_pencil_coverage':729,
 'literal_inverse_and_source_target_port_vectors':'PASS','all9_noise_values_per_new_chart':'PASS',
 'saved_PGL_coefficients_reused':720,'PGL_group_regenerated':False,'halfset_classification_rerun':False,
 'old12_charts_rechecked':False,'fixed_S_only':True,'global6_edge_coloring_required':False,
 'CPU_seconds':cpu,'CPU_limit_seconds':5,'workers':1,'pid':os.getpid(),
 'controller_generated':False,'fiber_graph_generated':False,'BFS_calls':0,'solver_calls':0,'Lean_calls':0,
 'hashes_generated':False,'installation_performed':False,'new_graph_claim':False,
 'source_artifacts':['../PARAMETERS.json','../RESULT.json','../CHART_CHECKS.json','../ORBIT_WITNESSES.json']}
dump('RESULT.json',result)
dump('TERMINAL.json',{'status':'COMPLETE_PASS_LOCAL_GLUE_ONLY','pid':os.getpid(),'CPU_seconds':cpu,
 'jobs_running':False,'live_handle':None,'new_graph_claim':False,'next_action_here':'none'})
print(json.dumps(result,indent=2,ensure_ascii=False))

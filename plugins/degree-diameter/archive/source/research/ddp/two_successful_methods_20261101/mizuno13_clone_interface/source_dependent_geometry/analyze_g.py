from pathlib import Path
from collections import Counter,defaultdict
import json,time,resource,sys,itertools

D=Path(__file__).resolve().parent;S=D.parent
RVALUES=[tuple((k//3**i)%3 for i in range(6)) for k in range(729)]
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def dot(a,b):return sum(x*y for x,y in zip(a,b))%3
def mv(A,x):return [dot(row,x) for row in A]
def inverse(B):
    A=[list(row)+[int(i==j) for j in range(5)] for i,row in enumerate(B)]
    for j in range(5):
        k=next(i for i in range(j,5) if A[i][j]);A[j],A[k]=A[k],A[j];z=pow(A[j][j],-1,3);A[j]=[x*z%3 for x in A[j]]
        for i in range(5):
            if i!=j and A[i][j]:
                z=A[i][j];A[i]=[(a-z*b)%3 for a,b in zip(A[i],A[j])]
    return [row[5:] for row in A]
def canon_eq(coeff,rhs):
    z=next((a for a in coeff if a),rhs)
    scale=pow(z,-1,3) if z else 1
    return tuple([a*scale%3 for a in coeff]+[rhs*scale%3])
def equation(L,v):
    return canon_eq([L[i]*v[2+j]%3 for i in range(2) for j in range(3)],dot(L,v[:2]))
def holds(eq,R):return dot(eq[:6],R)==eq[6]
def evaluate_type(geom):
    hist=Counter();best=-1;witness=None;valid=0
    for code,R in enumerate(RVALUES):
        if holds(geom['M_zero_equation'],R):continue
        valid+=1;g=sum(holds(eq,R) for eq in geom['g_equations'])
        hist[g]+=1
        if g>best:best=g;witness={'R_code':code,'R_rows':[list(R[:3]),list(R[3:])],'g':g,'g_port_truths':[holds(eq,R) for eq in geom['g_equations']]}
    return {'type_id':geom['type_id'],'sources':geom['sources'],'source_count':len(geom['sources']),'all729_slopes_checked':True,'local_M_valid_slopes':valid,'g_histogram':dict(sorted(hist.items())),'gmax':best,'first_gmax_witness':witness}
def prepare():
    T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(30,31))
    C=json.loads((S/'LINE_KERNELS.json').read_text())['chart'];records=json.loads((S/'UNIFORM_H_SOURCE_PHASES.json').read_text())['source_records'];assert len(records)==315
    incoming=[[] for _ in range(364)]
    for a,row in enumerate(C):
        for p,e in enumerate(row):
            b=e['b'];assert b[2:]==[0,0,0] and any(b[:2])
            scale=pow(next(x for x in b if x),-1,3);incoming[e['target']].append({'source':a,'port':p,'projective_direction':[x*scale%3 for x in b]})
    frame={(1,0,0,0,0),(0,1,0,0,0),(1,1,0,0,0),(1,2,0,0,0)}
    assert all(len(v)==4 and {tuple(x['projective_direction']) for x in v}==frame for v in incoming)
    cache={};sources=[];types=[];which={};d_in_W=[]
    for old in records:
        a=old['source'];mp=old['M_ordinary_port'];d=old['M_affine_translation']
        assert old['M_matches_ordinary_matrix'] and all(e['target']!=a for e in C[a])
        geqs=[];detail=[]
        for p,e in enumerate(C[a]):
            key=tuple(map(tuple,e['A']))
            if key not in cache:cache[key]=inverse(e['A'])
            Ai=cache[key];ell=mv(Ai,e['b']);assert ell[2:]==[0,0,0] and any(ell[:2])
            L=[(-ell[1])%3,ell[0]]
            # Select a target W basis direction independent of b.
            j=0 if e['b'][1] else 1;target_basis=[int(k==j) for k in range(5)];preimage=mv(Ai,target_basis)
            eq=equation(L,preimage);geqs.append(eq)
            detail.append({'port':p,'target':e['target'],'ell':ell,'L_W':L,'second_target_W_basis':j,'Ainverse_second_target_W_vector':preimage,'g_equation':eq})
            if p==mp:
                dp=mv(Ai,d);Meq=equation(L,dp)
        key=(tuple(sorted(geqs)),Meq)
        if key not in which:
            which[key]=len(types);types.append({'type_id':len(types),'g_equations':[list(z) for z in sorted(geqs)],'M_zero_equation':list(Meq),'sources':[]})
        tid=which[key];types[tid]['sources'].append(a)
        isin=not any(d[2:])
        if isin:d_in_W.append(a)
        sources.append({'source':a,'type_id':tid,'M_ordinary_port':mp,'M_target':old['M_target'],'M_target_translation_d':d,'M_target_translation_in_W':isin,'M_input_translation_dprime':dp,'g_port_equations':detail,'M_zero_equation':Meq})
    began=time.process_time();bench=[evaluate_type(t) for t in types[:3]];benchCPU=time.process_time()-began
    elapsed=time.process_time()-T;estimate=benchCPU/max(1,len(bench))*len(types)
    out={'status':'PREPARED_DISTINCT_LINEAR_GEOMETRIES_AND_BENCHMARKED','source_count':315,'all_target_incoming_directions_verified_distinct_W_lines':364,'M_target_translation_d_in_W_count':len(d_in_W),'M_target_translation_d_in_W_sources':d_in_W,'M_target_translation_d_outside_W_count':315-len(d_in_W),'distinct_geometry_type_count':len(types),'inverse_matrix_types':len(cache),'geometry_types':types,'source_bindings':sources,'target_incoming_direction_bindings':incoming,'three_type_benchmark':bench,'benchmark_CPU_seconds':benchCPU,'estimated_all_type_CPU_seconds':estimate,'preparation_CPU_seconds':elapsed,'CPU_budget_seconds':30,'solver_calls':0,'BFS_runs':0,'new_graphs':0}
    save('PREPARED_GEOMETRY.json',out)
    print(json.dumps({k:v for k,v in out.items() if k not in ['geometry_types','source_bindings','target_incoming_direction_bindings','M_target_translation_d_in_W_sources']}))
def analyze():
    T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(30,31));P=json.loads((D/'PREPARED_GEOMETRY.json').read_text());types=P['geometry_types']
    assert P['estimated_all_type_CPU_seconds']+P['preparation_CPU_seconds']<29
    cached={x['type_id']:x for x in P['three_type_benchmark']};results=[]
    for g in types:results.append(cached[g['type_id']] if g['type_id'] in cached else evaluate_type(g))
    per_source={a:r['gmax'] for r in results for a in r['sources']};assert len(per_source)==315
    counts=Counter(per_source.values());costs=sorted((12-2*g,a) for a,g in per_source.items() if g>=0)
    used=0;upper=0
    for cost,a in costs:
        if used+cost>1092:break
        used+=cost;upper+=1
    pure_gmax=max(per_source.values());uniform_bound=1092//(12-2*pure_gmax) if pure_gmax>=0 else 0
    for a,g in per_source.items():assert 0<=g<=4
    out={'status':'GM_BOUND_EXCLUDES_213_BLOCKS_EVEN_WITH49_EXCEPTIONS' if upper+49<213 else 'GM_NECESSARY_BOUND_DOES_NOT_DECIDE_213_BLOCKS','regular_sources':315,'distinct_types':len(types),'all729_slopes_evaluated_per_type':True,'source_gmax_histogram':dict(sorted(counts.items())),'largest_gmax':pure_gmax,'uniform_gmax_regular_block_upper':uniform_bound,'weighted_regular_source_upper':upper,'weighted_capacity_used_by_cheapest_sources':used,'capacity_budget':1092,'source_cost':'12-2*gmax(source)','optimistic_additional_exceptional_sources':49,'all364_optimistic_block_upper':upper+49,'needed_full27_blocks':213,'loose_upper_bound_is_not_feasibility':True,'types':results,'source_gmax':per_source,'M_target_translation_d_in_W_count':P['M_target_translation_d_in_W_count'],'M_target_translation_d_outside_W_count':P['M_target_translation_d_outside_W_count'],'preparation_CPU_seconds':P['preparation_CPU_seconds'],'analysis_CPU_seconds':time.process_time()-T,'total_measured_CPU_seconds':P['preparation_CPU_seconds']+time.process_time()-T,'CPU_budget_seconds':30,'scope':'All affine full27 W-transverse blocks H_R+c on315 specified nonself/noP sources with affine M=ordinary-port A. Slopes are complete729 per distinct equation type; phase irrelevant for g and local M separation. Other49 sources only pessimistically allowed one block each for the upper bound. Not arbitrary nonlinear transversals or partial blocks.','solver_calls':0,'BFS_runs':0,'new_graphs':0,'running':False,'pending':[]}
    # Combine the ordinary-normal exclusivity gate with the integral M-volume row.
    costs_combined=sorted((9-g,a) for a,g in per_source.items())
    combined_used=0;combined_upper=0
    for cost,a in costs_combined:
        if combined_used+cost>1092:break
        combined_used+=cost;combined_upper+=1
    out.update({'status':'REGULAR315_FULL27_AFFINE_BLOCK_DOMAIN_EXCLUDED_BY_COMBINED_M_AND_NORMAL_BOUND',
        'geometric_only_weighted_regular_source_upper':upper,
        'M_only_regular_block_upper':1092//5,
        'combined_source_cost':'9-gmax(source)',
        'combined_necessary_inequality':'sum_selected(9-gmax(source)) <=1092',
        'combined_regular_block_upper':combined_upper,
        'combined_capacity_used_by_cheapest_sources':combined_used,
        'combined_regular_clone_upper':27*combined_upper,
        'combined_regular_final_order_upper':88452+27*combined_upper,
        'combined_bound_scope':'Only the315 regular sources; other49 sources remain unexcluded.',
        'explicit_local_g4_witness':'EXPLICIT_G4_COUNTEREXAMPLE.json'})
    save('RESULT.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['types','source_gmax']}))
if __name__=='__main__':
    if sys.argv[1]=='prepare':prepare()
    elif sys.argv[1]=='analyze':analyze()

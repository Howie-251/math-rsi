"""One composed four-step route experiment; no graph/BFS/old rank verifier."""
import collections,itertools,json,os,resource,time
from pathlib import Path
start=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(10,10))
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'research/ddp/more_graphs_20261027').is_dir())
def save(name,value):(D/name).write_text(json.dumps(value,indent=2)+'\n')
save('NEW_ROUTE4_HANDLE.json',dict(pid=os.getpid(),running=True,CPU_budget_seconds=10))
path=R/'research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json'
p=json.loads(path.read_text());types=[];transition=[[None]*5 for _ in range(192)]
for a in p['arcs']:
    typ=(tuple(tuple(row)for row in a['B']),tuple(a['v']),tuple(a['c']))
    if typ not in types:types.append(typ)
    t=types.index(typ);assert t<5 and transition[a['from']][t]is None
    transition[a['from']][t]=a['to']
assert len(types)==5 and all(None not in row for row in transition)
def mv(A,x):return tuple(sum(A[i][j]*x[j]for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j]for k in range(4))%3 for j in range(4))for i in range(4))
def rank(columns):
    A=[[c[i]for c in columns]for i in range(4)];r=0
    for j in range(len(columns)):
        pivot=next((i for i in range(r,4)if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r];q=A[r][j]
        A[r]=[(x*q)%3 for x in A[r]]
        for i in range(4):
            if i!=r:
                q=A[i][j];A[i]=[(x-q*y)%3 for x,y in zip(A[i],A[r])]
        r+=1
        if r==4:break
    return r
def inverse(columns):
    A=[[columns[j][i]for j in range(4)]+[int(i==j)for j in range(4)]for i in range(4)]
    for j in range(4):
        pivot=next(i for i in range(j,4)if A[i][j]);A[j],A[pivot]=A[pivot],A[j]
        q=A[j][j];A[j]=[(q*x)%3 for x in A[j]]
        for i in range(4):
            if i!=j:
                q=A[i][j];A[i]=[(x-q*y)%3 for x,y in zip(A[i],A[j])]
    return[row[4:]for row in A]
identity=tuple(tuple(int(i==j)for j in range(4))for i in range(4));zero=(0,0,0,0)
words=[dict(word=(),M=identity,c=zero,N=())];layers=[[words[0]]]
for length in range(1,5):
    current=[]
    for prev in layers[-1]:
        for t,(B,v,c)in enumerate(types):
            mc=mv(B,prev['c']);entry=dict(word=prev['word']+(t,),M=mm(B,prev['M']),
               c=tuple((mc[i]+c[i])%3 for i in range(4)),N=tuple(mv(B,col)for col in prev['N'])+(v,))
            current.append(entry)
    layers.append(current);words+=current
four=layers[4]
for w in four:
    w['rank']=rank(w['N'])
    if w['rank']==4:w['inverse_noise']=inverse(w['N'])
rank_hist=dict(sorted(collections.Counter(w['rank']for w in four).items()))
covered=[[None]*192 for _ in range(192)];all_endpoints=[[set()for _ in range(192)]for _ in range(192)]
def endpoint(a,word):
    for t in word:a=transition[a][t]
    return a
for a in range(192):
    for wi,w in enumerate(four):
        b=endpoint(a,w['word'])
        if w['rank']==4 and covered[a][b]is None:covered[a][b]=wi
missing=[(a,b)for a in range(192)for b in range(192)if covered[a][b]is None]
strata=collections.Counter('equal'if a==b else'adjacent'if b in transition[a]else'other'for a,b in missing)
save('NEW_ROUTE4_TYPES_AND_TRANSITIONS.json',dict(source=str(path.relative_to(R)),type_order='first appearance in actual960 arcs',
    types=[dict(type=t,B=B,v=v,c=c)for t,(B,v,c)in enumerate(types)],transition=transition,actual_arcs_bound=960))
save('NEW_ROUTE4_WORDS625.json',four)
save('NEW_ROUTE4_MISSING_PAIRS.json',dict(count=len(missing),strata=dict(strata),ordered_pairs=missing))
selected=None
if missing:
    a,b=missing[0];routes=[w for w in words if endpoint(a,w['word'])==b]
    def code(x):return sum(x[i]*3**i for i in range(4))
    groups={};coverage=[set(),set()];starts=[zero,(1,0,0,0)]
    route_details=[]
    for w in routes:
        images={}
        for noise in itertools.product(range(3),repeat=len(w['word'])):
            y=tuple(sum(col[i]*t for col,t in zip(w['N'],noise))%3 for i in range(4))
            images.setdefault(code(y),dict(word=w['word'],noise=noise))
        key=(w['M'],w['c']);group=groups.setdefault(key,dict(words=[],noise_witnesses={}))
        group['words'].append(w['word']);group['noise_witnesses'].update(images)
        for si,x in enumerate(starts):
            z=mv(w['M'],x);shift=tuple((z[i]+w['c'][i])%3 for i in range(4))
            for yc in images:
                y=tuple(yc//3**i%3 for i in range(4));coverage[si].add(code(tuple((y[i]+shift[i])%3 for i in range(4))))
        route_details.append(dict(word=w['word'],M=w['M'],c=w['c'],noise_columns=w['N'],noise_image_size=len(images)))
    group_details=[dict(M=M,c=c,word_count=len(g['words']),words=g['words'],noise_union_size=len(g['noise_witnesses']),
         noise_union_codes=sorted(g['noise_witnesses']),noise_witnesses=g['noise_witnesses'])for(M,c),g in groups.items()]
    group_details.sort(key=lambda g:-g['noise_union_size'])
    full_group=next((g for g in group_details if g['noise_union_size']==81),None)
    selected=dict(pair=[a,b],selection='lexicographically first missing controllerpair only',
        words_length0_through4_tested_total=781,words_reaching_selected_pair=len(routes),
        route_lengths=dict(sorted(collections.Counter(len(w['word'])for w in routes).items())),
        route_noise_image_sizes=dict(sorted(collections.Counter(r['noise_image_size']for r in route_details).items())),
        tested_starts=[dict(x=x,covered=len(coverage[i]),missing_codes=sorted(set(range(81))-coverage[i]))for i,x in enumerate(starts)],
        same_M_c_group_count=len(groups),best_same_M_c_noise_union_size=group_details[0]['noise_union_size']if group_details else 0,
        same_M_c_all81_group_found=full_group is not None,full_group_allx_certificate=full_group,
        two_test_starts_imply_allx=False,route_details=route_details,same_M_c_groups=group_details)
    save('NEW_ROUTE4_SELECTED_PAIR.json',selected)
else:save('NEW_ROUTE4_PAIR_WORD_CERTIFICATE.json',dict(word_indices=covered,words_file='NEW_ROUTE4_WORDS625.json',types_file='NEW_ROUTE4_TYPES_AND_TRANSITIONS.json'))
result=dict(status='HYPOTHESIS_REFUTED_FULLRANK4_WORDS_DO_NOT_COVER_ALL_CONTROLLERPAIRS'if missing else'HYPOTHESIS_SUPPORTED_ALL192x192_PAIRS_HAVE_FULLRANK4_WORD',
    source_n=15552,controller_order=192,field='F3',fiber_dimension=4,actual960_arc_type_binding=True,
    global_type_count=5,length4_typewords=625,composed_noise_rank_histogram=rank_hist,
    fullrankword_covered_controller_pairs=192*192-len(missing),missing_controller_pairs=len(missing),missing_strata=dict(strata),
    missing_file='NEW_ROUTE4_MISSING_PAIRS.json',composed_words_file='NEW_ROUTE4_WORDS625.json',
    selected_one_pair=None if selected is None else selected['pair'],selected_pair_file=None if selected is None else'NEW_ROUTE4_SELECTED_PAIR.json',
    selected_pair_zero_basis_covered=None if selected is None else[d['covered']for d in selected['tested_starts']],
    selected_pair_same_M_c_full81_group=None if selected is None else selected['same_M_c_all81_group_found'],
    selected_pair_best_same_M_c_noise_union=None if selected is None else selected['best_same_M_c_noise_union_size'],
    fullrankword_missing_does_not_refute_source_D4=True,old_five_atomic_B_kernel_ranks_repeated=False,
    graph_BFS_solver_Lean_query_paidreview_runs=0,new_graph_parameter_Lean_count=0,
    CPU_seconds=time.process_time()-start,CPU_budget_seconds=10,running=False)
save('NEW_ROUTE4_RESULT.json',result);save('NEW_ROUTE4_TERMINAL.json',dict(status=result['status'],CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=10,running=False,selected_pairs_examined=0 if selected is None else 1))
save('NEW_ROUTE4_HANDLE.json',dict(status=result['status'],CPU_seconds=result['CPU_seconds'],running=False))
print(json.dumps(result))

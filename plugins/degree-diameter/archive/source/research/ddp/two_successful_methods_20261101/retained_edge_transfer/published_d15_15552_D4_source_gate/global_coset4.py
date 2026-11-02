"""Single finite global route-cover check; no graph, BFS or Lean execution."""
import collections,itertools,json,os,resource,time
from pathlib import Path
started=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(20,20))
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'research/ddp/more_graphs_20261027').is_dir())
def save(name,value):(D/name).write_text(json.dumps(value,indent=2)+'\n')
save('GLOBAL_COSET4_HANDLE.json',dict(pid=os.getpid(),running=True,CPU_budget_seconds=20))
bound=json.loads((D/'NEW_ROUTE4_TYPES_AND_TRANSITIONS.json').read_text())
types=bound['types'];T=bound['transition']
actual=json.loads((R/bound['source']).read_text())
for a in actual['arcs']:
    matches=[t['type']for t in types if(t['B'],t['v'],t['c'])==(a['B'],a['v'],a['c'])]
    assert len(matches)==1 and T[a['from']][matches[0]]==a['to']
def mv(A,x):return tuple(sum(A[i][j]*x[j]for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j]for k in range(4))%3 for j in range(4))for i in range(4))
def code(x):return sum((x[i]%3)*3**i for i in range(4))
def vec(n):return tuple(n//3**i%3 for i in range(4))
I=tuple(tuple(int(i==j)for j in range(4))for i in range(4));Z=(0,0,0,0)
words=[dict(word=(),M=I,c=Z,N=())];layer=words[:]
for length in range(1,4):
    new=[]
    for w in layer:
        for t in types:
            B,v,c=t['B'],t['v'],t['c'];mc=mv(B,w['c'])
            new.append(dict(word=w['word']+(t['type'],),M=mm(B,w['M']),
               c=tuple((mc[i]+c[i])%3 for i in range(4)),N=tuple(mv(B,q)for q in w['N'])+(tuple(v),)))
    words+=new;layer=new
assert len(words)==156
four=json.loads((D/'NEW_ROUTE4_WORDS625.json').read_text())
assert len(four)==625
words+=four
for wi,w in enumerate(words):w['word_index']=wi
references=list(range(31))
images=[];image_bits=[]
for w in words:
    H={}
    for noise in itertools.product(range(3),repeat=len(w['word'])):
        y=tuple(sum(col[i]*t for col,t in zip(w['N'],noise))%3 for i in range(4))
        H.setdefault(code(y),list(noise))
    images.append(H);image_bits.append(sum(1<<h for h in H))
FULL=(1<<81)-1
membership={}
def usable(rid,wi):
    key=(rid,wi)
    if key in membership:return membership[key]
    r,w=words[rid],words[wi];H=images[wi]
    columns=[code([(w['M'][i][j]-r['M'][i][j])%3 for i in range(4)])for j in range(4)]
    if any(h not in H for h in columns):membership[key]=None;return None
    delta=tuple((w['c'][i]-r['c'][i])%3 for i in range(4))
    K={code(tuple((vec(h)[i]+delta[i])%3 for i in range(4))):alpha for h,alpha in H.items()}
    value=dict(column_coefficients=[H[h]for h in columns],offset=delta,
               coset_witnesses=K,bits=sum(1<<h for h in K))
    membership[key]=value;return value
groups=[];memo={}
def group(rid,endpoint_words):
    key=(rid,tuple(endpoint_words))
    if key in memo:return memo[key]
    union=0;witnesses={};contributing=[]
    for wi in endpoint_words:
        u=usable(rid,wi)
        if u is None:continue
        gain=u['bits']&~union
        if gain:
            contributing.append(dict(word_index=wi,M_difference_column_noise_coefficients=u['column_coefficients'],
                                      constant_offset=u['offset']))
            for h,alpha in u['coset_witnesses'].items():
                witnesses.setdefault(h,dict(word_index=wi,noise_coefficients=alpha))
            union|=u['bits']
        if union==FULL:break
    gid=len(groups);memo[key]=gid
    groups.append(dict(group_index=gid,reference_word_index=rid,endpoint_word_indices=endpoint_words,
        actual_offset_coset_union_size=union.bit_count(),missing_coset_vector_codes=[h for h in range(81)if not(union>>h)&1],
        column_certificates=contributing,coset_vector_route_noise_witnesses=witnesses,
        complete=union==FULL,controller_pairs=[]))
    return gid
old_missing={tuple(v)for v in json.loads((D/'NEW_ROUTE4_MISSING_PAIRS.json').read_text())['ordered_pairs']}
pair_certs=[];remaining=[];fullrank_count=coset_count=0
for a in range(192):
    endpoints=[[]for _ in range(192)];fullrank=[None]*192
    for wi,w in enumerate(words):
        b=a
        for t in w['word']:b=T[b][t]
        endpoints[b].append(wi)
        if wi>=156 and w['rank']==4 and fullrank[b]is None:fullrank[b]=wi
    for b in range(192):
        if fullrank[b]is not None:
            assert(a,b)not in old_missing;fullrank_count+=1
            pair_certs.append(dict(a=a,b=b,kind='fullrank',word_index=fullrank[b]));continue
        assert(a,b)in old_missing
        refs=[wi for wi in endpoints[b]if wi<31];chosen=None;trials=[]
        for rid in refs:
            gid=group(rid,endpoints[b]);trials.append(gid)
            if groups[gid]['complete']:
                chosen=gid;break
        if chosen is None:
            remaining.append(dict(a=a,b=b,reference_candidates=refs,tried_cover_groups=trials,
                                  best_coset_union_size=max((groups[g]['actual_offset_coset_union_size']for g in trials),default=0)))
        else:
            coset_count+=1;groups[chosen]['controller_pairs'].append([a,b])
            pair_certs.append(dict(a=a,b=b,kind='coset',group_index=chosen,reference_word_index=groups[chosen]['reference_word_index']))
    if(a+1)%32==0:save('GLOBAL_COSET4_CHECKPOINT.json',dict(source_rows_complete=a+1,CPU_seconds=time.process_time()-started,
          fullrank_pairs=fullrank_count,coset_pairs=coset_count,remaining_pairs=len(remaining),distinct_groups=len(groups),running=True))
assert fullrank_count==33216 and coset_count+len(remaining)==3648
success=[g for g in groups if g['complete']];used=[g for g in success if g['controller_pairs']]
used_words=sorted({q['word_index']for g in used for q in g['column_certificates']})
selected_strata=collections.Counter('equal'if p['a']==p['b']else'adjacent'if p['b']in T[p['a']]else'other'for p in remaining)
save('GLOBAL_COSET4_WORDS781.json',words)
save('GLOBAL_COSET4_GROUPS.json',groups)
save('GLOBAL_COSET4_PAIR_CERTIFICATES.json',dict(controller_order=192,pairs=pair_certs,fullrank_word_global_index_offset=156))
save('GLOBAL_COSET4_REMAINING_PAIRS.json',dict(count=len(remaining),strata=dict(selected_strata),pairs=remaining))
result=dict(status='SUPPORTED_ALL3648_MISSING_PAIRS_HAVE_SHORT_REFERENCE_OFFSET_COSET_COVER'if not remaining else'REFUTED_GLOBAL_SHORT_REFERENCE_COSET_HYPOTHESIS',
    source_n=15552,controller_pairs=36864,fullrank_pairs_inherited=fullrank_count,coset_pairs_proved=coset_count,remaining_pairs=len(remaining),remaining_strata=dict(selected_strata),
    old_fullrank4_hypothesis_refuted_preserved=True,old_exactM39_and_two_start_limit_preserved=True,
    reference_max_length=2,route_max_length=4,actual960_arc_binding=True,global_words=781,
    inherited_length4_words=625,new_short_words=156,atomic_B_ranks_recomputed=False,
    distinct_reference_endpointwordmask_groups=len(groups),complete_groups=len(success),used_complete_cover_groups=len(used),
    used_coset_route_words=len(used_words),used_group_column_certificates=sum(len(g['column_certificates'])for g in used),
    used_group_column_membership_equations=4*sum(len(g['column_certificates'])for g in used),
    used_group_81cover_witnesses=81*len(used),inherited_inverse_noise_basis_equations=256*4,
    full_unconditional_source_D4_paper_interface=not remaining,Lean_kernel_status='NOT_STARTED',
    allx_coset_formula='Mw x+cw+Hw=Mr x+cr+((cw-cr)+Hw); noise=alpha-Σxi*di from storedcolumn andoffset-coset witnesses',
    first_remaining_gap=remaining[0]if remaining else None,
    graph_BFS_solver_Lean_newfield_query_paidreview_runs=0,new_graph_parameter_Lean_counts=0,
    CPU_seconds=time.process_time()-started,CPU_budget_seconds=20,running=False)
save('GLOBAL_COSET4_RESULT.json',result)
save('GLOBAL_COSET4_TERMINAL.json',dict(status=result['status'],CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=20,
    running=False,all36864_controllerpairs_have_actual_allx_cover_certificate=not remaining,Lean_started=False))
save('GLOBAL_COSET4_HANDLE.json',dict(status=result['status'],CPU_seconds=result['CPU_seconds'],running=False))
print(json.dumps(result))

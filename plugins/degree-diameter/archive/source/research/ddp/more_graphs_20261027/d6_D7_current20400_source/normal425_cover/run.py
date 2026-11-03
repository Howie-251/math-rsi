"""Bounded actual-permutation recovery of a normal425 abelian voltage cover."""
from array import array
from itertools import product
from pathlib import Path
import json
import resource
import time

START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(10,10))
OUT=Path(__file__).resolve().parent;SRC=OUT.parent/'rooted_wl_recovery'
meta=json.loads((SRC/'six_generators/GENERATORS.json').read_text())
n=meta['source_n'];assert n==20400 and meta['generated_group_order']==n
INV=[3,4,5,0,1,2]

def readints(path):
    a=array('I');a.frombytes(Path(path).read_bytes());return list(a)

S=[readints(r['map_file']) for r in meta['generators']]
assert len(S)==6 and all(len(a)==n for a in S)

def compose(a,b):return [a[x] for x in b]
def inverse(a):
    b=[0]*n
    for u,v in enumerate(a):b[v]=u
    return b
def word_image(word,x):
    for s in reversed(word):x=S[s][x]
    return x
def word_order(word):
    x=0
    for k in range(1,n+1):
        x=word_image(word,x)
        if x==0:return k
    raise AssertionError('not a permutation cycle')
def word_perm(word):
    return [word_image(word,x) for x in range(n)]
def power(a,e):
    ans=[0]*n;seen=[False]*n
    for start in range(n):
        if seen[start]:continue
        cyc=[];x=start
        while not seen[x]:seen[x]=True;cyc.append(x);x=a[x]
        assert x==start
        for j,v in enumerate(cyc):ans[v]=cyc[(j+e)%len(cyc)]
    return ans
def order0(a):
    x=0
    for k in range(1,n+1):
        x=a[x]
        if x==0:return k
    raise AssertionError
def commutes(a,b):return all(a[b[v]]==b[a[v]] for v in range(n))
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2)+'\n')
def stop(status,detail):
    d={'status':status,'detail':detail,'CPU_seconds':time.process_time()-START,
       'source_n':n,'source_BFS':0,'candidate_graphs':0,'group_enumeration':False,'pending':[],'running':False}
    save('RESULT.json',d);save('checkpoint.json',d);print(json.dumps(d));raise SystemExit

tested=[];a_witness=z_witness=None
for length in range(1,5):
    for word in product(range(6),repeat=length):
        if any(word[j]==INV[word[j-1]] for j in range(1,length)):continue
        if time.process_time()-START>8.0:stop('UNKNOWN_SHORT_WORD_CPU_LIMIT',{'tested':len(tested)})
        o=word_order(word);assert n%o==0
        tested.append({'word':list(word),'order':o})
        if a_witness is None and o%5==0:a_witness={'word':list(word),'order':o,'power':o//5}
        if z_witness is None and o%17==0:z_witness={'word':list(word),'order':o,'power':o//17}
        if a_witness and z_witness:break
    if a_witness and z_witness:break
save('WORD_SEARCH.json',{'scope_max_NB_words':936,'examined':tested,'a5_witness':a_witness,'z17_witness':z_witness,
                         'prefix_stop_after_both_witnesses':bool(a_witness and z_witness)})
if not(a_witness and z_witness):stop('UNKNOWN_NO_SUFFICIENT_WITNESSES_IN_936_WORD_SCOPE',{'tested':len(tested)})
a=power(word_perm(a_witness['word']),a_witness['power'])
z=power(word_perm(z_witness['word']),z_witness['power'])
assert order0(a)==5 and order0(z)==17
a0=set();x=0
for _ in range(5):a0.add(x);x=a[x]
b=None;conjugator_used=None;attempts=[]
for label,h in [('B^4',power(S[1],4)),('A',S[0]),('B',S[1]),('C',S[2])]:
    candidate=compose(compose(h,a),inverse(h))
    independent=candidate[0] not in a0
    commuting=commutes(a,candidate)
    attempts.append({'conjugator':label,'order':order0(candidate),'independent':independent,'commutes_a':commuting})
    if independent and commuting:b=candidate;conjugator_used=label;break
if b is None:stop('UNKNOWN_FIXED_CONJUGATORS_GIVE_NO_COMMUTING_INDEPENDENT_B5',attempts)
checks={'a_order':order0(a),'b_order':order0(b),'z_order':order0(z),
        'a_b_commute':commutes(a,b),'a_z_commute':commutes(a,z),'b_z_commute':commutes(b,z),
        'b0_outside_a0':b[0] not in a0}
if not all(checks[k] for k in ['a_b_commute','a_z_commute','b_z_commute','b0_outside_a0']):
    stop('REFUTED_SELECTED_GENERATOR_COMMUTATION_OR_INDEPENDENCE',checks)

def orbit(rep):
    rows=[];zk=rep
    for k in range(17):
        bj=zk
        for j in range(5):
            ai=bj
            for i in range(5):rows.append((ai,(i,j,k)));ai=a[ai]
            bj=b[bj]
        zk=z[zk]
    return rows
zero_rows=orbit(0);zero={v:c for v,c in zero_rows}
if len(zero)!=425:stop('REFUTED_N425_ORBIT_NOT_DISTINCT',len(zero))
normal=[]
for s in range(6):
    si=S[INV[s]]
    for label,g in [('a5',a),('b5',b),('z17',z)]:
        q=S[s][g[si[0]]]
        normal.append({'source_generator':s,'normal_generator':label,'conjugate0':q,
                       'N_coordinates':zero.get(q)})
if any(r['N_coordinates'] is None for r in normal):stop('REFUTED_SELECTED_N425_NORMALITY',normal)
save('checkpoint.json',{'status':'NORMAL425_VERIFIED_COORDINATES_IN_PROGRESS','short_words_tested':len(tested),
                       'a_witness':a_witness,'z_witness':z_witness,'checks':checks,'normality':normal})

coord=[None]*n;reps=[];coordinate_vertices=[]
for rep in range(n):
    if coord[rep] is not None:continue
    c=len(reps);reps.append(rep);rows=orbit(rep);assert len({v for v,_ in rows})==425
    block=[0]*425
    for v,(i,j,k) in rows:
        assert coord[v] is None
        coord[v]=(c,i,j,k);block[i+5*j+25*k]=v
    coordinate_vertices.extend(block)
assert len(reps)==48 and all(c is not None for c in coord)
raw=readints(SRC/'adjacency.csr.u32le.bin');assert raw[:2]==[20400,122400]
offsets=raw[2:2+n+1];flat=raw[2+n+1:]
adj=[flat[offsets[v]:offsets[v+1]] for v in range(n)]
bases=[]
for c,rep in enumerate(reps):
    darts=[]
    for port,w in enumerate(sorted(adj[rep])):
        d,i,j,k=coord[w]
        darts.append({'port':port,'to':d,'a':i,'b':j,'c17':k,'source_neighbor':w})
    bases.append({'base':c,'representative':rep,'darts':darts})
for c,base in enumerate(bases):
    for dart in base['darts']:
        inverse_port=[q['port'] for q in bases[dart['to']]['darts']
                      if (q['to'],q['a'],q['b'],q['c17'])==(c,(-dart['a'])%5,(-dart['b'])%5,(-dart['c17'])%17)]
        assert len(inverse_port)==1;dart['reverse_port']=inverse_port[0]
arcs=0
for v,(c,i,j,k) in enumerate(coord):
    generated=[]
    for d in bases[c]['darts']:
        idx=425*d['to']+(i+d['a'])%5+5*((j+d['b'])%5)+25*((k+d['c17'])%17)
        generated.append(coordinate_vertices[idx]);arcs+=1
    assert sorted(generated)==sorted(adj[v])
assert arcs==122400
for label,perm in [('a5',a),('b5',b),('z17',z)]:
    (OUT/f'{label}.pi.u32le.bin').write_bytes(array('I',perm).tobytes())
(OUT/'vertex_coordinates.u32le.bin').write_bytes(array('I',[x for row in coord for x in row]).tobytes())
(OUT/'coordinate_vertices.u32le.bin').write_bytes(array('I',coordinate_vertices).tobytes())
normal_meta={'a5':a_witness,'z17':z_witness,'b5_conjugator':conjugator_used,'fixed_conjugator_attempts':attempts,
             'checks':checks,'normality_via_regular_unique0image':normal,'orbit0_size':425,
             'normal_generator_maps':[str(OUT/f'{x}.pi.u32le.bin') for x in ['a5','b5','z17']]}
save('NORMAL_GENERATORS.json',normal_meta)
recipe={'status':'READY_ACTUAL_SOURCE_48_BASE_ABELIAN_VOLTAGE_RECIPE','source_n':n,'source_m':61200,
        'source_D_reported':7,'degree':6,'base_count':48,'moduli':[5,5,17],
        'base_ports':bases,'normal_generators':normal_meta,
        'vertex_coordinate_file':str(OUT/'vertex_coordinates.u32le.bin'),
        'vertex_coordinate_layout':'uint32 quadruples(base,i,j,k) in oldvertex order',
        'coordinate_vertex_file':str(OUT/'coordinate_vertices.u32le.bin'),
        'coordinate_vertex_layout':'uint32 oldvertex at425*base+i+5*j+25*k',
        'edge_rule':'(c,i,j,k) -- (dart.to,i+dart.a mod5,j+dart.b mod5,k+dart.c17 mod17)',
        'base_representative_rule':'Minimumoldvertex ofeachNorbit; bases inincreasing representativeorder',
        'port_order':'Neighbors ofeachrepresentative sorted byoldvertex ID',
        'full_source_darts_checked':122400,'full_source_edges_matched':61200,
        'reverse_port_binding_checked':True,'source_graph_CSR':str(SRC/'adjacency.csr.u32le.bin')}
save('COVER_RECIPE.json',recipe)
result={'status':recipe['status'],'short_words_tested':len(tested),'shortword_scope_max':936,
        'a_witness':a_witness,'z_witness':z_witness,'b5_conjugator':conjugator_used,
        'normal_N_structure':'C5 x C5 x C17','normal_N_order':425,'base_count':48,
        'source_n':n,'source_m':61200,'degree':6,'orders_and_commutation':checks,
        'normality_checks':18,'orbit_sizes':[425]*48,'all_vertex_coordinates':20400,
        'source_directed_adjacencies_matched':arcs,'source_undirected_edges_matched':61200,
        'source_graph_BFS':0,'large_group_enumeration':False,'multiplication_table':False,
        'new_candidates':0,'CPU_seconds':time.process_time()-START,'running':False,'pending':[]}
save('RESULT.json',result);save('checkpoint.json',result);save('terminal.json',result)
print(json.dumps(result,indent=2))

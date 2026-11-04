"""Independent reviewer: reads producer witnesses; writes reviewer result only.
Run with D:/anaconda/python.exe FOURTEEN_MAXIMAL_A_REVIEW_check.py.
No producer module is imported or executed.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
import hashlib,json,time

P=Path(__file__).resolve().parent
def read(n): return (P/n).read_bytes()
def js(n): return json.loads(read(n))
def sha(n): return hashlib.sha256(read(n)).hexdigest()
def short(a,b): return (a^b).bit_count()==1
def mask(s): return sum(1<<v for v in s)
start=time.time()
manifest=js('FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json')
for group in ('input_hashes','output_hashes'):
    for n,h in manifest[group].items(): assert sha(n)==h,(n,'hash')
assert sha('FOURTEEN_FORCED_REVIEW.json')=='3e3042d5ea24490589b7d75242d5140614503fc5dc920c6eee4a11c6358e34b1'
assert sha('TWELVE_NEW_FORCED_REVIEW.json')=='60317e5e8c091ece3d16834c71b29fd196ebee11d93a0ed8dbbab2cc4dc895dd'
up=js('FOURTEEN_FORCED_REVIEW.json'); local=js('TWELVE_NEW_FORCED_REVIEW.json')
assert up['verdict']==local['verdict']=='PASS'
assert up['details']['remaining_covered_target_geometries']==2587
assert up['details']['remaining_free_target_geometries']==0
assert up['details']['fourteen_hole_free_targets_proved'] is True
for r in up['details']['reports']:
    assert sha(f"FOURTEEN_FORCED_remaining_v{r['v']}_covered.bin")==r['remaining_sha256']
Z={39,43,45,51,60,63};J={1,2,4,8,14,16};W=J|{32}
G=set(range(32))-{0}-J
E=sorted(v for v in G if v.bit_count()%2==0)
O=sorted(G-set(E));T={z^32 for z in Z}
assert (len(E),len(O),T)==(15,10,{7,11,13,19,28,31})
adj=[[e for e in E if short(o,e)] for o in O]
# Exhaust actual matching domain with a fresh vertex recursion. Partner words
# encode each odd's exact even partner or 0 when unmatched. All maximal sizes
# are included; there is no cardinality cutoff or producer traversal dependence.
domain=set();hist=Counter()
def enumerate_domain(k,used,word,omitted,m):
    if k==len(O):
        if any(any(not (used>>e&1) for e in adj[j]) for j in omitted): return
        assert word not in domain
        domain.add(word);hist[m]+=1;return
    if O[k] not in T:
        enumerate_domain(k+1,used,word,omitted+(k,),m)
    for e in adj[k]:
        if not (used>>e&1):
            enumerate_domain(k+1,used|(1<<e),word|((e+1)<<(5*k)),omitted,m+1)
enumerate_domain(0,0,0,(),0)
assert hist=={10:274691,9:12772,8:6} and len(domain)==287469
print('Independent complete domain',dict(hist),flush=True)
perms=list(permutations(range(5)))
maps=[[sum(((v>>p[k])&1)<<k for k in range(5)) for v in range(32)] for p in perms]
row=next(r for r in js('FOURTEEN_RESIDUAL_STRUCTURE_maxA_options.json') if r['orbit_index']==85)
assert set(row['Z'])==Z and set(row['W'])==W
accepted={s['index']:s for s in local['details']['accepted_marked_statements']}
options={};bmaps=[];bclass=Counter()
for op in row['options']:
    q,t,w,b,c,pi=(op[k] for k in ('q','t','w','b','case','permutation'))
    assert q in E and t in T-{31} and short(q,t)
    assert w in {1,2,4,8,16} and b in {1,2,4,8,16}-{w}
    S=J-{w,b};M={0};major={z^32 for z in Z}-{t}|S;U=S
    R={v for v in range(32) if op['B_R']>>v&1}
    assert len(R)==2 and R&{w,b} and not R&(M|major)
    assert op['sources']==sorted(S)
    assert (op['B_M'],op['B_J'],op['B_U'])==(mask(M),mask(major),mask(U))
    # Every protected endpoint is original internally B covered and outside
    # ALL transfer endpoints: its A mirror is an original hole; it is outside
    # Y, Z, root32 and consumed z. Its original mate has opposite parity Y.
    assert not {w,b}&(U|{z^32 for z in Z}|{0,t})
    assert all(v.bit_count()%2==1 for v in R|U|{w,b})
    assert op['local_family']==21 and op['local_status']=='accepted'
    idx=op['local_id'];assert idx in {79,178,361,363,373}
    s=accepted[idx]
    # Minority singleton forces the translation to be zero; search a COMMON
    # coordinate permutation for minority, majority, omissions AND obstruction.
    witness=next((i for i,tr in enumerate(maps)
                  if {tr[v] for v in s['minority']}==M
                  and {tr[v] for v in s['majority']}==major
                  and {tr[v] for v in s['omitted']}==U
                  and {tr[v] for v in s['forced_pair']}==R),None)
    assert witness is not None,(idx,q,t,w,b)
    assert {maps[witness][s['forced_hole']]}==M
    bmaps.append(dict(q=q,t=t,w=w,b=b,case=c,forest_permutation=pi,
                      accepted_class=idx,common_map=perms[witness]))
    bclass[idx]+=1
    options[q,t,w,b,c,pi]=op
assert len(options)==len(row['options'])==208
print('Exact B common-map checks',dict(bclass),flush=True)
pools=[read(f'TWELVE_ROOT_STAR_OPENING_case_{c:02}_forests.bin') for c in range(5)]
raw=read('FOURTEEN_RESIDUAL_STRUCTURE_maxA_full_85_certificates.bin')
assert len(raw)==32*len(domain)
seen=set();sizes=Counter();cases=Counter();usedforests=set();endhist=Counter()
for offset in range(0,len(raw),32):
    a=raw[offset:offset+32];m=a[22];q,t,w,b,c=a[23:28];fi=int.from_bytes(a[28:30],'little');pi=a[30]
    assert 0<=m<=11 and a[31]==1 and (q,t,w,b,c,pi) in options
    assert all(v==255 for v in a[2*m:22])
    L=[tuple(a[k:k+2]) for k in range(0,2*m,2)]
    assert L==sorted(L)
    covered=set();word=0
    for x,y in L:
        assert x<y and x in G and y in G and short(x,y)
        assert x not in covered and y not in covered
        covered.update((x,y));o=x if x in O else y;e=y if x in O else x
        word|=(e+1)<<(5*O.index(o))
    assert T<=covered and q not in covered
    assert word in domain and word not in seen
    seen.add(word)
    block=pools[c][32*fi:32*(fi+1)];assert len(block)==32
    tr=maps[pi];F=[(tr[block[k]],tr[block[k+1]]) for k in range(0,32,2)]
    parent=list(range(32));deg=[0]*32
    def root(x):
        while parent[x]!=x: x=parent[x]
        return x
    def insert(x,y):
        rx,ry=root(x),root(y)
        assert rx!=ry,('labelled cycle',offset,x,y)
        parent[rx]=ry;deg[x]+=1;deg[y]+=1
    for x,y in F:
        assert short(x,y);insert(x,y)
    assert all(deg[x]==(0 if x in (0,31) else 2 if x in (q,b) else 1) for x in range(32))
    assert any({x,y}=={q,t} for x,y in F)
    h=next(y if x==31 else x for x,y in L if 31 in (x,y))
    Lp=[(x,y) for x,y in L if 31 not in (x,y)]+[(w,h)]
    for x,y in Lp: insert(x,y)
    assert all(deg[x]==0 if x in (0,31) else deg[x] in (1,2) for x in range(32))
    ends={x for x in range(32) if deg[x]==1}
    assert ends==((G-covered)-{q})|(J-{w,b})
    assert len(ends)>=8 and sum(v.bit_count()%2==0 for v in ends)*2==len(ends)
    assert len({root(v) for v in range(32) if deg[v]})==len(ends)//2
    assert q not in ends and t not in ends and 14 in ends
    sizes[m]+=1;cases[c]+=1;endhist[len(ends)]+=1;usedforests.add((c,fi,pi))
assert seen==domain and sizes==hist
print('All physical forest witnesses, exact endpoints and labelled unions PASS',flush=True)
# Exact orbit and byte-for-byte disjoint complements, including supplied maps.
rep=sorted(Z)+sorted(W)
orbit=set()
for tr in maps:
    full=lambda x:tr[x&31]|(x&32)
    orbit.add(tuple(sorted(full(x) for x in Z))+tuple(sorted(full(x) for x in W)))
assert len(orbit)==60
transport=js('FOURTEEN_RESIDUAL_STRUCTURE_maxA_transport.json');transportset=set()
reports=[]
for v in (1,7,31):
    source=read(f'FOURTEEN_FORCED_remaining_v{v}_covered.bin');assert len(source)%13==0
    rr=[tuple(source[k:k+13]) for k in range(0,len(source),13)]
    assert len(rr)==len(set(rr))
    positive=[r for r in rr if v==31 and r in orbit]
    remain=[r for r in rr if not(v==31 and r in orbit)]
    for label,rows in [('positive',positive),('remaining',remain)]:
        assert read(f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_{label}_v{v}_covered.bin')==b''.join(map(bytes,rows))
    if v==31:
        assert set(positive)==orbit
        for item in transport:
            i=item['source_index'];p=item['permutation_output_reads_input']
            assert sorted(p)==list(range(6))
            f=lambda x:sum(((x>>p[k])&1)<<k for k in range(6))
            target=tuple(sorted(f(x) for x in Z))+tuple(sorted(f(x) for x in W))
            assert target==tuple(item['actual_record'])==rr[i]
            assert f(0)==0 and f(31)==31
            assert target not in transportset;transportset.add(target)
    reports.append(dict(v=v,input=len(rr),positive=len(positive),remaining=len(remain)))
assert transportset==orbit and [r['remaining'] for r in reports]==[240,702,1585]
result=dict(status='PASS',independent_domain_count=len(domain),size_histogram=dict(hist),
 certificates_checked=len(seen),case_histogram=dict(cases),endpoint_histogram=dict(endhist),
 distinct_transformed_forests=len(usedforests),B_options_checked=len(options),B_class_histogram=dict(bclass),
 B_common_maps=bmaps,application_reports=reports,transport_count=len(transportset),
 manifest_hash=sha('FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json'),
 source_review_hash=sha('FOURTEEN_FORCED_REVIEW.json'),
 local_review_hash=sha('TWELVE_NEW_FORCED_REVIEW.json'),elapsed_seconds=time.time()-start)
(P/'FOURTEEN_MAXIMAL_A_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='B_common_maps'},indent=2))

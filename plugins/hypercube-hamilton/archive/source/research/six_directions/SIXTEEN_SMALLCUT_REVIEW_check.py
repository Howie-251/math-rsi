"""Independent read-only certificate checker. No producer modules imported.
Run with D:/anaconda/python.exe; writes only its own check-result JSON.
"""
from pathlib import Path
import hashlib, itertools, json
from collections import Counter

P = Path(__file__).resolve().parent
def read(name): return (P/name).read_bytes()
def obj(name): return json.loads(read(name))
def sha(name): return hashlib.sha256(read(name)).hexdigest()
assert sha('SIXTEEN_SMALLCUT_MANIFEST.json') == '944a4a0f22448c318e2306e5d53e9e0747d29b81f959a575f809527cd952325a'
mf = obj('SIXTEEN_SMALLCUT_MANIFEST.json')
hash_checks = 1
for group in ('input_hashes', 'output_hashes'):
    for name, digest in mf[group].items():
        assert sha(name) == digest, name
        hash_checks += 1
for name, size in mf['output_sizes'].items(): assert len(read(name)) == size
assert sha('SIXTEEN_LOCAL_REVIEW.json') == '762ec4f5555a255e0182c0a6c9f0d235e4255a917dbf73651a74c5c121e07060'
prior = obj('SIXTEEN_LOCAL_REVIEW.json')
assert prior['verdict'] == 'PASS'
for v in (1,7,31):
    name=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin'
    assert sha(name) == prior['audited_input_hashes'][name]
assert obj('Q5_A10_FULL_REVIEW.json')['details']['all_balanced_Q5_endpoints_proved_modulo_imports']

HE={0,3,5}; HO={1,2,14,22,25,26,28}; H=HE|HO; U={1,2}
K=set(range(32))-H; reduced=K-{13,21,30,31}
local=obj('SIXTEEN_SMALLCUT_local.json')
assert set(local['covered'])==K and set(local['twice_reduced_vertices'])==reduced
assert local['geometry']['minority']==sorted(HE)
assert local['geometry']['majority']==sorted(HO)
assert local['geometry']['omitted']==sorted(U)
assert local['required_edge']==[30,31] and local['forbidden_pair']==[13,21]
assert len(set(local['source_rows']))==256

class DSU:
    def __init__(self, vertices): self.p={v:v for v in vertices}
    def root(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def join(self,a,b):
        a,b=self.root(a),self.root(b)
        if a==b: return False
        self.p[a]=b
        return True
def pairs(block, vertices):
    assert len(block)==len(vertices)
    assert set(block)==set(vertices) and len(set(block))==len(block)
    return list(zip(block[::2],block[1::2]))
def mate(edge_list):
    return {a:b for x,y in edge_list for a,b in ((x,y),(y,x))}

forest_data=read('SIXTEEN_SMALLCUT_forests.bin')
source_data=read('Q5_T37_INDEPENDENT_orbit_00_forests.bin')
source_pairs=read('Q5_T37_INDEPENDENT_orbit_00_pairs.bin')
row_data=read('SIXTEEN_SMALLCUT_pairs18.bin')
column_data=read('SIXTEEN_SMALLCUT_columns18.bin')
matrix_data=read('SIXTEEN_SMALLCUT_matrix.bin')
rows=[]; cols=[]
for i, source_index in enumerate(local['source_rows']):
    block=forest_data[38*i:38*(i+1)]
    assert block==source_data[38*source_index:38*(source_index+1)]
    edges=list(zip(block[::2],block[1::2])); assert len(set(edges))==19
    adj={x:[] for x in range(32)}; dsu=DSU(range(32))
    for a,b in edges:
        assert a in adj and b in adj and (a^b).bit_count()==1
        assert dsu.join(a,b), ('cycle',i)
        adj[a].append(b); adj[b].append(a)
    assert all(len(adj[x])==(0 if x in U else 2 if x in H else 1) for x in adj)
    components={}
    for x in set(range(32))-U: components.setdefault(dsu.root(x),[]).append(x)
    endpoint_pairs=[]
    for comp in components.values():
        ends=[x for x in comp if x in K]
        assert len(ends)==2
        endpoint_pairs.append(tuple(ends))
    pm=mate(endpoint_pairs)
    assert pm==mate(pairs(source_pairs[22*source_index:22*(source_index+1)],K))
    assert pm[30]!=31 and (30,31) not in edges and (31,30) not in edges
    # Independent graph suppression: merge endpoints 30 and 31 by the required edge.
    augmented=DSU(K)
    for a,b in endpoint_pairs+[(30,31)]: assert augmented.join(a,b)
    groups={}
    for x in K-{30,31}: groups.setdefault(augmented.root(x),[]).append(x)
    assert all(len(g)==2 for g in groups.values())
    q=mate([tuple(g) for g in groups.values()])
    assert q[13]==21
    expected={x:q[x] for x in reduced}
    ep=pairs(row_data[18*i:18*(i+1)],reduced)
    assert mate(ep)==expected
    rows.append(ep)
for j in range(256): cols.append(pairs(column_data[18*j:18*(j+1)],reduced))
assert len({tuple(c) for c in cols})==256
bits=0; pivots={}
for i,row in enumerate(rows):
    encoded=0
    for j,col in enumerate(cols):
        dsu=DSU(reduced)
        for a,b in row+col: dsu.join(a,b)
        connected=len({dsu.root(x) for x in reduced})==1
        encoded |= int(connected)<<j; bits+=1
    assert encoded==int.from_bytes(matrix_data[32*i:32*(i+1)],'little'), i
    residue=encoded
    while residue:
        lead=residue.bit_length()-1
        if lead in pivots: residue ^= pivots[lead]
        else: pivots[lead]=residue; break
assert len(pivots)==256

perms=list(itertools.permutations(range(5)))
def parity(x): return x.bit_count()%2
def project(x,d):
    return sum(((x>>bit)&1)<<i for i,bit in enumerate(b for b in range(6) if b!=d))
def lift(q,d): return sum(((q>>i)&1)<<bit for i,bit in enumerate(b for b in range(6) if b!=d))
def permute(x,perm): return sum(((x>>perm[i])&1)<<i for i in range(5))
def chunks(name):
    b=read(name); assert len(b)%15==0
    return [tuple(b[i:i+15]) for i in range(0,len(b),15)]
def forced_chain(record,chain):
    alive=set(range(64))-{0}-set(record)
    forced=[]
    for leaf,other in chain:
        assert leaf in alive and other in alive
        neighbors={leaf^(1<<d) for d in range(6)} & alive
        assert neighbors=={other}
        forced.append(frozenset((leaf,other))); alive-={leaf,other}
    return forced

application=obj('SIXTEEN_SMALLCUT_application.json')
witnesses=application['witnesses']; assert len(witnesses)==118
by_key={(w['v'],w['input_index']):w for w in witnesses}; assert len(by_key)==118
reports=[]; remaining_all=[]
for v in (1,7,31):
    records=chunks(f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin')
    assert len(set(records))==len(records)
    positives=[]; remaining=[]
    for index,record in enumerate(records):
        Z=set(record[:7]); W=set(record[7:])
        assert len(Z)==7 and len(W)==8 and 0 not in Z|W
        assert all(parity(z)==0 for z in Z) and all(parity(w)==1 for w in W)
        assert all((z^w).bit_count()!=1 for z in Z for w in W)
        assert v not in Z|W and parity(v)==1
        w=by_key.get((v,index))
        if w is None: remaining.append(record); continue
        positives.append(record)
        assert tuple(w['record'])==record
        d=w['cut']; assert 0<=d<6 and (v>>d)&1
        A={x for x in range(64) if (x>>d)&1}; B=set(range(64))-A
        assert len(Z&A)==4 and len(W&A)==3
        S=set(w['sources']); assert len(S)==2 and S<=Z&A
        Y={s^(1<<d) for s in S}
        ca=w['canonical_anchor']; aa=w['actual_anchor']; perm=perms[w['permutation_index']]
        assert ca in HE and aa in {project(x,d) for x in Z&B}
        image=lambda x:lift(permute(x^ca,perm)^aa,d)
        assert {image(x) for x in range(32)}==B
        assert {image(x) for x in HE}==Z&B
        assert {image(x) for x in HO}==(W&B)|Y
        assert {image(x) for x in U}==Y
        e={image(30),image(31)}; R={image(13),image(21)}
        assert e==set(w['actual_required_edge']) and R==set(w['actual_forbidden_pair'])
        assert e<=B and not e&Y and len(e)==2
        assert (min(e)^max(e)).bit_count()==1
        assert e<=set(range(64))-{0}-Z-W
        assert frozenset(e) in forced_chain(record,w['leaf_chain'])
        assert 0 not in R and not R&Y and len(R)==2
        assert R<=set(range(64))-{0}-Z-W
        assert all(parity(x)==parity(next(iter(Y))) for x in R)
    assert positives==chunks(f'SIXTEEN_SMALLCUT_positive_v{v}_covered.bin')
    assert remaining==chunks(f'SIXTEEN_SMALLCUT_remaining_v{v}_covered.bin')
    reports.append(dict(v=v,input=len(records),positive=len(positives),remaining=len(remaining)))
    remaining_all.extend(remaining)
assert reports==application['reports']
assert [r['positive'] for r in reports]==[0,18,100]
assert [r['remaining'] for r in reports]==[0,0,30]
assert len(set(remaining_all))==30
# Verify all 30 residual records are exactly one orbit of the first under target31 stabilizer.
def act6(x,p): return sum(((x>>p[i])&1)<<i for i in range(6))
seed=remaining_all[0]; orbit=set()
for p in itertools.permutations(range(6)):
    if act6(31,p)!=31: continue
    orbit.add(tuple(sorted(act6(x,p) for x in seed[:7]))+tuple(sorted(act6(x,p) for x in seed[7:])))
assert orbit==set(remaining_all)
# 'root-star': all six odd neighbors of root0 occur among W.
assert all({1<<d for d in range(6)} <= set(r[7:]) for r in remaining_all)

# Counterexample pass for the new prescribed-gap argument. No cube/path theorem
# is guessed: exhaust arbitrary abstract simple paths and all legal other gaps.
def matchings(xs):
    if not xs: yield []; return
    x=xs[0]
    for i,y in enumerate(xs[1:],1):
        for rest in matchings(xs[1:i]+xs[i+1:]): yield [(x,y)]+rest
abstract_cases=0
for n,c in ((6,3),(8,3),(8,5)):
    gap=list(range(1,c+2)); ports=set(range(2,c+2))
    for v in (2,n-1):
        if v==1: continue
        internal=[x for x in range(n) if x not in (0,v)]
        for residual_D in matchings([x for x in gap if x not in (2,3)]):
            D={frozenset(e) for e in [(2,3)]+residual_D}
            for middle in itertools.permutations(internal):
                path=(0,)+middle+(v,); path_edges={frozenset(e) for e in zip(path,path[1:])}
                if not D<=path_edges: continue  # A theorem path must retain D.
                ds=DSU(range(n+len(gap)+2))
                for edge in path_edges-D: assert ds.join(*edge)
                # Unique B leaves for each gap, source r, and tagged root.
                leaf={a:n+i for i,a in enumerate(gap)}
                for a,b in leaf.items(): assert ds.join(a,b)
                assert ds.join(0,n+len(gap))
                assert ds.join(v,n+len(gap)+1)
                assert ds.root(leaf[2])!=ds.root(leaf[3])
                leafsets={}
                for b in list(leaf.values())+[n+len(gap),n+len(gap)+1]:
                    leafsets.setdefault(ds.root(b),[]).append(b)
                assert all(len(ls)==2 for ls in leafsets.values())
                abstract_cases+=1
assert abstract_cases>0
result=dict(status='PASS',manifest_sha256=sha('SIXTEEN_SMALLCUT_MANIFEST.json'),
    hash_comparisons=hash_checks,forests=256,reduced_rows=256,columns=256,
    connectivity_bits_recomputed=bits,independent_GF2_rank=len(pivots),
    reports=reports,exact_rootstar_orbit_size=len(orbit),
    prescribed_gap_abstract_path_cases=abstract_cases,
    producer_code_executed_or_imported=False,
    full_fourteen_hole_proved=False,full_sixteen_hole_proved=False,full_P6_proved=False)
(P/'SIXTEEN_SMALLCUT_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

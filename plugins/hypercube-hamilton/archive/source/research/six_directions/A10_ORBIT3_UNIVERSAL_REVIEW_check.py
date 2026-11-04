"""Fresh checker: DSU connectivity and low-column Gauss elimination.
Does not import/execute producer code; writes only reviewer evidence.
"""
from pathlib import Path
import json, hashlib, time
R=Path(__file__).resolve().parent
H={0,1,2,4,8,15,23,27,29,30}; K=set(range(32))-H
def sha(p): return hashlib.sha256((R/p).read_bytes()).hexdigest()
def readj(p): return json.loads((R/p).read_text(encoding='utf-8-sig'))
def records(p,n):
    b=(R/p).read_bytes(); assert len(b)%n==0
    return [list(zip(b[i:i+n:2],b[i+1:i+n:2])) for i in range(0,len(b),n)]
class DSU:
    def __init__(self): self.p=list(range(32))
    def root(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def join(self,x,y):
        a,b=self.root(x),self.root(y)
        if a==b: return False
        self.p[a]=b; return True
def matching(m):
    assert len(m)==11 and len({x for e in m for x in e})==22
    assert {x for e in m for x in e}==K
    assert all(a<b for a,b in m) and m==sorted(m)
start=time.time()
manifest=readj('A10_ORBIT3_UNIVERSAL_MANIFEST.json')
hashchecks={}
for e in manifest['files']:
    assert (R/e['file']).stat().st_size==e['bytes']
    assert sha(e['file'])==e['sha256']; hashchecks[e['file']]=sha(e['file'])
frozen=readj('A10_ORBIT3_SPECTRUM_FROZEN.json')
for p,h in frozen['input_hashes'].items():
    assert sha(p)==h.removeprefix('sha256:'); hashchecks[p]=sha(p)
P=records('A10_ORBIT3_UNIVERSAL_rank_selected_pairs.bin',22)
S=records('A10_ORBIT3_UNIVERSAL_rank_selected_forests.bin',40)
X=records('A10_ORBIT3_UNIVERSAL_rank_columns.bin',22)
assert len(P)==len(S)==len(X)==1024
inds=readj('A10_ORBIT3_UNIVERSAL_rank.json')['selected_row_indices']
srcp=(R/'A10_ORBIT3_SPECTRUM_pairs.bin').read_bytes()
srcs=(R/'A10_ORBIT3_SPECTRUM_forests.bin').read_bytes()
for i,(p,s) in enumerate(zip(P,S)):
    matching(p); assert len(s)==20 and len(set(s))==20 and s==sorted(s)
    d=DSU(); deg=[0]*32
    for a,b in s:
        assert 0<a<b<32 and (a^b).bit_count()==1
        assert d.join(a,b), 'cycle in forest'
        deg[a]+=1; deg[b]+=1
    assert deg[0]==0
    assert all(deg[v]==(2 if v in H else 1) for v in range(1,32))
    groups={}
    for v in range(1,32): groups.setdefault(d.root(v),[]).append(v)
    assert len(groups)==11
    ends=[]
    for comp in groups.values():
        ep=sorted(v for v in comp if deg[v]==1)
        assert len(ep)==2; ends.append(tuple(ep))
    assert sorted(ends)==p
    j=inds[i]
    assert bytes(x for e in p for x in e)==srcp[j*22:(j+1)*22]
    assert bytes(x for e in s for x in e)==srcs[j*40:(j+1)*40]
for x in X: matching(x)
saved=(R/'A10_ORBIT3_UNIVERSAL_rank_matrix.bin').read_bytes()
assert len(saved)==1024*128
rows=[]; ones=0; common_success=0
for i,p in enumerate(P):
    bits=0
    for j,x in enumerate(X):
        d=DSU()
        for a,b in p: d.join(a,b)
        for a,b in x: d.join(a,b)
        ok=len({d.root(v) for v in K})==1
        if ok:
            assert not set(p).intersection(x)
            bits |= 1<<j; ones+=1
    assert bits==int.from_bytes(saved[128*i:128*(i+1)],'little')
    rows.append(bits)
# Column scanning with row swaps/elimination below pivot, lowest column first.
# Producer uses streaming highest-bit pivots and saved combinations; neither used.
work=rows.copy(); rank=0
for col in range(1024):
    pivot=next((r for r in range(rank,1024) if (work[r]>>col)&1),None)
    if pivot is None: continue
    work[rank],work[pivot]=work[pivot],work[rank]
    for r in range(rank+1,1024):
        if (work[r]>>col)&1: work[r]^=work[rank]
    rank+=1
assert rank==1024
out={'status':'PASS','selected_forests_checked':1024,'selected_pair_source_alignment':True,
     'valid_matching_columns':1024,'matrix_bits_recomputed_DSU':1024**2,
     'matrix_bits_match_saved':True,'matrix_ones':ones,'GF2_rank_low_column_gauss':rank,
     'producer_elimination_artifacts_used':False,'complete_spectrum_exhaustiveness_checked':False,
     'audited_input_hashes':hashchecks,'seconds':time.time()-start}
(R/'A10_ORBIT3_UNIVERSAL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='audited_input_hashes'},indent=2))

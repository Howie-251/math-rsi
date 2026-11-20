"""Separate equation-level reconstruction of the84 necessary formula.

Does not import/execute the first builder or read its CNF during reconstruction.
Only the semantic key -> variable bijection is reused.  The six-point library
is exhaustively recalculated; every imported hole support is reconstructed.
Original-CNF/proof hashes and a second external DRAT bind the resulting bytes.
"""
import collections as co
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
assert platform.system() == 'Linux'
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
ROOT = Path(__file__).resolve().parent
FIRST = ROOT / 'chain858-v2'
OUT = ROOT / 'independent84-v2'

def save(p,x):
    t=p.with_suffix('.tmp'); t.write_text(json.dumps(x,indent=2)); t.replace(p)
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

W=list(it.combinations(range(1,10),3))
ht=[tuple(w[2-j]-3+j for j in range(3)) for w in W]
I=[{(c,r) for c in range(1,4) for r in range(1,h[c-1]+1)} for h in ht]
G=set(it.product(range(1,4),range(1,7)))
successors={a:[b for b in range(84) if I[a]<I[b]] for a in range(84)}
AB=[(a,b) for a in range(84) for b in successors[a]]
ABC=[(a,b,c) for a,b in AB for c in successors[b]]

def verify_library(path):
    records=json.loads(path.read_text())['templates']; bymask={r['mask']:r for r in records}
    assert len(records)==len(bymask)==843
    triples=list(it.combinations(range(6),3)); ti={t:j for j,t in enumerate(triples)}
    packets=[[ti[t] for t in it.combinations(q,3)] for q in it.combinations(range(6),4)]
    valid={0,1,3,7,8,12,14,15}; legal=accepted=0
    for mask in range(1<<20):
        if any(sum(((mask>>v)&1)<<j for j,v in enumerate(q)) not in valid for q in packets): continue
        legal+=1; labels={}
        for b in range(1,6):
            for a in range(b):
                rank=[1,1]
                for p in range(a):
                    color=(mask>>ti[p,a,b])&1
                    rank[color]=max(rank[color],labels[p,a][color]+1)
                labels[a,b]=rank
        if any(v[0]>3 for v in labels.values()):
            assert mask not in bymask; continue
        accepted+=1; rec=bymask[mask]
        shapes=[tuple(max([v[1] for (a,b),v in labels.items() if b==z and v[0]>=c]+[0]) for c in range(1,4)) for z in range(6)]
        words=[tuple(h[2-j]+j+1 for j in range(3)) for h in shapes]
        assert shapes==list(map(tuple,rec['shapes_in_actual_order']))
        assert words==list(map(tuple,rec['words_in_actual_order']))
        assert {(r['start'],r['end']):r['label'] for r in rec['pair_labels']}==labels
    assert (legal,accepted)==(908,843)
    return records,{'all_masks':1<<20,'packet_legal':legal,'no_blue5':accepted,'sha256':digest(path)}

def verify_rows(filepath):
    given=json.loads(filepath.read_text()); assert given['states']==list(map(list,W))
    index={w:s for s,w in enumerate(W)}; necessary={}
    def register(words,d):
        support=tuple(sorted(index[w] for w in words))
        necessary[support]=max(d,necessary.get(support,0))
    # Baek native Y,S,P,E paths on the mother and each one-coordinate trace.
    for fixed in [()]+[(v,) for v in range(1,10)]:
        for include in (False,True) if fixed else (False,):
            a=3-int(bool(fixed) and include); b=6-int(bool(fixed) and not include)
            remain=[v for v in range(1,10) if v not in fixed]
            for asc in it.combinations_with_replacement(range(1,b+1),a-1):
                q=asc[::-1]
                for bits in it.product((0,1),repeat=a-1):
                    p=tuple(x+y for x,y in zip(q,bits))
                    if any(p[j]<p[j+1] for j in range(a-2)): continue
                    if any(p[j]>((b,)+q)[j] for j in range(a-1)): continue
                    lo=tuple(t-1 for t in p)+(0,); hi=(b,)+q
                    path={hi[:j]+lo[j:] for j in range(a+1)}
                    path|={tuple(max(l,min(h,r)) for l,h in zip(lo,hi)) for r in range(b+1)}
                    assert len(path)==a+b
                    words=[tuple(sorted(tuple(remain[h+a-1-j] for j,h in enumerate(shape))+(fixed if include else ()))) for shape in path]
                    register(words,a+b-7)
    for aa,bb,cap in [(3,6,66),(3,5,50),(2,6,22)]:
        for inc in it.combinations(range(1,10),3-aa):
            for exc in it.combinations([v for v in range(1,10) if v not in inc],6-bb):
                words=[w for w in W if set(inc)<=set(w) and not set(exc)&set(w)]
                register(words,len(words)-cap)
    # All six-column three-threshold horizontal2x6 embeddings.
    thresholds=list(it.combinations(range(4),3))
    maps=0
    def visit(cols):
        nonlocal maps
        if len(cols)==6:
            images=set()
            for ws in it.combinations_with_replacement(range(3),6):
                widths=[col[w] for col,w in zip(cols,ws[::-1])]
                heights=[sum(v>=c for v in widths) for c in range(1,4)]
                images.add(tuple(sorted(h+3-j for j,h in enumerate(heights))))
            assert len(images)==28; register(images,6); maps+=1; return
        for t in thresholds:
            if cols and (any(t[j]>cols[-1][j] for j in range(3)) or any(t[j]>cols[-1][j-1]+1 for j in (1,2))): continue
            visit(cols+[t])
    visit([])
    assert len(given['rows'])==len(necessary)==563
    for r in given['rows']:
        d=len(r['support'])-50 if r['kind']=='slice-(3, 5)' else r['demand']
        assert necessary[tuple(r['support'])]==d,(r,necessary.get(tuple(r['support'])))
    return given['rows'],{'supports':len(necessary),'horizontal_maps':maps,'sha256':digest(filepath)}

def reconstruct():
    OUT.mkdir(exist_ok=False); start=time.monotonic()
    meta=json.loads((FIRST/'model/metadata.json').read_text())
    assert meta['words']==list(map(list,W)) and meta['heights']==list(map(list,ht))
    ledger={tuple(k):v for k,v in meta['semantic_variables']}
    assert len(ledger)==len(meta['semantic_variables']) and set(ledger.values())==set(range(1,len(ledger)+1))
    used=set()
    def V(*key): used.add(key); return ledger[key]
    body=OUT/'body.cnf'; f=body.open('w'); counts=co.Counter()
    def C(lits,kind):
        f.write(' '.join(map(str,lits))+' 0\n'); counts[kind]+=1
    H=[V('h',s) for s in range(84)]
    def O(a,b): return V('order',min(a,b),max(a,b))*(1 if a<b else -1)
    for a,b,c in it.combinations(range(84),3):
        C([-O(a,b),-O(b,c),O(a,c)],'order'); C([O(a,b),O(b,c),-O(a,c)],'order')
    for a,b in AB: C([O(a,b)],'ideal_order')
    labels={(p,a,b):{g:V(p,a,b,*g) for g in sorted(I[b]-I[a])} for p in ('l','u') for a,b in AB}
    for p in ('l','u'):
        for a,b in AB:
            ds=labels[p,a,b]; C(list(ds.values()),'label')
            for x,y in it.combinations(ds.values(),2): C([-x,-y],'label')
            for (x,y),v in ds.items():
                forbidden=(x>sum(t>0 for t in ht[a])+1 or y>ht[a][0]+1) if p=='l' else (x<sum(t==6 for t in ht[b]) or y<ht[b][2])
                if forbidden:C([H[a],H[b],-v],'extent')
    for a,b in AB:
        for g,lv in labels['l',a,b].items():
            for q,uv in labels['u',a,b].items():
                if any(x>y for x,y in zip(g,q)): C([H[a],H[b],-lv,-uv],'l_le_u')
    color={t:V('color',*t) for t in ABC}
    for a,b,c in ABC:
        for p in ('l','u'):
            for g,x in labels[p,a,b].items():
                for q,y in labels[p,b,c].items():
                    for coordinate,sign in [(0,1),(1,-1)]:
                        if q[coordinate]<=g[coordinate]:C([H[a],H[b],H[c],-x,-y,sign*color[a,b,c]],'growth')
    first=ht.index((0,0,0)); second=ht.index((1,0,0)); penult=ht.index((6,6,5)); last=ht.index((6,6,6))
    for s in (first,second,penult,last):C([-H[s]],'extreme_units')
    for a,b in AB:
        if a==first:C([H[b],labels['l',a,b][1,1]],'first')
        if b==last:C([H[a],labels['u',a,b][3,6]],'last')
        if a==second:
            for g,v in labels['l',a,b].items():
                if g not in ((1,2),(2,1)):C([H[b],-v],'second')
            if (first,a,b) in color:
                for sign,g in [(-1,(1,2)),(1,(2,1))]: C([H[b],sign*color[first,a,b]]+([labels['l',a,b][g]] if g in labels['l',a,b] else []),'second')
        if b==penult:
            for g,v in labels['u',a,b].items():
                if g not in ((2,6),(3,5)):C([H[a],-v],'penult')
            if (a,b,last) in color:
                for sign,g in [(-1,(3,5)),(1,(2,6))]:C([H[a],sign*color[a,b,last]]+([labels['u',a,b][g]] if g in labels['u',a,b] else []),'penult')
    E={}; samepair=co.defaultdict(list)
    for a,b in it.permutations(range(84),2):
        for x,y in sorted(I[b]-I[a]):
            if ((x,y)==(1,1) and a!=first) or ((x,y)==(3,6) and b!=last):continue
            if x>sum(h>0 for h in ht[a])+1 or y>ht[a][0]+1 or x<sum(h==6 for h in ht[b]) or y<ht[b][2]:continue
            v=V('corner',a,b,x,y); E[a,b,(x,y)]=v; samepair[a,b].append(v)
            C([-v,-H[a]],'corner');C([-v,-H[b]],'corner');C([-v,O(a,b)],'corner')
            if (a,b) in AB:
                for p in ('l','u'):C([-v,labels[p,a,b][x,y]],'corner')
    for values in samepair.values():
        for x,y in it.combinations(values,2): C([-x,-y],'corner_unique')
    for s in range(84):
        for x,y in G:
            g=(x,y)
            if g in I[s] and (x+1,y) not in I[s] and (x,y+1) not in I[s]: C([H[s]]+[v for (a,b,q),v in E.items() if b==s and q==g],'in_corner')
            if g not in I[s] and (x==1 or (x-1,y) in I[s]) and (y==1 or (x,y-1) in I[s]): C([H[s]]+[v for (a,b,q),v in E.items() if a==s and q==g],'out_corner')
    B3={(a,b):V('b3',a,b) for a,b in AB}; B4={(a,b):V('b4',a,b) for a,b in AB}
    R={(a,b,k):V('rend',a,b,k) for a,b in AB for k in (6,7)}
    P={(a,b,c,3):V('rpath',a,b,c,3) for a,b,c in ABC}
    for a,b,c in ABC:
        C([H[a],H[b],H[c],-color[a,b,c],P[a,b,c,3]],'red3')
        C([H[a],H[b],H[c],color[a,b,c],B3[a,c]],'blue3')
    for k in range(4,8):
        extensions=co.defaultdict(list)
        for (a,t,b,length),v in list(P.items()):
            if length==k-1:
                for c in successors[b]:extensions[a,b,c].append((t,v))
        for (a,b,c),previous in extensions.items():
            flag=V('rpath',a,b,c,k);P[a,b,c,k]=flag
            for t,v in previous:C([H[c],-v,-color[t,b,c],flag],'red_extend')
            if k in (6,7):C([-flag,R[a,c,k]],'red_end')
    for a,b,c in ABC:
        for d in successors[c]:
            cs=[color[t] for t in [(a,b,c),(a,b,d),(a,c,d),(b,c,d)]]
            for mask in range(16):
                if mask not in {0,1,3,7,8,12,14,15}:C([H[a],H[b],H[c],H[d]]+[v*(-1 if mask&(1<<j) else 1) for j,v in enumerate(cs)],'packet')
            C([H[a],H[b],H[c],H[d],cs[0],cs[3],B4[a,d]],'blue4')
    for a,b in AB:
        C([-R[a,b,7],-B3[a,b]],'weak');C([-R[a,b,6],-B4[a,b]],'weak')
    for s in range(84):
        if s in (first,last):continue
        if any(x>1 and y==1 and (x+1,y) not in I[s] and (x,y+1) not in I[s] for x,y in I[s]):C([H[s],B3[first,s]],'in_blue3')
        if any(x<3 and y==6 and (x==1 or (x-1,y) in I[s]) and (x,y-1) in I[s] for x,y in G-I[s]):C([H[s],B3[s,last]],'out_blue3')
    lib=ROOT.parent/'n8_residual_slice_20261119/prefix6-bound-858-h18/prefix6-library.json'
    records,lib_receipt=verify_library(lib);selectors={'front':[],'back':[]}
    for rec in records:
        front=[W.index(tuple(w)) for w in rec['words_in_actual_order']]
        back=[ht.index(tuple(6-t for t in shape[::-1])) for shape in rec['shapes_in_actual_order']]
        for side,seq in [('front',front),('back',back)]:
            flag=V('prefix',side,rec['mask']);selectors[side].append(flag);support=set(seq)
            for s in support:C([-flag,-H[s]],'prefix_support')
            for pair in rec['pair_labels']:
                p,q=pair['start'],pair['end'];r=pair['label']
                a,b=(seq[p],seq[q]) if side=='front' else (seq[q],seq[p]);phase='l' if side=='front' else 'u';g=tuple(r) if side=='front' else (4-r[0],7-r[1])
                if (phase,a,b) in labels:C([-flag,labels[phase,a,b][g]],'prefix_labels')
            for j,(p,q,r) in enumerate(it.combinations(range(6),3)):
                t=(seq[p],seq[q],seq[r]) if side=='front' else (seq[r],seq[q],seq[p])
                if t in color:C([-flag,color[t]*(1 if rec['mask']&(1<<j) else -1)],'prefix_color')
            for s in range(84):
                if s not in support and (any(I[s]<I[t] for t in support) if side=='front' else any(I[t]<I[s] for t in support)):C([-flag,H[s]],'prefix_shadow')
    for side in selectors:C(selectors[side],'prefix_exists')
    assert used==set(ledger),(len(used),len(ledger),set(ledger)-used)
    physical=sum(counts.values());pool=IDPool(start_from=len(ledger)+1)
    for j in range(1,10):
        for c in CardEnc.equals([H[s] for s,w in enumerate(W) if j in w],6,vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'degree')
    for c in CardEnc.equals(H,18,vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'holes')
    c_begin=sum(counts.values())
    for c in CardEnc.atleast([H[s] for s,w in enumerate(W) if 1 in w and 9 in w],2,vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'c_le_5')
    c_end=sum(counts.values())
    rows,rows_receipt=verify_rows(ROOT.parent/'n8_residual_slice_20261119/858-rows.json')
    for row in rows:
        d=len(row['support'])-50 if row['kind']=='slice-(3, 5)' else row['demand']
        for c in CardEnc.atleast([H[s] for s in row['support']],d,vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'rows')
    f.close();total=sum(counts.values());cnf=OUT/'formula.cnf'
    with cnf.open('w') as o,body.open() as source:
        o.write(f'p cnf {pool.top} {total}\n')
        for line in source:o.write(line)
    manifest=json.loads((FIRST/'model/manifest.json').read_text())
    result={'status':'RECONSTRUCTED','variables':pool.top,'clauses':total,'physical_clauses':physical,'counts':dict(counts),'library':lib_receipt,'rows':rows_receipt,'cnf_sha256':digest(cnf),'original_cnf_sha256':digest(FIRST/'model/formula.cnf'),'original_manifest_sha256':manifest['cnf_sha256'],'source_sha256':digest(Path(__file__)),'seconds':time.monotonic()-start}
    save(OUT/'reconstruction.json',result)
    assert result['cnf_sha256']==result['original_cnf_sha256']==result['original_manifest_sha256'],result
    # Preserve original counter IDs; weakening deletes17 c clauses and4 units.
    for label,drop_units in [('without-c',False),('without-c-and-extreme-units',True)]:
        target=OUT/(label+'.cnf');omit=17+(4 if drop_units else 0)
        with target.open('w') as o,body.open() as source:
            o.write(f'p cnf {pool.top} {total-omit}\n')
            for idx,line in enumerate(source):
                if c_begin<=idx<c_end:continue
                if drop_units and line.strip() in {f'-{H[s]} 0' for s in (first,second,penult,last)}:continue
                o.write(line)
    return result

def work():
    result=reconstruct(); checker='<private-linux-workspace>/cadical-sc2025/build/drat-trim';proof=FIRST/'proof.drat'
    result.update(proof_sha256=digest(proof),checks=[])
    for name in ['formula','without-c','without-c-and-extreme-units']:
        cnf=OUT/(name+'.cnf');cmd=[checker,str(cnf),str(proof),'-t','2147483647'];beg=time.monotonic()
        with (OUT/(name+'-checker.log')).open('w') as log:
            process=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            save(OUT/'progress.json',{'status':'CHECKING','name':name,'pid':process.pid,'command':cmd,'deadline':None})
            code=process.wait()
        text=(OUT/(name+'-checker.log')).read_text();markers=sum(line.strip()=='s VERIFIED' for line in text.splitlines())
        result['checks'].append({'name':name,'exit_code':code,'verified_markers':markers,'seconds':time.monotonic()-beg,'cnf_sha256':digest(cnf),'command':cmd})
        save(OUT/'second-result.json',result)
    result['status']='SECOND_DRAT_PASS' if result['checks'][0]['exit_code']==0 and result['checks'][0]['verified_markers']==1 else 'SECOND_DRAT_FAILED'
    save(OUT/'second-result.json',result);save(OUT/'progress.json',result)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='worker':work()
    elif len(sys.argv)>1 and sys.argv[1]=='start':
        log=(ROOT/'independent84-v2-worker.log').open('w');p=subprocess.Popen([sys.executable,'-B',str(Path(__file__)),'worker'],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        print(json.dumps({'pid':p.pid,'pgid':p.pid,'source_sha256':digest(Path(__file__)),'deadline':None}))
    else:
        for name in ['reconstruction.json','progress.json','second-result.json']:
            if (OUT/name).exists():print(name,(OUT/name).read_text())
        print('worker_tail',(ROOT/'independent84-v2-worker.log').read_text()[-3000:])

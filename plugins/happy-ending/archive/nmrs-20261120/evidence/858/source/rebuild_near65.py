"""Independent equation-level replay of trueP65, never imports its builder.

Recompute all semantic domains, exact variable allocation (including numeric
counter/semantic interleaving), both complete finite libraries and every clause.
The first CNF is read only after the new file is complete, for byte-hash binding.
"""
import collections as co
import itertools as it
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
assert platform.system()=='Linux'
from pysat.card import CardEnc,EncType
from pysat.formula import IDPool
import rebuild84_v2 as audit
ROOT=Path(__file__).resolve().parent;FIRST=ROOT/'near65-v1';OUT=ROOT/'near65-independent-v1'
W=audit.W;HT=audit.ht;I=audit.I;G=audit.G;AB=audit.AB;ABC=audit.ABC;SU=audit.successors
IX={tuple(sorted(c)):s for s,c in enumerate(I)}
def reconstruct():
    OUT.mkdir(exist_ok=False);start=time.monotonic();meta=json.loads((FIRST/'model/metadata.json').read_text())
    def freeze(x):return tuple(freeze(a) if isinstance(a,list) else a for a in x)
    meanings={freeze(k):v for k,v in meta['semantic_variables']}
    assert len(meanings)==len(meta['semantic_variables']) and len(set(meanings.values()))==len(meanings)
    assert meta['words']==list(map(list,W)) and meta['heights']==list(map(list,HT))
    pool=IDPool();used=set();counts=co.Counter();body=OUT/'body.cnf';stream=body.open('w')
    def V(*key):
        used.add(key);v=pool.id(key);assert v==meanings[key],(key,v,meanings[key]);return v
    def C(c,kind):stream.write(' '.join(map(str,c))+' 0\n');counts[kind]+=1
    H=[V('h',s) for s in range(84)]
    def O(a,b):return V('order',min(a,b),max(a,b))*(1 if a<b else -1)
    for a,b,c in it.combinations(range(84),3):C([-O(a,b),-O(b,c),O(a,c)],'order');C([O(a,b),O(b,c),-O(a,c)],'order')
    for a,b in AB:C([O(a,b)],'ideal_order')
    L={(a,b):{g:V('l',a,b,*g) for g in sorted(I[b]-I[a])} for a,b in AB}
    for (a,b),ds in L.items():
        C(list(ds.values()),'label')
        for x,y in it.combinations(ds.values(),2):C([-x,-y],'label')
        for g,v in ds.items():
            if g[0]>sum(h>0 for h in HT[a])+1 or g[1]>HT[a][0]+1:C([H[a],H[b],-v],'source_extent')
    color={t:V('color',*t) for t in ABC}
    for a,b,c in ABC:
        for g,x in L[a,b].items():
            for q,y in L[b,c].items():
                if q[0]<=g[0]:C([H[a],H[b],H[c],-x,-y,color[a,b,c]],'growth')
                if q[1]<=g[1]:C([H[a],H[b],H[c],-x,-y,-color[a,b,c]],'growth')
    C([-H[0]],'first_two');C([-H[1]],'first_two')
    for a,b in AB:
        if a==0:C([H[b],L[a,b][1,1]],'first_pair')
        if a==1:
            for g,v in L[a,b].items():
                if g not in ((1,2),(2,1)):C([H[b],-v],'second_pair')
            for sign,g in [(-1,(1,2)),(1,(2,1))]:C([H[b],sign*color[0,a,b]]+([L[a,b][g]] if g in L[a,b] else []),'second_color')
    E={};pairflags=co.defaultdict(list)
    for a,b in it.permutations(range(84),2):
        for g in sorted(I[b]-I[a]):
            if g==(1,1) and a!=0:continue
            if g[0]>sum(h>0 for h in HT[a])+1 or g[1]>HT[a][0]+1:continue
            v=V('corner',a,b,*g);E[a,b,g]=v;pairflags[a,b].append(v)
            C([-v,-H[a]],'real_corner');C([-v,-H[b]],'real_corner');C([-v,O(a,b)],'real_corner')
            if (a,b) in L:C([-v,L[a,b][g]],'same_l_corner')
    for flags in pairflags.values():
        for x,y in it.combinations(flags,2):C([-x,-y],'corner_unique')
    M={};coordinate=co.defaultdict(list)
    for s in range(84):
        for x,y in G:
            g=x,y
            if g in I[s] and (x+1,y) not in I[s] and (x,y+1) not in I[s]:C([H[s]]+[v for (a,b,q),v in E.items() if b==s and q==g],'incoming')
            if g not in I[s] and (x==1 or (x-1,y) in I[s]) and (y==1 or (x,y-1) in I[s]):
                m=V('missing',s,x,y);M[s,g]=m;C([-m,-H[s]],'missing_real');C([H[s],m]+[v for (a,b,q),v in E.items() if a==s and q==g],'out_or_missing')
                t=IX[tuple(sorted(I[s]|{g}))];new=set(W[t])-set(W[s]);assert len(new)==1;coordinate[new.pop()].append(m)
    B3={(a,b):V('b3',a,b) for a,b in AB};B4={(a,b):V('b4',a,b) for a,b in AB};R={(a,b,k):V('rend',a,b,k) for a,b in AB for k in (6,7)}
    P={(a,b,c,3):V('rpath',a,b,c,3) for a,b,c in ABC}
    for a,b,c in ABC:C([H[a],H[b],H[c],-color[a,b,c],P[a,b,c,3]],'red3');C([H[a],H[b],H[c],color[a,b,c],B3[a,c]],'blue3')
    for k in range(4,8):
        extensions=co.defaultdict(list)
        for (a,t,b,length),v in list(P.items()):
            if length==k-1:
                for c in SU[b]:extensions[a,b,c].append((t,v))
        for (a,b,c),previous in extensions.items():
            flag=V('rpath',a,b,c,k);P[a,b,c,k]=flag
            for t,v in previous:C([H[c],-v,-color[t,b,c],flag],'red_extend')
            if k in (6,7):C([-flag,R[a,c,k]],'red_end')
    for a,b,c in ABC:
        for d in SU[c]:
            cs=[color[t] for t in [(a,b,c),(a,b,d),(a,c,d),(b,c,d)]]
            for mask in range(16):
                if mask not in {0,1,3,7,8,12,14,15}:C([H[a],H[b],H[c],H[d]]+[v*(-1 if mask&(1<<j) else 1) for j,v in enumerate(cs)],'packet')
            C([H[a],H[b],H[c],H[d],cs[0],cs[3],B4[a,d]],'blue4')
    for a,b in AB:C([-R[a,b,7],-B3[a,b]],'weak');C([-R[a,b,6],-B4[a,b]],'weak')
    for s in range(1,84):
        if any(x>1 and y==1 and (x+1,y) not in I[s] and (x,y+1) not in I[s] for x,y in I[s]):C([H[s],B3[0,s]],'incoming_blue3')
    records,lib_receipt=audit.verify_library(ROOT.parent/'n8_residual_slice_20261119/prefix6-bound-858-h18/prefix6-library.json');selectors=[]
    for rec in records:
        seq=[W.index(tuple(w)) for w in rec['words_in_actual_order']];flag=V('prefix',rec['mask']);selectors.append(flag)
        for s in set(seq):C([-flag,-H[s]],'prefix_support')
        for pair in rec['pair_labels']:
            a,b=seq[pair['start']],seq[pair['end']]
            if (a,b) in L:C([-flag,L[a,b][tuple(pair['label'])]],'prefix_l')
        for j,(a,b,c) in enumerate(it.combinations(seq,3)):
            if (a,b,c) in color:C([-flag,color[a,b,c]*(1 if rec['mask']&(1<<j) else -1)],'prefix_color')
        for s in range(84):
            if s not in seq and any(I[s]<I[t] for t in seq):C([-flag,H[s]],'prefix_shadow')
    C(selectors,'prefix_exists')
    for c in CardEnc.equals(H,19,vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'nineteen_holes')
    for j in range(1,10):
        for c in CardEnc.atleast([H[s] for s,w in enumerate(W) if j in w]+[-m for m in coordinate[j]],6+len(coordinate[j]),vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'coordinate_missing_charge')
    rows,rows_receipt=audit.verify_rows(ROOT.parent/'n8_residual_slice_20261119/858-rows.json');entry_count=0
    for k,row in enumerate(rows):
        support=set(row['support']);d=len(support)-50 if row['kind']=='slice-(3, 5)' else row['demand'];entries=co.defaultdict(list)
        for (s,g),m in M.items():
            if s not in support and IX[tuple(sorted(I[s]|{g}))] in support:entries[s].append((g,m))
        flags=[]
        for s,gm in entries.items():
            v=V('rowentry',k,s,tuple(g for g,m in gm));flags.append(v);entry_count+=1
            for g,m in gm:C([-m,v],'row_entry')
        for c in CardEnc.atleast([H[s] for s in row['support']]+[-v for v in flags],d+len(flags),vpool=pool,encoding=EncType.seqcounter).clauses:C(c,'row_missing_charge')
    stream.close();assert used==set(meanings),(len(used),len(meanings));cnf=OUT/'formula.cnf';total=sum(counts.values())
    with cnf.open('w') as out,body.open() as source:
        out.write(f'p cnf {pool.top} {total}\n')
        for line in source:out.write(line)
    result={'status':'INDEPENDENT_COMPLETE_RECONSTRUCTION','variables':pool.top,'clauses':total,'semantic_variables':len(used),'counts':dict(counts),'row_entry_groups':entry_count,'library':lib_receipt,'rows':rows_receipt,'cnf_sha256':audit.digest(cnf),'original_cnf_sha256':audit.digest(FIRST/'model/formula.cnf'),'original_source_sha256':audit.digest(ROOT/'near65.py'),'source_sha256':audit.digest(Path(__file__)),'seconds':time.monotonic()-start}
    audit.save(OUT/'reconstruction.json',result)
    assert result['cnf_sha256']==result['original_cnf_sha256']=='f8f5cdead0740948641ea3f025c21a0a37e342eb8ab16968bdf90b022db3ba26'
    return result
def worker():
    result=reconstruct();proof=FIRST/'proof.drat';cnf=OUT/'formula.cnf';result['proof_sha256_before']=audit.digest(proof)
    command=['<private-linux-workspace>/cadical-sc2025/build/drat-trim',str(cnf),str(proof),'-t','2147483647'];start=time.monotonic()
    with (OUT/'second-checker.log').open('w') as log:
        p=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True);result.update(status='SECOND_CHECKING',pid=p.pid,pgid=p.pid,command=command,deadline=None);audit.save(OUT/'second-result.json',result)
        while p.poll() is None:audit.save(OUT/'progress.json',{'status':'SECOND_CHECKING','pid':p.pid,'elapsed':time.monotonic()-start,'deadline':None});time.sleep(5)
        code=p.returncode
    markers=sum(s.strip()=='s VERIFIED' for s in (OUT/'second-checker.log').read_text().splitlines());result.update(checker_exit=code,verified_markers=markers,checker_seconds=time.monotonic()-start,proof_sha256_after=audit.digest(proof),cnf_sha256_after=audit.digest(cnf))
    assert result['proof_sha256_before']==result['proof_sha256_after'] and result['cnf_sha256']==result['cnf_sha256_after']
    result['status']='SECOND_DRAT_PASS' if code==0 and markers==1 else 'SECOND_DRAT_FAILED';audit.save(OUT/'second-result.json',result);audit.save(OUT/'progress.json',result)
if __name__=='__main__':
    case=sys.argv[1] if len(sys.argv)>1 else 'status'
    if case=='worker':worker()
    elif case=='start':
        log=(ROOT/'near65-independent-worker.log').open('w');p=subprocess.Popen([sys.executable,'-B',str(Path(__file__)),'worker'],stdout=log,stderr=subprocess.STDOUT,start_new_session=True);print(json.dumps({'pid':p.pid,'pgid':p.pid,'deadline':None,'source_sha256':audit.digest(Path(__file__))}))
    else:
        for name in ['reconstruction.json','second-result.json','progress.json']:
            if (OUT/name).exists():print(name,(OUT/name).read_text())
        path=ROOT/'near65-independent-worker.log'
        if path.exists():print('worker_tail',path.read_text()[-2500:])

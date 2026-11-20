"""True-P ordinary85865-point necessary model, no frozen u=l assumptions.

All maximal incoming corners have actual l witnesses. Missing minimal outgoing
corners are charged to the introduced word coordinate and to every pure hole
row they can enter. This is one global fixed-l chart, not independently chosen
daughter charts. External AE and DRAT have no deadline.
"""
import collections as co
import hashlib
import heapq
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
ROOT=Path(__file__).resolve().parent
W=list(it.combinations(range(1,10),3));HT=[tuple(w[2-j]-3+j for j in range(3)) for w in W]
I=[{(x,y) for x in range(1,4) for y in range(1,h[x-1]+1)} for h in HT]
IX={tuple(sorted(c)):s for s,c in enumerate(I)};G=set(it.product(range(1,4),range(1,7)))
SU={a:[b for b in range(84) if I[a]<I[b]] for a in range(84)}
PAIRS=[(a,b) for a in range(84) for b in SU[a]];TRIPLES=[(a,b,c) for a,b in PAIRS for c in SU[b]]
def save(p,x):
    t=p.with_suffix('.tmp');t.write_text(json.dumps(x,indent=2));t.replace(p)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

class Calibration:
    def __init__(self):
        path=ROOT/'owner-C-v1/witness.json';r=json.loads(path.read_text());physical=r['occupied']
        renumber={p:i for i,p in enumerate(physical)};self.n=len(physical)
        self.red={tuple(renumber[p] for p in t) for t in r['red_triples']};self.l={}
        for b in range(1,self.n):
            for a in range(b):
                rank=[1,1]
                for p in range(a):
                    c=int((p,a,b) in self.red);rank[c]=max(rank[c],self.l[p,a][c]+1)
                self.l[a,b]=tuple(rank)
        self.owner={}
        for p in range(self.n):
            cells={g for a in range(p) for g in G if all(x<=y for x,y in zip(g,self.l[a,p]))}
            self.owner[IX[tuple(sorted(cells))]]=p
        assert len(self.owner)==self.n
        # Actual chronological constraints plus the full ideal partial order.
        arcs={s:set(SU[s]) for s in range(84)}
        for a,b in it.permutations(self.owner,2):
            if self.owner[a]<self.owner[b]:arcs[a].add(b)
        degrees=co.Counter(b for a in arcs for b in arcs[a]);ready=[s for s in range(84) if not degrees[s]];heapq.heapify(ready);order=[]
        while ready:
            s=heapq.heappop(ready);order.append(s)
            for t in arcs[s]:
                degrees[t]-=1
                if degrees[t]==0:heapq.heappush(ready,t)
        assert len(order)==84;self.order={s:k for k,s in enumerate(order)}
        self.rpath={};self.rend=co.defaultdict(int);self.b3=set();self.b4=set()
        for s in range(self.n):
            for v in range(s+1,self.n):
                self.rpath[s,s,v]=1<<2
                for u in range(s+1,v):
                    bits=0
                    for t in range(s,u):
                        if (t,u,v) in self.red:bits|=self.rpath[s,t,u]<<1
                    self.rpath[s,u,v]=bits;self.rend[s,v]|=bits
                    if (s,u,v) not in self.red:self.b3.add((s,v))
        for a,b,c,d in it.combinations(range(self.n),4):
            if (a,b,c) not in self.red and (b,c,d) not in self.red:self.b4.add((a,d))
        self.mask=sum(1<<j for j,t in enumerate(it.combinations(range(6),3)) if t in self.red)
        self.missing={}
        for s in range(84):
            for g in G-I[s]:
                x,y=g
                if (x==1 or (x-1,y) in I[s]) and (y==1 or (x,y-1) in I[s]):
                    p=self.owner.get(s);self.missing[s,g]=p is not None and not any(self.l[p,q]==g for q in range(p+1,self.n))
        self.source_sha256=sha(path)
    def value(self,key):
        kind,*a=key
        if kind=='h':return a[0] not in self.owner
        if kind=='order':return self.order[a[0]]<self.order[a[1]]
        if kind=='missing':return self.missing[a[0],tuple(a[1:])]
        if kind=='rowentry':return any(self.missing[a[1],g] for g in a[2])
        if kind=='prefix':return a[0]==self.mask
        if kind in ('l','corner'):
            s,t,x,y=a
            if s not in self.owner or t not in self.owner:return kind=='l' and (x,y)==min(I[t]-I[s])
            p,q=self.owner[s],self.owner[t]
            return p<q and self.l[p,q]==(x,y)
        if kind=='color':return all(s in self.owner for s in a) and tuple(self.owner[s] for s in a) in self.red
        if kind in ('b3','b4','rend','rpath'):
            endpoints=a[:3] if kind=='rpath' else a[:2]
            if any(s not in self.owner for s in endpoints):return False
            b=[self.owner[s] for s in endpoints]
            if b!=sorted(b):return False
            if kind in ('b3','b4'):return tuple(b) in getattr(self,kind)
            if kind=='rend':return bool(self.rend[tuple(b)]&(1<<a[-1]))
            return bool(self.rpath[tuple(b)]&(1<<a[-1]))
        raise AssertionError(key)

def build(out,calibrate=False):
    out.mkdir(exist_ok=False);pool=IDPool();ledger=[];counts=co.Counter();checked=co.Counter();truth={};oracle=Calibration() if calibrate else None
    body=out/'body.cnf';f=body.open('w')
    def V(*key):
        fresh=key not in pool.obj2id;v=pool.id(key)
        if fresh:
            ledger.append((key,v))
            if oracle:truth[v]=oracle.value(key)
        return v
    def C(clause,kind,check=True):
        if oracle and check:
            assert any(truth[abs(v)]==(v>0) for v in clause),(kind,clause,[ledger[abs(v)-1] for v in clause]);checked[kind]+=1
        f.write(' '.join(map(str,clause))+' 0\n');counts[kind]+=1
    H=[V('h',s) for s in range(84)]
    def O(a,b):return V('order',min(a,b),max(a,b))*(1 if a<b else -1)
    for a,b,c in it.combinations(range(84),3):C([-O(a,b),-O(b,c),O(a,c)],'order');C([O(a,b),O(b,c),-O(a,c)],'order')
    for a,b in PAIRS:C([O(a,b)],'ideal_order')
    L={(a,b):{g:V('l',a,b,*g) for g in sorted(I[b]-I[a])} for a,b in PAIRS}
    for (a,b),ds in L.items():
        C(list(ds.values()),'label')
        for x,y in it.combinations(ds.values(),2):C([-x,-y],'label')
        for g,v in ds.items():
            if g[0]>sum(h>0 for h in HT[a])+1 or g[1]>HT[a][0]+1:C([H[a],H[b],-v],'true_source_extent')
    color={t:V('color',*t) for t in TRIPLES}
    for a,b,c in TRIPLES:
        for g,x in L[a,b].items():
            for q,y in L[b,c].items():
                if q[0]<=g[0]:C([H[a],H[b],H[c],-x,-y,color[a,b,c]],'growth')
                if q[1]<=g[1]:C([H[a],H[b],H[c],-x,-y,-color[a,b,c]],'growth')
    first,second=0,1;C([-H[first]],'true_first_two');C([-H[second]],'true_first_two')
    for a,b in PAIRS:
        if a==first:C([H[b],L[a,b][1,1]],'true_first_pair')
        if a==second:
            for g,v in L[a,b].items():
                if g not in ((1,2),(2,1)):C([H[b],-v],'true_second_pair')
            for sign,g in [(-1,(1,2)),(1,(2,1))]:C([H[b],sign*color[first,a,b]]+([L[a,b][g]] if g in L[a,b] else []),'true_second_color')
    E={};pairflags=co.defaultdict(list)
    for a,b in it.permutations(range(84),2):
        for g in sorted(I[b]-I[a]):
            if g==(1,1) and a!=first:continue
            if g[0]>sum(h>0 for h in HT[a])+1 or g[1]>HT[a][0]+1:continue
            v=V('corner',a,b,*g);E[a,b,g]=v;pairflags[a,b].append(v)
            C([-v,-H[a]],'real_corner');C([-v,-H[b]],'real_corner');C([-v,O(a,b)],'real_corner')
            if (a,b) in L:C([-v,L[a,b][g]],'same_l_corner')
    for flags in pairflags.values():
        for x,y in it.combinations(flags,2):C([-x,-y],'corner_unique')
    misses={};by_coordinate=co.defaultdict(list)
    for s in range(84):
        for x,y in G:
            g=x,y
            if g in I[s] and (x+1,y) not in I[s] and (x,y+1) not in I[s]:C([H[s]]+[v for (a,b,q),v in E.items() if b==s and q==g],'true_all_in_corners')
            if g not in I[s] and (x==1 or (x-1,y) in I[s]) and (y==1 or (x,y-1) in I[s]):
                m=V('missing',s,x,y);misses[s,g]=m;C([-m,-H[s]],'missing_only_real')
                C([H[s],m]+[v for (a,b,q),v in E.items() if a==s and q==g],'missing_or_true_l_out_corner')
                new=IX[tuple(sorted(I[s]|{g}))];introduced=set(W[new])-set(W[s]);assert len(introduced)==1
                by_coordinate[introduced.pop()].append(m)
    B3={(a,b):V('b3',a,b) for a,b in PAIRS};B4={(a,b):V('b4',a,b) for a,b in PAIRS};R={(a,b,k):V('rend',a,b,k) for a,b in PAIRS for k in (6,7)}
    P={(a,b,c,3):V('rpath',a,b,c,3) for a,b,c in TRIPLES}
    for a,b,c in TRIPLES:C([H[a],H[b],H[c],-color[a,b,c],P[a,b,c,3]],'red3');C([H[a],H[b],H[c],color[a,b,c],B3[a,c]],'blue3')
    for k in range(4,8):
        extension=co.defaultdict(list)
        for (a,t,b,length),v in list(P.items()):
            if length==k-1:
                for c in SU[b]:extension[a,b,c].append((t,v))
        for (a,b,c),previous in extension.items():
            flag=V('rpath',a,b,c,k);P[a,b,c,k]=flag
            for t,v in previous:C([H[c],-v,-color[t,b,c],flag],'red_extend')
            if k in (6,7):C([-flag,R[a,c,k]],'red_end')
    for a,b,c in TRIPLES:
        for d in SU[c]:
            cs=[color[t] for t in [(a,b,c),(a,b,d),(a,c,d),(b,c,d)]]
            for mask in range(16):
                if mask not in {0,1,3,7,8,12,14,15}:C([H[a],H[b],H[c],H[d]]+[v*(-1 if mask&(1<<j) else 1) for j,v in enumerate(cs)],'packet')
            C([H[a],H[b],H[c],H[d],cs[0],cs[3],B4[a,d]],'blue4')
    for a,b in PAIRS:C([-R[a,b,7],-B3[a,b]],'weak');C([-R[a,b,6],-B4[a,b]],'weak')
    for s in range(1,84):
        if any(x>1 and y==1 and (x+1,y) not in I[s] and (x,y+1) not in I[s] for x,y in I[s]):C([H[s],B3[first,s]],'true_in_blue3')
    library=ROOT.parent/'n8_residual_slice_20261119/prefix6-bound-858-h18/prefix6-library.json';records=json.loads(library.read_text())['templates'];selectors=[]
    for r in records:
        seq=[W.index(tuple(w)) for w in r['words_in_actual_order']];flag=V('prefix',r['mask']);selectors.append(flag)
        for s in set(seq):C([-flag,-H[s]],'prefix_support')
        for p in r['pair_labels']:
            a,b=seq[p['start']],seq[p['end']]
            if (a,b) in L:C([-flag,L[a,b][tuple(p['label'])]],'prefix_l')
        for j,(a,b,c) in enumerate(it.combinations(seq,3)):
            if (a,b,c) in color:C([-flag,color[a,b,c]*(1 if r['mask']&(1<<j) else -1)],'prefix_color')
        for s in range(84):
            if s not in seq and any(I[s]<I[t] for t in seq):C([-flag,H[s]],'prefix_shadow')
    C(selectors,'prefix_exists')
    # Fix exactly64 physical points only in the production query.
    def card(lits,bound,kind,check=True,equal=False):
        clauses=(CardEnc.equals if equal else CardEnc.atleast)(lits,bound,vpool=pool,encoding=EncType.seqcounter).clauses
        # Aux values for calibration are not assigned: evaluate source inequality.
        if oracle and check:assert sum(truth[abs(v)]==(v>0) for v in lits)>=bound,(kind,bound)
        for c in clauses:C(c,kind,False)
    card(H,19,'exact19',False,True)
    for j in range(1,10):card([H[s] for s,w in enumerate(W) if j in w]+[-m for m in by_coordinate[j]],6+len(by_coordinate[j]),'coordinate_missing_charge')
    rowsfile=ROOT.parent/'n8_residual_slice_20261119/858-rows.json';rows=json.loads(rowsfile.read_text())['rows'];entry_groups=0
    for k,row in enumerate(rows):
        support=set(row['support']);d=len(support)-50 if row['kind']=='slice-(3, 5)' else row['demand'];entries=co.defaultdict(list)
        for (s,g),m in misses.items():
            if s not in support and IX[tuple(sorted(I[s]|{g}))] in support:entries[s].append((g,m))
        ev=[]
        for s,gs in entries.items():
            e=V('rowentry',k,s,tuple(g for g,m in gs));ev.append(e);entry_groups+=1
            for g,m in gs:C([-m,e],'row_entry_or')
        card([H[s] for s in row['support']]+[-v for v in ev],d+len(ev),'pure_row_missing_charge')
    f.close();cnf=out/'formula.cnf'
    with cnf.open('w') as dest,body.open() as source:
        dest.write(f'p cnf {pool.top} {sum(counts.values())}\n')
        for line in source:dest.write(line)
    save(out/'metadata.json',{'words':W,'heights':HT,'semantic_variables':ledger})
    result={'status':'CALIBRATION_PASS' if oracle else 'PREPARED','variables':pool.top,'clauses':sum(counts.values()),'counts':dict(counts),'checked':dict(checked),'missing_angles':len(misses),'row_entry_point_groups':entry_groups,'cnf_sha256':sha(cnf),'source_sha256':sha(Path(__file__)),'rows_sha256':sha(rowsfile),'library_sha256':sha(library),'calibration_sha256':oracle.source_sha256 if oracle else None,'scope':'trueP only, n65 necessary relaxation, no u=l/no full66 frozen units','deadline':None}
    save(out/'manifest.json',result);print(json.dumps(result),flush=True);return result

def worker():
    out=ROOT/'near65-v1';out.mkdir(exist_ok=False);result=build(out/'model');cnf=out/'model/formula.cnf';proof=out/'proof.drat'
    for phase,cmd in [('SOLVING',['<private-linux-workspace>/AE_kissat2025_MAB/build/kissat',str(cnf),str(proof)]),('CHECKING',['<private-linux-workspace>/cadical-sc2025/build/drat-trim',str(cnf),str(proof),'-t','2147483647'])]:
        if phase=='CHECKING' and result.get('solver_exit')!=20:break
        with (out/(phase.lower()+'.log')).open('w') as log:
            p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,start_new_session=True);start=time.monotonic()
            result.update(status=phase,pid=p.pid,pgid=p.pid,command=cmd);save(out/'result.json',result)
            while p.poll() is None:save(out/'progress.json',dict(status=phase,pid=p.pid,elapsed=time.monotonic()-start,proof_bytes=proof.stat().st_size if proof.exists() else 0,deadline=None));time.sleep(5)
            result['solver_exit' if phase=='SOLVING' else 'checker_exit']=p.returncode
    if result.get('checker_exit')==0:
        text=(out/'checking.log').read_text();result['verified_markers']=sum(s.strip()=='s VERIFIED' for s in text.splitlines());result['status']='CHECKED_UNSAT' if result['verified_markers']==1 else 'CHECK_FAILED'
    else:result['status']='SAT_RELAXATION_NEEDS_ACTUAL_INTERFACE' if result.get('solver_exit')==10 else 'INCOMPLETE'
    if proof.exists():result['proof_sha256']=sha(proof)
    save(out/'result.json',result);save(out/'progress.json',result)

if __name__=='__main__':
    case=sys.argv[1] if len(sys.argv)>1 else 'status'
    if case=='calibrate':build(ROOT/'near65-calibration-v1',True)
    elif case=='worker':worker()
    elif case=='start':
        assert json.loads((ROOT/'near65-calibration-v1/manifest.json').read_text())['status']=='CALIBRATION_PASS'
        log=(ROOT/'near65-worker.log').open('w');p=subprocess.Popen([sys.executable,'-B',str(Path(__file__)),'worker'],stdout=log,stderr=subprocess.STDOUT,start_new_session=True);print(json.dumps({'pid':p.pid,'pgid':p.pid,'deadline':None,'source_sha256':sha(Path(__file__))}))
    else:
        for name in ['model/manifest.json','result.json','progress.json']:
            if (ROOT/'near65-v1'/name).exists():print(name,(ROOT/'near65-v1'/name).read_text())
        log=ROOT/'near65-worker.log'
        if log.exists():print('worker_tail',log.read_text()[-1500:])

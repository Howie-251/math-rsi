"""Joint PSD-ray and Q5-cut column generation with exhaustive row separation."""
from pathlib import Path
import sys,json,time,argparse
import numpy as np
from scipy import sparse
from scipy.optimize._highspy import _core as hs
P=Path(__file__).resolve().parent;BASE=P.parent/'optimization_20261028_q4'
sys.path.insert(0,str(BASE))
from model import Model
ap=argparse.ArgumentParser();ap.add_argument('--rounds',type=int,default=80);ap.add_argument('--prefix',default='column_lift');ap.add_argument('--no-q5',action='store_true');args=ap.parse_args()
M=Model();nv=M.nv;H=np.ones((5,5));rng=np.random.default_rng(20261029)
for i in range(5):H[i,(i+1)%5]=H[(i+1)%5,i]=-1
f=M.fb[0];V=[];tags=[]
def add_psd(b,v):
    ray=M.ray(b,v);V.append(ray);tags.append(None);return ray
def horn(labels):
    Q=H[np.ix_(labels,labels)];v=np.zeros(nv)
    v[M.oldnv:M.oldnv+M.fs[1]]=np.bincount(f['orbit'],weights=Q[f['ii'],f['jj']],minlength=len(f['counts']))/f['counts']
    return v
initial=np.load(BASE/'q5control_best.npz');x0=initial['x']
for b in range(6,12):
    q=M.matrix(x0,b);tr=float(np.trace(q));v=np.zeros(nv)
    if b<11:v[M.oldnv+M.fs[b-6]:M.oldnv+M.fs[b-5]]=x0[M.oldnv+M.fs[b-6]:M.oldnv+M.fs[b-5]]/tr
    else:v[-45:]=x0[-45:]/tr
    V.append(v);tags.append(None)
    w,U=np.linalg.eigh(q)
    for j in np.where(w>1e-6)[0][-5:]:add_psd(b,U[:,j])
seen=set()
for rec in ([] if args.no_q5 else json.loads((P/'selected_cuts.json').read_text())):
    labels=np.array(rec['labels']);v=horn(labels);seen.add(v.tobytes());V.append(v);tags.append(labels)
base=M.evaluate(x0);best=float(base.max())
np.savez(P/(args.prefix+'_best.npz'),x=x0,x_psd=x0,weights=np.zeros(0),labels=np.zeros((0,240),dtype=int),upper=best)
active=np.unique(np.r_[np.argsort(base)[-3000:],rng.choice(M.N,500,replace=False)])
isin=np.zeros(M.N,bool);isin[active]=True;A=M.amat(active)
AA=sparse.csc_matrix(np.c_[-np.ones(len(active)),A@np.column_stack(V)])
lp=hs.HighsLp();lp.num_col_=AA.shape[1];lp.num_row_=len(active)
lp.col_cost_=np.r_[1.,np.zeros(len(V))];lp.col_lower_=np.zeros(len(V)+1);lp.col_upper_=np.full(len(V)+1,np.inf);lp.col_upper_[0]=1
lp.row_lower_=np.full(len(active),-np.inf);lp.row_upper_=-M.dd[active]
lp.a_matrix_.format_=hs.MatrixFormat.kColwise;lp.a_matrix_.start_=AA.indptr.astype(np.int32);lp.a_matrix_.index_=AA.indices.astype(np.int32);lp.a_matrix_.value_=AA.data
h=hs._Highs();h.setOptionValue('output_flag',False);h.setOptionValue('solver','simplex');h.setOptionValue('threads',1);h.setOptionValue('simplex_strategy',1)
h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9);h.passModel(lp)
hist=[];start=time.time()
for iteration in range(args.rounds):
    h.run();assert h.getModelStatus()==hs.HighsModelStatus.kOptimal
    sol=h.getSolution();values=np.array(sol.col_value);weights=np.maximum(values[1:],0);nr=len(V)
    VV=np.column_stack(V);x=VV@weights;scores=M.evaluate(x);upper=float(scores.max());obj=float(values[0])
    iscut=np.array([t is not None for t in tags]);xpsd=VV[:,~iscut]@weights[~iscut]
    if upper<best:
        best=upper;np.savez(P/(args.prefix+'_best.npz'),x=x,x_psd=xpsd,weights=weights[iscut],
                            labels=np.array([t for t in tags if t is not None]),upper=best,iteration=iteration)
    p=-np.array(sol.row_dual);moment=A.T@p;new=[];mineig=0
    for b in range(6,12):
        w,U=np.linalg.eigh(M.moment(moment,b));mineig=min(mineig,float(w[0]))
        for j in np.where(w < -1e-8)[0][:4]:new.append(add_psd(b,U[:,j]))
    W=M.moment(moment,6);bestcut=0.;addedcuts=0
    for trial in range(0 if args.no_q5 else 30):
        labels=rng.integers(0,5,len(W));Z=W@np.eye(5)[labels]
        for sweep in range(15):
            changed=0
            for i in rng.permutation(len(W)):
                old=labels[i];costs=(Z[i]-W[i,i]*np.eye(5)[old])@H;newlabel=int(np.argmin(costs))
                if costs[newlabel]<costs[old]-1e-15:
                    labels[i]=newlabel;Z[:,old]-=W[:,i];Z[:,newlabel]+=W[:,i];changed+=1
            if not changed:break
        cost=float(np.sum(W*H[np.ix_(labels,labels)]));bestcut=min(bestcut,cost)
        if cost < -1e-8 and len(set(labels))==5:
            ray=horn(labels);key=ray.tobytes()
            if key not in seen:
                seen.add(key);new.append(ray);V.append(ray);tags.append(labels.copy());addedcuts+=1
                if addedcuts==3:break
    extra=np.where((scores>obj+2e-8)&~isin)[0]
    if len(extra)>300:extra=extra[np.argsort(scores[extra])[-300:]]
    rec=dict(iteration=iteration,full_upper=upper,best_upper=best,restricted_objective=obj,
             active_cuts=int(np.sum(iscut&(weights>1e-10))),cut_weight_sum=float(weights[iscut].sum()),
             columns=nr,rows=len(active),new_cuts=addedcuts,priced_cut_min=bestcut,
             moment_min_eig=mineig,seconds=time.time()-start)
    hist.append(rec);(P/(args.prefix+'_history.json')).write_text(json.dumps(hist,indent=2),encoding='utf-8')
    print(json.dumps(rec),flush=True)
    drop=np.where((weights<1e-11)&(np.arange(nr)<max(0,nr-48)))[0]
    if len(drop):
        h.deleteCols(len(drop),(1+drop).astype(np.int32));ds=set(drop.tolist());keep=[j for j in range(len(V)) if j not in ds]
        V=[V[j] for j in keep];tags=[tags[j] for j in keep]
    if new:
        B=sparse.csc_matrix(A@np.column_stack(new));k=len(new)
        h.addCols(k,np.zeros(k),np.zeros(k),np.full(k,np.inf),B.nnz,B.indptr.astype(np.int32),B.indices.astype(np.int32),B.data)
    if len(extra):
        B=M.amat(extra);AA=sparse.csr_matrix(np.c_[-np.ones(len(extra)),B@np.column_stack(V)])
        h.addRows(len(extra),np.full(len(extra),-np.inf),-M.dd[extra],AA.nnz,AA.indptr.astype(np.int32),AA.indices.astype(np.int32),AA.data)
        A=sparse.vstack([A,B],format='csr');active=np.r_[active,extra];isin[extra]=True

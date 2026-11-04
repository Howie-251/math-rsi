"""Small SDP by exact separation of PSD cones + HiGHS LP outer approximation.
Final upper certificates are formed as rational Gram matrices, not by trusting LP residuals.
"""
import numpy as np
from scipy.optimize import linprog
from scipy import sparse
import time,json

def pairs(n): return [(i,j) for i in range(n) for j in range(i,n)]
def unpack(x,n):
    Q=np.zeros((n,n))
    for v,(i,j) in zip(x,pairs(n)): Q[i,j]=Q[j,i]=v
    return Q

def vec(Q): return np.array([Q[i,j] for i,j in pairs(len(Q))])
def coeff(Q):return np.array([Q[i,j]*(1 if i==j else 2) for i,j in pairs(len(Q))])

def solve_sdp(A,d,dims,neq=0,maxiter=250,tol=1e-8,bound=10.,prefix=None,initial=None):
    # A has linear coefficients for upper triangular Q entries followed by unconstrained equality multipliers.
    A=sparse.csr_matrix(A); d=np.asarray(d); n=A.shape[1]
    starts=np.cumsum([0]+[k*(k+1)//2 for k in dims])
    assert starts[-1]+neq==n
    objective=np.r_[np.zeros(n),1.]
    con=sparse.hstack([A,-np.ones((len(d),1))],format='csr')
    cuts=[];cutrhs=[]
    # simple diagonal nonnegativity and random quadratic cuts
    for b,k in enumerate(dims):
        for i in range(k):
            z=np.zeros(n+1);v=np.zeros(k);v[i]=1
            z[starts[b]:starts[b+1]]=-coeff(np.outer(v,v));cuts.append(z)
        for i in range(k):
            for j in range(i+1,k):
                for sign in [-1,1]:
                    v=np.zeros(k);v[i]=1;v[j]=sign
                    z=np.zeros(n+1);z[starts[b]:starts[b+1]]=-coeff(np.outer(v,v));cuts.append(z)
    bounds=[(-bound,bound)]*n+[(0.,1.)]
    active=np.arange(len(d))
    # Cutting plane on state inequalities too, to avoid huge dense LPs.
    if len(d)>2000:
        rng=np.random.default_rng(104729)
        active=np.unique(np.r_[np.argsort(d)[-300:],rng.choice(len(d),min(1000,len(d)),replace=False)])
    best=1.;bestx=None;hist=[];st=time.time()
    for it in range(maxiter):
        CC=sparse.vstack([con[active],sparse.csr_matrix(np.array(cuts))],format='csr')
        rhs=np.r_[-d[active],np.zeros(len(cuts))]
        res=linprog(objective,A_ub=CC,b_ub=rhs,bounds=bounds,method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        if not res.success: raise RuntimeError(res.message)
        x=res.x[:-1]; lower=res.x[-1]
        xp=x.copy();mineig=0
        newcuts=[]
        for b,k in enumerate(dims):
            Q=unpack(x[starts[b]:starts[b+1]],k)
            w,U=np.linalg.eigh(Q);mineig=min(mineig,float(w[0]))
            xp[starts[b]:starts[b+1]]=vec((U*np.maximum(w,0))@U.T)
            for h in np.where(w< -1e-10)[0]:
                z=np.zeros(n+1);z[starts[b]:starts[b+1]]=-coeff(np.outer(U[:,h],U[:,h]));newcuts.append(z)
        vals=d+A@xp;upper=float(np.max(vals))
        if upper<best:best=upper;bestx=xp.copy()
        rawvals=d+A@x
        viol=np.where(rawvals>lower+tol/4)[0]
        if len(viol)>500:viol=viol[np.argsort(rawvals[viol])[-500:]]
        active=np.union1d(active,viol)
        cuts.extend(newcuts)
        hist.append((it,lower,best,mineig,len(active),len(cuts),time.time()-st))
        if it%10==0 or best-lower<tol:
            print('iter %d lower %.12f upper %.12f eig %.3g states %d cuts %d seconds %.2f'%hist[-1],flush=True)
        if prefix:
            np.savez(prefix+'_latest.npz',x=bestx,lower=lower,upper=best,dims=dims,hist=np.array(hist))
        if best-lower<tol:break
    return bestx,lower,best,hist

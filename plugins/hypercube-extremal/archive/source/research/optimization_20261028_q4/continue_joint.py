"""Continue all six PSD blocks; certify separately with verify.py.

Every saved best passes a floating scan of all 3,312,331 rows.
No restricted objective or optimizer success flag is called an upper certificate.
"""
import argparse, json, time
import numpy as np
from scipy.optimize import minimize
from model import Model, P
from sdp_core import vec

ap = argparse.ArgumentParser()
ap.add_argument('--input', default='certification_snapshot.npz')
ap.add_argument('--prefix', default='joint28')
ap.add_argument('--cycles', type=int, default=12)
ap.add_argument('--iterations', type=int, default=500)
ap.add_argument('--tau', type=float, default=2e-6)
args = ap.parse_args()
M = Model()
od = M.oldnv
dims = M.dims[6:]
bs = np.cumsum(np.r_[0, np.array(dims)**2])
x = np.load(P / args.input)['x'].copy()
assert np.max(np.abs(x[:od])) == 0
values = M.evaluate(x)
best = float(values.max())
active = np.unique(np.r_[np.load(P/'refine_latest.npz')['active'],
                         np.argsort(values)[-3500:]])
isin = np.zeros(M.N, bool)
isin[active] = True
history = []
start = time.time()
np.savez(P/(args.prefix+'_best.npz'), x=x, upper=best)

def factors(x):
    result = []
    for j in range(6):
        w, U = np.linalg.eigh(M.matrix(x, j+6))
        result.append(U * np.sqrt(np.maximum(w, 1e-12)))
    return np.concatenate([L.ravel() for L in result])

def decode(y):
    out = np.zeros(M.nv)
    ls = []
    for j, n in enumerate(dims):
        L = y[bs[j]:bs[j+1]].reshape(n, n)
        ls.append(L)
        Q = L @ L.T
        if j < 5:
            f = M.fb[j]
            out[od+M.fs[j]:od+M.fs[j+1]] = np.bincount(
                f['orbit'], weights=Q[f['ii'],f['jj']],
                minlength=len(f['counts'])) / f['counts']
        else:
            out[-45:] = vec(Q)
    return out, ls

for cycle in range(args.cycles):
    A = M.amat(active)
    density = M.dd[active]
    tau = args.tau
    calls = 0
    def fun(y):
        global calls
        out, ls = decode(y)
        scores = density + A @ out
        peak = scores.max()
        probs = np.exp((scores-peak)/tau)
        total = probs.sum()
        probs /= total
        moment = A.T @ probs
        gradient = np.concatenate([(2*M.moment(moment,j+6)@L).ravel()
                                   for j,L in enumerate(ls)])
        calls += 1
        return peak + tau*np.log(total), gradient
    result = minimize(fun, factors(x), method='L-BFGS-B', jac=True,
                      options=dict(maxiter=args.iterations, ftol=1e-15,
                                   gtol=1e-10, maxcor=25, maxls=40))
    x, _ = decode(result.x)
    values = M.evaluate(x)
    upper = float(values.max())
    restricted = float(values[active].max())
    if upper < best:
        best = upper
        np.savez(P/(args.prefix+'_best.npz'),x=x,upper=best,cycle=cycle)
    add = np.where((values > restricted-3*tau) & ~isin)[0]
    if len(add)>1000:
        add = add[np.argsort(values[add])[-1000:]]
    active = np.r_[active, add]
    isin[add] = True
    record = dict(cycle=cycle, tau=tau, full_upper=upper,
                  best_upper=best, restricted_max=restricted,
                  rows=len(active), added=len(add), calls=calls,
                  optimizer_status=int(result.status),
                  optimizer_message=str(result.message),
                  seconds=time.time()-start)
    history.append(record)
    (P/(args.prefix+'_history.json')).write_text(json.dumps(history,indent=2),encoding='utf-8')
    np.savez(P/(args.prefix+'_latest.npz'),x=x,upper=upper,active=active)
    print(json.dumps(record), flush=True)

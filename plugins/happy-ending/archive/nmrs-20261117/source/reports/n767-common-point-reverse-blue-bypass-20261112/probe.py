"""Fresh finite local signotope probes, Linux only; no production encoding imports."""
from itertools import combinations, permutations
from pathlib import Path
import hashlib, json, os, platform, signal, socket, subprocess, sys, time
ROOT = Path(__file__).resolve().parent
SOLVER='/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat'
CHECKER='/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim'

def write(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def controlled(cmd,prefix,limit):
    start=time.monotonic(); killed=False
    with Path(str(prefix)+'.stdout').open('w') as out, Path(str(prefix)+'.stderr').open('w') as err:
        p=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=True)
        try: p.wait(timeout=limit)
        except subprocess.TimeoutExpired:
            killed=True; os.killpg(p.pid,signal.SIGTERM)
            try: p.wait(timeout=3)
            except subprocess.TimeoutExpired: os.killpg(p.pid,signal.SIGKILL); p.wait()
    return dict(command=cmd,exit_code=p.returncode,timeout_killed=killed,seconds=time.monotonic()-start,
                stdout=Path(str(prefix)+'.stdout').read_text(),stderr=Path(str(prefix)+'.stderr').read_text())

def build(n,roles,x,strict):
    vv=tuple(range(n)); triples=tuple(combinations(vv,3)); color={t:i+1 for i,t in enumerate(triples)}
    clauses=set(); nextvar=len(triples)
    def add(clause):
        c=set(clause)
        if not any(-v in c for v in c): clauses.add(tuple(sorted(c)))
    def terms(path): return [color[path[i:i+3]] for i in range(len(path)-2)]
    def exists(paths,red):
        nonlocal nextvar
        selectors=[]
        for path in paths:
            nextvar+=1; s=nextvar; selectors.append(s)
            for v in terms(path): add([-s,v if red else -v])
        add(selectors)
    for packet in combinations(vv,4):
        ids=[color[t] for t in combinations(packet,3)]
        for mask in range(16):
            bits=[(mask>>i)&1 for i in range(4)]
            if sum(a!=b for a,b in zip(bits,bits[1:]))>1: add([-v if b else v for v,b in zip(ids,bits)])
    for p in combinations(vv,7): add([-v for v in terms(p)])
    for p in combinations(vv,6): add(terms(p))
    # All actual same-endpoint opposite paths, including overlapping interiors.
    # Splits R2+B7,R3+B6,R7+B2 already excluded by the cap clauses.
    for a,b in combinations(vv,2):
        middle=tuple(range(a+1,b))
        for nr in (2,3,4):
            nb=5-nr
            for ri in combinations(middle,nr):
                r=(a,)+ri+(b,)
                for bi in combinations(middle,nb):
                    blue=(a,)+bi+(b,)
                    add([-v for v in terms(r)]+terms(blue))
    p1,p2,q1,q2=roles
    diagonal={(p1,q1),(p2,q2)}; forward=(p1,q2); allowed=diagonal|{forward}
    candidates={edge:[] for edge in allowed}
    for p in combinations(vv,6):
        edge=(p[0],p[-1])
        if (strict and edge not in allowed) or (edge in diagonal and x not in p[1:-1]):
            add([-v for v in terms(p)])
        if edge in diagonal and x in p[1:-1]: candidates[edge].append(p)
        if edge==forward and x not in p: candidates[edge].append(p)
    for edge in allowed: exists(candidates[edge],True)
    exists([p for p in combinations(vv,5) if (p[0],p[-1])==(p2,q1)],False)
    text='p cnf %d %d\n'%(nextvar,len(clauses))+''.join(' '.join(map(str,c))+' 0\n' for c in sorted(clauses))
    return text,dict(n=n,roles=roles,x=x,strict=strict,variables=nextvar,clauses=len(clauses),color_variables=len(triples))

def inspect(n,roles,x,strict,model):
    vv=tuple(range(n)); triples=tuple(combinations(vv,3)); color={t: ('R' if i+1 in model else 'B') for i,t in enumerate(triples)}
    paths={c:[] for c in 'RB'}
    for k in range(2,n+1):
        for p in combinations(vv,k):
            for c in paths:
                if all(color[p[i:i+3]]==c for i in range(k-2)): paths[c].append(p)
    packets=[dict(vertices=p,colors=''.join(color[t] for t in combinations(p,3))) for p in combinations(vv,4)]
    maxima=[]; weak=[]
    for edge in combinations(vv,2):
        pp={c:[p for p in paths[c] if (p[0],p[-1])==edge] for c in paths}
        maxima.append(dict(endpoints=edge,R=max(map(len,pp['R'])),B=max(map(len,pp['B']))))
        weak.extend(dict(R=r,B=b) for r in pp['R'] for b in pp['B'] if len(r)+len(b)==9)
    p1,p2,q1,q2=roles; diag={(p1,q1),(p2,q2)}; allowed=diag|{(p1,q2)}
    red6=[p for p in paths['R'] if len(p)==6]; edges=sorted(set((p[0],p[-1]) for p in red6))
    after=[p for p in red6 if x not in p]; afteredges=sorted(set((p[0],p[-1]) for p in after))
    def matching(edges):
        best=[]
        for k in range(1,len(edges)+1):
            good=[e for e in combinations(edges,k) if len(set(a for a,b in e))==k and len(set(b for a,b in e))==k]
            if not good: break
            best=good[0]
        return dict(size=len(best),example=best)
    checks=dict(packet_valid=all(sum(a!=b for a,b in zip(p['colors'],p['colors'][1:]))<=1 for p in packets),
      no_R7=max(map(len,paths['R']))<7,no_B6=max(map(len,paths['B']))<6,no_weak7=not weak,
      diagonal_existence=diag<=set(edges),all_diagonal_R6_contain_x=all(x in p[1:-1] for p in red6 if (p[0],p[-1]) in diag),
      forward_bypass=any((p[0],p[-1])==(p1,q2) for p in after),reverse_B5=any(len(p)==5 and (p[0],p[-1])==(p2,q1) for p in paths['B']),
      strict_endpoint_restriction=(not strict or set(edges)<=allowed))
    return dict(checks=checks,all_checks_pass=all(checks.values()),colors=[dict(vertices=t,color=color[t]) for t in triples],
        packets=packets,all_paths=paths,same_endpoint_maxima=maxima,weak7=weak,R6=red6,R6_endpoint_edges=edges,
        after_delete_x_R6=after,after_delete_x_edges=afteredges,matching_before=matching(edges),matching_after=matching(afteredges),
        selected_diagonals=[next(p for p in red6 if (p[0],p[-1])==e) for e in sorted(diag)],
        selected_forward_bypass=next((p for p in after if (p[0],p[-1])==(p1,q2)),None),
        selected_reverse_B5=next((p for p in paths['B'] if len(p)==5 and (p[0],p[-1])==(p2,q1)),None))

def run(index,spec,seconds):
    n,roles,x,strict=spec; directory=ROOT/('case-%03d'%index); directory.mkdir()
    text,meta=build(*spec); cnf=directory/'formula.cnf'; cnf.write_text(text)
    write(directory/'spec.json',meta); proof=directory/'proof.drat'
    result=dict(spec=meta,cnf_sha256=sha(cnf),source_sha256=sha(__file__),proof_checked=False)
    sol=controlled([SOLVER,'--no-binary','--time='+str(seconds),str(cnf),str(proof)],directory/'solve',seconds+8)
    result['solve']=sol; result['status']='SAT' if '\ns SATISFIABLE\n' in sol['stdout'] else 'RAW_UNSAT' if '\ns UNSATISFIABLE\n' in sol['stdout'] else 'UNKNOWN'
    if result['status']=='SAT':
        model={int(v) for line in sol['stdout'].splitlines() if line.startswith('v ') for v in line[2:].split() if int(v)}
        result['model_satisfies_actual_dimacs']=all(any(int(v) in model for v in line.split()[:-1]) for line in text.splitlines()[1:])
        result['witness']=inspect(n,roles,x,strict,model); write(directory/'witness.json',result['witness'])
        result['status']='SAT_WITNESS_VERIFIED' if result['model_satisfies_actual_dimacs'] and result['witness']['all_checks_pass'] else 'SAT_CHECK_FAILED'
    elif result['status']=='RAW_UNSAT':
        check=controlled([CHECKER,str(cnf),str(proof),'-t','90'],directory/'check',98)
        result['check']=check; result['proof_sha256']=sha(proof)
        result['proof_checked']=check['exit_code']==0 and '\ns VERIFIED\n' in check['stdout'] and result['cnf_sha256']==sha(cnf)
        if result['proof_checked']: result['status']='CHECKED_UNSAT'
    write(directory/'result.json',result)
    return result

def main():
    # Each pair of sources precedes each terminal; each diagonal contains x.
    # First small family: four relative endpoint orders, several wing placements,
    # central and off-centre common points, strict and unrestricted endpoint sets.
    specs=[]
    for n,left,right in [(13,(0,1),(11,12)),(13,(1,2),(10,11)),(14,(0,2),(11,13)),(15,(1,3),(11,13)),(16,(1,3),(12,14))]:
        for strict in (True,False):
            for ps in permutations(left):
                for qs in permutations(right):
                    for x in sorted(set(((max(left)+min(right))//2,max(left)+2,min(right)-2))):
                        specs.append((n,ps+qs,x,strict))
    write(ROOT/'plan.json',dict(specs=specs,per_case_seconds=20,scope='Finite specified orders only; not all abstract signotopes or 75 points.'))
    results=[]; start=time.monotonic()
    for index,spec in enumerate(specs):
        write(ROOT/'progress.json',dict(current=index,spec=spec,completed=len(results),elapsed=time.monotonic()-start,statuses=[r['status'] for r in results]))
        result=run(index,spec,20); results.append(result)
        write(ROOT/'summary.json',dict(host=socket.gethostname(),platform=platform.platform(),python=sys.executable,
          source_sha256=sha(__file__),completed=len(results),planned=len(specs),cases=[dict(index=i,spec=r['spec'],status=r['status'],proof_checked=r['proof_checked']) for i,r in enumerate(results)]))
        if result['status'].startswith('SAT'): break
        if time.monotonic()-start>900: break
    write(ROOT/'done.json',dict(completed=len(results),planned=len(specs),elapsed=time.monotonic()-start))
if __name__=='__main__': main()

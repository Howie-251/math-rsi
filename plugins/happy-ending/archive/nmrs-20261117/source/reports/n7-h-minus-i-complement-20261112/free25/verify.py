from itertools import combinations
from pathlib import Path
import argparse,hashlib,json,platform,time
ROOT=Path(__file__).resolve().parent
POINTS=tuple(range(1,26))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read():
    lines=(ROOT/'formula.cnf').read_text().splitlines();nv,nc=map(int,lines[0].split()[2:])
    rows=[list(map(int,line.split()))[:-1] for line in lines[1:]]
    assert len(rows)==nc and all(all(0<abs(x)<=nv for x in row) for row in rows)
    return nv,rows
def schema():
    nv,rows=read()
    receipt=dict(passed=True,check='DIMACS structural audit only, not an independent clause-set reconstruction',variables=nv,clauses=len(rows),cnf_sha256=sha(ROOT/'formula.cnf'))
    (ROOT/'schema-audit.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
def physical_dp(colors, red):
    # Every state stores ALL exact achievable lengths and one actual witness
    # per length. Last-coordinate order makes the recurrence acyclic.
    reach = {(s, s, t): {2: (s, t)} for s, t in combinations(POINTS, 2)}
    for last in POINTS:
        states = [(key, table) for key, table in reach.items() if key[2] == last]
        for (first, previous, _), table in states:
            for new in POINTS[last:]:
                if colors[previous, last, new] == red:
                    target = reach.setdefault((first, last, new), {})
                    for length, path in table.items():
                        target.setdefault(length + 1, path + (new,))
    endpoints = {}
    for (first, _, last), table in reach.items():
        target = endpoints.setdefault((first, last), {})
        for length, path in table.items():
            target.setdefault(length, path)
    return endpoints, len(reach)



def sat():
    begin=time.monotonic();nv,rows=read();model=set()
    for line in (ROOT/'solve.stdout').read_text().splitlines():
        if line.startswith('v '):model.update(int(x) for x in line[2:].split() if int(x))
    assert all((x in model)!=(-x in model) for x in range(1,nv+1))
    assert all(any(x in model for x in row) for row in rows)
    triples=tuple(combinations(POINTS,3));colors={q:j+1 in model for j,q in enumerate(triples)}
    dynamic={}
    for red in (False,True):dynamic[red],unused=physical_dp(colors,red)
    roles={}
    for name,red,k in [('R6',True,6),('B5',False,5)]:
        roles[name+'_out']={s for (s,t),tab in dynamic[red].items() if k in tab}
        roles[name+'_in']={t for (s,t),tab in dynamic[red].items() if k in tab}
    H=roles['B5_out']&roles['B5_in'];active=set.union(*roles.values());I=set(POINTS)-active
    weak=[(edge,r,b) for edge in dynamic[True] for r in dynamic[True][edge] for b in dynamic[False][edge] if r+b>=9]
    maxR=max(k for tab in dynamic[True].values() for k in tab);maxB=max(k for tab in dynamic[False].values() for k in tab)
    checks=dict(literal_assignment=True,packets=all(sum(a!=b for a,b in zip(bits,bits[1:]))<=1
       for packet in combinations(POINTS,4) for bits in [[colors[q] for q in combinations(packet,3)]]),
       no_R7=maxR<=6,no_B6=maxB<=5,no_weak7=not weak,h_minus_i_at_least_11=len(H)-len(I)>=11)
    spec=json.loads((ROOT/'spec.json').read_text())
    checks['all_four_role_flags_exact']=all((int(var) in model)==(int(x) in roles[name]) for name,table in spec['exact_roles'].items() for x,var in table.items())
    checks['H_flags_exact']=all((int(var) in model)==(int(x) in H) for x,var in spec['H_flags'].items())
    checks['active_flags_exact']=all((int(var) in model)==(int(x) in active) for x,var in spec['active_flags'].items())
    assert all(checks.values()),checks
    with (ROOT/'colors.tsv').open('w') as f:
        f.write('a\tb\tc\tcolor\n')
        for q in triples:f.write('\t'.join(map(str,q))+('\tR\n' if colors[q] else '\tB\n'))
    anchors={x:dict(incoming=next(tab[5] for (s,t),tab in dynamic[False].items() if t==x and 5 in tab),
                   outgoing=next(tab[5] for (s,t),tab in dynamic[False].items() if s==x and 5 in tab)) for x in H}
    data=dict(n=25,h=len(H),i=len(I),h_minus_i=len(H)-len(I),H=sorted(H),I=sorted(I),roles={k:sorted(v) for k,v in roles.items()},H_anchors=anchors,
       endpoints=[dict(pair=e,R=sorted(dynamic[True][e]),B=sorted(dynamic[False][e]),R_witnesses=dynamic[True][e],B_witnesses=dynamic[False][e]) for e in dynamic[True]])
    (ROOT/'physical-witness.json').write_text(json.dumps(data,indent=2)+'\n')
    receipt=dict(passed=True,checks=checks,n=25,h=len(H),i=len(I),h_minus_i=len(H)-len(I),max_R=maxR,max_B=maxB,seconds=time.monotonic()-begin,
      bindings={p.name:sha(p) for p in (ROOT/'formula.cnf',ROOT/'solve.stdout',ROOT/'colors.tsv',ROOT/'physical-witness.json',Path(__file__))})
    (ROOT/'independent-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
if __name__=='__main__':
    assert platform.system()=='Linux';p=argparse.ArgumentParser();p.add_argument('--schema',action='store_true');p.add_argument('--sat',action='store_true');a=p.parse_args()
    assert a.schema!=a.sat
    schema() if a.schema else sat()

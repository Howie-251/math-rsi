"""Independent actual blue-through model audit; no builder imports."""
from itertools import combinations, product
from pathlib import Path
import argparse, hashlib, json, platform, time
ROOT=Path(__file__).resolve().parent
POINTS=tuple(range(1,22))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read_cnf():
    lines=(ROOT/'formula.cnf').read_text().splitlines()
    nv,nc=map(int,lines[0].split()[2:])
    rows=[tuple(sorted(set(map(int,line.split()[:-1])))) for line in lines[1:]]
    assert len(rows)==nc==len(set(rows))
    assert all(all(0<abs(v)<=nv for v in row) for row in rows)
    return nv,set(rows)
def schema_audit():
    triples=tuple(combinations(POINTS,3)); var={t:i+1 for i,t in enumerate(triples)}
    pairs=tuple(combinations(POINTS,2)); nv=len(triples)
    flags={}
    for k in (4,5,6):
        for edge in pairs: nv+=1; flags[k,edge]=nv
    expected=set()
    def add(xs): expected.add(tuple(sorted(set(xs))))
    def terms(p):return tuple(var[p[i:i+3]] for i in range(len(p)-2))
    for q in combinations(POINTS,4):
        ids=[var[t] for t in combinations(q,3)]
        for bits in product((0,1),repeat=4):
            if sum(a!=b for a,b in zip(bits,bits[1:]))>1:
                add([-x if bit else x for x,bit in zip(ids,bits)])
    for p in combinations(POINTS,7):add([-x for x in terms(p)])
    for p in combinations(POINTS,6):add(terms(p))
    for k in (4,5,6):
        for p in combinations(POINTS,k):add(tuple(-x for x in terms(p))+(flags[k,(p[0],p[-1])],))
        for p in combinations(POINTS,9-k):add((-flags[k,(p[0],p[-1])],)+terms(p))
    blue={}
    for p in combinations(POINTS,5):
        nv+=1;blue[p]=nv
        for x in terms(p):add((-nv,-x))
        add((nv,)+terms(p))
    tables=[]
    for unused in range(3):
        table={}
        for x in POINTS:nv+=1;table[x]=nv
        tables.append(table)
    src,end,K=tables
    for p,s in blue.items():add((-s,src[p[0]]));add((-s,end[p[-1]]))
    for x in POINTS:
        add([-src[x]]+[s for p,s in blue.items() if p[0]==x])
        add([-end[x]]+[s for p,s in blue.items() if p[-1]==x])
        add((-K[x],src[x]));add((-K[x],end[x]));add((K[x],-src[x],-end[x]))
    buckets={}
    families=((3,True),(4,True),(4,False),(5,False))
    for length,red in families:
        for p in combinations(POINTS,length):
            nv+=1
            buckets.setdefault((length,red,(p[0],p[-1])),[]).append(nv)
            for x in terms(p):add((-nv,x if red else -x))
            for x in p:add((-nv,K[x]))
    endpoint={}
    for length,red in families:
        for edge in pairs:
            nv+=1;endpoint[length,red,edge]=nv
            add([-nv]+buckets.get((length,red,edge),[]))
    choices=[]
    for edge in pairs:
        for r,b in ((3,5),(4,4)):
            nv+=1;choices.append(nv)
            add((-nv,endpoint[r,True,edge]));add((-nv,endpoint[b,False,edge]))
    add(choices)
    for p in combinations(POINTS,5):add((-K[p[0]],-K[p[-1]])+tuple(-x for x in terms(p)))
    for p in combinations(POINTS,6):
        for x in (p[0],p[-1]):add((-K[x],)+tuple(-v for v in terms(p)))
    actual_nv,actual=read_cnf()
    assert nv==actual_nv and expected==actual,(nv,actual_nv,len(expected-actual),len(actual-expected))
    receipt=dict(passed=True,variables=nv,clauses=len(actual),missing=0,extra=0,cnf_sha256=sha(ROOT/'formula.cnf'))
    (ROOT/'schema-audit.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

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



def sat_audit():
    began=time.monotonic();nv,clauses=read_cnf();model=set()
    for line in (ROOT/'solve.stdout').read_text().splitlines():
        if line.startswith('v '):model.update(int(x) for x in line[2:].split() if int(x))
    assert all((v in model)!=(-v in model) for v in range(1,nv+1))
    assert all(any(v in model for v in row) for row in clauses)
    triples=tuple(combinations(POINTS,3)); colors={t:i+1 in model for i,t in enumerate(triples)}
    dyn={};states={}
    for red in (False,True):dyn[red],states[red]=physical_dp(colors,red)
    source={x for x in POINTS if any(5 in table for (s,t),table in dyn[False].items() if s==x)}
    terminal={x for x in POINTS if any(5 in table for (s,t),table in dyn[False].items() if t==x)}
    K=source&terminal
    inside={}
    for size,red in ((3,True),(4,True),(4,False),(5,False)):
        for path in combinations(sorted(K),size):
            if all(colors[path[i:i+3]]==red for i in range(size-2)):
                inside.setdefault((size,red,(path[0],path[-1])),[]).append(path)
    central=[]
    for edge in combinations(sorted(K),2):
        for r,b in ((3,5),(4,4)):
            red=inside.get((r,True,edge),[]);blue=inside.get((b,False,edge),[])
            if red and blue:central.append(dict(endpoints=edge,R_length=r,B_length=b,R_path=red[0],B_path=blue[0]))
    weak=[(edge,r,b) for edge in combinations(POINTS,2) for r in dyn[True][edge] for b in dyn[False][edge] if r+b>=9]
    maxR=max(k for tab in dyn[True].values() for k in tab);maxB=max(k for tab in dyn[False].values() for k in tab)
    checks=dict(literal_assignment=True,packets=all(sum(a!=b for a,b in zip(bits,bits[1:]))<=1
        for q in combinations(POINTS,4) for bits in [[colors[t] for t in combinations(q,3)]]),
        no_R7=maxR<=6,no_B6=maxB<=5,no_weak7=not weak,actual_weak6_inside_actual_K=bool(central),
        K_no_R6_endpoints=all(not any(6 in tab for (s,t),tab in dyn[True].items() if s==x or t==x) for x in K),
        no_R5_between_K=all(5 not in dyn[True][a,b] for a,b in combinations(sorted(K),2)))
    spec=json.loads((ROOT/'spec.json').read_text())
    for name,actual in [('K_flags',K),('B5_source_flags',source),('B5_terminal_flags',terminal)]:
        checks[name+'_exact']=all((int(var) in model)==(int(x) in actual) for x,var in spec[name].items())
    assert all(checks.values()),checks
    with (ROOT/'colors.tsv').open('w') as f:
        f.write('a\tb\tc\tcolor\n')
        for q in triples:f.write('\t'.join(map(str,q))+('\tR\n' if colors[q] else '\tB\n'))
    anchors={}
    for x in sorted(K):
        anchors[x]=dict(incoming=next(tab[5] for (s,t),tab in dyn[False].items() if t==x and 5 in tab),
                       outgoing=next(tab[5] for (s,t),tab in dyn[False].items() if s==x and 5 in tab))
    endpoints=[dict(pair=edge,R_lengths=sorted(dyn[True][edge]),B_lengths=sorted(dyn[False][edge]),
                    R_witnesses=dyn[True][edge],B_witnesses=dyn[False][edge]) for edge in combinations(POINTS,2)]
    witness=dict(n=21,K=sorted(K),weak6_in_actual_H=central,K_anchors=anchors,endpoints=endpoints,
                 R6_witness=next((tab[6] for tab in dyn[True].values() if 6 in tab),None))
    (ROOT/'physical-witness.json').write_text(json.dumps(witness,indent=2)+'\n')
    receipt=dict(passed=True,checks=checks,K=sorted(K),K_size=len(K),weak6_in_actual_H=central,DP_states=states,
                 max_R=maxR,max_B=maxB,endpoint_pairs=len(endpoints),seconds=time.monotonic()-began,
                 bindings={p.name:sha(p) for p in (ROOT/'formula.cnf',ROOT/'solve.stdout',ROOT/'colors.tsv',ROOT/'physical-witness.json',Path(__file__))})
    (ROOT/'independent-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
if __name__=='__main__':
    assert platform.system()=='Linux'
    parser=argparse.ArgumentParser();parser.add_argument('--schema',action='store_true');parser.add_argument('--sat',action='store_true')
    args=parser.parse_args();assert args.schema!=args.sat
    schema_audit() if args.schema else sat_audit()

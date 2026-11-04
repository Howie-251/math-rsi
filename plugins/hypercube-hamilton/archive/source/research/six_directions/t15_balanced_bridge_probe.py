"""Prepare the only B exceptions for four promising r3 singleton bridges."""
import itertools,json,collections,sys
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def prepare():
    source=json.loads((R/'q4_balanced_two_avoided_generation.json').read_text());negative={}
    perms=[p+(3,) for p in itertools.permutations(range(3))]
    def tr(v,p):return sum(((v>>j)&1)<<p[j] for j in range(4))
    for row in source['rows']:
        r,y=row['avoided'];raw=(R/f'q4_balanced_two_avoided_{r}_{y}.bin').read_bytes()
        negatives=[]
        for i in range(0,len(raw),30):
            if raw[i+16:i+30]==bytes([255])*14:
                m=raw[i:i+16];negatives.append(frozenset((v,m[v]) for v in range(16) if v<m[v]<16))
        for p in perms:
            key=tr(r,p),tr(y,p);values={frozenset(edge(tr(a,p),tr(b,p)) for a,b in f) for f in negatives}
            if key in negative:assert values==negative[key]
            negative[key]=values
    orbits=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits']
    cases=[];groups=[]
    for idx,cut in ((2,1),(7,0),(10,1),(44,3)):
        row=orbits[idx]
        def drop(z):return (z&((1<<cut)-1))|((z>>(cut+1))<<cut)
        b=drop(next(z for z in row['included'] if not(z>>cut&1)))
        p=[j for j in range(4) if b>>j&1]+[j for j in range(4) if not(b>>j&1)]
        def norm(z):return sum(((z>>p[j])&1)<<j for j in range(4))
        x=norm(drop(next(z for z in row['avoided'] if z>>cut&1)))
        y=norm(drop(next(z for z in row['avoided'] if not(z>>cut&1))))
        zs=[norm(drop(z)) for z in row['included'] if z>>cut&1]
        good=next(z for z in zs if not negative[z,y]);other=next(z for z in zs if z!=good)
        group=dict(orbit=idx,cut=cut,A_omitted=x,B_omitted=y,B_free=7,good_bridge=good,other_bridge=other,
            bad_B_count=len(negative[other,y]));groups.append(group)
        for f in sorted(negative[other,y],key=lambda f:sorted(f)):
            mate={a:b for e in f for a,b in (e,e[::-1])};k=mate[good]
            fb=f-{edge(good,k)}|{edge(other,k)}
            cases.append(dict(id=len(cases),**group,matching=sorted(fb),
                support=65535^(1<<good)^(1<<y),root=0,target=-1,cyclic=1))
    (R/'t15_balanced_bridge_spectrum_inputs.json').write_text(json.dumps(cases,indent=2)+'\n')
    (R/'t15_balanced_bridge_spectrum_inputs.txt').write_text('\n'.join(' '.join(map(str,[c['id'],1,c['support'],0,-1,6,*[v for e in c['matching'] for v in e]])) for c in cases)+'\n')
    print(json.dumps(groups))
def check():
    cases=json.loads((R/'t15_balanced_bridge_spectrum_inputs.json').read_text())
    results=json.loads((R/'t15_balanced_bridge_spectra.json').read_text())
    edges=[(a,b) for a in range(16) for b in range(a+1,16) if (a^b).bit_count()==1];eid={e:i for i,e in enumerate(edges)}
    out=[]
    for c,r in zip(cases,results):
        assert c['id']==r['id'];F=set(map(tuple,c['matching']));union=set()
        for path in r['witnesses']:
            assert len(path)==len(set(path))==14 and set(path)=={v for v in range(16) if c['support']>>v&1}
            E={edge(a,b) for a,b in zip(path,path[1:]+path[:1])};assert F<=E and all(e in eid for e in E-F);union|=E-F
        assert sum(1<<eid[e] for e in union)==r['spectrum']
        allowed={e for e in edges if c['A_omitted'] not in e}-union
        support=set(range(16))-{c['A_omitted']};center=c['other_bridge'];factors=[]
        def match(vs):
            if not vs:yield [];return
            a=min(vs)
            for b in sorted(vs-{a}):
                if edge(a,b) in allowed:
                    for f in match(vs-{a,b}):yield [edge(a,b),*f]
        ns=[v for v in support if edge(center,v) in allowed]
        for a,b in itertools.combinations(ns,2):
            for f in match(support-{center,a,b}):factors.append([edge(center,a),edge(center,b),*f])
        out.append(dict(id=c['id'],orbit=c['orbit'],B_union_size=len(union),outside_union_factors=factors,
            every_A_path_forced_to_intersect=(not factors)))
    result=dict(scope='c1 exceptional B spectra and unconditional A new-degree factor obstruction',
        positive_witnesses_checked=True,cases=out,full_t15_proved=False)
    (R/'t15_balanced_bridge_spectrum_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in c.items() if k!='outside_union_factors'}|{'outside_factors':len(c['outside_union_factors'])} for c in out]))
if __name__=='__main__':(prepare if len(sys.argv)>1 and sys.argv[1]=='prepare' else check)()

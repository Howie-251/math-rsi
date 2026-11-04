"""Independent audit; does not import any author generator/checker.

Negative search uses degree completions, not alternating-path DFS.
Run from any directory with Python 3.10+.
"""
import hashlib
import itertools as it
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALL = set(range(16))
SHORT = {(a,b) for a in ALL for b in ALL if a < b and (a^b).bit_count()==1}
def edge(a,b): return tuple(sorted((a,b)))
def read(name): return json.loads((ROOT/name).read_text(encoding='utf-8'))
def pairs(vs):
    if not vs:
        yield frozenset(); return
    a=min(vs)
    for b in sorted(vs-{a}):
        for rest in pairs(vs-{a,b}): yield rest | {edge(a,b)}
def restricted_pairs(vs, allowed):
    if not vs:
        yield frozenset(); return
    a=min(vs)
    for b in sorted(vs-{a}):
        if edge(a,b) in allowed:
            for rest in restricted_pairs(vs-{a,b},allowed): yield rest | {edge(a,b)}
def cycle_check(path, support, required):
    assert len(path)==len(set(path))==len(support) and set(path)==support
    es={edge(a,b) for a,b in zip(path,path[1:]+path[:1])}
    assert len(es)==len(support) and required<=es and es-required<=SHORT
    return es-required
def connected(es, support):
    seen={min(support)}
    while True:
        nxt=seen|{b for a,b in es if a in seen}|{a for a,b in es if b in seen}
        if nxt==seen: return seen==support
        seen=nxt
def disprove_negative(F, omitted):
    support=ALL-set(omitted)
    allowed={e for e in SHORT-F if set(e)<=support}
    n0=[v for v in support if edge(0,v) in allowed]
    n7=[v for v in support if edge(7,v) in allowed]
    factors=0
    for a,b in it.combinations(n0,2):
        for c,d in it.combinations(n7,2):
            if len({a,b,c,d})!=4: continue
            for M in restricted_pairs(support-{0,7,a,b,c,d},allowed):
                H=M|{edge(0,a),edge(0,b),edge(7,c),edge(7,d)}
                factors+=1
                assert not connected(F|H,support), ('false negative',omitted,sorted(F),sorted(H))
    return factors
def transform(v,p): return sum(((v>>j)&1)<<p[j] for j in range(4))

def main():
    inputs=['T15_BALANCED_BRIDGE_FOUR_CORES.md','q4_balanced_two_avoided_generation.json',
            't15_analytic_geometry.json','t15_balanced_bridge_spectrum_inputs.json',
            't15_balanced_bridge_spectra.json','t15_balanced_bridge_spectrum_verification.json',
            'Q4_CORE_AND_A4_SPLIT.md']
    n14_report=[]
    for other in (3,15):
        name=f'q4_two_hole_{other}.bin'; inputs.append(name)
        raw=(ROOT/name).read_bytes(); assert len(raw)==31*135135
        expected=set(pairs(ALL-{0,other})); assert len(expected)==135135
        seen=set()
        for offset in range(0,len(raw),31):
            mate=list(raw[offset:offset+16]); path=list(raw[offset+16:offset+31])
            assert mate[0]==mate[other]==255
            covered=ALL-{0,other}
            assert all(mate[v] in covered-{v} and mate[mate[v]]==v for v in covered)
            F=frozenset(edge(v,mate[v]) for v in covered)
            assert F in expected and F not in seen; seen.add(F)
            cycle_check(path,ALL-{0},F)
        assert seen==expected
        n14_report.append(dict(other_hole=other,omitted=0,records=len(seen),all_certificates_valid=True))
        del expected,seen
    generation=read(inputs[1]); tables={}; table_report=[]; perms=[p+(3,) for p in it.permutations(range(3))]
    for row in generation['rows']:
        t,y=row['avoided']; name=f'q4_balanced_two_avoided_{t}_{y}.bin'; inputs.append(name)
        raw=(ROOT/name).read_bytes(); assert len(raw)==30*10395
        expected=set(pairs(ALL-{0,7,t,y})); assert len(expected)==10395
        seen=set(); negatives=set(); positive=0; factors=0
        for offset in range(0,len(raw),30):
            mate=list(raw[offset:offset+16]); path=list(raw[offset+16:offset+30])
            assert all(mate[v]==255 for v in (0,7,t,y))
            assert all(mate[v] in ALL-{v,0,7,t,y} and mate[mate[v]]==v for v in ALL-{0,7,t,y})
            F=frozenset(edge(v,mate[v]) for v in ALL-{0,7,t,y})
            assert F in expected and F not in seen; seen.add(F)
            if path==[255]*14:
                negatives.add(F); factors+=disprove_negative(F,(t,y))
            else:
                cycle_check(path,ALL-{t,y},F); positive+=1
        assert seen==expected and positive==row['positive'] and len(negatives)==row['negative']
        orbit=set()
        for p in perms:
            key=(transform(t,p),transform(y,p)); orbit.add(key)
            ns={frozenset(edge(transform(a,p),transform(b,p)) for a,b in F) for F in negatives}
            assert key not in tables or tables[key]==ns
            tables[key]=ns
        assert orbit==set(map(tuple,row['orbit'])) and len(orbit)==row['orbit_size']
        table_report.append(dict(omitted=[t,y],records=len(seen),positives=positive,negatives=len(negatives),disconnected_degree_completions=factors))
    assert set(tables)=={(t,y) for t in ALL-{0} if t.bit_count()%2==0 for y in ALL-{7} if y.bit_count()%2==1}
    assert len(tables)==49
    orbits=read('t15_analytic_geometry.json')['T15']['residual_orbits']
    cases=read('t15_balanced_bridge_spectrum_inputs.json'); spectra=read('t15_balanced_bridge_spectra.json')
    assert len(cases)==len(spectra)==15
    rows=[(2,1,0,1,9,3),(7,0,0,1,9,10),(10,1,0,1,9,15),(44,3,9,11,10,6)]
    geometric=[]; exception_report=[]; witness_count=0
    for idx,cut,x,y,r,s in rows:
        geo=orbits[idx]
        def drop(v): return (v&((1<<cut)-1))|((v>>(cut+1))<<cut)
        b=drop(next(v for v in geo['included'] if not(v>>cut&1)))
        ordering=[j for j in range(4) if b>>j&1]+[j for j in range(4) if not(b>>j&1)]
        def norm(v): return sum(((v>>ordering[j])&1)<<j for j in range(4))
        assert norm(b)==7
        assert {norm(drop(v)) for v in geo['included'] if v>>cut&1}=={r,s}
        assert [norm(drop(v)) for v in geo['avoided'] if v>>cut&1]==[x]
        assert [norm(drop(v)) for v in geo['avoided'] if not(v>>cut&1)]==[y]
        assert len([v for v in geo['included'] if not(v>>cut&1)])==1
        assert not tables[r,y]
        expected_FB=set()
        for F in tables[s,y]:
            k=next(b if a==r else a for a,b in F if r in (a,b))
            FB=(F-{edge(r,k)})|{edge(s,k)}
            assert set().union(*(set(e) for e in FB))==ALL-{0,7,y,r} and len(FB)==6
            assert (FB-{edge(s,k)})|{edge(r,k)}==F
            expected_FB.add(FB)
        actual=[c for c in cases if c['orbit']==idx]
        assert {frozenset(map(tuple,c['matching'])) for c in actual}==expected_FB
        assert len(actual)==len(expected_FB)==len(tables[s,y])
        geometric.append(dict(orbit=idx,cut=cut,x=x,y=y,r=r,s=s,exception_count=len(actual)))
        for c in actual:
            assert (c['cut'],c['A_omitted'],c['B_omitted'],c['good_bridge'],c['other_bridge'])==(cut,x,y,r,s)
            sp=spectra[c['id']]; assert sp['id']==c['id']
            FB=frozenset(map(tuple,c['matching'])); U=set()
            assert c['support']==sum(1<<v for v in ALL-{y,r})
            for path in sp['witnesses']:
                U|=cycle_check(path,ALL-{y,r},FB); witness_count+=1
            assert sum(1<<i for i,e in enumerate(sorted(SHORT)) if e in U)==sp['spectrum']
            G={e for e in SHORT if x not in e}-U
            neighbors=[v for v in ALL-{x,s} if edge(s,v) in G]
            checked_pairs=0; factor_count=0
            for a,b in it.combinations(neighbors,2):
                checked_pairs+=1
                for M in restricted_pairs(ALL-{x,s,a,b},G): factor_count+=1
            assert factor_count==0
            exception_report.append(dict(id=c['id'],orbit=idx,union_size=len(U),witnesses=len(sp['witnesses']),center_neighbor_pairs=checked_pairs,forbidden_factors=factor_count))
    assert [g['exception_count'] for g in geometric]==[3,1,10,1]
    report=dict(status='PASS',scope='All 13 Q4 table orbits, N14 Q4 base, and four complete T15 cores 2,7,10,44',
        model='gpt-6.1-sol',reasoning_effort='high',fork_turns='none',review_independence='same-family',acceptance_status='provisional',
        generated_at=datetime.now(timezone.utc).isoformat(),author_checker_imported=False,
        record_count=sum(t['records'] for t in table_report),negative_count=sum(t['negatives'] for t in table_report),
        tables=table_report,n14_base=n14_report,n14_records_verified=sum(r['records'] for r in n14_report),geometries=geometric,exceptional_B=exception_report,positive_B_witnesses=witness_count,
        hashes={n:'sha256:'+hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in inputs+[Path(__file__).name]})
    (ROOT/'T15_BALANCED_BRIDGE_independent_check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('status','record_count','negative_count','positive_B_witnesses')}))
if __name__=='__main__': main()

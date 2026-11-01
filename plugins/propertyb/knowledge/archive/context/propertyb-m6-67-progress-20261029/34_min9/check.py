"""Complete independent local certificate: v34, minimum degree nine."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json,time,signal
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
START=time.process_time()
spec=importlib.util.spec_from_file_location('independent_pool_kernel',BASE/'independent31_33/check.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
signal.setitimer(signal.ITIMER_PROF,10)
signal.alarm(90)


def main():
    pairs=json.loads((BASE/'root/PAIRS_PROBE.json').read_text())
    triple=json.loads((BASE/'root/TWO_ARM_PROBE.json').read_text())['rows']
    rows=[]
    def add(kind,degrees,paircounts,source):
        ell=a.ell_case(degrees,paircounts,tau=0)
        slots=source['pos']
        assert len(slots)==len(degrees)
        assert min(ell.values())>=0 and sum(ell.values())==66
        for j,d in enumerate(degrees):
            assert sum(n for t,n in ell.items() if t>>j&1)==d
        for (i,j),lam in paircounts.items():
            assert sum(n for t,n in ell.items() if t>>i&1 and t>>j&1)==lam
        if 'ell' in source:
            assert ell=={int(t):n for t,n in source['ell'].items() if n}
        value=a.bound(34,slots,ell)
        assert value==Q(source['U'])<1,(kind,degrees,paircounts,value,source['U'])
        rows.append(dict(kind=kind,degrees=list(degrees),paircounts={f'{i},{j}':lam for (i,j),lam in paircounts.items()},tau=0 if len(degrees)==3 else None,ell=ell,positions=slots,U=str(value),strict=True,exact_match_with_root=True))
    def unique(seq):
        assert len(seq)==1
        return seq[0]
    for e in range(9,12):
        source=unique([r for r in pairs if (r['v'],r['d'],r['e'],r['lam'])==(34,9,e,1)])
        add('unit_partner_at_most11',(9,e),{(0,1):1},source)
    for f in (12,13):
        for lam in range(1,12):
            source=unique([r for r in triple if (r['v'],r['d'],r['e'],r['f'],r['lam'],r['tau'])==(34,9,12,f,lam,0)])
            add('noncoincident_unit_arms',(9,12,f),{(0,1):1,(0,2):1,(1,2):lam},source)
    for lam in (2,3):
        source=unique([r for r in pairs if (r['v'],r['d'],r['e'],r['lam'])==(34,9,9,lam)])
        add('two_nine_vertices',(9,9),{(0,1):lam},source)
    assert len(rows)==27
    assert Counter(r['kind'] for r in rows)=={'unit_partner_at_most11':3,'noncoincident_unit_arms':22,'two_nine_vertices':2}
    # Selection arithmetic, including both possible thirteen-degree cases.
    assert 396-34*9==90 and 2*33-5*9==21
    assert 9+90//21==13 and 5*21-10>90
    thirteen=[]
    for u in range(21,34):
        if 4*u>90:continue
        lower9=34-u-(90-4*u)
        assert u in (21,22) and lower9>=7 and 3*(lower9-1)>12
        thirteen.append(dict(unit_neighbors=u,excess_remaining=90-4*u,nine_vertices_lower=lower9))
    result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',
                scope='Complete v34/66-edge/paircover/minimum-nine branch, with 27 necessary local types',
                mathematical_selection='REPORT.md, lemmas34.9.1-34.9.3; root derivation independently checked',
                method='Independent falling-factorial injection probabilities and independent component-support quota DP; full-link-pool deletion',
                submitted_probability_or_generator_imported=False,
                complete_profiles=len(rows),independently_replayed=len(rows),
                minimum_unit_degree_upper=13,thirteen_partner_budget=thirteen,
                maximum=str(max(Q(r['U']) for r in rows)),
                summaries=[dict(kind=k,profiles=sum(r['kind']==k for r in rows),maximum=str(max(Q(r['U']) for r in rows if r['kind']==k))) for k in sorted({r['kind'] for r in rows})],
                cpu_seconds=time.process_time()-START,rows=rows)
    (HERE/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'CHECK.json').write_text(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))


if __name__=='__main__':main()

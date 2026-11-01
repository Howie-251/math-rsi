"""Independent complete min10 audit plus old v34/min7-8 interface replay."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from itertools import combinations
from collections import Counter
import importlib.util,json,time,signal
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
START=time.process_time()
spec=importlib.util.spec_from_file_location('component_injection',BASE/'independent31_33/check.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
full_deletion=a.deletion
signal.setitimer(signal.ITIMER_PROF,20)
signal.alarm(120)


def maximum_R(v,slots,ell,j):
    types=[t for t in ell if t>>j&1];cells=[]
    for i,t in enumerate(types):
        for u in types[i:]:
            cap=comb(ell[t],2) if t==u else ell[t]*ell[u]
            if cap:
                weight=a.prob(v,slots,slots[j],t,u)+a.prob(v,slots,slots[j],u,t)
                cells.append((weight,cap,t|u))
    costs=[]
    for R in range(1<<len(slots)):
        if R>>j&1:continue
        f=sum(n for t,n in ell.items() if t>>j&1 and not t&R)
        need=a.quota(f,v-1-R.bit_count());cost=Q(0)
        for w,cap,union in sorted(cells):
            if not union&R:
                take=min(cap,need);cost+=take*w;need-=take
        assert need==0
        costs.append(cost)
    return max(costs)


# Independent reconstruction of the OLD component support relaxation:
# CW plus feedback-vertex/forest only, no unique-complement eleven-point term.
FMAX,QMAX,INF=12,80,100000
exact=[[INF]*(QMAX+1) for _ in range(FMAX+1)];exact[0][0]=0
for f in range(1,FMAX+1):
    for t in range(1,f+1):
        for e in range(t-1,min(comb(t,2),QMAX)+1):
            cw=a.ceil(t*t,t+2*e);forest=a.ceil(2*t-e-1,2)
            support=5 if t==1 else max(6,5*cw,5*forest)
            for q in range(e,QMAX+1):
                exact[f][q]=min(exact[f][q],support+exact[f-t][q-e])
old_support=[]
for row in exact:
    best=INF;prefix=[]
    for x in row:best=min(best,x);prefix.append(best)
    old_support.append(prefix)


def old_quota(f,N):
    return next(q for q in range(QMAX+1) if old_support[f][q]<=N)


def old_joint(v,slots,ell,j):
    assert len(slots)==2 and ell.get(3)==1
    bit=1<<j
    degree=sum(n for t,n in ell.items() if t&bit)
    singleton=ell[bit]
    q_all=old_quota(degree,v-1)
    q_avoid=old_quota(singleton,v-2)
    core_cap=comb(singleton,2)
    rest_cap=singleton
    w_core=2*a.prob(v,slots,slots[j],bit,bit)
    w_rest=a.prob(v,slots,slots[j],bit,3)+a.prob(v,slots,slots[j],3,bit)
    feasible=[]
    for rest in range(rest_cap+1):
        core=max(0,q_avoid,q_all-rest)
        if core<=core_cap:
            feasible.append(core*w_core+rest*w_rest)
    assert feasible
    return min(feasible)


def norm(ell):return tuple(sorted((int(t),n) for t,n in ell.items() if n))


def main():
    cert=json.loads((BASE/'34_min10/CERTIFICATE.json').read_text())
    assert cert['v']==34 and cert['M']==66
    expected={norm(a.two(10,10,lam)) for lam in range(1,11)}
    expected.add(norm(a.two(10,11,1)))
    triple_domain=set()
    for lam in range(1,12):
        for tau in range(min(2,lam)+1):
            if 9-lam+tau<0:continue
            ell=a.ell_case((10,11,11),{(0,1):2,(0,2):2,(1,2):lam},tau)
            expected.add(norm(ell));triple_domain.add((lam,tau))
    assert len(triple_domain)==29 and len(expected)==40
    keys=[norm(r['ell']) for r in cert['rows']]
    assert len(keys)==len(set(keys))==40 and set(keys)==expected
    # Exact selection inequalities across every allowed actual u.
    budgets=[]
    for u in range(16,24):
        eleven_lower=(33-u)-(23-u)
        high_codegree_upper=17-(33-u)
        assert eleven_lower==10 and high_codegree_upper==u-16<=7
        assert eleven_lower-high_codegree_upper>=3
        budgets.append(dict(u=u,nonunit_eleven_lower=eleven_lower,codegree_ge3_upper=high_codegree_upper,eleven_codegree2_lower=eleven_lower-high_codegree_upper))
    replay=[]
    for r in cert['rows']:
        ell=dict(norm(r['ell']));ds=r['ds']
        assert all(sum(n for t,n in ell.items() if t>>j&1)==degree for j,degree in enumerate(ds))
        if len(ds)==3:
            assert ds==[10,11,11]
            actual_pairs=[sum(n for mask,n in ell.items() if mask>>i&1 and mask>>j&1) for i,j in combinations(range(3),2)]
            assert actual_pairs==r['ls'] and ell.get(7,0)==r['tau']
        else:
            assert ell.get(3,0)==r['lam']
        use_max=(len(ds)==3 and r['ls'][2]==2)
        assert r['deduction']==('component_max_R' if use_max else 'component_full_pool')
        a.deletion=maximum_R if use_max else full_deletion
        value=a.bound(34,r['pos'],ell)
        assert value==Q(r['U'])<1 and r['strict']
        replay.append(dict(ds=ds,ell=ell,positions=r['pos'],deduction=r['deduction'],U=str(value),exact_match=True,strict=True))
    assert sum(r['deduction']=='component_max_R' for r in replay)==3
    assert max(Q(r['U']) for r in replay)==Q('413127/413540')==Q(cert['maximum'])
    adaptive=json.loads((BASE/'mid34_38/ADAPTIVE_COMPONENT.json').read_text())
    rr=[r for r in adaptive['rows'] if r['v']==34 and r['degrees'][0] in (7,8)]
    pair_domain={(d,e) for d in (7,8) for e in range(d,d+(396-34*d)//(66-5*d)+1)}
    assert len(rr)==len(pair_domain)==11
    assert {tuple(r['degrees']) for r in rr}==pair_domain
    old_rows=[]
    old_quotas=set()
    a.deletion=old_joint
    for r in rr:
        assert r['blocks']==[3] and sorted(r['assigned'])==sorted(r['degrees'])
        ds=r['assigned'];ell=a.two(ds[0],ds[1],1)
        value=a.bound(34,r['positions'],ell)
        assert value==Q(r['U'])<1 and r['strict']
        for degree in ds:
            old_quotas.add((degree,33,old_quota(degree,33)))
            old_quotas.add((degree-1,32,old_quota(degree-1,32)))
        old_rows.append(dict(degrees=r['degrees'],assigned=ds,positions=r['positions'],ell=ell,U=str(value),exact_match=True,strict=True))
    # Connect all possible actual minimum degrees at v34. Existing audited
    # min9/min11 files are read for interface integrity, not recomputed here.
    c9=json.loads((BASE/'34_min9/CERTIFICATE.json').read_text())
    c11=json.loads((BASE/'34_min11/CERTIFICATE.json').read_text())
    assert c9['complete_profiles']==27 and c9['status']=='PASS' and all(Q(r['U'])<1 for r in c9['rows'])
    assert c11['profiles']==9 and c11['status']=='PASS' and all(Q(r['U'])<1 for r in c11['rows'])
    assert (33+4)//5==7 and 396//34==11
    interface=dict(vertex_count=34,minimum_degree_range=[7,8,9,10,11],branch_profiles={'7_and_8':11,'9':27,'10':40,'11':9},total_profiles=87,
                   min9_evidence='../34_min9/REPORT.md and CERTIFICATE.json (previous independent audit)',
                   min11_evidence='../34_min11/REPORT.md and CERTIFICATE.json (previous root-read proof and dual arithmetic)',
                   statement='All possible v34 minimum degrees have complete actual selection arguments and strict full necessary local domains, modulo the common reduction/probability/component-lemma imports.')
    result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',
                scope='All40 v34/min10 local types plus all11 older adaptive v34/min7-8 types; complete34 minimum-degree interface',
                min10_profiles=40,min10_triple_types=29,min10_max_R_types=3,minimum10_maximum=str(max(Q(r['U']) for r in replay)),
                min10_selection_budgets=budgets,
                adaptive78_profiles=11,adaptive78_quota_version='CW plus feedback-vertex only; joint complete/avoid-other-lock quota integer minimization',
                adaptive78_maximum=str(max(Q(r['U']) for r in old_rows)),
                adaptive78_quotas=[dict(f=f,N=N,q=q) for f,N,q in sorted(old_quotas)],
                interface34=interface,submitted_generator_or_probability_imported=False,
                cpu_seconds=time.process_time()-START,minimum10_rows=replay,adaptive78_rows=old_rows)
    (HERE/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('minimum10_rows','adaptive78_rows','adaptive78_quotas','min10_selection_budgets')},indent=2))


if __name__=='__main__':main()

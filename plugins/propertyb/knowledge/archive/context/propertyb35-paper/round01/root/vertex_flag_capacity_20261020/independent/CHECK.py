"""Independent bounded min-plus DP and saved63-key application; no pilot imports."""
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
Q4 = ROOT / 'middle/min_degree_seven_residual_cap12_pilot_20261020'
START = time.process_time()
INF = 10**12


def balanced(d, t):
    a, b = divmod(2*t, d)
    return (d-b)*a*a + b*(a+1)*(a+1)


# Direct slot DP: each slot is an integer in [0,d-1]. It does not assume
# balancing or use a marginal-sort implementation.
slot_checks = []
for d in range(1, 14):
    dp = [0]
    for slot in range(d):
        nxt = [INF]*(len(dp)+d-1)
        for mass, cost in enumerate(dp):
            for x in range(d):
                nxt[mass+x] = min(nxt[mass+x], cost+x*x)
        dp = nxt
    costs = [dp[2*t] for t in range(d*(d-1)//2+1)]
    assert costs == [balanced(d,t) for t in range(len(costs))]
    steps = [b-a for a,b in zip(costs,costs[1:])]
    assert steps == sorted(steps)
    slot_checks.append({'d':d, 'all_t_checked':len(costs)})


def vertex_dp(degrees, top):
    # Ordinary bounded min-plus convolution, one original vertex at a time.
    # Prefix marginal sorting is deliberately not used.
    dp = [0]
    quotas = []
    for d in degrees:
        quota = d*(d-1)//2 - max(0,(4*d-20+2)//3)
        quotas.append(quota)
        values = [balanced(d,t) for t in range(quota+1)]
        nxt = [INF]*min(top+1,len(dp)+quota)
        for old_mass, cost in enumerate(dp):
            for t in range(min(quota,len(nxt)-1-old_mass)+1):
                candidate = cost+values[t]
                if candidate < nxt[old_mass+t]:
                    nxt[old_mass+t] = candidate
        dp = nxt
    return dp, quotas


def flag_pair(s):
    a,b = divmod(s,5)
    return (s*s-((5-b)*a*a+b*(a+1)*(a+1)))//2


def p_bound(n1, squares):
    q,r = divmod(2*n1,30)
    assert q<=35 and (q<35 or r==0)
    old = q*flag_pair(30)+flag_pair(r)
    new = min(old,(900*q+r*r-squares)//2)
    return new,old


def allocate(n1,caps,p):
    # Fill the largest actual coefficient first. This is an independent
    # implementation of the five-capacity/shared-P linear maximization.
    value = 6864*n1
    used = []
    for i in range(4,-1,-1):
        x = min(caps[i],p)
        value += (36,120,330,792,1716)[i]*x
        p -= x
        used.append([i,x])
    return value,used


cap = json.loads((Q4/'CAP12_KEY_REFINEMENT.json').read_text())
primary = json.loads((Q4/'NEWP_REFINEMENT.json').read_text())
source = json.loads((ROOT/'root/tau_shared_capacities_20261020/FINAL_LAMBDA4_VERIFY.json').read_text())
root_primary = json.loads((HERE.parent/'RESULT.json').read_text())
prior_audit = json.loads((Q4/'independent/RESULT.json').read_text())
assert prior_audit['full63_contexts_equal']
assert len(cap['all_keys'])==63
degree_map = {j['spectrum_id']:j['degrees'] for j in source['jobs']}
for job in source['jobs']:
    if job['spectrum_id'] in {x['spectrum_id'] for x in cap['jobs']}:
        assert job['full_paircap_from_nonB_pair_gates'] and not job['lambda4_subcase_only']
old63 = {(j['spectrum_id'],tuple(k['n']),k['tau']):k
         for j in source['jobs'] for k in j['survivors']
         if j['spectrum_id'] in {x['spectrum_id'] for x in cap['jobs']}}
assert len(old63)==63
root_lookup = {(j['spectrum_id'],tuple(k['n']),k['tau']):k
               for j in root_primary['jobs'] for k in j['keys']}
new_lookup = {(k['spectrum_id'],tuple(k['n']),k['tau']):k for k in primary['keys']}
prior_contexts = {(k['spectrum_id'],k['survivor_index']):k for k in prior_audit['contexts']}

dp_records = []
tables = {}
for sid in sorted({k['spectrum_id'] for k in cap['all_keys']}):
    targets = sorted({k['n'][1] for k in cap['all_keys'] if k['spectrum_id']==sid})
    dp,quotas = vertex_dp(degree_map[sid],max(targets))
    tables[sid] = dp
    dp_records.append({'spectrum_id':sid,'degrees':degree_map[sid],
                       'vertex_quotas':quotas,'all_N_through':len(dp)-1,
                       'requested_B':{str(n):dp[n] for n in targets}})

rows = []
for k in cap['all_keys']:
    sid,n,tau = k['spectrum_id'],k['n'],k['tau']
    key = sid,tuple(n),tau
    old = old63[key]
    assert old['caps'][0:3]==k['new_caps'][0:3] and old['caps'][4]==k['new_caps'][4]
    assert k['new_caps'][3] == (12 if k['cap12_caller_complete_in_pilot'] else old['C3_coefficient'])*n[3]
    # The independently replayed2633 certificates and caller domains establish
    # the cap12 flags. We import that already completed audit, not its counter.
    ctx = prior_contexts[sid,k['survivor_index']]
    assert ctx['all_missing_gates_strict']==k['cap12_caller_complete_in_pilot']
    p,oldp = p_bound(n[1],tables[sid][n[1]])
    assert root_lookup[key]['newP']==p and root_lookup[key]['oldP']==oldp
    value, allocation = allocate(n[1],k['new_caps'],p)
    if key in new_lookup:
        ref = new_lookup[key]
        assert (ref['newP'],ref['oldP'],ref['new_twice_L'],ref['strict']) == (p,oldp,value,value<5445440)
    rows.append({'spectrum_id':sid,'n':n,'tau':tau,'B_star':tables[sid][n[1]],
                 'P_bound':p,'old_P_bound':oldp,'caps':k['new_caps'],
                 'twice_L':value,'threshold_minus_twice_L':5445440-value,
                 'strict':value<5445440,'greedy_allocation_descending':allocation})

remaining = [k for k in rows if not k['strict']]
strict_ids = sorted(sid for sid in tables if all(k['strict'] for k in rows if k['spectrum_id']==sid))
assert len(remaining)==3 and strict_ids==[50,52,53,78,83,84,85,88,89,93,98]
out = {'status':'PASS_WITH_DECLARED_IMPORTS','review_independence':'same-family',
       'acceptance_status':'provisional','new_domain_scan':False,
       'scope':'13 actual all-lambda<=4 source spectra, all63 previously saved moment keys; new P independently by min-plus DP; cap12 uses independently replayed2633 certificates and actual caller.',
       'slot_DP_checks':slot_checks,'vertex_DP':dp_records,'source_keys':63,
       'strict_keys':60,'whole_source_spectrum_ids_strict':strict_ids,
       'remaining_keys':remaining,'all_keys':rows,'cpu_seconds':time.process_time()-START}
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('all_keys','vertex_DP','slot_DP_checks')},indent=2))

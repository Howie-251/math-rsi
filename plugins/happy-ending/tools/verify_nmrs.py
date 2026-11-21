#!/usr/bin/env python3
"""Bounded, read-only exact replays for the 2026-11-20 N(m,r,s) archive.

Python >=3.10, standard library only. This checks finite certificates and
arithmetic consequences. It does not prove the input-to-inequality bridges or
replay omitted multi-gigabyte SAT proofs. Output is JSON on stdout.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceil(x):
    x = F(x)
    return -(-x.numerator // x.denominator)


def read(path):
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def seed(path):
    d, digest = read(path)
    t, den = d['v'], d['denominator']
    require(d['a'] == 5 and d['profile'] == 'normalized', 'wrong seed profile')
    require(type(t) is int and 5 <= t <= 128 and type(den) is int and den > 0,
            'invalid or unbounded seed dimensions')
    weights = {}
    for i, j, w in d['weights']:
        require(all(type(x) is int for x in (i,j,w)), 'noninteger seed')
        require(i >= 0 and j >= 0 and i+j < t-4 and w >= 0 and (i,j) not in weights,
                'illegal or duplicate weight')
        weights[i,j] = w
    maxe = maxp = 0
    faces = 0
    for i in range(t-3):
        for j in range(t-3-i):
            e = sum(weights.get((x,j),0) for x in range(i))
            e += sum(weights.get((i,y),0) for y in range(j))
            p = e + (t-4-i-j)*weights.get((i,j),0)
            require(e <= den and p <= 5*den, 'infeasible face')
            maxe, maxp = max(maxe,e), max(maxp,p)
            faces += 1
    numerator = sum(comb(t-2-i-j,3)*w for (i,j),w in weights.items())
    W = F(numerator,den)
    return {'file':path.name,'sha256':digest,'height':t,'faces':faces,
            'positive_weights':sum(w > 0 for w in weights.values()),
            'max_E_numerator':maxe,'max_P_numerator':maxp,'denominator':den,
            'objective_numerator':numerator,'W':str(W),
            'coefficient':str(W/(5*comb(t,4)))}, W


def envelope(v, p, roww, unionw, unioncost):
    volume = comb(v,4)
    rr, ru = roww*F(volume,comb(44,4)), unionw*F(volume,comb(44,4))
    theta = F(40,v-4)
    a = theta*40+(1-theta)*unioncost
    require(v-4 >= 4*max(10,ceil(a/(44-a))), 'envelope monotonicity not established')
    q = max(0,ceil((rr-40*p)/4),ceil((ru-a*p)/(44-a)))
    require(q <= p, 'empty feasible envelope')
    h = ceil(F(comb(v+4,4)+(v-4)*p+4*q,v+1))
    return {'p':p,'q':q,'H':h,'N':comb(v+6,5)-h}


def window(root):
    names = ['normalized-a5-v44.json','normalized-a5-v45.json',
             'normalized-a5-v48.json','normalized-a5-v56.json',
             'normalized-a5-v64-repaired.json']
    records, seeds = [], {}
    for name in names:
        rec, w = seed(root/'inputs/window'/name)
        records.append(rec)
        seeds[rec['height']] = ceil(w)
    oldrec, oldw = seed(root/'inputs/old-window/normalized-a5-v44.json')
    row, rowhash = read(root/'inputs/old-window/a5-v44.json')
    union, unionhash = read(root/'inputs/old-window/union-a5-v44.json')
    def objective(d):
        require(d['v'] == 44 and d['a'] == 5, 'wrong comparator seed')
        return F(sum(comb(42-i-j,3)*w for i,j,w in d['weights']),d['denominator'])
    rw, uw = objective(row), objective(union)
    for d,is_union in [(row,False),(union,True)]:
        wmap = {(i,j):w for i,j,w in d['weights']}
        require(len(wmap) == len(d['weights']) and all(type(x) is int and x >= 0 for triple in d['weights'] for x in triple), 'invalid old weight')
        require(all(i+j < 40 for i,j in wmap), 'old weight outside domain')
        endpoint = {}
        for i in range(41):
            for j in range(41-i):
                e = sum(wmap.get((x,j),0) for x in range(i))+sum(wmap.get((i,y),0) for y in range(j))
                endpoint[i,j] = e
                require((e if is_union else 5*e) <= 40*d['denominator'], 'old red face infeasible')
                require(e+(40-i-j)*wmap.get((i,j),0) <= 44*d['denominator'], 'old private face infeasible')
        if is_union:
            count = 0
            for ii in range(1,41):
                for jj in range(1,42-ii):
                    for i in range(ii):
                        for j in range(jj):
                            cost = 3*endpoint[i,j]+endpoint[ii,j]+endpoint[i,jj]-wmap.get((i,j),0)
                            require(cost <= 40*d['denominator'], 'old union profile infeasible')
                            count += 1
            require(count == comb(43,4), 'incomplete union profile domain')
    # Integer-lift manuscript §§9.2–9.4 transports the union seed using
    # theta*C + (1-theta)*a*E_max for a nonprivate red hole. E is
    # endpoint service only: P = E + (40-i-j)*w is the PRIVATE-face
    # service and remains bounded separately by 44 above.
    unionweights = {(i,j):w for i,j,w in union['weights']}
    union_endpoint_max = max(F(sum(unionweights.get((x,j),0) for x in range(i))+
                              sum(unionweights.get((i,y),0) for y in range(j)),
                              union['denominator'])
                             for i in range(41) for j in range(41-i))
    require(union_endpoint_max == F(8205564,10**6), 'union endpoint cost mismatch')
    unioncost = 5*union_endpoint_max
    require(rw == F(501410212499,10**6) and uw == F(502561846116,10**6),
            'comparator objective mismatch')
    require(unioncost == F(41027820,10**6), 'union partial red-hole cost mismatch')
    olda, newa = {}, {}
    for h in range(44,1025):
        olda[h] = ceil(oldw) if h == 44 else (h*olda[h-1]+h-5)//(h-4)
        newa[h] = max(seeds.get(h,0),0 if h == 44 else (h*newa[h-1]+h-5)//(h-4))
        if h > 44:
            require(F(newa[h],comb(h,4)) >= F(newa[h-1],comb(h-1,4)), 'lift decreased')
    comparisons = []
    expected = {64:(292483,12036380),100:(1805108,100951778),
                128:(4910964,332820841),256:(80465298,9883903109),
                1024:(20966536167,9562924688644)}
    for v in expected:
        old = envelope(v,ceil(F(62043237111,678755000000)*comb(v,4)),rw,uw,unioncost)
        oldlift = envelope(v,ceil(F(olda[v],5)),rw,uw,unioncost)
        new = envelope(v,ceil(F(newa[v],5)),rw,uw,unioncost)
        require((newa[v],new['N']) == expected[v], 'published finite value mismatch')
        comparisons.append({'v':v,'A':newa[v],'new':new,'old_named':old,
                            'old_seed_lifted':oldlift,'gain_named':new['H']-old['H'],
                            'gain_old_seed_lifted':new['H']-oldlift['H']})
    return {'status':'PASS','seeds':records,'old_seed':oldrec,
            'old_row_sha256':rowhash,'old_union_sha256':unionhash,
            'union_endpoint_max':str(union_endpoint_max),
            'union_partial_red_hole_cost':str(unioncost),'recurrence_heights':[44,1024],
            'comparisons':comparisons,'coefficient_1024':str(F(newa[1024],5*comb(1024,4))),
            'limit_upper_strict':str(F(newa[1024],5*comb(1024,4))+F(4,15*comb(1024,3)))}


def arithmetic():
    rows = []
    for m,u,t in [(8,56,100),(9,222,380),(10,773,1372)]:
        rhs = (m-1)*comb(2*m-7,m-4)+(m-3)*u+(m-2)*t
        q = rhs//(m-2)
        rows.append({'m':m,'u':u,'t':t,'budget':rhs,'Q_upper':q,
                     'F_upper_conditional_on_chart_bridge':q+1,
                     'ES_upper_conditional_on_geometric_bridge':q+2,
                     'critical_remainder':rhs-(m-2)*q})
    require([r['Q_upper'] for r in rows] == [293,1098,3978], 'sector arithmetic')
    # Q8=292 uses the extra structural proof; the sector formula alone gives293.
    require((9*comb(9,4)+11*126)//6 == 420, 'H56 relaxed')
    require((9*comb(10,5)+10*237)//6 == 773, 'H66')
    require((9*comb(11,5)+13*419)//7 == 1372, 'H67')
    holes = comb(11,5)-420
    require(holes == 42 and 6*holes == 2*comb(9,4), 'hole incidence')
    degree = F(2*comb(8,3)-holes,5)
    pair_degree = F(2*comb(7,2)-2*degree,4)
    require(degree == 14 and pair_degree.denominator != 1, 'equality divisibility contradiction')
    return {'status':'PASS','sector_budget':rows,'ten_parameter':{
            'H56_relaxed':420,'equality_holes':holes,'label_degree':str(degree),
            'forced_pair_degree':str(pair_degree),
            'pair_equation':'4*d_ij=14 (no integer solution)',
            'H56_conditional_on_equality_bridge':419,'H66':773,'H67':1372},
            'scope':'Exact arithmetic only; capacity imports and structural bridges are mathematical assumptions'}


def signotope(path):
    d, digest = read(path)
    colors = {tuple(map(int,k.split(','))):v for k,v in d.get('chi_in_natural_order',d.get('colors',{})).items()}
    vertices = sorted({x for triple in colors for x in triple})
    n = len(vertices)
    require(vertices == list(range(n)) and n <= 60, 'unsupported witness domain')
    require(set(colors) == set(itertools.combinations(range(n),3)), 'incomplete triple coloring')
    require(set(colors.values()) <= {'B','R'}, 'invalid color')
    for a,b,c,e in itertools.combinations(range(n),4):
        seq = [colors[b,c,e],colors[a,c,e],colors[a,b,e],colors[a,b,c]]
        require(sum(x != y for x,y in zip(seq,seq[1:])) <= 1, 'invalid four-packet')
    best = {c:{} for c in ['B','R']}
    maximum = {}
    for color in best:
        # Every pair is a 2-vertex monochromatic path in either color.
        for start in range(n):
            dp = {(start,j):2 for j in range(start+1,n)}
            for last in range(start+1,n):
                for prev in range(start,last):
                    value = dp.get((prev,last))
                    if value is None:
                        continue
                    best[color][start,last] = max(best[color].get((start,last),2),value)
                    for nxt in range(last+1,n):
                        if colors[prev,last,nxt] == color:
                            dp[last,nxt] = max(dp.get((last,nxt),2),value+1)
        maximum[color] = max(best[color].values())
    weak = max(best['B'][ends]+best['R'][ends] for ends in best['B'])
    require((n == 36 and maximum == {'B':5,'R':5} or
             n == 17 and maximum == {'B':6,'R':7}) and weak < 10,
            'finite calibration mismatch')
    owners = []
    if n == 17:
        for owner in [5,6]:
            prefix = (0,1,2,3,4,owner)
            require(all(colors[t] == 'R' for t in zip(prefix,prefix[1:],prefix[2:])), 'red prefix')
            counts = {}
            for color,length in [('R',7),('B',6)]:
                paths = [(owner,)+tail for tail in itertools.combinations(range(owner+1,n),length-1)
                         if all(colors[t] == color for t in zip((owner,)+tail,tail,tail[1:]))]
                require(paths and all(path[-1] == 12 if color == 'R' else path[1] == 12 for path in paths),
                        'shared lock path interface failed')
                counts[color] = len(paths)
            owners.append({'owner':owner,'shared_lock':12,'all_red7_and_blue6_paths':counts})
    return {'status':'PASS','input':path.name,'sha256':digest,'vertices':n,
            'triples':len(colors),'four_packets':comb(n,4),'max_path_vertices':maximum,
            'max_same_endpoint_path_sum':weak,'predicate':'noB6/noR6/noWeak8' if n == 36 else 'noB7/noR8/noWeak8',
            'shared_lock_owners':owners,
            'scope':'One actual abstract signotope, not a geometric realization or upper-bound certificate'}

def scalar(root):
    rows, digest = read(root/'inputs/scalar/all-n292-types.json')
    require(len(rows) == 6126 and len({tuple(sorted(r.items())) for r in rows}) == 6126,
            'listed scalar count or uniqueness mismatch')
    for r in rows:
        h,d,w,g,e,m,s,b,p,z,a,q,ell,k,Z,R = (r[x] for x in
            ['h','d','w','g','e','m','s','b','p','z','a','q','ell','k','Z_deficit','native_slack'])
        t = lambda x:(3+5*x)//4
        require(all(type(x) is int and x >= 0 for x in r.values()), 'negative scalar')
        require(0 <= h <= 15 and d == 105+h and 0 <= w <= t(h), 'outer scalar domain')
        require(g == 0 if w == 0 else w <= g <= 120-d+w, 'g domain')
        require(e <= min(d,h+w) and m <= min(t(h)-w,d-e,d-w) and
                5*e+4*m <= 3+5*h+w, 'joint scalar budget')
        require(a == d-e-m-56 and a in (45,46) and b == 56+g+m and
                p == 100-g-m and s == d-e+g and z == 292-s-p, 'scalar sectors')
        require(0 <= p <= 100 and 0 <= z <= 100 and g+m <= b <= min(s,100), 'scalar caps')
        require(max(0,m-h) <= q <= m and w+q <= t(h-m+q), 'q domain')
        require(max(w+q,int(g+m>0)) <= ell <= w+m and ell-q <= e and k == ell,
                'lock domain')
        require(Z == h-e-m+ell and 4*ell <= 3+5*Z, 'deficit budget')
        require(s-b == a and p+b == 156 and z == 136-a and
                R == 882-292-5*a-4*z == (1 if a == 45 else 0), 'saturation')
    upper = max(187-h+min(120,(627+6*h+(3+(3+5*h)//4)//5)//6) for h in range(188))
    require(upper == 292, 'global h envelope mismatch')
    return {'status':'PASS_LISTED_SCALAR_TYPES','sha256':digest,'distinct_listed_types':len(rows),
            'h_envelope_domain':[0,187],'h_envelope_maximum':upper,
            'listed_h_range':[min(r['h'] for r in rows),max(r['h'] for r in rows)],
            'listed_lock_range':[min(r['ell'] for r in rows),max(r['ell'] for r in rows)],
            'scope':'Every supplied type satisfies the stated old scalar predicate; listing completeness not re-enumerated. Necessary relaxation, not a 292-point signotope.'}

def receipts(root):
    base = root/'evidence'
    first,_ = read(base/'866/primary02/result.json')
    manifest,_ = read(base/'866/primary02/manifest.json')
    rebuild,_ = read(base/'866/reconstruction.json')
    require(first['solver_returncode'] == 20 and first['checker_returncode'] == 0 and first['verified_markers'] == 1,
            '866 historical checker unsuccessful')
    require(first['cnf_sha256'] == manifest['cnf_sha256'], '866 identity mismatch')
    require((base/'866/primary02/checker.log').read_text().splitlines().count('s VERIFIED') == 1,
            '866 log marker mismatch')
    require(rebuild['cnf_sha256'] == first['cnf_sha256'] == rebuild['expected_cnf_sha256'],
            '866 reconstruction hash mismatch')
    require((rebuild['variables'],rebuild['clauses']) == (manifest['variables'],manifest['clauses'])
            == (543459,41049536), '866 reconstruction size mismatch')
    projection_records,_ = read(base/'PUBLIC_PROJECTIONS.json')
    projections = {r['path']:r for r in projection_records}
    source_records = []
    for item in manifest['sources']:
        relative = 'evidence/866/source/'+Path(item['snapshot']).name
        source = root/relative
        actual = hashlib.sha256(source.read_bytes()).hexdigest()
        projected = projections.get(relative)
        if projected:
            require(projected['original_sha256'] == item['sha256'] and actual == projected['projection_sha256'], '866 projected source binding mismatch')
        else:
            require(actual == item['sha256'], '866 original source hash mismatch')
        source_records.append({'file':relative,'historical_original_sha256':item['sha256'],
                               'public_sha256':actual,'is_projection':bool(projected)})
    receipt858,_ = read(base/'858/ordinary858-64-final-receipt.json')
    require(receipt858['status'].startswith('PASS_TWO_ACTUAL_DRAT'), '858 receipt unsuccessful')
    for relative,record in projections.items():
        require(hashlib.sha256((root/relative).read_bytes()).hexdigest() == record['projection_sha256'], 'public projection identity mismatch')
    source858_records = []
    for source in sorted((base/'858/source').glob('*.py')):
        relative = 'evidence/858/source/'+source.name
        historical = receipt858['files'][source.name]['sha256']
        actual = hashlib.sha256(source.read_bytes()).hexdigest()
        projected = projections.get(relative)
        if projected:
            require(projected['original_sha256'] == historical and actual == projected['projection_sha256'], '858 projected source binding mismatch')
        else:
            require(actual == historical, '858 original source mismatch')
        source858_records.append({'file':relative,'historical_original_sha256':historical,
                                  'public_sha256':actual,'is_projection':bool(projected)})
    checks = receipt858['checks']
    for name in ['first','second']:
        log = checks[name]['full_log'].encode()
        require(hashlib.sha256(log).hexdigest() == checks[name]['log_sha256'] and
                len(log) == checks[name]['log_bytes'] and
                log.decode().splitlines().count('s VERIFIED') == checks[name]['unique_verified'] == 1,
                '858 saved log mismatch')
    original,_ = read(base/'858/near65-v1/result.json')
    second,_ = read(base/'858/near65-independent-v1/second-result.json')
    reconstruction,_ = read(base/'858/near65-independent-v1/reconstruction.json')
    for data in [original,second]:
        require(data.get('solver_exit',20) == 20, '858 solver')
        require(data['checker_exit'] == 0 and data['verified_markers'] == 1, '858 checker')
    cnf = 'f8f5cdead0740948641ea3f025c21a0a37e342eb8ab16968bdf90b022db3ba26'
    proof = 'ace3d9e1479d998fdb883a429803b09e05005b9bc08b276c59838d50054bea05'
    require(reconstruction['cnf_sha256'] == reconstruction['original_cnf_sha256'] ==
            original['cnf_sha256'] == second['cnf_sha256'] == second['cnf_sha256_after'] == cnf, '858 CNF binding')
    require(original['proof_sha256'] == second['proof_sha256_before'] == second['proof_sha256_after'] == proof, '858 proof binding')
    require((original['variables'],original['clauses']) == (reconstruction['variables'],reconstruction['clauses']) == (298421,5187084), '858 reconstruction size')
    return {'status':'PASS_RECEIPT_CONSISTENCY_ONLY','866':{
            'CNF':first['cnf_sha256'],'proof':first['proof_sha256'],
            'variables':manifest['variables'],'clauses':manifest['clauses'],
            'checker_exit':first['checker_returncode'],'reconstruction_same_bytes':True,
            'source_identities':source_records},
            '858':{'CNF':cnf,'proof':proof,'successful_saved_checks':2,
                   'saved_log_hashes_verified':True,'source_identities':source858_records},
            'scope':'Saved historical success fields and log bindings; no new DRAT replay'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=Path,help='Check one normalized seed; infeasibility exits nonzero')
    parser.add_argument('--archive',type=Path,default=Path(__file__).resolve().parents[1]/'archive/nmrs-20261120')
    args = parser.parse_args()
    if args.seed:
        report,_ = seed(args.seed)
        print(json.dumps(report,indent=2))
        return
    root = args.archive.resolve()
    result = {'status':'PASS_BOUNDED_EXACT_REPLAY','window':window(root),
              'arithmetic':arithmetic(),'finite_inputs':[signotope(root/'inputs/signotopes/ambient36.json'),
                               signotope(root/'inputs/signotopes/shared-lock17.json')],
              'scalar':scalar(root),'historical_receipts':receipts(root),
              'scope':'Finite seed predicates, recurrence, arithmetic, two finite colorings, and saved receipt consistency; no theorem audit or omitted DRAT replay'}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

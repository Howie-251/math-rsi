#!/usr/bin/env python3
"""Bounded q=2 trace/composition relaxation; no hypergraph enumeration."""
import itertools as it
import json
import math
from pathlib import Path
from time import process_time

OUT = Path(__file__).resolve().parent
R, B, D, E0 = 3432, 364, 31824, 1794

def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for v in range(n + 1):
            for tail in compositions(n-v, k-1):
                yield (v,) + tail

def perm_mask(m, p):
    return sum(1 << p[i] for i in range(5) if m >> i & 1)

def main():
    t0 = process_time()
    perms = list(it.permutations(range(5)))
    masks = [0] + [m for m in range(1, 32) if m.bit_count() in (2, 3, 4)]
    images = {m: [perm_mask(m, p) for p in perms] for m in masks}
    orbits = {}
    for i, m in enumerate(masks):
        for n in masks[i:]:
            key = min(tuple(sorted((x, y))) for x, y in zip(images[m], images[n]))
            orbits.setdefault(key, 0)
            orbits[key] += 1
    variants = []
    for six in (None, 1821, 1840, 1900, 2616):
        for eight in (None, 4369, 4400):
            name = 'existing' if six is None and eight is None else f'six{six or 0}_eight{eight or 0}'
            variants.append((name, six, eight))
    results = {name: {'six_assumption': six, 'eight_assumption': eight,
                      'hard_labeled_count': 0, 'hard_profile_orbits': [],
                      'max_best_bound_numerator': 0, 'tightest_margin': None}
               for name, six, eight in variants}
    orbit_rows = []
    total = 0
    for orbit_id, ((m, n), trace_labeled_count) in enumerate(sorted(orbits.items())):
        h = tuple(((m >> i) & 1) + ((n >> i) & 1) for i in range(5))
        lower = tuple(6-x for x in h)
        residual = 32-sum(lower)
        # Both exceptional original edges may have the same trace; indexed multiplicity retained.
        exceptions = tuple(sum(E0 if q == 0 else (0 if q >> i & 1 else math.comb(13+q.bit_count(), 11))
                               for q in (m, n)) for i in range(5))
        stab = [p for j,p in enumerate(perms) if tuple(sorted((images[m][j], images[n][j]))) == (m,n)]
        domain_count = 0
        hard_seen = {name:set() for name,_,_ in variants}
        orbit_hard_counts = {name:0 for name,_,_ in variants}
        for extra in compositions(residual, 5):
            a = tuple(lower[i]+extra[i] for i in range(5))
            total += 1
            domain_count += 1
            canonical = None
            base_bounds = [a[i]*R+(32-a[i])*B+exceptions[i] for i in range(5)]
            for name, six, eight in variants:
                numerators = []
                for i in range(5):
                    k = a[i]
                    deduction = max(0, k-1)*120
                    if k >= 7:
                        deduction = max(deduction, (k-7)*120+1770)
                    if six is not None and k >= 6:
                        deduction = max(deduction, (k-6)*120+six)
                    if eight is not None and k >= 8:
                        deduction = max(deduction, (k-8)*120+eight)
                    numerators.append(base_bounds[i]-deduction)
                best = min(numerators)
                res = results[name]
                res['max_best_bound_numerator'] = max(res['max_best_bound_numerator'], best)
                if best < D:
                    margin = D-best
                    if res['tightest_margin'] is None or margin < res['tightest_margin']:
                        res['tightest_margin'] = margin
                    continue
                res['hard_labeled_count'] += 1
                orbit_hard_counts[name] += 1
                if canonical is None:
                    transformed = []
                    for p in stab:
                        row = [0]*5
                        for j in range(5): row[p[j]] = a[j]
                        transformed.append(tuple(row))
                    canonical = min(transformed)
                if canonical in hard_seen[name]:
                    continue
                hard_seen[name].add(canonical)
                # Recompute numerators if a is not canonical to make saved key+bound consistent.
                if a != canonical:
                    cn = []
                    for i,k in enumerate(canonical):
                        deduct = max(0,k-1)*120
                        if k>=7: deduct=max(deduct,(k-7)*120+1770)
                        if six is not None and k>=6: deduct=max(deduct,(k-6)*120+six)
                        if eight is not None and k>=8: deduct=max(deduct,(k-8)*120+eight)
                        cn.append(k*R+(32-k)*B+exceptions[i]-deduct)
                else:
                    cn=numerators
                res['hard_profile_orbits'].append({'trace_orbit':orbit_id,'traces':[m,n],
                    'trace_sizes':[m.bit_count(),n.bit_count()], 'intersection':(m&n).bit_count(),
                    'a':canonical, 'degrees':[1+canonical[i]+h[i] for i in range(5)],
                    'anchor_numerators':cn, 'best':min(cn)})
        orbit_rows.append({'id':orbit_id,'traces':[m,n],
            'trace_sizes':[m.bit_count(),n.bit_count()], 'intersection':(m&n).bit_count(),
            'labeled_trace_pairs':trace_labeled_count,'h':h,'a_lower':lower,
            'residual':residual,'compositions':domain_count,'stabilizer_order':len(stab),
            'exception_numerators':exceptions,'hard_counts':orbit_hard_counts})
    for res in results.values():
        res['hard_orbit_count']=len(res['hard_profile_orbits'])
        res['hard_trace_orbit_ids']=sorted({p['trace_orbit'] for p in res['hard_profile_orbits']})
    assert sum(orbits.values()) == len(masks)*(len(masks)+1)//2 == 351
    assert all(o['compositions'] == math.comb(o['residual']+4,4) for o in orbit_rows)
    # Direct size-pair count cross-check, independent of the S5 orbit reduction.
    direct_weighted = sum(math.comb(6+m.bit_count()+n.bit_count(),4)
                          for i,m in enumerate(masks) for n in masks[i:])
    weighted = sum(o['labeled_trace_pairs']*o['compositions'] for o in orbit_rows)
    assert weighted == direct_weighted
    payload={'status':'necessary_relaxation_only','n':23,'M':35,'F_size':5,'q':2,
        'D':D,'R':R,'B':B,'empty_exception':E0,
        'trace_pair_count':sum(orbits.values()),'trace_orbits':len(orbits),
        'all_trace_pairs_weighted_compositions':weighted,
        'coverage_checks':'trace-pair count, binomial composition counts, direct weighted count PASS',
        'total_labeled_compositions_over_trace_representatives':total,
        'orbits':orbit_rows,'variants':results,'cpu_seconds':process_time()-t0}
    (OUT/'Q2_ANCHOR_PROFILE.json').write_text(json.dumps(payload,indent=2)+'\n')
    lines=['# 23点δ7：qΓ(F)=2的anchor必要域诊断','',
        '本次仅生成两个异常F迹的S5轨道及singleton计数组合，不枚举H、布局或LP。假定扣除列是待证引理条件结论，不能计为已证闭合。','',
        f'完整域：{sum(orbits.values())}个无序带重复迹对，{len(orbits)}个S5轨道；各代表全部下界组合合计{total}。',
        '迹允许空或大小2/3/4；其他32条实际边逐条保留为singleton。下界a_i≥6−h_i，Σa_i=32。',
        '每个anchor唯一红，外18点11红，D=31824；取五个anchor坏上界的最小值。严格通过必须小于D。',
        '现有扣除为(a−1)120，a≥7时可加强为(a−7)120+1770。假定6/8门以同一森林补边给L_k+(a−k)120，只在a≥k使用，和已有界取最大。','',
        '|六集假定|八集假定|hard组合|hard轨道|最坏best/D|',
        '|---:|---:|---:|---:|---:|']
    for name,six,eight in variants:
        r=results[name]
        lines.append(f'|{six or "无"}|{eight or "无"}|{r["hard_labeled_count"]}|{r["hard_orbit_count"]}|{r["max_best_bound_numerator"]}/{D}|')
    lines += ['', '## 现有门的全部四个hard key','',
        '以下每项在异常迹对的稳定子群下取最简a；JSON另保存各假设变体的全部hard key及逐anchor数。','']
    for p in results['existing']['hard_profile_orbits']:
        lines.append(f'- orbit{p["trace_orbit"]}: T={p["traces"]} (sizes{p["trace_sizes"]}, intersection{p["intersection"]}), a={list(p["a"])}, d={p["degrees"]}, bounds={p["anchor_numerators"]}, min={p["best"]}/{D}.')
    lines += ['',
        '六集扣1821恰好消掉前三个空迹剖面：双空迹的a6 anchor从33044减至31823；空+二迹的a6 anchor从32615减至31394。余下两三迹交一点剖面，共同点a8的未扣基数为36192，需扣至少4369才能strict；八集门4369给31823。',
        '所以六集1821与八集4369这两个通用集合引理若均成立，已足够覆盖本q2/δ7整个必要域；更强1840/1900或4400不必作为接口门槛。单补六集（即使1900）仍留两三迹交一点；单补八集（即使4400）仍留三个空迹剖面。','',
        '## 原1900/4400组合的全部hard key','',
        '以下采用六集扣1900、八集扣4400；完整各变体hard列表与逐anchor整数在JSON中。空迹及两三迹交一点均保留，不作不可实现假定。','']
    strongest=results['six1900_eight4400']
    for p in strongest['hard_profile_orbits']:
        lines.append(f'- orbit{p["trace_orbit"]}: T={p["traces"]} (sizes{p["trace_sizes"]}, intersection{p["intersection"]}), a={list(p["a"])}, d={p["degrees"]}, bounds={p["anchor_numerators"]}, min={p["best"]}/{D}.')
    lines += ['', '## 新六集2616假设单独足够','',
        '追加父代理提出的六集扣2616，仅复用相同必要域，不使用任何八集门。全部strict，最大31808/31824，最小余量16。最后两三迹交一点剖面选非共同点anchor，其a6，异常一proper、另一蓝三迹，准确坏数6·3432+26·364+4368−2616=31808。集合引理尚待独立读核，故此为条件结论。专项摘要保存Q2_SIX2616_RESULT.json。','',
        '## 原1900/4400组合结论','',
        ('该必要域在最强所测假设下全部strict；若相应集合引理成立，则此anchor接口足以覆盖固定q2/δ7必要域。' if not strongest['hard_orbit_count'] else
         '仅补所测六/八集合扣除仍不足整类：最强1900/4400假设亦有上述hard输入。它们是必要迹/次数剖面，不是实际H或不可染见证；可能需不同anchor颜色、异常迹共同结构或真实外点容量。'),
        f'CPU {payload["cpu_seconds"]:.6f}秒。']
    (OUT/'Q2_ANCHOR_PROFILE.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k not in ('orbits','variants')}))
    print(json.dumps({k:{q:v for q,v in r.items() if q!='hard_profile_orbits'} for k,r in results.items()}))

if __name__=='__main__':main()

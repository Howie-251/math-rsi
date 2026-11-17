"""Finite free25 analysis; execute only on the authoritative Linux server."""
import csv
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path('/data/ktqiu_hdd/math_agent/reports/n7-h-minus-i-complement-20261112/free25')
color_path = SOURCE / 'colors.tsv'
rows = list(csv.DictReader(color_path.read_text().splitlines(), delimiter='\t'))
colors = {tuple(int(row[k]) for k in ('a', 'b', 'c')): row['color'] for row in rows}
points = tuple(range(1, 26))
P = frozenset((2, 4, 5))
Q = frozenset((14, 19, 20, 22, 23, 25))
core = frozenset(points) - P - Q
HR, HL = frozenset(points) - Q, frozenset(points) - P
J = frozenset((6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18))

def mask(seq):
    return sum(1 << (x - 1) for x in seq)

def mono(seq, color):
    return all(colors[t] == color for t in itertools.combinations(seq, 3))

blue5 = [(seq, mask(seq)) for seq in itertools.combinations(points, 5) if mono(seq, 'B')]
red6 = [(seq, mask(seq)) for seq in itertools.combinations(points, 6) if mono(seq, 'R')]
in_paths = [(seq, bits) for seq, bits in blue5 if set(seq) <= HR]
out_paths = [(seq, bits) for seq, bits in blue5 if set(seq) <= HL]

def supplies(domain):
    bits = mask(domain)
    ends = {seq[-1] for seq, b in in_paths if b & bits == b}
    starts = {seq[0] for seq, b in out_paths if b & bits == b}
    return sorted(J & ends & starts)

safe_cache = {}
def safe(domain):
    bits = mask(domain)
    if bits not in safe_cache:
        safe_cache[bits] = not any(rb & bits == rb for _, rb in red6)
    return safe_cache[bits]

core_blue5 = [seq for seq, _ in blue5 if set(seq) <= core]
core_ends = sorted({seq[-1] for seq in core_blue5})
core_starts = sorted({seq[0] for seq in core_blue5})
cut_table = []
for k in range(26):
    t = k + 0.5
    domain = core | {p for p in P if p > t} | {q for q in Q if q < t}
    old = supplies(domain)
    cut_table.append({'gap_after': k, 't': t, 'domain': sorted(domain), 'old_rows': old,
                      'm': len(old), 'safe': safe(domain)})
best_m = max(row['m'] for row in cut_table)
best = [row for row in cut_table if row['m'] == best_m]

def subsets(pool, nonempty=False):
    pool = sorted(pool)
    for size in range(int(nonempty), len(pool) + 1):
        for seq in itertools.combinations(pool, size):
            yield frozenset(seq)

counter = None
tested = {'best_cuts': len(best), 'core_containing_bases_preserving_all_old_rows': 0,
          'safe_left_extensions': 0, 'safe_extension_pairs': 0}
for row in best:
    t = row['t']
    ft = frozenset(row['domain'])
    old = frozenset(row['old_rows'])
    left = P - ft
    right = Q - ft
    if not left or not right:
        continue
    for private_base in subsets(ft - core):
        G = core | private_base
        if not old <= set(supplies(G)):
            continue
        tested['core_containing_bases_preserving_all_old_rows'] += 1
        for U in subsets(left, True):
            if not safe(G | U):
                continue
            tested['safe_left_extensions'] += 1
            for V in subsets(right, True):
                if not safe(G | V):
                    continue
                tested['safe_extension_pairs'] += 1
                merged = G | U | V
                if not safe(merged):
                    merged_bits = mask(merged)
                    witness = next(seq for seq, rb in red6 if rb & merged_bits == rb)
                    counter = {'cut': row, 'G': sorted(G), 'U': sorted(U), 'V': sorted(V),
                               'red6': witness,
                               'old_in': {str(x): next(seq for seq, b in in_paths
                                   if seq[-1] == x and b & mask(G) == b) for x in sorted(old)},
                               'old_out': {str(x): next(seq for seq, b in out_paths
                                   if seq[0] == x and b & mask(G) == b) for x in sorted(old)}}
                    break
            if counter:
                break
        if counter:
            break
    if counter:
        break

result = {'source': str(color_path), 'source_sha256': hashlib.sha256(color_path.read_bytes()).hexdigest(),
          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope': 'exact 25-point colors; all 5-subsets and 6-subsets checked on Linux; no solver',
          'all_blue5_count': len(blue5), 'all_red6_count': len(red6),
          'core': sorted(core), 'core_blue5': core_blue5,
          'core_blue5_starts': core_starts, 'core_blue5_ends': core_ends,
          'core_J_starts': sorted(J & set(core_starts)), 'core_J_ends': sorted(J & set(core_ends)),
          'cut_table': cut_table, 'best_m': best_m, 'optimal_gaps_after': [r['gap_after'] for r in best],
          'optimal_old_sets': sorted({tuple(r['old_rows']) for r in best}),
          'protected_double_extension_counterexample': counter,
          'counter_search_scope': 'G contains all C0, G subset original optimal Ft, all original old rows supplied in G; U subset omitted P, V subset omitted Q; both nonempty',
          'counter_search_counts': tested,
          'all_red6': [seq for seq, _ in red6]}
(HERE / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ('source_sha256', 'script_sha256', 'all_blue5_count',
    'all_red6_count', 'core_J_starts', 'core_J_ends', 'best_m', 'optimal_gaps_after',
    'optimal_old_sets', 'protected_double_extension_counterexample', 'counter_search_counts')},
    ensure_ascii=False, indent=2))

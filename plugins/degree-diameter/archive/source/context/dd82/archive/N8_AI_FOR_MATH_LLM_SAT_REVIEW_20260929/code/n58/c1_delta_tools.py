#!/usr/bin/env python3
"""Local adapters for the N58 c=1 incremental patch, 2026-09-08.

Standard library only. These routines do NOT invoke a SAT solver, modify a
campaign, canonically classify roots, or establish any new UNSAT result.

Normalized input: H_edges use X indices 0..7; parent_masks has 49 nonzero
8-bit masks in the EXISTING Y order. No sorting/relabeling of Y is performed.
Use a repository adapter to translate these indices to existing primary IDs.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Root:
    H_edges: tuple[tuple[int, int], ...]
    parent_masks: tuple[int, ...]

    @classmethod
    def from_dict(cls, data: dict) -> 'Root':
        edges = []
        for pair in data['H_edges']:
            if len(pair) != 2 or any(type(v) is not int for v in pair):
                raise ValueError('H_edges must contain integer pairs')
            u, v = sorted(pair)
            if not 0 <= u < v < 8:
                raise ValueError('H edge indices must satisfy 0<=u<v<8')
            edges.append((u, v))
        if len(set(edges)) != len(edges):
            raise ValueError('Duplicate H edge')
        parents = tuple(data['parent_masks'])
        if len(parents) != 49 or any(type(m) is not int or not 0 < m < 256 for m in parents):
            raise ValueError('Exactly 49 nonzero 8-bit parent masks required')
        obj = cls(tuple(sorted(edges)), parents)
        if len(obj.H_edges) > 3:
            raise ValueError('Root neighborhood has more than three edges')
        h = obj.H
        for i in range(8):
            if sum(h[i]) + sum((m >> i) & 1 for m in parents) != 7:
                raise ValueError(f'X vertex {i}: root degree/capacity inconsistent')
        if 2 * len(edges) + sum(m.bit_count() - 1 for m in parents) != 7:
            raise ValueError('Root excess budget inconsistent')
        return obj

    @property
    def H(self) -> list[list[int]]:
        h = [[0] * 8 for _ in range(8)]
        for u, v in self.H_edges:
            h[u][v] = h[v][u] = 1
        return h

    def as_dict(self) -> dict:
        return {'H_edges': [list(e) for e in self.H_edges],
                'parent_masks': list(self.parent_masks)}


def fixture_root(edges: Sequence[tuple[int, int]], multi: Sequence[int]) -> Root:
    """Build a LOCAL TEST fixture, not a catalogue or a canonical root generator."""
    if any(type(m) is not int or not 0 < m < 256 or m.bit_count() < 2 for m in multi):
        raise ValueError('multi must contain genuine multi-parent masks')
    h = [0] * 8
    for u, v in edges:
        h[u] += 1
        h[v] += 1
    parents = list(multi)
    for i in range(8):
        n = 7 - h[i] - sum((m >> i) & 1 for m in multi)
        if n < 0:
            raise ValueError('Negative singleton multiplicity')
        parents.extend([1 << i] * n)
    return Root.from_dict({'H_edges': list(edges), 'parent_masks': parents})


def y_row_budgets(root: Root) -> list[dict]:
    """The source report's Eq.(5.1), in existing local Y order.

    Terms refer to K[y,z]. All output coefficients/rhs are exact integers.
    Negative rhs is a contradiction for the FULL rooted extension, not only
    for an extremal-root view.
    """
    p = root.parent_masks
    h = [sum(row) for row in root.H]
    excess = [m.bit_count() - 1 for m in p]
    out = []
    for y, mask in enumerate(p):
        hp = sum(h[i] for i in range(8) if (mask >> i) & 1)
        f = sum(max((mask & m).bit_count() - 1, 0)
                for z, m in enumerate(p) if z != y)
        terms = [{'z': z, 'coefficient': excess[z] + int(bool(mask & m))}
                 for z, m in enumerate(p) if z != y]
        out.append({'y': y, 'degree': 8 - mask.bit_count(),
                    'r_y': excess[y], 'h_parent': hp, 'F_y': f,
                    'rhs': 7 - excess[y] - hp - f, 'terms': terms})
    return out


def budget_propagation(row: dict, fixed: Mapping[int, bool] | None = None) -> dict:
    """Elementary integer propagation using one budget plus exact Y degree.

    fixed maps OTHER local Y indices to actual fixed 0/1 assignments.
    Not a search; no inference about equal degrees within parent classes.
    Returned forbidden edges are conditional on all supplied fixed facts.
    """
    fixed = {} if fixed is None else dict(fixed)
    costs = {x['z']: x['coefficient'] for x in row['terms']}
    if any(z not in costs or type(b) is not bool for z, b in fixed.items()):
        raise ValueError('fixed must map valid other-Y indices to booleans')
    chosen = [z for z, b in fixed.items() if b]
    remaining = [z for z in costs if z not in fixed]
    need = row['degree'] - len(chosen)
    rhs = row['rhs'] - sum(costs[z] for z in chosen)
    reason = None
    if need < 0 or need > len(remaining):
        reason = 'EXACT_DEGREE_INFEASIBLE'
    elif rhs < 0:
        reason = 'BUDGET_ALREADY_EXCEEDED'
    elif sum(sorted(costs[z] for z in remaining)[:need]) > rhs:
        reason = 'CHEAPEST_DEGREE_COMPLETION_EXCEEDS_BUDGET'
    forbidden = []
    if reason is None:
        for z in remaining:
            others = sorted(costs[w] for w in remaining if w != z)
            if need == 0 or need - 1 > len(others) or costs[z] + sum(others[:need-1]) > rhs:
                forbidden.append(z)
    return {'contradiction': reason, 'forbidden_z': forbidden,
            'remaining_degree': need, 'remaining_rhs': rhs,
            'depends_on_fixed': [[z, b] for z, b in sorted(fixed.items())]}


def b5_normal_form(root: Root, target_y: int) -> dict:
    """B5 normal form from the source, not the weaker V4 nonempty matching.

    Allowed z,w must come from the two specified singleton parent classes.
    K[z,w]=0 is CONDITIONAL on both being selected as neighbors of target_y.
    """
    if not 0 <= target_y < 49 or root.parent_masks[target_y].bit_count() != 6:
        raise ValueError('target_y must be a six-parent vertex')
    if root.H_edges:
        return {'target_y': target_y, 'contradiction': 'B5_ROOT_MUST_HAVE_t0',
                'left': [], 'right': [], 'allowed_pairs': []}
    c = root.parent_masks[target_y]
    a, b = [i for i in range(8) if not ((c >> i) & 1)]
    left = [z for z, p in enumerate(root.parent_masks) if p == 1 << a]
    right = [z for z, p in enumerate(root.parent_masks) if p == 1 << b]
    return {'target_y': target_y, 'contradiction': None if left and right else 'EMPTY_B5_DOMAIN',
            'missing_X': [a, b], 'left': left, 'right': right,
            'allowed_pairs': [[z, w] for z in left for w in right],
            'conditional_nonedge': 'K[y,z] AND K[y,w] => NOT K[z,w]'}


def b5_cnf_clauses(root: Root, target_y: int,
                   edge_ids: Mapping[tuple[int, int], int]) -> list[list[int]]:
    """Append-only clauses over EXISTING positive primary K-edge IDs.

    edge_ids covers all 1176 local Y pairs; no auxiliary is allocated.
    An existing general degree encoding is retained, not replaced.
    If the repository has already removed variables, substitute constants
    through its native emitter instead of passing an incomplete edge map.
    """
    keys = set(combinations(range(49), 2))
    if set(edge_ids) != keys:
        raise ValueError('Full existing Y-Y edge map required; use native constant substitution otherwise')
    ids = list(edge_ids.values())
    if any(type(v) is not int or v <= 0 for v in ids) or len(set(ids)) != len(ids):
        raise ValueError('Primary IDs must be distinct positive integers')
    table = b5_normal_form(root, target_y)
    if table['contradiction']:
        return [[]]
    def edge(a: int, b: int) -> int:
        return edge_ids[tuple(sorted((a, b)))]
    left, right = table['left'], table['right']
    eligible = set(left + right)
    clauses = [[-edge(target_y, z)] for z in range(49)
               if z != target_y and z not in eligible]
    for group in (left, right):
        variables = [edge(target_y, z) for z in group]
        clauses.append(variables)
        clauses.extend([[-u, -v] for u, v in combinations(variables, 2)])
    clauses.extend([[-edge(target_y, z), -edge(target_y, w), -edge(z, w)]
                    for z, w in table['allowed_pairs']])
    return clauses


def energy_diagnostics(root: Root) -> dict:
    """Lower bounds for the OPTIONAL max(rho,E,t) view only.

    Diagnostic vertex convention: r=0, Xi=i+1, Yj=j+9. This is NOT a
    permutation to install in an existing encoder. Map through its atom map.
    A failure here excludes this extremal VIEW, not the original rooted graph.
    """
    hmat, parents = root.H, root.parent_masks
    h = [sum(row) for row in hmat]
    excess = [p.bit_count() - 1 for p in parents]
    M = max(h + excess)
    E0 = sum(v*v for v in h + excess)
    t0 = len(root.H_edges)
    lower = [[0] * 58 for _ in range(58)]
    def put(i: int, j: int, val: int) -> None:
        lower[i][j] = lower[j][i] = val
    for i in range(8):
        put(0, i+1, h[i])
    for y, r in enumerate(excess):
        put(0, y+9, r)
    mij = [[sum(bool(p & (1 << i)) and bool(p & (1 << j)) for p in parents)
            for j in range(8)] for i in range(8)]
    for i, j in combinations(range(8), 2):
        value = hmat[i][j] + sum(hmat[i][k]*hmat[k][j] for k in range(8)) + mij[i][j]
        put(i+1, j+1, value)
    for i in range(8):
        for y, p in enumerate(parents):
            a = int(bool(p & (1 << i))) + sum(hmat[i][j] for j in range(8) if (p >> j) & 1)
            put(i+1, y+9, max(a-1, 0))
    for y, z in combinations(range(49), 2):
        put(y+9, z+9, max((parents[y] & parents[z]).bit_count()-1, 0))
    triangle_lb = [t0]
    for i in range(8):
        tau = sum(hmat[i][u] and hmat[i][v] and hmat[u][v]
                  for u, v in combinations(range(8), 2))
        triangle_lb.append(h[i] + tau + sum(mij[i][j] for j in range(8) if hmat[i][j]))
    triangle_lb.extend(sum(bool(p & (1 << u)) and bool(p & (1 << v))
                           for u, v in root.H_edges) for p in parents)
    rows = []
    violations = []
    for v in range(58):
        lb = 7 + sum(b*(b-1) for b in lower[v])
        mx = max(lower[v])
        row = {'vertex_in_diagnostic_order': v, 'repeat_mass_lb': sum(lower[v]),
               'max_repeat_lb': mx, 'energy_lb': lb, 'triangle_lb': triangle_lb[v]}
        rows.append(row)
        if mx > M:
            violations.append({'vertex': v, 'reason': 'MAX_REPEAT_EXCEEDS_ROOT'})
        if lb > E0:
            violations.append({'vertex': v, 'reason': 'ENERGY_EXCEEDS_ROOT'})
        if mx == M and lb == E0 and triangle_lb[v] > t0:
            violations.append({'vertex': v, 'reason': 'TIE_TRIANGLES_EXCEED_ROOT'})
    if M == 1 and t0 == 0:
        violations.append({'vertex': 0, 'reason': 'M1_EXTREMAL_T0_PARITY'})
    return {'scope': 'EXTREMAL_VIEW_ONLY', 'M': M, 'E0': E0, 't0': t0,
            'rows': rows, 'view_violations': violations,
            'may_close_original_root': False}


def _permutation(values: Sequence[int], n: int) -> tuple[int, ...]:
    p = tuple(values)
    if len(p) != n or any(type(v) is not int for v in p) or set(p) != set(range(n)):
        raise ValueError(f'Expected a permutation of range({n})')
    return p


def verify_root_relabeling(old: Root, new: Root, x_old_to_new: Sequence[int],
                          y_old_to_new: Sequence[int]) -> bool:
    """Check a SUPPLIED rooted isomorphism witness. Does not find one.

    This checks H and all 49 parent sets. It DOES NOT check transport of old
    lex leaders, cube side conditions, macro restrictions or solver auxiliaries.
    Therefore it is necessary but insufficient for partial-leaf UNSAT transfer.
    """
    x = _permutation(x_old_to_new, 8)
    y = _permutation(y_old_to_new, 49)
    edges = tuple(sorted(tuple(sorted((x[u], x[v]))) for u, v in old.H_edges))
    if edges != new.H_edges:
        return False
    for j, mask in enumerate(old.parent_masks):
        mapped = sum(1 << x[i] for i in range(8) if (mask >> i) & 1)
        if new.parent_masks[y[j]] != mapped:
            return False
    return True


def map_semantic_edge_cube(cube: Sequence[dict], vertex_old_to_new: Sequence[int]) -> list[dict]:
    """Map edge atoms, never raw auxiliary literal numbers.

    Output is a mapped CUBE, NOT permission to mark it closed. A caller must
    establish base-formula/symmetry/scope implication separately.
    """
    p = _permutation(vertex_old_to_new, 58)
    values: dict[tuple[int, int], bool] = {}
    for atom in cube:
        if atom.get('kind') != 'edge' or type(atom.get('value')) is not bool:
            raise ValueError('Only semantic edge atoms with boolean values are supported')
        u, v = atom['u'], atom['v']
        if type(u) is not int or type(v) is not int or not 0 <= u < v < 58:
            raise ValueError('Expected sorted, distinct graph vertices 0..57')
        pair = tuple(sorted((p[u], p[v])))
        if pair in values and values[pair] != atom['value']:
            raise ValueError('Inconsistent cube')
        values[pair] = atom['value']
    return [{'kind': 'edge', 'u': u, 'v': v, 'value': val}
            for (u, v), val in sorted(values.items())]


def integer_partitions(n: int, bound: int | None = None):
    if n == 0:
        yield ()
        return
    for head in range(min(n, n if bound is None else bound), 0, -1):
        for tail in integer_partitions(n-head, head):
            yield (head,) + tail


def repeat_row_table() -> dict:
    base = list(integer_partitions(7, 5))
    forbidden = {(5, 2), (4, 3)}
    def row(p):
        return {'partition': list(p), 'support_size': len(p), 'rho': max(p),
                'energy': sum(b*b for b in p),
                'threshold_counts': [sum(b >= k for b in p) for k in range(1, 6)]}
    return {'scope': 'c=1; inherited B<=5', 'pure_c1_rows': [row(p) for p in base],
            'working_rows': [row(p) for p in base if p not in forbidden],
            'working_extra_dependencies': ['t0-lambda(5,2) full family RAW_UNSAT',
                                           't0-lambda(4,3) full family RAW_UNSAT'],
            'threshold_energy_coefficients': [1, 3, 5, 7, 9],
            'row_sum_reduced_energy': {'constant': 7, 'q_coefficients': [0, 2, 4, 6, 8]}}


def audit_source_ledger(ledger: dict, audit_text: str | None = None) -> dict:
    c = ledger['preferred_cover']
    by_m: Counter[str] = Counter()
    for row in c['strata']:
        by_m[str(row['M'])] += row['count']
    discrepancies = []
    for m in sorted(set(by_m) | set(c['by_max_B'])):
        if by_m[m] != c['by_max_B'].get(m):
            discrepancies.append({'M': int(m), 'source_summary': c['by_max_B'].get(m),
                                  'sum_of_source_strata': by_m[m]})
    issues = []
    if discrepancies:
        issues.append('BY_M_SUMMARY_DISAGREES_WITH_STRATA')
    if sum(by_m.values()) != c['count_upper_bound']:
        issues.append('TOTAL_DISAGREES_WITH_STRATA')
    if len(c['strata']) != c['coarse_strata_count']:
        issues.append('STRATUM_COUNT_MISMATCH')
    if not c.get('all_18_old_macro_ids_remapped', False):
        issues.append('OLD_MACRO_CLOSURES_NOT_ALL_REMAPPED')
    if audit_text is not None and '2848' not in audit_text and '2,848' not in audit_text:
        issues.append('ATTACHED_AUDIT_DOES_NOT_RECORD_2848_REPRODUCTION')
    return {'scope': 'source arithmetic and provenance only; no theory reproof',
            'source_total': c['count_upper_bound'], 'strata_total': sum(by_m.values()),
            'strata_count': len(c['strata']), 'source_by_M': c['by_max_B'],
            'summed_by_M': dict(by_m), 'discrepancies': discrepancies,
            'issues': issues,
            'extremal_view_gate': 'HOLD_FOR_CATALOGUE_RECONCILIATION' if issues else 'SOURCE_CHECKS_OK',
            'unconditional_patch_on_V4': 'MAY_PROCEED',
            'original_counts': ledger['old_extension_ledger'],
            'real_remote_mapping_performed': False}


def prepare_root(root: Root) -> dict:
    rows = y_row_budgets(root)
    b5 = [b5_normal_form(root, y) for y, p in enumerate(root.parent_masks) if p.bit_count() == 6]
    return {'description': 'Reference patch data; integrate using existing primary atom maps',
            'parent_order_preserved': True, 'original_root': root.as_dict(),
            'unconditional': {'y_budgets': rows,
                              'budget_propagation': [budget_propagation(row) for row in rows],
                              'b5': b5},
            'optional_extremal_view': energy_diagnostics(root),
            'solver_run': False, 'campaign_mutated': False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    s = sub.add_parser('audit-source')
    s.add_argument('--ledger', type=Path, required=True)
    s.add_argument('--audit', type=Path)
    s.add_argument('--out', type=Path, required=True)
    s = sub.add_parser('prepare-root')
    s.add_argument('--input', type=Path, required=True)
    s.add_argument('--out', type=Path, required=True)
    s = sub.add_parser('row-table')
    s.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'audit-source':
        data = audit_source_ledger(json.loads(args.ledger.read_text()),
                                   args.audit.read_text() if args.audit else None)
    elif args.command == 'prepare-root':
        data = prepare_root(Root.from_dict(json.loads(args.input.read_text())))
    else:
        data = repeat_row_table()
    if args.out.exists():
        raise FileExistsError(f'Refusing to overwrite {args.out}; choose a new output path')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'Wrote {args.out}')
    if args.command == 'audit-source':
        for issue in data['issues']:
            print('SOURCE ISSUE:', issue)
        print('No campaign modified; base V4 patch is not blocked.')
        return 2 if data['issues'] else 0
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

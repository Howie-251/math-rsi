"""Deterministic clause encoding of the frozen even FINAL_JOINT_PROBE model."""

from collections import Counter
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path
import sys
import tempfile
from time import monotonic, process_time

from google.protobuf import text_format
from ortools.sat import cp_model_pb2


HERE = Path(__file__).resolve().parent
for name in ('TMP', 'TEMP', 'TMPDIR'):
    os.environ[name] = str(HERE)
tempfile.tempdir = str(HERE)


def neg(literal):
    return not literal if isinstance(literal, bool) else -literal


def tuples_with_sum(maxima, target):
    if not maxima:
        if target == 0:
            yield ()
        return
    rest = maxima[1:]
    first = max(0, target - sum(rest))
    last = min(maxima[0], target)
    for value in range(first, last + 1):
        for suffix in tuples_with_sum(rest, target - value):
            yield (value, *suffix)


class Encoder:
    def __init__(self, domains):
        self.domains = tuple(domains)
        self.num_vars = 0
        self.clauses = []
        self.thresholds = []
        self.equalities = {}
        for low, high in self.domains:
            if low != 0 or not 1 <= high <= 8:
                raise ValueError(f'unsupported variable domain {(low, high)}')
            thresholds = tuple(self.new_var() for _ in range(high))
            self.thresholds.append(thresholds)
            for lower, higher in zip(thresholds, thresholds[1:]):
                self.add((-higher, lower))

    def new_var(self):
        self.num_vars += 1
        return self.num_vars

    def add(self, literals, guards=()):
        clause = []
        seen = set()
        for literal in (*map(neg, guards), *literals):
            if literal is True:
                return
            if literal is False:
                continue
            if -literal in seen:
                return
            if literal not in seen:
                clause.append(literal)
                seen.add(literal)
        self.clauses.append(clause)

    def cp_bool(self, ref):
        index = ref if ref >= 0 else -1-ref
        if self.domains[index] != (0, 1):
            raise ValueError(f'non-boolean literal {ref}')
        lit = self.thresholds[index][0]
        return lit if ref >= 0 else -lit

    @staticmethod
    def at_least(thresholds, value):
        if value <= 0:
            return True
        if value > len(thresholds):
            return False
        return thresholds[value - 1]

    def equal(self, index, value):
        thresholds = self.thresholds[index]
        if not 0 <= value <= len(thresholds):
            return False
        lower = self.at_least(thresholds, value)
        upper = neg(self.at_least(thresholds, value + 1))
        if lower is True:
            return upper
        if upper is True:
            return lower
        key = index, value
        if key not in self.equalities:
            result = self.new_var()
            self.add((-result, lower))
            self.add((-result, upper))
            self.add((result, -lower, -upper))
            self.equalities[key] = result
        return self.equalities[key]

    def prefix_thresholds(self, literals, limit):
        # New threshold is old[j] or (literal and old[j-1]).
        old = ()
        for lit in literals:
            new = []
            for j in range(1, min(len(old) + 1, limit) + 1):
                same = self.at_least(old, j)
                lower = self.at_least(old, j - 1)
                target = self.new_var()
                self.add((neg(same), target))
                self.add((neg(lit), neg(lower), target))
                self.add((-target, same, lit))
                self.add((-target, same, lower))
                new.append(target)
            old = tuple(new)
        return old

    def at_most(self, terms, target, guards):
        maxima = tuple(map(len, terms))
        if target >= sum(maxima):
            return
        for violating in tuples_with_sum(maxima, max(0, target + 1)):
            self.add(tuple(neg(self.at_least(t, v)) for t, v in zip(terms, violating)), guards)

    def complement(self, thresholds):
        return tuple(neg(lit) for lit in reversed(thresholds))

    def outside_value(self, terms, target, guards):
        for choice in tuples_with_sum(tuple(map(len, terms)), target):
            clause = []
            for thresholds, value in zip(terms, choice):
                clause.append(neg(self.at_least(thresholds, value)))
                clause.append(self.at_least(thresholds, value + 1))
            self.add(clause, guards)

    def short_linear(self, variables, coeffs, intervals, guards):
        terms = []
        shift = 0
        for index, coefficient in zip(variables, coeffs):
            thresholds = self.thresholds[index]
            if coefficient < 0:
                shift += len(thresholds)
                thresholds = self.complement(thresholds)
            terms.append(thresholds)
        total = sum(map(len, terms))
        rows = [(max(0, lo + shift), min(total, hi + shift)) for lo, hi in intervals]
        rows = [(lo, hi) for lo, hi in rows if lo <= hi]
        if not rows:
            self.add((), guards)
            return
        self.at_most(terms, rows[-1][1], guards)
        self.at_most([self.complement(t) for t in terms], total - rows[0][0], guards)
        for (_, before), (after, _) in zip(rows, rows[1:]):
            for missing in range(before + 1, after):
                self.outside_value(terms, missing, guards)

    def linear(self, variables, coeffs, domain, guards):
        if len(variables) != len(coeffs) or set(coeffs) - {-1, 1}:
            raise ValueError('unsupported linear coefficients')
        intervals = tuple(zip(domain[::2], domain[1::2]))
        if not domain or len(domain) % 2:
            raise ValueError('empty or invalid linear domain')
        if len(variables) <= 6:
            self.short_linear(variables, coeffs, intervals, guards)
            return

        integers = [i for i in variables if self.domains[i] != (0, 1)]
        if not integers and set(coeffs) == {1} and len(intervals) == 1:
            lo, hi = intervals[0]
            if lo != hi or not 0 <= lo <= len(variables):
                raise ValueError('unsupported wide boolean sum')
            levels = self.prefix_thresholds([self.cp_bool(i) for i in variables], lo + 1)
            self.add((self.at_least(levels, lo),), guards)
            self.add((neg(self.at_least(levels, lo + 1)),), guards)
            return

        if len(integers) == 1 and intervals == ((0, 0),):
            integer = integers[0]
            sign = coeffs[variables.index(integer)]
            source = [(i, a) for i, a in zip(variables, coeffs) if i != integer]
            if source and all(a == -sign for _, a in source):
                levels = self.thresholds[integer]
                computed = self.prefix_thresholds([self.cp_bool(i) for i, _ in source], len(levels) + 1)
                for j, original in enumerate(levels, 1):
                    derived = self.at_least(computed, j)
                    self.add((-original, derived), guards)
                    self.add((original, neg(derived)), guards)
                self.add((neg(self.at_least(computed, len(levels) + 1)),), guards)
                return
        raise ValueError('unrecognized wide linear form')

    def table(self, variables, rows, forbidden, guards):
        selectors = []
        for row in rows:
            values = tuple(self.equal(index, value) for index, value in zip(variables, row))
            if forbidden:
                self.add(tuple(map(neg, values)), guards)
            elif not any(value is False for value in values):
                selector = self.new_var()
                selectors.append(selector)
                for value in values:
                    self.add((-selector, value), guards)
        if not forbidden:
            self.add(selectors, guards)


def encode(proto):
    if proto.HasField('objective') or proto.HasField('floating_point_objective') or proto.assumptions:
        raise ValueError('unsupported objective or assumptions')
    encoder = Encoder(tuple(tuple(v.domain) for v in proto.variables))
    for index, constraint in enumerate(proto.constraints):
        kind = constraint.WhichOneof('constraint')
        guards = tuple(encoder.cp_bool(i) for i in constraint.enforcement_literal)
        try:
            if kind == 'bool_or':
                encoder.add(tuple(encoder.cp_bool(i) for i in constraint.bool_or.literals), guards)
            elif kind == 'linear':
                x = constraint.linear
                encoder.linear(list(x.vars), tuple(x.coeffs), tuple(x.domain), guards)
            elif kind == 'table':
                x = constraint.table
                if x.vars or not x.exprs or any(len(e.vars) != 1 or tuple(e.coeffs) != (1,) or e.offset for e in x.exprs):
                    raise ValueError('unsupported table expression')
                variables = [e.vars[0] for e in x.exprs]
                n = len(variables)
                if len(x.values) % n:
                    raise ValueError('table row width mismatch')
                rows = (x.values[i:i+n] for i in range(0, len(x.values), n))
                encoder.table(variables, rows, x.negated, guards)
            else:
                raise ValueError(f'unsupported constraint type {kind}')
        except ValueError as exc:
            raise ValueError(f'constraint {index} ({kind}): {exc}') from exc
    return encoder


def self_test():
    """Truth-table every input assignment for each reduced encoder template."""
    from pysat.solvers import Minisat22

    total = 0

    def check(maxima, emit, expected):
        nonlocal total
        encoder = Encoder(tuple((0, maximum) for maximum in maxima))
        emit(encoder)
        with Minisat22(bootstrap_with=encoder.clauses) as solver:
            for values in product(*(range(maximum + 1) for maximum in maxima)):
                inputs = [lit if value >= threshold else -lit
                          for levels, value in zip(encoder.thresholds, values)
                          for threshold, lit in enumerate(levels, 1)]
                obtained = solver.solve(assumptions=inputs)
                assert obtained == expected(values), (values, obtained)
                total += 1

    check((3, 2, 3, 1, 1),
          lambda enc: enc.linear([0, 1, 2], (1, -1, 1), (-1, 1, 3, 4),
                                 (enc.cp_bool(3), enc.cp_bool(-5))),
          lambda x: not (x[3] and not x[4]) or x[0]-x[1]+x[2] in {-1, 0, 1, 3, 4})
    check((1, 1, 1),
          lambda enc: enc.add((enc.cp_bool(-1), enc.cp_bool(1)), (enc.cp_bool(2),)),
          lambda x: not x[2] or not x[0] or bool(x[1]))
    check((2, 2, 1, 1),
          lambda enc: enc.table([0, 1], ((0, 1), (2, 0), (3, 1)), False,
                                (enc.cp_bool(2), enc.cp_bool(-4))),
          lambda x: not (x[2] and not x[3]) or x[:2] in {(0, 1), (2, 0)})
    check((2, 2, 1, 1),
          lambda enc: enc.table([0, 1], ((1, 0), (2, 1), (3, 1)), True,
                                (enc.cp_bool(2), enc.cp_bool(-4))),
          lambda x: not (x[2] and not x[3]) or x[:2] not in {(1, 0), (2, 1)})
    check((2, 1, 1, 1, 1, 1, 1, 1),
          lambda enc: enc.linear(list(range(7)), (1, -1, -1, -1, -1, -1, -1), (0, 0),
                                 (enc.cp_bool(7),)),
          lambda x: not x[7] or x[0] == sum(x[1:7]))
    check((1,) * 8,
          lambda enc: enc.linear(list(range(7)), (1,) * 7, (3, 3), (enc.cp_bool(-8),)),
          lambda x: x[7] or sum(x[:7]) == 3)
    print(f'PASS: {total} small truth-table assignments', flush=True)
    return total


def digest(path):
    with path.open('rb') as stream:
        return sha256(stream.read()).hexdigest()


def main():
    started = monotonic()
    cpu = process_time()
    assignments = self_test()
    if sys.argv[1:] == ['test']:
        return
    if sys.argv[1:] != ['build']:
        raise SystemExit('usage: even_cnf.py test|build')

    sys.path.insert(0, str(HERE.parent))
    import FINAL_JOINT_PROBE as source

    model, holes, _ = source.make_model(0)
    source.add_forward_exclusions(model, holes, 0)
    source.add_split_exclusions(model, 0)
    source.add_scalar_reduction(model, 0, source.scalar_rows())
    if error := model.validate():
        raise ValueError(error)
    proto = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    kinds = Counter(c.WhichOneof('constraint') for c in proto.constraints)
    domains = Counter(tuple(v.domain) for v in proto.variables)
    print(f'Constraints {kinds}; domains {domains}', flush=True)
    encoder = encode(proto)
    cnf_path = HERE / 'even.cnf'
    with cnf_path.open('w', encoding='ascii', newline='\n') as stream:
        stream.write(f'p cnf {encoder.num_vars} {len(encoder.clauses)}\n')
        for clause in encoder.clauses:
            stream.write(' '.join(map(str, (*clause, 0))) + '\n')
    pb_path = HERE / 'even.pb'
    pb_path.write_bytes(proto.SerializeToString(deterministic=True))
    map_path = HERE / 'even_map.json'
    mapping = {
        'threshold_meaning': 'Each list is x>=1, x>=2, ..., in CP variable index order.',
        'original_variables': [[variable.name, *encoder.thresholds[i]]
                               for i, variable in enumerate(proto.variables)],
        'extra_equalities': [[i, value, lit] for (i, value), lit in encoder.equalities.items()],
        'other_variables': 'Local cumulative counter coordinates and allowed-table row selectors.',
    }
    map_path.write_text(json.dumps(mapping, separators=(',', ':')) + '\n', encoding='utf-8')
    files = [cnf_path, pb_path, map_path, Path(__file__)]
    inputs = ('FINAL_JOINT_PROBE.py', 'GLOBAL_PROBE.py', 'FREE_A6_JOINT_PROBE.py', 'FREE_A6_SUPPLY.py',
              'SPLIT_SMALL_GLOBAL_PROBE.py', 'SCALAR_NEW_GATES.json', 'PROBE.py')
    stats = {
        'status': 'CNF_BUILT',
        'parity': 0,
        'truth_table_assignments': assignments,
        'constraint_types': kinds,
        'num_cnf_vars': encoder.num_vars,
        'num_cnf_clauses': len(encoder.clauses),
        'sha256': {path.name: digest(path) for path in files},
        'source_sha256': {name: digest(HERE.parent / name) for name in inputs},
        'wall_seconds': monotonic() - started,
        'cpu_seconds': process_time() - cpu,
    }
    (HERE / 'build.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(stats, indent=2), flush=True)


if __name__ == '__main__':
    main()

"""Encode the frozen odd high-weight union model using the frozen even compiler."""

from collections import Counter
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic, process_time

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model

from even_cnf import Encoder, HERE, digest, neg, self_test as test_shared_encoder


class OddEncoder(Encoder):
    def __init__(self, domains):
        self.original_domains = domains
        super().__init__(tuple((0, 1) if domain == (0, 0) else domain for domain in domains))
        for index, domain in enumerate(domains):
            if domain == (0, 0):
                self.add((neg(self.cp_bool(index)),))

    def linear(self, variables, coeffs, domain, guards):
        if len(variables) <= 6 or any(self.domains[i] != (0, 1) for i in variables):
            return super().linear(variables, coeffs, domain, guards)
        if len(variables) != len(coeffs) or set(coeffs) - {-1, 1} or len(domain) != 2:
            raise ValueError('unsupported wide Boolean sum')

        # -x = (1-x)-1. Normalize the sum to nonnegative Boolean literals.
        literals = [self.cp_bool(i if coeff == 1 else -1-i) for i, coeff in zip(variables, coeffs)]
        width = len(literals)
        shift = coeffs.count(-1)
        low = max(0, domain[0] + shift)
        high = min(width, domain[1] + shift)
        if low > high:
            self.add((), guards)
            return

        def cutoff(lo, hi):
            return max(lo, hi + 1 if hi < width else 0)

        # Complement every literal if counting its failures has a smaller cutoff.
        if cutoff(width - high, width - low) < cutoff(low, high):
            literals = list(map(neg, literals))
            low, high = width - high, width - low
        limit = cutoff(low, high)
        if not limit:
            return
        thresholds = self.prefix_thresholds(literals, limit)
        self.add((self.at_least(thresholds, low),), guards)
        if high < width:
            self.add((neg(self.at_least(thresholds, high + 1)),), guards)


def encode(proto):
    if proto.HasField('objective') or proto.HasField('floating_point_objective') or proto.assumptions:
        raise ValueError('unsupported objective or assumptions')
    encoder = OddEncoder(tuple(tuple(v.domain) for v in proto.variables))
    for index, constraint in enumerate(proto.constraints):
        kind = constraint.WhichOneof('constraint')
        guards = tuple(encoder.cp_bool(i) for i in constraint.enforcement_literal)
        try:
            if kind == 'bool_or':
                encoder.add(tuple(encoder.cp_bool(i) for i in constraint.bool_or.literals), guards)
            elif kind == 'linear':
                linear = constraint.linear
                encoder.linear(list(linear.vars), tuple(linear.coeffs), tuple(linear.domain), guards)
            elif kind == 'table':
                table = constraint.table
                if table.vars or not table.exprs or any(len(e.vars) != 1 or tuple(e.coeffs) != (1,) or e.offset for e in table.exprs):
                    raise ValueError('unsupported table expression')
                variables = [e.vars[0] for e in table.exprs]
                width = len(variables)
                if len(table.values) % width:
                    raise ValueError('table row width mismatch')
                rows = (table.values[i:i+width] for i in range(0, len(table.values), width))
                encoder.table(variables, rows, table.negated, guards)
            else:
                raise ValueError(f'unsupported constraint type {kind}')
        except ValueError as exc:
            raise ValueError(f'constraint {index} ({kind}): {exc}') from exc
    return encoder


def self_test():
    from pysat.solvers import Minisat22

    num_tested = 0
    examples = (
        ((1,) * 8, (-100, 2)),
        ((1, 1, -1, -1, -1, -1, -1, -1), (0, 1)),
        ((1, 1, -1, -1, -1, -1, -1, -1), (-4, -1)),
        ((1, 1, -1, -1, -1, -1, -1, -1), (3, 4)),
        ((-1,) * 8, (-100, 100)),
    )
    for coefficients, interval in examples:
        domains = ((0, 1),) * 10 + ((0, 0),)
        encoder = OddEncoder(domains)
        guards = encoder.cp_bool(8), encoder.cp_bool(-10)
        encoder.linear(list(range(8)), coefficients, interval, guards)
        encoder.add((encoder.cp_bool(0),), (encoder.cp_bool(10),))
        with Minisat22(bootstrap_with=encoder.clauses) as solver:
            for values in product((0, 1), repeat=11):
                assumptions = [encoder.cp_bool(i if val else -1-i) for i, val in enumerate(values)]
                amount = sum(val * coeff for val, coeff in zip(values, coefficients))
                expected = not values[10] and (not (values[8] and not values[9]) or interval[0] <= amount <= interval[1])
                actual = solver.solve(assumptions=assumptions)
                assert actual == expected, (coefficients, interval, values, actual)
                num_tested += 1
    print(f'PASS: {num_tested} wide signed bounded and constant truth-table assignments', flush=True)
    return num_tested


def main():
    wall, cpu = monotonic(), process_time()
    if sys.argv[1:] not in (['test'], ['build']):
        raise SystemExit('usage: odd_cnf.py test|build')
    reuse_hash = digest(HERE / 'even_cnf.py')
    assert reuse_hash == json.loads((HERE / 'build.json').read_text(encoding='utf-8'))['sha256']['even_cnf.py']
    shared = test_shared_encoder()
    new = self_test()
    if sys.argv[1] == 'test':
        return

    source = HERE.parent / 'ODD_DGE26_STRUCTURED_FULL.pb'
    proto = cp_model_pb2.CpModelProto.FromString(source.read_bytes())
    wrapper = cp_model.CpModel()
    assert wrapper.proto.parse_text_format(text_format.MessageToString(proto))
    if error := wrapper.validate():
        raise ValueError(error)
    kinds = Counter(c.WhichOneof('constraint') for c in proto.constraints)
    domains = Counter(tuple(v.domain) for v in proto.variables)
    print(f'Constraints {kinds}; domains {domains}', flush=True)
    enc = encode(proto)
    cnf = HERE / 'odd.cnf'
    with cnf.open('w', encoding='ascii', newline='\n') as stream:
        stream.write(f'p cnf {enc.num_vars} {len(enc.clauses)}\n')
        for clause in enc.clauses:
            stream.write(' '.join(map(str, (*clause, 0))) + '\n')
    mapping = HERE / 'odd_map.json'
    mapping.write_text(json.dumps({
        'threshold_meaning': 'Each list is x>=1, x>=2, ..., in CP variable index order. Constant zero is pinned by a negative unit.',
        'original_variables': [[v.name, *enc.thresholds[i]] for i, v in enumerate(proto.variables)],
        'extra_equalities': [[i, value, lit] for (i, value), lit in enc.equalities.items()],
        'other_variables': 'Local cumulative counter coordinates and allowed-table row selectors.',
    }, separators=(',', ':')) + '\n', encoding='utf-8')
    result = {
        'status': 'CNF_BUILT',
        'branch': 'odd_high_weight_union',
        'truth_table_assignments': {'shared': shared, 'wide_signed_and_constant': new},
        'constraint_types': kinds,
        'domains': {str(k): v for k, v in domains.items()},
        'num_cnf_vars': enc.num_vars,
        'num_cnf_clauses': len(enc.clauses),
        'sha256': {path.name: digest(path) for path in (source, cnf, mapping, Path(__file__), HERE / 'even_cnf.py')},
        'wall_seconds': monotonic() - wall,
        'cpu_seconds': process_time() - cpu,
    }
    (HERE / 'build_odd.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()

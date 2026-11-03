"""Append proved port clauses to saved inputs; never rebuild the baseline."""
import argparse
import importlib.util
from itertools import product
import json
from pathlib import Path
import shutil
import sys
import time

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
CASES = ('r1_h0_b0', 'r2_h0_b1')
SCOPE = ('Complete original-A order61 internal-double case with appended proved '
         'port consequences; the checked common-attachment exclusion leaves '
         'these two types, without choosing a port or freezing an interface')
FINAL_PORT_PROOF = 'proofs/dd82/n61/INTERNAL_DOUBLE_FINAL_PORT_CONSEQUENCES.md'
COMMON_PROOF = 'proofs/dd82/n61/INTERNAL_DOUBLE_COMMON_ATTACHMENT_EXCLUSION.md'


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def import_parent():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('internal_double_parent_decode', PARENT / 'encode.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def evaluate(clauses, values):
    return all(any(values[abs(literal)] == (literal > 0) for literal in clause)
               for clause in clauses)


def make_delta(case, normalization, constraints, variables):
    """Read already exact actual-B bits; allocate no variables."""
    norm = normalization
    groups = {int(t): row for t, row in norm['groups'].items()}
    ordinary = {int(t): row for t, row in norm['ordinary'].items()}
    parent = {z: t for t, row in groups.items() for z in row}
    assert set(parent) == set(norm['Z']) and len(parent) == 50
    records = [row for row in constraints['records']
               if row['kind'] == 'all_Z_endpoint_actual_B_bounds']
    bits = {tuple(row['pair']): row['actual_B_threshold_bits'] for row in records}
    assert len(bits) == len(records) == 100
    u, w = norm['u'], norm['w']
    assert set(bits) == {(endpoint, z) for endpoint in (u, w) for z in norm['Z']}
    clauses, obligations = [], []
    if case == 'r1_h0_b0':
        assert (norm['r'], norm['h'], norm['beta']) == (1, 0, 0)
        counts, constant_false = {}, 0
        for endpoint, subset in ((u, set(norm['U'])), (w, set(norm['W']))):
            selected = [z for z in norm['Z'] if parent[z] not in subset]
            assert len(selected) == 33
            counts[endpoint] = len(selected)
            for z in selected:
                second_bit = bits[(endpoint, z)][1]
                row = dict(pair=[endpoint, z], parent=parent[z],
                           actual_B_second_threshold=second_bit,
                           kind='double_endpoint_port_parent_outside_endpoint_T_neighbors')
                if second_bit is False:
                    constant_false += 1
                    row.update(status='already_constant_false', delta_clause=None)
                elif second_bit is True:
                    # A true exact B2 would contradict the new necessary
                    # condition; preserving that condition means an empty clause.
                    clauses.append([])
                    row.update(status='constant_true_contradiction', delta_clause=len(clauses))
                else:
                    clauses.append([-second_bit])
                    row.update(status='negative_unit', delta_clause=len(clauses))
                    # Exhaust the one relevant Boolean: the emitted unit is
                    # true precisely when the already defined B2 bit is false.
                    for value in (False, True):
                        assert evaluate([clauses[-1]], {second_bit: value}) == (not value)
                obligations.append(row)
        assert len(obligations) == 66
        sanity = dict(status='PASSED', kind='r1_parent_domain_B2_units',
                      parent_positions_per_endpoint=counts,
                      pre_simplification_conditions=66, constant_false_conditions=constant_false,
                      emitted_clauses=len(clauses),
                      proof_dependency='Universal h=0 for the new consecutive triple v,u,z or v,w,z')
    else:
        assert case == 'r2_h0_b1' and (norm['r'], norm['h'], norm['beta']) == (2, 0, 1)
        c_set, d_set = set(norm['U']) - set(norm['W']), set(norm['W']) - set(norm['U'])
        assert len(c_set) == len(d_set) == 1
        c, d = next(iter(c_set)), next(iter(d_set))
        qset, pset = set(norm['Q']) & set(groups[c]), set(norm['P']) & set(groups[d])
        assert len(qset) == len(pset) == 1
        q0, p0 = next(iter(qset)), next(iter(pset))
        oc, od = set(ordinary[c]), set(ordinary[d])
        assert len(oc) == len(od) == 5 and not oc & od
        x_domain, y_domain = sorted({q0} | oc | od), sorted({p0} | oc | od)
        assert len(x_domain) == len(y_domain) == 11
        allowed = {(q0, p0)} | set(product(oc, od)) | set(product(od, oc))
        assert len(allowed) == 51
        x_bits = {x: bits[(u, x)][0] for x in x_domain}
        y_bits = {y: bits[(w, y)][0] for y in y_domain}
        # The saved reviewed input has 22 distinct nonconstant exact bits.
        assert all(type(bit) is int for bit in list(x_bits.values()) + list(y_bits.values()))
        assert len(set(x_bits.values()) | set(y_bits.values())) == 22
        for x, y in product(x_domain, y_domain):
            if (x, y) in allowed:
                continue
            clauses.append([-x_bits[x], -y_bits[y]])
            obligations.append(dict(kind='forbidden_coupled_unit_ports', x=x, y=y,
                               actual_B_u_x_first_threshold=x_bits[x],
                               actual_B_w_y_first_threshold=y_bits[y], delta_clause=len(clauses)))
        assert len(clauses) == len(obligations) == 70
        accepted = []
        # The parent input already requires exactly one unit port in each
        # eleven-element domain. Check every one of its 121 ordered choices.
        for x, y in product(x_domain, y_domain):
            values = {bit: vertex == x for vertex, bit in x_bits.items()}
            values.update({bit: vertex == y for vertex, bit in y_bits.items()})
            passed = evaluate(clauses, values)
            assert passed == ((x == q0 and y == p0)
                              or (x in oc and y in od) or (x in od and y in oc))
            if passed:
                accepted.append([x, y])
        assert len(accepted) == 51
        sanity = dict(status='PASSED', kind='r2_all_coupled_port_choices',
                      q0=q0, p0=p0, O_c=sorted(oc), O_d=sorted(od),
                      x_domain=x_domain, y_domain=y_domain,
                      one_hot_assignments_checked=121, allowed_pairs=accepted,
                      allowed_count=51, forbidden_count=70, emitted_clauses=70)
    assert all(type(literal) is int and 1 <= abs(literal) <= variables
               for clause in clauses for literal in clause)
    return clauses, obligations, sanity


def append_and_compare(source_path, target_path, variables, parent_clauses, additions):
    """Copy every baseline body byte; reread linewise to verify the prefix."""
    new_count = parent_clauses + len(additions)
    added_lines = [(' '.join(map(str, clause)) + ' 0\n').encode('ascii') for clause in additions]
    with source_path.open('rb') as source, target_path.open('wb') as target:
        assert source.readline().split() == [b'p', b'cnf', str(variables).encode(), str(parent_clauses).encode()]
        target.write(f'p cnf {variables} {new_count}\n'.encode('ascii'))
        body_lines = 0
        for line in source:
            target.write(line)
            body_lines += 1
        assert body_lines == parent_clauses
        target.writelines(added_lines)
    with source_path.open('rb') as source, target_path.open('rb') as target:
        source.readline()
        assert target.readline() == f'p cnf {variables} {new_count}\n'.encode('ascii')
        compared = 0
        for line in source:
            assert target.readline() == line
            compared += 1
        for line in added_lines:
            assert target.readline() == line
        assert target.read() == b'' and compared == parent_clauses
    return dict(status='PASSED', comparison='Every baseline body line compared as bytes; '
                'then every appended clause and EOF checked', parent_body_lines=compared,
                added_clauses=len(additions), variables_unchanged=True,
                new_variables=0, total_clauses=new_count)


def prepare(case):
    started_cpu, started_wall = time.process_time(), time.monotonic()
    source, target = PARENT / case, HERE / case
    target.mkdir(exist_ok=True)
    assert not (target / 'input.cnf').exists() and not (target / 'encoding.json').exists(), 'Preserve prepared input'
    parent_encoding = json.loads((source / 'encoding.json').read_text())
    norm = json.loads((source / 'normalization.json').read_text())
    constraints = json.loads((source / 'constraints.json').read_text())
    assert parent_encoding['case'] == norm['case'] == case and parent_encoding['n'] == 61
    variables, old_clauses = parent_encoding['variables'], parent_encoding['clauses']
    additions, obligations, sanity = make_delta(case, norm, constraints, variables)
    prefix = append_and_compare(source / 'input.cnf', target / 'input.cnf', variables, old_clauses, additions)
    # These two unchanged maps suffice for graph decoding and labeling review.
    for filename in ('edge_variables.json', 'normalization.json'):
        shutil.copyfile(source / filename, target / filename)
    for row in obligations:
        if row['delta_clause'] is not None:
            row['actual_clause_id'] = old_clauses + row['delta_clause']
    save(target / 'delta_constraints.json', dict(parent_constraints=str(source / 'constraints.json'),
         clauses=additions, obligations=obligations))
    save(target / 'delta_sanity.json', dict(boolean_conditions=sanity, parent_body=prefix,
         baseline_rebuilt=False, solver_calls=0))
    result = dict(parent_encoding)
    dependencies = list(parent_encoding['mathematical_dependencies']) + [FINAL_PORT_PROOF]
    if case == 'r1_h0_b0':
        dependencies.append(COMMON_PROOF)
    result.update(status='PREPARED_NOT_RUN', solver_calls=0, scope=SCOPE,
         variables=variables, clauses=old_clauses + len(additions),
         parent_input=str(source / 'input.cnf'), parent_encoding=str(source / 'encoding.json'),
         parent_clause_count=old_clauses, appended_clause_count=len(additions),
         new_variables=0, baseline_rebuilt=False, parent_body_byte_comparison='PASSED',
         source_semantic_sanity='Parent semantic sanity inherited; appended Boolean conditions checked separately',
         delta_boolean_sanity=sanity['status'],
         small_sanity='Only appended conditions checked; baseline sanity suites not rerun',
         mathematical_dependencies=dependencies,
         cnf_bytes=(target / 'input.cnf').stat().st_size,
         review_status='Root-managed reused source delta and mathematical reviews',
         preparation_cpu_seconds=time.process_time() - started_cpu,
         preparation_wall_seconds=time.monotonic() - started_wall)
    save(target / 'encoding.json', result)
    print(json.dumps(result, indent=2))


def decode(case, log_path=None):
    parent = import_parent()
    parent.HERE = HERE
    parent.decode(case, log_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--case', choices=CASES, required=True)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    prepare(args.case) if args.action == 'prepare' else decode(args.case, args.log)

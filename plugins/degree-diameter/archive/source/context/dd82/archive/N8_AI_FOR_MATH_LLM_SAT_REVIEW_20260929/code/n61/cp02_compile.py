#!/usr/bin/env python3
"""Append only I12.18 to frozen CP01 INSIDE; never submit or solve."""
import argparse
import json
import resource
import time
from pathlib import Path
from cp02_common import (ROUND, CP01, SNAPSHOT, CNF, VERSION, CONSTRAINTS,
                         QUESTION, add_W_le5)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    source = CP01 / 'generated/inside.cnf'
    source_map = CP01 / 'generated/inside.map.json'
    # One direct comparison establishes that the live source is the supplied
    # CP01 input, not a later similarly named formula. No digests are used.
    for relative in ('generated/inside.cnf', 'generated/inside.map.json',
                     'code/i12_compile.py'):
        if (CP01 / relative).read_bytes() != (SNAPSHOT / relative).read_bytes():
            raise ValueError(f'CP01 differs from the supplied frozen input: {relative}')
    gm = json.loads(source_map.read_text())
    if (gm['encoding_version'] != 'n61_i12_cp01_r1_increment_v1'
            or gm['n'] != 61 or gm['no_O_encoded'] is not False):
        raise ValueError('requires the exact CP01 necessary-condition INSIDE input')
    c = CNF(gm['cnf_variables'])
    ge6 = add_W_le5(c, gm['exact_W_literals'])
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / 'inside.cnf'
    count = 0
    with source.open() as src, target.open('x') as dst:
        dst.write(f'c {VERSION}: CP01 INSIDE plus I12.18 under H/global not-O\n')
        dst.write(f'p cnf {c.pool.top} {gm["cnf_clauses"] + len(c.clauses)}\n')
        for line in src:
            if line.startswith('p '):
                assert list(map(int, line.split()[2:])) == [gm['cnf_variables'], gm['cnf_clauses']]
            elif line.strip() and not line.startswith('c'):
                dst.write(line)
                count += 1
        assert count == gm['cnf_clauses']
        for clause in c.clauses:
            dst.write(' '.join(map(str, clause)) + ' 0\n')
    inherited_variables = gm['cnf_variables']
    gm.update(encoding_version=VERSION, research_round='I12_CP02', package_revision='r1',
              parent_cnf=str(source), parent_variable_map=str(source_map),
              strengthened_cnf=str(target), cnf_variables=c.pool.top,
              cnf_clauses=count + len(c.clauses), enabled_constraints=CONSTRAINTS,
              CP02_W_count_ge6_literal=ge6, CP02_W_count_upper_bound=5,
              CP02_R_connected_encoded=False, CP02_pairing_kernels_encoded=False,
              calculation_question=QUESTION)
    (output / 'inside.map.json').write_text(json.dumps(gm, indent=2) + '\n')
    job = dict(job_id='I12_CP02_inside_Wle5', source_template='I10_B_inside',
               case_key=dict(round='I12_CP02', mode='inside',
                             scope='H_G_B_inside_global_notO_necessary_consequences'),
               cnf='inside.cnf', variable_map='inside.map.json',
               variable_map_schema=gm['schema_version'], encoding_version=VERSION,
               mode='noO_necessary_condition_relaxation', conditional_c1=False,
               theory_flags=CONSTRAINTS, representative_of=[], result_status='unknown',
               seed=0, calculation_question=QUESTION, O15_closed=False,
               full_no_O_encoded=False, parent_job_id='I12_CP01_inside',
               parent_encoding_version='n61_i12_cp01_r1_increment_v1')
    (output / 'jobs.jsonl').write_text(json.dumps(job) + '\n')
    usage = resource.getrusage(resource.RUSAGE_SELF)
    report = dict(encoding_version=VERSION, round='I12_CP02', package_revision='r1',
                  question=QUESTION, enabled_constraints=CONSTRAINTS,
                  parent_cnf=str(source), parent_variable_map=str(source_map),
                  CP01_matches_supplied_snapshot=True, parent_clauses_preserved=count,
                  parent_variables=inherited_variables, variables=c.pool.top,
                  clauses=count + len(c.clauses), added_variables=c.pool.allocated,
                  added_clauses=len(c.clauses), cnf_bytes=target.stat().st_size,
                  W_true_vertices=[v for v, x in enumerate(gm['exact_W_literals']) if x is True],
                  W_false_vertices=[v for v, x in enumerate(gm['exact_W_literals']) if x is False],
                  MATCH='unchanged; no job generated', production_run_started=False,
                  generation_resources=dict(wall_seconds=time.monotonic()-started,
                      process_user_seconds=usage.ru_utime, process_system_seconds=usage.ru_stime,
                      peak_rss_KiB=usage.ru_maxrss))
    (output / 'build_report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

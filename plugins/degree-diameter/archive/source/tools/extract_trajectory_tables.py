#!/usr/bin/env python3
"""Export recorded experiment trajectories and raw timing fields, without summing them."""
import argparse
import csv
import json
from pathlib import Path
import re


def timing_fields(value, prefix=''):
    result = {}
    if isinstance(value, dict):
        for key, child in value.items():
            path = f'{prefix}.{key}' if prefix else key
            lower = key.lower()
            timing = ('cpu' in lower or 'wall' in lower or 'elapsed' in lower
                      or 'duration' in lower or lower in {'seconds', 'time_seconds'})
            if timing and not isinstance(child, (dict, list)):
                result[path] = child
            if isinstance(child, (dict, list)):
                result.update(timing_fields(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            if isinstance(child, (dict, list)):
                result.update(timing_fields(child, f'{prefix}[{index}]'))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'guide')
    args = parser.parse_args()
    source = args.source_root / 'research-wiki/DDP_METHOD_LEDGER.json'
    ledger = json.loads(source.read_text())
    args.output.mkdir(parents=True, exist_ok=True)
    trajectory = []
    times = []
    for row in ledger['rows']:
        raw = row.get('source_record') or {}
        goal = row.get('goal') or {}
        match = re.search(r'(20\d{6})(?:$|[^0-9])', row['id'])
        date = raw.get('date') or (match.group(1) if match else '')
        duration = raw.get('duration_raw')
        evidence = row.get('evidence_paths') or []
        trajectory.append({
            'id': row['id'], 'recorded_or_id_date': date, 'title': row.get('title'),
            'method_family': row.get('method_family'), 'degree_target': goal.get('Delta'),
            'diameter_target': goal.get('D'), 'saved_baseline': goal.get('savedL'),
            'baseline_date': goal.get('baseline_date'), 'object_level': row.get('object_level'),
            'actual_order': row.get('actual_order'), 'hypothetical_order': row.get('hypothetical_order'),
            'actual_diameter': row.get('actual_diameter'), 'status': row.get('status'),
            'exact_scope': row.get('exact_scope'), 'actual_result_or_distance': row.get('distance_text'),
            'positive_guarantees': json.dumps(row.get('positive_guarantees'), ensure_ascii=False),
            'remaining_gap': row.get('remaining_gap'), 'lesson': row.get('lesson'),
            'restart_condition': row.get('restart_condition'), 'duration_raw': duration,
            'wiki_path': row.get('wiki_path'), 'evidence_paths': '\n'.join(evidence),
            'full_record_location': f'research-wiki/DDP_METHOD_LEDGER.json :: {row["id"]}'})
        times.append({
            'id': row['id'], 'recorded_or_id_date': date, 'title': row.get('title'),
            'duration_raw': duration, 'hardware_raw': raw.get('hardware_raw'),
            'recorded_timing_fields_json': json.dumps(timing_fields(row), ensure_ascii=False),
            'evidence_paths': '\n'.join(evidence), 'wiki_path': row.get('wiki_path'),
            'interpretation': '原字段保留；包含预算/累计/分项/重叠时段，不能直接相加；空值不代表零耗时。'})
    for name, rows in [('trajectory_index.csv', trajectory), ('timings_by_experiment.csv', times)]:
        with (args.output / name).open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps({'research_records': len(trajectory),
                      'nonempty_duration_raw': sum(bool(r['duration_raw']) for r in times),
                      'records_with_any_timing_fields': sum(r['recorded_timing_fields_json'] != '{}' for r in times),
                      'summed_research_seconds': None}, ensure_ascii=False))


if __name__ == '__main__':
    main()

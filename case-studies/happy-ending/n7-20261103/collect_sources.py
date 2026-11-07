"""Inventory linked Markdown proofs and the previous 756 evidence handoff."""

import hashlib
import json
import re
from collections import deque
from pathlib import Path
from urllib.parse import unquote


REPORT = Path(__file__).resolve().parent
REPO = REPORT.parents[1]
RESEARCH = REPO / '.trellis/tasks/10-19-nr7-structure-capacity/research'
OLD = REPO / 'reports/n756-professor-review-20261027'
ROOTS = [REPO / 'RESEARCH_SYNTHESIS_N7_20261103_UPPER_BOUND_UPDATE.md', *(
    RESEARCH / name for name in (
        'N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md',
        'N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md',
        'N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md',
        'N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md',
        'N7_THROUGH_CLIQUE_COUNTERFAMILY_AND_LOWER_PARAMETER_FRONTIER_20261103.md',
    )
)]
LINK = re.compile(r'\[([^\]\n]*)\]\(\s*(?:<([^>\n]+)>|([^\s()]+))')
ADMIN = re.compile(r'DOCUMENT_(?:RECEIPT|CHECK)|ENGINEERING_(?:NOTE|REPORT|CHECK)|EXECUTION_(?:REPORT|UNAVAILABLE)|^(?:AGENTS|README|PRD|TASK|WORKFLOW|WORKLOG|JOURNAL|README_TASK|DESIGN|IMPLEMENT|STAGE_SUMMARY)\.md$|(?:^|_)ADMIN(?:_|\.)', re.I)


def repo_path(path):
    return path.relative_to(REPO).as_posix()


def describe(path):
    data = path.read_bytes()
    return {'source_path': repo_path(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def markdown_target(source, raw):
    value = unquote(raw).split('#', 1)[0]
    value = re.sub(r'(?<=\.md):\d+(?::\d+)?$', '', value, flags=re.I)
    if not value.lower().endswith('.md') or re.match(r'https?://', value, re.I):
        return None
    path = (source.parent / value).resolve()
    if not path.is_relative_to(REPO):
        return None
    return path


def proof_inventory(roots=None):
    roots = [path.resolve() for path in (roots or ROOTS)]
    queue = deque(roots)
    seen = set()
    rows, edges, skipped = [], [], []
    while queue:
        path = queue.popleft().resolve()
        if path in seen:
            continue
        seen.add(path)
        rows.append({**describe(path), 'kind': 'selected-root' if path in roots else 'linked-markdown'})
        for match in LINK.finditer(path.read_text(encoding='utf-8-sig')):
            label, angle_target, bare_target = match.groups()
            target = markdown_target(path, angle_target or bare_target)
            if target is None:
                continue
            edge = {'from': repo_path(path), 'to': repo_path(target), 'label': label}
            if ADMIN.search(target.name) or target.relative_to(REPO).parts[0] == '.aris':
                skipped.append({**edge, 'reason': 'administrative receipt or log'})
            elif not target.is_file():
                skipped.append({**edge, 'reason': 'not present at the cited local path'})
            else:
                edges.append(edge)
                queue.append(target)
    return {'files': rows, 'links': edges, 'excluded_or_unresolved': skipped}


def capacity_inventory():
    manifest = json.loads((OLD / 'evidence-manifest.json').read_text(encoding='utf-8'))
    rows = []
    for item in manifest['files']:
        if not item['local_available']:
            continue
        file = OLD / item['packaged_path']
        row = describe(file)
        row['published_hash_matches'] = row['sha256'] == item['sha256']
        row['capacity_group'] = item['evidence']
        row['historical_original_path'] = item['source_path']
        rows.append(row)
    extras = [
        '55-case-register.csv', '55-case-register.json', 'case-register-validation.json',
        'color.tsv', 'verify_color.py', 'verification.json', 'portable-verification.json',
        'evidence-manifest.json',
    ]
    return {'manifest_items': rows, 'additional_files': [describe(OLD / name) for name in extras]}


def main():
    proofs = proof_inventory()
    capacity = capacity_inventory()
    path = REPORT / 'working/proof-candidates.json'
    path.write_text(json.dumps({'proofs': proofs, 'capacity_756': capacity}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Proof Markdown', len(proofs['files']), sum(row['bytes'] for row in proofs['files']))
    print('Excluded/unresolved links', len(proofs['excluded_or_unresolved']))
    for row in proofs['files']:
        print(row['bytes'], row['source_path'])
    for key, rows in capacity.items():
        print('756', key, len(rows), sum(row['bytes'] for row in rows))
    print('Manifest hash mismatches:', [r['source_path'] for r in capacity['manifest_items'] if not r['published_hash_matches']])
    print(path)


if __name__ == '__main__':
    main()

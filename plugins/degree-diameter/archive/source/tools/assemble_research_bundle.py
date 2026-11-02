#!/usr/bin/env python3
"""Assemble the recorded research sources under the user's 100 MB ZIP limit.

This copies existing research data. It does not run a search, solver, graph
validator, model, or Lean build. Large regenerable outputs are accounted for in
the archive-scope note rather than silently presented as embedded evidence.
"""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import shutil
import time
import zipfile
import zlib

ROOTS = ['research-wiki', 'context', 'research', 'computations', 'proofs',
         'reviews', 'review-stage', 'literature', 'N8', 'formal', 'prompts']
SKIP_DIRS = {'.git', '.lake', '__pycache__', '.venv', 'node_modules', 'build',
             'deps', '.ipynb_checkpoints', '.compiled'}
SOURCE = {'.py', '.cpp', '.cc', '.c', '.h', '.hpp', '.lean', '.sh', '.toml',
          '.yaml', '.yml', '.bib', '.tex', '.sage', '.ipynb', '.smt2', '.opb', '.lp'}
TEXT = {'.md', '.rst', '.txt', '.log', '.out', '.err', '.stdout', '.stderr',
        '.html', '.htm', '.json', '.jsonl', '.csv', '.tsv', '.sol', '.sat',
        '.adjlist', '.adj', '.g6', '.s6', '.cnf', '.lrat', '.drat', '.proof'}
SMALL_ASSETS = {'.pdf', '.svg', '.png', '.jpg', '.jpeg', '.gz', '.xz', '.zip', '.docx'}


def compressed_size(path):
    compressor = zlib.compressobj(9, zlib.DEFLATED, -15)
    total = 0
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            total += len(compressor.compress(block))
    return total + len(compressor.flush())


def source_files(root):
    for name in ROOTS:
        for here, dirs, files in os.walk(root / name):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in files:
                path = Path(here) / name
                if path.is_file():
                    yield path
    # Human-facing delivery summaries are retained; their repeated attachments
    # already have their original research/formal sources in the roots above.
    for path in (root / 'expert_review_current').iterdir():
        if path.is_file() and path.suffix.lower() in TEXT | {'.pdf', '.docx'}:
            yield path


def classify(path, relative, size, evidence, graph_files, guide_sources):
    suffix = path.suffix.lower()
    name = path.name.lower()
    if re.fullmatch(r'core\.\d+', name) or name == 'core':
        return None, '进程崩溃转储'
    if suffix in {'.olean', '.ilean', '.o', '.a', '.so', '.exe'}:
        return None, '编译产物；自有源码保留'
    if 'checksum' in name or name in {'sha256sums', 'sha256sums.json'}:
        return None, '独立校验和材料；不是研究轨迹或构造输入'
    if relative in graph_files:
        return None, '已接受图的重复边表；由constructors完整定义'
    if suffix == '.edges':
        if relative.startswith('context/') and size <= 2_000_000:
            return -2, ''
        return (1, '') if size <= 2_000_000 else (None, '大型边表；保留构造代码/输入/验收记录')
    if suffix in {'.bin', '.bits', '.u32', '.u8', '.npz', '.npy', '.clauses', '.body', '.tmp'}:
        return None, '大块中间数组/缓存/生成数据；保留生成源码与结果记录'
    if suffix in {'.cnf', '.lrat', '.drat', '.proof'} and size > 2_000_000:
        return None, '超大生成模型或证明流；保留建模源码、命令与判定/核验记录'
    if relative.startswith(('research-wiki/', 'context/')) or relative in guide_sources:
        if suffix in SOURCE | TEXT | SMALL_ASSETS and size <= 40_000_000:
            return -2, ''
    if suffix in SOURCE or path.name in {'lean-toolchain', 'Makefile', 'CMakeLists.txt'}:
        return 0, ''
    if relative.startswith(('proofs/', 'prompts/', 'reviews/', 'review-stage/')):
        if suffix in TEXT | SMALL_ASSETS and size <= 40_000_000:
            return 0, ''
    if suffix in {'.md', '.rst', '.html', '.htm'}:
        return 0, ''
    if suffix == '.json':
        return (1 if size <= 256_000 else 2 if size <= 2_000_000 else 3), ''
    if suffix in {'.csv', '.tsv'}:
        return (1 if size <= 2_000_000 else 2), ''
    if suffix in TEXT:
        if suffix == '.txt' and size > 30_000_000:
            return None, '大型外部源图/批量生成文本；出处和获取/生成程序保留'
        return (1 if size <= 2_000_000 else 4), ''
    if suffix in SMALL_ASSETS and size <= 5_000_000:
        return 2, ''
    return None, '不属于本包的文字/源码/关键小输入；或重复归档/可再生成大产物'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--bundle-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--budget', type=int, default=95_000_000)
    parser.add_argument('--reuse-selected', action='store_true',
                        help='Finalize the existing snapshot, including explicit supplemental small inputs.')
    args = parser.parse_args()
    root, bundle = args.source_root.resolve(), args.bundle_root.resolve()
    import csv
    with (root / 'research/graph_catalog.csv').open(encoding='utf-8-sig') as f:
        graph_files = {r['edge_file'] for r in csv.DictReader(f) if r['edge_file']}
    ledger = json.loads((root / 'research-wiki/DDP_METHOD_LEDGER.json').read_text())
    evidence = {p.split('#')[0] for r in ledger['rows'] for p in r.get('evidence_paths', [])}
    guide_sources = set()
    for guide in (bundle / 'guide').glob('0[1-4]*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', guide.read_text()):
            if target.startswith(('http:', 'https:', '#')):
                continue
            path = (guide.parent / target.split('#')[0]).resolve()
            try:
                relative = path.relative_to(bundle).as_posix()
            except ValueError:
                continue
            if (root / relative).is_file():
                guide_sources.add(relative)
    candidates, excluded = [], []
    for path in source_files(root):
        relative = path.relative_to(root).as_posix()
        size = path.stat().st_size
        priority, reason = classify(path, relative, size, evidence, graph_files, guide_sources)
        if priority is None:
            excluded.append((relative, size, reason))
        else:
            candidates.append((priority, size, relative, path))
    # Reserve space for the still-being-finalized reading guides and scope note.
    fixed = [p for p in bundle.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    estimated = 0 if args.reuse_selected else sum(
        compressed_size(p) + 256 + 2 * len(p.relative_to(bundle).as_posix().encode()) for p in fixed)
    estimated += 1_000_000
    selected, by_root = [], Counter()
    for index, (priority, size, relative, path) in enumerate(sorted(candidates), 1):
        if args.reuse_selected:
            if (bundle / relative).is_file():
                selected.append((relative, size))
                by_root[relative.split('/')[0]] += 1
            else:
                excluded.append((relative, size, '100MB上限下未内嵌；优先保全原始题目、Wiki、源码和判定记录'))
            continue
        if args.budget - estimated < 512:
            excluded.append((relative, size, '100MB上限下未内嵌；优先保全原始题目、Wiki、源码和判定记录'))
            continue
        packed = compressed_size(path)
        overhead = 256 + 2 * len((bundle.name + '/' + relative).encode())
        if estimated + packed + overhead > args.budget:
            excluded.append((relative, size, '100MB上限下未内嵌；优先保全原始题目、Wiki、源码和判定记录'))
        else:
            destination = bundle / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
            selected.append((relative, size))
            by_root[relative.split('/')[0]] += 1
            estimated += packed + overhead
        if index % 2500 == 0:
            print(json.dumps({'scanned_candidates': index, 'selected': len(selected),
                              'estimated_zip_bytes': estimated}), flush=True)
    note = [
        '# 归档范围与体积取舍', '',
        '本包按用户“尽量控制在100 MB”要求整理。原始文字、源码、题目与人工意见、完整研究Wiki和判定记录优先保留。',
        '153个已接受命名图用constructors/里的确定性程序和固定输入表达，不重复放大边表。',
        '不是原工作区的逐字节磁盘镜像。未内嵌的大模型/证明流、缓存、重复边表及崩溃转储不改写为不存在；需要它们的原始独立重验应按原路径取回或运行对应生成程序。',
        '历史命令、ACTIVE状态与timer是原记录，不是启动旧研究的新授权。', '',
        f'本轮原样收录原工作区文件：{len(selected)}份；原样字节总量：{sum(s for _,s in selected):,}。',
        f'本轮未内嵌候选产物：{len(excluded)}份；字节总量：{sum(s for _,s,_ in excluded):,}（包含多GB转储和重复/生成性数据）。', '',
        '## 原样材料按目录计数', '',
        '| 原目录 | 收录文件数 |', '|---|---:|',
        *[f'| {name} | {count} |' for name, count in sorted(by_root.items())], '',
        '## 未内嵌原因', '', '| 原因 | 文件数 | 原字节量 |', '|---|---:|---:|']
    reasons = Counter(reason for _,_,reason in excluded)
    for reason, count in reasons.items():
        note.append(f'| {reason} | {count} | {sum(s for _,s,r in excluded if r==reason):,} |')
    note += ['', '## 主要未内嵌大产物（原路径可定位生成器及结果）', '',
             '| 原路径 | 原字节量 | 原因 |', '|---|---:|---|']
    note += [f'| `{name}` | {size:,} | {reason} |'
             for name,size,reason in sorted(excluded,key=lambda x:x[1],reverse=True)[:70]]
    # Non-bulk textual omissions are itemized so a missing data table is visible.
    limited = [(n,s,r) for n,s,r in excluded if r.startswith('100MB')]
    note += ['', '## 由于100MB预算未内嵌的文字/数据文件', '',
             '以下不属于缓存自动忽略；是明确的体积取舍。请勿据“本包没有”推断原研究没有记录。', '']
    note += [f'- `{n}`（{s:,}字节）' for n,s,_ in limited] or ['无。']
    (bundle / 'guide/05_ARCHIVE_SCOPE.md').write_text('\n'.join(note) + '\n')
    with zipfile.ZipFile(args.output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        files = sorted(p for p in bundle.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
        for path in files:
            archive.write(path, bundle.name + '/' + path.relative_to(bundle).as_posix())
    result = {'archive': str(args.output), 'archive_bytes': args.output.stat().st_size,
              'embedded_files': len(files), 'original_files_copied': len(selected),
              'original_bytes_copied': sum(s for _,s in selected),
              'raw_files_omitted': len(excluded), 'hard_limit_bytes': 100_000_000}
    print(json.dumps(result), flush=True)
    if result['archive_bytes'] > 100_000_000:
        raise SystemExit('Archive exceeds the requested 100 MB cap.')


if __name__ == '__main__':
    main()

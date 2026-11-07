"""Stage the selected source and receipt bytes, then verify the proof ZIP."""

from html import escape
from pathlib import Path, PurePosixPath
from urllib.parse import quote
import argparse
import csv
import hashlib
import io
import json
import os
import zipfile


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
WORK = ROOT / 'working'
STAGE = WORK / 'package'
OUT = ROOT / 'n7-upper-bounds-20261103-proofs.zip'
OLD = 'reports/n756-professor-review-20261027/'
HTML = ROOT / 'n7-upper-bounds-20261103.html'
HELPER = REPO / '.agents/skills/render-html/scripts/render_html.py'
REFERENCE_ROOT = Path('D:/科研/math agent/ref')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded_json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def disk_path(path):
    """Keep the original deep proof tree accessible on Windows."""
    return Path('\\\\?\\' + str(path.absolute())) if os.name == 'nt' else path


class Package:
    def __init__(self):
        self.records = {}

    def add(self, member, data, category, original=None, expected=None):
        key = PurePosixPath(member)
        target = STAGE / member
        if key.is_absolute() or '..' in key.parts or '\\' in member or not target.resolve().is_relative_to(STAGE.resolve()):
            raise ValueError(f'Unsafe package path: {member}')
        file_hash = digest(data)
        if expected is not None and file_hash != expected:
            raise ValueError(f'Source hash drift: {original}')
        if member in self.records:
            raise ValueError(f'Duplicate package path: {member}')
        target = disk_path(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        record = {'path': member, 'bytes': len(data), 'sha256': file_hash, 'category': category}
        if original is not None:
            record['original_path'] = original
        self.records[member] = record
        return record

    def local(self, member, source, category, expected=None):
        path = (REPO / source).resolve()
        if not path.is_relative_to(REPO):
            raise ValueError(f'Source outside repository: {source}')
        return self.add(member, path.read_bytes(), category, source, expected)

    def text(self, member, text, category='guide'):
        return self.add(member, text.encode('utf-8'), category)


def classify(row, selection):
    path = row['source_path']
    for category in ('primary', 'dependency'):
        if path in selection[category]:
            return category
    return 'history'


def name_link(record, prefix=''):
    name = Path(record['original_path']).name
    return f'- [{name}](<{prefix}{record["path"]}>)'


def proof_reader(records):
    groups = [('primary', '当前主稿'), ('dependency', '依赖原稿'), ('history', '关联历史原稿')]
    parts = ['<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; base-uri \'none\'">',
             '<title>N7 证明源稿浏览</title><style>body{font:16px/1.6 "Times New Roman","SimSun",serif;max-width:980px;margin:30px auto;padding:0 16px;color:#172535}a{color:#1d6367}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f5f7f7;padding:1em;font:14px/1.6 "Times New Roman","SimSun",serif}summary{cursor:pointer;font-weight:600}details{border-top:1px solid #dce3e5;padding:.7em 0}li{overflow-wrap:anywhere}code{overflow-wrap:anywhere}</style></head><body>',
             '<h1>N7 证明源稿浏览</h1><p>展开条目即可选取源文本，也可在浏览器中查找。底稿、SHA256 与定位路径均可从每个条目核对。</p><p><a href="proofs/READING_GUIDE.md">阅读顺序与引用口径</a></p>']
    for kind, title in groups:
        parts.append(f'<h2>{title}</h2>')
        for record in [r for r in records if r['category'] == kind]:
            source = escape(Path(record['original_path']).name)
            href = quote(record['path'], safe='/._-')
            if kind == 'history':
                parts.append(f'<p><a href="{href}">{source}</a></p>')
            else:
                raw = disk_path(STAGE / record['path']).read_text(encoding='utf-8-sig')
                parts.append(f'<details><summary>{source}</summary><p><a href="{href}">原稿</a> · SHA256 <code>{record["sha256"]}</code></p><pre>{escape(raw)}</pre></details>')
    return ''.join(parts) + '</body></html>\n'


def stage_proofs(package, inventory, selection):
    all_paths = {row['source_path'] for row in inventory['proofs']['files']}
    primary = set(selection['primary'])
    dependency = set(selection['dependency'])
    if not primary or primary & dependency or not (primary | dependency) <= all_paths:
        raise ValueError('Proof roles must be explicit, disjoint and present in inventory')
    records = []
    for row in inventory['proofs']['files']:
        source = row['source_path']
        member = f'proofs/source-tree/{source}'
        records.append(package.local(member, source, classify(row, selection), row['sha256']))
    for category, title, filename in (
        ('primary', '当前主稿', 'CURRENT.md'), ('dependency', '依赖原稿', 'DEPENDENCIES.md'), ('history', '关联历史原稿', 'HISTORY_INDEX.md'),
    ):
        links = [name_link({**row, 'path': row['path'].removeprefix('proofs/')}) for row in records if row['category'] == category]
        package.text(f'proofs/{filename}', f'# {title}\n\n' + '\n'.join(links) + '\n')
    package.text('proof-reader.html', proof_reader(records), 'generated-proof-reader')
    package.add('proofs/source-map.json', encoded_json(records), 'source-map')
    tsv = ['category\tbytes\tsha256\toriginal_repo_path\tpackage_path']
    tsv.extend('\t'.join(str(row[key]) for key in ('category', 'bytes', 'sha256', 'original_path', 'path')) for row in records)
    package.text('proofs/source-map.tsv', '\n'.join(tsv) + '\n', 'source-map')
    return records


def stage_capacity(package, inventory):
    capacity = inventory['capacity_756']
    for row in capacity['manifest_items'] + capacity['additional_files']:
        source = row['source_path']
        name = source.removeprefix(OLD)
        package.local(f'proofs/sat-756/{name}', source, 'historical-756-sat-evidence', row['sha256'])
    by_hash = {row['sha256']: row for row in package.records.values()}
    register = REPO / OLD / '55-case-register.csv'
    table = io.StringIO(newline='')
    writer = csv.writer(table, delimiter='\t', lineterminator='\n')
    writer.writerow(('case_id', 'artifact', 'original_path', 'sha256', 'bytes', 'package_path'))
    with register.open(encoding='utf-8-sig', newline='') as handle:
        for case in csv.DictReader(handle):
            for artifact in ('cnf', 'proof', 'checker', 'checker_receipt'):
                file_hash = case[f'{artifact}_sha256']
                included = by_hash.get(file_hash, {})
                writer.writerow((case['case_id'], artifact, case[f'{artifact}_path'], file_hash,
                                 case.get(f'{artifact}_bytes') or included.get('bytes', ''),
                                 included.get('path', '')))
    package.text('proofs/sat-756/EXTERNAL-MATERIALS.tsv', table.getvalue(), 'historical-756-artifact-map')
    package.text('proofs/sat-756/README.md', '''# 756 容量 25 的既有资料

- [55 个反例单元的证据索引（CSV）](55-case-register.csv)
- [同一索引及原始收据字段（JSON）](55-case-register.json)
- [原始 CNF、证明、检查器与收据定位（TSV）](EXTERNAL-MATERIALS.tsv)
- [旧证据目录的来源和文件散列](evidence-manifest.json)
- [25 点染色见证](color.tsv) · [便携核验源码](verify_color.py) · [历史核验收据](verification.json) · [历史便携核验收据](portable-verification.json)

旧 E 编号是档案标识。证据目录沿用旧 manifest 的精确 95 项。55 单元索引记录原始 CNF、证明、检查器、收据的位置、散列及现有字节数等字段。大型 CNF 和 DRAT 等证明主体仍以索引中的 Linux 原路径定位。本包提供本机留存的原始收据和索引，文件完整性检查的对象是本包所含文件。

25 点见证核验记录属于旧交付。若需要重验，可在 Linux 上把 `verify_color.py` 与 `color.tsv` 复制到独立临时目录，在其中运行 `python3 verify_color.py color.tsv`，以保留包内历史回执。该脚本仅核验下界见证。此次打包核对原字节及散列，历史证书检查状态沿用旧原件。
''')


def stage_report_sources(package):
    for name in ('source/report.md', 'source/report.json', 'source/package-guide.md', 'source/proof-roles.json', 'report-template.html', 'render_report.py', 'draw_figures.py'):
        package.add(name, (ROOT / name).read_bytes(), 'report-source')
    for path in sorted((ROOT / 'figures').iterdir()):
        if path.is_file() and path.suffix in {'.svg', '.json'}:
            package.add(f'figures/{path.name}', path.read_bytes(), 'figure-source')
    package.add('rendering/aris_render_html.py', HELPER.read_bytes(), 'rendering-helper', str(HELPER.relative_to(REPO).as_posix()))
    for source_name, member in (('ON THE ERDŐS-TUZA-VALTR CONJECTURE.pdf', 'Baek-ETV-v1.pdf'),
                                ('The Erdős–Szekeres Conjecture Revisited.pdf', 'Baek-Balko-SoCG-2025.pdf')):
        original = REFERENCE_ROOT / source_name
        package.add(f'references/{member}', original.read_bytes(), 'user-supplied-literature', str(original))


def guides(package, reading_guide):
    package.text('README.md', '''# 从受限路径到凸七边形 · 证明材料

- [阅读顺序与范围](proofs/READING_GUIDE.md)
- [阅读报告正文](n7-upper-bounds-20261103.html)
- [浏览当前主稿及其依赖源文本](proof-reader.html)
- [756 容量的 SAT 证据与回执](proofs/sat-756/README.md)
- [全包字节数与 SHA256 清单](MANIFEST.json)

当前 N(7,6,7)≤75，N(7,7,7)≤76，几何强迫阈值 ES(7)≤77。更强的 74 点结论限于指定子类，详见阅读导引及当前原稿。

可直接打开 [START_HERE.html](START_HERE.html)。阅读报告为自包含 HTML，原始数学档案保存在 proofs/source-tree，生成报告的 Markdown、图源和生成器位于 source、figures 及根目录。[BUILD.md](BUILD.md) 说明正文的重生成方法。
''')
    package.text('proofs/READING_GUIDE.md', reading_guide.read_text(encoding='utf-8'))
    package.text('BUILD.md', '''# 重生成报告正文

在此目录运行 `python draw_figures.py`，再运行 `python render_report.py`。需要 Python 3、Matplotlib 和已安装的 Times New Roman（普通、斜体、粗体及粗斜体）。数学公式转为 SVG 轮廓，报告打开时不加载网络依赖。

source/report.md 是正文源，source/report.json 是标题配置，report-template.html 是版式，figures 是图源生成结果，rendering/aris_render_html.py 是随包提供的 Markdown 渲染辅助模块。重生成可能改变生成时间元数据和文件散列。

proofs/source-tree 是原始证明档案，不参与正文生成。collect_sources.py 与 package_delivery.py 保存本次仓库资料清点与封装逻辑，其读取路径以原仓库为环境。包内科研核验源码如需运行，应按各自说明在 Linux 执行。
''')
    package.text('START_HERE.html', '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'"><title>N7 报告与证明材料</title><style>body{font:18px/1.8 "Times New Roman","SimSun",serif;max-width:760px;margin:50px auto;padding:0 20px;color:#172535}a{color:#1d6367}</style><h1>从受限路径到凸七边形</h1><ul><li><a href="n7-upper-bounds-20261103.html">阅读报告正文</a></li><li><a href="proofs/READING_GUIDE.md">证明阅读顺序与范围</a></li><li><a href="proof-reader.html">浏览证明原稿</a></li><li><a href="proofs/sat-756/README.md">受限极值 25 的资料</a></li><li><a href="MANIFEST.json">文件完整性清单</a></li><li><a href="BUILD.md">正文重生成方法</a></li></ul></html>
''')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', type=Path, required=True)
    parser.add_argument('--selection', type=Path, required=True)
    parser.add_argument('--guide', type=Path, required=True)
    parser.add_argument('--qa', type=Path, required=True)
    args = parser.parse_args()
    if not HTML.is_file():
        raise FileNotFoundError(HTML)
    inventory = json.loads(args.inventory.read_text(encoding='utf-8'))
    selection = json.loads(args.selection.read_text(encoding='utf-8'))
    package = Package()
    proof_records = stage_proofs(package, inventory, selection)
    stage_capacity(package, inventory)
    stage_report_sources(package)
    guides(package, args.guide)
    package.add(HTML.name, HTML.read_bytes(), 'rendered-report')
    for name in ('collect_sources.py', 'package_delivery.py'):
        package.add(name, (ROOT / name).read_bytes(), 'delivery-source')
    package.add('integrity/source-inventory.json', encoded_json(inventory), 'source-inventory')
    package.add('integrity/proof-roles.json', encoded_json(selection), 'source-inventory')
    report_hash = digest(HTML.read_bytes())
    browser_bytes = args.qa.read_bytes()
    browser_result = json.loads(browser_bytes)
    if not browser_result['pass'] or browser_result['htmlSHA256'] != report_hash:
        raise ValueError('Browser QA is missing or belongs to a different HTML')
    package.add('integrity/browser-validation.json', browser_bytes, 'delivery-engineering-check')
    manifest = {'kind': 'n7-upper-bounds-reading-and-proof-materials', 'report_sha256': report_hash, 'files': list(package.records.values())}
    package.add('MANIFEST.json', encoded_json(manifest), 'manifest')
    names = sorted(package.records)
    if len({name.casefold() for name in names}) != len(names):
        raise ValueError('Case-insensitive ZIP name collision')
    pending = WORK / OUT.name
    with zipfile.ZipFile(pending, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in names:
            archive.write(disk_path(STAGE / name), name)
    with zipfile.ZipFile(pending) as archive:
        if archive.testzip() is not None or archive.namelist() != names:
            raise ValueError('ZIP member or CRC mismatch')
        for name in names:
            if digest(archive.read(name)) != package.records[name]['sha256']:
                raise ValueError(f'ZIP SHA256 mismatch: {name}')
    pending.replace(OUT)
    result = {'html': HTML.name, 'html_sha256': report_hash, 'zip': OUT.name, 'zip_sha256': digest(OUT.read_bytes()), 'zip_bytes': OUT.stat().st_size, 'zip_members': len(names), 'proof_markdown': len(proof_records), 'historical_756_evidence_files': len(inventory['capacity_756']['manifest_items']), 'zip_readback_passed': True}
    (ROOT / 'delivery-validation.json').write_bytes(encoded_json(result))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

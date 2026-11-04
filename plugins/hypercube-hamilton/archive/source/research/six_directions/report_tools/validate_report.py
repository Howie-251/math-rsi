"""Check rendered completeness, local links and frozen source preservation."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
R = HERE.parent
ROOT = R.parent.parent
manifest = json.loads((HERE / 'REPORT_BUILD_MANIFEST.json').read_text(encoding='utf-8'))
soup = BeautifulSoup((ROOT / 'Ruskey-Savage_Q6_研究报告.html').read_text(encoding='utf-8'), 'html.parser')
ids = [item['id'] for item in soup.select('[id]')]
broken = []
local = anchors = 0
for a in soup.select('a[href]'):
    href = a['href']
    if href.startswith('#'):
        anchors += 1
        if unquote(href[1:]) not in ids:
            broken.append(href)
    elif not urlsplit(href).scheme:
        local += 1
        if not (ROOT / unquote(urlsplit(href).path)).exists():
            broken.append(href)
assert len(soup.select('details.source-doc')) == manifest['proof_documents'] + manifest['review_documents']
assert len(soup.find_all('math')) == manifest['math_converted']
assert len(ids) == len(set(ids))
assert not broken, broken
assert not manifest['math_conversion_errors']
for name, digest in manifest['embedded_source_hashes'].items():
    assert hashlib.sha256((R / name).read_bytes()).hexdigest() == digest, name
for name, meta in manifest['outputs'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == meta['sha256'], name
assert manifest['main_source_sha256'] in (R / 'RUSKEY_SAVAGE_REPORT_SEMANTIC_REVIEW.md').read_text(encoding='utf-8')
result = {
    'status': 'PASS',
    'source_documents': len(soup.select('details.source-doc')),
    'mathml_formulas': len(soup.find_all('math')),
    'main_math_formulas': manifest['main_math_converted'],
    'unique_ids': len(ids), 'local_links_checked': local,
    'internal_links_checked': anchors, 'broken_links': broken,
    'frozen_source_hashes_unchanged': True,
    'main_narrative_semantic_review_hash_matches': True,
    'offline_math_no_cdn': not bool(soup.find('script', src=True)),
}
(HERE / 'REPORT_VALIDATION.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result))

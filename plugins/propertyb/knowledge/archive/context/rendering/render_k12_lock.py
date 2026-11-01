#!/usr/bin/env python3
"""Standalone k=12 lock-certificate reader; never writes existing general pages."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import tempfile
from render_general_growth import (ROOT, aris, embed_math, normalize_math,
    source_math_inputs, reader_links, prepare_reader_source, browser_check,
    general_reader_template)
SOURCE = ROOT / 'context/propertyb-general/k12-lock-pilot-20261021/DERIVATION_PACKAGE.md'
TRACE = ROOT / '.aris/traces/render-html/2026-10-21_k12-lock-comparison'

def template(name):
    text = general_reader_template(name)
    text = re.sub(r'<footer class="aris-footer">[\s\S]*?</footer>',
       '<footer class="aris-footer"><a href="K12_LOCK_COMPARISON.md">阅读稿 Markdown</a> · '
       '<a href="context/propertyb-general/k12-lock-pilot-20261021/DERIVATION_PACKAGE.md">规范源</a> · '
       '<a href="context/propertyb-general/k12-lock-pilot-20261021/pilot/REPORT.md">完整计算报告</a></footer>', text, count=1)
    return text.replace('</style>', '''
main :not(pre)>code {white-space:normal;overflow-wrap:anywhere}
main .table-scroll{margin:22px 0}
@media(max-width:700px){main table{min-width:630px}main table th,main table td{overflow-wrap:anywhere}nav.toc ol{white-space:normal;display:block}nav.toc ol li{margin:7px 0}}
</style>''',1)

def main():
    TRACE.mkdir(parents=True,exist_ok=True)
    raw=SOURCE.read_text()
    body=reader_links(normalize_math(raw),SOURCE).rstrip()+'\n'
    source=ROOT/'K12_LOCK_COMPARISON.md'
    output=ROOT/'K12_LOCK_COMPARISON.html'
    source.write_text(body)
    aris.load_template=template
    aris.strip_frontmatter=prepare_reader_source
    with tempfile.TemporaryDirectory(prefix='k12-lock-render-',dir=ROOT) as tmp:
        stage=Path(tmp)/'reader.html'
        aris.main([str(source),'--out',str(stage),'--template','academic',
            '--title','k=12：锁点法的更强局部下界',
            '--eyebrow','PROPERTY B · LOCAL CERTIFICATE',
            '--subtitle','4633 → 4635 → 4647 → 4661 · 完整归约与整数证书 · 合作者方法的新实例',
            '--lang','zh-CN'])
        math_report=embed_math(stage,output,source)
    (TRACE/'math-build.json').write_text(json.dumps(math_report,ensure_ascii=False,indent=2)+'\n')
    report=browser_check(output,TRACE,source,source_math_inputs(body))
    report.update(generatedAt=datetime.now(timezone.utc).isoformat(),
       canonicalSource=str(SOURCE.relative_to(ROOT)),markdown=source.name,html=output.name)
    (TRACE/'browser-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (TRACE/'canonical-source.md').write_text(raw)
    print(f'Rendered {output.name}; {math_report["math"]} embedded SVG formulas; offline desktop/phone checks passed.')
if __name__=='__main__':main()

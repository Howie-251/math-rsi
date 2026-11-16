#!/usr/bin/env python3
"""Render both case manuscripts with ARIS and add their offline illustrations.

The original ARIS parser and academic template are used without modification.
The case adapter embeds local figures and adds the requested interaction.
Source fingerprints are not computed, following the project owner's preference.
"""
import base64
from copy import deepcopy
from datetime import datetime, timezone
import html
import importlib.util
import json
from pathlib import Path
import re
import shutil

CASE = Path(__file__).resolve().parents[1]
REPO = CASE.parent.parent
ENGINE = REPO / "base/skills/skills-codex/render-html/scripts/render_html.py"
if not ENGINE.exists():
    ENGINE = CASE / "tools/aris-render-html/render_html.py"
spec = importlib.util.spec_from_file_location("aris_render_html", ENGINE)
aris = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aris)

LANGUAGES = [
    {"lang":"en", "source":"README.md", "output":"index.html",
     "subtitle":"Latest D5 endpoints and dated construction history", "toc":"Contents",
     "tabs":["A · Covering neighborhoods", "B · Controller and fibers", "C · Geometric reallocation"],
     "method_label":"Construction methods", "step_label":"Cube extension examples"},
    {"lang":"zh-CN", "source":"README.zh-CN.md", "output":"index.zh-CN.html",
     "subtitle":"最新 D5 端点与有日期的构造历史", "toc":"目录",
     "tabs":["A · 保边补点", "B · 控制器与有限域", "C · 几何连接重分配"],
     "method_label":"构造方法", "step_label":"立方体补点示例"},
]
EN_STEPS = {
    "one":("One attachment", "Connecting x only to vertex 0 leaves vertex 7 at distance 4. The degree bound holds, but the diameter bound fails."),
    "cover":("Complementary attachments", "Connecting x to opposite corners 0 and 7 covers all eight original vertices within three steps, with degrees at most 4."),
    "capacity":("Reuse the same points", "A second vertex y attached to 0 and 7 preserves coverage, but raises both attachment points to degree 5, exceeding the limit of 4."),
    "rebalance":("Choose different points", "Attaching y to 1 and 6 covers all nine existing vertices, including x, while keeping every degree at most 4."),
}


def cube_demo(config, original_alt):
    data = deepcopy(json.loads((CASE/"data/construction_demo.json").read_text()))
    buttons, figures = [], []
    for state in data["states"]:
        sid = state["id"]
        if config["lang"] == "en":
            state["label"], state["explanation"] = EN_STEPS[sid]
        buttons.append(f'<button type="button" data-step="{sid}" aria-controls="demo-{sid}" '
                       f'aria-pressed="{str(sid=="cover").lower()}">{html.escape(state["label"])}</button>')
        alt = html.unescape(original_alt) if sid=="cover" else state["explanation"]
        figures.append(f'<figure class="demo-state" id="demo-{sid}" data-state="{sid}">'
                       f'<img src="assets/{state["file"]}.svg" alt="{html.escape(alt,quote=True)}">'
                       f'<figcaption>{html.escape(state["explanation"])}</figcaption>'
                       f'<div class="figure-links"><a href="assets/{state["file"]}.svg">SVG</a>'
                       f'<a href="assets/{state["file"]}.png">PNG</a></div></figure>')
    result = f'<div class="step-controls" role="group" aria-label="{config["step_label"]}">'+"".join(buttons)+"</div>"
    result += "".join(figures)
    result += '<p id="demo-description" class="demo-description" aria-live="polite">'+html.escape(data["states"][1]["explanation"])+"</p>"
    result += '<script type="application/json" id="demo-data">'+json.dumps(data,ensure_ascii=False).replace("<","\\u003c")+"</script>"
    return result


def enhance_methods(body, config):
    headings = list(re.finditer(r'<h3 id="([^"]+)">.*?</h3>',body))
    assert len(headings)==3, "The case has three construction subsections."
    end = body.index('<h2 ',headings[-1].end())
    method_ids = ["method-filling", "method-controller", "method-geometry"]
    tabs = f'<div class="method-tabs" role="group" aria-label="{config["method_label"]}">'
    panels=[]
    for i,(heading,mid) in enumerate(zip(headings,method_ids)):
        tabs += f'<button type="button" data-method="{mid}" aria-controls="{mid}" aria-pressed="{str(i==0).lower()}">{config["tabs"][i]}</button>'
        stop = headings[i+1].start() if i<2 else end
        panels.append(f'<article class="method-panel" id="{mid}">'+body[heading.start():stop]+"</article>")
    body = body[:headings[0].start()]+'<span id="construction"></span>'+tabs+"</div>"+"".join(panels)+body[end:]
    pattern = r'<p><img\s+src="assets/construction_filling\.png"\s+alt="([^"]*)"\s*/?></p>'
    body, count = re.subn(pattern,lambda m:cube_demo(config,m.group(1)),body)
    assert count==1, "Expected one source illustration for the interactive cube."
    body = body.replace("<table>",'<div class="case-table"><table>').replace("</table>","</table></div>")
    return body


def embed_figure(match):
    local = CASE/match.group(2)
    if local.suffix==".png" and local.with_suffix(".svg").exists():
        local=local.with_suffix(".svg")
    payload=base64.b64encode(local.read_bytes()).decode("ascii")
    mime="image/svg+xml" if local.suffix==".svg" else "image/png"
    return match.group(1)+f"data:{mime};base64,"+payload+'"'


def render(config):
    raw=(CASE/config["source"]).read_text(encoding="utf-8")
    blocks=aris.parse_blocks(aris.strip_frontmatter(raw).split("\n"))
    # The source title is presented once, in the generated hero.
    assert blocks[0]["type"]=="heading" and blocks[0]["level"]==1
    body,toc=aris._render_blocks(blocks[1:],collect_toc=True)
    body=enhance_methods(body,config)
    template=aris.load_template("academic")
    # Omit the default fingerprint fields before substitution; do not invoke
    # the CLI, which computes a fingerprint unconditionally.
    template="\n".join(line for line in template.split("\n") if "SOURCE_SHA256" not in line)
    # Keep production metadata in the footer, outside the research narrative.
    template=re.sub(r'<div class="meta">.*?</div>',"",template,flags=re.S)
    template=template.replace('content="ARIS render-html (academic, v1)"',
                              'content="ARIS render-html (academic; Degree–Diameter interactive adapter)"')
    generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    source_path=f'case-studies/degree-diameter/{config["source"]}'
    vars_={"LANG":config["lang"],"TITLE":"Degree–Diameter",
           "SUBTITLE_BLOCK":f'<p class="subtitle">{config["subtitle"]}</p>',
           "EYEBROW_BLOCK":'<div class="eyebrow">MathRSI · Research Case</div>',
           "BYLINE_BLOCK":"","SOURCE_PATH":source_path,"GENERATED_AT":generated_at,
           "HEAD_CDN":aris.CDN_BLOCK_OFFLINE,"TOC_HTML":aris.render_toc(toc),
           "TOC_LABEL":config["toc"],"BODY_HTML":body,"EXTRA_META":""}
    page=aris.substitute(template,vars_)
    css=(CASE/'assets/case.css').read_text()
    page=page.replace('</head>',f'<style>\n{css}\n</style>\n</head>',1)
    page=re.sub(r'(<img\b[^>]*\bsrc=")(assets/[^"]+\.(?:svg|png))"',embed_figure,page)
    script=(CASE/'assets/construction.js').read_text()
    page=page.replace('</body>',f'<script>\n{script}\n</script>\n</body>',1)
    (CASE/config["output"]).write_text(page,encoding="utf-8")
    print(f'Rendered {config["output"]} from {config["source"]} with ARIS; {generated_at}.')


if __name__=="__main__":
    for config in LANGUAGES:
        render(config)
    shutil.copyfile(CASE/'README.md',CASE/'CASE_STUDY_EN.txt')
    shutil.copyfile(CASE/'README.zh-CN.md',CASE/'CASE_STUDY.txt')

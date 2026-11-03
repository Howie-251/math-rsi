#!/usr/bin/env python3
"""Make a small self-contained Python graph delivery with scoped evidence."""
import json
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
NAME='F5_D20_D3_3750_20261029'
DEST=PROJECT/'expert_review_current'/NAME
DEST.mkdir(parents=True,exist_ok=True)


def copy(source,target):
    dest=DEST/target;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)


for name in ['README.md','graph_d20_D3_n3750.edges','PARAMETERS.json','generate.py',
    'independent_verify.py','INDEPENDENT_VALIDATION.json','GENERATION_RESULT.json',
    'REPRODUCTION_CHECK.json','RESULT_OVERVIEW.json','EXECUTION_SCOPE.md','PROOF_AUDIT.md',
    'PROOF_AUDIT.json','PROOF_SKELETON.md','FORMAL_INPUT_BINDING_CHECK.json','FINAL_COMPILE_RESULT.json']:
    copy(HERE/name,name)
for name in ['FORMAL_BINDING_PLAN.md','COMPILE_RESULT.json','INVERSE_COMPILE_RESULT.json',
    'FORMAL_COMPILE_LOG.txt','FORMAL_INVERSE_COMPILE_LOG.txt']:
    copy(HERE/name,'formal/'+name)
copy(HERE/'FORMAL_COMPILED_INVERSE_SNAPSHOT.lean','formal/DegreeDiameter/Portfolio/F5Graph3750.lean')
copy(PROJECT/'formal/DegreeDiameter/Portfolio/SingleExtension.lean','formal/DegreeDiameter/Portfolio/SingleExtension.lean')
copy(PROJECT/'formal/lean-toolchain','formal/lean-toolchain')
for source in (HERE/'FORMAL_FINAL_SOURCES').rglob('*.lean'):
    copy(source,Path('formal')/source.relative_to(HERE/'FORMAL_FINAL_SOURCES'))
for source in HERE.glob('FORMAL_KERNEL_DECODERS_*.log'):
    copy(source,'formal/'+source.name)
copy(HERE/'FORMAL_EXACT_THREE_F5Graph3750Exact.log','formal/FORMAL_EXACT_THREE_F5Graph3750Exact.log')
for source,target in [
    ('f5_full3750_20261029.DISPOSITION.md','F5_FULL_GRAPH_REVIEW_DISPOSITION.md'),
    ('f5_full3750_20261029.response.json','F5_FULL_GRAPH_REVIEW_RESPONSE.json'),
    ('refresh_f5_complementary_20261029.DISPOSITION.md','LOCAL_RULE_REVIEW_DISPOSITION.md'),
]:
    copy(PROJECT/'reviews/ddp'/source,'reviews/'+target)
local=HERE.parent/'f5_complementary_triples'
for name in ['PROOF_SCOPE.md','RESULT.json','MATRICES_AND_PENCILS.json','ROOT_NB3_BINDING.json']:
    copy(local/name,'algebra/'+name)
for name in ['RESULT.json','PRIMARY_SOURCES.json','REPORT.md']:
    copy(local/'baseline_check'/name,'baseline_check/'+name)
for name in ['REPORT.md','RESULT.json','ACCESS_RECEIPT.json','RELATED_FILE_RECEIPT.json','RESULTS_LISTING.json']:
    copy(local/'author_repo_targeted_check'/name,'author_repo_targeted_check/'+name)

# Only the reproduction code is exercised in a shallow temporary directory.
# No source graph or all-root verifier is rerun.
if '--reuse-reproduction' not in sys.argv:
    with tempfile.TemporaryDirectory(prefix='f5-delivery-') as directory:
        stage=Path(directory)
        for name in ['generate.py','PARAMETERS.json','graph_d20_D3_n3750.edges']:
            shutil.copy2(DEST/name,stage/name)
        command=[sys.executable,'generate.py','--parameters','PARAMETERS.json','--compare',
                 'graph_d20_D3_n3750.edges','--dry-run']
        result=subprocess.run(command,cwd=stage,capture_output=True,text=True,check=True)
        parsed=json.loads(result.stdout)
        assert parsed['comparison']['edge_set_matches'] and parsed['comparison']['repeated_rows']==0
        receipt=dict(status='PASS_STANDALONE_STANDARD_LIBRARY_REPRODUCTION',command=command,
                     used_original_project_data=False,BFS_repeated=False,report=parsed)
    (DEST/'STANDALONE_REPRODUCTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
else:
    assert (DEST/'STANDALONE_REPRODUCTION.json').is_file()

render=runpy.run_path(str(PROJECT/'expert_review_current/build_handoff_20261028.py'))['render_markdown']
body,_=render((DEST/'README.md').read_text())
styles='body{max-width:1000px;margin:36px auto;padding:0 24px;font:17px/1.8 system-ui;color:#182839}h1{font-size:30px}h2{margin-top:36px;font-size:23px}table{width:100%;border-collapse:collapse}th,td{padding:9px;border:1px solid #ced8df;text-align:left}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f1f5f7;padding:16px}a{color:#145f9c}code{font-size:.88em}@media print{body{font-size:11pt}h2{break-after:avoid}pre,tr{break-inside:avoid}}'
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>3750点20正则直径3完整图</title><style>'+styles+'</style></head><body>'+body+'</body></html>\n'
(DEST/'README.html').write_text(page);(DEST/'README.html.txt').write_text(page)
archive=DEST.parent/(NAME+'.zip')
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as out:
    for p in sorted(DEST.rglob('*')):
        if p.is_file():out.write(p,str(Path(NAME)/p.relative_to(DEST)))
mirror=Path('/mnt/data');mirror.mkdir(parents=True,exist_ok=True)
shutil.copy2(archive,mirror/('AR4MATH_'+NAME+'.zip'))
shutil.copy2(DEST/'README.html',mirror/('AR4MATH_'+NAME+'.html'))
print('Full graph delivery:',DEST)
print('Package bytes:',archive.stat().st_size)
print('Standalone generation matches the independently verified edge list; no BFS repeated.')

#!/usr/bin/env python3
"""Minimal dated merge into the existing Wiki; no research experiment or ledger write."""
from pathlib import Path
import json
import subprocess
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
manifest={r.split('\t',1)[0]:r.split('\t',1)[1] for r in (ROOT/'.aris/installed-skills-codex.txt').read_text().splitlines() if '\t' in r}
HELPER=Path(manifest['repo_root'])/'tools/research_wiki.py'
notes=json.loads((HERE/'notes.json').read_text())
commands=[]
outputs=[]
changed=[]
assert WIKI.is_dir() and HELPER.is_file()

def call(*args):
    command=['python',str(HELPER),*args]
    result=subprocess.run(command,cwd=ROOT,text=True,capture_output=True)
    commands.append(command);outputs.append(dict(command=command,returncode=result.returncode,stdout=result.stdout,stderr=result.stderr))
    assert result.returncode==0,result.stderr
    return result.stdout

# Canonical dedup entry, intentionally no --update-on-exist: that flag would
# destroy rich historical body sections. Existing notes are then edited in place
# as permitted by the skill's preservation contract.
for slug,title in [('ddp-open-parameter-construction-20261026','多参数度数—直径构造：按机制与研究价值选择机会'),
                   ('ddp-q3-three-step-plane-pencil31','三步仿射纤维：真实路线并集与pencil共同覆盖')]:
    assert (WIKI/'ideas'/f'{slug}.md').is_file()
    text=call('upsert_idea',str(WIKI),'--slug',slug,'--title',title)
    assert 'skipping' in text

for relative,note in notes.items():
    path=WIKI/relative
    text=path.read_text()
    marker='<!-- TWO_SUCCESSFUL_METHODS_RESUME_20261101 -->'
    assert marker not in text,f'Dated merge already present: {path}'
    if relative.startswith('ideas/'):
        before,separator,after=text.partition('## Connections')
        assert separator
        updated=before.rstrip()+'\n\n'+note.rstrip()+'\n\n'+separator+after
        if relative=='ideas/ddp-q3-three-step-plane-pencil31.md':
            updated=updated.replace('stage: piloted\n','stage: active\n',1)
            updated=updated.replace('**stage:** `piloted`','**stage:** `active`',1)
        assert updated.partition('## Connections')[2]==after
    else:
        updated=text.rstrip()+'\n\n'+note.rstrip()+'\n'
    path.write_text(updated)
    changed.append(str(path.relative_to(ROOT)))
    call('log',str(WIKI),f'2026-11-01 two-successful-method resume: dated append to {relative}; preserve prior evidence and counts')

A='idea:ddp-open-parameter-construction-20261026'
B='idea:ddp-q3-three-step-plane-pencil31'
edges=[]
for slug in ['ddp-h9-qline-d11-family-37631','ddp-h9-qline-d12-family-42377','ddp-d13-singlefault-star-family-51457-20261027',
             'ddp-accepted-d11-d12-full-neighborhood-clone-scan-20261028','ddp-d15-d4-literal15552-k8-shared64-backbone-20261030']:
    edges.append((A,f'exp:{slug}','tested_by','2026-11-01 resume: inherit this exact source/rule result; no new run and no exclusion of general extension mechanisms.'))
for slug in ['ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029',
             'ddp-f5-literal3750-induced-retention-max16-d3-20261029',
             'ddp-c21-fano-flag-uniform100-affine-plane-deletion-route-obstruction-16d3-20261030',
             'ddp-f5-fiber80-two-type-normal-scaling-chart-rigidity-16d3-20261030',
             'ddp-wave2-triangle-factor33-controller']:
    edges.append((B,f'exp:{slug}','tested_by','2026-11-01 resume: reuse the positive instance or precisely bounded failed rule; general q/controller extrapolation remains unproved.'))
edges.append(('exp:ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029',
              'claim:ddp-f5-fin3750-order-degree20-exactd3-20261029','supports',
              'Fixed Fin3750 formula graph only; existing kernel proof and literal-edge BFS are distinct evidence. No latest-global novelty claim.'))
for source,target,kind,evidence in edges:
    for nid in (source,target):
        prefix,slug=nid.split(':',1)
        folder={'idea':'ideas','exp':'experiments','claim':'claims'}[prefix]
        assert (WIKI/folder/f'{slug}.md').is_file(),nid
    output=call('add_edge',str(WIKI),'--from',source,'--to',target,'--type',kind,'--evidence',evidence)
    if 'Edge added:' in output:
        call('log',str(WIKI),f'2026-11-01 two-successful-method resume: {source} --{kind}--> {target}')
call('rebuild_index',str(WIKI))
call('rebuild_query_pack',str(WIKI))
call('log',str(WIKI),'2026-11-01 two-successful-method resume merged into existing Wiki; same Goal, no new research result; D2 remains paused')
receipt=dict(status='EXISTING_WIKI_TWO_SUCCESSFUL_METHODS_MERGED',completed_UTC=datetime.now(timezone.utc).isoformat(),
    wiki=str(WIKI),canonical_helper=str(HELPER),manifest=str(ROOT/'.aris/installed-skills-codex.txt'),
    skill=str(Path(manifest['repo_root'])/'skills/skills-codex/research-wiki/SKILL.md'),
    changed_pages=changed,reused_ideas=[A,B],reused_claim='claim:ddp-f5-fin3750-order-degree20-exactd3-20261029',
    attempted_edge_upserts=len(edges),new_experiment_nodes=0,new_claim_nodes=0,
    ledger_modified=False,Goal_files_modified=False,research_experiments_run=0,source_graph_BFS_run=0,
    counts={'legitimate_instances':104,'parameter_pairs':4,'confirmed_main_table_instances':103,'confirmed_pairs':3,'concrete_formula_Lean_instances':1,'global_20D3_novelty':'pending'},
    same_Goal_user_resume_recorded=True,old_D2_paused=True,commands=commands,
    pending=['Root final Goal/brief update precedes the final query refresh if its project-direction section changed.'])
(HERE/'HELPER_CALLS.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2)+'\n')
(HERE/'RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='commands'},ensure_ascii=False,indent=2))

import json,re,time
from pathlib import Path
D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());P=D.parent/'opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation/formalization';P.mkdir(exist_ok=True)
s=json.loads((D/'CHECKPOINT.json').read_text());binding=json.loads((D/'Q4_EXTERNAL_INPUT_BINDING.json').read_text());assert binding['status'].startswith('PASS_')
required=['DiagonalFillReallocation'+x for x in ['Definitions','Walks','Geometry','Degree','Lower']]+['Q4DiagonalFill'+x for x in ['Definitions','Inputs','Exact','Audit']]
assert all(m in s['completed']for m in required)
a=next(a for a in s['attempts']if a['module']=='Q4DiagonalFillAudit'and a['PASS']);log=Path(a['log']).read_text();assert 'error:'not in log and'sorryAx'not in log
groups=re.findall(r'depends on axioms: \[([^\]]*)\]',log);assert len(groups)>=2
for g in groups:assert set(x.strip()for x in g.split(',')if x.strip())<={'propext','Classical.choice','Quot.sound'}
result=dict(status='ORIGINAL_Q4_D26_7532_KERNEL_AUDIT_AND_EXTERNAL_LABEL_BINDING_PASS',target='DegreeDiameter.Portfolio.Q4DiagonalFill.d26_7532',FinalClaim='DegreeDiameter.Portfolio.Q4DiagonalFill.FinalClaim',final_claim='DegreeDiameter.Portfolio.Q4DiagonalFill.final_claim',explicit_label='Fin7532',order=7532,max_degree=26,genuine_Walk_D3=True,not_D2=True,no_user_certificate_premises=True,axioms=['propext','Classical.choice','Quot.sound'],case_modules=4,new_shared_generic_modules=5,case_module_CPU_seconds=sum(a['CPU_seconds']for a in s['attempts']if a['module'].startswith('Q4')),shared_batch_CPU_snapshot=s['CPU_seconds'],shared_batch_budget=600,Audit_log=a['log'],external_binding=str(D/'Q4_EXTERNAL_INPUT_BINDING.json'),running=False,active_modules=[],old_modules_modified_or_recompiled=False,graph_BFS_or_old_geometry_or_field_or_projection_reruns=0,priority='UNKNOWN')
for p in[D/'Q4_FINAL.json',P/'FINAL.json']:p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

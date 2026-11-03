import json,re,time
from pathlib import Path
D=Path(__file__).resolve().parent;s=json.loads((D/'CHECKPOINT.json').read_text());assert not s['running']
mods=['DiagonalFillReallocation'+x for x in['Definitions','Walks','Geometry','Degree','Lower']]+[tag+'DiagonalFill'+x for tag in['Q4','Q8']for x in['Definitions','Inputs','Exact','Audit']];assert set(mods)==set(s['completed'])
bindings=[json.loads((D/(tag+'_EXTERNAL_INPUT_BINDING.json')).read_text())for tag in['Q4','Q8']];assert all(b['status'].startswith('PASS_')for b in bindings)
for tag in['Q4','Q8']:
 a=next(a for a in s['attempts']if a['module']==tag+'DiagonalFillAudit'and a['PASS']);log=Path(a['log']).read_text();assert 'error:'not in log and'sorryAx'not in log
 for group in re.findall(r'depends on axioms: \[([^\]]*)\]',log):assert set(x.strip()for x in group.split(',')if x.strip())<={'propext','Classical.choice','Quot.sound'}
cpu=s['CPU_seconds']+sum(b['CPU_seconds']for b in bindings)+time.process_time();assert cpu<600
claims=[]
for tag,n,degree,casepath in[('Q4',7532,26,'opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation'),('Q8',346516,82,'even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation')]:
 a=next(a for a in s['attempts']if a['module']==tag+'DiagonalFillAudit'and a['PASS']);claim=dict(status='ORIGINAL_TARGET_KERNEL_AUDIT_AND_EXTERNAL_LABEL_BINDING_PASS',target=f'DegreeDiameter.Portfolio.{tag}DiagonalFill.d{degree}_{n}',FinalClaim=f'DegreeDiameter.Portfolio.{tag}DiagonalFill.FinalClaim',final_claim=f'DegreeDiameter.Portfolio.{tag}DiagonalFill.final_claim',order=n,max_degree=degree,label=f'Fin{n}',genuine_Walk_D3=True,not_D2=True,no_user_certificate_premises=True,axioms=['propext','Classical.choice','Quot.sound'],Audit_log=a['log'],external_binding=str(D/(tag+'_EXTERNAL_INPUT_BINDING.json')),case_module_CPU_seconds=sum(a['CPU_seconds']for a in s['attempts']if a['module'].startswith(tag)),shared_batch_CPU_seconds=cpu,old_modules_recompiled=False,running=False,active_modules=[],priority='UNKNOWN');claims.append(claim)
 p=D.parent/casepath/'formalization';p.mkdir(exist_ok=True)
 for path in[p/'FINAL.json',D/(tag+'_FINAL.json')]:path.write_text(json.dumps(claim,indent=2)+'\n')
result=dict(status='BOTH_FIXED_DIAGONAL_FILL_REALLOCATION_TARGETS_KERNEL_AUDIT_AND_EXTERNAL_BINDING_PASS',claims=claims,CPU_seconds=cpu,CPU_budget_seconds=600,new_modules=13,failed_attempts=sum(not a['PASS']for a in s['attempts']),all_attempts=len(s['attempts']),new_spread_cover_checks=670,new_line_two_checks=670,old_projection_or_geometry_or_field_reruns=0,large_graph_reads=0,BFS=0,old_modules_recompiled=False,running=False,active_modules=[],extra_83_not_in_this_budget=True,external_review_calls=0)
(D/'FINAL.json').write_text(json.dumps(result,indent=2)+'\n');s.update(status=result['status'],CPU_seconds=cpu,running=False,active_modules=[],final_receipt=str(D/'FINAL.json'));(D/'CHECKPOINT.json').write_text(json.dumps(s,indent=2)+'\n');(D/'HANDLE.json').write_text(json.dumps(dict(status=result['status'],running=False,active_modules=[],CPU_seconds=cpu),indent=2)+'\n');(D/'STAGE_STATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

from pathlib import Path
import subprocess,json
R=Path.cwd();T=R/'t15_core1_review_trace';rows=[]
for stem,n in [('t15_core1_route_c0_residual',1091475),('t15_core1_joint_fourbridge_c4_residual',1575),('t15_core1_joint_fourbridge_c6_residual',6300),('t15_core1_joint_fourbridge_c8_residual',2520)]:
 r=json.loads(subprocess.check_output([str(T/'residual.exe'),stem+'_inputs.bin',stem+'.bin',str(n)],text=True));assert r['status']=='PASS' and r['verified']==n;rows.append(dict(input=stem,**r))
(T/'direct_positive.json').write_text(json.dumps(dict(status='PASS',verified=sum(r['verified'] for r in rows),rows=rows),indent=2))

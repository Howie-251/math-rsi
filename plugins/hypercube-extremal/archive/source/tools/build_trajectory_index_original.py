"""Read-only extraction of historical Q4 evidence; writes only this handoff directory."""
from pathlib import Path
import json
import hashlib
from decimal import Decimal, getcontext
getcontext().prec = 50
OUT = Path(__file__).resolve().parent
ROOTS = {
    'completion_20261027': Path('E:/上界/Q4_059970530_research/Q4_059970530_research'),
    'orientation_20261027': Path('E:/上界/Q4_refined_research_20261027/Q4_refined_research_20261027'),
    'polish_20261028': Path('E:/上界/optimization_20261028_q4'),
    'control_20261028': Path('E:/上界/q5_empty_moment_20261028'),
}
def read(p):
    return json.loads(p.read_text(encoding='utf-8'))
def source(p):
    return {'path': p.as_posix(), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}
records=[]
for stage, filename, label in [
    ('completion_20261027','certificate_six.json','完整补全，旧六块控制'),
    ('completion_20261027','certificate.json','完整补全，新增45与9阶块'),
    ('orientation_20261027','certificate.json','保留共同根相对朝向，完整五种根面'),
    ('polish_20261028','certificate28a.json','同一模型中间认证'),
    ('polish_20261028','final_certificate.json','同一模型精修认证'),
    ('control_20261028','certificate_control.json','最终纯Q4控制认证'),
]:
    p=ROOTS[stage]/filename; d=read(p)
    n,dn=d['upper_numerator'],d['upper_denominator']
    records.append({'stage':stage,'label':label,'source':source(p), 'exact':f'{n}/{dn}',
      'decimal_exact':str(Decimal(n)/Decimal(dn)), 'outward_decimal':d.get('upper_decimal_ceil_8'),
      'dimensions':d['dimensions'],'gram_denominator':d['gram_denominator'],
      'q5_cut_count':len(d.get('q5_cuts',[])), 'floating_upper':d.get('floating_upper_before_rounding',d.get('numerical_search_upper')),
      'sdp_optimality_proved':False})
histories=[]
for stage,root in ROOTS.items():
    for p in sorted(root.glob('*history.json')):
        if stage=='control_20261028' and p.name!='final_control_history.json':
            continue
        data=read(p)
        duplicate = next((h['source']['path'] for h in histories if h['source']['sha256']==source(p)['sha256']),None)
        histories.append({'stage':stage,'source':source(p),'duplicate_of':duplicate,
          'record_count':len(data),'records':data,
          'count_warning':'数值求解日志条数，非ARIS审稿轮数；seconds通常为本次进程累计墙钟，不能逐行求和。'})
evidence={}
for stage,names in {
 'completion_20261027':['standalone_verification.log','six_verification.log','joint_shadow_summary.json','variant_audit.json','completion_summary.json','研究报告.md'],
 'orientation_20261027':['verification.log','folding_audit.json','final_metrics.json','horn_pricing.json','horn_psd_repair_pricing.json','研究报告.md'],
 'polish_20261028':['certificate28a.json.log','final_certificate.json.log','run_manifest.json','continue_joint.py'],
 'control_20261028':['verification_control.log','result_control.json','run_manifest.json','column_lift.py'],
}.items():
    evidence[stage]=[source(ROOTS[stage]/n) for n in names]
obj={'scope':'Q4历史与纯Q4 control；排除Q5/Q6研究尝试。历史日志审计，不代表本次重新运行整数穷举。',
 'literature_baseline':{'value':'0.60318','attribution':'Baber, arXiv:1201.3587v2, Theorem 4.1','evidence_level':'本地研究报告引用；本任务未联网复核优先权'},
 'certificates':records,'histories':histories,'evidence':evidence,
 'unresolved_numbers':[{'value':'0.5916766','status':'未在指定历史证书、报告、日志中定位，不能替代0.59167941576459375'}],
 'aris_provenance':{'q4_review_rounds':None,'q4_token_usage':None,'cross_model_review':None,
   'status':'可核对求解代码/日志/证书迭代；未定位这些Q4阶段逐调用ARIS请求响应档案。其他任务审稿不得移植。'},
 'best':records[-1]}
(OUT/'trajectory.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Extracted',len(records),'certificates and',len(histories),'history files.')

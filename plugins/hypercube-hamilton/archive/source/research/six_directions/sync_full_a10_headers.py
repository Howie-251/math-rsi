"""Publish only accepted full A10 and ten-hole combined coverage state."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
d=json.loads((R/'RUN_STATE.json').read_text(encoding='utf-8'))
assert d['q5_a10_proved'] and d['q5_all_balanced_hole_endpoints_proved']
assert d['covered_ten_geometry_residual']['remaining']==41236 and not d['full_p6_proved']
note=('2026-11-01 最新已接受：**完整五维 A10 已独立汇总审计 PASS，55/55 几何全部关闭**。'
      '最后轨道由 1024 个合法短补森林及 GF(2) 满秩矩阵覆盖全部任意匹配；独立重算全部 1048576 个矩阵项。'
      '结合已接受 A8 与高孔归约，所有可行五维奇偶孔数差二的指定避一孔定理、所有平衡孔数的指定端点路径及整圈延拓均已接受。'
      '新 T63 标记切分及完整五维端点应用分别新增 12916、70 个十孔覆盖目标几何，互不重叠；'
      '**当前剩余 41236 = 12910 + 12696 + 15630**。'
      '见 `Q5_A10_FULL_REVIEW.md`、`Q5_T63_COMPLETE_SPLIT_REVIEW.md`、`TEN_COVERED_Q5_ENDPOINT_REVIEW.md`。'
      '**完整十孔、12/14/16/18 孔及完整 Q6/P6 仍 OPEN**；下一步为实际多避孔输入的短森林秩证书。'
      '保证等级 same-family/provisional，相对于显式导入与确定性有限证书，非形式化验证。以下冲突状态为历史。\n\n')
for name in ['NEXT_OBLIGATIONS.md','HIGHER_HOLE_CURRENT_PROGRESS.md','TEN_HOLE_COVERED_NEXT.md','POST_A8_ROUTE_PRIORITIES.md']:
    p=R/name;s=p.read_text(encoding='utf-8');head,body=s.split('\n',1)
    if not body.lstrip().startswith(note.strip()):p.write_text(head+'\n\n'+note+body.lstrip(),encoding='utf-8')
p=R.parent.parent/'PROOF_PACKAGE.md';s=p.read_text(encoding='utf-8');head,body=s.split('\n',1)
main=note
for file in ['Q5_A10_FULL_REVIEW.md','Q5_T63_COMPLETE_SPLIT_REVIEW.md','TEN_COVERED_Q5_ENDPOINT_REVIEW.md']:
    main=main.replace('`'+file+'`','['+file+'](research/six_directions/'+file+')')
if not body.lstrip().startswith(main.strip()):p.write_text(head+'\n\n'+main+body.lstrip(),encoding='utf-8')
print('Full A10 and exact 41236 remaining coverage published to mutable progress headers.')

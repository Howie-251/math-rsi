"""Update mutable progress headers after finalized, hash-checked reviews."""
from pathlib import Path
R=Path(__file__).resolve().parent
note=('2026-11-01 最新已接受：完整 A8 的平衡八孔端点后果及十孔应用已独立审计 PASS，'
      '十孔覆盖目标残余由 91225 减为 **54222**（v=1/7/31 分别 16920/17022/20280）；'
      'A10 前两个轨道已独立审计 PASS，55 个非邻接规范几何已关闭 50 个，剩 **5 个、1 个轨道**。'
      '第二轨道 2366577 条正圈及完整规范域均独立核验。'
      '见 `Q5_A8_CONSEQUENCES_REVIEW.md`、`A10_FIRST_ORBIT_REVIEW.md` 与 `A10_ORBIT2_REVIEW.md`。'
      '以上数量是几何数，已关闭几何覆盖其全部实现匹配。完整 A10、完整十孔及完整 P6 仍 OPEN；'
      '保证等级 same-family/provisional，相对于显式导入与有限证书，非形式化验证。以下冲突进度为历史。\n\n')
for name in ['NEXT_OBLIGATIONS.md','HIGHER_HOLE_CURRENT_PROGRESS.md','TEN_HOLE_COVERED_NEXT.md']:
    p=R/name;s=p.read_text(encoding='utf-8');head,body=s.split('\n',1)
    if not body.lstrip().startswith(note.strip()):p.write_text(head+'\n\n'+note+body.lstrip(),encoding='utf-8')
p=R.parent.parent/'PROOF_PACKAGE.md';s=p.read_text(encoding='utf-8');head,body=s.split('\n',1)
main=note.replace('`Q5_A8_CONSEQUENCES_REVIEW.md`','[A8 后果审计](research/six_directions/Q5_A8_CONSEQUENCES_REVIEW.md)').replace('`A10_FIRST_ORBIT_REVIEW.md`','[A10 首轨道审计](research/six_directions/A10_FIRST_ORBIT_REVIEW.md)').replace('`A10_ORBIT2_REVIEW.md`','[A10 第二轨道审计](research/six_directions/A10_ORBIT2_REVIEW.md)')
if not body.lstrip().startswith(main.strip()):p.write_text(head+'\n\n'+main+body.lstrip(),encoding='utf-8')
print('Mutable progress headers synchronized; frozen proof inputs unchanged.')

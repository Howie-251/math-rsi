"""Synchronize mutable progress headers from the validated acceptance ledger."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
d=json.loads((R/'RUN_STATE.json').read_text(encoding='utf-8'))
res=d['covered_ten_geometry_residual']
if d.get('full_p6_proved'):
    assert d['remaining_full_p6_hole_levels']==[]
    assert d['final_p6_acceptance']['full_p6_proved'] is True
    assert all(d.get(k) for k in ('full_fourteen_hole_proved','full_sixteen_hole_proved','full_eighteen_hole_proved'))
    note=('2026-11-02 最新已接受：**完整 Q6 核心命题 P6 已通过 ARIS 独立总装审计。** '
          '对任意 $M\\subseteq E(Q_6)$、任意未被 $M$ 覆盖的顶点 $u$、'
          '任意与 $u$ 奇偶性相反的顶点 $v$（可以已被 $M$ 覆盖），'
          '存在包含 $M$ 全部边的 Hamilton $u$–$v$ 路径。'
          '完整2、4、6、8、10、12、14、16、18孔层均已接受；保持起点自由的极大补全归约覆盖任意原匹配。'
          '总证明见 `P6_FULL_CLOSURE.md`，独立审计见 `P6_FULL_REVIEW.md`，'
          '最终状态核验见 `P6_RELEASE_CHECK.json`。'
          '十四孔与十六/十八孔总装分别见 `FOURTEEN_HOLE_FULL_REVIEW.md`、`SIXTEEN_EIGHTEEN_FULL_REVIEW.md`。'
          '**当前 P6 证明义务为空。**')
elif d.get('full_twelve_hole_proved'):
    assert d['twelve_hole_geometry_residual']['covered_remaining']==0
    note=('2026-11-02 最新已接受：**完整 Q6 十二孔层已通过独立汇总审计**，'
          '对任意26条短边匹配、任意自由起点与任意异奇偶目标（包括已覆盖目标），'
          '均有包含原匹配的 Hamilton 路径。最后235个几何由完整3,620,052个局部极大匹配的正证书及已审拼接归约关闭。'
          '见 `TWELVE_HOLE_FULL_CLOSURE.md` / `TWELVE_HOLE_FULL_REVIEW.md`。'
          '**完整2/4/6/8/10/12孔层已关闭；完整 Q6/P6 仍 OPEN，剩余完整层为14、16、18孔。**')
elif d.get('twelve_hole_free_targets_proved'):
    rr=d['twelve_hole_geometry_residual']
    note=('2026-11-02 最新已接受：**完整 Q6 十二孔自由目标分支已通过独立汇总审计**，'
          '对任意26条短边匹配和任意两个指定异奇偶自由端点，均有包含匹配的 Hamilton 路径。'
          '见 `TWELVE_HOLE_FREE_CLOSURE.md` / `TWELVE_HOLE_FREE_REVIEW.md`。'
          f'十二孔覆盖目标在已审路线下精确剩余 **{rr["covered_remaining"]}** 个几何，分目标 {rr["covered_by_target"]}，'
          f'见 `{rr["review"].replace(".json",".md")}`。'
          '完整2/4/6/8/10孔层及所有已接受五维输入保持关闭。'
          '**完整 Q6/P6 仍 OPEN，剩余完整层为12、14、16、18孔；自由分支不能代替完整十二孔前层。**')
elif d['full_ten_hole_proved']:
    assert res['remaining']==0
    note=('2026-11-01 最新已接受：**完整 Q6 十孔层已通过独立汇总审计**，涵盖任意27条短边匹配、'
          '任意自由起点与任意异奇偶目标（含已覆盖目标）。十孔自由与覆盖目标均无剩余。'
          '见 `TEN_HOLE_FULL_CLOSURE.md` / `TEN_HOLE_FULL_REVIEW.md`。'
          '完整五维 A8/A10 及所有平衡孔数端点/圈、可行奇偶孔差二避一孔输入保持已接受。'
          '**完整 Q6/P6 仍 OPEN，剩余完整层为12、14、16、18孔。**')
else:
    note=('2026-11-01 最新已接受：完整五维 A8/A10 与全部平衡孔数端点/圈、可行奇偶孔差二避一孔输入已关闭。'
          f'六维十孔覆盖目标当前精确剩余 **{res["remaining"]}** 个几何，分目标为 {res["by_target"]}。'
          f'最新接受范围见 `{res["review"].replace(".json",".md")}`。'
          '完整2/4/6/8孔及十孔自由目标已接受；完整十孔、12/14/16/18孔及完整P6仍OPEN。')
if not d.get('full_p6_proved') and d.get('fourteen_hole_geometry_residual'):
    fr=d['fourteen_hole_geometry_residual']
    note+=(f' 十四孔最新已接受余域：已覆盖目标 **{fr["covered_remaining"]}** 个几何，'
           f'自由目标 **{fr["free_remaining"]}** 个几何，见 `{fr["review"].replace(".json",".md")}`。')
    if d.get('fourteen_hole_free_targets_proved'):
        note+=' **十四孔任意两个指定异奇偶自由端点分支已关闭**；已覆盖目标分支仍待完成。'
if not d.get('full_p6_proved') and d.get('complete_sixteen_hole_implies_complete_eighteen_hole_proved'):
    hr=d['sixteen_hole_conditional_geometry_residual']
    note+=(f' 已审条件递推：**完整十六孔推出完整十八孔**；以完整十四孔为前提，十六孔已审路线剩 **{hr["covered_remaining"]}** 个覆盖目标几何，自由目标余域为0。'
           '前层条件尚未解除，不能将十六/十八孔记为完整关闭。见 `HIGHER_POST12_T39_REVIEW.md`。')
note+=' 保证等级 same-family/provisional，相对于显式导入与确定性有限证书，非形式化验证。以下冲突状态为历史。\n\n'
for name in ['NEXT_OBLIGATIONS.md','HIGHER_HOLE_CURRENT_PROGRESS.md','TEN_HOLE_COVERED_NEXT.md','POST_A8_ROUTE_PRIORITIES.md']:
    p=R/name;s=p.read_text(encoding='utf-8');head,body=s.split('\n',1)
    if not body.lstrip().startswith(note.strip()):p.write_text(head+'\n\n'+note+body.lstrip(),encoding='utf-8')
p=R.parent.parent/'PROOF_PACKAGE.md';s=p.read_text(encoding='utf-8');head,body=s.split('\n',1)
main=note
for name in ['P6_FULL_CLOSURE.md','P6_FULL_REVIEW.md','P6_RELEASE_CHECK.json',
             'FOURTEEN_HOLE_FULL_REVIEW.md','SIXTEEN_EIGHTEEN_FULL_REVIEW.md',
             'TEN_HOLE_FULL_CLOSURE.md','TEN_HOLE_FULL_REVIEW.md',res['review'].replace('.json','.md'),
             'TWELVE_HOLE_FREE_CLOSURE.md','TWELVE_HOLE_FREE_REVIEW.md',
             'TWELVE_HOLE_FULL_CLOSURE.md','TWELVE_HOLE_FULL_REVIEW.md',
             d.get('twelve_hole_geometry_residual',{}).get('review','').replace('.json','.md'),
             d.get('fourteen_hole_geometry_residual',{}).get('review','').replace('.json','.md'),
             'HIGHER_POST12_T39_REVIEW.md']:
    main=main.replace('`'+name+'`','['+name+'](research/six_directions/'+name+')')
if not body.lstrip().startswith(main.strip()):p.write_text(head+'\n\n'+main+body.lstrip(),encoding='utf-8')
print(json.dumps({'full_twelve_hole_proved':d.get('full_twelve_hole_proved',False),'fourteen_hole_geometry_residual':d.get('fourteen_hole_geometry_residual'),'full_p6_proved':d.get('full_p6_proved',False)},ensure_ascii=False))

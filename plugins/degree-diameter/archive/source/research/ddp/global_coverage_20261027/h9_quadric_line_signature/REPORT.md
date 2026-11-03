# 675 个 non-star 附件恢复为环境二次曲面直线

事前冻结的 **P_Qline 在675/675个现有对象上全部命中**。这些点（41502..42176）的核心邻集 A_i 均包含 Q(6,9) 上一条 totally singular projective line 的完整 partial-fold 像；余下邻点可精确分成 anchors。675条选中的线全部不是 H(9) 的 incidence lines，故不与此前否定的 P_line 冲突。

这是从成功 source 恢复出的具体邻接规则，不是新图或新下界；没有执行新—新距离检验、候选池筛选或优化。该规则的全局路由证明由同问题的另一代理单独研究，本报告的实际计算只认证几何与邻接分解。

## 覆盖对象和结果

| 项目 | 数量 |
|---|---:|
| 实际检验的原 non-star 段 | 675 |
| 含完整 Q-line 像 | 675 |
| 选中 line 的 folded-image 大小10 / 7 | 657 / 18 |
| anchors 为0 / 1 / 2 / 3 / 4 | 25 / 230 / 412 / 7 / 1 |
| 选中 line 属于 H9 incidence lines | 0 |
| 不同选中原始 lines / 不同 folded-images | 675 / 675 |

每个 A_i 找到**一条就停止该对象的候选枚举**。因此只证明每个 A_i 至少需一条已找到的 line 即可解释其 line 部分，不能声称该 line 唯一，也没有完整列出一个 A_i 可能容纳的所有 lines。25个对象无需 anchors，其余650个需要在当前这份 witness 分解中另列 anchors；不声称 anchors 在所有路由中都不可删除。

18条像大小为7的选中线全部被坐标 Frobenius 固定，其余657条不固定。前者是环境 Q 上的 F3-defined lines，仍非 H9 incidence lines；故其缩小像并不违反旧 H9-line 筛选的固定线例外处理。

首个41502的分解尤其直接：A 恰等于一条 line 的10个不同 folded images，无 anchors。原始 point labels 是

`[7,7051,13366,19772,26816,33131,39534,46578,52893,59541]`。

可用 normalized 坐标

`p=(1,0,0,0,0,0,7)`，`q=(1,1,0,6,0,2,4)`

定义该线。F9 元素以 x+3y 编码 x+yt，t²=−1；生成全部 [p+tq]（t∈F9）与 [q]，折叠后恰得

`[7,4212,8259,12377,12453,19260,19421,25736,26058,36805]`。

完整10个原坐标、labels、像、anchors及定义 pair 均在 `first41502.json`；所有675份在 `RESULT.json`。

## 确定的坐标与 fold 校准

只复写原作者 `build_hexagon` 的有限域和 **points** 枚举片段，不导入 verifier，也不调用它后续的 H9 lines / incidence 构造。按首个非零坐标为1的作者次序枚举597871个 PG(6,9) 候选，用

`X0*X4 + X1*X5 + X2*X6 = X3²`

筛得66430个 points。用现存 τ 对全部66430个 point 校准：逐坐标 cubing 所得 point 的作者编号与 τ²(p) 完全一致。无需任何关联图邻接。

partial-fold π 使用已有7959 split 状态：H(3) point 与 split pair 的两点各保留自身 label，未 split pair 合并为 min(p,φp)，再将所有保留 labels 排序为0..41355。此为作者 `partial_fold` 的明确编号约定；`Q_data.json` 中 generic representatives 与 `witness12_state.json` 的顺序相配，未重新求 S/c。σ 的颜色会影响核心边，但不影响这一 π；本次识别不需重建 σ 关联邻接。核心 K 与现有 source 的对应继承此前已完成的逐边共同核心核对，本轮没有重做该核对。

每个 line 的 H9/non-H9 判定直接用原文六条 Plücker 等式，675份选中 witness 均失败至少一式。因此环境 Q-line 比 H9 incidence-line 的实际范围更大；“φ 固定 line 必含完整 star”的旧例外论证只针对 H9 incidence lines，不能套到所有环境奇异 lines。

## 完整候选规则及实际成本

针对每个 A_i，枚举**所有不同 pins 的原始 point lifts 两两组合**。每个 pin 有1或2个 lifts。两个不同 projective points 唯一确定一条线，生成其10点，逐点检查 Q 方程、求 π 像，再检查像⊆A_i。

候选规则完整：partial fold 每个 fiber 至多含2个原点，所以10点 line 的像至少有5个不同 pins。任何合格 line 必包含 A_i 中某两个不同 pins 的一对原始 lifts。故即使存在 anchors 或像小于10，也不会因只取两个预选 pins 而漏检；本实现不是只用前两个 pins。

本批实际尝试11745对 lifts、生成2103条去重后的有效 Q-line 候选，找到675个 witnesses。CPU0.619809秒、单worker；未用满预算。小缓存 `point_coords.u8.bin` 保存66430×7个 uint8 坐标，`point_to_core.u16.bin` 保存66430个 native-endian uint16 fold labels，方便直接复用，避免再次预热。

## 不依赖源邻接的生成 API

`geometry.py` 给出 literal deterministic API：

```python
from geometry import line_attachment, read_cached_fold
fold = read_cached_fold('point_coords.u8.bin', 'point_to_core.u16.bin')
attachment = line_attachment(
    (1, 0, 0, 0, 0, 0, 7),
    (1, 1, 0, 6, 0, 2, 4),
    fold,
)
# attachment['point_coordinates']: 全部10个 normalized points
# attachment['pins']: 按 fold 去重后的核心邻点
```

API 只接受两点坐标和 coordinate→core fold 映射，不读取 source 邻接或675份 A_i。`line_points` 拒绝不全落在 Q 上的 span；`line_attachment` 不自动加 anchors。`api_calibration.json` 保存首41502与既有 witness 的10点/10pins完全一致对照。若以后用该 API 生成新附件，仍必须独立处理核心度预算、anchors选择和所有新类之间的D5覆盖；本批没有执行这些后续步骤。

## 结论边界

已恢复：固定共同 K 内，成功 source 的整块675个 non-star 附件均有“环境 Q-singular line 像 + 0..4 anchors”的显式几何分解，675份可以逐项重新生成。未恢复：作者选择哪675条 lines、anchors 的批量公式、完整度负载设计，以及新—新全局覆盖证明。也没有检验其余135个 non-stars。新下界仍为0。

未执行下一项 flat-plane Π_y 预测，也未枚举所有 Q-lines。冻结预测、实际识别代码、小缓存、API与全部见证均留在本目录；不修改 Wiki、root计划或旧675 witnesses。

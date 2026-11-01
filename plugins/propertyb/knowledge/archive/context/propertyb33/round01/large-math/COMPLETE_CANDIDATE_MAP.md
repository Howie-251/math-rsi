# T33：23、24点候选闭合与形式化交接

2026-10-08。本轮负责的剩余数学已形成覆盖23、24点全部分支的完整候选。所有新结论仍是纸面候选与精确局部证书；23/24点的实际连接尚未在Lean实现，也尚未送Grok/Gemini完成跨家族审阅。已完成的19–22、25点Lean保持不变。本文件是主代理审阅及继续形式化的导航。

## 23点的完整分支树

点对覆盖保证每点度数至少6。设r为六度点数、t为七度点数，则

165=Σd(v)≥6r+7t+8(23−r−t)=184−2r−t，

故2r+t≥19。以下分支穷尽r的所有非负整数值。

| 真实分支 | 完整候选入口 | 关键局部证据 |
|---|---|---|
| r≥4 | `TWENTY_THREE_FOUR_SIXES.md` | 464有标号/50代表/3176实际坏槽输入；131不同caller独立ABC；最坏4183/4199 |
| r=3，t≥13 | `TWENTY_THREE_THREE_SIXES.md` | 三低两高844有标号/372代表；全部8556行独立ABC；最坏43753/43758 |
| r=2，t≥15 | `r123-child/TWENTY_THREE_TWO_SIXES.md` | 两低三高412有标号/208代表；4784行独立ABC、4个exact dual；最坏7292/7293 |
| r=1，t≥17，六度x有七度非单位邻居 | `TWENTY_THREE_LOW_WITH_SEVEN_BAD.md` | 十点有色图选点；完整296有标号/194代表，真实禁止条件保留130代表；全部strict，最坏21877/21879 |
| r=1，t≥17，x与全部七度单位 | `r123-child/TWENTY_THREE_ONE_SIX_ALL_SEVENS_UNIT.md` | 75个含λ3五锁先排除；四份defect1选5高；六锁1430有标号/243代表；318实际赢家7314行独立ABC、1个exact dual；最坏19439/19448 |
| r=0，t≥19 | `TWENTY_THREE_MANY_SEVENS.md` | λ≥3排除→P3排除→团并→三团moment或多团选点；102实际赢家2346行独立ABC；最坏24307/24310 |

反复使用的七度点对λ≥4排除，在 `TWENTYTHREE_HIGH_PAIRS.json` 中只取λ=4,5,6,7四行。λ=3行本身没有通过，必须按各分支的真实多锁选点另行处理。

## 24点的完整分支树

点对覆盖给最小度6，总度165给r≥3和2r+t≥27。

- r≥5：`TWENTY_FOUR_AT_LEAST_FIVE_SIXES.md`。六度bad图为匹配；有单位四集时处理全pair、单triple、quad；没有单位四集时只剩五低两matching的完整51局部域。
- r=3或4：t≥21或19，满足主代理 `proofs/propertyb33/TWENTY_FOUR_MANY_SEVENS.md` 的t≥18条件。

因此两份条件候选覆盖24点全部实际输入。

### 可简化Lean的全pair四低证书

原 `AVERAGED_LOCK_ORDER.md` 的441/442平均界成立，独立审阅已核对其随机中心条件分布及Jensen方向。为了避免新增概率混合接口，现在另给直接局部证书：

- `adaptive_four_pairs.py` 枚举每个中心7种真实坏槽，覆盖全部7⁴=2401槽元组；
- 所有元组都能在固定窗口11–14的24个标签序中找到严格赢家；
- 最坏8301/8398；12个实际caller的A/B/C独立复算；
- 原始结果 `ADAPTIVE_FOUR_PAIRS.json`。

该形式直接复用单triple448输入及五低119输入的“实际坏槽→位置证书→CustomDeletion”接口，无需新建随机排列混合定理。平均方法可以保留为数学解释。

## 需要的最小Lean新增连接

1. **实际选点。** 依上述分支证明低度/七度集合计数、单位邻居选择、十点有色图引理、四份defect1分组及三团moment选择。不能把选出的类型作为顶层额外前提。
2. **完整pair预算递归。** 在有限锁点上记录真实迹重数；逐个大迹或首个剩余pair递归，其总pair余量严格下降。单元与空迹由实际度数及33边唯一恢复。二元迹允许重复；三低triangle的三元迹也可能重复。六锁全6迹不合法，实际边仅5点。
3. **实际坏槽。** 为结构保证存在的坏边对记录实际类型；枚举的是有限槽，不是整图。槽容量为C(n_t,2)或n_t n_u，共享另一锁的槽权重仍为0。按实际输入选择位置后，再应用旧概率定理。
4. **avoided-lock配额与有理dual。** `REFINED_DELETION_CERTIFICATES.md` 给出精确纸面证明。有限子族F_R位于v−1−|R|点，配额ceil((4|F_R|−(v−1−|R|))/3)。任意非负α的主项减逐槽容量罚项，给实际可删权重下界。只需证明这一通用有限不等式，数值证书由内核算术核验；LP不进入可信证明。
5. **最终caller。** 新损失需要证明 `CustomDeletion.propertyB_of_custom_deletion` 的 `center_lower`，绑定到实际 `directedBadPairs`。然后装配23、24点定理与已有 `ThirtyThree.Assembly`。

形式化可直接使用全部有标号局部域，避免证明数百代表的同构分类；若使用代表，必须补齐实际标签等价及完整域的覆盖见证。这里列出的独立复算验证算术，不代替这个覆盖义务。

## 独立审查范围

- `candidate-audit/REPORT.md`：24≥5six与23≥19seven的完整结构、随机平均、局部域覆盖、三团不等式、43个中心exact dual回放；未发现实质数学错误。
- `candidate-audit/LOW_HIGH_COLORED_SELECTION.md`：十点着色引理、真实y边颜色绑定、194局部型的完整域与130适用型。
- `candidate-audit/ONE_LOW_ALL_UNIT_SELECTION.md`：四分组与λ3排除；独立重建1430个六锁有标号输入及75个含λ3五锁代表的全部局部域，核对r=1两个分支穷尽。
- `candidate-audit/C4_SELECTION.md`：早期剩余路线的正确选点与压缩结构反例，保留为失败路线经验；最终完整分支树不依赖排除那些残余C4坏槽。

以上均是same-family、provisional。Grok/Gemini由主代理统一组织；本代理未重复调用。没有读取、修改或干扰aris4math_v2。

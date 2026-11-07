# v4 临界取等：research-review Step 3 意见（数学维护适配）

**结论：**现有的 v4 基础段落和 Happy Ending 执行说明大体正确，可以直接采用。我找到 3 处真实缺口，都在“交换之后怎样定位被迫出的见证”和“追下一层”两步：

- **情形排除可能循环引用：**关闭各情形用的引理，必须在交换之前独立证出，不能拿本次交换要导出的矛盾当前提。目前只有 HE 插件写了这条，基础文件没有。
- **被迫见证的情形没有穷尽：**基础文件没有要求按新域 F 的不交分块逐块关闭。
- **下一层没有重算松弛：**排除 n=B 后再追 B−1，原来闭合的链会多出一单位空间，上一层的单射/精确覆盖不能照搬。

另有 1 处文档过时（DOMAIN_ROUTING 第 23 行）。DD 内容放进原插件、不加基础规则，这个处理是对的。

**执行身份与范围：**我是 Antigravity 里的 Claude Opus 5.5，只做了静态阅读：没有改文件、没有运行程序、没有派作者，也没有保存 trace。按 composed 约定，下面的内容由 Root 并入 [EVOLUTION.md](file:///Users/rfy_naiveai/Desktop/MathRSI/development/evolution/v4-20261108/EVOLUTION.md)。Root 是什么模型家族我无法确认，独立性和接受状态请按 Root 实际路由记录，暂按 provisional。

---

## 0. 直接认可的部分（已对照原稿）

- **基础文件：**[critical-equality.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/references/critical-equality.md)、[prove L69–73](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L69-L73)、[route-loop L94–98](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L94-L98)、[verify L79](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L79)。
  - 都在原五阶段里增量接入，没有新增阶段或状态机。
  - 已写清：同一对象、不同选择的等号不能拼接、单射/集合相等/单例的翻译依据、端点覆盖与一般覆盖的区别、按同一端点选外部见证。
- **Happy Ending 插件：**[equality-exchange.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/happy-ending/skills/mathrsi-happy-ending/references/equality-exchange.md) 与原稿一致。我逐式核对了：
  - 全供给稿 (6)–(10)；
  - 替锁稿 (2)–(8)：F 的不交并、|F|=b+1、无 B5、r≤z、末前驱两种情形；
  - 边界情形 q=0、R=∅、d=p=0。
  - 状态始终保持 same-session/unreviewed/unaccepted。
- **DD：**[saturated-insertion-and-replay.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/references/saturated-insertion-and-replay.md) 与 FACTS 一致：最后一步没有 switch，2565/2566 两步有 switch；formal C 未完成；归属 v2+DD+PR7。没有在 base 重复加规则，正确。
- **不需要新增：**哈希、状态 JSON、单独的临界层 verify 流程、DD 的 base 规则。

## 1. 真实共性缺口与应接步骤

| # | 缺口 | 原稿证据 | 应接位置 |
|---|---|---|---|
| G1 | 情形排除引理必须先于交换、独立证出（防循环） | 替锁稿 §3 的 j∈S 情形，靠旧根稿 §1–3 先证的 z∉Ê∪F̂ 关闭；HE 参考 [L59](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/happy-ending/skills/mathrsi-happy-ending/references/equality-exchange.md#L59) 已写“不能用最终替锁矛盾反证其自身进口”。base 三处都没有这条 | critical-equality §3；prove 段落；verify 段落 |
| G2 | 被迫见证不一定经过新点，要按 F 的分块穷尽定位 | 替锁稿 (6)：先用 F∩T 定末点 r≤z，再按 F⊆S∪(U\L) 把末前驱 j 分两类。base §4 只写了第二次迫证“K∪{x}⇒经过 x”的做法 | critical-equality §4 开头 |
| G3 | 标出临界假设在哪一步被消耗；下一层要重算总松弛 | 全供给稿 (7)：ℓ0+r0=U0+V0−m 用到人口里的 “+1”，即 n=3b+1。t=0 稿 §4：上端变成 m+1，“原来迫单射的 m 等号不再得到”；§8 的策略审计记录了照搬 t=1 结构只得到必要条件。base §1 只有一句“分别说明剩余整数层” | critical-equality §1；route-loop 一句 |
| G4 | 冻结选择；供给集按全部实际见证定义，而不是某个选中的匹配 | 全供给稿 L52、L59：L、R 由全部实际路径定义，L→R 禁止的是全部路径，所以 \|L\|=ℓ0 才推出“最大匹配饱和每个端口” | prove 段落第 1 步（一句话） |
| G5 | 边界参数 | 原稿注明“初步 ℓ0/r0 可负”；AUD 审计覆盖了无 owner、空右供给、零缺额 | verify 段落一项 |
| G6 | 文档过时（Root 负责） | [DOMAIN_ROUTING L23](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/DOMAIN_ROUTING.md#L23) 仍写“只有聊天截图的新75/76记为待取得原稿”，与插件现状矛盾；L37/L46 的 HE 分支没有指向 equality-exchange（经由 base 参考 → HE 主技能 §5 仍可到达，属次要） | 改 DOMAIN_ROUTING |

**证据面：**这个方法目前只有 HE 一个领域的工作稿支持。base 参考已声明“不声称测得新题成功率提升”，范围恰当，不需要追加。

## 2. 最小必要条件与常见错误

**必要条件（缺一项，就不能宣布排除了临界层）：**
1. 目标量是整数；旧界 n≤B 无条件覆盖当前全部对象，不是浮点、条件版本或只覆盖部分分支。
2. 有一条闭合的不等式链，作用于同一母体和冻结的选择，并且 n=B 在其中被实际消耗。
3. 每个 “≤” 的差额都已证非负；总和是正系数的组合；取整步回到取整前的式子。
4. 从基数等式推结构时有依据：包含关系、映射关系、或非空纤维。
5. 交换合法：D⊆J、R 与保留部分不交、z 是新点；|F| 只在这些集合关系成立后才算；F 中所有禁形都保持，包括另一类型（例如无 B5 需要单独论证）。
6. 容量进口的全部假设在 F 上成立，再用逆否命题迫出见证 W。
7. 定位：情形穷尽 F 的分块；每个情形的关闭引理在交换之前已独立证明；“是端点”要靠端点覆盖加唯一命中点；“首/末”要靠角色排除。
8. 外部见证按同一个端点 k 选取；最后的矛盾确实达到禁形阈值。
9. 空集、零缺额、初步下界为负等边界参数都有处理。

**常见错误：**
- E1：左右分别取不同中间匹配，或用不同母体的等号拼成联合取等。
- E2：把 |A|=|B| 当成 A=B。
- E3：从取整后的等号推原式取等。
- E4：链两端不依赖 n=B 也相等，说明它是恒等式，不给出结构。
- E5：只算了 |F|=b+1，没证另一禁形不出现。
- E6：以为容量迫出的见证必然经过新增点。
- E7：把一般顶点覆盖当成端点覆盖；没有角色排除就定方向。
- E8：把“有私有 R5”写成“端点相容”。
- E9：情形关闭引理反过来依赖本次交换的矛盾，或用“对称可得”漏掉对称侧新增的异常角色。
- E10：下一层直接继承上一层的单射/单例。
- E11：矛盾差一个顶点。HE 中同端 B3+R5 只有 8，不是 weak7。
- E12：固定小反例或策略例 PASS，被当成原证明 PASS；或拿缺少临界条件的反例去反驳带条件的引理。

## 3. 可直接采用的技能段落

### 3a. 替换 [prove L69–73](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L69-L73)

```markdown
### 临界层的结构回收与容量迫证

**触发。** 原题量为整数，旧界 n≤B 已无条件覆盖当前全部对象，目标 n≤B−1；或推导已把反例逼到某个整数层。读取并执行[临界取等与相容见证](references/critical-equality.md)。旧界仍带条件、浮点或未覆盖分支时，先补该缺口，不进入本段。

**实际动作。**
1. 反设 n=B。在现用草稿开头写本链冻结的选择：母体、所用核/根/分划，以及按**全部实际见证**（而非某个选中匹配）定义的端口与容器。后续交换和定位只用这些选择；需要换选择时，重证受影响的等式。
2. 写同一对象上的整条链 Lo ≤ … ≤ Up，标出 n=B 在哪一步进入。把每个 ≤ 改写成已证非负的差额，正系数总和为零才逐项归零；取整步回到原式。
3. 兑现结构：像等于原集给单射，包含加等数给相等，非空纤维计数给单例，匹配下界取等给饱和全部端口。缺包含、共同选择或整数性，先补。
4. 给 proof-writer 或领域作者明确的删除 D、加入 R、新标记 z，要求证明 D⊆J、不交、|F|，以及 F 中**每一类**禁形仍被禁止，然后才用容量的逆否命题迫出见证 W。
5. 定位 W：按 F 的不交分块列出它的承重点（端点、前驱、新增点）可能落在哪些块，并穷尽。每块用一条**在定义 F 之前已独立证得**的排除引理，或用另一个实际域上的第二次容量迫证来关闭。“是端点”须有端点覆盖加唯一命中点，“首/末”须有角色排除；外部见证按刚定位的同一端点选取，并核最终禁形确实达到阈值。
6. 排除临界层后由整数性得 n≤B−1，接回原 caller。要追 B−1 时，按参考 §1 重算松弛，不继承本层的结构。

**产物。** 草稿中的一节，依次是：冻结选择；含非负项和 n=B 位置的链；结构引理；F 的定义与合法性；容量进口；情形表及每一情形的关闭引理（注明出处，以及是否先于交换取得）；边界参数（空集、零缺额、初步下界为负）；原题结算。

**谁消费。** 父调用者交 verify 逐箭头核对；领域细节由插件参考提供；当前任务 wiki 记录适用层、结构引理和失败边界。

**失败返回。** 缺非负性或共同选择：本义务内补证。交换破坏某个进口：把 F 和失效条件退给作者改操作，这不是原题反例。只得到“W 经过 z”，而 caller 需要端点：保留这个缺口，改定位。关闭某情形所需的引理尚未独立取得：列为新义务先证。下一层链的上端多出一单位：不复用本层结构，带着精确松弛式回 route-loop。
```

### 3b. 补入 [critical-equality.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/references/critical-equality.md)

**接在 §1 末（L11 之后）：**
```markdown
写链时标出 n=B 在哪一步被消耗。若不用 n=B 链两端也相等，它只是恒等式，不给临界结构。若 n=B 只进入一端，则在 n=B−j 时同一链的总松弛为 j。追下一层（j=1）时：若各非负项都是整数，恰有一项取 1，就按“哪一项吸收这一单位”分支，每支重建结构。凡是让原来给出单射/单例/精确覆盖的那段不等式重新获得一单位空间的支，不能再引用上一层的这些结论。两次把上一层结构搬到新层，都只得到同类必要条件时，带各支的精确松弛式回 route-loop。
```

**接在 §3 末（L29 之后）：**
```markdown
交换后用来关闭情形的“某类旧见证不存在”之类引理，必须在定义 F 之前，从临界假设和已得结构独立证明，并在正文写出证明位置；不能借用本交换要导出的矛盾。对称侧若有新增的异常角色，要分别写出，不以“对称可得”略过。
```

**放在 §4 开头：**
```markdown
被迫见证不一定经过新增点。先用 F 的显式不交分块和次序定位它的承重点（例如末点只能在 F 的某个角色交集里，于是前驱落在哪些块），列出全部可能块，各块之并要等于该点的全部可能位置。每块给一个关闭：已独立证明的排除引理，或在另一实际域上的第二次容量迫证。下面的端点定位用于这种第二次迫证。
```

### 3c. 替换 [verify L79](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L79)

```markdown
临界层证明按[取等与见证接口](../mathrsi-prove/references/critical-equality.md)核实际连接：旧整数界无条件覆盖原域；链在同一输入和冻结选择下闭合，且标明 n=B 的消耗点；每个归零项确实非负、系数为正，取整等式回到原式；基数等式到集合/映射结构有包含或映射依据；F 的不交、大小和全部禁形保持（含其它类型）；被迫见证的定位情形穷尽 F 的分块，每一情形关闭引理的证明不依赖本次交换；端点来自端点覆盖加唯一命中点，方向来自角色排除，外部见证兑现同一端点，最终禁形达到阈值；空集、零缺额、初步下界为负等边界参数都有处理。只核了人口式、一份匹配，或两条端点不同的路径时，相应箭头保持开放。失败时把具体链节返回原 prove，保留不受影响的结构。历史工作稿吸收进插件，不升级其审计状态。
```

### 3d. [route-loop L96](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L96) 的两处小改

- 把“旧界已经严格覆盖本次对象”改为“旧界已**无条件**覆盖本次对象”。
- 在该段末追加：
  ```markdown
  刚排除一层又要追下一层时，先在同一条链上重算总松弛；按吸收那一单位的非负项分支安排探针，不复用上一层的单射/精确覆盖。
  ```

### 3e. DOMAIN_ROUTING（Root 负责）

- **[L23](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/DOMAIN_ROUTING.md#L23)：**把“只有聊天截图的新75/76记为待取得原稿，不覆盖旧结构稿”替换为：
  ```markdown
  新75/76完整原稿在插件 archive/n7-20261103，状态 same-session/unreviewed/unaccepted；survey 只核 a16、b25 等进口，不把它当已审定理。
  ```
- **L37（路线迭代）追加：**
  ```markdown
  整数差一单位时，先按主技能 §5 追取等，不扩局部表；n=3b 一层重算预算。
  ```
- **L46（证明推进）追加：**
  ```markdown
  临界层交回同一母体的取等结构、替锁域 F、被迫路径及其端点，并核旧根排除先于替锁。
  ```

## 4. 实际阅读范围

- **全文读过：**
  - [EVOLUTION.md](file:///Users/rfy_naiveai/Desktop/MathRSI/development/evolution/v4-20261108/EVOLUTION.md)、research-review SKILL；
  - base 的 prove / route-loop / verify SKILL，以及 [critical-equality.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/references/critical-equality.md)；
  - HE 的 [mathrsi-happy-ending](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/happy-ending/skills/mathrsi-happy-ending/SKILL.md)、[happy-ending-certificate](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/happy-ending/skills/happy-ending-certificate/SKILL.md)、[equality-exchange.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/happy-ending/skills/mathrsi-happy-ending/references/equality-exchange.md)；
  - 两份 RESEARCH_SYNTHESIS（7576 UPDATE、AUDIT_WEIGHTED_UPDATE）；
  - 原稿：替锁稿、全供给稿、t=0 稿；
  - DD 的 [FACTS.md](file:///Users/rfy_naiveai/Desktop/MathRSI/development/homepage-redesign-20261105/reviews/dd-v4-20261107/intake/FACTS.md)、[dd-construction](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/skills/dd-construction/SKILL.md)、[saturated-insertion-and-replay.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/degree-diameter/references/saturated-insertion-and-replay.md)；
  - [DOMAIN_ROUTING.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/DOMAIN_ROUTING.md)。
- **部分读过：**HE 插件的 archive/n7-20261103/README.md（只核链接）、check_strategy_examples.py 前 30 行。
- **未读：**加权/增强根稿、旧根排除稿、AUD 依赖审计全文、R20 chart 稿、DD 的 archive 原件和 receipts；以上涉及的结论都按 FACTS 或插件转述。没有执行任何程序或重放。

## Memory update（reviewer）

- **已认可：**base 的临界取等接入范围；HE 执行说明的数学转写；DD 只放进插件。
- **未解：**G1–G3 尚未落到 base 文本；G6 文档过时。
- **新疑点：**无。下次复核只看 3a–3e 是否按原意落地，以及有没有引入 HE 专用常数。

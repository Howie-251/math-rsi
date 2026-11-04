**结论：** 先做一版范围小但内容扎实的 v3，再上线网页。网页里的成果页现在就可以同时起草。ECC 是同一个插件的两代，不需要拆成两个插件。以下只是建议，我没有改任何文件。

## A. 先后顺序

| 现在可以并行做 | 等 v3 落地后再做 |
|---|---|
| 六个主题的成果页文案和图意。数学事实已经整理在 [三案例 README](file:///Users/rfy_naiveai/Desktop/aris4math/mathrsi_new_results/_intake/three-cases-20261104/README.md) 和各案例的 VISUALS 里，与 v3 无关 | 网页“研究反馈线”里 v3 那一格 |
| 首页结构提案（README 里已计划由 Gemini 4 和 Opus 5.5 提） | 插件的使用和下载页，以及指向 ECC 插件的链接 |

理由是：v3 是这条迭代线上第二次真正走完“经验 → 改方法 → 再使用”的循环。网页先上线的话，v3 那一格要么空着，要么只能写成承诺。另外，ECC 插件现在还不能独立使用，读者点进去只会看到旧项目的路径代号。

## B. v3 的最小范围

先说一个观察：README 第 4 节列了 6 条“可进 base 的候选”，其中三项 v2 已经有了：
- “成员合法 ≠ 无遗漏”：[route-loop](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L88)，以及 ECC 插件第 94–108 行；
- 共同来源约束：route-loop 第 149–153 行；
- 在独立目录重放证书：[handoff §4](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md#L71-L85)。

把这几条筛掉，正是 meta-evolve §2“读到好经验不等于 base 缺这项能力”这一步的实际作用，可以如实写进 v3 的 EVOLUTION。真正的改动建议如下：

| # | 改动 | 证据 | 放在哪里 |
|---|---|---|---|
| 1 | **取商和规范化时同步运输所有共享结构。** 现在这条只写在 [ECC 插件](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/SKILL.md#L127-L141) 里。Erdős 的同步根稳定子（推进主要发生在约 0.59970 → 0.59168 这一步）和 Q6 的带根轨道、补全后伙伴身份改变，说明它是跨领域问题 | 三个领域 | 从插件提升到 base 的 route-loop Phase C 和 prove；根群、旗矩阵等具体内容仍留在领域里 |
| 2 | **工作集里的候选必须过全域门。** 分别记录受限域、全域和历史最佳三个值；违反的对象回流到下一轮；证书取最佳那一轮，不取最后一行 | Erdős 活动池约 0.59175，放到全域变成 0.83472 | base 的 prove/verify；列生成方法留在单题材料 |
| 3 | **先如实估算真实域的规模，再选证明机制，而不是继续扩大枚举。** 局部充分门失败后，里面合法的对象仍可以逐个实例当正证书用 | Q6：1024 个森林满秩，替代约 137 亿的完全匹配域；缺秩的池转成正证书 | 在 route-loop 第 90、94 行原段落上补一两句动作，Q6 例子进 [evidence-and-transfer](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md) |
| 4 | **把 ECC 插件第二代补成能独立使用的插件**（见 C） | 新发布包 | 插件 |

Happy Ending 我没有读到它的 LESSONS，它进 base、进插件还是只留作案例，交给 meta-evolve 分类时再判断。Erdős 和 Q6 先作为 base 的例子加只读案例存档，等真有同领域的下一题（比如 Q7、Q5 切面）再提炼成插件，这与 [PLUGIN_CONTRACT](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md#L83) 的说法一致。

整个过程从读 meta-evolve 开始：intake 阶段的阅读算作输入，不追认为已经按 meta-evolve 执行过。每项改动由协调者自己拿真实的小片段用一次，再对 diff 做一次 composed research-review。

## C. ECC：同一插件的两代

两波研究处理的是同一个对象、同一条归约链、同一批检查器，第二波深化的是验证、形式化和交接这一层。拆成两个并列插件会让两边重复写定理和失败机制。

现在只有三个文件意味着什么：[PLUGIN_CONTRACT 第 81 行](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md#L81) 自己就把 ECC 称为旧草案，并要求原始资料在仓内、不能只有一张来源路径表。而 [source-map](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/references/source-map.md#L3-L5) 写明大数据、搜索器和检查器都不在仓内，指向的是旧项目的路径代号。新发布包已经按相对路径整理好，正好用来补这一层：

- 参照 DD 的 archive 做法收进论文、两个 Lean 工程、172 母码数据、检查器和重放器；1.68GB 的见证列为省略的大文件并写明获取方式；
- 新增一个证书与 Lean 桥接入口，供 verify 调用；
- 把 fixed-parent 示例改成实际执行过的小命令，比如在新路径里重放一个母码的配对证书；
- 写入 42/16 的文献路线，45/11 写明仍开放。

版本不必绑定，插件的修订号写在插件自己的 README 里，例如：

```text
ECC 插件
- r1（base v1 时期）：领域指导草案，资料留在源项目。
- r2（随 base v3 发布）：收入五案例发布包、两个 Lean 工程和便携重放；
  新增证书/Lean 入口。依赖插件契约（v2 起）。
```

base 的发布说明里列出这次附带的插件修订号即可。

## D. 研究反馈线怎么讲

| 版本 | 吸收了哪些研究 | 方法上的变化 | 下一次实际使用 | 状态 |
|---|---|---|---|---|
| v0 | Property B、ECC 初始研究 | 各题独立的 skills | — | 已做 |
| v1 | 上面两题 | 5 个子工作流、PB 插件、ECC 草案 | ECC 后续研究（作者说明） | 已做 |
| v2 | DD | 新增 meta-evolve 并首次实际使用；四项 base 调用改动；DD 插件 | ECC 第二波 | 已做 |
| v3 | ECC 第二波、Erdős 86、Q6、Happy Ending | 第二次运行 meta-evolve；B 中的改动；ECC 插件 r2 | 下一题 | 待做 |

可以这样概括：

> MathRSI 每一版都来自上一轮真实研究的反馈。v0 用独立技能完成了 Property B 和 ECC 的初始研究；v1 把这两题的做法沉淀为五个自适应子工作流和领域插件；v2 新增 meta-evolve，并用它吸收 Degree–Diameter 的经验，把公开基线变化、对象改变后的证据继承、共同覆盖和直接 Lean 分支写回原有技能。ECC 研究在 v1/v2 的方法上继续推进：把已有的不存在性证明接到 Lean 和实际矩阵上，整理成可以独立重放的完整证书包，并整合 42/16 的文献路线。v3 将第二次运行 meta-evolve，把这些新研究中跨领域的经验写回 base 和 ECC 插件。

v3 那一句在落地前用将来时，落地后再改成完成时。

## E. 什么时候停 v3、切到网页

满足下面四条就收尾：
1. B 里的 1–3 都改在现有文件的实际调用处，上下游消费方同步更新；
2. ECC r2 能独立使用，至少有一条实际执行过的小命令；
3. v3 的 EVOLUTION 记下每项改动的一次使用和审阅处理，并写好 V3_CHANGES；
4. PLUGIN_CONTRACT 里 ECC 的“旧草案”描述改掉。

做 v3 期间冒出来的新想法，一律写进 EVOLUTION 的“下一轮”，不扩大本轮范围。历史断点评测、效率对比、Erdős/Q6 插件和 45/11 都明确不在 v3 里。

**实际读过的文件：** V2_CHANGES、meta-evolve SKILL、ECC 的 SKILL 和 source-map、PLUGIN_CONTRACT、三案例 README、ECC 的 EVOLUTION、Erdős 和 Ruskey–Savage 的 LESSONS、route-loop SKILL、handoff SKILL。没有读 verify、prove 的全文，也没有读 Happy Ending 的材料，所以第 2 项要以 meta-evolve 运行时对照 verify/prove 原文为准。


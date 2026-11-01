# T33：19点装配与22点结构选择

日期：2026-10-07。

## 已闭合的实际连接

`formal/Aris4Math/ThirtyThree/Assembly.lean` 导出：

- `RemainingGoal`：20≤v≤25，实际超图恰有33条边且覆盖点对时的Property B；目前仍是未证命题。
- `finite_goal_of_remaining`：实际调用新 `Nineteen.nineteen_propertyB` 处理v=19，把RemainingGoal接入已证的原始有限归约。
- `target_of_remaining_goal`：RemainingGoal → Target33。
- `target_iff_remaining_goal`：任意宇宙层级的Target33 ↔ RemainingGoal。

这将原目标的剩余范围精确缩到20–25点，并没有给RemainingGoal本身提供证明。模块名刻意使用Assembly，未创建容易误读为完成的新Main。

## 22点的新结构定理

`formal/Aris4Math/ThirtyThree/TwentyTwoStructure.lean` 中的
`Aris4Math.ThirtyThree.exists_two_locks_of_twenty_two` 接受任意有限类型上的实际H、点对覆盖、边数33、顶点数22，给出不同x,y，使共度为1且有如下三种度数组合之一：

    (6,6)、(6,7)、(7,7)。

它以原通用共度/度预算引理处理两类：

1. 有六度点x：x至少有18个共度1伙伴，若这些伙伴全为至少八度，总度至少168，与实际33边总度165矛盾。因此有度≤7的伙伴。
2. 无六度点：全部至少七度；从实际总度165推出至少11个七度点。任取七度点x，自己及坏伙伴共至多8点，从七度集合中删除它们仍有顶点。

此处证明了结构选择，不声称三种新类型的概率界已经成立，也没有得到22点可染性。

## 运行与验收

在 `formal/` 中，设置项目本地ELAN_HOME和PATH后执行：

```sh
lake build Aris4Math.ThirtyThree.Assembly
lake build Aris4Math.ThirtyThree.TwentyTwoStructure
lake env lean ../context/propertyb33/round01/reduction/next/ImportAudit.lean
```

对应日志为 `assembly-build.log`、`twenty-two-build.log`、`import-audit.log`。两个模块构建及独立导入审计均退出0；审计打印实际定义、声明类型和传递公理，并测试原始Bool染色caller以及Fin22上的真实锁对调用。

新装配、22点选点的传递公理均仅 `propext`、`Classical.choice`、`Quot.sound`。没有修改旧模块，没有新增 `sorry`、公理或 `native_decide`。这是现有环境的增量构建，不是另一机器复现。

跨家族审阅由主代理统一安排，本记录不自行记模型审阅通过。

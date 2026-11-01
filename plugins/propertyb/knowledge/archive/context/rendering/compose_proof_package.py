#!/usr/bin/env python3
"""Assemble one reader edition from the authoritative mathematical sources."""
from fractions import Fraction
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "PROOF_PACKAGE_FULL.md"


def read(path):
    return (ROOT / path).read_text()


def sections(text):
    parts = re.split(r"(?m)^## (.+)\n", text)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def relocate(text, folder=""):
    anchors = {
        "FORMAL_SPEC.md": "#spec",
        "proofs/PROBABILITY_LEMMAS.md": "#probability",
        "proofs/STRUCTURE_19_23.md": "#small-structure",
        "proofs/STRUCTURE_24_25.md": "#large-structure",
        "context/FORMAL_VERIFICATION_PROGRESS.md": "#lean",
    }
    def replace(match):
        label, href = match.groups()
        if href.startswith(("https:", "http:", "#")):
            return match[0]
        path = (ROOT / folder / href).resolve().relative_to(ROOT).as_posix()
        return f"[{label}]({anchors.get(path, path)})"
    return re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)", replace, text)


def chapter(anchor, title, body):
    return f'<div id="{anchor}" class="chapter-anchor"></div>\n\n## {title}\n\n{body.strip()}\n'


def subsection(title, body):
    return f"### {title}\n\n{body.strip()}\n"


def table_only(text):
    return "\n".join(line for line in text.splitlines() if line.startswith("|"))


def lean_section():
    source = read("formal/Aris4Math.lean")
    definitions = source[source.index("structure Simple5Hypergraph"):source.index("\nsection FiniteEvents")]
    definitions = re.sub(r"/--.*?-/", "", definitions, flags=re.S)
    definitions = re.sub(r"\n{3,}", "\n\n", definitions).strip()
    main = read("formal/Aris4Math/Main.lean")
    main = main[main.index("theorem finite_goal"):main.index("\nend Aris4Math")].strip()
    audit = read(".aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.log")
    axioms = "\n".join(line for line in audit.splitlines() if "depends on axioms:" in line)
    for filename in ("lean-main-build-meta.json", "lean-main-import-audit-meta.json"):
        assert json.loads(read(".aris/traces/proof-checker/2026-10-06_run09/" + filename))["exit_code"] == 0
    return r"""
### 形式化声明与原题的对应

Lean用有限集合的有限集合表示无重边超图，用布尔函数表示染色。下面直接展示
源码中的定义；`Fintype V`表示任意有限顶点类型，未限制顶点数。
因为每条边恰有五点，红点数介于1与4，恰好表示每条边均含两色。

```lean
""" + definitions + r"""
```

### 七个分支如何接回主定理

下面是`Main.lean`中的实际装配及三个主声明。`finite_goal`的中间条件由
第一章的约化提供；`target_of_finite_goal`消除这些条件，回到任意有限顶点集。
展开声明只保留五元简单超图和边数至多32，没有预选剖面、点对覆盖或概率界假设。

```lean
""" + main + r"""
```

`non_propertyB_edges_ge_thirty_three`直接证明不可二染色超图至少有33条边。
依据D3中$m(5)$的定义，这就是所需下界；项目没有另将极值函数定义为一个Lean对象。

### 纸面义务与形式化模块

| 义务 | 已完成的模块与作用 |
|---|---|
|任意有限超图的约化|`Reduction`、`Structure`、`SmallVertices`：重标号、合并点、补边、顶点数范围、至多18点排除|
|真实算法与条件排列计数|`Greedy`、`Counting`、`JointCounting`、`EndpointCounting`、`CriticalCounting`：实际事件及无放回计数|
|实际选点、类型及分类|`LowDegree`、`BlockClassification`、`K6Classification`、`K6Traces`、各`*Profiles`：实际输入与表中类型对应|
|坏边对的真实加权扣除|`LinkCounting`、`LinkDeletion`、`LinkWeightCertificates`、`ProfileDeletion`：数量、双方向、零槽及不重复扣除|
|精确界到染色存在|`Numeric`、`TypeCounting`、`ProfileProbability`、`ConditionalUnion`、`ProfileApplication`：精确公式、总界与原Property B|
|七个完整有限分支|`NoLocks`、`GlobalPairs`、`TwentyOne`、`TwentyTwo`、`TwentyThree`、`LargeVertices`|
|原命题T|`Aris4Math.propertyB_of_at_most_thirty_two`（`Main.lean`）|

### 构建及传递公理核验

已记录的默认`lake build`与另行导入`Main`的审计，退出码均为0。
默认构建目标是`Aris4Math.Main`；构建日志的1005个任务包含依赖缓存重放。
以下为四个顶层声明的实际传递公理输出：

```text
""" + axioms + r"""
```

`propext`是命题外延性，`Classical.choice`是经典选择，
`Quot.sound`是商类型的标准基础。依赖中没有`sorryAx`或项目自加公理，
也未使用`native_decide`。形式证明的基础是Lean内核与固定的Lean/Mathlib工具链；
模型审阅和反例搜索不参与这条逻辑依赖。

### 重现方法

工具链为Lean 4.24.0，Mathlib v4.24.0，`lake-manifest.json`固定提交
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。在本项目根目录运行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build
lake env lean ../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.lean
```

也可以新建以下独立审计文件，用`lake env lean 文件名.lean`检查：

```lean
import Aris4Math.Main
#print Aris4Math.Target
#check @Aris4Math.two_colorable_of_at_most_thirty_two
#check @Aris4Math.non_propertyB_edges_ge_thirty_three
#print axioms Aris4Math.propertyB_of_at_most_thirty_two
```

数学论证、形式声明与核验范围已经在本页展示。需要重新运行验证时，可使用
[主定理完整源码](formal/Aris4Math/Main.lean)、
[构建日志](.aris/traces/proof-checker/2026-10-06_run09/lean-main-build.log)、
[独立导入日志](.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.log)
和项目中的其余Lean模块。
"""


def arithmetic_appendix():
    cases = json.loads(read("results/reproduced_bounds.json"))["cases"]
    chunks = [r"""
本附录把每个配置的完整输入和逐位置有理数列在页内。根据P2–P7及第三、四章的类型表，
可直接核算这些有限和，无需打开外部JSON。分数保持精确值，不用浮点近似。

每行的$D_k$是实际已证明可扣除的下界，$C'_k=C_k-D_k$；
最后一列是$\min(A_k,B_k,C'_k)$。对最后一列求和即得$U$。
20点无锁配置已把$C_k$的单交有序对上限由992改为948。

共有21个成功配置；另保留23点两锁67、25点K6-4两个非成功配置，说明适用边界。
前者由66/677结构二分替代，后者由七点引理避开，均不用于推出$U<1$。
每个条目可单独展开；表格可横向滚动。
"""]
    assert len(cases) == 23
    for case in cases:
        rows = case["rows"]
        total = sum((Fraction(row["bound"]) for row in rows), Fraction(0))
        assert total == Fraction(case["corrected_bound"])
        assert all(Fraction(row["bound"]) == min(Fraction(row["A"]), Fraction(row["B"]),
                   Fraction(row["corrected_C"])) for row in rows)
        assert all(Fraction(row["C"]) - Fraction(row["deduction"]) ==
                   Fraction(row["corrected_C"]) for row in rows)
        assert sum(case["counts"].values()) == 32
        success = "成功配置" if total < 1 else "非成功配置"
        chunks.append(f'<details id="arith-{case["name"]}" class="arithmetic-case">\n'
                      f'<summary>{case["name"]} · {success} · U = {total}</summary>\n')
        positions = case["positions"]
        chunks.append(f'顶点数：{case["v"]}；锁定位置：{", ".join(map(str, positions)) or "无"}。'
                      f'普通总界：`{case["base_bound"]}`；最终总界：`{case["corrected_bound"]}`。\n')
        chunks.append("| 精确锁定类型（以位置表示） | 边数 |\n|---|---:|")
        for mask, count in sorted(case["counts"].items(), key=lambda item: int(item[0])):
            locks = [str(pos) for i, pos in enumerate(positions) if int(mask) & (1 << i)]
            label = "{" + ", ".join(locks) + "}" if locks else "∅"
            chunks.append(f"|`{label}`|{count}|")
        chunks.append("\n| k | A | B | C | D | C′ | min(A,B,C′) |\n"
                      "|---:|---:|---:|---:|---:|---:|---:|")
        for row in rows:
            chunks.append("|" + "|".join(str(row[key]) for key in
                          ("k", "A", "B", "C", "deduction", "corrected_C", "bound")) + "|")
        chunks.append(f"\n最后一列之和：**{total}**。\n\n</details>\n")
    return "\n".join(chunks)


def compose():
    overview = sections(read("PROOF_PACKAGE.md"))
    spec = sections(read("FORMAL_SPEC.md"))
    prob = sections(read("proofs/PROBABILITY_LEMMAS.md"))
    small = sections(read("proofs/STRUCTURE_19_23.md"))
    large = sections(read("proofs/STRUCTURE_24_25.md"))
    pieces = [r"""# 五元超图的32条边界：完整证明

**定理T。** 任意有限简单五元超图，只要边数至多32，就存在使每条边同时包含两色的二染色。因此$m(5)\ge33$。

证明的主线是：先把任意反例约化到19–25点，再证明每种结构都能选取适当锁点，
最后用条件随机排列的贪心染色给出严格小于1的失败概率上界。
最紧的成功分支为23点三锁配置，界为$645/646$。

本页包含数学规格、全部概率引理、结构分类、修正权重和完整算术明细。
数学对象与量词遵循`FORMAL_SPEC.md`；第一章将其规范内容直接列出。
Lean部分给出原始声明、顶层装配、核验结果和复现方法。

[规格与约化](#spec) · [概率引理](#probability) · [19–23点](#small-structure) ·
[24–25点](#large-structure) · [结论闭合](#closure) · [Lean核验](#lean) · [算术明细](#arithmetic)
"""]
    spec_parts = []
    for name, body in spec.items():
        if name.startswith("6."):
            body = body.split("\n\n具体候选分数与页码见", 1)[0]
        spec_parts.append(subsection(name, relocate(body)))
    pieces.append(chapter("spec", "一、数学规格与完整约化", "\n".join(spec_parts)))

    prob_names = {"Claim / Target": "范围与目标", "Invariant Object": "固定的概率对象",
                  "Assumptions": "假设与样本空间", "Notation": "记号",
                  "Proof Strategy / Derivation Map": "推导路线",
                  "Corrections or Missing Assumptions": "适用条件核对"}
    prob_parts = []
    for name, body in prob.items():
        if name in {"Status", "Independent Finite Checks", "Boundaries / Open Risks"}:
            continue
        body = relocate(body, "proofs").replace("本文只建立", "本节建立").replace(
            "所需概率接口，不证明该规格的主目标 T。",
            "所需概率接口；第三、四章给出结构输入，第五章接回主目标T。")
        body = body.replace("尚未用它宣称所有目标超图都拥有这种选择。", "相应锁点存在性在第三章中证明。")
        body = body.replace("脚本还独立重算全部位置的普通界及上述修改后的界，得到：",
                            "按P2–P7对全部位置求和，得到下表；逐位置精确值列于本页第七章。")
        prob_parts.append(body if name == "Proof" else subsection(prob_names.get(name, name), body))
    pieces.append(chapter("probability", "二、条件排列与概率引理 P1–P9", "\n".join(prob_parts)))

    small_parts = []
    for name, body in small.items():
        if name == "依赖与剩余验收":
            continue
        if name == "精确计算接口":
            body = r"""所有表项按P2–P7的有限求和计算，完整参数和逐位置
$A_k,B_k,C_k,C'_k,\min$已列于[第七章](#arithmetic)。
本章的权重表直接证明应用所需下界，不依赖优化程序的正确性。"""
        body = re.sub(r"(?m)^### ", "#### ", body)
        small_parts.append(subsection(name, relocate(body, "proofs")))
    small_parts.append(subsection("19–23点全部上界", table_only(overview["3. 19至23点：度数与 link 修正"])))
    pieces.append(chapter("small-structure", "三、19–23点的结构选择与修正", "\n".join(small_parts)))

    large_parts = []
    name_map = {"Claim：所证明的准确命题": "结构命题", "Assumptions": "假设",
                "Notation": "记号", "Proof Strategy": "证明路线", "Dependency Map": "推理依赖"}
    for name, body in large.items():
        if name in {"Status", "独立枚举及完备性", "Corrections or Missing Assumptions", "Open Risks"}:
            continue
        body = re.sub(r"\\tag\{([1-8])\}", lambda m: r"\tag{L" + m[1] + "}", body)
        body = re.sub(r"式 \(([1-8])\)", lambda m: "式 (L" + m[1] + ")", body)
        body = body.replace("式 (L5)–(6)", "式 (L5)–(L6)")
        body = body.replace(
            "7. 概率应用还须证明一个仅依赖 $v,t,(l_T)$ 的有效上界，并验证代表处的值。本文不把该项当作既有前提。",
            "7. 第二章证明仅依赖$v,t,(l_T)$的有效上界；本章末列出所需代表的严格值。")
        body = body.replace(
            "因此，如果另有已证明的概率上界 $U(v,t,(l_T))$，且对表中每个所需代表存在位置向量 $t$ 使 $U<1$，则该代表对应的任意实际超图都可以选择相应标签及位置。",
            "第二章已证明概率上界$U(v,t,(l_T))$。本章末对每个所需代表给出位置向量$t$及严格界$U<1$；因此，该代表对应的任意实际超图都可以选择相应标签及位置。")
        large_parts.append(body if name == "Proof" else subsection(name_map.get(name, name), body))
    large_parts.append(subsection("9. 全部代表的精确概率界", r"""
以下取表中标签顺序。空类型、单点类型及多点类型由式(L5)、(L6)唯一恢复，
其余未覆盖点对各自补成二元块，其他类型计数为零。代入P2–P7所得：

""" + table_only(overview["4. 24与25点：有限局部型"]) + r"""

24点三型的界均小于1。25点的K6-4给出的界大于1，而第7节证明总能选择非K6-4的六点集；
其余八型均给出严格小于1的界。具体类型向量、每个位置的三个上界和最小值均在第七章内联。
"""))
    pieces.append(chapter("large-structure", "四、24–25点的解析分类与选点", "\n".join(large_parts)))
    pieces.append(chapter("closure", "五、回到任意有限超图", r"""
第一章证明：若存在至多32边的不可二染色五元超图，就存在19–25点、
恰32边、任意点对共边的反例。

第三章的选点预算覆盖19–23点全部情形；第四章的解析分类与七点引理覆盖24、25点。
在每个实际超图上，先选定锁点、同构标签与位置，再抽取剩余随机排列，
符合M1及LOCK的量词。各分支给出的实际类型计数与加权扣除，均满足P2–P9的假设。

因此每个有限目标中的超图都满足

$$\Pr(\mathrm{Fail})\le \sum_{k=1}^v\min\{A_k,B_k,C'_k\}<1.$$

条件排列空间非空且有限，必存在成功的排列。P1证明贪心输出没有全红边，
成功又排除了全蓝边，故得到原定义要求的二染色。这与反例不可染矛盾。

所以对任意有限简单五元超图，$|E|\le32$都蕴含Property B，
等价地$m(5)\ge33$。$\square$

分类的完备性来自第四章的解析证明，严格数值界来自明确的有理数有限和。
全称结论不依赖整图搜索或有限样例外推。
"""))
    pieces.append(chapter("lean", "六、Lean形式证明与可复现核验", lean_section()))
    pieces.append(chapter("arithmetic", "七、逐位置精确算术明细", arithmetic_appendix()))
    auxiliary = relocate(large["独立枚举及完备性"], "proofs").replace(
        "上表的固定标签代表", "第四章表中的固定标签代表")
    auxiliary += "\n\n" + relocate(prob["Independent Finite Checks"], "proofs")
    pieces.append(chapter("sources", "八、来源与辅助复算", overview["来源与范围"] + r"""

<details class="auxiliary-checks">
<summary>辅助程序及独立有限检查（不承担一般证明义务）</summary>

局部分类已在第四章解析证明。以下保留辅助程序的完备性说明和实际核对范围，
便于重复计算；它们没有替代数学论证。

""" + auxiliary + r"""

</details>

<details class="source-info">
<summary>规范源与阅读版的组织</summary>

数学规格来自`FORMAL_SPEC.md`；概率引理、两个结构章节分别来自
`proofs/PROBABILITY_LEMMAS.md`、`proofs/STRUCTURE_19_23.md`、
`proofs/STRUCTURE_24_25.md`。公式、适用条件和证明步骤保留；
历史阶段的候选/待审阅文字不进入正文。第四章的局部公式统一加前缀L，
避免编号冲突。`PROOF_PACKAGE_FULL.md`是由这些规范源生成的单卷阅读稿。

算术明细来自已核验的`results/reproduced_bounds.json`。
Lean声明、装配和公理输出直接取自项目源码及run09日志；
浏览本页无需跳到外部引理文件。

</details>
"""))
    OUTPUT.write_text("\n\n".join(pieces).strip() + "\n")
    return OUTPUT


if __name__ == "__main__":
    print(compose())

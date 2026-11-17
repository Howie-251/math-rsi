# E14 全局孔差归约独立复核

冻结稿 SHA-256 为 `b8857167107c129e5bcddb14b15c244ec7480486e1b7d9f74052c5f92821133c`，输入清单为 `8a222e5047baa43962784f870d448b06264b6fe7f96c3f8a646be607203d43a4`。采用用户指定的 fresh GPT-6.1-sol / high 独立审稿角色，实际等级为 **PASS / same-family / provisional / sound-modulo-imports**。对同一冻结稿无未决问题。此审查未作跨模型或 Lean 核验。

## 全文覆盖与义务

- **S00，第 1–39 行，命题、量词、约定和依赖。** 每条原短边恰消耗两色各一点，57 边与补图短完美匹配互换。分类针对孔集，强制边针对其任意原匹配。所有可能用到的导入仅 E12，依赖无环。
- **S01，第 40–58 行，定向和奇偶。** 逐位翻转用原组名计算差，故 D 是所示逐列和。若 t 为奇，两组距各自中心均为偶数，每组至多一项为 0，其余至少 2，推出 D≥24>21。t 为偶时 L=B、V=补 A 都是奇组。
- **S02，第 59–72 行，上界和模板。** 全单位组的中心因独立性为非孔且在剩余图孤立，排除零超额。D=14+2(e(L)+e(V)) 给总超额 2 或 3。μ≥5 给 D≤14，矛盾。全补交换两组。超额二的五元支撑漏掉六个单位方向之一，物理异色孔因此短邻接。
- **S03，第 73–78 行，筛选充要性和强制边。** 物理异色距离是 7−组间距离；单位参与时距离至多 4，三元间相距 6 恰为不交。δ=7−c，模板总负载至少 18，所以 c≤3 时有列 c=3，从而 μ=4。两中心均存活，邻点可用数分别为 1 和 1 或 2；完美匹配须恰选一条。
- **S04，第 79–95 行，全部自同构、计数与证书。** 固定原点及所有邻点的自同构逐位保真。规范形间保色只允许零平移，换色只允许全补。缺位与唯一三元支撑决定标准 L 及稳定子。双三元有序类再模换组，三三元按超额已定向。直接孔差和物理邻接筛选及生成元 BFS 独立重建计数。19 份边证书精确覆盖两色补集各 57 点，长度 57 排除重复端点。
- **S05，第 96–101 行，E12 回代和穷尽。** 一条孔短边与 M 点不交，加入后是 58 边短匹配。冻结 E12 §5 与 PASS 回执覆盖任意此类输入，并保留增广匹配。若孔独立，由前四节分为 μ≤3 或 μ=4 的十九轨道。
- **S06，第 102–104 行，未决范围。** 低差尚未全称闭合。高差枚举仅回答几何与每轨道可实现性。相邻孔结论是旧 E12 的推论。新增全称 Hamilton 关闭域为 0，完整 E14 与 R7 仍开放。

第 1–4 节的主结构结果与有限证书不依赖 Hamilton 导入。第 5 节使用 E12 的任意 58 边短匹配全称接口。已逐项重哈希 E12 证明和回执并读取 §5 及回执的证明绑定、接受范围与排除项。沿用该冻结 PASS 回执的条件化结论，未重做 E12 的内部证明。TWO_TARGET 37、67 均未调用。有限图论证没有极限交换、渐近常数或概率模式义务。

## 边界及独立有限复验

尝试打破归约时检查了定向翻转奇重、中心本身为孔、超额零和超额二的五元替代、跨组三元不交、两标准第一组在换组后的合并、重复代表、漏代表及重复匹配端点。奇翻转的最小贡献仍超预算；中心为孔与独立性矛盾；五元替代和三元不交均产生短邻接；匹配覆盖的两色基数与边数同时排除漏点和重复端点。

以下脚本仅读取冻结目录 JSON。候选来自直接的两色孔位计数与物理短邻接。轨道由相邻坐标换位生成元的可达性遍历构造，双三元型再加换组；与作者的置换预像和稳定子取最小方法独立。脚本逐代表核验各切片不交、无漏及每个 57 边证书，并检查中心边。运行环境为 Python 3.14.0，退出码 0。两种固定第一组的三元组依次记录原始、孔差通过和独立候选数。

```text
I [(245, 90, 62), (245, 46, 18)] 8 5 [21, 24, 8, 21, 6] [2520, 2520, 840, 2520, 630]
II [(147, 17, 0), (147, 3, 0)] 0 0 [] []
III [(12495, 410, 216), (12495, 177, 36)] 14 14 [24, 24, 48, 24, 12, 12, 6, 12, 12, 24, 6, 12, 18, 18] [2520, 2520, 5040, 2520, 1260, 1260, 630, 1260, 1260, 2520, 630, 1260, 2520, 2520]
```

```python
import json
from itertools import combinations
from pathlib import Path

U = frozenset(1 << i for i in range(7))
N = frozenset(range(128))
EVEN = frozenset(x for x in N if x.bit_count() % 2 == 0)
ODD = N - EVEN
L0, L1 = (U - {1} | {7}), (U - {1} | {14})
data = json.loads(Path("R7_E14_HIGH_GAP_INVENTORY.json").read_text())
swap = [tuple(x ^ (3 << i) if (x >> i) & 3 in (1, 2) else x for x in range(128))
        for i in range(6)]

def orbit(seed, exchange):
    seen = {seed}
    queue = [seed]
    for l, v in queue:
        nxt = [(frozenset(p[x] for x in l), frozenset(p[x] for x in v)) for p in swap]
        if exchange:
            nxt.append((v, l))
        for state in nxt:
            if state not in seen:
                seen.add(state)
                queue.append(state)
    return seen

def witness(r, l, v):
    ho = l
    he = {x ^ 127 for x in v}
    gap = [sum(bool(x & u) for x in he) - sum(bool(x & u) for x in ho)
           for u in sorted(U)]
    assert min(gap) == 4 and gap == r["coordinate_hole_gap"]
    assert sorted(gap) == r["hole_gap_spectrum"]
    assert [7 - g for g in gap] == r["column_load"]
    e = r["short_matching"]
    assert len(e) == r["matching_size"] == 57
    assert {a for a, b in e} == EVEN - he
    assert {b for a, b in e} == ODD - ho
    assert all(a ^ b in U for a, b in e)
    assert (0, next(iter(U - l))) in map(tuple, e)
    assert next(a for a, b in e if b == 127) in {127 ^ u for u in U - v}

for name, sizes in {"I": (1, 3, 1), "II": (1, 5, 1), "III": (2, 3, 2)}.items():
    d, weight, count = sizes
    possible_v = [U - set(missing) | set(heavy) for missing in combinations(U, d)
                  for heavy in combinations([x for x in ODD if x.bit_count() == weight], count)]
    assert len(set(possible_v)) == len(possible_v)
    domain = set()
    stage_counts = []
    for l in (L0, L1):
        c = 0
        for v in possible_v:
            even_holes = {x ^ 127 for x in v}
            delta = [sum(bool(x & u) for x in even_holes) - sum(bool(x & u) for x in l)
                     for u in U]
            if min(delta) < 4:
                continue
            c += 1
            if all(a ^ b not in U for a in l for b in even_holes):
                domain.add((l, v))
        stage_counts.append((len(possible_v), c, sum(a == l for a, b in domain)))
    ordered = set()
    dir_count = 0
    for pair in domain:
        if pair not in ordered:
            dir_count += 1
            ordered.update(orbit(pair, False) & domain)
    assert ordered == domain
    assert dir_count == data[name]["orbits_before_group_exchange"]
    universe = set()
    slice_sizes = []
    full_sizes = []
    for r in data[name]["orbits"]:
        l, v = (frozenset(r[k]) for k in ("L", "V"))
        assert (l, v) in domain
        full = orbit((l, v), name == "I")
        sliced = {p for p in full if p[0] in (L0, L1)}
        assert sliced <= domain and not universe & sliced
        universe.update(sliced)
        assert len(sliced) == r["fixed_first_group_slice_size"]
        slice_sizes.append(len(sliced))
        full_sizes.append(len(full))
        witness(r, l, v)
    assert universe == domain
    print(name, stage_counts, dir_count, len(slice_sizes), slice_sizes, full_sizes)
```

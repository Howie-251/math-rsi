# 节点推进协议验证（2026-11-10）

本增量限于 ECC 插件的 Markdown 执行协议、技能入口与示例；没有修改 base、调度服务或现有数学证据。基于 main d29c5ad4。验证由维护者本地执行，不称为独立模型审阅或原数学研究验收。

- 6份新增/修改入口与说明中的33个本地链接均存在，diff whitespace检查通过。
- 研究入口实际指向归属检查、工作包和结构示例；证书入口核局部域与父结论连接；README提供恢复入口。
- 手工路径检查：换基/换算法→同节点；未知等价→归属核对；新对象→父域补集；共用距离表→一个任务多个消费者；中断→同任务真实断点；缺覆盖→父节点仍未解；存在性候选→原题验收。
- 初等代数的缩小实例读回：n=6，S=span(3,12)，整数位序 bit j 为坐标 j。枚举不在S内的60个向量v，偶正交4个（A）、偶非正交24个（B）、奇32个（C）。对每个扩张基实际计算Gram矩阵，A秩0、B秩2；所有C的偶子码恰为S。这里统计向量，未除以每个陪集的4个代表，不混称60个不同扩张码。
- 本地运行未启动模型、距离大扫描或原研究Goal。72/36示例只给代数分类，不导入本机局部数值闭合。

可在仓库根重放上述小实例：

```sh
python3 - <<'PY'
def rank(rows):
    basis = {}
    for x in rows:
        while x:
            k = x.bit_length()-1
            if k in basis:
                x ^= basis[k]
            else:
                basis[k] = x
                break
    return len(basis)
S = [3, 12]
span = {0, 3, 12, 15}
counts = dict(A=0, B=0, C=0)
for v in range(64):
    if v in span:
        continue
    rows = S + [v]
    gram = [sum(((a & b).bit_count() % 2) << j
                for j, b in enumerate(rows)) for a in rows]
    kind = ('C' if v.bit_count() % 2 else
            'A' if all((v & s).bit_count() % 2 == 0 for s in S) else 'B')
    if kind in ('A', 'B'):
        assert rank(gram) == {'A': 0, 'B': 2}[kind]
    else:
        words = span | {x ^ v for x in span}
        assert {x for x in words if x.bit_count() % 2 == 0} == span
    counts[kind] += 1
assert counts == dict(A=4, B=24, C=32)
print(counts)
PY
```

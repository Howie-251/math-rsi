# 当前交付：57例，N(12,5)≥42396

主family现为degree12的42343..42396全部54个完整前缀，加degree11的37629..37631共3例，总57例、两组参数。旧53例literal步骤逐项保持，新增4步来自8pin Q-line＋4anchors构造，每步actualcurrent degree与完整R4通过；没有新全源BFS或外审。degree12最新全源阶数仍42377，之后由完整逐步覆盖归纳保证。完整Lean实例仍0，不主张最优值或57种独立方法。

生成最新图：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42396 --output /tmp/graph_d12_D5_n42396.edges`。root生产边表在`../h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges`；一次生成器edge-set对照记录在同目录`generator_dry_run.json`。

下方保留历史交付快照，当前例子数、范围与最强值以本段和families.json为准。

---

# 当前主family：53例，N(12,5)≥42392

本轮从数学已接受42391起新增1个完整前缀；degree12现覆盖42343..42392共50例，degree11仍37629..37631共3例。原52例literal步骤保持原样。每个新点只做必要的实际degree和完整currentR4生产检查，没有新全源BFS或外审；最新全源仍42377，后续由逐步完整覆盖归纳保证。完整Lean实例仍0，非最优值声明。

生成最新例子：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42392 --output /tmp/graph_d12_D5_n42392.edges`。完整边表在`../h9_d12_changed_base_round2/graphs/graph_d12_D5_n42392.edges`，一次生成器edge-set对照记录在该目录generator_dry_run.json。

此次只重试上次评估base早于42391且当前degree合法的冻结列表；same-base失败跳过，不回头旧失败。允许真实degree承载的多重line顶点并逐项标识，未混入独立8pin分支。下方保留先前交付记录；当前例子数与最强值以本段为准。

---

# 当前主family更新：52例、两组参数

旧38例的literal步骤保持不变；degree12现可生成42343至42391的全部49个整数前缀，degree11仍为37629至37631共3例。最强数学下界为N(12,5)≥42391、N(11,5)≥37631。

本轮从已独立验收42377起接受14个完整新点，每步只做必要的实际degree与完整currentR4生产检查；没有再跑全源BFS或外审。42377仍是degree12最新全源BFS阶数，后续前缀由完整逐步覆盖归纳保证。完整Lean图实例仍为0。独立8-pin分支未混入本family。

最新例子：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42391 --output /tmp/graph_d12_D5_n42391.edges`。

新增字面参数已接入families.json，最强完整边表在`../h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges`。一次生成器edge-set dry-run结果在`../h9_d12_global_remainder/generator_dry_run.json`。下面保留旧38例交付快照，表中“最强”以本段为准。

---

# 全部38个显式图：两组参数的确定性生成包

本包可从原作者图生成 **38个不同阶数的完整例子**：

| 最大度 | 直径 | 可生成阶数 | 例子数 | 当前最强下界 |
|---:|---:|---|---:|---|
| 11 | 5 | 37629至37631，每个整数阶 | 3 | N(11,5)≥37631 |
| 12 | 5 | 42343至42377，每个整数阶 | 35 | N(12,5)≥42377 |
| 合计 | | 两组参数 | 38 | 两格下界得到改进 |

这些是同一Q-line＋anchors扩张机制的两个参数族、38个显式图，**不是38种独立构造方法，也不是N(11,5)或N(12,5)的最优值声明**。数学例子及最强图的独立验收已完成；完整Lean图实例仍为0，不能把生成器或已有Lean接口算作完成形式化。公开参考表在root于2026-10-27实时核对时仍分别为37628、42342，最强图相对该快照提升3、35点。

## 一条命令生成任意例子

在项目root运行，指定一个新输出路径。除Python标准库外无依赖，不搜索、不求解、不运行BFS：

```bash
python research/ddp/more_graphs_20261027/delivery/family_generator.py \
  --degree 11 --order 37631 --output /tmp/graph_d11_D5_n37631.edges

python research/ddp/more_graphs_20261027/delivery/family_generator.py \
  --degree 12 --order 42377 --output /tmp/graph_d12_D5_n42377.edges
```

把`--order`改成表中任意整数，即生成对应完整前缀。脚本逐步检查source_n/source_m、newlabel、邻集唯一性、邻点旧度、增边数和最大度，输出实际n/m/min_degree/max_degree。输出格式第一行为`n m`，后面每行一条`u v`无向边（u<v）。所有原图边完整保留。

`families.json`保存全部35＋3次增点的literal参数；`pins`就是新点的**完整邻集**，另列mandatory_pins与anchors。生成时只需这个JSON、生成器及两份原作者raw adjacency，不依赖历史搜索缓存、几何重建或外部网络。跨目录/独立导出时，可用`--source /path/to/deg11_diam5_n37628.txt`或对应degree12原图覆盖默认路径。

如需一次写出全部38个边表，可在保存两份原图后执行下述Python片段，输出目录可自行修改：

```python
from pathlib import Path
import subprocess
generator = 'research/ddp/more_graphs_20261027/delivery/family_generator.py'
out = Path('/tmp/h9_all38')
out.mkdir(exist_ok=True)
for degree, first, last in [(11, 37629, 37631), (12, 42343, 42377)]:
    for n in range(first, last + 1):
        subprocess.run(['python', generator, '--degree', str(degree),
                        '--order', str(n), '--output',
                        str(out / f'graph_d{degree}_D5_n{n}.edges')], check=True)
```

## 原图、署名和来源

两份基图均由 **Dharunish Yugeswardeenoo** 发布于[Zenodo23653049](https://zenodo.org/records/23653049)，*Large graphs of given maximum degree and diameter (Degree-Diameter Problem):34 constructions*（metadata日期2026-10-26）。完整原图贡献属于该作者；其H9 partial-fold与duality基础采用 **Rishabh Rajiv** 的[22907863](https://zenodo.org/records/22907863)、[23056128](https://zenodo.org/records/23056128)。当前工作给出这里列出的explicit增点、几何见证恢复、完整有限覆盖证书和独立验收，不主张上述底层几何定理原创。

- 原degree11图：[deg11_diam5_n37628.txt](https://zenodo.org/api/records/23653049/files/deg11_diam5_n37628.txt/content)，项目保存于`research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt`，n37628、m205296。
- 原degree12图：[deg12_diam5_n42342.txt](https://zenodo.org/api/records/23653049/files/deg12_diam5_n42342.txt/content)，同目录对应文件，n42342、m245217。
- [F. Comellas主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)及[D5原始来源描述](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html)提供公开基线与作者引用。

raw adjacency每行是`vertex neighbor1 neighbor2 ...`，labels从0连续编号。`families.json`保留精确sourceURLs、项目路径、作者credit，以及每步来自哪份有限批记录；其中degree11后续两步读自`accepted_sequence.json`的 **accepted** 键，未误用records。

## 为什么每个前缀都是完整D5图

设旧图B的D≤5，保留其全部边，添新点z，完整邻集为S。如果`R4_B(S)=V(B)`，旧—旧距离继承，新—旧距离至多1+4=5，故新图D≤5。每条已接受增点均对**实际当时的base**检验了全部旧顶点，包括此前新加入点；其证据在参数所列原始文件中。失败项未当作可加入，后来的边也没有被借来证明更早一步。

因此原作者D5基图＋逐步完整R4证书，保证全部38个前缀。最大度由逐步邻点旧度和新点cardinality检查保证。所有阶数又大于相应D4 Moore上界（Δ11为12222、Δ12为17569），所以直径实际必须恰为5。并未声称38个前缀都分别重跑全源BFS。

## 最强图独立验收与结构复现

| 最强图 | 边数 | 全部BFS根 | 最大度 | 实际直径 | >5无序对 | 不可达对 |
|---:|---:|---:|---:|---:|---:|---:|
| 37631 | 205329 | 37631 | 11 | 5 | 0 | 0 |
| 42377 | 245637 | 42377 | 12 | 5 | 0 | 0 |

两者均simple、connected。root的原始JSON分别为`../h9_d11_followups/independent_all_source_BFS_37631.json`、`../h9_d12_global_extensions/graphs/independent_all_source_BFS_42377.json`；实测4workers，分别10.2909/15.1431wall秒、41.0824/60.4583CPU秒。更早37629、42343、42345亦有独立全源验收；其它前缀用逐步完整归纳证书，不混计验收次数。root另统一提供验收CSV/JSON与专家导出包，本生成器不重新运行这些检查。

本次交付只对上述两张最强图各执行一次dry-run edge-set比较，生成内存图而不写旧文件、不BFS；结果见`dry_run_d11_37631.json`、`dry_run_d12_42377.json`。手动复现结构对照：

```bash
python research/ddp/more_graphs_20261027/delivery/family_generator.py \
  --degree 11 --order 37631 --dry-run \
  --compare research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges

python research/ddp/more_graphs_20261027/delivery/family_generator.py \
  --degree 12 --order 42377 --dry-run \
  --compare research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges
```

如需独立重验新生成的文件，可复用`../../global_coverage_20261027/candidate42343/verify_all.cpp`编译后运行`verify_all EDGES DEGREE 5 THREADS`；它读取完整边表并对每个根BFS。本次打包没有再次运行该程序，也没有创建哈希或校验清单。

from pathlib import Path
import json,sys
out=Path(__file__).resolve().parent
project=out.parents[3]
repo=next(x.split('\t')[1] for x in (project/'.aris/installed-skills-codex.txt').read_text().splitlines() if x.startswith('repo_root\t'))
sys.path.insert(0,str(Path(repo)/'tools'))
from capture_filter import screen
t=json.loads((out/'terminal.json').read_text())
r=json.loads((out/'run.json').read_text())
c=json.loads((out/'first.independent_calibration.json').read_text())
assert t['starts_completed']==8 and t['pending']==[] and not r['running'] and c['matches']
report='''# 122 点六正则一般图：有限模拟退火初筛

本批是用户要求扩大方法探索后的一个独立入口：使用全部顶点上的普通两边交换，允许破坏所有群作用及轨道对称性。目标为 122 点、最大度六、直径三，超过项目保存的 120 点下界。点数不是构造成功的保证。

**8 个新起点的指定有限试验完整结束，没有得到直径三。** 搜索器保存的最好完整图有 122 点、366 边、各点度六，精确全根半径三评分为 403 个距离大于三或不可达的无序点对。唯一最好图的独立最终全源距离检查交由主代理，避免重复验收；本报告没有据搜索器声称实际直径四。

## 实际范围与成本

- 8 个独立种子：20261027180 至 20261027187。
- 每个起点从简单六正则循环图的正负一步、二步、三步边开始，再接受 10000 次随机合法两边交换进行混合；不声称这是所有六正则图上的均匀抽样，也没有读取旧失败源图。
- 每起点固定 250000 个交换提案，共 2000000 个。每次选两条不共端点的边，换成其端点之间另一种配边；新增边必须原先不存在，因此始终保持简单和六正则。
- 1804174 个提案合法并评分，另加 8 个正式起点，合计 1804182 次精确全 122 根半径三评分。它们是评分次数，不是非同构图数。
- Metropolis 接受 115596 次移动。每起点五个 50000 提案冷却段，温度从 8 降至 0.1；允许变差移动以离开严格局部最小。
- 最好 403 坏点对首次在第 5 个起点、第 99959 步保存，见 best.json 和 best.edges。
- 含编译和首次校准实测总 CPU 4.666272 秒，生产 CPU 3.813 秒，墙钟 4.674636 秒；单 worker，总预算 90 CPU 秒。固定试验提前完成，不补满预算、不追加种子、不扩大邻域。

## 精确评分与首次校准

对每个根 v，先算半径二集合 B2(v)，再取 B2(v) 与所有邻居 u 的 B2(u) 的并，即得到半径三集合。对全部 122 根计算缺失数，求和后除以二得到无序坏点对数。评分不假定任何轨道对称性，断连目标同样计为缺失。

第一个正式起点的 122 个逐根缺失数已与独立 Python 普通全源 BFS 逐项一致，坏点对均为 1457。该起点评分直接复用于本批，没有独立额外试图调参；检查记录为 first.independent_calibration.json。这一次首图校准不代替最终最好图验收。

## 结论与下一决策

这次试验展示了可以极低成本测试完全释放轨道对称性的入口，但本批最好的 403 坏点对仍未达到目标。它只关闭所列 8 起点、固定移动数的试验，不排除一般 122 点图，也不排除更有效的一般图搜索算法。按用户最新探索优先要求，本入口在本次初筛后停止，不继续追逐同源小邻域，资源让给其他构造方法。

复现程序为 run.py 与 search.cpp；metadata.json 保存全部参数，starts.jsonl 保存逐起点结果，terminal.json 为完整终态。所有已启动进程已正常退出，无自动重启或待续作业。独立最终检查由主代理追加记录。
'''
assert not screen(report),screen(report)
(out/'REPORT.md').write_text(report)
print('REPORT written; no further search or final BFS run.')

from pathlib import Path
import json,sys
out=Path(__file__).resolve().parent
project=out.parents[3]
repo=next(x.split('\t')[1] for x in (project/'.aris/installed-skills-codex.txt').read_text().splitlines() if x.startswith('repo_root\t'))
sys.path.insert(0,str(Path(repo)/'tools'))
from capture_filter import screen
t=json.loads((out/'terminal.json').read_text());r=json.loads((out/'run.json').read_text())
assert t['samples_scored']==30000 and t['connected_samples']==29729 and t['disconnected_samples']==271
assert t['pending']==[] and not r['running'] and json.loads((out/'first.independent_calibration.json').read_text())['matches']
report='''# 108 点 Möbius 置换 Schreier 图：有限矩阵对采样

**固定 30000 个矩阵对的采样完整结束，无直径至多四的图。** 其中 29729 个图连通、271 个图断连；全部正式样本均以全部 108 根精确半径四集合评分，未因断连或非正则而从计数中删除。

## 构造与参数

顶点为射影直线 P1(F107)，即有限域元素 0 至 106 加上无穷点，后者标号 107，总计 108 点。对两个行列式非零的矩阵 A、B，分别取分式线性置换

    x -> (a*x+b)/(c*x+d).

有限点分母为零时映到无穷；无穷在 c 非零时映到 a/c，在 c 为零时仍为无穷。无向边为全部 x--A(x) 与 x--B(x)，删除自环、合并重边。无向化已经包含 A、B 及其逆置换对应的邻接，每个顶点最多四个邻居。非正则样本合法保留。

这是基于两个具体置换的 Schreier 生成图，不是射影直线全群作用保持的轨道边图。没有把 PGL 的整个作用误当成所生成图的自同构；评分始终使用全部 108 根。

目标是最大度四、直径四，在点数上超过保存的 104 点下界；该算术只说明若成功可改善门槛，不保证存在。

## 实际有限范围

- 固定随机种子 20261027190，逐项采样两个可逆二乘二矩阵；每个矩阵除以首个非零项，保存射影归一化代表。
- 30000 个正式矩阵对，不追加样本、素数或围绕某一矩阵对的局部搜索。样本之间可能给出同图或重标号图，没有声称非同构图数。
- 共使用 60000 个可逆矩阵；原始矩阵抽取共 60599 次，其中 599 次行列式为零。这些原始抽取不定义正式图，单独记录；全部 30000 个正式图均已评分。
- 连通 29729 个，断连 271 个；samples.jsonl 每行保留正式样本索引、两个矩阵、根零连通分量大小、坏点对数和零至四度的顶点计数。
- 17 次严格最好改善，每次完整边表和参数保留在 improvements/；最终最好同样保存为 best.edges 和 best.json。
- 含编译及首图校准实测总 CPU 1.214109 秒，生产 CPU 0.288247 秒，墙钟 1.246650 秒；单 worker，总预算 60 CPU 秒。所有程序正常退出，无重启或待续作业。

## 最好候选与精确校准

最好正式样本索引 20934，两个矩阵按 a,b,c,d 顺序为

    A = [1,79,41,84]
    B = [1,28,78,95].

搜索器展开图为 108 点、216 边、四正则且连通，精确评分为 784 个距离大于四的无序点对。它没有达到直径四；本子任务没有做最好图的最终独立全源 BFS，该唯一最终验收由主代理负责。

评分使用 B4(v)=并集{B2(u):u属于B2(v)}，其中 B2 是包含根自身的半径二集合。每个根的缺失数求和除以二得到坏无序点对；不可达点同样计为缺失。

第一个正式样本由独立 Python 程序直接按分式线性公式重建全部边，有限域除法使用 pow(den,105,107)，与生产程序的逆元表无共享。两置换各自均检查为 108 点排列，完整边表一致；普通 Python 全 108 根 BFS 的逐根半径四缺失数与 C++ 位集结果逐项一致，坏点对均为 1366。这个正式评分被复用，没有额外重复首图搜索。

## 范围与后续

结果只结束指定种子和 30000 个正式矩阵对的采样，不排除全部 PGL(2,107) 置换对或一般 108 点图。按用户“及时跳出同一构造”的要求，这个入口在初筛后停止，不围绕 784 坏对的候选继续扩大搜索。

run.py 和 search.cpp 可复现本批，metadata.json 保存参数，terminal.json 保存完整终态，first.independent_calibration.json 保存唯一首图校准。主代理负责追加最终最好图的独立检查结果。
'''
assert not screen(report),screen(report)
(out/'REPORT.md').write_text(report)
print('REPORT written; no further sampling or best-graph BFS run.')

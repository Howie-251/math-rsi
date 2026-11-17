# Q7 E16 研究 Wiki

本知识库按 MathRSI v3 的 `research-wiki/` 结构保存了 E16 已验收结论及可复用经验。证明条目沿用原审计的 `sound-modulo-imports`、`same-family`、`provisional`，证书验真记录单独保存。

## 已验收结论

- [完整 E16](claims/q7-e16.md) 给出至少 56 边七维短匹配的全称结论和分支合并。
- [μ=0](claims/q7-e16-mu0.md)、[μ=1](claims/q7-e16-mu1.md) 和 [μ=3](claims/q7-e16-mu3.md) 连接冻结证明、审计和主线接受记录。μ=2、4 和 E14 的旧档定位见[汇总 HTML](../START_HERE.html#baseline-title)。

## 可复用构造与工作方法

- [六维参数化双桥](claims/q6-double-bridge.md) 记录适用的内切孔型、规定边及新增边条件。[完整六维 A8](claims/q6-a8.md) 记录指定多数孔的避一圈及调用边界。
- [难余域优先的分类流程](ideas/hard-remainder-first.md) 与[旧易证子族循环](ideas/easy-subfamily-loop.md) 说明按整域验收时如何选分类、判重与停损。
- [结构剥离后的完备有限核](ideas/complete-finite-kernel.md) 与 [μ=0 RUP 验真](experiments/e16-mu0-rup.md) 说明如何将原反例送入有限核，以及验证结果进入证明的位置。

## MathRSI 读取与维护

先用[实体索引](index.md)或[查询摘要](query_pack.md)查找条目，再读有关实体页及其引用的冻结证明。可用[关系图](graph/edges.jsonl)核对实际依赖。Wiki 写入日志见 [log.md](log.md)，证明工作的原时间线见 [E16 研究轨迹](../trajectories/SESSION_INDEX_E16.md)。页面 front matter 中的 `provenance` 路径相对该页。

维护时在本地 MathRSI v3 的 `base/tools` 下使用原 `research_wiki.py`。在本包根目录，以该工具的文件路径替换示例中的 `<research_wiki.py 路径>`。

```powershell
python '<research_wiki.py 路径>' stats research-wiki
python '<research_wiki.py 路径>' rebuild_index research-wiki
python '<research_wiki.py 路径>' rebuild_query_pack research-wiki
```

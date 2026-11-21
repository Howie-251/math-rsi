<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# 真实D123联合排除：完整重建与两次实际DRAT

原输入及固定σ区间证明在[JOINT154_PROOF.md](JOINT154_PROOF.md)。本文原证使用
A57/B44/C22共享154态、全部32655条D必要行、九份真实D0避面57、563条U行、
U九度齐22、真实首尾各284模板和其shadow、共同亏损式及13纤维。完整公式
45012变量、124264句，CNF SHA256：

`e333f34f8fa13d8c0339d681e75f1f4ec3aebda3d5eaa86c82765d5d98d04970`

原109730009字节DRAT SHA256：

`254b6448037e7834b5f993a3e7945339f1df7cb5e34b594bc3911b74b25b8c4b`

第一AE20，求解124.606秒；实际第一DRAT0且唯一VERIFIED。另写编译器从规范
四集/三集物理目录和全部2^20六点色表重建完整公式，得到同一字节hash；第二
实际DRAT也退出0、唯一VERIFIED，94.707秒，检查前后两个hash不变。两次使用
相同drat-trim实现的不同进程，不称第二种checker或外部审稿。

进一步另写source regenerator重算1553条D原生支撑、295个短帽映射、529条U
原生支撑、24个短帽映射，并重新按45份有序双删除提升641纯核及全部15个Hall
费用，最终D32655行/U563行逐支撑逐需求完全一致。641纯核为冻结数学进口，
其来源纯局部schema只含差格/增长/packet/同端路径/负占用单位；不含真实P首二
单位、外部洞或counter。故可用于任意admissible chart；Hall纸证同样只用上述
性质。历史实际源核回放定位在主中文入口，未伪称本次又重跑所有旧核DRAT。

所有858的(3,5)切片使用已证857≤50；旧U导出JSON中记录51，由编译器明确
升级成50。源再生器也明确区分该版本，未把索引或初次检查失败藏为PASS。

迁移复现（Linux，需python-sat及drat-trim）：

```bash
python3 reproduce_joint154.py --output /absolute/new-empty-directory --checker /path/to/drat-trim
```

该命令检查两原件hash，在新目录重建CNF，再实际回放原proof；不重新求解。
完整CNF/DRAT在小包内的`joint154-saturated01/`，冻结行输入在`inputs/`。
可复现范围是本联合有限证书及其源支撑重建；旧641纯核的历史proof依赖单列。
研究参数、最大避免人口与几何强迫阈值分别见稳定中文入口，不作sharp性主张。

# 知识来源、完整wiki与原件地图

所有source链接均在本克隆。原件是历史证据而非当前Goal；当前任务先读整理层，再按承重问题打开完整证明／代码／结果。下面不是“所有文件已读”的标记。

## 原始整体与本次阅读范围

[原交接README](../archive/source/README.md)和[guide](../archive/source/guide/)解释原题、轨迹、成果与cost；[原research-wiki](../archive/source/research-wiki/)保留完整领域知识库，[DDP_METHOD_LEDGER.md](../archive/source/research-wiki/DDP_METHOD_LEDGER.md)为长账本。wiki／guide定位之后须读当前判断依赖的primary，不以node数等同方法数。

[本次源库存](../archive/intake/SOURCE_INVENTORY.json)覆盖原包；[逐文件ledger](../archive/intake/late/READ_LEDGER.tsv)与[family地图](../archive/intake/late/READING_MAP_BY_FAMILY.tsv)记录本作者实际阅读子集。late ledger有10376行，733全文／7部分／4994结构解析／1135精确重复／3507未读的收卷快照。它不包括其它作者全部阅读，也不代表其余source未被别人读过。完整461trajectory metadata见[轨迹表](../archive/intake/late/TRAJECTORY_MAP_ALL461.tsv)，metadata不替代primary。

[原数学提炼](../archive/intake/DD_MATHEMATICAL_EXTRACTION.md)和[扩展审计](../archive/intake/late/SOURCE_AUDIT_LATE.md)提供详尽假设／caller／缺件，文本中较早preliminary、未实施插件建议是开发历史，当前可调用实现以本插件skills为准。未读无关材料不阻塞已成熟操作，遇到影响当前判断的新冲突再定点补读。

## 成功与失败原链

| 知识／行为 | 承重原件 | 实际意义 |
| --- | --- | --- |
| 当前cover序列 | [D5原证明](../archive/source/constructors/verification/D5_ORIGINAL_PROOF.md)、[families](../archive/source/constructors/early_d5/families.json)、[checker](../archive/source/constructors/early_d5/verify_covers.py) | 每一步当前G的B4与余度，继承baseD5 |
| GenericfullN | [Lean](../archive/source/formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean)、[retained原proof](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/PROOF.md) | repeated／adjacentcenter合法，load另证 |
| 一般ports／pencil | [推导](../archive/source/research/ddp/two_successful_methods_20261101/affine_field_conditions/general_ports/DERIVATION_PACKAGE.md)、[四port反例](../archive/source/research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md) | q=2r−3是jointcertificate，F25反例保留 |
| F11真正inverse | [反例程序](../archive/source/research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_f11_port_orbits/INDEPENDENT_INVERSE_COUNTEREXAMPLE.py) | normalizedPGLinverse不等actualinverse |
| Global到edge-local | [global目录](../archive/source/research/ddp/two_successful_methods_20261101/f4_c60_global_projective/)、[edgeMODEL](../archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/MODEL_CODE.md)、[exact域](../archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/EXACT_CERTIFICATE_DOMAIN.md) | 释放共享约束，后继必要性证明加强原scope |
| q4ovoid与diagonal | [ovoidPROOF](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/PROOF.md)、[generalnote](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md) | disjointN允许中心matching；新hub不能旧collapse |
| D4共同coset | [NOTE](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/GLOBAL_COSET4_NOTE.md)、[目录](../archive/source/research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/) | 同一x的噪声cosets并，非每word满rank |
| C4条件定理及Hall | [机制proof](../archive/source/research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_PROOF.md)、[quotient放宽](../archive/source/research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PROOF.md) | 有价值conditionaltool与两实际控制器NO分别保留 |
| matching失败失效与重证 | [purecross](../archive/source/research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PROOF.md)、[general](../archive/source/research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PROOF.md) | 放宽后旧必需路线命题被反例否定，新exact门关域 |
| shared256 | [目录](../archive/source/research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/) | 全61440归一／57344连通的shared冲突，不排所有256graph |
| D2helper容量 | [Brown57](../archive/source/research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown57_cap9_capacity/PROOF.md)、[Brown91](../archive/source/research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PROOF.md) | 从总预算到excess等号奇偶，必要松弛非图 |
| D2actualinternalrepair | [exactnote](../archive/source/research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/INTERNAL_PIN_REWIRING_NOTE.md)、[code/result](../archive/source/research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/) | UNKNOWN与后继restrictedNO不混用 |
| affine27dual | [完整目录](../archive/source/research/ddp/two_successful_methods_20261101/mizuno13_clone_interface/)、[exactbound](../archive/source/research/ddp/two_successful_methods_20261101/mizuno13_clone_interface/source_dependent_geometry/controller213_capacity_gate/lp_exact_bound/PROOF.md) | 几何必要row＋exact364列组合，非一般14D5上界 |
| 公开baseline纠正 | [F7比较](../archive/source/research/ddp/two_successful_methods_20261101/f7_c60_d35/PUBLIC_COMPARISON.md)、[P33primary](../archive/source/research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md) | 合法性、公开族后果与优先权分开 |
| 原图到kernel | [F4CHECKPOINT_C](../archive/source/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/CHECKPOINT_C.md)、[源码](../archive/source/formal/DegreeDiameter/Portfolio/) | 实际carrier／trueWalk／caller／representationbridge |

## 原程序与新适配的归属

原构造器与所有历史算法原样保留，具体作者与框架归属仍见原注释／README。插件新增Python仅[replay_mizuno_dual.py](../tools/replay_mizuno_dual.py)：把原包缺失的LP_INPUT运输改为从现存MODEL透明重建，核同一个exactdual；未换数学模型、未重跑solver。可移植graphproduction直接复用原rebuild，不新建统一graph平台。

新的理论／案例／失败修法进入当前任务wiki，达到可迁移内容后按meta维护插件。原archive不成为新任务的可写状态库。程序存在、文件copy、链接全或来源review均不提升原数学验收状态。

## v4新增只读来源：PR11

[archive/pr11-2567/SOURCE.md](../archive/pr11-2567/SOURCE.md)和[MANIFEST](../archive/pr11-2567/MANIFEST.json)固定head 7bd5a0cf34db9454cb0badf79c8622fb5fb7b833，包含原构造SVG、运行版本、有限编辑源/配方/程序、BFS和Lean compact receipts及LICENSE。它独立于网站开发目录。整理调用见[饱和增点参考](saturated-insertion-and-replay.md)，原程序原样保留，未新增search或统一checker。历史完整数学结果与当前运行范围分别消费。

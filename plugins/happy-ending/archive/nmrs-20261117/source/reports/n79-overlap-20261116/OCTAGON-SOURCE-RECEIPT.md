# Schroeder 八边形原件与执行证据收据

日期：2026-11-16。范围：公开归档的字节身份、作者封存执行记录、有限检查与几何接口；不是本项目对整套 Lean 证明的独立接受。

## 1. 可直接接用的原件身份

官方入口为 [companion](https://michaelschroeder.ai/research/ErdosSzekeres/companion)，DOI 为 [10.5281/zenodo.22842891](https://doi.org/10.5281/zenodo.22842891)。网页声明的对象是实平面一般位置点集，结论 ES(7)≤81、ES(8)≤319；不是抽象 signotope 的同名结论。网页明确披露 native evaluation 信任边界，未声称外部同行评审。

官方 [SHA256SUMS](https://michaelschroeder.ai/research/ErdosSzekeres/SHA256SUMS) 给出：

```text
706786a26ec7537396c069fcedf89ab298618e0064a4be5944e96982e85a5fc2  es7_es8_bounds_81_319_v1.zip
```

本地原包 `tmp/schroeder_comparison_20261021/es7_es8_bounds_81_319_v1_full_20261116.zip` 实测 **240352401 bytes**，SHA-256 与上述值相同。ZIP 的共同前缀是 `es7_es8_bounds_81_319_v1/`，含 323 个文件。

仅用 PowerShell/.NET 读取 ZIP 字节并核对 manifest，没有在 Windows 运行作者 Python/Lean 检查器：

| manifest | SHA-256 | 条目数 | 不匹配 |
|---|---|---:|---:|
| `MANIFEST.json` | `1be95b4a7a30a6cb8cf454b153e770505a67e0adf03d75244ccaa80c5a065c05` | 322 | 0 |
| `formal/MANIFEST.json` | `81d3fb7e1d49ce780cd0ddb69506f4833c9a507c550dc5d57168ac2132e036c1` | 237 | 0 |

全部 ZIP 文件的哈希和逐项结果保存在本目录 `octagon-source-replay/local-archive-hashes.json`。顶层 manifest 不自列，其余 322 个文件均有绑定。

## 2. 可消费的作者机器回执

`audit/octagon_finite.json` 的 SHA-256 是 `b8fd04ba2ee58a27c6cb6e3ea73da1b2b2f3bd465094b9b2fa03b3411cd251c6`，内容为 **PASS**，作者报告用时 3.426 秒，`lean_or_native_evaluation_used=false`。其具体检查量：

| 数据域 | 状态 | cyclic 行 | 有向盒 | 三态六时序 | 树分支 / 叶 | 排除洞预算 | 得到占用界 |
|---|---:|---:|---:|---:|---:|---:|---:|
| balanced 5×5 | 252 | 2685 | 63504 | 1156464 | 1590 / 1591 | 58 | 193 |
| residual 4×6 限域 | 154 | 1164 | 23716 | 423024 | 7314 / 7315 | 29 | 124 |

另有 23 个 `baek_block`，每块从 2×6 的 28 状态压缩，容量 22、洞需求 6；8581 条增长蕴含被检查。残余 1187 行由 1164 个 cyclic 行及 23 个 block 行不交且完整覆盖。最小树叶整数余量分别为 21 和 1，分母尺度为 1000000。负控包括反转 cyclic 顺序、重复状态、不完整分支及错误块阈值，作者回执均记为拒绝。

这份回执可以作为**由归档哈希绑定的作者封存执行证据**使用；它不是我们运行的检查结果，也不是经形式验证的 Python checker。

`audit/joint_rebuild/verification.json`（SHA-256 `386fc5a40b54187743a3bf5e7305d7b0e8de5aa459defa35852881d66372f92f`）是更直接的共同 Lean 构建回执：`status=PASS`、`mode=full-clean-rebuild`、208 个源模块、237 项 formal manifest，1292.941 秒；作者机器为 `arm64-apple-darwin24.6.0`。固定版本：

```text
Lean 4.32.0-rc1
Lean commit b4812ae53eea93439ad5dce5a5c26591c31cb697
mathlib commit 360da6fa66c1273b76b6b2d8c5666fd5ac2e3b56
```

ES8 最终定理依赖 `Classical.choice`、`Quot.sound`、`propext` 及八个 native-evaluation 公理：两棵树、balanced 盒表/cyclic、residual 盒表/cyclic、block 有效性/覆盖各一项。`formal/sources/ES8/Certificates/Native.lean` 明说这些是编译器信任下的有限算术回放，不是 kernel-only 评估。`audit/revision_1_2/verification.json` 则明确为 `existing-source-identical-build`，不能另称一次 clean build。更早 `audit/es8_sealed_release.json` 指向的是另一个 319 完成包的 SHA，不能拿它代替本次共同归档身份。

## 3. 数据、checker 与 Lean 绑定

以下路径都相对于 ZIP 共同前缀；完整哈希表见上述 JSON。

| 用途与路径 | SHA-256 |
|---|---|
| Python finite checker：`tools/check_octagon_finite.py` | `9c9c48954c155270c0c0baa8cff686608705583657cc73fcb72c8cce866929b5` |
| 树算术 checker：`tools/check_octagon_arithmetic.py` | `1ce1fe937eeb0118305e839c8f983053ba6d8a8411ff337a2e129804e464ada9` |
| balanced 目录、行、叶权和树：`certificates/balanced.json` | `23363c9e341a7edf4de28b6bf21970983cc6d4cafa6f2bdef54ce3d25b1c5a94` |
| residual 目录、行、叶权和树：`certificates/residual.json` | `bccd12477064d8a490bbe863ae49dbc8d9dfececf7a65426ba36f7537c66293a` |
| balanced Lean 目录：`formal/sources/ES8BalancedCatalogData.lean` | `b0a5a964c898d00535ac4f9c454c1ac32a6f7d170f658e3f449a524f41bfe12b` |
| residual Lean 目录：`formal/sources/ES8ResidualCatalogData.lean` | `9a8453ddfdc32496e2273a7d6f7c53da8aeb67576f8873fd55c616e600e717b9` |
| balanced cycles/盒表：`formal/sources/ES8CycleData.lean` | `f9131e0803a88a4eec49eb0f2a48c50560e65bedf289c9dba1a37b63f648643d` |
| residual cycles/盒表：`formal/sources/ES8ResidualCycleData.lean` | `a79dcd5b72a62fd21d47439f8297835e7ed33e7cfeca6408ee18a3ed402a4681` |
| block 数据：`formal/sources/ES8BlockData.lean` | `c116d7be3ca01083334f5daced97ca38cd6155db4c24aef0cece02566ee864fa` |
| balanced Lean 行、叶、树：`formal/sources/ES8/Certificates/BalancedData.lean` | `a3731422478b3ca6f160d02e523c53c6f380e03bbe2993823d331ab0713e084c` |
| residual Lean 行、叶、树：`formal/sources/ES8/Certificates/ResidualData.lean` | `9c86709852cc3bc546a61ecb9b0ccdba72e869438bf7943b9484da5f445f63dc` |

`certificates/PROVENANCE.json` 的四个 JSON/Lean 数据哈希与实测完全一致。有限 checker 重建 Ferrers 目录和全部有向差，逐项比较 Lean 目录、盒表、行、叶权、树文字常量，而后进行全树回放。因此“JSON 行成立”与“Lean 原件确实使用相同数据”有明确的源码检查接口，不只是数量相同。

`certificates/README.md` 还解释：JSON 中历史 `mixed_cut` 字段保留来源身份；其中全部 973 行在当前 `ES8ResidualCycleData.lean` 中均有直接 cyclic 证书，不需要额外的 mixed-cut 几何假设。residual 状态是 4×6 目录加尾零，删除第一列高度 6 而第二列未满的状态；不是无条件全 4×6 域。

## 4. finite cyclic validity 的精确范围

对状态下理想 A、B，checker 令 D(A,B)=B\A。给一个有序三态 (a,b,c)，逐一检查六种真实时间顺序。若某个 D(a,b)、D(b,c)、D(a,c) 为空，该时间顺序不能出现在真实状态增广中；其余情形检查相应坐标满足

```text
max coordinate(D(b,c)) ≤ min coordinate(D(a,b)).
```

该条件阻止一种颜色的严格增长，因而强迫另一色。cycle 内三态的位置奇偶决定所检查的坐标：cap,cup 坐标下偶排列检查 cap，奇排列检查 cup。其输入只有有限状态、真实有向差及严格标签增长；**有限 `Safe` / `CheckTriple` 定义本身没有额外实平面可实现性假设**。

但源码向“任意占用八态不可能”的转接是实平面定理：

- `ES8CycleSigns.checked_triple_positive` 明确接收真实点 `p : Fin n → Point`、颜色与定向符号的等价 `signs`、非零定向 `nonzero`。
- `ES8CycleRows.Model` 保存上述真实点、增长标签、占用单射和有向盒适配。
- `ES8Cyclic.cyclic_positive_convex_position` 从所有 cycle 三元组正定向推出真实凸位置；`ES8CycleCapacity.occupied_cycle_capacity` 对实际占用位置应用它，洞位不补虚点。
- `ES8CycleValidation` 与 `ES8ResidualCycleValidation` 用 native_decide 接上有限盒表和 cycle 检查。

因此可在本项目中直接复用有限“强迫 cyclic 三元符号”的数表条件；若目标改为抽象有序 rank-3 signotope 的 weak8，还须在该对象内证明“这些 cyclic 符号 ⇒ weak8”的桥。不能因为 Python finite PASS，便把整个 ES8≤319 几何定理自动改写成抽象 signotope 上界。23 个 Baek 压缩块还各有其容量进口，须分别核对抽象对象的可用定理。

## 5. 本轮 Linux 实际复放：PASS

父会话随后授权本项目 Linux 实际复放。隔离目标：

```text
/data/ktqiu_hdd/math_agent/reports/n79-overlap-20261116/schroeder-octagon-replay-20261116/
```

只读搜索目标 tmp/reports 的 maxdepth5 未发现旧同名原包。SSH 实收 `hostname=ubun`。最初新连接多次被关闭；父会话代送冻结启动脚本后，远端 Zenodo 下载实际返回 HTTP403、`download.exit=22`。这些不是数学检查失败。

随后从本地已核完整 ZIP **只复制有限 checker 所需的15个公开原文件**，生成 `octagon-source-replay/finite-inputs.zip`，10026826 bytes，SHA-256 `a1ea809858958d59e457b0bdf77952b9f6913aef31d1f67e61a08943291cc8b9`。一次明确限定此包与目标目录的 legacy `scp -O` 上传成功。Linux 收到的是该子包，不是240MB原包；不能宣称 Linux 重算了完整原包的官方 SHA。

已核实显式 `gpt-6.1-sol/high` 的本执行者通过其自行建立的 SSH 长连接完成后续复放。`octagon-source-minimal-replay.py` 在 Linux 校验子包 SHA、官方 manifest SHA 和全部14个被 manifest 列出的输入文件（manifest 自身另核），然后后台有界执行：

```text
timeout 360 /opt/anaconda3/envs/forktqiu3/bin/python3.12 -B replay-minimal.py
```

内层原作者 `tools/check_octagon_finite.py --output finite-result.json` 另有300秒时限。实际 Linux 平台 `Linux-6.2.0-34-generic-x86_64-with-glibc2.35`、Python3.12.12。结果：**`replay.exit=0`，`checker_exit_code=0`，`status=PASS`，8.538秒，`author_result_equal_except_seconds=true`**。因此§2全部有限计数和两棵全树已由本项目真实复放，除耗时外与作者回执一致。未执行 Lean 或 native evaluator。

本地已定向回收原始证据至 `octagon-source-replay/`：`replay-receipt.json`、`finite-result.json`、`finite-stdout.log`、空 `finite-stderr.log`、`replay.exit`、driver及失败下载日志。原始回流包 `replay-evidence.tgz` 的 Linux/Windows SHA 同为 `5c9416c379d91770f71059bcb307b96ea9ab33a358b2c78fe0cf186ef69b6fcf`；执行 driver 的两端 SHA 同为 `fc9359777862ca9f379724470ef80de876120aa919af9f258a85087ab3fe6ddb`。`finite-result.json` 与 stdout 的 SHA 均为 `42aaa3ca04924b10dd47e2ee48d9b9f2c1102d54e73db4b66c1f1e645f51f65d`。

共用只读原件根为上述隔离目录下 `source/es7_es8_bounds_81_319_v1/`；其中只含15文件。控制脚本及全部失败/成功控制回执仍保留；没有触碰任何旧进程或封存原件。此 PASS 的范围是有限 checker 和实际数据绑定；§4所述抽象符号/几何桥仍须分别连接。

## 6. 本项目另补的纯组合 cyclic→weak 桥

本节是本会话新增的短证，不冒充公开包中已有的抽象定理，也未经过独立审阅。它补上§4对 **cyclic 行**指出的对象运输义务；不处理23个压缩块的另一个容量进口。

**引理。** 设一个完整有序 rank-3 signotope 的某实际顶点子集带循环次序 C，且其每个有序三元组的颜色，等于该三元组相对于 C 的循环定向符号（可整体交换两色）。则该子集任意 m 个顶点给出 weak m；从而无 weak m 的输入中，任一通过上述六时序认证的 cyclic 行至多占 m−1 态。

**证明。** 取这 m 个实际顶点中时间最早、最晚的 A、B。其余点分成循环上 A→B 的开弧 I 与 B→A 的开弧 J；固定前者的三元组 (A,u,B) 为正色，后者为负色。

取同弧两点 u<v（这里是实际时间序）。对四个实际顶点 A<u<v<B，按删去 A,u,v,B 的顺序列出四个三元颜色：

```text
(u,v,B), (A,v,B), (A,u,B), (A,u,v).
```

若 u,v∈I，而循环弧 I 上 v 先于 u，则这四个符号恰是 `−,+,+,−`；若 u,v∈J，而弧 J 上 u 先于 v，则恰是 `+,−,−,+`。两者都出现两次符号变化，违反 rank-3 signotope 的四点 packet 条件。因此 I 中实际顺序必须沿 A→B，J 中实际顺序必须逆 B→A。

将 I 中顶点按实际次序置于 A、B 间，所得路径所有三元组均为正；将 J 中顶点按实际次序置于同一 A、B 间，所有三元组均为负。两条真实同端路径的长度和为 |I|+|J|+4=m+2。空弧给两点路径，其颜色条件为空。故构成 weak m。证毕。

六时序 finite Safe 检查逐三态保证：无论实际时间怎样排列，只要三态占用，其实际三元色就具有指定循环定向。应用本引理不要求 D=E，也不要求顶点实平面可实现；可分别用于真实 D 或真实 E 的状态注入，不能把两个注入的不同洞集混合。对 m=8 得各公开 cyclic 行占用≤7，对 m=7 得认证 cyclic 行占用≤6。作者原树中的其他约束仍须独立接入，有限树 PASS 本身没有替代这项检查。

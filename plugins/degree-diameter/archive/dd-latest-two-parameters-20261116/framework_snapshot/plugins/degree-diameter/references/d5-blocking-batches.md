# D5：极小核心集合与共同补全

本接口来自2026-11-15本地 (12,5) 的42403…42411九个合法版本。数学独验已通过；源图具体 Lean 前提仍未闭合。它们由当时整合版生成，本次维护只回收方法和程序，不追认为维护后新成果。

## 数学条件与实现范围

当前完整图为 G，最大度≤Δ、已有直径≤5；F={v:deg_G(v)<Δ}。选择互异 S⊆F，|S|≤Δ，且所有 B4_G(s) 的并覆盖完整 V(G)，则加 z 并连 S、保留全部旧边得到同参数合法图。旧点对继承原路径，新旧点对经一个 pin；后继每一步仍须针对当时完整图。

当某个已绑定几何接口提供“命中全部核心行即可覆盖核心”的充分证书时，可枚举 inclusion-minimal 核心命中集 P，再在 **全部当前 F∖P** 中用剩余 Δ−|P| 个位置共同补齐外围。对于任何具该证书的完整 S，其中都包含一个这样的 P，S∖P 可作为尾部，所以此分解不必强加角色配额。它只对该证书域保真，不代表全部合法图必有这种几何证书。外围包含作者原附点、本地新增点以及此前全部前缀；每次重新计算当前 provider，并对命中实际检查全图 B4(S)。

旧85模板、11+1、10+2、最早命中的平面及枚举顺序都不是数学必要条件。真实成本是实际映射后不同 pins 的数量及当时余度。只在 Frobenius 稳定且所用共轭对未 split 的已绑定情形下，f 个固定点＋p 个二点对的 raw 大小 f+2p 对应 f+p 个端口；不能把此公式强加到别的折叠。raw 更少也可能更贵。

`tools/d5_blocking_batch.cpp` 保留成功程序的搜索逻辑，但将42403源及8步上限改为明确输入。本实现仍限定 Δ=12、原核心标签<41356、754张原平面的91行；它不是任意 D5 源的通用生成器。迁移时必须重新绑定核心覆盖引理、折叠与完整外围，不能只改常数。

## 收件和下次输入

父调度先读原件并作实际接受判断。`extension_receipts.py` 只核已有作者/独验收据的源、每个前缀与终图相容，然后更新原 STATE.json 的 `current_context`；不运行 BFS、不新造数学接受、不改变 Goal 状态/认证缺口。重复消费同一批次不会重复增加成果数。现格式只处理当前逐点保边 checker，别的构造使用其真实验收返回。

已消费的旧成功收据也不能覆盖同图后来收回的零新增 UNKNOWN 或限定域 No；它仍是有效的历史成功，当前停止决定保持。原 STATE 配置 `current_context_view` 后，收件写回会自动更新已有阅读视图，不再依赖手工补跑渲染命令。

每批作者与独验使用各自不覆写的原件路径。适配器在同一家族的 `consumed_receipts`
保留已消费的路径对，旧零新增收据重读也不会抹去后来停止状态；不按 UNKNOWN／No
排严重程度，真正新的一批仍可更新当前决定。已有历史不会被自动推断为已登记，首次接入仍由父调度核对。
派工前可把本批最终 `RESULT.json` 登记到原在途项的 `terminal_result`；结果返回后先由父
收件，再生成下次任务输入。不要登记运行中输出，也不要因作者终态存在而跳过独验。

```bash
python3 /path/to/MathRSI/plugins/degree-diameter/tools/extension_receipts.py \
  --state /task/STATE.json --family 12,5 \
  --author /task/batch/RESULT.json --independent /task/batch/independent/RESULT.json \
  --acceptance-basis '父调度已读取原件；逐前缀独验通过，源D5进口沿用；具体Lean仍开'
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --output /task/CURRENT_RESULTS.txt
```

首次接入用现有已核结果初始化 current 区，保留原目录和历史；本轮全局基数163版本/44参数/49具体Lean与新增九个同参数版本分开。以后同一家族的共享源证明、真实证书绑定、实例装配分别显示，原理定理不代替具体源 Lean。不得为每个 wrapper 重开同一个源认证任务。

## 有界续批

```bash
python3 /path/to/MathRSI/plugins/degree-diameter/tools/d5_blocking_batch.py \
  --state /task/STATE.json --planes /task/RAW_PLANES_ACTUAL_IDS.txt \
  --output /task/new-batch --max-new 8 --cpu-limit 20 --wall-limit 480 --plan-only
```

这些限额是命令示例，父调度按现有授权和剩余预算选择。`--plan-only` 读取已接受最新前缀及源文件头，不构图/编译/求解；去掉它才执行，且数学 Goal 必须 ACTIVE。输出目录必须新建，旧实验原件不覆盖。编译、控制检查和 native 共用预算；异常也保存已用资源和终态，保留已刷出的前缀待核，不能称全域 No。

实际执行时从原 STATE 再读状态，并复用 base 的已登记终态收件检查，
在创建批次目录和启动编译之前完成。保存过的 ACTIVE plan 不覆盖后来的暂停，
直接运行本程序也不能绕过已经返回的 `terminal_result`。
同样复核计划绑定的源路径、点边数、当前最新合法前缀和生成域；若父调度在计划之后
已经接受新源，旧计划在创建目录或启动进程前退出，须重建计划，不静默切源。
`--plan-only` 仍可只读查看；父调度先消费返回事实，再按原授权执行，不自动接受作者候选。

`BATCH_LIMIT_REACHED` 表示达到本批实例数；`UNKNOWN_*` 表示预算内未决；`COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN` 只限当前图的指定充分证书域；进程错误独立记录。父调度收回后选择另一有限批、迁移或暂存，不自动接无限循环。当前新版本先经原独立核验流程，随后再收件。复用保边原理的审阅不免除任何前缀检查，最终合同的形式化和审阅仍保留。

批次 `RESULT.json` 另给实际终止阶段 `stage`（compile/control/native/native_result/finished）、native 调用是否尝试以及 `search_started`。后者根据已刷出的步骤计数或完整作者前缀判断；只有调用尝试而无实际输出时保留未知，准备完成也不代表核心搜索开始。`author_prefixes_written` 只数完整作者记录，仍为待独验产物，不能增加 accepted 图计数。中断的半行输出保持未完成，不当作另一张图。

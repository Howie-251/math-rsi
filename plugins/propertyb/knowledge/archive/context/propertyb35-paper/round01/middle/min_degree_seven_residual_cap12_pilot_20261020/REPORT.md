# 本批13个全λ≤4剩余谱全部闭合

最新收尾见 [BAD_KERNEL_AUDIT.md](BAD_KERNEL_AUDIT.md) 与 `BAD_KERNEL_CHECK.json`：root的新共享坏核计数已独立核验，给当前两键实际 $C_3\le12n_3+18$，最终 $2L=5437440,5439576$，余量8000／5864。于是本批原13谱在声明进口下全部闭合。本文其余内容记录前置完整域和局部证据；不包括18个唯一pair5例外谱的整支结论。

# 前置cap12补门与最后两键的来源

本批对13个已具全λ≤4非B门的剩余degree谱、63个保存moment键定位缺口。只处理实际相关37种quad，其中旧 $10^4$ 的310域／304strict直接复用；36新quad的22684 labels／2901 D8代表按真实τ条件过滤到2633，仅用旧3四锁位置quota0。主pilot CPU1.632567秒，无原H枚举或新布局。

实际得到2620新strict、13新失败。另有旧 $10^4$ 四个τ8失败标签。`RESULT.json` 保存全部17失败的35边投影、K6成本、最小τ、受影响真实键与可用外七池。

root另授权独立代理在 `independent/` 完整复核：exact高迹生成36quad22684 labels／2901 D8，τ-filter2633与63contexts全相等；2633选定证书的原35索引55293行逐项相等，包括全部13新失败。2620strict最大1101/1105，实际PASS；其单独完整运行CPU20.301257秒，未冒充本代理5秒pilot预算。

49/63键的全部实际cap12 caller已经齐备，重算后48键strict，原剩15。原共享P下完整谱50,53,78,83,84,88,93闭合。再合root新vertex-flag P容量，15键又strict12，完整谱52,85,89,98也闭合；此步条件于root的新P引理，未在此重复证明或扫描全矩域。

剩余τ8键又有真实选点修复：九七池避K-singleton原边、K6预算耗尽使全部外pair共度≤2、十一度点外row全二。两源各十五必要七星，30份固定证书经630行原35索引独立核全strict，最大64/65与1413/1430，连S4运输均实际核。S95τ8键因此2L=5431764严格。

进入共享坏核收尾的两个必要键（均已由上述新计数排除）：

| 谱 | n=(n0,n1,n2,n3,n4) | τ | newP | 2L |
|---:|---|---:|---:|---:|
|90|(29,525,0,32,9)|10|12552|5446848|
|95|(28,525,2,31,9)|9|12546|5448312|

最坏无singletonS90源已做一个十五域的前二view pilot，第二view仍不严格best35317/34320，立即停，没有扩位置。其共享列／余τ／实际外七池的准确接口保存在 `IMPLICATED_THREE_KEYS.json` 与 `SHARED_COLUMN_ANALYSIS.md`，没有宣称LP不可行或假松弛可实现成H。

正文及入口：

- `PROOF.md`：13谱实际caller、分类覆盖、49键refinement及当前scope。
- `K6_BUDGET_LEMMA.md`：实际六pair成本＋四组17外行的无重复预算、旧六尾τ8／9运输。
- `LOW_TAU_PROOF.md`、`LOW_TAU_VERIFY.json`：真实九七池补门及30独立证书。
- `CAP12_KEY_REFINEMENT.json`、`NEWP_REFINEMENT.json`、`LOW_TAU_KEY_REFINEMENT.json`：63→15→3→2的全部精确键与容量。
- `independent/RESULT.json`：另代理对2633新证书及完整域的独立确定性核。

本代理所有新计算CPU不足5秒；独立2633批次另记。模型审阅独立性same-family/provisional。18个唯一pair5例外谱未处理；没有宣称全部21点或m(5)≥36已证，无Lean／v2。

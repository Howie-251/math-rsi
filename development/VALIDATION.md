# MathRSI：自包含技能与 Property B 重建验收

2026-11-01。本轮验收的是可以实际接手研究的技能、知识与工具连接。首版只有总控与薄插件，未满足用户要求；其测试保留在[历史记录](VALIDATION_FIRST_VERSION.md)，不再作为当前能力层完整性的依据。

## 实际交付与阅读

Base携带ARIS固定提交 c485faa59a68e51c6575dea67ca57abc7a6a2b9c 的30项技能双宿主完整副本及资源，[来源清单](../base/ARIS_SNAPSHOT.json)固定实际复制范围。MathRSI总控负责数学目标、前置广搜、义务/路线选择、并行、验证与交接，实际读取并消费仓内各技能。[调用说明](../docs/ARIS_REUSE.md)明确helper来源、双宿主路径及外部运行依赖。

Property B重建为领域总控、文献、下界研究、证书四项技能。正文包含归约选锁、真实迹与分类、排列与共同坏对、signed修复、共同结构、一般k完整证明、小参数迁移、L1–L117库存；实务层包含具体失败、反例、计算效率、Lean接口/性能与完整执行案例。原wiki、证明、研究源码、完整Lean源码和选定输入/PDF随仓保存，不要求另一份aris4math目录。

实际阅读范围分列[数学报告](propertyb-rebuild/MATH_READING_REPORT.md)和[实务报告](propertyb-rebuild/PRACTICE_READING_REPORT.md)。全文提炼、定点核读、仅复制原件明确区分；没有把归档数千文件称为重新数学审计了全部材料。

## 实际本地功能验证

|验证|证据|准确范围|
|---|---|---|
|ARIS副本与搬迁执行|[Root复验](aris-integration/root-smoke/RESULT.json)、[来源报告](aris-integration/BUNDLE_REPORT.md)|207份上游文件；搬迁后9条本地命令：wiki三条、路由解析四条、双端HTML两条；未知后端按预期exit2，其余exit0|
|五项自写技能格式|[正式validator输出](propertyb-rebuild/SKILL_FORMAT_RESULTS.json)|主总控与Property B四技能均通过quick_validate；只验技能元数据|
|六元已完成案例|[本次结果](propertyb-rebuild/practice-replay/m6/independent/RESULTS.json)|M65、379必要型、621579共同整数向量，最紧682298/682341；不是本次重跑m6≥67|
|signed错误推广|[实际输出](propertyb-rebuild/practice-replay/signed/PRACTICE_REPLAY.stdout)|显式十点输入的1024红子集、合法修复0，只反驳所述泛化门|
|component无收益路线|[复放结果](propertyb-rebuild/practice-replay/component/VERIFY.json)|C++重新编译运行，Python核33867小图及明确松弛最大值；并非构造原超图|
|十二元已有独核范围|[本次结果](propertyb-rebuild/practice-replay/k12/independent/RESULTS.json)|完整664355键/692点数域与真实迹重建，20例Fraction；不是第二套全表概率复算|
|独立接手七元|[完整forward-use报告](propertyb-rebuild/forward-use/REPORT.md)|未参与写作的Sol仅凭仓内材料重放424型，独核2115296共同整数向量；核对完整原H到原染色的自然语言链|
|下一预算不能沿用旧PASS|[具体诊断](propertyb-rebuild/forward-use/SCOPE_RESULTS.json)|130→131边新增13双锁键、旧三锁保证失效、两旧布局不再严格；没有将松弛失败当不可染超图|
|一个完整短证明|[五元26点排除](propertyb-rebuild/forward-use/PROOF_PACKAGE_26.md)|明确paircover前提下每点至少七度，182>165；没有把内部前提添加到原题|
|八/九元缺件修复后的完整独核|[搬迁报告](propertyb-rebuild/final-portability/REPORT.md)|2094/3450型精确匹配且严格，八元299组件配额；CPU约8.862/27.740秒|

实务四组本次墙钟分别约1.45、0.023、0.198、3.02秒，见[运行总记录](propertyb-rebuild/practice-replay/SUMMARY.json)。七元作者/独核分别约1.81/2.50秒，见[命令](propertyb-rebuild/forward-use/COMMANDS.json)。全部在独占工作副本执行，原项目和archive不被旧脚本改写。

独立使用也暴露了真实衔接问题：wiki把条件写进实体页，但自动query_pack没有收入部分positive idea内容。已在[工作区说明](../docs/WORKSPACE.md)明确按当前义务读取实体页、让恢复入口直链关键条件；不把helper退出零当自动摘要完整。

## 搬迁与依赖

维护文档与仓内相对发现别名由tools/check_links.py检查；最终Root检查41份文档、783条本地链接无缺件；独立搬迁时为781条，随后补入两条实测报告链接。历史archive的旧展示/日志引用不在这一结论内，上游资源另由base smoke验证。没有安装到全局技能或改用户私有reviewer配置。

独立搬迁检查发现八/九元检查器缺输入JSON；Root已补入实际读取的CERTIFICATE.json/CANDIDATE.json并更新库存。修复后两个完整独核在搬迁副本均exit0；73项发现别名全部在副本内解析。[命令证据](propertyb-rebuild/final-portability/COMMAND_EVIDENCE.json)保留修复前缺件与修复后的真实检查，不抹去发现过程。

Base smoke只解析reviewer配置，未调用模型；HTML验证的是模板生成和原始公式文本保留，不声称已嵌入离线数学SVG。本轮未运行Lean/Mathlib或TeX构建，既有形式证明状态来自原项目记录与随仓源码。

## 模型审阅与最终范围

Gemini 4参与自包含设计、Property B内容组织和成稿核读，前两轮是协作意见，不称独立验收。最终回复曾错误描述本地测试范围，Root逐项对照原结果纠正，Gemini已明确撤回。原回应与更正全部保留，不能只摘取认可结论。

Grok做成稿的独立有限范围审阅。实际模型、返回状态和逐项处理见[审阅处置](propertyb-rebuild/REVIEW_DISPOSITION.md)，原回应在其reviews/。跨模型审阅未执行数学程序；forward-use来自同家族Sol，保留provisional。具体数学成果各自的原有验证范围没有因本次开发而升级。

本次没有恢复35 Lean、36或ECC研究，没有重新判定全部历史数学成果，也没有评测通用解题率或提速倍数。ECC仍是首版草案，留给用户安排的领域agent。当前本地仓库未远端发布。

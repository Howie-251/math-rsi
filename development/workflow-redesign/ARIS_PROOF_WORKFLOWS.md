# ARIS 证明与知识库工作流：逐项原文合同阅读

日期：2026-11-01。只读源：`/Users/rfy_naiveai/Desktop/aris_main`，实际 `HEAD=c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。本文是 MathRSI 重设计的输入材料，不是已经修改或运行的新工作流。

## 阅读范围与证据边界

**完整阅读**主线 `skills/{proof-orchestrator,proof-checker,proof-writer,lean-formalize,formula-derivation,research-wiki}/SKILL.md`（分别255、900、236、376、285、462行），包括模板、可选分支、输出与失败合同，而非只读目录/标题。完整阅读 `proof-orchestrator/references/` 六份 Markdown，以及 `lean-formalize/references/` 三份 Markdown。完整阅读仓库 `AGENTS.md`、`CONTRIBUTING.md`，并读 MathRSI `AGENTS.md` 与当前 `base/skills/mathrsi-research/SKILL.md`。

Codex 比较采取主线全文＋完整差异阅读；`proof-checker`、`research-wiki`差异较大，另读其完整实质流程（605、421行）。`proof-writer`、`formula-derivation`实质正文同主线；`lean-formalize`与`proof-orchestrator`的全部宿主差异已读。三份 Lean reference 双端逐份比较一致；orchestrator 六份 reference 中三份一致，另外三份完整读取差异。

**共享参考为有目的的部分阅读**：全文读 `reviewer-backends.md`（156行）、`reviewer-independence.md`（79行）、`capture-antipatterns.md`（78行）；细读 `integration-contract.md` 1–130、215–350、360–440，`assurance-contract.md` 63–213，`fan-out-pattern.md` 16–95，`external-cadence.md`129–166，`review-tracing.md`1–48、137–195；读双端 reviewer-routing 的默认、能力fallback与选择合同，并检索其余大节。没有逐行审计全部2671行共享参考、第三方论文、浏览器/模型桥接源码或整个wiki程序。为核对两个wiki文档差异，静态读 `tools/research_wiki.py` 的 init、query-pack方向提取等实际片段；没有执行helper。

以下定位的 `skills/...` 均相对上述源仓；行号固定于该revision。本文不调用研究模型、不运行Lean/TeX/数学计算，不触碰 aris4math/v2 研究文件。源文引用是本地一次阅读的证据，不宣称新设计已经通过执行验收。

## 1. 首先区分六个入口：它们没有一个共同的“什么都做”语义

|实际输入/请求|进入技能|它独占的主要产物与出口|
|---|---|---|
|公式主线、顶层对象、假设尚未稳定|`formula-derivation`|`DERIVATION_PACKAGE.md`；coherent/reframed/blocker；固定claim后才进入proof-writer|
|明确命题、假设和记号，要求证明/反驳/补证|`proof-writer`|`PROOF_PACKAGE.md`或指定已有目标；完整原命题证明、显式修正版证明、或准确卡点|
|跨run续接、困难证明的本地尝试与GPT Pro交接|`proof-orchestrator`|`prompts/<YYMMDDHH-num>/`的一次run；local attempt→audit→final或手动handoff；不是proof-checker替代品|
|已有完整证明要求严查、修复、提交前验收|`proof-checker`|`PROOF_SKELETON.md`、`PROOF_AUDIT.{md,json}`、报告、`PROOF_CHECK_STATE.json`；canonical审计及wiki claim出生点|
|要求Lean、继续已有Lean、或某项具体义务值得形式验证|`lean-formalize`|项目原有spec/ledger、实际Lean主模块/声明、build/type/axiom证据与handoff；无强制新文件名|
|建立/维护/查询项目知识库|`research-wiki`|同一个`research-wiki/`、规范实体/图、日志与query pack；不是自己给定理验真的新裁判|

依据：formula L3、19–44、250–268；writer L19–36、40–44、202–219；orchestrator L3、9–19、32–66；checker L3、61–74、733–755；Lean L25–34、60–95、329–367；wiki L20–42、60–78、420–437。

重要的调用区别：原文有些位置是“该用哪个技能”的入口判定，并不意味着每一次写证明必须顺序调用六技能。`formula-derivation → proof-writer`是目标成熟后的条件交接；writer/orchestrator/checker都只在明确需求时接Lean；普通证明不必先建GPT Pro run，不必最后制造论文审计或HTML。Lean已明确禁止父子互调递归（见下）。

## 2. formula-derivation：先把理论对象搭顺，再把一个确定命题交给证明技能

入口读取顺序是用户指定文件→本地notes已引用的derivation draft→根目录`DERIVATION_PACKAGE.md`。已存在文件必须先读再更新相关节；不会直接写paper/appendix `.tex`，除非用户指定那个目标（L48–64、139–149）。输入同时包含目标现象/关系、角色、原假设、记号、散乱公式、相关本地文件、希望输出的文体；歧义先写清采用何种解释（L26–44）。

实际八步是：①采集上下文；②固定所解释/推导的target以及它是identity、proposition、approximation还是interpretation；③选择组织整条推导的invariant object，并判断旧量是本体、proxy、slice还是approximation；④整理假设/记号/参数是否固定或自适应；⑤逐步标注上述四类推导性质；⑥建立目标、所需identity/lemma、假设用处、近似进入点与特殊/一般情形的derivation map；⑦写指定文档；⑧核对对象稳定、假设明确、精确/近似未偷换、最终路线仍支持target（L46–181）。

固定输出段为Target、Status、Invariant Object、Assumptions、Notation、Strategy、Map、Main Derivation、Remarks、Boundaries and Non-Claims、Open Risks（L183–226）。三种分支分别交回原目标coherent包；指出错配并提供reframed对象/假设/范围后的包；或`NOT YET COHERENT`及具体缺口（缺对象、假设不稳定、符号冲突、无依据近似或条件不够）。**不能把coherent误读成某定理已证。**

后继判定写得很清楚：exact claim fixed、assumptions stable、notation settled，并且下一任务是rigorously prove/refute，才转`proof-writer`（L250–263）。若其中具体义务要Lean，才转`lean-formalize`（L265–268）。该技能没有自带外部reviewer、自动迭代直到PASS或专用恢复状态；恢复是读已有文档再更新。

## 3. proof-writer：对准确命题作实质作者工作，交回一个能接入caller的证明包

入口目标优先级同类但独立：用户明确路径→本地notes/theorem引用的proof draft→`PROOF_PACKAGE.md`（L40–55）。它不接管全部项目状态，也不默认把草稿写进论文。先读原目标、抽取exact claim/assumptions/notation/sketch/nearby lemmas，再规范化而保持用户原命题；更方便的强表面normalization只能是internal proof device（L57–70）。

执行顺序：①上下文；②规范化claim；③**先可行性分诊**为`PROVABLE AS STATED`、`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`、`NOT CURRENTLY JUSTIFIED`；检查引用条件、过强结论、明显反例与量词失败；④挑direct/contradiction/induction/construction/reduction/probabilistic等实质策略，写依赖图与每步假设，困难步骤单列lemma；⑤写带编号主要步骤和每个非平凡implication的proof package；⑥核对原声明、实际证明、假设、方向、引用适用性、退化情形与未证依赖（L85–160）。

成功输出完整原命题证明；原题过强时输出“为何原题不成立/未获支持＋显式corrected claim＋最小附加假设＋修正版证明”；证不完则降级并精确写缺lemma/invalid implication/hidden assumption/counterexample方向，及完成需要什么（L202–219）。“Prefer weakening”不能在总控中被实现成悄悄替换用户目标：原题是否survived unchanged是最终必须答复的一项（L221–235）。

**Lean调用/返回合同（L72–83）**：只在用户要求或具体formalization实质帮助正确性时，把original statement/current attempt/known dependencies交`lean-formalize`。收回checked scope、exported theorem和remaining obligations，接回当前proof package。若writer本来就是Lean为补数学论证调用的子任务，则返回证明/缺口给原Lean run，禁止再调Lean递归。部分Lean结果只关闭相应义务。writer没有自行执行canonical proof-checker审计或创建verified wiki claim的权限。

## 4. proof-orchestrator：有run血缘的local-first工作流，卡住才做窄交接

### 4.1 产物、恢复与本地成功路径

工作目录为`prompts/<YYMMDDHH-num>/`，按需使用`task.md`、`materials.md`、`local-proof.md`、`sources/`、`source-manifest.md`、`browser-prompt.md`、`handoff.md`、`gpt-pro-output.md`、`deepseek-review.md`、`audit.md`、`final.md`，可选`codex-ledger.md`与`next.md`（L32–56）。没有发生升级就不要先建browser prompt/handoff/remote state，除非用户已经要求直接handoff或跳过local attempt（L58）。

恢复先读prior final/audit/local-proof/ledger/source-manifest/handoff及next/redo/continuation；raw GPT output仅是证据，未经audit不继承为定理。**新proof work开新run**，登记prior run ID、读过的准确文件、继承的proved/conjectural/rejected claim、保留sources以及单一当前义务。旧run和旧GPT对话追加保存，不覆盖。再次升级时新prompt与fresh GPT conversation；matching ChatGPT Project可复用（L60–66）。这与Lean“复用原有简短continuation”不是同一个状态所有权，不能把所有任务一概强制成orchestrator run。

主顺序（L117–170）：freeze exact target/assumptions/quantifiers/sources→按需要维护稳定本地source→**真正尝试原proof/disproof/counterexample/diagnosis**→写`local-proof.md`→成功`LOCAL_PROVED`→local correctness/source audit→notation与target-first exposition编辑→`final.md`。本地失败则`LOCAL_BLOCKED`，隔离smallest hard obligation后才准备升级。local correctness逐条查theorem/reduction/equality/bound/constant/quantifier，区分proved/imported/conjectural/repaired/unsupported；optional remote意见不代替本地audit（L129–153）。

可按需求调用`lean-formalize`，但复用当前run的target/continuation并记录Lean entry、checked scope、next unresolved obligation；Lean不成为每个proof或handoff的先决条件（L130）。

### 4.2 升级、回收与精确授权

manual GPT Pro是默认：维护sources→manifest每源相对路径、browser-visible稳定文件名、作用、单独上传或材料摘要、ready/missing/optional/returned-by-user→self-contained exact `browser-prompt.md`，不放本地私有路径/路由账务→要求distinct completion marker例如`END_GPT_PRO_OUTPUT`→`handoff.md`给上传顺序、粘贴prompt、返回结果保存位置→`READY_FOR_MANUAL_GPT_PRO`并等待（L154–159、212–227）。required source缺失就handoff blocked，不能用记忆替换。

只有当前run明确授权执行者去操作/调用GPT Pro、且外部`call-gpt-pro`确已安装，才能`READY_FOR_CODEX_DISPATCH`并读取该技能、确认web/API及spending/upload范围，按它完成（L160–164）。泛泛“use GPT Pro”在该技能原文中不足以授权browser/API spending；旧run授权不自动继承；browser失败不能转API。**这是这个特殊GPT Pro分支自己的限制，不是每次MathRSI调用已授权reviewer都要重新确认。**

返回保存raw `gpt-pro-output.md`，只修无歧义复制损伤（completion marker、数学delimiter、明显brace/operator/分隔符），不改claims/constants/assumptions/status/proof order；完整correctness audit后在`final.md`做实质编辑。中心缺口仍在则`NEEDS_GPT_PRO_REDO`，先准备focused manual redo；自动redo需本run新的明确授权（L165–170、229–241；reference `dispatch-prompts.md`148–227）。

### 4.3 Optional DeepSeek与编辑gate

仅当前proof run明确请求DeepSeek/independent second opinion触发，困难本身不触发；普通`proof-checker`请求不得改道此branch（L172–177）。顺序是exact proof boundary→explicit quantified restatement→`proof-audit-rubric.md`的obligation ledger→`deepseek-routing.md`已声明路由→raw `deepseek-review.md`→本地核每个serious issue和counterexample→按`audit-output-contract.md`写`audit.md`。只有caller明确需JSON才写run内`PROOF_ORCHESTRATOR_AUDIT.json`，**绝不能覆盖paper `PROOF_AUDIT.json`**（L179–201）。

bridge通用default可能是GPT、fallback也可能非DeepSeek；必须从实际返回核DeepSeek身份，错模型/unknown就`DEEPSEEK_REVIEW_BLOCKED`，local fallback标`local-executor-fallback`/`local-codex-fallback`，不算跨家族（reference `deepseek-routing.md`8–36）。其reference L76写了一次fresh retry，但本机AGENTS“ambiguous paid failure不自动重试”及当前调用合同优先；不要把此旧reference变成通用无限/自动retry。raw外部负面CRITICAL/FATAL未解决会阻止`READY_FOR_USER`，需真实修复或用户explicit waiver；只审阅不自动改source proof（主skill L203–210）。这个特殊“不能自行由negative改acceptance”的规则不应抹去Lean协议允许据数学证据reject误读的细节。

两个exposition gate有准确触发和执行步骤。notation在符号请求/theorem-heavy/一步≥5 nonstandard symbols时读reference，保留七行原scorecard：core objects retention、undefined、collision、one-use、parallel representations、alias depth、active symbols。retention100%且undefined/collision0才可ready；其它阈值是可说明理由的编辑warning，不能发明数学降低数值。top-down derivation须target→足以成立的subgoals及理由→逐项证明来源→回到原target，`Top-down derivation structure`不能FAIL（L86–115；notation reference1–56、58–135）。应复用其具体分工，但不要把所有数学研究强制加符号评分仪式。

## 5. proof-checker：审计拥有者、修复循环、失败出口与父工作流交接

### 5.1 进入和准备

输入是LaTeX proof或proof description；Phase0读**完整证明和所依赖原材料**，提取theorem/lemma/proposition/corollary/definition/assumption，做含行号section map，识别main theorem（L165–173）。Phase0.5将原文变成`PROOF_SKELETON.md`：Dependency DAG+cycle detection、at-each-application Assumption Ledger、Typed Symbol Table、精确quantified statement、非平凡micro-claims及side-condition位置、Limit-Order Map（L228–270）。这里的source-location receipt并不证明数学真。

可并行的是**抽取**：先冻结source unit IDs，source-order分片≤8，wave concurrency≤4、每leaf≤8turn；Claude使用`aris-fanout-leaf`，无leaf则同批顺序处理；失败/畸形/timeout最多一次executor sequential fallback，不能不断换worker。schema为`{shard_id,assigned_unit_ids,covered_unit_ids,status,entries,errors}`，obligation IDs在抽取后从source anchor派生。先reconcile coverage receipt，只有100% source execution coverage才算全局DAG/symbol/cycle；漏unit则INCOMPLETE/BLOCKED。**source execution complete不证明义务发现完整，更不证明proof valid**（L175–226）。

只有具体需求才嵌`lean-formalize`：给该义务及原假设，取checked scope/exported declaration/alignment/build/transitive axioms，**然后resume原audit**。canonical acceptance/wiki产物仍归checker；嵌套Lean不得再启动checker（L272–282）。

### 5.2 真实循环

Phase1把完整数学给resolved reviewer，mandatory checks包括definition、每次application的hypothesis discharge、inequality、analysis interchange、probability mode、uniformity/constants、key-lemma counterexample、dependency consistency；返回structured issue包含id/status/impact/category/location/claim/problem/counterexample/downstream/minimal_fix。保存reviewer handle与raw结果，写`PROOF_AUDIT.md`（L284–395）。

Phase1.5不是再投票：对CRITICAL/MAJOR和新关键inequality/identifiability/curvature/uniformity/convergence升级lemma尝试具体反例，包括low-dim/degenerate/extremal distribution/scaling/numeric falsification。只有代数验证后称found，否则candidate；所有尝试入audit（L397–418）。

Phase2依severity修：明确选择`ADD_DERIVATION`/`STRENGTHEN_ASSUMPTION`/`WEAKEN_CLAIM`/`ADD_REFERENCE`→完整数学推导→实现`.tex`保留label→登记before/why/after/key equation/new obligations/downstream→compile。statement-changing选择必须显式记录并传播到main theorem，不能用“修好”隐藏原目标改变（L420–462）。

Phase3 re-review→未过再Phase2/3，`MAX_REVIEW_ROUNDS=3`。**主线重用Phase1的threadId和reply，Codex mirror每轮fresh agent，见§8。** 不可把两者混成一个惯例。

Phase3.5整体验statement–conclusion、全部义务、完整case partition、induction、WLOG losslessness、假设增量。曾修FATAL/CRITICAL的section独立fresh blind reviewer，只给fixed section不带旧critique；新issue再回Phase2。重跑DAG、modified lemma全部downstream counterexamples、assumption delta（L470–509）。

三轮仍不过，Phase3.9交Proof Unrecoverable Report：minimal blocking issues、ranked salvage（weaken/add assumption/missing lemmas/restructure）、可复用部分及下一步。**不是自动改题成功，也不是要求整个数学Goal永远停下**（L557–565）。Phase4产`proof_audit_report.tex/.pdf`，Phase5写`PROOF_CHECK_STATE.json`（rounds、handle、fixed counts、counterexamples、acceptance、timestamp；L567–597）。

### 5.3 成功的数学条件、总控消费和wiki

Acceptance gate四条件：0 open FATAL/CRITICAL；每theorem/lemma假设与proof/interchanges齐且每次应用discharged；all asymptotics声明依赖/一致性；所有key lemmas反例pass执行（L67–74）。verdict细分：no theorem→NOT_APPLICABLE；source unreadable→BLOCKED；all obligations→PASS；minor→WARN；fatal/critical→FAIL；review failure→ERROR；MAJOR由reviewer明确理由判WARN/FAIL（L867–879）。这不是“收到PASS字符串就定理真”的规则，且review independence/acceptance metadata与verdict是两个轴。

无论有无theorem、成功或失败，都在paper-dir写`PROOF_AUDIT.json`；无theorem不能silent skip。声明input hashes、trace与handle等依assurance合同保存；hash是现有submission verifier的freshness接口，不是给MathRSI添加一套新指纹框架的理由（L746–782、854–865）。`PROOF_AUDIT.{md,json}`是canonical，默认末尾调用`render-html "PROOF_AUDIT.md" --json "PROOF_AUDIT.json"`但render failure **不使audit无效**（L733–744）。

子audit **always emit, never block parent itself**；parent `paper-writing` Phase6与`verify_paper_audits.sh`按assurance决定是否finalize。submission下FAIL/BLOCKED/ERROR/STALE/missing artifact阻止final report；same-family green可exit0但overall provisional，不能呈作submission-ready yes（assurance reference63–91、173–213）。普通数学任务应消费证明缺口和具体证据，不能凭此paper专用父gate强加会场、投稿、PDF报告要求。

active `research-wiki/`才Phase5.5，checker是claim node的出生点；top-level theorem/headline从audit映射：PASS/no flagged imports→verified；闭合但flagged imports→sound-modulo-imports；verified counterexample/statement false→refuted；gap而无反例→unproven。用canonical helper `add_claim --slug ... --status ... --provenance <trace> --statement ... --scope ... --evidence ... --update-on-exist`，wiki失败warn-and-skip不改变audit。不能让writer、derivation或experiment自己生verified theorem；普通gap也不叫refuted（L599–663）。

### 5.4 可选模式和恢复不能补写成原文没有的能力

主线`--deep-fix`是opt-in，在Phase1原prompt上**追加**repair-grade corrected statement、equation before/after、downstream labels、anchored patch、closure tests；某些operator/Schur等步骤另algebra sanity。JSON只增sibling advisory fields，不改issues/verdict；plan malformed不影响可恢复的正常review（L331–386、665–695、784–823）。

主线`--restatement-check`也是opt-in，严格位于3.5与3.9之间；全tex收canonical labeled theorem，扫描ref/table/contribution/abstract paraphrases，比较conditional/scope/quantifier/envelope/constant/rename。它不自动改文、独立输出`details.restatement_drift`，不能自动改变verdict；CRITICAL且实际被下游误用时reviewer可另写regular issue；缺canonical/parse不可用非blocking（L511–555、825–852）。Codex mirror缺这两mode，不能宣称已支持。

有recovery state但主skill没有像orchestrator那样详细的“中断后先读哪些文件、恢复哪一phase”算法。可确知的是主线单次调用Phase1→3保持handle；**另一次top-level invocation必须fresh thread**，旧audit不能替代原始输入；FATAL/CRITICAL blind另fresh（L881–885）。MathRSI若要更强跨turn恢复必须明确继承、或新增自己的caller适配，不能说ARIS原文已经解决所有恢复细节。

## 6. lean-formalize：主张保真、实际连接、形式审计与A/B/C的完整闭环

它接implement/continue/audit/package四种scope；audit只看与报告，不静默修/弱化；implement负责缺失数学而非仅将已知证明转语法，持续至main assembly（L60–80）。起步读authoritative statement、actual Lean entry、toolchain+lockfile、latest progress；reuse project，早报main module/export/next obligation。partial Lean先inspect actual caller和last useful error；completed handoff只核证据/打包，不重开数学（L70–95）。

顺序是original statement+actual definitions→A alignment→obligations/representations/interfaces→implementation↔B关键论证→actual input/main theorem assembly→executed type/definition/transitive axioms→C final exported result→handoff/state update（L36–58）。小routine按比例；continuation复用unchanged checks；指定Grok和Gemini则分别保留，两者缺一不以same-family代替，缺review时继续独立工作但review义务pending。

spec包括objects/domains/quantifiers/hypotheses/conclusion、方便表示equivalence、用户允许的computation/certificates/foundations、目标Lean declarations。原题一直是baseline；working spec改成实现样子不能替换。更强证明可由implication回原题；较弱版本明确原义务仍开（L97–123）。

连接表逐项写declaration/assumes/actual inputs come from/evidence-gap；分别证明formula computes number、actual object realizes formula、computed fact implies conclusion。`Certificate x → Desired x`并不构造任意原input的Certificate。split workers按stable interface+module ownership+compile target，收件必须接actual caller（L125–184）。

implementation loop是选影响main theorem的highest unclosed connection→搜**固定版本**library/project并`#check`→lemma+actual use site→compile changed module与downstream→分first causal error为API/implementation或missing mathematics→必要时换general counting/recurrence/smaller certificate而非偷偷换trust→B→更新原ledger并继续（L155–192）。`lean-working-loop.md`给可实际使用的库检索/完整Finset应用、表示constructor+consumer试验、error→next-action表，区分implementation/decomposition/method三类失败与其不同后继；build queue/download/import/elaboration成本不可混称数学失败（reference7–22、24–69、71–143、145–169）。

有限样本、proved exhaustive domain、checked certificate、general proof分别表明证据范围；end-to-end Lean必须让coverage和interpretation也在proved dependency chain。数值exactness按claim需要，计数顺序/重数/indices/zero/rounding明确。不得把本项目禁native_decide/枚举变成所有数学的普遍禁令（L194–214）。

### A/B/C每步都不是抽象“找模型看看”

* **A trigger**：new theorem/spec或meaning-changing representation；packet actual definitions+target+needed notation，第一轮不泄漏intended prose/prior verdict；收independent backtranslation后才比较原题。mismatch先修表示，数学歧义才据已有授权/必要时问user；可并行unaffected lemmas（adversarial reference68–102）。
* **B trigger**：new load-bearing lemma/reduction/case/computational interpretation/interface；packet proof+assumptions+actual caller+finite data+relevant local change。attack原输入满足条件、coverage和encoding意义；概率仅其适用时检查joint sampling。主执行者验证counterexample、修实际论证/callers、compile后targeted follow-up；不每改tactic调模型（reference104–134）。
* **C trigger**：assembled theorem且local type/axiom audit ready；fresh packet original statement、final definitions/top proof/branch entries、actual build/log、expanded type+axioms、交付prose。trace任意原input回来，区分semantic defect、missing reproduction和exposition。修affected内容、rerun/review，不重审unchanged artifact（reference136–164、180–217）。

真实review transport各自合同不同：file-read reviewer接primary paths；remote prompt-only API须源文而不是它读不到的path；Claude reply重给tools，Grok/Antigravity固定first cwd/session；查看logs不等于执行；plan review不等于final source review。raw回应与disposition分开、可据数学理由reject错误counterexample，不靠数票；provider失败留pending，partial reviewer不装双审完成（reference8–66、166–240）。

### 最后形式验收、交付和恢复

build**实际主模块**，multi-module另independent import actual entry，print definitions、`#check`完整声明和`#print axioms`传递链；小单文件direct compilation+type/axiom足够。不是main默认build成功、target proposition定义存在或`P→P`就完成。无用户未允许的sorryAx/extra axiom，trust按实际foundation说明，不机械要求某固定三公理名单。保留command/exit/output（L284–327；verification reference7–80）。

portable包含sources/pinned config/audit/log/readable proof及重现命令，不带machine toolchain/cache/credential；incremental/import audit/clean rebuild/他人独立reproduction分开说明。reference的`ExampleProof.Main`、Lean4.24.0 named clean、Mathlib cache只是示例/version-specific，不写成general math固定命令（verification reference82–127）。

恢复复用原spec/ledger/continuation，记录Original target/source、current export/module、closed connections/build evidence、next obligation/completion、A/B/C scope/raw/thread、next action。unfinished保留smallest gap/dependencies/last useful error；finished明确completion避免重启旧gap。claim语义/假设变更需alignment+affected review；仅wording/layout保留数学不重做（L329–376）。active wiki通过既有research-wiki/proof-checker接回，**不再造一套claim acceptance格式**。父proof-checker调用时仅return scope+evidence，禁止回调checker；standalone Lean不自动要求paper audit（L224–230）。

## 7. research-wiki：不是“顺便记一下”，而是有出生点与helper的跨技能契约

实体paper/idea/experiment/claim各有canonical ID与目录；关系只在`graph/edges.jsonl`，page Connections为generated view不可手改（L20–42）。`index.md`、`log.md`、`gap_map.md`、`query_pack.md`及四类目录是已有schema（L60–78）。

主线操作前resolve `research_wiki.py`；wiki本身helper缺失hard fail，因为它就是wiki工具；paper/idea等caller的附属capture缺helperwarn-and-skip仍交primary output（L82–119）。init单调创建目录、index/log/gaps/**query_pack**/graph并append log（L121–139；实际helper127–153）。不应覆盖已有wiki重新开始。

ingest是metadata→slug→dedup→page→rebuild index/query→append log；**不自动抽关系**，identified relation需后续`add_edge`。阅读技能直接call同一helper而非额外LLM绕一轮wiki skill。`sync --arxiv-ids`/`--from-file`是explicit missed-input backfill，不扫trace猜读过什么（L141–200）。paper helper先留schema空body，需要实质enrichment另完成，文件出生不等于论文深读。

query压到8000chars，读short fields而非每次重总结所有body；failed ideas/top gaps优先保留。query pack用于复用失败，不代替新题外部查漏。update后rebuild/log；lint交`LINT_REPORT.md`查orphan/stale/contradiction/dead/sparse等；不是发现stale drafted就判数学假（L262–319）。

具体hooks：research-lit synthesis后top8–12 ingest+关系；idea-creator开始读recent pack并仍搜recent work，生成后每个recommended/killed idea用`upsert_idea`，default skip-on-exist不毁此前实验丰富内容；result-to-claim先`add_experiment`出生成功才加supports/invalidates edge，不能把empirical verdict写进claim proof status；proof-checker Phase5.5才生claim（L333–437）。significant updates只**suggest**re-ideation，原技能不自动启动（L439–448），但用户已授权的Goal如何持续探索由上层任务决定。

durable capture先区分研究失败与transient operational failure；可保留真实失败定理条件、原输入、重试理由，不要把429或配置问题写成“模型永远不会某事”。filter通过也不授予定理状态；graph/helper还负有injection hygiene义务（L44–58；capture reference13–49；Codex wiki44–65）。

## 8. 双端实质差异与不可直接继承的矛盾

|位置|主线|Codex版|MathRSI需要采取的动作|
|---|---|---|---|
|checker Phase3|saved thread reply，保留原issue memory（464–468、713、883）|每轮fresh reviewer agent（361–365、489–493、587–593）|按具体host真实skill执行，不抽象成“一律fresh”或“一律continue”|
|checker opt-ins|deep-fix、restatement，完整900行|无对应mode，605行|不能两端统一宣传可用；需要时独立维护adaptation|
|checker failure|verdict table ERROR（876）|顶部“reviewer failure BLOCKED”（24）而table ERROR（582）|报告unavailable/failure真实事实；caller adapter须明确一种schema mapping，不凭这处冲突谎称支持统一恢复|
|review default|Claude host Codex MCP|Codex host fresh native GPT reviewer|actual family决定provisional，不以工具名断言跨模型|
|extraction enforcement|真实leaf限制read-only/no mutation/delegation|stock Codex限制为prompt-only，shared caps仍executor enforce（142–175）|不说两个宿主都有OS/工具硬隔离；implementation workers另合同|
|wiki init|canonical helper，包括query_pack（121–139）|prose manual bootstrap漏query_pack（89–96）|实际helper init才是当前实现；适配可修文档，不能继承遗漏|
|wiki query direction|structured RESEARCH_BRIEF，无field小cap（270）|300chars AGENTS/brief（233）|实际helper225起使用structured brief；明确文档漂移|
|helper lookup|`.aris/tools`→project tools→repo/global pointer|Codex manifest/env repo→project tools→global skill helper|MathRSI本机AGENTS要求绑定**本仓base/tools**，不照抄作者全局fallback|
|orchestrator GPT Pro|可有different-family assistance，仍非canonical acceptance|明确GPT Pro与Codex same-family（Codex L20–24）|assistance与review/acceptance分开，不把换GPT名称作独立性|

其余有用差异：writer实质正文一致，Codex去掉Claude frontmatter工具字段；formula仅去`Skill(lean-formalize)`allowed-tools但正文保留optional Lean，故执行仍读宿主实际能力。Lean A/B/C数学包双端一致，host段明确Codex peer provisional、required跨家族继续pending（Codex260–280）。orchestrator references中deepseek routing补充GPT fallback属same-family警告，dispatch/stress多是executor→Codex措辞，不是新流程。

源`AGENTS.md`要求双端科研流程/产物/验收同步、host调用适配，但本次实际读到的上述差异必须保留为事实，不能拿维护意图覆盖源码。它还明确same-family/provisional、实际模型身份、不自动重试付费调用、owned module分工和HERO。`CONTRIBUTING.md`30–56只要求frontmatter/content、安装后实际本地试用；没有“每个skill最低多少行”的官方标准，也没有要求通用数学默认跑ML科研/venue流水线。

## 9. 对当前 MathRSI 的直接重设计含义

当前main skill已有不错的数学规则：量词、AND/OR、共同对象、exact computation、停滞诊断、真实caller与证据范围。这些可保留为阶段内判断。**缺的主要是技能之间真实接棒，而非再补一页原则。** 当前L75–94的技能表有“给它什么”，但大部分没有明确以哪个产物/状态选择下一个调用；L143–173把Lean和review再概括一遍，却没有接入完整A/B/C、checker canonical产物与wiki owner；L176–191装配交付没有展示审计失败如何回流、claim何时能持久化。

重设计主线应从实际阶段写起：初步问题/文献发现→正式问题与已知依赖→未稳定公式对象走derivation，确定claim走writer→计算/归约/结构引理各有真实caller并取证→整卷proof-checker（或任务明确允许的相应数学验收）→根据具体issue返回writer/derivation/领域implementation，重核affected descendants→需要的Lean可早进并行、最后按实际type/axioms/C收口→wiki与handoff。这是从原文合同提炼的**设计建议**；未稳定目标的文献前段需Root另一阅读报告补全，不由这六skill凭空生成。

每次条件交接应写清：当前什么已成立、读取哪一份源文、调用哪个完整skill、明确target output path、完成后Root读哪个artifact与checked scope、失败后哪个数学义务仍开。不要仅“按需调用proof-writer/review”。例如：

1. derivation的`COHERENT AS STATED`只说明理论线可用；取其exact propositions与假设，再把尚未证明的命题交writer；reframe则先对照原目标，blocker则回到对象/假设研究。
2. writer交回complete theorem需查actual caller再关闭该义务；corrected claim不关闭原题，blocker用于选下一数学动作。Lean返回单lemma时不直接进入“正式全证完成”。
3. 整卷checker有FAIL时消费exact blocking issue和downstream，不把失败写成数学Goal不可解；有ERROR时保留review pending并推进独立工作；有PASS还要核实际scope/identity与requested review完成，而不是另开无穷review。
4. 所有义务闭合、arbitrary input→conclusion与所需核验成立后，才进入完成交接。wiki claim出生沿checker既有接口；不让主skill直接“每次实质结果add verified claim”。未到完整验收的局部成果可以进入适当研究记录，保持条件状态。

需要复用的是这些**分工、artifact ownership、分支和回流**；不宜通用化的包括固定GPT/DeepSeek型号、所有步骤ultra、统一三轮/8shard/4并发、paper-dir/LaTeX/venue、所有数学强制Lean或HTML、把finitary概率清单当所有数学清单、manual GPT Pro每run审批套到已授权常规review、为普通handoff重造hash框架。若真实调用原skill，保留它自己适用的limits与artifact；若MathRSI另作适配，明确是什么适配并检验实际运行，不能一边声称继承完整ARIS一边跳过其合同。

本报告未修改任何技能，也未通过实际研究运行证明上述建议有效。下一步应由Root把完整多技能workflow写成可以从一个阶段接到下一阶段的执行文本，复用已有rules/reference作为阶段内支撑，再以具体完整案例核验交接与恢复。

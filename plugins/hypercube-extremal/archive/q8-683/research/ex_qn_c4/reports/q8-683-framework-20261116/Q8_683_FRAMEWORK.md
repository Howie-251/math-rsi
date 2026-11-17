<section class="hero" id="overview">
<div>
<div class="eyebrow">MATHRSI × 上下界协同</div>
<h1>让构造与证明<br><em>互相推进。</em></h1>
<p class="lead">用大模型生成构造程序，用局部指标连接图与不等式，再把上界侧的发现变成下一轮搜索的奖励。MathRSI 将这条反馈回路组织成可恢复、可核验的数学研究。</p>
<div class="tags"><span class="tag">共享指标</span><span class="tag">近极值探索</span><span class="tag">精确证书</span><span class="tag">持续知识复用</span></div>
</div>
<div class="interval" aria-label="当前已知下界682，本次上界683，主目标上界682仍开放">
<div class="eyebrow">本次结果 · 计算辅助证明</div>
<div class="range"><strong>682</strong><span class="middle">≤ ex(Q₈, C₄) ≤</span><strong>683</strong></div>
<div class="range-labels"><span>已有合法构造</span><span>本次证明的上界</span></div>
<div class="rule" aria-hidden="true"></div>
<div class="range-labels"><span>下界侧提供见证</span><span>上界侧排除所有 ≥684</span></div>
<div class="status"><span class="status-dot"></span>主目标仍为 <b>ex(Q₈, C₄) ≤ 682</b>，尚未闭合。<br>当前证明已通过内部计算核验与非作者全文审查；审查保障为同模型家族、暂定验收。</div>
</div>
</section>

<div class="question-strip"><b>研究的是什么？</b><p>Q₈ 的顶点是 256 个八位二进制串，相差一位的顶点相连，共 1,024 条边。我们要尽可能多地保留边，同时不出现四边形环 C₄。ex(Q₈, C₄) 表示最多能保留的边数。</p></div>

<nav class="toc" aria-label="页面章节"><ol><li><a href="#mathrsi">01 · MathRSI 外层流程</a></li><li><a href="#coevolution">02 · 上下界协同</a></li><li><a href="#reward">03 · 奖励与近极值</a></li><li><a href="#certificate">04 · 从发现到证明</a></li><li><a href="#result">05 · 683 的关键结果</a></li><li><a href="#review">06 · 审查与证据</a></li></ol></nav>

<section id="mathrsi">
<h2>01 · MathRSI：组织完整研究</h2>
<p class="section-intro">MathRSI 以 ARIS 的推导、写作、文献、审阅与知识库能力为基础，组织五组数学研究流程。面对 Q₈ 的无四环问题，领域适配提供超立方体的局部面、共同补全、覆盖论证和检查器；主流程负责把各项产物接回同一个原目标。</p>
<figure class="figure-box">
<div class="figure-heading"><b>外层 / RESEARCH WORKFLOW</b><span>按当前断点进入；每一步都读回实际产物。</span></div>
<div class="workflow">
<article class="stage"><div class="step">01 / PREPARE</div><h3>问题与知识</h3><p>澄清量词、恢复已有成果，核对文献与可用引理。</p><div class="wiki-action">读：目标、原件与旧结论<br>写：精确条件、进口与缺口</div></article>
<article class="stage"><div class="step">02 / ROUTE</div><h3>路线迭代</h3><p>提出方法，审阅质疑，用数学探针决定如何修订。</p><div class="wiki-action">读：失败路线与反例<br>写：路线判断、适用范围</div></article>
<article class="stage"><div class="step">03 / PROVE</div><h3>证明推进</h3><p>推导、构造、计算与多 agent 分工，回收可用结果。</p><div class="wiki-action">读：已证引理与未闭义务<br>写：新事实、见证与障碍</div></article>
<article class="stage"><div class="step">04 / VERIFY</div><h3>装配与核验</h3><p>接通完整论证，检查覆盖、算术与原题条件。</p><div class="wiki-action">读：证明及实际证据<br>写：审查结论与准确范围</div></article>
<article class="stage"><div class="step">05 / HANDOFF</div><h3>交付与恢复</h3><p>整理可读结果、复现入口和下一次工作的断点。</p><div class="wiki-action">读：当前严格结论<br>写：导航、证据链与下一步</div></article>
</div>
<div class="wiki-rail"><b>Research wiki ↔</b><p>导航定位 → 阅读实体及原证据 → 形成新事实 → 增量写回 → 后继任务实际使用。旧失败也保留其条件，避免重复探索已经排除的范围。</p></div>
<p class="reflow">回流：局部证明缺口 → 证明推进；关键路线失效 → 路线迭代；新的文献疑问 → 定点调查。已有完整候选可直接进入核验。</p>
<figcaption>本次任务先读取原有 682 边构造和局部修补障碍，再开展协同研究；683 上界随后以 claim 实体写入当前任务 wiki，供继续排除 683 边时使用。</figcaption>
</figure>
<div class="two-col">
<article class="note-card"><h3>协作角色有具体交付</h3><p>主代理维护原目标和共同数学连接；作者 agent 交出引理、程序或证书；非作者审阅者检查完整声明与证据。成熟结果立即接入后续义务。</p></article>
<article class="note-card"><h3>审阅与框架演进各有位置</h3><p>MathRSI 支持跨模型对抗审阅；本次 683 定理的已完成审查属于同模型家族。meta-evolve 是独立维护流程，用研究经验改善框架，不作为第六个解题阶段。</p></article>
</div>
</section>

<section id="coevolution">
<h2>02 · 上下界协同：让两端共用一套指标</h2>
<p class="section-intro">这一协同方案由用户提出：维护关键中间变量集合；下界侧借鉴程序进化思想，让大模型生成搜索程序；上界侧分析图簇、提出局部不等式；不等式再转成构造侧的 reward。每一轮消费上一轮的真实图、程序、反例和评价。</p>
<figure class="figure-box">
<div class="figure-heading"><b>内层 / CO-EVOLUTION LOOP</b><span>在 MathRSI 的路线迭代与证明推进中运行。</span></div>
<div class="flow-desktop">
<svg class="flow-graphic" viewBox="0 0 1000 485" role="img" aria-labelledby="loop-title loop-desc">
<title id="loop-title">共享局部指标驱动的上下界协同</title>
<desc id="loop-desc">下界侧生成程序，经宿主检查后把图簇和统计送给上界侧。上界侧提出有条件的不等式，经反例检验后将残差反馈为下一轮奖励。两端共用精确定义的局部指标；待证义务另外进入完整证明与核验。</desc>
<defs><marker id="arrow-teal" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#166a5a"/></marker><marker id="arrow-orange" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#ad4b26"/></marker><marker id="arrow-gray" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#7b9185"/></marker></defs>
<rect x="213" y="4" width="574" height="76" rx="13" fill="#e9eee6" stroke="#ccd8cc"/>
<text x="500" y="35" text-anchor="middle" class="node-title" fill="#1c302f">共享局部指标 φ(G)</text>
<text x="500" y="60" text-anchor="middle" class="body" fill="#526562">边数 · 度数 · 方形状态 · 子面统计 · 精确适用条件</text>
<path d="M260 80 V113 H175 V143" fill="none" stroke="#7b9185" stroke-width="2" marker-end="url(#arrow-gray)"/>
<path d="M740 80 V113 H825 V143" fill="none" stroke="#7b9185" stroke-width="2" marker-end="url(#arrow-gray)"/>
<rect x="8" y="150" width="333" height="164" rx="14" fill="#fff0e5" stroke="#dbbba5"/>
<text x="31" y="183" class="label" fill="#ad4b26">LOWER / 构造侧</text>
<text x="31" y="217" class="node-title" fill="#7f3b21">大模型生成并修改程序</text>
<text x="31" y="246" class="body" fill="#526562">搜索、重构、交换 → 提交候选边表</text>
<text x="31" y="274" class="body" fill="#526562">在近极值图附近探索新的结构</text>
<text x="31" y="299" class="label" fill="#ad4b26">保留程序、父图、失败与评价</text>
<rect x="659" y="150" width="333" height="164" rx="14" fill="#e7f1eb" stroke="#b7d1bf"/>
<text x="682" y="183" class="label" fill="#166a5a">UPPER / 上界侧</text>
<text x="682" y="217" class="node-title" fill="#166a5a">分析图簇，提出不等式</text>
<text x="682" y="246" class="body" fill="#526562">结合指标、反例与已有局部引理</text>
<text x="682" y="274" class="body" fill="#526562">记录适用域，导出待证义务</text>
<text x="682" y="299" class="label" fill="#166a5a">候选 → 反驳 / 保留 / 送交证明</text>
<path d="M341 197 H651" fill="none" stroke="#ad4b26" stroke-width="2.5" marker-end="url(#arrow-orange)"/>
<text x="500" y="171" text-anchor="middle" class="body" fill="#ad4b26">已核验图簇与精确统计</text>
<text x="500" y="222" text-anchor="middle" class="label" fill="#526562">宿主独立检查合法性与 C₄</text>
<path d="M659 282 H349" fill="none" stroke="#166a5a" stroke-width="2.5" marker-end="url(#arrow-teal)"/>
<text x="500" y="260" text-anchor="middle" class="body" fill="#166a5a">不等式残差 → 下一轮奖励</text>
<text x="500" y="306" text-anchor="middle" class="label" fill="#526562">全部档案反驳；移除失效候选</text>
<path d="M175 314 V345 H825 V314" fill="none" stroke="#7b9185" stroke-width="1.5"/>
<text x="500" y="371" text-anchor="middle" class="label" fill="#526562">共同档案：图 / 程序 / 指标 / 条件 / 反例 / 奖励版本</text>
<path d="M825 345 V399" fill="none" stroke="#166a5a" stroke-width="2" marker-end="url(#arrow-teal)"/>
<rect x="213" y="407" width="779" height="65" rx="12" fill="#1c302f"/>
<text x="600" y="435" text-anchor="middle" class="body" fill="#f3f7f1">进入严格证明：共同对象约束 → 精确证书 → 完整覆盖 → 独立核验</text>
<text x="600" y="458" text-anchor="middle" class="label" fill="#c5d5ce">研究代理将发现接回原题；样本检验阶段保留“待证”状态</text>
</svg>
</div>
<div class="flow-mobile">
<div class="mobile-node"><h3>共享局部指标 φ(G)</h3><p>两端共用边数、度数、方形状态、子面统计及精确条件。</p></div>
<div class="mobile-arrow">↓ 定义统一的评价对象</div>
<div class="mobile-node orange"><h3>下界侧：大模型生成程序</h3><p>搜索、重构、交换，提交候选边表；宿主独立检查图与 C₄，计算精确指标。</p></div>
<div class="mobile-arrow">↓ 已核验图簇与统计</div>
<div class="mobile-node green"><h3>上界侧：提出不等式</h3><p>分析图簇，明确适用域；在全部档案中寻找反例。保留的残差成为下一轮构造奖励。</p></div>
<div class="mobile-arrow">↺ 不等式残差 → 奖励 → 回到构造侧</div>
<div class="mobile-node"><h3>待证义务进入 MathRSI 核验</h3><p>共同对象约束、精确证书、完整覆盖和独立核验，将候选接回原题。</p></div>
</div>
<figcaption>协同是信息与目标的反馈关系，不要求两端同时执行。当前闭环每轮分别调用构造侧与上界侧；新增指标后对旧图重新计算，下一轮奖励在轮初冻结。</figcaption>
</figure>
<div class="three-col">
<article class="metric-card orange"><div class="micro">CONSTRUCTION</div><h3>下界侧的交付是图</h3><p>合法的 682 边图支撑下界；若找到合法的 683 边图，经独立核验便会反驳目标上界 682。生成程序声称的分数由宿主重算。</p></article>
<article class="metric-card green"><div class="micro">INEQUALITY</div><h3>上界侧的交付是义务</h3><p>候选包含系数、右端与适用条件。有限样本支持后，继续寻找结构证明、完整有限排除或可重放证书。</p></article>
<article class="metric-card blue"><div class="micro">SHARED LANGUAGE</div><h3>指标连接两种工作</h3><p>构造暴露上界遗漏的局部形态；上界指出下一批构造应挑战的结构关系。指标扩展后，历史图也参与重新评价。</p></article>
</div>
<p class="accent-rule">当前工程闭环已经支持程序生成、图核验、候选检验与奖励反馈。683 定理由随后推进的共同约束与精确证书路线完成；这里展示二者如何衔接，不把定理归因于单独运行一次搜索循环，也不据此宣称效率提升已被对照实验验证。</p>
</section>

<section id="reward">
<h2>03 · 奖励设计：在接近极值的地方获得信息</h2>
<p class="section-intro">用户指出，646–648 边的图虽然合法，却离 682 太远，难以区分紧上界。研究因此引入近极值工作带，同时保留全档案反驳：发现数据集中于高边数区域，低边数的真实反例仍可推翻不等式。</p>
<div class="band">
<div><h3>以 680–682 边为主要探索区域</h3><p>启动时保留四张已有 682 边种子，以及通过删去一、两条边得到的 24 张校准样本。主体亲本与上界发现优先工作带；搜索内部允许先损失更多边，再重构回来。680 是可调启发式阈值。</p></div>
<div class="band-visual"><div class="band-title">近极值工作带 → 对抗搜索阈值</div><div class="edge-values"><b>680</b><b>681</b><b>682</b><b class="target">683</b></div><div class="edge-label"><span>校准、结构多样性、精英保留</span><span>待寻找 / 待排除</span></div></div>
</div>
<div class="reward-panel">
<div><h3>尚未违反，也提供方向信号</h3><p>对适用的候选 a·φ(G) ≤ b，使用有符号残差，并按系数和档案中的分散程度归一化：</p><div class="formula">r(G) = a·φ(G) − b<br>z(G) = r(G) / max(‖a‖₁, IQR(r))</div><p class="reward-caption">残差由 −5 改进到 −1，已经说明更接近约束边界；正残差表示找到了该候选的反例。</p></div>
<div><div class="eyebrow">示意 · 同一候选的残差</div><div class="residual-track"><span>−5</span><i>→</i><span class="close">−1</span><i>→</i><span>0</span><i>→</i><span class="violate">+1</span></div><p>挑战通道轮换不同候选，避免一条总是取等号的边数约束掩盖其它结构。近极值带内使用有界残差和新颖性，带外优先惩罚边数缺口。</p><p class="reward-caption">在适用条件内的真实反例仍优先保留；被反驳候选退出后续奖励。</p></div>
</div>
<div class="channel-grid"><div class="channel"><b>目标通道</b>推动边数接近或达到对抗阈值。</div><div class="channel"><b>挑战通道</b>逼近、检验一条具体不等式。</div><div class="channel"><b>新颖性通道</b>保留指标空间中不同的结构区域。</div><div class="channel"><b>条件通道</b>探索指定局部条件及其可行性。</div></div>
<details>
<summary>条件目标怎样回到无条件上界？</summary>
<div class="details-body"><p>框架允许研究有条件的构造或不等式，例如某个最小度约束。每条候选条件独立记录；只有满足条件的图才参与其反驳。若要据此证明无条件上界，就必须证明每个潜在反例均满足条件，或把剩余分支全部覆盖。</p><p>近极值阈值只改变样本和亲本的优先级。即使发现阶段主要看高边数图，候选仍在全部归档图上检验；不会把探索偏好偷偷变成原定理的假设。</p></div>
</details>
</section>

<section id="certificate">
<h2>04 · 从协同发现，走到可核验的证明</h2>
<p class="section-intro">最终上界使用固定维数的局部矩方法、整数约束和精确 LP 对偶证书。关键推进是把多个统计量接到同一个假想反例 H 上，证明它们必须同时满足的关系，再用一个有限的矛盾证书排除整个反例范围。</p>
<div class="bridge">
<article class="bridge-item"><div class="n">A / 假想反例</div><h3>归约对象</h3><p>把至少 684 边的图添边为极大无 C₄ 图；Q₆ 局部引理把边数限制在 684–688。</p></article>
<article class="bridge-item"><div class="n">B / 共同统计</div><h3>连接同一个 H</h3><p>H 的 Q₄ 面、奇偶侧度数和环境边邻域，满足精确双重计数与抽样恒等式。</p></article>
<article class="bridge-item"><div class="n">C / 证书发现</div><h3>组合有效约束</h3><p>将平方非负、整数性及结构约束组合。数值优化寻找权重，再转为精确有理数。</p></article>
<article class="bridge-item"><div class="n">D / 全域核验</div><h3>完成严格排除</h3><p>完整局部域最大化，加上严格舍入误差界，得到正矛盾余量；独立重建并审查。</p></article>
</div>
<div class="quote"><p>来自同一张图的局部统计必须相容。<br><strong>这一共同约束，把“看起来成立的相关性”接到了全称上界。</strong></p></div>
<div class="two-col"><article class="note-card"><h3>程序搜索承担发现</h3><p>图簇用于提出和挑战关系，局部列库用于寻找有效证书。候选在样本上未被推翻时，仍保留其待证状态。</p></article><article class="note-card"><h3>覆盖论证承担全称性</h3><p>最终 Q₄ 最大化独立于发现时的样本库，覆盖全部合法局部图；前置 Q₆ 引理使用结构论证及可检查的 SAT 不可满足证书。</p></article></div>
</section>

<section id="result">
<h2>05 · 683 上界：保留关键中间值</h2>
<p class="section-intro">本次定理覆盖 Q₈ 的所有无 C₄ 边子图。原图可以有孤立点；证明内部先取极大扩张，再使用相应结构条件。下表记录证书的主要尺度与数学作用，完整证明另附入口。</p>
<div class="result-lead"><div class="result-number">683</div><div><h3>每个无 C₄ 的 Q₈ 子图至多有 683 条边</h3><p>已排除所有至少 684 边的情形；恰好 683 边尚未排除。</p></div></div>
<div class="table-wrap"><table><thead><tr><th>证书环节</th><th>关键值</th><th>说明</th></tr></thead><tbody>
<tr><td>极大反例的边数</td><td>684–688</td><td>由局部引理与全局计数得到的必要范围。</td></tr>
<tr><td>度数分布覆盖</td><td>645</td><td>必要整数分布；不声称每个分布都能实现为图。</td></tr>
<tr><td>同一 H 的局部统计</td><td>1,120 / 1,024</td><td>全部坐标 Q₄ 面 / 全部环境边，分别取实际统计。</td></tr>
<tr><td>边邻域状态类别</td><td>1,751</td><td>按同一端点反转作用归并的完整允许直方图域。</td></tr>
<tr><td>共同一致性等式</td><td>356</td><td>连接局部面、度数与边邻域。</td></tr>
<tr><td>证书使用的有效约束</td><td>83</td><td>19 条平方非负 + 49 条整数约束 + 15 条其它有效约束。</td></tr>
<tr><td>完整 Q₄ 最大化</td><td>13,150,453</td><td>独立程序检查的带标记补全数；覆盖另有数学论证。</td></tr>
<tr><td>整数查询的最大值</td><td>−37,440</td><td>对应归一化值 −13 / 22,400,000,000。</td></tr>
</tbody></table></div>
<div class="exact-margin"><b>最终证书的严格矛盾余量</b><div class="math-line">δ − U = 782808475930428709 / 4209067950080000000000 &gt; 0</div><span>这里 δ 是有效约束组合给出的下限，U 是完整局部最大化与误差控制给出的上限。使用精确分数判断正性。</span></div>
<p class="result-foot">前置 Q₆ 引理的 25 份有限输入完成了覆盖重建及严格 RUP 轨迹检查，共核验 4,383,882 次添加。SAT 在这一局部证明环节提供可检查证据。</p>
</section>

<section id="review">
<h2>06 · 审查到哪里，后续继续做什么</h2>
<div class="review-grid">
<article class="review-card"><div class="badge">COMPUTATION / 已完成</div><h3>独立计算核验</h3><p>独立重建精确系数和共同等式，核查有限计数约束，并完成覆盖全部合法 Q₄ 的独立最大化。输入、代码和证书通过哈希绑定。</p></article>
<article class="review-card"><div class="badge">PROOF REVIEW / PASS</div><h3>非作者全文审查</h3><p>审阅者检查完整原图归约、前置引理、覆盖、归一化、83 条约束及最终矛盾，报告无未解决数学问题。未重复运行全部已核验的大规模计算。</p></article>
<article class="review-card limit"><div class="badge">ASSURANCE / 暂定验收</div><h3>准确的审查范围</h3><p>当前为同模型家族的独立 agent 审查与普通精确程序核验。尚无本定理的跨模型家族验收或 Lean 内核形式化；主目标上界 682 继续开放。</p></article>
</div>
<div class="next"><b>下一步：排除恰好 683 边。</b><p>继续强化同一个假想反例上的共同邻域、整数计数和覆盖约束；构造侧寻找接近边界的新结构与潜在反例。任何 683 边合法图都必须独立核验，并据实更新目标判断。</p></div>
<details>
<summary>证据与实现入口 · 本地工作区文件</summary>
<div class="details-body"><p>本 HTML 的正文、图示和样式均可单文件离线阅读。以下链接供在原工作区核对证据；单独转发 HTML 时，不会自动附带这些证明及代码。快照依据 2026-11-16 的已冻结 Theorem B 与审查记录。</p>
<div class="evidence-grid">
<article class="evidence-item"><a href="../../../../math-rsi/docs/WORKFLOWS.md">MathRSI 五阶段工作流</a><p>职责、实际产物消费、wiki 读写和回流。</p></article>
<article class="evidence-item"><a href="../../coevolve/README.md">双端协同框架说明</a><p>程序生成、指标注册、条件、奖励与断点恢复。</p></article>
<article class="evidence-item"><a href="../../coevolve/launches/near-extremal-20261115/TASK.md">近极值研究任务</a><p>已有成果复用、680 工作带与 682 主目标。</p></article>
<article class="evidence-item"><a href="../../coevolve/launches/near-extremal-20261115/finite8_degree_augmentation/pool_B684plus_enriched8/B684_EXCLUSION.md">683 上界完整证明</a><p>Theorem B、共同统计、精确证书及重放入口。</p></article>
<article class="evidence-item"><a href="../../coevolve/launches/near-extremal-20261115/finite8_degree_augmentation/pool_B684plus_enriched8/PROOF_AUDIT.md">非作者审查原文</a><p>实际检查范围、证据复用和同家族暂定保障。</p></article>
<article class="evidence-item"><a href="../../research-wiki/claims/q8-c4-upper683.md">已写回的 wiki 结论</a><p>上界 683 的声明、准确范围和证据链。</p></article>
</div>
<p class="small">证明文件 SHA256：<code>fe281f42382f0be418e1d1631b5334ddb569efcd5943a1e77dbe3007d7cee541</code><br>本页是框架与阶段性结果的说明，不作公开文献最优性、首创性或通用提速声明。</p></div>
</details>
</section>

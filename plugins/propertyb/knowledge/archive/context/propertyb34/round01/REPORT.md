# T34 round01持续研究

**2026-10-13 18:00 UTC，最后30分钟收卷。** 用户限定本轮截止18:06:37 UTC（北京02:06:37）；保存后暂停，不自动延长。新增21点唯一七度和至少五七度两个完整实际分支已Lean通过，接入Assembly并完成两份裸Finset/Bool独立导入，8项公理查询均标准三项。剩余精确为21点最小度7、恰有2/3/4个七度点，以及22–25完整染色。23点3→4实际分类与80项严格排除也已通过，保留22+19残型。T34 Main仍未完成，已验收下界仍为m(5)≥34。详细收卷见`context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md`，21点续接见同轮`twentyone-lean/DEGREE_SEVEN_CONTINUATION.md`。

2026-10-13 17:07 UTC阶段快照。长期Goal active；全部纸面分支齐备，完整Lean和验收未完成。

## 完整候选与形式状态

最新全链入口：[PAPER_CANDIDATE_MAP.md](PAPER_CANDIDATE_MAP.md)。

|点数|纸面候选|Lean|
|---|---|---|
|≤20|全支|实际原题已构建并独立审计|
|21|全支，twentyone-math/COMPLETE_TWENTYONE.md|δ5/δ6/δ8已完整；仅δ7在途|
|22|全支，middle-math/COMPLETE_TWENTYTWO.md|强共度真实排除已验；完整分类/染色待|
|23|全支，twentythree-seven-math/N23_COMPLETE_DISPATCHER.md|无低实际六锁选择/等号追加点已验；局部表和染色装配待|
|24|全支，high-math/CANDIDATE_TWENTYFOUR_COMPLETE.md|实际八匹配选锁已通过；完整分类与染色待|
|25|全支，high-math/CANDIDATE_TWENTYFIVE.md|三类实际单位锁选择已通过；局部分类与染色待|

23最后候选机制：无六度时最小六点加权交换，选点饱和提供实际八度外点；恰一低时common-unit七度集合至少10点，而所有五子集残型迫其分成至多三个至多三点团；恰二低实际五七度扩张唯一型1741/2002；恰三低实际U≥8且含至少两七度，四高完整域最终10型全严格。四/五低与至少六低论证分别在middle-math两篇候选稿。全部局部类型覆盖基于实际迹提升/投影，不是整图枚举。

24完整八匹配选择和目录已结合。重要细节：4912次七锁promotion有56次临时empty<0，恢复低度后救回207必要轨道，均实际保留，见SEVEN_TEMPORARY_NEGATIVE_AUDIT.json。必须在降回真实度数后才筛负值，正文已明确。数字表无需改动。

21δ5指定Assembly1068 jobs与裸Finite条件导入通过，标准三公理。ordinary avoided-quota共享坏向量混合布局已具备actual-H PropertyB接口，五个困难67888真实数字caller已通过构建/独立审计；最终证书只用ordinary quota，weighted诊断不在本次形式化依赖中。主定理尚未导出。

ARIS proof-checker全新上下文R1已完成，零实质问题、一项过时依赖说明已纠正：paper-audit/PROOF_AUDIT.md。Grok/Gemini具体审阅及失败/纠正分别记录reviews/REVIEW_DISPOSITION.md；Gemini新会话已恢复有效SUCCESS。模型没重算大表或执行Lean，不以认可代替证明。

最新正式增量：21δ6全部实际分流已闭合，`TwentyOneSix.propertyB_of_degree_six`无profile额外前提；Assembly1153 jobs与SixAudit四项标准三公理均通过。23三模块与SelectionAudit通过八项标准三公理；用选点权重饱和省去全局两K7正式依赖，具体见twentythree-seven-math/SELECTION_FORMALIZATION.md。MixedLayout实际源码B审阅已由Grok/Gemini有效完成；Gemini首次网络ERROR保留，retry1成功。

最新增量：21δ8已完整接实际H，更新Assembly1183 jobs和EightAudit四项标准三公理通过；21仅余δ7。通用`LockRelabel`支持21四锁356纯/24联合→31/1代表，完整15552参数域coverage已验。24`exists_eight_matching_vertices`已构建，953 jobs、标准三公理；22/23强共度代表、完整coverage与实际调用均已构建，各1023 jobs标准三公理；23条件五点残图→全局九点界也通过。证据见`middle-lean/REPORT.md`和`twentyone-lean/REPORT.md`。

新增连接：LockProjection r18、LockExtension r19、TwentyFiveSelection r19和TwentyOneSevenUnitSet r19均通过，标准三公理。23实际共同单位集合及五高选择r17已通过。容量剪枝BoundedAllocations处于编译修复中；21七度四锁大域改为分块覆盖，完整覆盖尚未通过，不将中止运行记入证据。24实际选择与重标号的新源码B审阅已获Grok/Gemini有效回应，均为静态读取，无Lean执行。

以下保留本轮历史进展；与当前表冲突时以当前表及实际源码/JSON为准。

## 最新增量（以下13:24段落保留为本轮早期状态）

- 20点恰两七度的实际PropertyB theorem已Lean通过，下游Assembly 1040 jobs、裸E原染色和Finite条件装配审计exit0，标准三公理。证据twenty-lean/REPORT.md。唯一七度与δ8尚待。
- 21点δ6全域形成完整候选，见twentyone-math/REPORT.md及三篇分支证明、SIX_UNIT_SET_LEMMA.md。新单布局323+5+404份及5份联合布局证书独立回放；旧61份沿用冻结证据。δ7/8开放。
- 24点恰六个低度点候选闭合：至少四个可选七度点，完整一/二高局部域后，只剩不能同时容纳三高的四种残型，解析矛盾见high-math/CANDIDATE_SIX_LOW.md；SIX_LOW_COVERAGE_AUDIT.json绑定131单高及完整双高。结合七低候选，24尚缺r=1…5。
- 25点得到九单位锁的完整局部块分解分类（不是原超图枚举），概率诊断在途，不能称25已解。
- 新weighted overlap quota只作诊断：22δ6剩余43个三锁输入在该加强后仍无严格界，约0.5秒；见middle-math/WEIGHTED_OVERLAP_QUOTA.md及RESULTS。该结果不排除更多锁或新结构。

## 有效审阅与处置

Grok/Gemini对22δ≥7的实际覆盖链和精确γ/β/δ弱对偶均有效返回、所读范围未发现实质问题；同时审阅21唯一六度且无七度选点。保存reviews/grok_twenty_two_and_six.json及gemini_twenty_two_and_six.json。两者没有重生成大分类；Gemini末尾把第一行24231/24310误作五型最大值，实际最大12152/12155，所有五行仍严格。另Grok对24至少七低新混合完成有效审阅，见grok_seven_low.json。24恰六低、21完整δ6正在提交新审阅，未完成不计认可。

新接口修复：joint_layout_lp接收subset DP返回的原标签positions时必须先排序，再单独置换标签。现在统一排序并断言。旧22数据原位置有序，全部13型独立再次回放无变化；21新五份证书已修后独立验证。各布局有各自的条件失败概率，固定的是H与坏向量；平均上界<1推出某布局的界<1，不称平均仍支配同一个布局的概率。

## 已获新数学成果

- **22点δ≥7完整纸面候选**：第一小时剩13局部迹已全修复。两型用避锁quota；十一型用同一个真实坏向量在有限布局间的联合证书。所有γ/β/δ、容量罚项、34边/锁度输入绑定及独立无放回注入ABC和双向权重都重放通过。见[middle-math/CANDIDATE_TWENTYTWO_SEVEN.md](middle-math/CANDIDATE_TWENTYTWO_SEVEN.md)、THIRTEEN_INDEPENDENT.json。δ=6仍开放，没有新22点Lean。
- **24点至少七个六度点完整纸面候选**：七点原两残型取得44/52布局精确混合，独立注入验证通过；从旧r≥8扩到r≥7。见[high-math/CANDIDATE_SEVEN_LOW.md](high-math/CANDIDATE_SEVEN_LOW.md)。r≤6其余情形及全25仍开放。
- **21点唯一六度且无七度支已得完整候选**：把先导的等号结构接到实际四点共边，完整5型全部严格，独立ABC/dual通过。见[twentyone-math/UNIQUE_SIX_NO_SEVEN.md](twentyone-math/UNIQUE_SIX_NO_SEVEN.md)。多六度的新323见证候选在整理，暂以分工原始报告为准；不计全21完成。

## Lean在途

20点恰两七度的三锁与169四锁完整分类、实际迹恢复和坏对扣除已构建；最终实际选点/容量caller仍在编译。唯一七度与δ8尚待实现。未据中间模块通过宣称全20形式化完成，正式剩余以Assembly实际源码为准。

## 审阅

Gemini已有效返回联合LP表示与固定H后选布局的量词检查，在有限义务内未发现实质问题；原回应reviews/gemini_multi_bad_lp.json。它未审后来生成的十一份证书及完整22点覆盖。其“唯一最优y”用语过强：只需把所有y取各自上界即可达到最优值，不要求最优解唯一。跨中心建议不是已证明新引理，本轮未使用。Grok对24七低新候选仍在途，尚不计认可。

## 新工具与真实纠正

高点代理新增子集DP，以(k,leftMask)同时优化标签和位置；接口核对发现verify错误地把已为原始值的C再加deduction。现按raw C和corrected_C分别检查，全部204份旧winner及5份非零扣除案例已重放，原界未变。详细原始证据在high-math/SUBSET_DP_REPLAY_CORRECTION.json；这项工具修复不改变覆盖义务。

## 接续

root继续22δ6与23；数学代理继续21其余、24少低度/25；唯一Lean执行者继续完整20。使用现有wiki，原T32/T33冻结。

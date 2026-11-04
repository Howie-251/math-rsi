你作为MathRSI研究harness设计顾问，就用户当前的问题给具体建议。只讨论，禁止编辑base/plugins、开发网站、运行研究或巨量验证。使用文件读取工具看真实当前实现与本轮案例底稿；读少而关键的原文件，不全盘扫描。

用户现在问：应该先做base v3和plugins，还是先做宣传网页？v0→v1→v2→v3是否能构成RSI逐步迭代的故事？ECC有两波工作是否应该有两个plugins/两次插件迭代？
用户澄清：ECC后续基于MathRSI v1或v2的研究方法与workflow，即使过程分散也可称流程继承，不要求每步调用固定release；尊重这项作者说明。主数学结果与172双扫在旧阶段已有，新波增加Lean归约/实际矩阵连接、完整便携证书重放、42/16文献路线整合。45/11距离17仍开放。
用户偏好：成果先行、详细可执行Markdown+薄Python；要真实增量修改现有base v2，不另起炉灶；利用已有mathrsi-meta-evolve，不能仅换版本号。不要强制陌生agent重跑、整题重算、复杂指标平台或为宣传做因果实验才能发版。用户尚未授权此轮实施v3或网页，只要我们讨论建议。

当前事实：
v0：独立skills处理Property B和ECC初始研究。
v1：从两题沉淀5个自适应子workflow、Property B插件与ECC草案。
v2：已有meta-evolve并实际吸收DD，DD插件；base已增加公开基线变化对队列的消费、变换后正证据/失败范围分别继承、共同原对象覆盖、纯形式目标直接Lean等。
新素材：Happy Ending（结构补偿、SAT证书与人工纠错），新版ECC，Erdős86（共同完整Q4、同步根群保相对朝向、活动池全域分离、精确Gram认证），Ruskey–Savage Q6（保根极大化；满秩短森林替代巨域枚举；缺秩池转正证书；s2接口修复）。
“RSI故事”要解释具体反馈循环：研究经验→修改方法/插件→下一轮实际使用。不同版本的数学或验证进步都可展示，不要求每个版本必须有新数值纪录；不要虚构历史版本运行、已实施v3、自动提速倍率。

优先读这些（cwd是共同父目录Desktop，所有文件均在其内）：
1. MathRSI/docs/V2_CHANGES.md
2. MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md（入口与实际采用/退出要求）
3. MathRSI/plugins/ecc/skills/mathrsi-ecc/SKILL.md 与 references/source-map.md（没有 plugins/ecc/README.md；请看实际列表）
4. MathRSI/docs/PLUGIN_CONTRACT.md
5. aris4math/mathrsi_new_results/_intake/three-cases-20261104/README.md
6. aris4math/mathrsi_new_results/_intake/three-cases-20261104/ecc/EVOLUTION.md
7. aris4math/mathrsi_new_results/_intake/three-cases-20261104/erdos86/LESSONS.md 与 ruskey-savage/LESSONS.md，按要讨论的具体机制读。
可按需读MathRSI中相关skill段落核查已有能力，引用准确路径。

请独立判断并回答（约1500中文字符，允许简短表格）：
A. 推荐先后顺序，是否可平行做素材/网页方案，什么应等v3实现。
B. v3最小但扎实的完成范围是什么？提出3–5个真正改动而非重复v2已有原则，指出进入base/领域plugin/单题材料的归属。
C. ECC是同一plugin的两代还是两个并列plugin？base版本和插件版本是否需要绑定？给一个可读示例即可，别设计版本管理平台。
D. v0→v1→v2→v3这条研究反馈线怎样讲清楚，什么是已做、什么待本次做。给一段自然且正面的概括，不要用一堆免责取代贡献。
E. 何时停止v3、切网站，避免不完备焦虑无限延迟？
简要列实际读到哪些文件；不为凑问题制造风险。HERO：不提哈希方案/评分表/通用引擎/重写harness，只针对真实科学与工作流缺口。

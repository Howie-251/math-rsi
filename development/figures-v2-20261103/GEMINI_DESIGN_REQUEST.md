我们已发布MathRSI v2，用户要用GPT Image重画README两图，请先帮我定构图及精简英文文案。当前图见figures/mathrsi/01-evolution.png和02-workflows.png（可读图片则看，否则看该目录README及docs/V2_CHANGES.md、docs/WORKFLOWS.md、base/skills/mathrsi-meta-evolve/SKILL.md相关段）。本次是视觉设计讨论，不改文件、不再完整数学审阅。
需求：
图1必须明确v0→v1→v2：v0是用ARIS散装skills完成PropertyB/ECC研究的经验来源，尚无MathRSI统一harness；v1沉淀五个subworkflow和领域插件（PropertyB成熟、ECC draft）；v2是在v1原位增量+mathrsi-meta-evolve+Degree–diameter(DD)插件。DD历史研究是吸收的额外输入，不能画成v1解出的题。但不写大段防御免责声明，正确箭头与“DD research evidence”标签表达即可。
图2保持5阶段（Prepare/Route loop/Prove/Verify/Handoff）、总控mathrsi-research、wiki贯穿、ARIS实际skills和反向文献/修复、插件插入（PropertyB/DD/ECCdraft）。新增独立外层mathrsi-meta-evolve：从工作区成功/失败/修正证据出发，分类base/plugin/task/defer，修改现有实现→review→use→adopt。不是第六解题阶段，不在单题中静默修改核心。需要画清到下一版本base/插件回馈以及task state留在wiki，defer可淡化。
风格沿用米白底、深青主干、紫色meta、橙色PropertyB、蓝色ECC、绿色DD；英语图，全高清清楚字体，架构图不写论文。希望每张图读一眼懂，正文数量比原图最多略增，不堆参数/声明。
请返回：两图各一个最优空间布局（版本图3列；执行图可下方独立meta带），确切英文短文案、关键箭头方向、你认为应删掉的冗余。重点避免箭头虚假历史和文字太密。只给一套可直接发GPT Image的设计，不额外让用户确认。

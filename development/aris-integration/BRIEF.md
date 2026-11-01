# 严重集成遗漏与修订要求

用户明确指出首版 base/skills 只有 mathrsi-research 一项，ARIS 其它成熟技能仅被提名，没有进入分发与实际工作流。这是能力层遗漏，先前格式/玩具试用不能验收完整MathRSI。用户要求自身包含完整所需内容，不能链接到作者机器另一个仓库。仍以详细Markdown为主、薄自编Python、agent自主推理；需要与Gemini4具体讨论。

拟定具体结构：把 MathRSI/base 当作内部ARIS数学子集根，保留上游布局：base/skills/<name>/SKILL.md 是完整Claude主版；base/skills/skills-codex/<name>/SKILL.md 是完整Codex适配；两端shared-references、skills内脚本/模板及base/tools辅助代码、base/agents必要leaf都实际复制保存。本机原仓库只作为本次源，不是运行依赖。主技能mathrsi-research保持跨宿主自己的入口。项目宿主发现可以使用仅指向本仓库内部的相对别名；不允许任何仓库外软链。复制离线验收不能设置作者原ARIS_REPO。

首批实际能力必须包括 research-lit、research-wiki、wiki-enrich、formula-derivation、proof-writer、proof-checker、proof-orchestrator、research-review、auto-review-loop、lean-formalize、render-html，以及必要的文献来源、引用核查、profile、transitive helpers。按实际调用补齐依赖，不能简单--all安装所有不相关专利/机器人等技能。保留原文件内容、来源提交和许可证；原有全局定制不动。

MathRSI需要另外明确数学专用衔接：原题规格与候选定理区分；目标义务/替代路线/共同对象/效率重判；按具体数学义务的对抗修正循环。原 auto-review-loop 仍可按其原合同用于研究方案改进，但其ML评分与论文收尾不等于定理成立，不能更名冒充数学验收。直接复用者不缩水为小router；新增数学技能要有完整输入、判断、真实路径、操作、输出与下一步，粒度和自主性并重。

Root请求你针对该具体方案找真正缺口，尤其哪些成熟能力还遗漏、哪些新skill只是重复、哪条引用会在离线复制后断。不要赞同只有总控就够，不要靠增加目录/机械清单代替完成。此轮不是解新数学题，原PropertyB/ECC继续暂停，v2仅只读。

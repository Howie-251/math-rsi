一般转移够做一篇有内容的专门期刊短文的主角，不够主投 *Combinatorics, Probability and Computing*、*Random Structures & Algorithms* 或 *Journal of Combinatorial Theory, Series A*。Lean 不进入这个分量判断。形式化能否另写一篇 ITP 或 CPP 论文，我没读源码，现有材料可能已经够，但不能在提炼和相关工作比较之前肯定。

正确的主角是这条一般转移。对每个被精确判据接受的整数 \(M\ge 2^k\)，在该不等式的同一个见证 \(p\) 下，真实最小反例的单交结构还能再吸收 \(\lfloor\sqrt M/(8(1+\ln k))\rfloor\) 条边；最大预算 \(B_{\rm RS}\) 是事后代入，不是事先挑的松基准。见证控制使退化的接受参数也走得通，严格余量从 \(k=12\) 起就在。概念内容是：平凡有向对计数下的接受预算，在最小反例上全体不稳定，不稳定的量有统一显式下界。

这够一篇短文，因为稳定性对全部接受预算成立，不只对充分大的 \(k\) 或某个内点。它必须是短文，因为公共点二分、Gram 秩和团数边数界是经典部件，对数比较是初等执行。写长以后，经典部件会把这一个想法淹成备注。分母里的 8 只改变二级项的常数。五项包络上的严格改进只覆盖那五项。全球查新没有做，手边比较写完也不等于新颖性已证。

Lean 抬不了这个分。转移的陈述和证明在纸面规范源里已经完整；形式化核验的是原超图量词下这条链接得上。转移若只是三行推论，Lean 认证的仍然是三行推论。

ITP 的征稿接受数学形式化与 proof pearls。CPP 接受数学定理的认证，并鼓励说明形式化设计、备选表示、库比较和可复用经验。两处都没有“必须新造工具，或在另一个无关定理上再演示”的条文。第一轮那个强门槛撤回。现有工作是一条新下界的完整形式化，不是对短式调用 `norm_num`，因此值得单独做形式化论文评估，材料里可能已经有足够内容。投稿前要提炼设计选择，并与 Edmonds/Paulson 2023 的 Isabelle AFP 条目 `Hypergraph_Colourings` 比较。不能写首个 Property B 形式化。我没读 Lean 源码，此处不断言够格，也不断言不够。这项评估与数学稿的分量无关。

数学期刊不要求小参数全部 Lean。第二次全量重放是可选加强，不是定理成立的定义。未终审状态保持不变：35、\(k=6,\ldots,11\) 和锁点 4661 现在仍不是已完成定理。

A 是现在就能当主结果的部分：全部 \(k\ge 12\) 的一般转移，以及已完成的 \(m(5)\ge 33\) 和 \(m(5)\ge 34\)。B 是把现有 5–12 的纸面证明整合，由专家把数学覆盖和算术可靠性查完。B 会增强竞争力。查完的具体下界表会使稿件从一条转移变成转移加上一组这个函数的整数，*European Journal of Combinatorics* 上关于分量的争论会因此变小。我给不出升档的数量，也不再把查完的小参数说成对期刊判断必定无影响。C 是另一层次的数学：固定比例的对节省、领先因子的改进，或某个 \(m(k)\) 的精确值。现在这一篇不依赖 C。

下表分开已核对的事实和我的判断。*The Electronic Journal of Combinatorics* 与 *European Journal of Combinatorics* 是两本刊物。分量预期是我的判断，不是官方排序。2026 年会议页只用来看范围。

| 对象 | 已核对的事实 | 我的判断 |
|---|---|---|
| *The Electronic Journal of Combinatorics* | 要求 substantiality | 主投。让转移接受这个标准 |
| *European Journal of Combinatorics* | 范围是组合理论与结构 | 唯一冲刺。争议在想法局部、执行初等 |
| *Discrete Mathematics* | 征稿列超图、极值集合、离散概率 | 主投若因分量被拒，原样改投这里 |
| *Australasian Journal of Combinatorics* | Aglave 等，76 (2020) 73–86，同题具体下界 | B 纳入时同样合适。先例不保证录用 |
| *SIAM Journal on Discrete Mathematics* | 范围含极值问题与概率方法 | 学科相符。不主投，因可迁移性有限 |
| CPC、RSA、JCTA；SODA | JCTA 要求重大推进、新技巧或其他实质进步，长稿更严。SODA 主要按算法见解选稿。CPC/RSA 无“必须改主项”的条文 | 现在不主投、不冲刺 |

主投 *The Electronic Journal of Combinatorics*。冲刺一次 *European Journal of Combinatorics*，并且先投冲刺：成稿若仍以一般转移为唯一主角，正文短，经典部件没有淹没该引理，就先送欧洲组合学。意见若是分量而不是错误，再投 Electronic，定理不改。若不想多等这一轮，取消冲刺，直接主投 Electronic。成稿若变成以小参数证书为主，同样取消冲刺，主投仍是 Electronic，*Discrete Mathematics* 留作分量意见出现后的改投。*SIAM Journal on Discrete Mathematics* 范围相符，但不占这唯一一次冲刺：我看到的想法是最小反例上的结构转移，欧洲组合学的读者更直接。

投稿前只做三件有终点的事。第一，按“任意被接受的 \(M\)，再代入最大预算”重写短文；加一的旧定理和定理 E 退出主线；比较段保持五项包络的原句。第二，只核 Radhakrishnan–Srinivasan、Cherkashin–Kozik、Grill–Linzmayer 是否已有同一条转移，以及 \(m(5)\ge 34\) 相对手边已引结果（含 Aglave 等）的位置；三问写完即停，正文注明全球查新未做。第三，用一份有清单的专家查验决定 B 是否进入这篇：覆盖与算术关上就纳入，关不上就只用 A 投稿。不启动 35/36 的 Lean，不把二次全量重放写成门槛。形式化若另写，独立于这三件，先做设计提炼和与该 AFP 条目的比较。

第一轮撤回的说法是：ITP/CPP 必须另造工具或在第二个定理上演示；*SIAM Journal on Discrete Mathematics* 学科不符；相对增益趋于零则 CPC/RSA 一定不够；JCTA 不发表有限参数或二级项；Electronic 是保底；查完的小参数对判断必定无影响；二次重放是发表定义；SODA 绝对不收纯组合。仍然坚持的判断是：新思想是这一条局部转移，执行是初等估计；它够专门期刊的一篇短文，不够我愿拿去主投 CPC、RSA 或 JCTA 的可迁移洞见。Cherkashin–Kozik 2015 能进 RSA，是因为随机贪心显著简化了同一领先界，并扩展到 \(r\)-染色与边度；本文没有展示同类扩展。未查完的数不是定理。查新没有做。Lean 不提高数学分量。

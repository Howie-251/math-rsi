# Grok / Gemini B 审阅：24点无六度分支

请只读项目内文件，按具体数学义务进行对抗审阅。遵循HERO，不为流程制造假想问题；真正不成立的推理或原命题连接缺口请直接指出。模型意见不代替Lean，不能把局部证书通过写成完整T34完成。

## 要攻击的精确命题

H是`Fin 24`上的简单五元超图，点对覆盖、恰34边，且六度点数为0，则H具有Property B。最终接口为`TwentyFourNoLow.propertyB_of_no_six`。这里的点数、点对覆盖和恰边数是主定理最小反例约化后的内部前提，本分支不负责消去它们。

## 实际结构链

请读：

- `formal/Aris4Math/ThirtyFour/TwentyFourSparseGraph.lean`：任意有限无环对称图关系R，若S无k+1个独立点，则`S.card^2 ≤ k*(S.card+energy (weight R) S)`。证明用最小度点的闭邻域归纳及平方非负，没有整图枚举。
- `TwentyFourStrongCodegree.lean`：两点同为七度或同为八度且共度至少5时的实际双锁染色。有限共度范围没有漏掉超过度数的值，见codegree≤degree。
- `TwentyFourNoLowSelection.lean`：最低度7，总度170给七度点数22或23；消去同一超额图的交叉项，将内部有向超额压为≤98或≤102。22七度时剩余两点均八度，在非B假设下它们共度≤4。坏图的单位边指示权≤超额权，通用不等式给五单位七度点。五点总超额25且外面≥17七度点，选第六点总超额≤1，实际规范到最多一条共度2边。

重点攻击：两种度数情形是否覆盖全部真实H；共同交叉项是否为同一个量；有向/无向能量的2因子；第六点是否真是七度且与前五点不同；唯一非单位对的标签选择是否正确。

## 实际分类与计数链

请读：

- `TwentyFourNoLowSixData.lean`、`TwentyFourNoLowSixNumeric.lean`、`TwentyFourNoLowSix.lean`：46个旧精确证书。实际已正规构建，标准三公理。最坏15907/15912；严格式控制逐位置真正的min(A,B,C-loss)。
- `TwentyFourNoLowCoverageData.lean`：所有3至5元高迹的容量完整目录，单位共度域352个输入、单条二共度域467个输入。每个高迹至少含一个单位点对，故重数≤1。旧lookup定义仍保留，但新的证明链不调用它。
- `TwentyFourSparseDecode.lean`：任意不重复类型列表及0/1分配的完整decode等于其稀疏support指示函数。这是一般Lean证明，不靠输入表猜测。
- `TwentyFourNoLowSparseData.lean`、`TwentyFourNoLowSparseBridge.lean`：每行直接存41位分配编码与一个实际case/perm，不做lookup。CheapMatch核对二值性、extraPair、需要时01对保持，以及真实稀疏高块集合等式；Bridge将它提升为所有T的低/高计数等式，并独立核对46个代表的高迹support与原μ一致。
- `TwentyFourNoLowCoverageKernel.lean`：一次证明rows解码后恰等于完整BoundedAllocations目录，另逐行核验CheapMatch；通过List.mem_map抽取具体见证。没有依赖编码哈希的单射性、搜索器成功标志或同构不变量；准确的完整列表相等与实际support相等才是覆盖依据。
- `TwentyFourPermutation.lean`：factoradic编号只负责给出五次交换复合的真实置换；不需要把所有置换完整枚举作为额外定理。新标签i表示旧标签perm p i，所以实际迹重数读T的前向像；`count_comp`固定该方向。
- `TwentyFourNoLowActual.lean`：实际H通过ActualAllocations进入完整目录；大小>5的迹为零；重标号后的低阶上计数与高迹合起来由MultiLockRecovery恢复所有真实迹，最终返回原H染色。
- `TwentyFourNoLow.lean`：全部选择、分类、数值和实际调用内部装配，不把证书或概率界留作外部前提。

重点攻击：完整目录来自任意实际高迹，而不是搜索成功清单；可出现的迹大小6是否处理；高迹容量与ordinary codegree的方向；代表映射是否使用逆置换错误；度数、空迹、低阶count与upperCount是否混用；真实坏对扣除是否仍使用原H。

## 当前证据边界

最新正规结果已闭合r=0：SparseData2.4秒、SparseBridge14秒、CoverageKernel63秒、Actual2.1秒、NoLow1.3秒，最后67.82秒成功（1035 jobs），最大RSS约10.20GB。覆盖与末端PropertyB的传递公理只有propext、Classical.choice、Quot.sound。原始证据`context/propertyb34/round02/twentyfour/TwentyFourNoLow-sparse-build.log`及同目录相应sparse-build.log。过去两个被终止的覆盖尝试保持失败日志，不计通过；新证据证明的是上述具体r=0内部命题，不是全部24点或完整T34。裸Finset/Bool独立命题复述源码已准备，运行状态以新日志为准。任何未执行Lean的审阅请明确说明是静态数学/源码检查。

请返回：是否发现具体数学错误或接口缺口、对应最小位置、反例或修法；实际读取哪些文件、是否执行任何命令；未执行或未读的范围。不要求一般性评分或无终点复核。

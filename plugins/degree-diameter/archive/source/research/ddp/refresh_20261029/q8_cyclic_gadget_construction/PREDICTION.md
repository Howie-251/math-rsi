# 以相对cube点对的和集覆盖确定循环电压

同一q8 fibre extension目标：若辅助K64含8个Q3、5regular、D≤3，则得到1088点13度D3图。旧J5⊕I1类、纯删published源、旧全crossfactor90秒模型不重跑。

新规则来自作者q9成功的cyclic-voltage gadget思路。顶点(a,l)∈Z8×F2³，编码8a+l；cube边为l xor1,2,4，额外permutation为sigma(a,l)=(a+δ_l mod8,π(l))，π(l)=l xor3（l偶parity）或l xor5（l奇parity）。π=[3,4,7,0,1,6,5,2]。

对最远的cube标签l→l xor7，三步phase集合可化为A_l+A_r，其中A_l={0,δ_l,−δ_π(l)}；r=l xor2（偶parity）或l xor4（奇parity）。八根条件化为四个三元和集全覆盖条件。

取A={0,1,2}、C={0,2,5}，A+C=Z8；令A0=A、A2=C、A1=−C、A5=−A，可同时满足这些远对条件。字面参数为delta=[1,3,2,6,2,6,1,3]。这不是随机seed或按总坏对数挑选，而是预先保证一整类目标覆盖。

具体预测：该唯一候选也覆盖其余标签，因此K64 D≤3；若失败，保存实际失败根/标签与phase类，判断是否需要修改生成规则，不按坏对微调。先严格检查sigma无1/2cycles、cube边不重复、全degree5，再检查全部64根R3。单worker CPU≤10秒；只有完整通过才生成1088主图和独验。此候选含失败即可停止，不能把部分对覆盖当完整辅助图。

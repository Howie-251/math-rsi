# Q4 完整补全 + 真实空面信息：认证上界 0.59970530

主证书：

    pi_Q(C4) <= 119941059204403/200000000000000
             = 0.599705296022015 < 0.59970530

这是渐近边密度上界，不是 Q8 的有限上界，也不是 Erdős 的 1/2 猜想证明。
本轮产出的计算机辅助证书尚未经过第三方独立复现/同行审阅；不声称 SDP 最优性。

## 最小独立验证

要求 Python >=3.10，及 g++ 或 clang++（支持 C++17）。不需要 NumPy、SciPy、SDP 求解器或预生成系数表。

    python verify_standalone.py

控制实验：

    python verify_standalone.py certificate_six.json

验证器从整数 Gram 因子保证半正定，重建 Q3 对称群，确认全部层对覆盖，枚举合法灰边补全，再对 3,312,331 个代表直接计数检查。它不读取搜索生成的巨大系数表。

权威数据是 certificate.json 中的整数因子；matrix_*.txt 的小数只供查看。
理论从局部到高维的平均引理见《研究报告.md》，此包不是 Lean 形式化证明。

## 文件

- certificate.json：最终八块精确 Gram 因子。
- certificate_six.json：只用旧六块但加入完整补全联合约束的控制证书。
- keys.bin：90,179 个部分类型代表；验证器会检查它们覆盖全部有序 Q3 层对。
- verify_standalone.py / verify_direct.cpp：独立验证入口及直接计数检查器。
- 研究报告.md：定义、证明、枚举覆盖、归一化与限制。
- standalone_verification.log / six_verification.log：本轮验证输出。
- variant_audit.json：固定证书消融；不是重新优化消融。
- worst_local_graph.json：达到最终证书最大值的一个局部图，不是渐近极值构造。
- SHA256.json：文件校验值。

## 研究代码包额外说明

使用 NumPy、SciPy 和 C++17。求解器通过 SciPy 内部 HiGHS 接口作 PSD 秩一列生成；内部接口可能随 SciPy 版本变化，独立验证器不受影响。

    python build_completion.py
    python build_joint_shadows.py
    python build_full_flags.py
    python solve_joint.py --rounds 150
    python solve_full_flags.py --rounds 180
    python certify_full_flags.py
    python verify_standalone.py

这些生成器会产生约 1 GB 中间数据。最小验证包不需要它们。

搜索日志的 min_eig 表示对偶定价矩阵的负特征值，不表示证书矩阵不半正定。最终所有证书矩阵都以精确 Gram 分解给出。

Baber 的文献基准是 0.60318（arXiv:1201.3587v2, Theorem 4.1）；本轮常数低于该基准，但不以有限网络检索代替完整文献优先权审查。

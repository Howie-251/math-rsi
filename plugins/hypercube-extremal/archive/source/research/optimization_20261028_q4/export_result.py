"""Create and freshly verify a minimal, self-contained certificate package."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

P = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('--input', required=True)
args = ap.parse_args()
snapshot = P / 'final_snapshot.npz'
shutil.copy2(P / args.input, snapshot)
subprocess.run([sys.executable, str(P/'certify_six.py'), '--input', snapshot.name,
                '--out', 'final_certificate.json'], cwd=P, check=True)
c = json.loads((P/'final_certificate.json').read_text(encoding='utf-8'))
bound = Fraction(c['upper_numerator'], c['upper_denominator'])
old = Fraction(18933741304467, 32000000000000)
assert bound < old, 'No certified improvement'
package = P.parent / 'Q4_optimized_certificate_20261028'
package.mkdir(exist_ok=True)
shutil.copy2(P/'final_certificate.json', package/'certificate.json')
for name in ['keys.bin','verify.py','verify_six.cpp']:
    shutil.copy2(P/name, package/name)
proc = subprocess.run([sys.executable, str(package/'verify.py')], cwd=package,
                      capture_output=True, text=True, encoding='utf-8')
(package/'verification.log').write_text(proc.stdout+'\n'+proc.stderr, encoding='utf-8')
print(proc.stdout, flush=True)
if proc.returncode:
    print(proc.stderr, flush=True)
    raise SystemExit(proc.returncode)
D = c['gram_denominator']
diags = [max(Fraction(sum(z*z for z in row),D*D) for row in L)
         for L in c['gram_factors']]
def ceil6(x):
    return Fraction((x.numerator*10**6+x.denominator-1)//x.denominator,10**6)
mf, mv = ceil6(max(diags[:5])), ceil6(diags[5])
summary = dict(previous_bound=str(old), certified_bound=str(bound),
               certified_decimal=float(bound), outward_decimal=c['upper_decimal_ceil_8'],
               absolute_improvement=float(old-bound), gap_to_059=float(bound-Fraction(59,100)),
               below_059=bound<Fraction(59,100), source_snapshot=args.input,
               worst_q4_mask=c['worst_graph'], max_face_diagonal_upper=str(mf),
               max_vertex_diagonal_upper=str(mv), verification_exit_code=proc.returncode,
               status='EXACT_INTEGER_VERIFICATION_PASSED; NOT_SDP_OPTIMALITY_PROOF',
               level='Q4; no Q5 constraints used')
(package/'result.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
readme=f'''# 2026-10-28 联合优化后的 Q4 上界证书

本轮认证的渐近上界为

pi_Q(C4) <= {bound} = {float(bound):.16f} < {c['upper_decimal_ceil_8']}。

原界为 {float(old):.16f}；绝对下降 {float(old-bound):.12f}。
距 0.59 尚有 {float(bound-Fraction(59,100)):.12f}，本轮未突破 0.59。

## 复核

本目录运行 `python verify.py`。只需 Python 标准库及支持 C++17 的 g++ 或 clang++。
不要使用 -DNDEBUG。核验器检查整数 Gram 半正定性、64 位算术安全、全部
8,421,604 个有序 Q3 层对的轨道覆盖、13,150,453 个合法带标记补全，
并直接整数检查 3,312,331 个代表。打包后已实际重跑，退出码 0，见 verification.log。

## 本轮做了什么

从前轮 certification_snapshot.npz 出发，联合优化五个面根块和一个顶点根块，
阶数为 240、212、190、187、170、9。提高每轮 L-BFGS 迭代数及历史容量，
保留每轮全量扫描；另运行半正定秩一列生成作为对照，再进行较低平滑温度的精修。
最终使用 {args.input}，整数 Gram 分母为 10^7。
原目录未修改；搜索记录与脚本在 ../optimization_20261028_q4/。

模型仍为原 Q4 层级，未加入 Q5 三方向约束，也没有得到 SDP 全局最优性证书。
浮点优化达到迭代预算不是数学最优。列生成分布矩阵的负特征值不是原图反例。
当前结果是一份更强的可行上界证书，不表示 0.59 无法在 Q4 层级实现。

## 证书到高维上界的证明

对完整合法 Q4 图 K，直接核验

e(K)/32 + C_F(K) + C_v(K) <= C。

C_F 是对 24 张根面平均的两个外部方向旗矩阵条目，保持共同根标号，
并按各根稳定子同步群平均。C_v 是对 16 个顶点、每顶点 3 种不相交方向对划分
平均的 9 状态矩阵条目。矩阵都由整数 L 给出 Q=LL^T/10^14。

在 Q_n 中随机取 Q4，边密度平均恰为 rho(G)。固定根面，q=n-2 个外部方向
的频率向量 u 与不同方向联合矩阵 R 满足
uu^T=((q-1)/q)R+diag(u)/q。
所以根面项平均 >= -M_F/(n-3)。五种根型互斥，M_F 取最大对角元即可。

顶点根下两个独立方向对的不相交概率为
p_n=(n-2)(n-3)/(n(n-1))。
PSD 给无条件平方型非负，矩阵条目绝对值不超过最大对角元 M_v，
故不相交条件下的平均 >= -M_v(1-p_n)/p_n。

本证书安全地取 M_F={float(mf):.6f}、M_v={float(mv):.6f}，于是 n>=4 时

rho(G) <= C + {float(mf):.6f}/(n-3)
             + {float(mv):.6f}(4n-6)/((n-2)(n-3))。

令 n 趋于无穷得到所述渐近界。不能把 C 直接当作任意固定维数的密度上界。
最坏局部代表的掩码为 {c['worst_graph']}。

## 验证边界

核验器从几何直接计数，不读取优化系数表；它与前轮使用相同验证程序。
本轮未声称跨研究者复现、跨模型独立审稿、形式化证明或文献优先权核查。
'''
(package/'README.md').write_text(readme,encoding='utf-8')
names=['certificate.json','keys.bin','verify.py','verify_six.cpp','verification.log','result.json','README.md']
hashes={name:hashlib.sha256((package/name).read_bytes()).hexdigest() for name in names}
(package/'SHA256SUMS.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2),flush=True)

# Signed edge-flow门：能排什么、不能排什么

仅核读本目录PAPER/RESULT及保存的66-path格式；未提取新flow、枚词、BFS、solver或换base。旧四全局系数12720代表完整NO不变；以下讨论更自由的**逐实际边C23平移电压**，不是任意permutation cover。

**精确不变量。** 给960条无向实际point-edge固定方向，路径w的整数signed flow记f_w（正走+1、反走−1）。任意边电压θ下，lift位移恰为f_w·θ mod23。因此同一个ordered base pair的相同flow永远碰撞；若其≤5 NB paths只有至多22个不同flow，便严格排该固定base的全部逐边C23电压D≤5。长度≤5时每坐标差在[−10,10]，故mod23相同flow等价于整数相同flow。四共享系数是进一步线性压缩，不能用旧26个forms充当任意边电压的flow数；旧paths1/14在edge{8,104}的使用数不同，已说明该碰撞可拆。

**闭路径的更强必要条件及反例边界。** u=u时空路flow0，反向路径flow为−f。零signed flow在任意abelian电压都回0，但本simple、无loop图在长度≤5没有非空零流NB闭路：零流长度必偶且≤4，每条用过的无向边至少两次，support至多两边、必为树；非空树上闭walk必即时回退，矛盾。所以这里不能未经数据就期待“大量零流”解释失败。设闭路径不同非零flow有r个反号类，则最多1+2r个phase，D5必要r≥11；实际赋值还须使这些flow值覆盖F23*的全部11个±类。r≥11只过数量门，不保证这些值互异非零，更不保证同一θ兼容其它pairs。不同roots共享同一cycle flow可造成兼容约束，但不能把不同base targets混成一个覆盖槽。

**最小缓存。** 当前先只给已有8→70的66条path附：稀疏`(min(u,v),max(u,v),signed_count)` flow、flow类→原path indices及一条代表、distinct数；若类分裂，给一个不同edge坐标即可。不需新源或BFS。若未来已有闭path缓存，可另给0类与±类绑定；本轮没有核读或生成diagonal/all-pair flow，不能宣称已排它们。任一packet去重后≥23仍未排，只能提出下一兼容问题，不能偷换成可行图。边界固定为C23/abelian位移：非abelian或一般permutation电压依赖顺序，零abelianized flow未必返回原点，不能套此NO。0目标图、0新数值；完成即停。

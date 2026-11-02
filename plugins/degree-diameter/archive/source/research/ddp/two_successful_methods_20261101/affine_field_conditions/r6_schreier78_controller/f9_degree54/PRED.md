# 唯一C78的完整F9纤维图生产预测

2026-11-01，运行前保存。仅使用父目录刚实际PASS的controller `(2,6,17,5,10)`；不继续参数搜索、不恢复C60+H18 CNF、无新field／modulus梯子。

目标：`(54,3)`，56862点、1535274边，全部54正则。单worker总30 CPU秒，包含准备、实际8chart局部核对、编译、生成与生产检查；完整新图fresh独验由另一代理承担。

GF9=`GF3[w]/(w²+1)`，code `a+3b`；纤维x label=`x0+9x1+81x2`，总label=`729u+x`。六方向及真实矩阵直接取 `../../r6_f9_projective_halves/cross_port_extension/PARAMETERS.json`。实际dart `u,p→v,q`，p<q取canonical跨port正向，p>q取其真逆，p=q按u<v取self正向／反向。关系 `y=T*x+t*ell_q`，`t∈GF9`。

保存完整全局lex排序的无向literal边表、完整参数与dart-chart绑定。对实际全部56862顶点生成54邻点，检查无自环、无重邻；逐dart／全部729坐标／全部9噪声验证真逆；比较完整234控制边对应的literal边计数与全局degree。核实际用到的8张chart的双向逆、方向运输、全部200个中央turn满秩、相邻pencil十平面覆盖729。

全部点对D3由父目录完整234类三port证据承担：216同层／非邻类NB3满秩，18相邻类pencil；任意源x的仿射中心不影响满覆盖，不假设fiber平移为图automorphism。此生产不把零坐标测试或少量BFS写成全根验收。原图不重验，无solver／Lean／hash／install。

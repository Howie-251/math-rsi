# 主线接受记录｜六维完整 A8 与七维差一门扩展

2026-11-15。主代理逐节读回整装证明、独立审计及孔位重算，接受**完整六维 $A_8$**。对任意 $K(Q_6)$ 匹配，若八个原孔分为三少数、五多数，则对任意指定多数孔 $z$，存在保留全部原边且恰避 $z$ 的 $63$ 点简单圈。所有新增边均短，原规定匹配允许长边和同色边。该结论可作为主线的已接受导入。 [整装证明](Q6_A8_FULL_CLOSURE.md) · [独立审计](Q6_A8_EASY_CUTS_REVIEW.md) · [机器回执](Q6_A8_EASY_CUTS_REVIEW.json)

独审回执为 **26/26 PASS · same-family · provisional · sound-modulo-imports**。预处理用相邻孔加短边降到六维 $A_6$，再用五类五维保边拼接。独立重算确认，预处理后的规范孔位覆盖表含 $83\,515$ 行，五类切分后恰余七个坐标置换轨道。若一轨的所有候选零差双桥均不可用，原匹配的每条边必须位于一个共同签名纤维内。七轨各有一个奇覆盖点纤维，故任意实际匹配都能找到可用双桥。有限计算用于孔位和奇纤维核查，未枚举规定匹配。 [独立重算](Q6_A8_FULL_REVIEW_check.json) · [奇纤维证书](zero_delta_obstructions.json)

主线同时接受六维 $B_4$，即任意两色各四孔的 $K(Q_6)$ 规定匹配，从任意自由根到任意异色目标都有保边生成路，目标允许已覆盖，新增边均短。旧七维差一门据此扩为 $0\le a\le3,\ 0\le b\le5$。原七维短匹配只要有一坐标切分的两面孔型为 $(a,a+1)/(b+1,b)$，就有含全部原边的全短生成圈。新范围包括 E16 中央型 $(a,b)=(3,4)$ 和 E18 的 $(a,b)=(3,5)$。 [整装证明 §5](Q6_A8_FULL_CLOSURE.md) · [保边回代补充审计](Q6_A8_APPLICATIONS_REVIEW.md)

补充审计也确认 FREE 和 SPLIT 的整面接收可扩至 $s\le3$。FREE 仍需同一组选定的三枚实际桥源及原避二供体条件。SPLIT 仍限 $k\in\{3,4,5\}$，须保留原分居供体的孔差、标记和供给条件。两项扩展给满足对应供体前提的实际接收匹配提供避一圈。 [回代范围及供体前提](Q6_A8_APPLICATIONS_REVIEW.md)

本轮后，E16 完整 $\mu=1$ 在此验收记录的范围内仍开放，两个边缘差一型 $(a,b)=(0,7),(1,6)$ 仍需主线另证联合覆盖。完整 E16、完整 E18 与 $R_7$ 均未由本轮验收关闭。

| 绑定文件 | SHA-256 |
| --- | --- |
| Q6_A8_FULL_CLOSURE.md | d11163cc2270b3873ec725238aba59368706ca47e9be3d6a969086872fe8596a |
| Q6_A8_EASY_CUTS_REVIEW.md | 17583d6e4d0dad7759b4a9bfca1cb793731d1f6c088f82af858b6c7387030599 |
| Q6_A8_EASY_CUTS_REVIEW.json | 4f034346c1a327dc286f2d20d26ffa68ed75cedbb71b9e0d0031d9fb60b71307 |
| Q6_A8_APPLICATIONS_REVIEW.md | d466612ada98014666fc1dc2b1087a12dfe458be239214daabf816cc544fe8d2 |
| Q6_A8_FULL_REVIEW_check.py | d96b4b3f889710a1e0beca645054b611cc47314d0c2b7de7980e3891efe7f392 |
| Q6_A8_FULL_REVIEW_check.json | e579546a6515f59dc3ddec72c98fcc09a6fc1917f5c4473bd2b4a91a6700fba9 |
| enumerate_a8_geometry.py | 295f0bbc2a6ba9b6298585b088ac77ccfaee8f1b66c930324bc44fc87be9859a |
| geometry.json | 4b2e02fccbae17b4a8b345b76158eadcba201e6ad3b965e59f86d32f88596398 |
| verify_zero_delta_obstructions.py | 307124556f6faaffe01e931dae4db74e3aeea885a723a0d56a982222d4256cda |
| zero_delta_obstructions.json | 88a00321632f957d464a59482362a68cc62d3dbd909d5175aadf592cd4d383d8 |

机器回执所列的九份审计输入、十八份导入及三份回代补充来源均已核对文件散列。

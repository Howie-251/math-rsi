# K4×16控制器：由同index路线计数直接排除

新K4 block确实增加三角形，但内部三角形不改变deck坐标。长度≤3返回同index的群位移类型，按P的五cycletypes，总有一个root至多13／11／11／13／15种，少于所需16。因此64点、5度、D3控制器在这个uniform K4＋单F／真逆规则下不存在。

执行了3120条symbolic words的精确小检验，整数signature和非交换free-word计数完全一致，CPU0.00208秒。原327680数值赋值gate只编译、未运行，实际赋值枚举0；没有fiber图、候选控制器、solver或Lean。

纸面路径计数还统一适用于任意regular deck group H：此机制若D3则|H|≤15、controller阶≤60。不需要换D8或其他16元素群再试；非uniform external2factor和其他控制器组织未被排除。

[完整证明](PROOF.md) · [原预测与执行前修订](PRED.json) · [所有symbolic见证](SYMBOLIC_CERTIFICATE.json) · [实际结果](RESULT.json) · [终态](TERMINAL.json)。

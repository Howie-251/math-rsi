# Bhakar104 unlettered(a)／b两cut／四星：新根可过、旧路线仍断

官方unlettered文件是104_d4D4.txt，a_unlettered及source104a.header.edges只是实验alias；另一个输入为104b。两者各104/208/全4度，source D4/非同构继承primary，未重验。旧104c同规则20904 NO只继承，不重跑。

两源各21528无序原边对剔除624共端点对，20904合法组完整。四端点P含全部cutends，source closedR3(P)是newroot R4精确门；a有16、b有24案通过，支持newroot预测，但全被actualcandidate旧旧距离拒绝。累计旧root普通BFS为18/27次，不是失败图数或source D4全验证。新深3支持各104次，保存反例的source单pair诊断各1次。

两首案cuts均0–8、4–12。a的0→19 source4路0–8–2–27–19，新图最短5路0–14–6–31–23–19；b的0→22 source4路0–8–16–47–22，新图最短5路0–4–60–52–14–22。展示的旧路都经过被删0–8；不是声称旧路唯一。实际新图最短5才是拒绝证据，说明newroot覆盖不继承oldold D4。

原RESULT/TERM case0.574206988/10CPU保留，通用engine编译已记在252原case，无重复编译费用。详见[TWO_SOURCE_SCOPE_REVIEW](TWO_SOURCE_SCOPE_REVIEW.md)。当前严格NO只限每个fixedliteral/two-disjoint-originalcuts/one4star/nootheredits，不排一般105/(4,4)、第三cut、repair或其它helpers。0完整命中、新图/参数/Lean/独立方法；停止，无fresh正例套件。

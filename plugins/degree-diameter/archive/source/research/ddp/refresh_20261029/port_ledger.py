#!/usr/bin/env python3
"""Bounded symbolic port diagnostic on an existing family, without network simulation."""
from fractions import Fraction
import json
from pathlib import Path
import time

start = time.process_time()
here = Path(__file__).resolve().parent
project = here.parents[2]
family = json.loads((project / "research/ddp/more_graphs_20261027/delivery/families.json").read_text())["families"]["13"]
base = family["base"]
rows = []
for n in [base["n"], 51437, 51457]:
    m = base["m"] if n == base["n"] else next(s["new_m"] for s in family["steps"] if s["new_n"] == n)
    a, b = n - base["n"], m - base["m"]
    rows.append(dict(n=n, m=m, routers_added=a, links_added=b,
        endpoint_slot_formula=f"{n}*r - {2*m}",
        slot_change_formula=f"{a}*r - {2*b}",
        zero_change_radix=str(Fraction(2*b,a)) if a else None,
        illustrative_uniform_radix16_slots=16*n-2*m,
        illustrative_uniform_radix16_change=16*a-2*b))
result = dict(status="PORT_ACCOUNT_ONLY_COMPLETE", family=[13,5], source="delivery/families.json",
    assumption="Each vertex is one uniform-radix-r router; each network edge consumes one port at each endpoint; r>=13",
    interpretation="Potential endpoint slot count only; current physical devices/endpoints/capacities unspecified",
    rows=rows, throughput_test_run=False, latency_test_run=False,
    routing_simulation_run=False, graph_verification_repeated=False,
    CPU_seconds=time.process_time()-start)
(here / "PORT_LEDGER_RESULT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
(here / "PORT_LEDGER_REPORT.md").write_text("""# 十三度成功族的有限端口诊断

仅完成端口账，不建立工业性能结论。没有仿真、采购、依赖安装或旧图复验。
假设每顶点是一台总端口数为r的路由器，每条网络边占两端各一口；r≥13。
潜在端点槽位 P=rn−2m。使用已保存原图51417/324451、中间图51437/324651、最终51457/324863。

|对象|新增路由器|新增网络边|相对原图槽位变化|
|---|---:|---:|---|
|中间图|20|200|20r−400|
|最终图|40|412|40r−824|

最终图若13≤r≤20，潜在端点槽位反而减少；r=21时净增16个，r≥21才可能净增加。r=16仅为明确的数学示例，没有声称使用某商业设备：总槽位173770→173690→173586，最终减少184。
若原有空口已接端点，新增网络边会占用其连接机会；保留网络旧边不自动保留端点服务。r较大时槽位可能增加，仍需扣新增40台设备与412条链路成本，不能直接当吞吐收益。

因此本轮止于端口诊断，不启动路由/吞吐/延迟模拟，不把它计为新数学下界。只有后续明确端点映射与端口预算后，再决定是否值得进行所述性能试验。
逐项输入和符号式见PORT_LEDGER_RESULT.json。新图结果仍103例/3格，Lean0。
""")
print(json.dumps(result, ensure_ascii=False))

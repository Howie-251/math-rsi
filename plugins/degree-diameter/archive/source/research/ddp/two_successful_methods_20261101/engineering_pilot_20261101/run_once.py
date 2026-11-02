from pathlib import Path
from collections import Counter, deque
from fractions import Fraction
import csv
import html
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREP = 0.2
BUDGET = 5.0
resource.setrlimit(resource.RLIMIT_CPU, (4, 5))


def dump(name, data):
    (HERE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


dump('HANDLE.json', {'pid': os.getpid(), 'status': 'RUNNING_NEW_TRAFFIC_PILOT',
                     'worker_count': 1, 'CPU_budget_seconds': BUDGET,
                     'conservative_preparation_charge_seconds': PREP})

stage = ROOT / 'research/ddp/two_successful_methods_20261101'
base = stage / 'retained_edge_transfer/published_d15_15552_D4_source_gate'
source = json.loads((base / 'RESULT.json').read_text())
final = json.loads((base / 'degree16_plane837/independent_acceptance/RESULT.json').read_text())
old_pilot_path = stage / 'retained_edge_transfer/engineering_pilot/RESULT.json'
old_pilot = json.loads(old_pilot_path.read_text())


def port_record(name, n, m, hist, physical_ports):
    slots = sum((physical_ports - int(degree)) * count for degree, count in hist.items())
    return {'name': name, 'switches': n, 'network_links': m,
            'inherited_degree_histogram': hist, 'physical_ports_per_switch': physical_ports,
            'network_port_endpoints': 2*m, 'available_non_network_switch_port_slots': slots,
            'slots_identity_Pn_minus2m': physical_ports*n - 2*m}


ports = [port_record('published_source15552', source['source_n'], source['source_m'],
                     source['actual_degree_histogram'], 16),
         port_record('accepted_clone16389', final['n'], final['m'], final['degree_histogram'], 16)]
port_delta = {'switches_added': ports[1]['switches']-ports[0]['switches'],
              'network_links_added': ports[1]['network_links']-ports[0]['network_links'],
              'server_port_slot_change': ports[1]['available_non_network_switch_port_slots']-ports[0]['available_non_network_switch_port_slots']}

old3750 = next(g for g in old_pilot['graphs'] if g['name'] == 'source3750')
physical3750 = {p: old3750['physical_port_counts'][p] for p in ['24', '32']}
raw_rel = 'research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges'
with (ROOT / raw_rel).open() as f:
    n, m = map(int, next(f).split())
    adj = [[] for _ in range(n)]
    for row in f:
        u, v = map(int, row.split())
        adj[u].append(v)
        adj[v].append(u)
for row in adj:
    row.sort()
endpoints = [i*n//16 for i in range(16)]


def route(removed=None):
    routes = {}
    loads = Counter()
    visits = []
    for source in endpoints:
        parents = [-1]*n
        distance = [-1]*n
        distance[source] = 0
        parents[source] = source
        queue = deque([source])
        missing = set(endpoints)
        missing.remove(source)
        expanded = 0
        while queue and missing:
            u = queue.popleft()
            expanded += 1
            for v in adj[u]:
                if removed is not None and (min(u, v), max(u, v)) == removed:
                    continue
                if distance[v] < 0:
                    distance[v] = distance[u]+1
                    parents[v] = u
                    queue.append(v)
                    missing.discard(v)
        visits.append({'source': source, 'expanded_for_sample_targets': expanded})
        for target in endpoints:
            if source == target:
                continue
            path = []
            if distance[target] >= 0:
                at = target
                path.append(at)
                while at != source:
                    at = parents[at]
                    path.append(at)
                path.reverse()
                for edge in zip(path, path[1:]):
                    loads[edge] += 1
            routes[(source, target)] = {'hops': None if not path else len(path)-1,
                                        'path': path}
    reachable = [r for r in routes.values() if r['path']]
    peak = max(loads.values(), default=0)
    return routes, loads, {'routing_BFS_sources': len(endpoints),
                          'requested_flows': len(routes), 'reachable_flows': len(reachable),
                          'unreachable_flows': len(routes)-len(reachable),
                          'total_hops_of_routed_flows': sum(r['hops'] for r in reachable),
                          'mean_hops_of_routed_flows': sum(r['hops'] for r in reachable)/len(reachable) if reachable else None,
                          'peak_directed_link_unit_flow_load': peak,
                          'one_peak_directed_link': list(min(e for e, v in loads.items() if v == peak)) if peak else None,
                          'fixed_route_common_flow_rate_upper_bound': float(Fraction(1, peak)) if peak and len(reachable)==len(routes) else 0.0,
                          'fixed_route_common_flow_rate_exact_fraction': str(Fraction(1, peak)) if peak and len(reachable)==len(routes) else '0',
                          'sample_target_expansion_counts': visits}


before_routes, before_loads, before = route()
undirected = Counter()
for (u, v), value in before_loads.items():
    undirected[min(u, v), max(u, v)] += value
max_both = max(undirected.values())
removed = min(e for e, value in undirected.items() if value == max_both)
after_routes, after_loads, after = route(removed)
detours = [after_routes[p]['hops']-before_routes[p]['hops'] for p in before_routes
           if before_routes[p]['path'] and after_routes[p]['path']]
changes = {'removed_undirected_link': list(removed),
           'baseline_bidirectional_unit_flow_load_on_removed_link': max_both,
           'rerouted_path_count': sum(before_routes[p]['path'] != after_routes[p]['path'] for p in before_routes),
           'max_detour_hops_among_still_routed_flows': max(detours, default=None),
           'detour_histogram': dict(sorted(Counter(detours).items())),
           'mean_hop_change': after['mean_hops_of_routed_flows']-before['mean_hops_of_routed_flows'],
           'peak_directed_load_change': after['peak_directed_link_unit_flow_load']-before['peak_directed_link_unit_flow_load']}
with (HERE / 'flow_paths.csv').open('w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['scenario', 'source', 'target', 'reachable', 'hops', 'path'])
    for scenario, routes in [('baseline', before_routes), ('one_link_removed', after_routes)]:
        for (s, t), value in routes.items():
            writer.writerow([scenario, s, t, bool(value['path']), value['hops'], ';'.join(map(str, value['path']))])
cpu = time.process_time()
result = {'status': 'BOUNDED_ENGINEERING_PILOT_COMPLETE', 'date': '2026-11-01',
          'port_accounting_16ports': ports, 'port_accounting_change': port_delta,
          'physical3750_24_32ports_inherited': physical3750,
          'prior_pilot_inherited': str(old_pilot_path.relative_to(ROOT)),
          'new_workload_differs_from_old_pilot': 'endpoints floor(i*n/16), unit demand, deterministic single shortest path, one link failure',
          'graph_literal_parses_for_new_traffic_question': 1, 'graph_source': raw_rel,
          'source_n_inherited': n, 'source_m_inherited': m,
          'source_degree_diameter_Lean_acceptance': 'inherited; no new validity or all-root diameter verification',
          'workload_endpoints': endpoints, 'ordered_nonself_unit_flows': 240,
          'routing': 'sort neighbors; BFS first parent; one shortest path per flow',
          'link_capacity_model': 'each directed link capacity1, full duplex; independent ideal static link capacities',
          'baseline': before, 'one_link_removed': after, 'changes': changes,
          'prediction_all_sample_flows_connected_and_max_detour_at_most1': after['unreachable_flows']==0 and max(detours, default=0)<=1,
          'traffic_route_BFS_total': 32, 'old_allroot_validity_or_D3_BFS': 0,
          'source15_or_final16_graph_parses': 0,
          'scope': '240 fixed sampled flows, one selected failed link, fixed routing and abstract port model; no global fault diameter or allpairs traffic inference',
          'industrial_advantage_claimed': False, 'real_hardware_throughput_measured': False,
          'wiring_lengths_or_money_cost_measured': False, 'new_graph_parameter_Lean_increment': [0, 0, 0],
          'process_CPU_seconds_subtotal_before_receipts': cpu, 'conservative_preparation_charge_seconds': PREP,
          'cumulative_CPU_seconds_subtotal': cpu+PREP, 'CPU_budget_seconds': BUDGET,
          'worker_count': 1, 'followup_started': False}
dump('RESULT.json', result)
note = f'''# 一次限定工程pilot

## 固定16口时，增交换机与可用服务器端口的取舍

从已接受度数元数据读取，15552源有16200个非网络交换机端口槽；16389终图有4554个。增加837台交换机和12519条网络链路，物理交换机端口增加13392，网络端点消耗增加25038，净少11646槽。端口假设只给每槽最多接一个服务器的上限；没有实测部署服务器数。两个大图均未解析或重验。

3750源的24/32口剩余槽15000/45000继承旧工程pilot。其交换机图degree20，服务器端口必须另占物理预算；若服务器边各增加一跳，服务器端到端路径会比交换机路径多两跳。

## 240个固定流与一次链路故障

16端点为{endpoints}。每个有序非自流需求1，邻接排序后BFS首父给一条最短路径，有向链路容量1。每场景仅16次新流量路由BFS，总32次，未做旧图3750根D3验证。

基线总hop={before['total_hops_of_routed_flows']}，平均hop={before['mean_hops_of_routed_flows']:.6f}，峰值有向负载={before['peak_directed_link_unit_flow_load']}，固定路由共同flowrate上界={before['fixed_route_common_flow_rate_exact_fraction']}。

删除样本双向负载最大的无向边{removed}（双向负载{max_both}，平手按字典序）后，同240流不可达{after['unreachable_flows']}，平均hop={after['mean_hops_of_routed_flows']:.6f}，最大绕行{changes['max_detour_hops_among_still_routed_flows']}，峰值负载={after['peak_directed_link_unit_flow_load']}，共同flowrate上界={after['fixed_route_common_flow_rate_exact_fraction']}。路径变化{changes['rerouted_path_count']}条；绕行分布{changes['detour_histogram']}。事前“全部连通且最大绕行≤1”预测结果为{result['prediction_all_sample_flows_connected_and_max_detour_at_most1']}。

共同flowrate上界是给定路径、理想静态有向容量模型中的归一化量；没有测量全网最优吞吐、硬件链路速率、队列、协议收敛或工业表现。旧pilot的端点/单位需求/等路径分流与本次不同，不能将两套峰值直接作图优劣比较。一次故障样本也不代表任意链路或全网故障直径。所有480条情景路径在flow_paths.csv。

只有这一次pilot，0新图、0参数、0Lean、0外审。CPU最终回执在TERMINAL.json，累计预算5CPU秒。全部停止，不追加工作负载或故障。
'''
(HERE / 'NOTE.md').write_text(note)
page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>限定工程pilot：端口、路由与单链路故障</title><style>body{{max-width:980px;margin:30px auto;padding:0 20px;font:16px/1.7 system-ui;color:#203449}}table{{border-collapse:collapse;width:100%}}th,td{{padding:9px;border-bottom:1px solid #d5dfe7;text-align:left}}a{{color:#17649a}}.note{{padding:12px 18px;background:#edf3fa}}</style></head><body><h1>限定工程pilot</h1><p>2026-11-01。<a href="RESULT.json">实际数据</a> · <a href="NOTE.md">模型说明</a> · <a href="flow_paths.csv">480条情景路径</a> · <a href="pilot.html.txt">HTML源码</a></p><div class="note">0新构造。只测240个固定流及一条样本链路故障；旧图合法性和直径继承。</div><h2>同为16物理口的端口记账</h2><table><tr><th>交换机图</th><th>交换机数</th><th>网络链路</th><th>非网络端点槽</th></tr><tr><td>原source</td><td>15552</td><td>116316</td><td>16200</td></tr><tr><td>扩张图</td><td>16389</td><td>128835</td><td>4554</td></tr></table><p>增加837交换机及12519链路，非网络端口槽减少11646。每槽至多接一个服务器；实际服务器数未测。3750图的24/32口槽15000/45000继承旧pilot。</p><h2>3750图的固定单路径流量</h2><p>16端点floor(i×3750/16)，240个有序非自流各1单位，有向链路容量1，sort-neighbor BFS选单条最短路径。</p><table><tr><th>情景</th><th>平均跳数</th><th>峰值有向负载</th><th>共同flowrate上界</th><th>不可达</th></tr><tr><td>基线</td><td>{before['mean_hops_of_routed_flows']:.6f}</td><td>{before['peak_directed_link_unit_flow_load']}</td><td>{before['fixed_route_common_flow_rate_exact_fraction']}</td><td>{before['unreachable_flows']}</td></tr><tr><td>删链路{removed}</td><td>{after['mean_hops_of_routed_flows']:.6f}</td><td>{after['peak_directed_link_unit_flow_load']}</td><td>{after['fixed_route_common_flow_rate_exact_fraction']}</td><td>{after['unreachable_flows']}</td></tr></table><p>最大绕行{changes['max_detour_hops_among_still_routed_flows']}跳，{changes['rerouted_path_count']}条路径变化。只作32次流量路由BFS，0旧全源直径复验。</p><p>这些是给定工作负载/路由/容量假设的归一化结果。队列、协议收敛、全网最优吞吐、任意故障、布线长度和货币成本未测；没有工业优势结论。<a href="PRED.md">事前预测与预算</a> · <a href="TERMINAL.json">终态CPU</a></p></body></html>'''
(HERE / 'pilot.html').write_text(page)
(HERE / 'pilot.html.txt').write_text(page)
final_cpu = time.process_time()
terminal = {'status': result['status'], 'all_processes_terminal': True, 'running': False,
            'actual_process_CPU_seconds': final_cpu, 'conservative_preparation_charge_seconds': PREP,
            'cumulative_charged_CPU_seconds': final_cpu+PREP, 'CPU_budget_seconds': BUDGET,
            'traffic_route_BFS_total': 32, 'old_allroot_validity_BFS': 0,
            'new_graph_parameter_Lean_increment': [0, 0, 0], 'no_automatic_continuation': True}
dump('TERMINAL.json', terminal)
dump('HANDLE.json', {'pid': os.getpid(), 'running': False, 'status': result['status'],
                     'cumulative_charged_CPU_seconds': final_cpu+PREP, 'CPU_budget_seconds': BUDGET})
print(json.dumps({'ports': port_delta, 'baseline': {k:v for k,v in before.items() if k!='sample_target_expansion_counts'},
                  'failure': {k:v for k,v in after.items() if k!='sample_target_expansion_counts'},
                  'changes': changes, 'terminal': terminal}, ensure_ascii=False, indent=2))

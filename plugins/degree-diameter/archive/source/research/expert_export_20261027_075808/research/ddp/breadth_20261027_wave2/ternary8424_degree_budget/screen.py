from pathlib import Path
from collections import deque, Counter
import json,time,sys

P=Path(__file__).resolve().parent
ROOT=P.parents[3]
t0=time.process_time()
source=P.parent/'sources/bhakar104.edges'
raw=[tuple(map(int,s.split())) for s in source.read_text().splitlines() if s.strip() and not s.startswith('#')]
assert raw[0]==(104,208)
edges=raw[1:];assert len(set(edges))==len(edges)==208
adj=[[] for _ in range(104)];edge_id={}
for i,(u,v) in enumerate(edges):
    assert 0<=u<v<104
    adj[u].append(v);adj[v].append(u);edge_id[u,v]=edge_id[v,u]=i
assert [len(x) for x in adj]==[4]*104
forced=set();forced_witness={};unique4=[];unique3=[];raw_paths=0
for root in range(104):
    dist=[-1]*104;dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    assert max(dist)==4 and -1 not in dist
    by_target=[[] for _ in range(104)]
    def walk(path):
        global raw_paths
        by_target[path[-1]].append(path)
        raw_paths+=1
        if len(path)==5:return
        for v in adj[path[-1]]:walk(path+[v])
    walk([root])
    for target in range(104):
        paths=by_target[target]
        if dist[target]==4:
            assert all(len(w)==5 for w in paths)
            if len(paths)==1:
                w=paths[0];ids=[edge_id[u,v] for u,v in zip(w,w[1:])]
                record=dict(root=root,target=target,path=w,source_edge_ids=ids)
                unique4.append(record)
                for eid in ids:
                    forced.add(eid)
                    forced_witness.setdefault(eid,record)
        if dist[target]==3:
            # A unique shortest three-step path alone is insufficient:
            # also require no additional four-cross-edge path.
            three=[w for w in paths if len(w)==4]
            four=[w for w in paths if len(w)==5]
            if len(three)==1 and not four:
                unique3.append(dict(root=root,target=target,path=three[0],three_step_paths=1,four_step_paths=0))

incident_forced=[sum(edge_id[u,v] in forced for v in adj[u]) for u in range(104)]
zero_internal=[u for u,k in enumerate(incident_forced) if k==4]
witness=next((w for w in unique3 if all(u in zero_internal for u in w['path'])),None)
cpu=time.process_time()-t0
assert cpu<2
result=dict(status='COMPLETE_UNIQUE_ROUTE_DEGREE_BUDGET_SCREEN',n=8424,fiber_size=81,branch_cap=3,degree_cap=12,target_D=4,source=str(source.relative_to(ROOT)),source_vertices=104,source_edges=208,source_diameter=4,unique_distance4_ordered_slots=len(unique4),forced_edge_count=len(forced),all_edges_forced=len(forced)==208,forced_edge_ids=sorted(forced),forced_edge_witnesses=[dict(edge_id=i,**forced_witness[i]) for i in sorted(forced)],forced_incident_degree_histogram=dict(sorted(Counter(incident_forced).items())),zero_internal_budget_vertices=zero_internal,unique_three_step_no_four_step_ordered_slots=len(unique3),closing_witness=witness,template_excluded=witness is not None,proof_if_closed='Unique control-distance-four routes force all their branch counts to3 to reach81 points. Four forced incident edges consume all12 degree, leaving no internal neighbor. A controller pair with exactly one three-step route and no four-step route, whose four route vertices all have zero internal budget, reaches at most3^3=27 of81 points in four graph steps.',not_claimed='A unique shortest three-step route by itself is not an obstruction if other four-step cross routes exist. No unrestricted lift, higher branch cap, or different controller is excluded.',raw_controller_walks_through_length4=raw_paths,control_BFS_roots=104,new_lift_graphs_generated=0,lift_BFS_roots=0,CPU_seconds=cpu,CPU_budget_seconds=2,pending=[])
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# 8424点三元纤维：度预算必要条件','','## 准确范围','','固定控制图为 sources/bhakar104.edges：104点四正则、直径四。每点换81点纤维（拟用F3^4），每条控制边的双向关系每点至多3个跨邻点；允许任意内部邻接，但每个顶点全部跨边与内部边合计度数至多12。点数104×81=8424，目标直径四，超过保存5832门槛。此任务只侦察必要度预算，不生成8424点图或搜索关系参数。','','## 唯一四步路的强迫','','若控制距离为四且只有一条四步控制路，则提升图的四步路必须全部走这四条控制边，不能消耗一步内部邻接。每步至多3分支，总共至多3^4=81端点。要覆盖目标纤维81点，四条边必须达到满3分支。对通常每控制边具有固定关系基数r_e的设置，这直接给出每边r_e=3。即使仅假定双向每点分支上界3，覆盖全部81×81源目标对也使路径每层的全部度数上界饱和：每个中间纤维顶点的前缀入路数至多3^k，而全部前缀数达到81×3^k，故每个顶点参与且对应跨度数都是3。','','将所有这种唯一四路上的边标记forced。如果一个控制顶点的四条基边都forced，其纤维每个顶点已用满4×3=12个跨邻点，内部度预算为零。','','## 实测结果','',f"唯一四步有序槽：{len(unique4)}；forced基边：{len(forced)}/208；内部预算为零的控制顶点：{len(zero_internal)}/104。",'',f"控制距离三、恰一条三步路且没有四步控制路的有序槽：{len(unique3)}。本程序枚举全部长度至多四的控制walk，包括立即往返；没有把唯一最短路偷换成唯一可用路。"]
if witness:
    lines+=['',f"**该准确模板被关闭。** 见证控制点对{witness['root']}→{witness['target']}，唯一可用跨路为"+'–'.join(map(str,witness['path']))+'。这条路上四个纤维的内部预算均为零；没有任何四步跨路。因此总长至多四只能使用这三条跨边，最多3^3=27个目标端点，小于81。继续在此范围内安排内部边或线方向无法补救。']
else:
    lines+=['','没有找到满足上述全部条件的关闭见证。这仅说明该便宜判据未关闭入口，不是存在性证据；保留forced边与剩余度预算条件，不继续随机分配。']
lines+=['','## 成本与边界','',f'本计算{cpu:.9f} CPU秒，低于2秒；104根已有控制图BFS及全部短walk枚举，0个新提升图、0个提升图BFS。RESULT.json保存全部forced边的唯一四路见证及关闭见证（若有）。不扩大branch cap3、不换控制图，不排除一般8424点图、非控制图模型或更大关系分支。']
text='\n'.join(lines)+'\n';sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
assert not screen(text),screen(text)
(P/'REPORT.md').write_text(text)
print(json.dumps({k:result[k] for k in ['status','unique_distance4_ordered_slots','forced_edge_count','all_edges_forced','unique_three_step_no_four_step_ordered_slots','closing_witness','template_excluded','CPU_seconds']}))

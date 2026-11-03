#!/usr/bin/env python3
"""Group the already saved independent root distances; no reachability/BFS recomputation."""
from pathlib import Path
import collections
import json
import time

base=Path(__file__).resolve().parent
start=time.process_time()
path=base.parent/'affine_cayley820_capacity/profile.best.independent_check.json'
saved=json.loads(path.read_text());dist=saved['root_0_distances']
assert len(dist)==820 and max(dist)==4
rows=[]
for j in range(20):
    fields=[x for x in range(41) if dist[x+41*j]>3]
    rows.append({'phase':j,'covered_within_3':41-len(fields),'distance4_count':len(fields),'distance4_fields':fields,'distance4_vertex_labels':[x+41*j for x in fields]})
assert sum(row['distance4_count'] for row in rows)==34
data={'source':'../affine_cayley820_capacity/profile.best.independent_check.json','read_saved_root_distances':True,'new_candidate_graphs':0,'new_BFS_runs':0,'new_reachability_enumerations':0,'encoding':'x+41*j','root_0_missing':34,'covered_within_3':786,'phases_with_missing':[row['phase'] for row in rows if row['distance4_count']],'phase_rows':rows,'CPU_seconds':time.process_time()-start}
(base/'phase_diagnosis.json').write_text(json.dumps(data,indent=2)+'\n')
report=(base/'REPORT.md').read_text()
section='''## 已保存最佳图的相位缺失分布

以下仅重分组前序独立验收文件中已保存的820项 `root_0_distances`，没有重新BFS、没有三步可达集合枚举，也没有新增候选。每个C20相位含41点；完整34个距离4顶点的field及顶点标签保存在 [phase_diagnosis.json](phase_diagnosis.json)。

| C20相位 | 三步以内覆盖 | 距离4缺失 | 缺失field坐标 |
|---:|---:|---:|---|
'''
for row in rows:
    section+=f"| {row['phase']} | {row['covered_within_3']} | {row['distance4_count']} | {', '.join(map(str,row['distance4_fields'])) or '—'} |\n"
missing=[row for row in rows if row['distance4_count']]
peak=max(row['distance4_count'] for row in rows)
section+=f"\n缺失分布在{len(missing)}个相位，单相位最大缺失{peak}。这里仅描述实际瓶颈位置，不据此推断其他field赋值不可能覆盖；本次固定下降轨迹已停止。分组读取CPU {data['CPU_seconds']:.6f}秒。\n\n"
report=report.replace('## CPU、源码与停止范围\n',section+'## CPU、源码与停止范围\n')
(base/'REPORT.md').write_text(report)
print(json.dumps(data,indent=2))

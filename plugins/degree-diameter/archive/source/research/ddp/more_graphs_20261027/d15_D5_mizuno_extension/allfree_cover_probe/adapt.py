"""Literal parameter adaptation of the frozen D14 probe; does not run that probe."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
OLD=P.parents[1]/'d14_D5_mizuno_extension/allfree_cover_probe'
s=(OLD/'probe.cpp').read_text()
replacements=[
 ('const int N=94186','const int N=100132'),
 ('edges.reserve(657452)','edges.reserve(749732)'),
 ('source94186.edges','source100132.edges'),
 ('assert(edges.size()==657452);vector<int>free,low,index(N,-1);','assert(edges.size()==749732);vector<int>free,cached,index(N,-1);'),
 ('for(int v=0;v<N;v++){assert(g[v].size()<=14);if(g[v].size()<14){index[v]=free.size();free.push_back(v);}if(g[v].size()==12)low.push_back(v);}',
  'for(int v=0;v<N;v++){assert(g[v].size()<=15);if(g[v].size()<15){index[v]=free.size();free.push_back(v);}}'),
 ('const int K=free.size();assert(K==3685&&low.size()==15);',
  'ifstream cr(out+"/cache_roots.txt");for(int v;cr>>v;)cached.push_back(v);const int K=free.size();assert(K==2498&&cached.size()==20);'),
 ('rare15_R4.u64le.bin','first20_R4.u64le.bin'),
 ('for(int v:low)','for(int v:cached)'),
 ('3670','2478'),
 ('old15_balls_reused','old20_balls_reused'),
 ('old15_reused','old20_reused'),
 (r'old20_balls_reused\":15',r'old20_balls_reused\":20'),
 (r'old20_reused\":15',r'old20_reused\":20'),
 ('selected.size()==14','selected.size()==15'),
 ('graph_d14_D5_n94187.edges','graph_d15_D5_n100133.edges'),
 ('g[v].size()<14','g[v].size()<15'),
 ('row.size()<=14','row.size()<=15'),
 ('COMPLETE94187_EXTENSION','COMPLETE100133_EXTENSION'),
]
for a,b in replacements:
 assert a in s,a
 s=s.replace(a,b)
(P/'probe.cpp').write_text(s)
r=json.loads((P.parent/'INTERFACE.json').read_text())
(P/'cache_roots.txt').write_text('\n'.join(map(str,r['cache_roots']))+'\n')
s=(OLD/'run.py').read_text()
for a,b in [('29.5-compiled','19.5-compiled'),('CPU_budget_seconds=30','CPU_budget_seconds=20'),('target_Delta=14','target_Delta=15'),('public_savedL=94186','public_savedL=100132'),('hypothetical_n=94187','hypothetical_n=100133'),('actual_n=94187','actual_n=100133'),('FROZEN_BEFORE_ALLFREE_BALLS','FROZEN_BEFORE_ALLFREE_CACHE_AND_CONSTRUCTION')]:
 assert a in s,a
 s=s.replace(a,b)
(P/'run.py').write_text(s)
print('D15 implementation ready; only the new literal source is scheduled.')

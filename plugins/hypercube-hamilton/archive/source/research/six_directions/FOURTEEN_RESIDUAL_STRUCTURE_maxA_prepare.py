from pathlib import Path
import json,itertools
P=Path(__file__).resolve().parent;j=json.loads((P/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text());maps=[[sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)] for p in itertools.permutations(range(5))]
seeds=json.loads((P/'TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json').read_text())['opening_cases'];rows=[]
for r in j['orbit_rows']:
 if not r['uncovered_by_FORCED'] or not r['maximal_A_B_options']:continue
 assert r['v']==31;opts=[]
 for op in r['maximal_A_B_options']:
  assert op['cut']==5
  for c,seed in enumerate(seeds):
   for pi,tr in enumerate(maps):
    q,b,t=map(tr.__getitem__,seed)
    if (t,b)!=(op['t'],op['b']):continue
    opts.append(dict(op,q=q,case=c,permutation=pi))
 raw=b''.join(bytes([o['q'],o['t'],o['w'],o['b'],o['case'],o['permutation']]) for o in opts)
 (P/f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_options_{r["index"]}.bin').write_bytes(raw)
 (P/f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_T_{r["index"]}.txt').write_text(' '.join(str(z^32) for z in r['Z']))
 rows.append({'orbit_index':r['index'],'Z':r['Z'],'W':r['W'],'options':opts})
print([(r['orbit_index'],len(r['options']),sorted({o['q'] for o in r['options']})) for r in rows]);(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_options.json').write_text(json.dumps(rows,indent=2)+'\n')
s=(P/'TWELVE_STAR_MAXIMAL_A_pilot.cpp').read_text();start=s.index(' vector<vector<int>>Ts=');end=s.index('\n fill(ei',start)
s=s[:start]+' ifstream tfile(dir+"/FOURTEEN_RESIDUAL_STRUCTURE_maxA_T_"+to_string(orbit)+".txt");int tx;while(tfile>>tx)T.push_back(tx);assert(T.size()==6);'+s[end:]
s=s.replace('TWELVE_STAR_MAXIMAL_A_pilot_','FOURTEEN_RESIDUAL_STRUCTURE_maxA_pilot_').replace('TWELVE_STAR_MAXIMAL_A_options_','FOURTEEN_RESIDUAL_STRUCTURE_maxA_options_')
s=s.replace('i<11','i<(int)O.size()').replace('>11-step','>int(O.size())-step').replace('step==11','step==(int)O.size()').replace('adj.resize(11);partner.assign(11,-2)','adj.resize(O.size());partner.assign(O.size(),-2)').replace('__builtin_popcount(unsigned(x))>=3','__builtin_popcount(unsigned(x))>=3&&x!=14')
s=s.replace('comp[2]','comp[5]').replace('casecounts{}','casecounts{}')
s=s.replace('array<U,2>casecounts','array<U,5>casecounts').replace('o.c==0?0:1','o.c')
s=s.replace('comp[which].size()==8031','comp[which].size()==(which==0||which==3?8031:7998)').replace('o.c==0||o.c==3','o.c>=0&&o.c<5')
start=s.index(' loadforests(dir+');end=s.index('\n cert.open',start)
s=s[:start]+''.join(f' loadforests(dir+"/TWELVE_ROOT_STAR_OPENING_case_{i:02}_forests.bin",{i},{q},{b},{t});\n' for i,(q,b,t) in enumerate(seeds))+s[end:]
(P/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_pilot.cpp').write_text(s)

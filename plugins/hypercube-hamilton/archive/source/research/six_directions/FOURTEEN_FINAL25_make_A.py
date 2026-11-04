from pathlib import Path
import json
P=Path(__file__).resolve().parent
o=json.loads((P/'FOURTEEN_FINAL25_options.json').read_text())
for z in o['orbits']:
 (P/f'FOURTEEN_FINAL25_options_{z["orbit"]}.bin').write_bytes(b''.join(bytes(x[k] for k in ['q','t','w','b','case','permutation_index']) for x in z['options']))
s=(P/'TWELVE_STAR_MAXIMAL_A_pilot.cpp').read_text()
s=s.replace('i<11','i<(int)O.size()').replace('>11-step','>(int)O.size()-step').replace('step==11','step==(int)O.size()').replace('adj.resize(11);partner.assign(11,-2);','adj.resize(O.size());partner.assign(O.size(),-2);')
a=s.index('vector<vector<int>>Ts=');b=s.index('fill(ei',a);s=s[:a]+'T={7,11,13,19,21,25};\n '+s[b:]
s=s.replace('else if(__builtin_popcount(unsigned(x))>=3)','else if(__builtin_popcount(unsigned(x))>=3 && (orbit==1 || x!=14))')
s=s.replace('void emit(U used,int size){','void emit(U used,int size){\n if(orbit==1 && !(used>>ei[30]&1))return;')
s=s.replace('TWELVE_STAR_MAXIMAL_A_options_','FOURTEEN_FINAL25_options_').replace('TWELVE_STAR_MAXIMAL_A_pilot_','FOURTEEN_FINAL25_A_')
(P/'FOURTEEN_FINAL25_A_search.cpp').write_text(s)

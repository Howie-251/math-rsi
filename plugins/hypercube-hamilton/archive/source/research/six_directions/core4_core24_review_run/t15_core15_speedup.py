from pathlib import Path
p=Path('t15_core15_residual.cpp');s=p.read_text()
s=s.replace('vector<pair<int,int>> route;','vector<pair<int,int>> route;unsigned neighborBlocks[32];')
s=s.replace('return __builtin_popcount(unsigned(a^b))==1;','unsigned d=a^b;return d&&!(d&(d-1));')
a=s.index(' for(int k=0;k<(int)blocks.size();++k)if(mask>>k&1u){');b=s.index('\n for(int k=0;k<(int)blocks.size();++k)if(mask>>k&1u){',a+10)
s=s[:a]+''' for(unsigned bits=mask;bits;bits&=bits-1){int k=__builtin_ctz(bits);
  for(int v:blocks[k])if(!shortedge(v,end)&&!shortedge(v,0)&&!(neighborBlocks[v]&mask&~(1u<<k))){dead.insert(key);return false;}
 }
'''+s[b:]
s=s.replace('for(int k=0;k<(int)blocks.size();++k)if(mask>>k&1u){','for(unsigned bits=mask&neighborBlocks[end];bits;bits&=bits-1){int k=__builtin_ctz(bits);')
s=s.replace('nodes=0;timeout=false;dead.clear();route={{0,0}};', 'for(int v=0;v<32;v++){neighborBlocks[v]=0;for(int k=0;k<int(blocks.size());k++)if(shortedge(v,blocks[k].front())||shortedge(v,blocks[k].back()))neighborBlocks[v]|=1u<<k;}nodes=0;timeout=false;dead.clear();route={{0,0}};')
Path('t15_core15_residual_fast.cpp').write_text(s)

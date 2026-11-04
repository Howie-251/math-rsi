from pathlib import Path
R=Path('.')
rows=[]
for line in (R/'t15_r3_small_core0_c1_failures.txt').read_text().splitlines():
 t=line.split();pi=t.index('ports');fi=t.index('F');rows.append(tuple(map(int,t[pi+1:fi]+t[fi+1:])))
assert len(rows)==len(set(rows))==6
(R/'t15_r3_small_core0_c1_B_inputs.txt').write_text('\n'.join(' '.join(map(str,r)) for r in rows)+'\n')
s=(R/'t15_core0_c2_residual.cpp').read_text().split('void solve(){')[0]
s=s.replace('// Exhaustive c2 residual: 24 B inputs times 62370 A inputs times two crossing bijections.','// Exact r3 c1 residual: 6 B inputs times 135135 A partials.').replace('int p,q;','int p;')
s+='''void solve(){
 vector<pair<int,int>> ar;
 for(int a=0;a<16;++a)if(am[a]>a)ar.emplace_back(2*a+1,2*am[a]+1);
 for(const auto& bc:bs){
  req=ar;for(auto [a,b]:bc.edges)req.emplace_back(2*a,2*b);
  req.emplace_back(2*ap+1,2*bc.p);
  blocks={{0},{7},{11},{14}};for(auto [a,b]:req)blocks.push_back({a,b});
  nodes=0;timeout=false;dead.clear();route={{0,0}};
  bool ok=dfs(0,((1u<<blocks.size())-1)&~1u);
  ++total;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);
  if(ok){++positive;for(auto [a,b]:req){out.put(char(a));out.put(char(b));}for(auto [k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int v:b)out.put(char(v));}}
  else{if(timeout)++unknown;else ++negative;fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED");for(auto [a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\\n';}
 }
}
void enumerate(unsigned mask){
 if(!mask){solve();return;}
 int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);am[a]=b;am[b]=a;enumerate(rest&~(1u<<b));am[a]=am[b]=-1;}
}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 ifstream in(argv[1]);BCase bc;
 while(in>>bc.p){for(auto& [a,b]:bc.edges)in>>a>>b;bs.push_back(bc);}
 if(bs.size()!=6)return 3;
 out.open(argv[2],ios::binary);fail.open(argv[3]);am.fill(-1);
 for(ap=1;ap<16;++ap)if(ap!=3&&ap!=5){
  enumerate(65534u&~(1u<<3)&~(1u<<5)&~(1u<<ap));
  cerr<<"port "<<ap<<" total="<<total<<" pos="<<positive<<" unknown="<<unknown<<" neg="<<negative<<'\\n';
 }
 cout<<"{\\"total\\":"<<total<<",\\"positive\\":"<<positive<<",\\"unknown\\":"<<unknown<<",\\"negative\\":"<<negative<<",\\"nodes\\":"<<totalNodes<<",\\"max_nodes\\":"<<maxNodes<<",\\"record_bytes\\":56}\\n";
}
'''
(R/'t15_r3_small_core0_c1_residual.cpp').write_text(s)

from pathlib import Path
R=Path(__file__).resolve().parent
for c,n in [(1,12),(3,1)]:
 rows=[]
 for line in (R/f't15_r3_small_core15_c{c}_B_exceptions.txt').read_text().splitlines():
  t=line.split();fi=t.index('F');rows.append(tuple(map(int,t[1:fi]+t[fi+1:])))
 assert len(rows)==len(set(rows))==n
 (R/f't15_core15_c{c}_B_inputs.txt').write_text('\n'.join(' '.join(map(str,t)) for t in rows)+'\n')
s=(R/'t15_r3_small_core0_c1_residual.cpp').read_text().split('void solve(){')[0]
s=s.replace('struct BCase{int p;array<pair<int,int>,6> edges;};','struct BCase{vector<int> ports;vector<pair<int,int>> edges;};').replace('int ap,aq;','int c;vector<int> ap;')
s+='''void solve(){
 vector<pair<int,int>> ar;for(int a=0;a<16;a++)if(am[a]>a)ar.emplace_back(2*a+1,2*am[a]+1);
 for(auto&bc:bs){auto bp=bc.ports;do{
  req=ar;for(auto[a,b]:bc.edges)req.emplace_back(2*a,2*b);for(int j=0;j<c;j++)req.emplace_back(2*ap[j]+1,2*bp[j]);
  blocks={{0},{21},{31},{14}};for(auto[a,b]:req)blocks.push_back({a,b});
  nodes=0;timeout=false;dead.clear();route={{0,0}};bool ok=dfs(0,((1u<<blocks.size())-1)&~1u);
  total++;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);
  if(ok){positive++;for(auto[a,b]:req){out.put(char(a));out.put(char(b));}for(auto[k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int v:b)out.put(char(v));}}
  else{if(timeout)unknown++;else negative++;fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED");for(auto[a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\\n';}
 }while(next_permutation(bp.begin(),bp.end()));}
}
void matchings(unsigned mask){if(!mask){solve();return;}int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);am[a]=b;am[b]=a;matchings(rest&~(1u<<b));am[a]=am[b]=-1;}}
void chooseports(vector<int>&base,int start,int n,unsigned mask){if(!n){matchings(mask);return;}for(int j=start;j<=int(base.size())-n;j++){int a=base[j];ap.push_back(a);chooseports(base,j+1,n-1,mask&~(1u<<a));ap.pop_back();}}
int main(int argc,char**argv){if(argc!=5)return 2;c=stoi(argv[1]);if(c!=1&&c!=3)return 3;
 ifstream in(argv[2]);int first;while(in>>first){BCase bc;bc.ports.push_back(first);for(int j=1;j<c;j++){int p;in>>p;bc.ports.push_back(p);}for(int j=0;j<(13-c)/2;j++){int a,b;in>>a>>b;bc.edges.emplace_back(a,b);}bs.push_back(bc);}if(bs.size()!=size_t(c==1?12:1))return 4;
 out.open(argv[3],ios::binary);fail.open(argv[4]);am.fill(-1);vector<int>base;for(int v=1;v<16;v++)if(v!=10&&v!=15)base.push_back(v);chooseports(base,0,c,65534u&~(1u<<10)&~(1u<<15));
 cout<<"{\\"c\\":"<<c<<",\\"total\\":"<<total<<",\\"positive\\":"<<positive<<",\\"unknown\\":"<<unknown<<",\\"negative\\":"<<negative<<",\\"nodes\\":"<<totalNodes<<",\\"max_nodes\\":"<<maxNodes<<",\\"record_bytes\\":56}\\n";}
'''
(R/'t15_core15_residual.cpp').write_text(s)

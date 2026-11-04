// Exhaustive zero-crossing residual: 18 B matchings times 11!! A matchings.
// Each positive emits 13 required edges followed by a 30-vertex cycle.
#include <array>
#include <vector>
#include <unordered_set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std;
array<int,16> am;
vector<array<pair<int,int>,7>> bs;
vector<pair<int,int>> req;
vector<vector<int>> blocks;
vector<pair<int,int>> route;
unordered_set<uint64_t> dead;
ofstream out,fail;
uint64_t nodes,totalNodes=0,cap=2000000,total=0,positive=0,unknown=0,negative=0,maxNodes=0;
bool timeout;
bool shortedge(int a,int b){return __builtin_popcount(unsigned(a^b))==1;}
bool dfs(int end,unsigned mask){
 if(++nodes>cap){timeout=true;return false;}
 if(!mask)return shortedge(end,0);
 uint64_t key=(uint64_t(mask)<<5)|unsigned(end);
 if(dead.count(key))return false;
 // Every remaining block needs two viable incidences among remaining endpoints,
 // the current endpoint and the root. This inexpensive necessary check matters.
 for(int k=0;k<(int)blocks.size();++k)if(mask>>k&1u){
  for(int v:blocks[k]){
   bool ok=shortedge(v,end)||shortedge(v,0);
   if(!ok)for(int l=0;l<(int)blocks.size();++l)if(l!=k&&(mask>>l&1u)){
    if(shortedge(v,blocks[l].front())||shortedge(v,blocks[l].back())){ok=true;break;}
   }
   if(!ok){dead.insert(key);return false;}
  }
 }
 for(int k=0;k<(int)blocks.size();++k)if(mask>>k&1u){
  for(int rev=0;rev<(blocks[k].size()==1?1:2);++rev){
   int entry=rev?blocks[k].back():blocks[k].front();
   if(!shortedge(end,entry))continue;
   int exit=rev?blocks[k].front():blocks[k].back();
   route.emplace_back(k,rev);
   if(dfs(exit,mask&~(1u<<k)))return true;
   route.pop_back();if(timeout)return false;
  }
 }
 dead.insert(key);return false;
}
void solve(){
 vector<pair<int,int>> ar;
 for(int a=0;a<16;++a)if(am[a]>a)ar.emplace_back(2*a+1,2*am[a]+1);
 for(int bi=0;bi<(int)bs.size();++bi){
  req=ar;for(auto [a,b]:bs[bi])req.emplace_back(2*a,2*b);
  blocks={{0},{7},{11},{13}};for(auto [a,b]:req)blocks.push_back({a,b});
  nodes=0;timeout=false;dead.clear();route={{0,0}};
  bool ok=dfs(0,((1u<<blocks.size())-1)&~1u);
  ++total;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);
  if(ok){
   ++positive;
   for(auto [a,b]:req){out.put(char(a));out.put(char(b));}
   for(auto [k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int v:b)out.put(char(v));}
  }else{
   if(timeout)++unknown;else ++negative;
   fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED");
   for(auto [a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\n';
  }
 }
 if(total%18711==0)cerr<<total<<" positive="<<positive<<" unknown="<<unknown<<" negative="<<negative<<'\n';
}
void enumerate(unsigned mask){
 if(!mask){solve();return;}
 int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);am[a]=b;am[b]=a;enumerate(rest&~(1u<<b));am[a]=am[b]=-1;}
}
int main(int argc,char**argv){
 if(argc!=4)return 2;
 ifstream in(argv[1]);array<pair<int,int>,7>b;
 while(in>>b[0].first>>b[0].second){for(int k=1;k<7;++k)in>>b[k].first>>b[k].second;bs.push_back(b);}
 if(bs.size()!=18)return 3;
 out.open(argv[2],ios::binary);fail.open(argv[3]);am.fill(-1);
 enumerate(65535u&~1u&~(1u<<3)&~(1u<<5)&~(1u<<6));
 cout<<"{\"total\":"<<total<<",\"positive\":"<<positive<<",\"unknown\":"<<unknown<<",\"negative\":"<<negative<<",\"nodes\":"<<totalNodes<<",\"max_nodes\":"<<maxNodes<<",\"record_bytes\":56}\n";
}

// Complete core15 residual input enumeration for c=1 and c=3, each with 1621620 cases.
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
struct BCase{vector<int> ports;vector<pair<int,int>> edges;};
vector<BCase> bs;
int c;vector<int> ap;
vector<pair<int,int>> req;
vector<vector<int>> blocks;
vector<pair<int,int>> route;unsigned neighborBlocks[32];
unordered_set<uint64_t> dead;
ofstream out,fail;
uint64_t nodes,totalNodes=0,cap=2000000,total=0,positive=0,unknown=0,negative=0,maxNodes=0;
bool timeout;
bool shortedge(int a,int b){unsigned d=a^b;return d&&!(d&(d-1));}
bool dfs(int end,unsigned mask){
 if(++nodes>cap){timeout=true;return false;}
 if(!mask)return shortedge(end,0);
 uint64_t key=(uint64_t(mask)<<5)|unsigned(end);
 if(dead.count(key))return false;
 // Every remaining block needs two viable incidences among remaining endpoints,
 // the current endpoint and the root. This inexpensive necessary check matters.
 for(unsigned bits=mask;bits;bits&=bits-1){int k=__builtin_ctz(bits);
  for(int v:blocks[k])if(!shortedge(v,end)&&!shortedge(v,0)&&!(neighborBlocks[v]&mask&~(1u<<k))){dead.insert(key);return false;}
 }

 for(unsigned bits=mask&neighborBlocks[end];bits;bits&=bits-1){int k=__builtin_ctz(bits);
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
 vector<pair<int,int>> ar;for(int a=0;a<16;a++)if(am[a]>a)ar.emplace_back(2*a+1,2*am[a]+1);
 for(auto&bc:bs){auto bp=bc.ports;do{
  req=ar;for(auto[a,b]:bc.edges)req.emplace_back(2*a,2*b);for(int j=0;j<c;j++)req.emplace_back(2*ap[j]+1,2*bp[j]);
  blocks={{0},{21},{31},{14}};for(auto[a,b]:req)blocks.push_back({a,b});
  for(int v=0;v<32;v++){neighborBlocks[v]=0;for(int k=0;k<int(blocks.size());k++)if(shortedge(v,blocks[k].front())||shortedge(v,blocks[k].back()))neighborBlocks[v]|=1u<<k;}nodes=0;timeout=false;dead.clear();route={{0,0}};bool ok=dfs(0,((1u<<blocks.size())-1)&~1u);
  total++;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);
  if(ok){positive++;for(auto[a,b]:req){out.put(char(a));out.put(char(b));}for(auto[k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int v:b)out.put(char(v));}}
  else{if(timeout)unknown++;else negative++;fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED");for(auto[a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\n';}
 }while(next_permutation(bp.begin(),bp.end()));}
}
void matchings(unsigned mask){if(!mask){solve();return;}int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);am[a]=b;am[b]=a;matchings(rest&~(1u<<b));am[a]=am[b]=-1;}}
void chooseports(vector<int>&base,int start,int n,unsigned mask){if(!n){matchings(mask);return;}for(int j=start;j<=int(base.size())-n;j++){int a=base[j];ap.push_back(a);chooseports(base,j+1,n-1,mask&~(1u<<a));ap.pop_back();}}
int main(int argc,char**argv){if(argc!=5)return 2;c=stoi(argv[1]);if(c!=1&&c!=3)return 3;
 ifstream in(argv[2]);int first;while(in>>first){BCase bc;bc.ports.push_back(first);for(int j=1;j<c;j++){int p;in>>p;bc.ports.push_back(p);}for(int j=0;j<(13-c)/2;j++){int a,b;in>>a>>b;bc.edges.emplace_back(a,b);}bs.push_back(bc);}if(bs.size()!=size_t(c==1?12:1))return 4;
 out.open(argv[3],ios::binary);fail.open(argv[4]);am.fill(-1);vector<int>base;for(int v=1;v<16;v++)if(v!=10&&v!=15)base.push_back(v);chooseports(base,0,c,65534u&~(1u<<10)&~(1u<<15));
 cout<<"{\"c\":"<<c<<",\"total\":"<<total<<",\"positive\":"<<positive<<",\"unknown\":"<<unknown<<",\"negative\":"<<negative<<",\"nodes\":"<<totalNodes<<",\"max_nodes\":"<<maxNodes<<",\"record_bytes\":56}\n";}

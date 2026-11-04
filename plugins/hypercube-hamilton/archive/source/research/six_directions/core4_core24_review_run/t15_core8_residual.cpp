// Generic core8 residual producer, with independently checkable positive records.
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
int crossing=1; vector<int> aports; uint64_t limit=0;
vector<BCase> bs;
int ap,aq;
vector<pair<int,int>> req;
vector<vector<int>> blocks;
vector<pair<int,int>> route;
unordered_set<uint64_t> dead;
ofstream out,fail;
uint64_t nodes,totalNodes=0,cap=2000000,total=0,positive=0,unknown=0,negative=0,maxNodes=0;
bool timeout;

uint32_t memo[1<<22]{},epoch=0;
uint32_t neighbourBlocks[32]{};
uint64_t neighbourEntries[32]{};
int entry[34]{},exitv[34]{};
uint64_t allEntries;
bool shortedge(int a,int b){unsigned d=a^b;return d && !(d&(d-1));}
void prepare(){
 ++epoch;if(!epoch){fill(begin(memo),end(memo),0);++epoch;}
 fill(begin(neighbourBlocks),end(neighbourBlocks),0);fill(begin(neighbourEntries),end(neighbourEntries),0);allEntries=0;
 for(int k=0;k<(int)blocks.size();k++)for(int rev=0;rev<(blocks[k].size()==1?1:2);rev++){
  int id=2*k+rev;entry[id]=rev?blocks[k].back():blocks[k].front();exitv[id]=rev?blocks[k].front():blocks[k].back();
  allEntries|=1ull<<id;
  for(int v=0;v<32;v++)if(shortedge(v,entry[id]))neighbourEntries[v]|=1ull<<id;
 }
 for(int v=0;v<32;v++)for(int k=0;k<(int)blocks.size();k++)if(shortedge(v,blocks[k].front())||shortedge(v,blocks[k].back()))neighbourBlocks[v]|=1u<<k;
}
bool fastdfs(int end,unsigned mask,uint64_t options){
 if(++nodes>cap){timeout=true;return false;}
 if(!mask)return shortedge(end,0);
 unsigned key=(mask<<5)|unsigned(end);if(memo[key]==epoch)return false;
 for(unsigned bits=mask;bits;bits&=bits-1){int k=__builtin_ctz(bits);unsigned others=mask&~(1u<<k);
  for(int v:blocks[k])if(!(neighbourBlocks[v]&others)&&!shortedge(v,end)&&!shortedge(v,0)){memo[key]=epoch;return false;}
 }
 for(uint64_t choices=neighbourEntries[end]&options;choices;choices&=choices-1){int id=__builtin_ctzll(choices),k=id/2;route.emplace_back(k,id%2);
  if(fastdfs(exitv[id],mask&~(1u<<k),options&~(3ull<<(2*k))))return true;
  route.pop_back();if(timeout)return false;
 }
 memo[key]=epoch;return false;
}
void solve(){
 vector<pair<int,int>> ar;
 for(int a=0;a<16;++a)if(am[a]>a)ar.emplace_back(2*a+1,2*am[a]+1);
 for(const auto& bc:bs){ auto bp=bc.ports; do{
  req=ar;for(auto [a,b]:bc.edges)req.emplace_back(2*a,2*b);
  for(int j=0;j<crossing;j++)req.emplace_back(2*aports[j]+1,2*bp[j]);
  blocks={{0},{7},{14},{31}};for(auto [a,b]:req)blocks.push_back({a,b});
  nodes=0;timeout=false;dead.clear();route={{0,0}};
  prepare();bool ok=fastdfs(0,((1u<<blocks.size())-1)&~1u,allEntries&~3ull);
  ++total;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);
  if(ok){++positive;for(auto [a,b]:req){out.put(char(a));out.put(char(b));}for(auto [k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int v:b)out.put(char(v));}}
  else{if(timeout)++unknown;else ++negative;fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED");for(auto [a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\n';}
 if(limit && total>=limit) return;
 }while(next_permutation(bp.begin(),bp.end()));
 }
}

void enumerate(unsigned mask,int skips){
 if(limit && total>=limit)return;
 if(!mask){if(!skips){aports.clear();for(int v=0;v<16;v++)if(v!=0&&v!=3&&v!=15&&am[v]<0)aports.push_back(v);solve();}return;}
 if(__builtin_popcount(mask)<skips)return;
 int a=__builtin_ctz(mask);unsigned rest=mask&~(1u<<a);
 if(skips)enumerate(rest,skips-1);
 for(unsigned bits=rest;bits;bits&=bits-1){int b=__builtin_ctz(bits);am[a]=b;am[b]=a;enumerate(rest&~(1u<<b),skips);am[a]=am[b]=-1;}
}
int main(int argc,char**argv){
 if(argc<5)return 2;crossing=stoi(argv[1]);limit=argc>5?stoull(argv[5]):0;
 ifstream in(argv[2]);int count;in>>count;
 for(int k=0;k<count;k++){BCase b;for(int j=0;j<crossing;j++){int p;in>>p;b.ports.push_back(p);}for(int j=0;j<(13-crossing)/2;j++){int a,z;in>>a>>z;b.edges.emplace_back(a,z);}bs.push_back(b);}
 if(!in)return 3;
 out.open(argv[3],ios::binary);fail.open(argv[4]);am.fill(-1);
 cap=2000000;enumerate(65535u&~1u&~(1u<<3)&~(1u<<15),crossing);
 cout<<"{\"c\":"<<crossing<<",\"B_cases\":"<<bs.size()<<",\"total\":"<<total<<",\"positive\":"<<positive<<",\"unknown\":"<<unknown<<",\"negative\":"<<negative<<",\"nodes\":"<<totalNodes<<",\"max_nodes\":"<<maxNodes<<",\"record_bytes\":56}\n";
}


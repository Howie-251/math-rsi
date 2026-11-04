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
int xhole,rhole,shole,yhole;
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
int main(int argc,char**argv){if(argc!=4)return 2;ifstream in(argv[1],ios::binary);out.open(argv[2],ios::binary);fail.open(argv[3]);unsigned char raw[26];while(in.read((char*)raw,26)){req.clear();for(int j=0;j<26;j+=2)req.emplace_back(raw[j],raw[j+1]);blocks={{0},{13},{21},{31}};for(auto[a,b]:req)blocks.push_back({a,b});nodes=0;timeout=false;route={{0,0}};prepare();bool ok=fastdfs(0,((1u<<blocks.size())-1)&~1u,allEntries&~3ull);total++;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);if(ok){positive++;out.write((char*)raw,26);for(auto[k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int v:b)out.put(char(v));}}else{if(timeout)unknown++;else negative++;fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED")<<'\n';}}cout<<"{\"total\":"<<total<<",\"positive\":"<<positive<<",\"unknown\":"<<unknown<<",\"negative\":"<<negative<<",\"nodes\":"<<totalNodes<<",\"max_nodes\":"<<maxNodes<<"}\n";}
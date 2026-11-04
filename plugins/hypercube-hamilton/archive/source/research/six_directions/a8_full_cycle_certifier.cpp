// Positive-certificate producer for arbitrary 12-edge K(Q5) matchings.
// Input24 bytes=edge pairs; output55 bytes=input plus a 31-cycle omitting argv4.
// Failure/timeout is only a diagnostic, never an A8 counterexample certificate.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> blocks;
vector<pair<int,int>> route;
uint32_t memo[1<<24]{},epoch=0,neighbor_blocks[32]{};
uint64_t neighbor_entries[32]{},all_entries;
int entry_v[64]{},exit_v[64]{},start_v;
uint64_t nodes,cap=2000000,total_nodes=0,max_nodes=0;bool timeout;
bool shortedge(int a,int b){unsigned x=a^b;return x&&!(x&(x-1));}
void prepare(){
 ++epoch;if(!epoch){fill(begin(memo),end(memo),0);++epoch;}
 fill(begin(neighbor_blocks),end(neighbor_blocks),0);fill(begin(neighbor_entries),end(neighbor_entries),0);all_entries=0;
 for(int k=0;k<int(blocks.size());k++)for(int r=0;r<(blocks[k].size()==1?1:2);r++){
  int id=2*k+r;entry_v[id]=r?blocks[k].back():blocks[k].front();exit_v[id]=r?blocks[k].front():blocks[k].back();all_entries|=1ull<<id;
  for(int v=0;v<32;v++)if(shortedge(v,entry_v[id]))neighbor_entries[v]|=1ull<<id;
 }
 for(int v=0;v<32;v++)for(int k=0;k<int(blocks.size());k++)if(shortedge(v,blocks[k].front())||shortedge(v,blocks[k].back()))neighbor_blocks[v]|=1u<<k;
}
bool dfs(int end,unsigned mask,uint64_t options){
 if(++nodes>cap){timeout=true;return false;}
 if(!mask)return shortedge(end,start_v);
 unsigned key=(mask<<5)|unsigned(end);assert(key<(1u<<24));if(memo[key]==epoch)return false;
 for(unsigned bits=mask;bits;bits&=bits-1){int k=__builtin_ctz(bits);unsigned others=mask&~(1u<<k);
  for(int v:blocks[k])if(!(neighbor_blocks[v]&others)&&!shortedge(v,end)&&!shortedge(v,start_v)){memo[key]=epoch;return false;}
 }
 for(uint64_t bits=neighbor_entries[end]&options;bits;bits&=bits-1){
  int id=__builtin_ctzll(bits),k=id/2;route.emplace_back(k,id%2);
  if(dfs(exit_v[id],mask&~(1u<<k),options&~(3ull<<(2*k))))return true;
  route.pop_back();if(timeout)return false;
 }
 memo[key]=epoch;return false;
}
int main(int argc,char**argv){
 if(argc<5)return 2;int omit=stoi(argv[4]);assert(omit>=0&&omit<32);
 uint64_t limit=argc>5?stoull(argv[5]):0;if(argc>6)cap=stoull(argv[6]);
 ifstream in(argv[1],ios::binary);ofstream out(argv[2],ios::binary),fail(argv[3]);assert(in&&out&&fail);
 unsigned char record[24];uint64_t total=0,positive=0,unknown=0,exhausted=0;
 while((!limit||total<limit)&&in.read(reinterpret_cast<char*>(record),24)){
  uint32_t used=0;vector<pair<int,int>> req;
  for(int j=0;j<24;j+=2){int a=record[j],b=record[j+1];assert(a<32&&b<32&&a!=b&&!(used>>a&1)&&!(used>>b&1));used|=(1u<<a)|(1u<<b);req.emplace_back(a,b);}
  assert(!(used>>omit&1));blocks.clear();
  for(int v=0;v<32;v++)if(v!=omit&&!(used>>v&1))blocks.push_back({v});
  assert(blocks.size()==7);start_v=blocks[0][0];for(auto [a,b]:req)blocks.push_back({a,b});assert(blocks.size()==19);
  nodes=0;timeout=false;route={{0,0}};prepare();
  bool ok=dfs(start_v,((1u<<blocks.size())-1)&~1u,all_entries&~3ull);
  ++total;total_nodes+=nodes;max_nodes=max(max_nodes,nodes);
  if(ok){++positive;out.write(reinterpret_cast<char*>(record),24);for(auto[k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int x:b)out.put(char(x));}}
  else{if(timeout)++unknown;else++exhausted;fail<<total-1<<' '<<(timeout?"UNKNOWN":"SEARCH_EXHAUSTED");for(auto[a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\n';}
  if(total%10000==0)cerr<<"checked="<<total<<" positive="<<positive<<" unknown="<<unknown<<" exhausted="<<exhausted<<'\n';
 }
 if(!limit)assert(in.eof()&&in.gcount()==0);
 cout<<"{\"total\":"<<total<<",\"positive\":"<<positive<<",\"unknown\":"<<unknown<<",\"search_exhausted\":"<<exhausted<<",\"nodes\":"<<total_nodes<<",\"max_nodes\":"<<max_nodes<<",\"record_bytes\":55,\"full_a8_proved\":false}\n";
}

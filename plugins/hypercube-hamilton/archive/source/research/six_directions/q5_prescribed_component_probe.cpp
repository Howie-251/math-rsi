// Exact component-contraction search, with explicit UNKNOWN on node cap.
// Each required component must be a path; all connecting edges are Q5 edges.
#include <array>
#include <vector>
#include <unordered_set>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdint>
using namespace std;
vector<vector<int>> blocks; vector<pair<int,int>> route;
unordered_set<uint64_t> dead;
uint64_t nodes, cap=2000000; bool timeout;
int startVertex;
bool shortedge(int a,int b){return __builtin_popcount(unsigned(a^b))==1;}
bool dfs(int end,unsigned mask){
 if(++nodes>cap){timeout=true;return false;}
 if(!mask)return shortedge(end,startVertex);
 uint64_t key=(uint64_t(mask)<<5)|unsigned(end);
 if(dead.count(key))return false;
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
int main(int argc,char**argv){
 if(argc<2)return 2;if(argc>2)cap=stoull(argv[2]);ifstream in(argv[1]);
 int id,omitted,m;bool sep=false;cout<<"[";
 while(in>>id>>omitted>>m){
  array<vector<int>,32> adj;bool valid=true;
  for(int i=0;i<m;++i){int a,b;in>>a>>b;if(a==b||a==omitted||b==omitted)valid=false;adj[a].push_back(b);adj[b].push_back(a);}
  for(auto& a:adj)if(a.size()>2)valid=false;
  array<bool,32> seen{};seen[omitted]=true;blocks.clear();
  if(valid)for(int x=0;x<32;++x)if(!seen[x]&&adj[x].size()<=1){
   vector<int> block;int prev=-1,cur=x;
   while(cur>=0){if(seen[cur]){valid=false;break;}seen[cur]=true;block.push_back(cur);int next=-1;for(int y:adj[cur])if(y!=prev)next=y;prev=cur;cur=next;}
   blocks.push_back(block);
  }
  for(bool b:seen)if(!b)valid=false;
  if(!valid)return 3;
  // The cycle can be reversed to fix either orientation of its first block.
  int root=0;for(int k=0;k<(int)blocks.size();++k)if(find(blocks[k].begin(),blocks[k].end(),0)!=blocks[k].end())root=k;
  startVertex=blocks[root].front();nodes=0;timeout=false;dead.clear();route={{root,0}};
  bool ok=dfs(blocks[root].back(),((1u<<blocks.size())-1)&~(1u<<root));
  if(sep)cout<<",";sep=true;
  cout<<"{\"id\":"<<id<<",\"status\":\""<<(ok?"FOUND":timeout?"UNKNOWN":"EXHAUSTED_NO_CYCLE")<<"\",\"nodes\":"<<nodes<<",\"dead_states\":"<<dead.size()<<",\"cycle\":[";
  bool cs=false;if(ok)for(auto [k,rev]:route){auto b=blocks[k];if(rev)reverse(b.begin(),b.end());for(int x:b){if(cs)cout<<",";cs=true;cout<<x;}}
  cout<<"]}"<<flush;
 }
 cout<<"]\n";
}

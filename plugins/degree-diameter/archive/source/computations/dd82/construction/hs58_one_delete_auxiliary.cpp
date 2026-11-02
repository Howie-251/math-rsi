// Four necessary auxiliary domains for HS58, with one shared ten-CPU-second cap.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using Edge=std::pair<int,int>;
std::array<Edge,28>edges;
std::array<unsigned,8>adj{};
std::array<int,8>degree{},cap{};
std::array<unsigned,8>allowed{};
clock_t began;bool timeout=false;long long totalnodes=0;
struct Result{int m,overlap,target;bool started=false,complete=false;long long nodes=0,leaves=0,survivors=0;double cpu=0;std::array<int,8>caps;std::vector<uint32_t>examples;};
constexpr int sample_limit=100;
bool accepted(){
 for(int u=0;u<8;u++){
  unsigned reach=(1U<<u)|adj[u],todo=adj[u];
  while(todo){int v=__builtin_ctz(todo);todo&=todo-1;reach|=adj[v];}
  if((255U&~reach)&~allowed[u])return false;
 }
 return true;
}
void visit(int pos,int need,uint32_t mask,Result&r){
 if(timeout)return;
 r.nodes++;totalnodes++;
 if((totalnodes&4095)==0 && double(clock()-began)/CLOCKS_PER_SEC>=10){timeout=true;return;}
 if(need==0){r.leaves++;if(accepted()){r.survivors++;if(r.examples.size()<sample_limit)r.examples.push_back(mask);}return;}
 if(28-pos<need)return;
 auto [u,v]=edges[pos];
 if(degree[u]<cap[u]&&degree[v]<cap[v]){
  degree[u]++;degree[v]++;adj[u]|=1U<<v;adj[v]|=1U<<u;
  visit(pos+1,need-1,mask|(1U<<pos),r);
  adj[u]^=1U<<v;adj[v]^=1U<<u;degree[u]--;degree[v]--;
 }
 visit(pos+1,need,mask,r);
}
int main(int argc,char**argv){
 assert(argc==2);int k=0;for(int u=0;u<8;u++)for(int v=u+1;v<8;v++)edges[k++]={u,v};
 began=clock();std::vector<Result>results;
 for(int m:{4,5})for(int overlap:{2,1}){
  Result r;r.m=m;r.overlap=overlap;r.target=6+m;std::array<bool,8>U{},V{};U[0]=U[1]=true;V[0]=true;V[overlap==2?1:2]=true;
  for(int u=0;u<8;u++)cap[u]=(U[u]&&V[u])?6:(U[u]||V[u])?7-m:8-m;
  r.caps=cap;adj.fill(0);degree.fill(0);allowed.fill(0);allowed[0]|=1U<<1;allowed[1]|=1U<<0;int w=overlap==2?1:2;allowed[0]|=1U<<w;allowed[w]|=1U<<0;
  if(!timeout){r.started=true;clock_t local=clock();visit(0,r.target,0,r);r.complete=!timeout;r.cpu=double(clock()-local)/CLOCKS_PER_SEC;}
  std::cout<<"m "<<m<<" overlap "<<overlap<<" started "<<r.started<<" complete "<<r.complete<<" degree-bounded graphs "<<r.leaves<<" survivors "<<r.survivors<<" CPU "<<r.cpu<<std::endl;
  results.push_back(r);
 }
 std::ofstream out(argv[1]);out<<"{\"scope\":\"Four labelled auxiliary necessary domains only; exact edge count, stated degree caps, and every bad pair contained in U or V\",\"n\":8,\"total_cpu_budget_seconds\":10,\"total_cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<",\"threads\":1,\"timed_out\":"<<(timeout?"true":"false")<<",\"total_backtracking_nodes\":"<<totalnodes<<",\"maximum_saved_survivors_per_case\":100,\"cases\":[";
 for(unsigned i=0;i<results.size();i++){
  if(i)out<<',';const auto&r=results[i];out<<"{\"m\":"<<r.m<<",\"U\":[0,1],\"V\":[0,"<<(r.overlap==2?1:2)<<"],\"intersection_size\":"<<r.overlap<<",\"edge_count\":"<<r.target<<",\"degree_upper_bounds\":[";
  for(int u=0;u<8;u++){if(u)out<<',';out<<r.caps[u];}out<<"],\"started\":"<<(r.started?"true":"false")<<",\"complete\":"<<(r.complete?"true":"false")<<",\"backtracking_nodes\":"<<r.nodes<<",\"degree_bounded_graphs_checked\":"<<r.leaves<<",\"survivor_count\":"<<r.survivors<<",\"all_survivors_saved\":"<<(r.survivors==static_cast<long long>(r.examples.size())?"true":"false")<<",\"cpu_seconds\":"<<r.cpu<<",\"saved_survivors\":[";
  for(unsigned j=0;j<r.examples.size();j++){if(j)out<<',';out<<"{\"edges\":[";bool comma=false;for(int e=0;e<28;e++)if(r.examples[j]>>e&1){if(comma)out<<',';comma=true;out<<'['<<edges[e].first<<','<<edges[e].second<<']';}out<<"]}";}out<<"]}";
 }
 out<<"]}\n";
}

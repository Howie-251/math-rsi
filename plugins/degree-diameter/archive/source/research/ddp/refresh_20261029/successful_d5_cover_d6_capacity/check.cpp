#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
struct Arc {int from,to;};
struct Spec {string label,path; int threshold;};
int main(){
 const clock_t started=clock();
 const vector<Spec> specs={
 {"d11_n37631","research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges",5},
 {"d12_n42402","research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges",9},
 {"d13_n51457","research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges",11}};
 cout<<"{\"sources\":[";
 bool first_source=true;
 for(const auto& s:specs){
  if(!first_source)cout<<","; first_source=false;
  ifstream in(s.path); int n,m; assert(in>>n>>m);
  vector<Arc> arcs; arcs.reserve(2*m); vector<int> degree(n);
  for(int i=0;i<m;i++){int u,v; assert(in>>u>>v); arcs.push_back({u,v}); arcs.push_back({v,u}); degree[u]++;degree[v]++;}
  const int minroot=min_element(degree.begin(),degree.end())-degree.begin();
  vector<int> roots; for(int r:{0,minroot,n-1}) if(find(roots.begin(),roots.end(),r)==roots.end())roots.push_back(r);
  cout<<"{\"label\":\""<<s.label<<"\",\"source\":\""<<s.path<<"\",\"n\":"<<n<<",\"m\":"<<m<<",\"kmin\":"<<s.threshold;
  cout<<",\"degree_min\":"<<degree[minroot]<<",\"degree_max\":"<<*max_element(degree.begin(),degree.end())<<",\"min_degree_first_label\":"<<minroot<<",\"requested_roots\":[";
  for(size_t j=0;j<roots.size();j++){if(j)cout<<",";cout<<roots[j];} cout<<"],\"roots\":[";
  bool failed=false, first_root=true;
  for(int root:roots){
   if(!first_root)cout<<","; first_root=false;
   array<vector<U>,7> count; for(auto& v:count)v.assign(n,0); count[0][root]=1;
   vector<U> current(arcs.size()),next(arcs.size()),totals(n),through5(n),through6(n);
   for(size_t a=0;a<arcs.size();a++) current[a]=(arcs[a].from==root);
   for(int len=1;len<=6;len++){
    fill(totals.begin(),totals.end(),0);
    for(size_t a=0;a<arcs.size();a++)totals[arcs[a].to]+=current[a];
    count[len]=totals;
    if(len<6){for(size_t a=0;a<arcs.size();a++){assert(totals[arcs[a].from]>=current[a^1]);next[a]=totals[arcs[a].from]-current[a^1];} current.swap(next);}
   }
   for(int v=0;v<n;v++){for(int l=0;l<=5;l++)through5[v]+=count[l][v];through6[v]=through5[v]+count[6][v];}
   const int w5=min_element(through5.begin(),through5.end())-through5.begin();
   const int w6=min_element(through6.begin(),through6.end())-through6.begin();
   size_t below6=0;for(U x:through6)below6+=(x<U(s.threshold));
   cout<<"{\"root\":"<<root<<",\"degree\":"<<degree[root]<<",\"minimum_through_5\":"<<through5[w5]<<",\"witness_through_5\":"<<w5;
   cout<<",\"minimum_through_6\":"<<through6[w6]<<",\"witness_through_6\":"<<w6<<",\"targets_below_kmin_through_6\":"<<below6;
   auto lengths=[&](const char* key,int v){cout<<",\""<<key<<"\":[";for(int l=0;l<=6;l++){if(l)cout<<",";cout<<count[l][v];}cout<<"]";};
   lengths("root_closed_by_exact_length",root); lengths("witness_5_by_exact_length",w5); lengths("witness_6_by_exact_length",w6);
   cout<<",\"root_closed_through_5\":"<<through5[root]<<",\"root_closed_through_6\":"<<through6[root];
   cout<<",\"total_walks_through_6\":"<<accumulate(through6.begin(),through6.end(),U(0))<<"}";
   if(below6){failed=true;break;}
  }
  cout<<"],\"status\":\""<<(failed?"ORDINARY_COVERS_AT_OR_ABOVE_KMIN_EXCLUDED":"NECESSARY_GATE_SUPPORTED")<<"\"}";
 }
 cout<<"],\"worker_cpu_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"graph_bfs_runs\":0,\"cover_graphs\":0,\"source_reads\":3}\n";
}

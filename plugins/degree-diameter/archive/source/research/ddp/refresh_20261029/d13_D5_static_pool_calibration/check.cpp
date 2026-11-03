#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int main(){
 const clock_t started=clock(); const int base_n=51417, added=40;
 const char* path="research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges";
 ifstream in(path);int n,m;assert(in>>n>>m);assert(n==base_n+added);
 vector<vector<int>> adj(base_n),S(added);vector<int> degree_final(n),usage(base_n);
 int old_edges=0,extra_edges=0,new_new=0;
 for(int e=0;e<m;e++){
  int u,v;assert(in>>u>>v);degree_final[u]++;degree_final[v]++;
  if(u<base_n&&v<base_n){adj[u].push_back(v);adj[v].push_back(u);old_edges++;}
  else if(u>=base_n&&v>=base_n)new_new++;
  else{if(u>=base_n)swap(u,v);S[v-base_n].push_back(u);usage[u]++;extra_edges++;}
 }
 assert(new_new==0);
 for(auto& a:S)sort(a.begin(),a.end());
 cout<<"{\"source\":\""<<path<<"\",\"final_n\":"<<n<<",\"final_m\":"<<m<<",\"base_n\":"<<base_n<<",\"base_m\":"<<old_edges<<",\"new_old_edges\":"<<extra_edges<<",\"new_new_edges\":"<<new_new;
 int used=0,overload=0;map<int,int> usage_hist;
 for(int v=0;v<base_n;v++)if(usage[v]){used++;usage_hist[usage[v]]++;overload+=(int(adj[v].size())+usage[v]>13);}
 cout<<",\"unique_used_ports\":"<<used<<",\"port_overloads\":"<<overload<<",\"final_max_degree\":"<<*max_element(degree_final.begin(),degree_final.end())<<",\"usage_histogram\":{";
 bool first=true;for(auto [k,c]:usage_hist){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":"<<c;}cout<<"},\"used_ports\":[";
 first=true;for(int v=0;v<base_n;v++)if(usage[v]){if(!first)cout<<",";first=false;cout<<"{\"vertex\":"<<v<<",\"usage\":"<<usage[v]<<",\"base_degree\":"<<adj[v].size()<<",\"base_spare\":"<<13-int(adj[v].size())<<"}";}cout<<"],\"sets\":[";
 array<array<int,40>,40> pd{}; int failed_sets=0;vector<int> dist(base_n),queue(base_n);
 for(int i=0;i<added;i++){
  fill(dist.begin(),dist.end(),-1);int begin=0,end=0;
  for(int v:S[i]){assert(dist[v]<0);dist[v]=0;queue[end++]=v;}
  while(begin<end){const int u=queue[begin++];if(dist[u]==4)continue;for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;queue[end++]=v;}}
  int missing=base_n-end,witness=-1;array<int,5> histogram{};
  for(int v=0;v<base_n;v++){if(dist[v]<0){if(witness<0)witness=v;}else histogram[dist[v]]++;}
  failed_sets+=(missing>0);
  for(int j=0;j<added;j++){int d=5;for(int v:S[j])if(dist[v]>=0)d=min(d,dist[v]);pd[i][j]=d;}
  if(i)cout<<",";cout<<"{\"new_vertex\":"<<base_n+i<<",\"neighbors\":[";
  for(size_t j=0;j<S[i].size();j++){if(j)cout<<",";cout<<S[i][j];}
  cout<<"],\"missing_B0_R4\":"<<missing<<",\"first_missing\":"<<witness<<",\"distance_histogram_0_to_4\":[";
  for(int d=0;d<5;d++){if(d)cout<<",";cout<<histogram[d];}cout<<"],\"set_distances_capped_at_5\":[";
  for(int j=0;j<added;j++){if(j)cout<<",";cout<<pd[i][j];}cout<<"]}";
 }
 int badpairs=0;map<int,int> pair_hist;
 for(int i=0;i<added;i++)for(int j=i+1;j<added;j++){assert(pd[i][j]==pd[j][i]);badpairs+=(pd[i][j]>3);pair_hist[pd[i][j]]++;}
 cout<<"],\"failed_sets\":"<<failed_sets<<",\"unordered_pair_count\":780,\"incompatible_pairs\":"<<badpairs<<",\"pair_distance_histogram\":{";
 first=true;for(auto [d,c]:pair_hist){if(!first)cout<<",";first=false;cout<<"\""<<d<<"\":"<<c;}
 cout<<"},\"source_reads\":1,\"multisource_radius4_runs\":40,\"source_diameter_BFS_runs\":0,\"new_graphs\":0,\"worker_cpu_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";
}

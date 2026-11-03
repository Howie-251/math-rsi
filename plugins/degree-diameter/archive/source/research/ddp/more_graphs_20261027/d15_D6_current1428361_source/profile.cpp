#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
constexpr int N=1428361,D=15;
void ints(ostream&out,const vector<int>&v){out<<'[';for(size_t i=0;i<v.size();i++){if(i)out<<',';out<<v[i];}out<<']';}
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit lim{10,10};setrlimit(RLIMIT_CPU,&lim);string folder=argv[2];
 ifstream input(argv[1]);assert(input);vector<vector<int>>adj(N);vector<int>seen(N);string line;int rows=0;
 while(getline(input,line)){
  if(line.empty()||line[0]=='#')continue;istringstream ss(line);int u,v;assert(ss>>u);assert(u>=0&&u<N&&!seen[u]);seen[u]=1;rows++;
  while(ss>>v){assert(v>=0&&v<N&&v!=u);adj[u].push_back(v);}
  sort(adj[u].begin(),adj[u].end());assert(adjacent_find(adj[u].begin(),adj[u].end())==adj[u].end());
 }
 assert(rows==N);array<int,D+1>hist{},satHist{};vector<int>free,sat(N),zero,one,minimum;long long arcs=0,slots=0;int maxdeg=0,minsat=D;
 for(int u=0;u<N;u++){
  int d=adj[u].size();assert(d<=D);hist[d]++;arcs+=d;maxdeg=max(maxdeg,d);if(d<D){free.push_back(u);slots+=D-d;}
  for(int v:adj[u])assert(binary_search(adj[v].begin(),adj[v].end(),u));
 }
 assert(arcs%2==0);
 for(int u=0;u<N;u++){
  for(int v:adj[u])sat[u]+=adj[v].size()==D;satHist[sat[u]]++;minsat=min(minsat,sat[u]);
  if(!sat[u])zero.push_back(u);if(sat[u]==1)one.push_back(u);
 }
 for(int u=0;u<N;u++)if(sat[u]==minsat)minimum.push_back(u);
 bool candidate=false;int prototype=-1;
 if(!zero.empty()){
  prototype=zero.front();assert(!adj[prototype].empty());for(int v:adj[prototype])assert(adj[v].size()<D);
  ofstream params(folder+"/CANDIDATE_PARAMETERS.json");
  params<<"{\"status\":\"COMPLETE_NEIGHBORHOOD_FALSE_TWIN_REQUIRES_PARENT_CHECK\",\"source_n\":"<<N<<",\"source_m\":"<<arcs/2<<",\"new_n\":"<<N+1<<",\"new_m\":"<<arcs/2+adj[prototype].size()<<",\"newlabel\":"<<N<<",\"prototype\":"<<prototype<<",\"pins\":";ints(params,adj[prototype]);params<<",\"old_pin_degrees\":[";
  for(size_t i=0;i<adj[prototype].size();i++){if(i)params<<',';params<<adj[adj[prototype][i]].size();}
  params<<"],\"source_reported_D\":6,\"new_D_upper\":6,\"source_BFS_roots\":0,\"new_root_BFS\":0}\n";
  ofstream edges(folder+"/graph_d15_D6_n1428362.edges");assert(edges);edges<<N+1<<' '<<arcs/2+adj[prototype].size()<<'\n';long long count=0;
  for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){edges<<u<<' '<<v<<'\n';count++;}
  for(int v:adj[prototype]){edges<<v<<' '<<N<<'\n';count++;}assert(count==arcs/2+adj[prototype].size());candidate=true;
 }
 ofstream out(folder+"/SOURCE_PROFILE.json");
 out<<"{\"status\":\"ACTUAL1428361_STRUCTURE_PROFILE_COMPLETE\",\"n\":"<<N<<",\"m\":"<<arcs/2<<",\"Delta\":"<<maxdeg<<",\"simple\":true,\"undirected\":true,\"degree_histogram\":{";
 bool comma=false;for(int d=0;d<=D;d++)if(hist[d]){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<hist[d];}
 out<<"},\"free_vertex_count\":"<<free.size()<<",\"free_slots\":"<<slots<<",\"minSatN\":"<<minsat<<",\"minSatN_count\":"<<minimum.size()<<",\"onefault_count\":"<<one.size()<<",\"zeroSatN_count\":"<<zero.size()<<",\"saturated_neighbor_histogram\":{";
 comma=false;for(int d=0;d<=D;d++)if(satHist[d]){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<satHist[d];}out<<"},\"free_vertices\":";ints(out,free);out<<",\"minSatN_first20\":[";
 for(size_t i=0;i<minimum.size()&&i<20;i++){if(i)out<<',';out<<minimum[i];}out<<"],\"onefault_vertices\":";ints(out,one);out<<",\"zeroSatN_vertices\":";ints(out,zero);
 out<<",\"source_reported_D\":6,\"actual_D\":null,\"ordinary_bad_unordered_pairs\":null,\"source_BFS_roots\":0,\"whole_neighborhood_candidate_exported\":"<<(candidate?"true":"false")<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"n="<<N<<" m="<<arcs/2<<" degree="<<maxdeg<<" free="<<free.size()<<" slots="<<slots<<" minSatN="<<minsat<<" zero="<<zero.size()<<" one="<<one.size()<<" candidate="<<candidate<<" nativeCPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

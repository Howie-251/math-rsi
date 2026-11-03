#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 const clock_t start=clock();const int N=102060;vector<vector<int>>adj(N);vector<int>seen(N);
 ifstream in(argv[1]);assert(in);string line;int rows=0;
 while(getline(in,line)){
  if(line.empty()||line[0]=='#')continue;
  istringstream ss(line);int u,v;assert(ss>>u);assert(u>=0&&u<N&&!seen[u]);seen[u]=1;rows++;
  while(ss>>v){assert(v>=0&&v<N&&v!=u);adj[u].push_back(v);}
  sort(adj[u].begin(),adj[u].end());assert(adjacent_find(adj[u].begin(),adj[u].end())==adj[u].end());
 }
 assert(rows==N);
 array<int,16>hist{},satHist{};vector<int>free,sat(N);long long arcs=0;int minSat=15,maxdegree=0,slots=0;
 for(int u=0;u<N;u++){
  const int d=adj[u].size();assert(d<=15);hist[d]++;arcs+=d;maxdegree=max(maxdegree,d);
  if(d<15){free.push_back(u);slots+=15-d;}
  for(int v:adj[u])assert(binary_search(adj[v].begin(),adj[v].end(),u));
 }
 vector<int>minprotos,onefault,zerofault;
 for(int u=0;u<N;u++){
  for(int v:adj[u])sat[u]+=adj[v].size()==15;
  satHist[sat[u]]++;minSat=min(minSat,sat[u]);
  if(sat[u]==0)zerofault.push_back(u);if(sat[u]==1)onefault.push_back(u);
 }
 for(int u=0;u<N;u++)if(sat[u]==minSat)minprotos.push_back(u);
 ofstream out(argv[2]);out<<"{\"status\":\"ACTUAL102060_STRUCTURE_PROFILE_COMPLETE\",\"n\":"<<N<<",\"m\":"<<arcs/2<<",\"Delta\":"<<maxdegree<<",\"simple\":true,\"undirected\":true,\"degree_histogram\":{";
 bool comma=false;for(int d=0;d<=15;d++)if(hist[d]){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<hist[d];}out<<"},\"free_vertex_count\":"<<free.size()<<",\"free_slots\":"<<slots<<",\"minSatN\":"<<minSat<<",\"minSatN_count\":"<<minprotos.size()<<",\"onefault_count\":"<<onefault.size()<<",\"zeroSatN_count\":"<<zerofault.size()<<",\"saturated_neighbor_histogram\":{";
 comma=false;for(int d=0;d<=15;d++)if(satHist[d]){if(comma)out<<',';comma=true;out<<'\"'<<d<<"\":"<<satHist[d];}out<<"},\"free_vertices\":[";
 for(size_t i=0;i<free.size();i++){if(i)out<<',';out<<free[i];}out<<"],\"minSatN_first20\":[";
 for(size_t i=0;i<minprotos.size()&&i<20;i++){if(i)out<<',';out<<minprotos[i];}out<<"],\"onefault_vertices\":[";
 for(size_t i=0;i<onefault.size();i++){if(i)out<<',';out<<onefault[i];}out<<"],\"source_reported_D\":5,\"actual_D\":null,\"ordinary_bad_unordered_pairs\":null,\"source_BFS_roots\":0,\"candidate_graphs\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"n "<<N<<" m "<<arcs/2<<" degree "<<maxdegree<<" free "<<free.size()<<" slots "<<slots<<" minSatN "<<minSat<<" onefault "<<onefault.size()<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

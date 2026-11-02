// One finite internal-Petersen assembly; external matching edges stay fixed.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using Graph=std::array<uint64_t,60>;
using Local=std::array<unsigned,10>;
Graph original;
int edge_index[10][10];
std::vector<std::pair<int,int>> local_edges;
std::vector<uint64_t> catalog;
std::vector<Local> local_catalog;
int match[6][6][10];
std::string out;
clock_t started;
Local decode(uint64_t mask){Local p{};for(int e=0;e<45;e++)if(mask>>e&1){auto [u,v]=local_edges[e];p[u]|=1U<<v;p[v]|=1U<<u;}return p;}
uint64_t local_mask(const Graph& g,int i){uint64_t mask=0;for(int e=0;e<45;e++){auto [u,v]=local_edges[e];if(g[10*i+u]>>(10*i+v)&1)mask|=1ULL<<e;}return mask;}
Graph replace(Graph g,int i,uint64_t mask){uint64_t fiber=1023ULL<<(10*i);for(int u=0;u<10;u++)g[10*i+u]&=~fiber;for(int e=0;e<45;e++)if(mask>>e&1){auto [u,v]=local_edges[e];g[10*i+u]|=1ULL<<(10*i+v);g[10*i+v]|=1ULL<<(10*i+u);}return g;}
std::pair<int,int> score(const Graph& g){int bad=0,energy=0;for(int u=0;u<60;u++)for(int v=u+1;v<60;v++){int r=__builtin_popcountll(g[u]&g[v])+int(g[u]>>v&1);bad+=r==0;energy+=(r-1)*(r-2)/2;}return {bad,energy};}
void save(const std::string& name,const Graph& g){auto [bad,e]=score(g);std::ofstream f(out+"/"+name+".json");f<<"{\"n\":60,\"bad_pairs\":"<<bad<<",\"energy\":"<<e<<",\"edges\":[";bool first=true;for(int u=0;u<60;u++){assert(__builtin_popcountll(g[u])==8);for(int v=u+1;v<60;v++)if(g[u]>>v&1){if(!first)f<<',';first=false;f<<'['<<u<<','<<v<<']';}}f<<"]}\n";std::ofstream edges(out+"/"+name+".edges");edges<<"60 240\n";for(int u=0;u<60;u++)for(int v=u+1;v<60;v++)if(g[u]>>v&1)edges<<u<<' '<<v<<'\n';}
struct Boundary {unsigned missing[2][10]{};int total=0;};
Boundary boundary(int i){Boundary b;for(int j=2;j<=3;j++)for(int u=0;u<10;u++){
  unsigned reached=1U<<match[i][j][u];int target=10*j+match[i][j][u];
  reached|=unsigned(original[target]>>(10*j))&1023U;
  for(int k=0;k<6;k++)if(k!=i&&k!=j)reached|=1U<<match[k][j][match[i][k][u]];
  unsigned miss=1023U&~reached;
  // Pull back target labels along Mij: P_i neighbors must contain these.
  for(int w=0;w<10;w++)if(miss>>match[i][j][w]&1)b.missing[j-2][u]|=1U<<w;
  b.total+=__builtin_popcount(b.missing[j-2][u]);
}return b;}
int boundary_bad(const Boundary& b,const Local& p){int n=0;for(int j=0;j<2;j++)for(int u=0;u<10;u++)n+=__builtin_popcount(b.missing[j][u]&~p[u]);return n;}
int main(int argc,char**argv){
  assert(argc==3);started=clock();out=argv[2];std::ifstream input(argv[1]);int n,m;input>>n>>m;assert(n==60&&m==240);
  for(int e=0,u,v;e<m;e++){input>>u>>v;original[u]|=1ULL<<v;original[v]|=1ULL<<u;}
  for(int u=0;u<10;u++)for(int v=u+1;v<10;v++){edge_index[u][v]=edge_index[v][u]=local_edges.size();local_edges.emplace_back(u,v);}
  for(int i=0;i<6;i++)for(int j=0;j<6;j++)if(i!=j)for(int u=0;u<10;u++){uint64_t row=(original[10*i+u]>>(10*j))&1023ULL;assert(__builtin_popcountll(row)==1);match[i][j][u]=__builtin_ctzll(row);}
  // One representative per labeled Petersen copy: root 0, ordered neighbors
  // of standard vertex 0, then the final pointwise-neighbor stabilizer.
  std::vector<std::pair<int,int>> standard={{0,1},{0,4},{0,5},{1,2},{1,6},{2,3},{2,7},{3,4},{3,8},{4,9},{5,7},{5,8},{6,8},{6,9},{7,9}};
  std::array<int,10> perm{};for(int u=0;u<10;u++)perm[u]=u;
  std::set<uint64_t> unique;
  do{if(!(perm[1]<perm[4]&&perm[4]<perm[5]&&perm[2]<perm[6]))continue;
    uint64_t mask=0;for(auto [u,v]:standard)mask|=1ULL<<edge_index[perm[u]][perm[v]];assert(unique.insert(mask).second);
  }while(std::next_permutation(perm.begin()+1,perm.end()));
  assert(unique.size()==30240);catalog.assign(unique.begin(),unique.end());for(auto mask:catalog)local_catalog.push_back(decode(mask));
  std::array<std::vector<int>,2> domains;
  std::ofstream detail(out+"/boundary_domains.jsonl");
  Graph best=original,best_new=original;auto bestscore=score(best);std::pair<int,int> best_new_score{9999,9999};std::string stop;int screened=0;
  for(int i=0;i<2;i++){
    Boundary b=boundary(i);int min_boundary=10000,best_boundary_id=-1;Graph best_boundary;
    std::map<int,int> hist;int best_single_bad=10000,best_single_energy=10000,best_single_id=-1;
    for(int idx=0;idx<int(catalog.size());idx++){
      int missing=boundary_bad(b,local_catalog[idx]);hist[missing]++;
      if(!missing)domains[i].push_back(idx);
      Graph g=replace(original,i,catalog[idx]);auto value=score(g);
      if(catalog[idx]!=local_mask(original,i)&&value<best_new_score){best_new_score=value;best_new=g;}
      if(value<std::pair<int,int>{best_single_bad,best_single_energy}){best_single_bad=value.first;best_single_energy=value.second;best_single_id=idx;}
      if(value<bestscore){bestscore=value;best=g;}
      if(missing<min_boundary){min_boundary=missing;best_boundary_id=idx;best_boundary=g;}
      if(idx%1024==1023&&double(clock()-started)/CLOCKS_PER_SEC>5.0){stop="cpu_cap_partial_boundary_domain";break;}
    }
    bool completed=stop.empty();if(completed)screened++;
    detail<<"{\"fiber\":"<<i<<",\"complete\":"<<(completed?"true":"false")<<",\"domain_size\":"<<domains[i].size()<<",\"minimum_boundary_bad_pairs\":"<<min_boundary<<",\"best_single_internal_bad_pairs\":"<<best_single_bad<<",\"best_single_internal_energy\":"<<best_single_energy<<",\"best_single_catalog_index\":"<<best_single_id<<",\"minimum_boundary_catalog_index\":"<<best_boundary_id<<",\"required_neighbors\":[";
    for(int u=0;u<10;u++){if(u)detail<<',';detail<<'[';bool first=true;unsigned row=b.missing[0][u]|b.missing[1][u];for(int v=0;v<10;v++)if(row>>v&1){if(!first)detail<<',';first=false;detail<<v;}detail<<']';}detail<<"],\"boundary_bad_histogram\":{";
    bool first=true;for(auto [value,count]:hist){if(!first)detail<<',';first=false;detail<<'"'<<value<<"\":"<<count;}detail<<"},\"surviving_catalog_indices\":[";first=true;for(int idx:domains[i]){if(!first)detail<<',';first=false;detail<<idx;}detail<<"]}\n";
    save("fiber"+std::to_string(i)+".best_single",replace(original,i,catalog[best_single_id]));save("fiber"+std::to_string(i)+".best_boundary",best_boundary);
    if(!completed)break;
    if(domains[i].empty()){stop="complete_empty_boundary_domain_fiber"+std::to_string(i);break;}
  }
  long long decompositions=0,boundary_valid_decompositions=0,assemblies=0;
  if(stop.empty()){
    uint64_t p4=local_mask(original,4),q=0;
    for(int e=0;e<45;e++){auto [u,v]=local_edges[e];if(original[50+match[4][5][u]]>>(50+match[4][5][v])&1)q|=1ULL<<e;}
    assert(!(p4&q));uint64_t support=p4|q;Boundary b4=boundary(4),b5=boundary(5);
    for(int id4=0;id4<int(catalog.size());id4++){
      uint64_t x=catalog[id4];if(x&~support)continue;uint64_t y=support^x;if(!unique.count(y))continue;decompositions++;
      uint64_t p5=0;for(int e=0;e<45;e++)if(y>>e&1){auto [u,v]=local_edges[e];p5|=1ULL<<edge_index[match[4][5][u]][match[4][5][v]];}
      if(boundary_bad(b4,local_catalog[id4])||boundary_bad(b5,decode(p5)))continue;boundary_valid_decompositions++;
      for(int id0:domains[0]){if(!stop.empty())break;for(int id1:domains[1]){Graph g=replace(replace(replace(replace(original,0,catalog[id0]),1,catalog[id1]),4,x),5,p5);auto value=score(g);assemblies++;if(value<bestscore){bestscore=value;best=g;}if(g!=original&&value<best_new_score){best_new_score=value;best_new=g;}
        if(double(clock()-started)/CLOCKS_PER_SEC>5.0){stop="cpu_cap_partial_joint_assembly";break;}}}
      if(!stop.empty())break;
    }
    if(stop.empty())stop="complete_joint_assembly";
  }
  save("best",best);
  save("best_new",best_new);
  std::ofstream result(out+"/search.json");result<<"{\"labeled_Petersen_catalog_size\":30240,\"completed_boundary_screens\":"<<screened<<",\"stop_reason\":\""<<stop<<"\",\"coupled45_decompositions\":"<<decompositions<<",\"boundary_valid45_decompositions\":"<<boundary_valid_decompositions<<",\"joint_assemblies\":"<<assemblies<<",\"best_bad_pairs\":"<<bestscore.first<<",\"best_energy\":"<<bestscore.second<<",\"cpu_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"cpu_budget_seconds\":5,\"solver_runs\":0}\n";
  std::cout<<stop<<" best "<<bestscore.first<<" energy "<<bestscore.second<<" cpu "<<double(clock()-started)/CLOCKS_PER_SEC<<'\n';
}

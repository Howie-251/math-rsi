// Complete new binary L-preserving palette; no random moves or SAT.
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
struct Palette {int i,j,p[2][10];};
std::array<Palette,15> palettes;
Graph base{};
void toggle(Graph& g,int u,int v){g[u]^=1ULL<<v;g[v]^=1ULL<<u;}
Graph expand(unsigned mask){Graph g=base;for(int b=0;b<15;b++)for(int u=0;u<10;u++)toggle(g,10*palettes[b].i+u,10*palettes[b].j+palettes[b].p[mask>>b&1][u]);return g;}
std::pair<int,int> score(const Graph& g){
  int bad=0,energy=0;
  for(int u=0;u<60;u++)for(int v=u+1;v<60;v++){
    int r=__builtin_popcountll(g[u]&g[v])+int(g[u]>>v&1);
    bad+=r==0;int d=r-1;energy+=d*(d-1)/2;
  }return {bad,energy};
}
int main(int argc,char**argv){
  assert(argc==3);std::ifstream input(argv[1]);int n,m,k;input>>n>>m>>k;assert(n==60&&m==90&&k==15);
  for(int e=0,u,v;e<m;e++){input>>u>>v;toggle(base,u,v);}
  for(auto& p:palettes){input>>p.i>>p.j;for(auto& row:p.p)for(int& v:row)input>>v;}
  std::string out=argv[2];clock_t start=clock();Graph g=expand(0);unsigned oldmask=0;
  int best_bad=9999,best_energy=9999;std::vector<unsigned> bad_masks,energy_masks;
  std::map<int,int> bad_hist,energy_hist;int visited=0;bool complete=true;
  for(unsigned step=0;step<(1U<<15);step++){
    unsigned mask=step^(step>>1);
    if(step){unsigned bit=__builtin_ctz(mask^oldmask);auto& p=palettes[bit];
      for(int u=0;u<10;u++)toggle(g,10*p.i+u,10*p.j+p.p[oldmask>>bit&1][u]);
      for(int u=0;u<10;u++)toggle(g,10*p.i+u,10*p.j+p.p[mask>>bit&1][u]);}
    oldmask=mask;auto [bad,energy]=score(g);visited++;bad_hist[bad]++;energy_hist[energy]++;
    if(bad<best_bad){best_bad=bad;bad_masks.clear();}if(bad==best_bad)bad_masks.push_back(mask);
    if(energy<best_energy){best_energy=energy;energy_masks.clear();}if(energy==best_energy)energy_masks.push_back(mask);
    if(step%256==255&&double(clock()-start)/CLOCKS_PER_SEC>3.0){complete=false;break;}
  }
  std::set<unsigned> saved(bad_masks.begin(),bad_masks.end());saved.insert(energy_masks.begin(),energy_masks.end());
  std::ofstream graphs(out+"/minimum_graphs.edges");graphs<<"60 240 "<<saved.size()<<'\n';
  for(unsigned mask:saved){Graph h=expand(mask);auto [bad,energy]=score(h);graphs<<mask<<' '<<bad<<' '<<energy<<'\n';
    for(int u=0;u<60;u++){assert(__builtin_popcountll(h[u])==8);for(int v=u+1;v<60;v++)if(h[u]>>v&1)graphs<<u<<' '<<v<<'\n';}}
  std::ofstream result(out+"/search.json");
  result<<"{\"complete\":"<<(complete?"true":"false")<<",\"assignments_examined\":"<<visited
    <<",\"domain_size\":32768,\"minimum_bad_pairs\":"<<best_bad<<",\"minimum_energy\":"<<best_energy
    <<",\"saved_complete_graphs\":"<<saved.size()<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC
    <<",\"cpu_budget_seconds\":3,\"minimum_bad_masks\":[";
  bool first=true;for(auto mask:bad_masks){if(!first)result<<',';first=false;result<<mask;}result<<"],\"minimum_energy_masks\":[";
  first=true;for(auto mask:energy_masks){if(!first)result<<',';first=false;result<<mask;}result<<"],\"bad_pair_histogram\":{";
  first=true;for(auto [value,count]:bad_hist){if(!first)result<<',';first=false;result<<'"'<<value<<"\":"<<count;}result<<"},\"energy_histogram\":{";
  first=true;for(auto [value,count]:energy_hist){if(!first)result<<',';first=false;result<<'"'<<value<<"\":"<<count;}result<<"}}\n";
  std::cout<<"complete "<<complete<<" examined "<<visited<<" bad "<<best_bad<<" energy "<<best_energy<<" saved "<<saved.size()<<" cpu "<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}

// Complete one-vertex deletion plus neighbor-perfect-matching repair of the
// saved 20-bad-pair order-60 graph. Exactly 60*7!! = 6300 candidates.
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using State=std::array<uint64_t,60>;
constexpr uint64_t ALL=(1ULL<<60)-1;
State original{},bestgraph{};
int best=100000,best_deleted=-1;long long checked=0;
std::vector<std::pair<int,int>> repair,bestrepair;
std::map<int,long long> histogram;
int score(const State&s,int deleted){
 int count=0;uint64_t live=ALL^(1ULL<<deleted);
 for(int u=0;u<60;u++)if(u!=deleted){
  uint64_t reach=s[u]|(1ULL<<u),todo=s[u];
  while(todo){int w=__builtin_ctzll(todo);todo&=todo-1;reach|=s[w];}
  count+=__builtin_popcountll(live&~reach);
 }assert(count%2==0);return count/2;
}
void enumerate(State& s,uint64_t unmatched,int deleted){
 if(!unmatched){
  int bad=score(s,deleted);checked++;histogram[bad]++;
  if(bad<best){best=bad;bestgraph=s;best_deleted=deleted;bestrepair=repair;}
  return;
 }
 int u=__builtin_ctzll(unmatched);unmatched^=1ULL<<u;uint64_t choices=unmatched;
 while(choices){
  int v=__builtin_ctzll(choices);choices&=choices-1;
  assert(!(s[u]>>v&1));s[u]|=1ULL<<v;s[v]|=1ULL<<u;repair.emplace_back(u,v);
  enumerate(s,unmatched^(1ULL<<v),deleted);
  repair.pop_back();s[u]^=1ULL<<v;s[v]^=1ULL<<u;
 }
}
int main(int argc,char**argv){
 assert(argc==3);std::ifstream input(argv[1]);int n,m;input>>n>>m;assert(n==60&&m==240);
 for(int z=0,u,v;z<m;z++){input>>u>>v;assert(u<v&&v<60);original[u]|=1ULL<<v;original[v]|=1ULL<<u;}
 for(int u=0;u<60;u++){
  assert(__builtin_popcountll(original[u])==8);
  uint64_t todo=original[u];while(todo){int v=__builtin_ctzll(todo);todo&=todo-1;assert(!(original[u]&original[v]));}
 }
 clock_t start=clock();
 for(int deleted=0;deleted<60;deleted++){
  State s=original;uint64_t neighbors=s[deleted];s[deleted]=0;
  for(int u=0;u<60;u++)s[u]&=~(1ULL<<deleted);
  enumerate(s,neighbors,deleted);
 }
 assert(checked==6300);double cpu=double(clock()-start)/CLOCKS_PER_SEC;
 std::string prefix=argv[2];std::ofstream edges(prefix+".best.edges"),json(prefix+".best.json");
 edges<<"59 236\n";json<<"{\"n\":59,\"edges\":[";bool comma=false;int ec=0;
 for(int u=0;u<60;u++)if(u!=best_deleted){
  assert(__builtin_popcountll(bestgraph[u])==8);
  for(int v=u+1;v<60;v++)if(bestgraph[u]>>v&1){
   int a=u-(u>best_deleted),b=v-(v>best_deleted);edges<<a<<' '<<b<<'\n';
   if(comma)json<<',';comma=true;json<<'['<<a<<','<<b<<']';ec++;
  }
 }assert(ec==236);json<<"]}\n";
 std::ofstream report(prefix+".json");report<<"{\"scope\":\"All vertex deletions and all perfect matchings on its eight neighbors, of the saved order60 twin-HS seed only\",\"complete_for_stated_neighborhood\":true,\"candidates\":"<<checked<<",\"minimum_bad_pairs\":"<<best<<",\"cpu_seconds\":"<<cpu<<",\"best_deleted_original_vertex\":"<<best_deleted<<",\"best_repair_original_edges\":[";
 comma=false;for(auto [u,v]:bestrepair){if(comma)report<<',';comma=true;report<<'['<<u<<','<<v<<']';}
 report<<"],\"bad_pair_histogram\":{";comma=false;
 for(auto [bad,count]:histogram){if(comma)report<<',';comma=true;report<<'\"'<<bad<<"\":"<<count;}
 report<<"}}\n";std::cout<<checked<<" candidates, best "<<best<<", CPU "<<cpu<<'\n';
}

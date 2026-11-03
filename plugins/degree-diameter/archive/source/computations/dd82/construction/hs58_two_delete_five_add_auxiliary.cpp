// Complete H(8,10) port-budget screen; exact S8 orbit compression.
// No HS completion test, graph optimization, or old H(8,8) or H(8,9) computation.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using Edge=std::pair<int,int>;
using Adj=std::array<unsigned,8>;
std::array<Edge,28> edges;
std::array<std::array<int,8>,8> edgeindex{};
struct Triple { std::array<int,3> vertices; uint32_t mask; };
std::vector<Triple> triples;
struct Entry {
 uint32_t graph,bad;
 long long count=0,orbit_size=0,automorphisms=0;
 bool disjoint,adjacent,universal;
 int triple_index;
};
Adj adjacency(uint32_t mask){
 Adj a{};
 while(mask){int e=__builtin_ctz(mask);mask&=mask-1;auto[u,v]=edges[e];a[u]|=1U<<v;a[v]|=1U<<u;}
 return a;
}
uint32_t badpairs(const Adj&a){
 uint32_t result=0;
 for(int u=0;u<8;u++){
  unsigned reach=(1U<<u)|a[u],todo=a[u];
  while(todo){int v=__builtin_ctz(todo);todo&=todo-1;reach|=a[v];}
  unsigned missing=(255U&~reach)&~((1U<<(u+1))-1);
  while(missing){int v=__builtin_ctz(missing);missing&=missing-1;result|=1U<<edgeindex[u][v];}
 }
 return result;
}
void edgejson(std::ostream&o,uint32_t mask){
 o<<'[';bool comma=false;
 for(int e=0;e<28;e++)if(mask>>e&1){if(comma)o<<',';comma=true;o<<'['<<edges[e].first<<','<<edges[e].second<<']';}
 o<<']';
}
void intarray(std::ostream&o,const std::array<int,8>&a){
 o<<'[';for(int i=0;i<8;i++){if(i)o<<',';o<<a[i];}o<<']';
}
void writeentry(std::ostream&o,const Entry&e,int id){
 Adj a=adjacency(e.graph),b=adjacency(e.bad);
 std::array<int,8>d{},bd{};
 for(int i=0;i<8;i++){d[i]=__builtin_popcount(a[i]);bd[i]=__builtin_popcount(b[i]);}
 auto sorted=d;std::sort(sorted.rbegin(),sorted.rend());
 o<<"{\"type_id\":"<<id<<",\"canonical_edge_mask\":"<<e.graph
  <<",\"labeled_multiplicity\":"<<e.count<<",\"orbit_size\":"<<e.orbit_size
  <<",\"automorphism_group_order\":"<<e.automorphisms
  <<",\"disjoint_budget\":"<<(e.disjoint?"true":"false")
  <<",\"adjacent_budget\":"<<(e.adjacent?"true":"false")
  <<",\"universal\":"<<(e.universal?"true":"false")<<",\"degrees\":";
 intarray(o,d);o<<",\"sorted_degrees\":";intarray(o,sorted);
 o<<",\"edges\":";edgejson(o,e.graph);
 o<<",\"bad_pair_count\":"<<__builtin_popcount(e.bad)<<",\"bad_pairs\":";edgejson(o,e.bad);
 o<<",\"bad_graph_degrees\":";intarray(o,bd);
 o<<",\"universal_vertices\":[";bool comma=false;
 for(int i=0;i<8;i++)if(d[i]==7){if(comma)o<<',';comma=true;o<<i;}o<<']';
 o<<",\"bad_graph_star_centers\":[";comma=false;
 for(int i=0;i<8;i++)if(e.bad&&bd[i]==__builtin_popcount(e.bad)){
  if(comma)o<<',';comma=true;o<<i;
 }o<<']';
 if(e.adjacent){const auto&t=triples[e.triple_index];
  o<<",\"adjacent_cover_triple\":["<<t.vertices[0]<<','<<t.vertices[1]<<','<<t.vertices[2]
   <<"],\"adjacent_cover_remaining_edges\":";edgejson(o,e.bad&~t.mask);
 }
 o<<'}';
}
int main(int argc,char**argv){
 assert(argc==2);const std::string prefix=argv[1];clock_t start=clock();int k=0;
 for(int u=0;u<8;u++)for(int v=u+1;v<8;v++){edges[k]={u,v};edgeindex[u][v]=edgeindex[v][u]=k++;}
 for(int a=0;a<8;a++)for(int b=a+1;b<8;b++)for(int c=b+1;c<8;c++)
  triples.push_back({{a,b,c},(1U<<edgeindex[a][b])|(1U<<edgeindex[a][c])|(1U<<edgeindex[b][c])});
 std::vector<Entry> reps;
 std::unordered_map<uint32_t,int> labeled_class;
 labeled_class.reserve(65536);
 std::array<long long,29> histogram{};
 long long checked=0,unioncount=0,disjointcount=0,adjacentcount=0;
 bool timeout=false;uint32_t mask=(1U<<10)-1;
 std::ofstream discoveries(prefix+".representatives.jsonl");
 while(mask<(1U<<28)){
  if((checked&4095)==0&&double(clock()-start)/CLOCKS_PER_SEC>=9.8){timeout=true;break;}
  Adj a=adjacency(mask);uint32_t bad=badpairs(a);int b=__builtin_popcount(bad);histogram[b]++;checked++;
  bool disjoint=b<=4,adjacent=false;int ti=-1;
  if(b<=5)for(unsigned i=0;i<triples.size();i++)
   if(__builtin_popcount(bad&triples[i].mask)>=b-2){adjacent=true;ti=i;break;}
  if(disjoint||adjacent){
   // Port budgets imply b<=5; disconnected eight-vertex graphs have b>=7.
   unsigned reach=1,old=0;
   while(reach!=old){old=reach;for(int u=0;u<8;u++)if(old>>u&1)reach|=a[u];}
   assert(reach==255);
   bool universal=false;for(unsigned row:a)if(__builtin_popcount(row)==7)universal=true;
   int id;auto found=labeled_class.find(mask);
   if(found==labeled_class.end()){
    id=int(reps.size());reps.push_back({mask,bad,0,0,0,disjoint,adjacent,universal,ti});
    // Enumerating S8 gives every labeled isomorphic graph and only those.
    // Gosper order is increasing, so this first representative is canonical.
    std::vector<Edge> present;
    for(int e=0;e<28;e++)if(mask>>e&1)present.push_back(edges[e]);
    std::array<int,8> p{0,1,2,3,4,5,6,7};
    do{
     uint32_t image=0;
     for(auto[u,v]:present)image|=1U<<edgeindex[p[u]][p[v]];
     assert(image>=mask);
     auto inserted=labeled_class.emplace(image,id);
     assert(inserted.second||inserted.first->second==id);
     reps[id].orbit_size+=inserted.second;
     reps[id].automorphisms+=(image==mask);
    }while(std::next_permutation(p.begin(),p.end()));
    assert(reps[id].orbit_size*reps[id].automorphisms==40320);
    writeentry(discoveries,reps[id],id+1);discoveries<<'\n';discoveries.flush();
   }else id=found->second;
   auto&e=reps[id];
   assert(e.disjoint==disjoint&&e.adjacent==adjacent&&e.universal==universal);
   e.count++;unioncount++;disjointcount+=disjoint;adjacentcount+=adjacent;
  }
  uint32_t low=mask&-mask,next=mask+low;
  mask=next+(((next^mask)/low)>>2);
 }
 bool complete=!timeout;
 assert(!complete||checked==13123110);
 if(complete){assert(labeled_class.size()==size_t(unioncount));for(const auto&e:reps)assert(e.count==e.orbit_size);}
 std::ofstream out(prefix+".json");
 out<<"{\"n\":8,\"edges\":10,\"old_original_deletions\":2,\"old_nonedge_additions\":5"
  <<",\"expected_labeled_graphs\":13123110,\"checked_labeled_graphs\":"<<checked
  <<",\"complete\":"<<(complete?"true":"false")<<",\"stop_reason\":\""<<(complete?"complete_domain":"cpu_cap")
  <<"\",\"cpu_limit_seconds\":10,\"internal_stop_seconds\":9.8,\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC
  <<",\"threads\":1,\"labeled_union_survivors\":"<<unioncount
  <<",\"labeled_disjoint_budget_survivors\":"<<disjointcount
  <<",\"labeled_adjacent_budget_survivors\":"<<adjacentcount
  <<",\"union_isomorphism_types\":"<<reps.size()
  <<",\"all_survivors_preserved_up_to_exact_isomorphism\":true"
  <<",\"classification\":\"Complete 40320-permutation orbit of each newly encountered representative\""
  <<",\"bad_pair_histogram\":[";
 for(int b=0;b<=28;b++){if(b)out<<',';out<<histogram[b];}
 out<<"],\"representatives\":[";
 for(unsigned i=0;i<reps.size();i++){if(i)out<<',';writeentry(out,reps[i],i+1);}
 out<<"]}\n";
 std::cout<<"complete="<<complete<<" checked="<<checked<<" union="<<unioncount
  <<" disjoint="<<disjointcount<<" adjacent="<<adjacentcount
  <<" types="<<reps.size()<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}

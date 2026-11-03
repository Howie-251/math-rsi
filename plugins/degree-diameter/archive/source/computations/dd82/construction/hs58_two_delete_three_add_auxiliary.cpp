// Complete auxiliary H(8,8) budget screen; no HS graph or attachment solver.
#include <algorithm>
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
using Edge=std::pair<int,int>;
using Adj=std::array<unsigned,8>;
std::array<Edge,28> edges;
std::array<std::array<int,8>,8> edgeindex{};
struct Triple { std::array<int,3> vertices; uint32_t mask; };
std::vector<Triple> triples;
struct Entry { uint32_t graph,bad; long long count=0; bool disjoint,adjacent,universal; int triple_index; };
std::string rooted(int u,int parent,const Adj&a,unsigned cycle){
 std::vector<std::string> children;
 for(int v=0;v<8;v++)if((a[u]>>v&1)&&v!=parent&&!(cycle>>v&1))children.push_back(rooted(v,u,a,cycle));
 std::sort(children.begin(),children.end());std::string s="(";for(const auto&t:children)s+=t;return s+")";
}
// Exact isomorphism key for connected unicyclic graphs.
std::string canonical(const Adj&a){
 std::array<int,8> degree{};std::vector<int> queue;unsigned cycle=255;
 for(int u=0;u<8;u++){degree[u]=__builtin_popcount(a[u]);if(degree[u]==1)queue.push_back(u);}
 for(unsigned k=0;k<queue.size();k++){int u=queue[k];cycle&=~(1U<<u);for(int v=0;v<8;v++)if((a[u]>>v&1)&&degree[v]>1)if(--degree[v]==1)queue.push_back(v);}
 assert(__builtin_popcount(cycle)>=3);int start=__builtin_ctz(cycle),prev=-1,u=start;std::vector<int> order;
 do{order.push_back(u);unsigned next=a[u]&cycle;if(prev>=0)next&=~(1U<<prev);assert(next);int v=__builtin_ctz(next);prev=u;u=v;}while(u!=start);
 assert(order.size()==unsigned(__builtin_popcount(cycle)));
 std::vector<std::string> trees;for(int v:order)trees.push_back(rooted(v,-1,a,cycle));
 std::string best;int n=trees.size();for(int shift=0;shift<n;shift++)for(int sign:{1,-1}){std::string key=std::to_string(n)+":";for(int j=0;j<n;j++)key+=trees[(shift+sign*j+n)%n]+"|";if(best.empty()||key<best)best=key;}return best;
}
Adj adjacency(uint32_t mask){Adj a{};while(mask){int e=__builtin_ctz(mask);mask&=mask-1;auto[u,v]=edges[e];a[u]|=1U<<v;a[v]|=1U<<u;}return a;}
uint32_t badpairs(const Adj&a){uint32_t result=0;for(int u=0;u<8;u++){unsigned reach=(1U<<u)|a[u],todo=a[u];while(todo){int v=__builtin_ctz(todo);todo&=todo-1;reach|=a[v];}unsigned missing=(255U&~reach)&~((1U<<(u+1))-1);while(missing){int v=__builtin_ctz(missing);missing&=missing-1;result|=1U<<edgeindex[u][v];}}return result;}
void edgejson(std::ostream&o,uint32_t mask){o<<'[';bool comma=false;for(int e=0;e<28;e++)if(mask>>e&1){if(comma)o<<',';comma=true;o<<'['<<edges[e].first<<','<<edges[e].second<<']';}o<<']';}
int main(int argc,char**argv){
 assert(argc==2);const std::string prefix=argv[1];clock_t start=clock();int k=0;
 for(int u=0;u<8;u++)for(int v=u+1;v<8;v++){edges[k]={u,v};edgeindex[u][v]=edgeindex[v][u]=k++;}
 for(int a=0;a<8;a++)for(int b=a+1;b<8;b++)for(int c=b+1;c<8;c++)triples.push_back({{a,b,c},(1U<<edgeindex[a][b])|(1U<<edgeindex[a][c])|(1U<<edgeindex[b][c])});
 std::map<std::string,Entry> reps;std::array<long long,29> histogram{};
 long long checked=0,unioncount=0,disjointcount=0,adjacentcount=0;bool timeout=false;
 uint32_t mask=(1U<<8)-1;
 while(mask<(1U<<28)){
  if((checked&4095)==0&&double(clock()-start)/CLOCKS_PER_SEC>=9.8){timeout=true;break;}
  Adj a=adjacency(mask);uint32_t bad=badpairs(a);int b=__builtin_popcount(bad);histogram[b]++;checked++;
  bool disjoint=b<=4,adjacent=false;int ti=-1;
  if(b<=5)for(unsigned i=0;i<triples.size();i++)if(__builtin_popcount(bad&triples[i].mask)>=b-2){adjacent=true;ti=i;break;}
  if(disjoint||adjacent){
   // Both port budgets imply b<=5. A disconnected 8-vertex graph has b>=7.
   unsigned reach=1,old=0;while(reach!=old){old=reach;for(int u=0;u<8;u++)if(old>>u&1)reach|=a[u];}assert(reach==255);
   bool universal=false;for(unsigned row:a)if(__builtin_popcount(row)==7)universal=true;
   auto key=canonical(a);auto it=reps.find(key);if(it==reps.end())it=reps.emplace(key,Entry{mask,bad,0,disjoint,adjacent,universal,ti}).first;
   assert(it->second.disjoint==disjoint&&it->second.adjacent==adjacent&&it->second.universal==universal);
   it->second.count++;unioncount++;disjointcount+=disjoint;adjacentcount+=adjacent;
  }
  uint32_t low=mask&-mask,next=mask+low;mask=next+(((next^mask)/low)>>2);
 }
 bool complete=!timeout;assert(!complete||checked==3108105);
 std::ofstream out(prefix+".json");out<<"{\"n\":8,\"edges\":8,\"expected_labeled_graphs\":3108105,\"checked_labeled_graphs\":"<<checked<<",\"complete\":"<<(complete?"true":"false")<<",\"stop_reason\":\""<<(complete?"complete_domain":"cpu_cap")<<"\",\"cpu_limit_seconds\":10,\"internal_stop_seconds\":9.8,\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"threads\":1,\"labeled_union_survivors\":"<<unioncount<<",\"labeled_disjoint_budget_survivors\":"<<disjointcount<<",\"labeled_adjacent_budget_survivors\":"<<adjacentcount<<",\"union_isomorphism_types\":"<<reps.size()<<",\"all_survivors_preserved_up_to_exact_isomorphism\":true,\"canonicalization\":\"Unique cycle with rooted-tree AHU strings, minimized under all rotations and reflections\",\"bad_pair_histogram\":[";
 for(int b=0;b<=28;b++){if(b)out<<',';out<<histogram[b];}out<<"],\"representatives\":[";
 bool comma=false;int id=0;for(const auto&[key,e]:reps){if(comma)out<<',';comma=true;Adj a=adjacency(e.graph);std::vector<int>d;for(unsigned row:a)d.push_back(__builtin_popcount(row));auto sorted=d;std::sort(sorted.rbegin(),sorted.rend());
  out<<"{\"type_id\":"<<++id<<",\"canonical_key\":\""<<key<<"\",\"labeled_multiplicity\":"<<e.count<<",\"disjoint_budget\":"<<(e.disjoint?"true":"false")<<",\"adjacent_budget\":"<<(e.adjacent?"true":"false")<<",\"universal\":"<<(e.universal?"true":"false")<<",\"degrees\":[";for(int u=0;u<8;u++){if(u)out<<',';out<<d[u];}out<<"],\"sorted_degrees\":[";for(int u=0;u<8;u++){if(u)out<<',';out<<sorted[u];}out<<"],\"edges\":";edgejson(out,e.graph);out<<",\"bad_pair_count\":"<<__builtin_popcount(e.bad)<<",\"bad_pairs\":";edgejson(out,e.bad);
  out<<",\"universal_vertices\":[";bool first=true;for(int u=0;u<8;u++)if(d[u]==7){if(!first)out<<',';first=false;out<<u;}out<<']';
  if(e.adjacent){const auto&t=triples[e.triple_index];out<<",\"adjacent_cover_triple\":["<<t.vertices[0]<<','<<t.vertices[1]<<','<<t.vertices[2]<<"],\"adjacent_cover_remaining_edges\":";edgejson(out,e.bad&~t.mask);}
  out<<'}';
 }out<<"]}\n";
 std::cout<<"complete="<<complete<<" checked="<<checked<<" union="<<unioncount<<" disjoint="<<disjointcount<<" adjacent="<<adjacentcount<<" types="<<reps.size()<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}

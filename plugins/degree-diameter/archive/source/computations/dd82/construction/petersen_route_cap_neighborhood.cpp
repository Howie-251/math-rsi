// Complete radius-two neighborhood in fifteen S10 matching coordinates.
// Every one of 675 first transpositions is expanded, regardless of its cap.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using Bits=uint64_t;
struct Move {int matching,a,b;};
struct Graph {std::array<Bits,60> adj{};std::array<std::array<int,10>,15> p{};};
std::array<std::pair<int,int>,15> fibers;
std::vector<Move> moves;
void change(Graph& g,const Move& x){
 auto [i,j]=fibers[x.matching];int u=10*i+x.a,v=10*i+x.b;
 int a=10*j+g.p[x.matching][x.a],b=10*j+g.p[x.matching][x.b];
 g.adj[u]^=(Bits(1)<<a)|(Bits(1)<<b);g.adj[v]^=(Bits(1)<<a)|(Bits(1)<<b);
 g.adj[a]^=(Bits(1)<<u)|(Bits(1)<<v);g.adj[b]^=(Bits(1)<<u)|(Bits(1)<<v);
 std::swap(g.p[x.matching][x.a],g.p[x.matching][x.b]);
}
int score(const Graph&g){
 int missing=0;
 for(auto [i,j]:fibers)for(int a=0;a<10;a++)for(int b=0;b<10;b++){
  int u=10*i+a,v=10*j+b;
  int routes=__builtin_popcountll(g.adj[u]&g.adj[v])+((g.adj[u]>>v)&1);
  if(routes>2)return -1;
  missing+=(routes==0);
 }
 return missing;
}
bool canonical(const Move&x,const Move&y){
 if(x.matching!=y.matching)return x.matching<y.matching;
 if(x.a==y.a&&x.b==y.b)return false; // identity counted separately
 const bool overlap=x.a==y.a||x.a==y.b||x.b==y.a||x.b==y.b;
 if(!overlap)return std::pair(x.a,x.b)<std::pair(y.a,y.b);
 int third=(y.a!=x.a&&y.a!=x.b)?y.a:y.b;
 return third>x.b; // each 3-cycle has unique factorization starting with two smallest labels
}
void output_hist(std::ostream&o,const std::map<int,long long>&h){o<<'{';bool c=false;for(auto [k,n]:h){if(c)o<<',';c=true;o<<'"'<<k<<"\":"<<n;}o<<'}';}
void output_move(std::ostream&o,int idx){const Move&x=moves[idx];auto [i,j]=fibers[x.matching];o<<"{\"move_index\":"<<idx<<",\"fibers\":["<<i<<','<<j<<"],\"source_coordinates\":["<<x.a<<','<<x.b<<"],\"source_vertices\":["<<10*i+x.a<<','<<10*i+x.b<<"]}";}
int main(int argc,char**argv){
 assert(argc==3);const std::string input=argv[1],prefix=argv[2];const clock_t start=clock();
 Graph seed;std::ifstream in(input);int n,m;in>>n>>m;assert(n==60&&m==240);
 int u,v;int lines=0;while(in>>u>>v){assert(u>=0&&v<60&&u<v);assert(!(seed.adj[u]>>v&1));seed.adj[u]|=Bits(1)<<v;seed.adj[v]|=Bits(1)<<u;lines++;}assert(lines==240);
 for(Bits row:seed.adj)assert(__builtin_popcountll(row)==8);
 int idx=0;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){
  fibers[idx]={i,j};int targets=0;
  for(int a=0;a<10;a++){Bits row=(seed.adj[10*i+a]>>(10*j))&1023;assert(__builtin_popcountll(row)==1);int b=__builtin_ctzll(row);seed.p[idx][a]=b;targets|=1<<b;}
  assert(targets==1023);for(int a=0;a<10;a++)for(int b=a+1;b<10;b++)moves.push_back({idx,a,b});idx++;
 }
 assert(moves.size()==675);const int seedbad=score(seed);assert(seedbad>=0);
 std::array<int,675> single{};std::map<int,long long>singlehist,doublehist,uniquehist;
 std::vector<std::pair<int,int>>singlevalid;
 Graph bestgraph,bestdoublegraph;int best=std::numeric_limits<int>::max(),bestdouble=std::numeric_limits<int>::max();std::vector<int>bestpath,bestdoublepath;
 auto consider=[&](const Graph&g,int e,std::vector<int>path){if(e>=0&&e<best){best=e;bestgraph=g;bestpath=path;}};
 Graph g=seed;
 for(int a=0;a<675;a++){
  change(g,moves[a]);single[a]=score(g);
  if(single[a]>=0){singlehist[single[a]]++;singlevalid.push_back({a,single[a]});consider(g,single[a],{a});}
  change(g,moves[a]);
 }
 long long ordered=0,feasible=0,unique=1,uniquefeasible=1,via_bad_first=0,canonical_nonidentity=0;
 uniquehist[seedbad]=1;
 for(int a=0;a<675;a++){
  change(g,moves[a]);
  for(int b=0;b<675;b++){
   change(g,moves[b]);ordered++;int e=score(g);const bool canon=canonical(moves[a],moves[b]);
   if(canon){unique++;canonical_nonidentity++;}
   if(e>=0){feasible++;doublehist[e]++;if(single[a]<0)via_bad_first++;
    if(canon){uniquefeasible++;uniquehist[e]++;}
    if(a!=b){consider(g,e,{a,b});if(e<bestdouble){bestdouble=e;bestdoublegraph=g;bestdoublepath={a,b};}}
   }
   change(g,moves[b]);
  }
  change(g,moves[a]);
 }
 assert(g.adj==seed.adj&&g.p==seed.p);
 assert(ordered==675LL*675&&canonical_nonidentity==225675&&unique==225676);
 assert(best<std::numeric_limits<int>::max());
 std::ofstream edge(prefix+".best.edges");edge<<"60 240\n";for(int a=0;a<60;a++)for(int b=a+1;b<60;b++)if(bestgraph.adj[a]>>b&1)edge<<a<<' '<<b<<'\n';
 std::ofstream doubleedge(prefix+".best_double.edges");doubleedge<<"60 240\n";for(int a=0;a<60;a++)for(int b=a+1;b<60;b++)if(bestdoublegraph.adj[a]>>b&1)doubleedge<<a<<' '<<b<<'\n';
 const double cpu=double(clock()-start)/CLOCKS_PER_SEC;
 std::ofstream o(prefix+".json");
 o<<"{\"source\":\""<<input<<"\",\"scope\":\"all at most two image transpositions in any of 15 perfect matchings; all 675 first moves expanded regardless of cap\",\"complete\":true,\"route_cap\":2,\"seed_bad_pairs\":"<<seedbad<<",\"single_moves\":675,\"single_cap_feasible\":"<<singlevalid.size()<<",\"single_feasible_bad_histogram\":";output_hist(o,singlehist);
 o<<",\"ordered_double_moves\":"<<ordered<<",\"ordered_double_cap_feasible\":"<<feasible<<",\"ordered_double_feasible_bad_histogram\":";output_hist(o,doublehist);
 o<<",\"unique_double_endpoints_including_seed\":"<<unique<<",\"unique_double_cap_feasible_including_seed\":"<<uniquefeasible<<",\"unique_double_feasible_bad_histogram\":";output_hist(o,uniquehist);
 o<<",\"unique_radius_two_endpoints_including_seed\":"<<unique+675<<",\"unique_radius_two_cap_feasible\":"<<uniquefeasible+singlevalid.size()<<",\"ordered_feasible_doubles_with_cap_violating_first_move\":"<<via_bad_first<<",\"minimum_bad_pairs_including_seed\":"<<std::min(seedbad,best)<<",\"minimum_bad_pairs_among_distinct_neighbors\":"<<best<<",\"best_path\":[";
 for(unsigned k=0;k<bestpath.size();k++){if(k)o<<',';output_move(o,bestpath[k]);}
 o<<"],\"minimum_bad_pairs_among_distinct_double_neighbors\":"<<bestdouble<<",\"best_double_path\":[";
 for(unsigned k=0;k<bestdoublepath.size();k++){if(k)o<<',';output_move(o,bestdoublepath[k]);}
 o<<"],\"best_first_move_cap_feasible\":"<<(single[bestpath[0]]>=0?"true":"false")<<",\"cpu_seconds\":"<<cpu<<",\"threads\":1,\"single_feasible_moves\":[";
 for(unsigned k=0;k<singlevalid.size();k++){if(k)o<<',';o<<"{\"move\":";output_move(o,singlevalid[k].first);o<<",\"bad_pairs\":"<<singlevalid[k].second<<'}';}
 o<<"]}\n";
 std::cout<<"ordered doubles "<<ordered<<", final cap feasible "<<feasible<<", unique endpoints "<<unique<<", best distinct neighbor "<<best<<", CPU "<<cpu<<'\n';
}

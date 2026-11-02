// Complete unrestricted simple-graph two-edge-switch neighborhoods.
// Deterministic best strict descent, no fiber constraints, no annealing.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <utility>
#include <vector>
using State=std::array<uint64_t,60>;
using Edge=std::pair<int,int>;
struct Change {std::array<Edge,2> removed,added;};
struct Scan {int before,best=100000;long long pairs=0,disjoint=0,valid=0,blocked=0;bool complete=true;std::map<int,long long>hist;State bestgraph{};Change move{};double cpu=0;};
int n;uint64_t all;
Edge norm(int a,int b){return std::minmax(a,b);}
void toggle(State&g,Edge e){auto [a,b]=e;g[a]^=1ULL<<b;g[b]^=1ULL<<a;}
int score(const State&g){int total=0;for(int u=0;u<n;u++){uint64_t reach=g[u]|(1ULL<<u),todo=g[u];while(todo){int v=__builtin_ctzll(todo);todo&=todo-1;reach|=g[v];}total+=__builtin_popcountll(all&~reach);}assert(total%2==0);return total/2;}
void save(const State&g,const std::string&path){std::ofstream o(path);assert(o);o<<n<<' '<<4*n<<'\n';int count=0;for(int u=0;u<n;u++){assert(__builtin_popcountll(g[u])==8);for(int v=u+1;v<n;v++)if(g[u]>>v&1){o<<u<<' '<<v<<'\n';count++;}}assert(count==4*n);}
void edgejson(std::ostream&o,Edge e){o<<'['<<e.first<<','<<e.second<<']';}
void changejson(std::ostream&o,const Change&c){o<<"{\"removed\":[";edgejson(o,c.removed[0]);o<<',';edgejson(o,c.removed[1]);o<<"],\"added\":[";edgejson(o,c.added[0]);o<<',';edgejson(o,c.added[1]);o<<"]}";}
Scan scan(const State&state,clock_t start,double budget){
 Scan r;r.before=score(state);clock_t local=clock();State g=state;std::vector<Edge>edges;
 for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(g[u]>>v&1)edges.emplace_back(u,v);
 for(unsigned e=0;e<edges.size();e++)for(unsigned f=e+1;f<edges.size();f++){
  r.pairs++;auto [a,b]=edges[e];auto [c,d]=edges[f];if(a==c||a==d||b==c||b==d)continue;r.disjoint++;
  for(int mode=0;mode<2;mode++){
   Change ch{{edges[e],edges[f]},mode==0?std::array<Edge,2>{norm(a,c),norm(b,d)}:std::array<Edge,2>{norm(a,d),norm(b,c)}};
   if((g[ch.added[0].first]>>ch.added[0].second&1)||(g[ch.added[1].first]>>ch.added[1].second&1)){r.blocked++;continue;}
   for(auto x:ch.removed){toggle(g,x);}
   for(auto x:ch.added){toggle(g,x);}
   int energy=score(g);r.hist[energy]++;r.valid++;
   if(energy<r.best){r.best=energy;r.bestgraph=g;r.move=ch;}
   for(auto x:ch.added){toggle(g,x);}
   for(auto x:ch.removed){toggle(g,x);}
   if((r.valid&2047)==0 && double(clock()-start)/CLOCKS_PER_SEC>=budget){r.complete=false;r.cpu=double(clock()-local)/CLOCKS_PER_SEC;return r;}
  }
 }
 assert(g==state);r.cpu=double(clock()-local)/CLOCKS_PER_SEC;return r;
}
int main(int argc,char**argv){
 assert(argc==5);std::string source=argv[1],prefix=argv[2];int maxsteps=std::stoi(argv[3]);double budget=std::stod(argv[4]);
 std::ifstream in(source);int m;in>>n>>m;assert((n==59||n==60)&&m==4*n);all=(1ULL<<n)-1;State state{};int u,v,count=0;
 while(in>>u>>v){assert(0<=u&&u<v&&v<n&&!(state[u]>>v&1));toggle(state,{u,v});count++;}assert(count==m);for(int u=0;u<n;u++)assert(__builtin_popcountll(state[u])==8);
 const int initial=score(state);int steps=0;clock_t start=clock();std::vector<Scan>scans;std::vector<std::string>saved;std::string stop;
 while(true){
  Scan result=scan(state,start,budget);scans.push_back(result);
  if(!result.complete){stop="cpu_budget_during_neighborhood";break;}
  if(result.best>=result.before){stop="no_strict_improvement";std::string path=prefix+".best_distinct_neighbor.edges";save(result.bestgraph,path);saved.push_back(path);break;}
  state=result.bestgraph;steps++;std::string path=prefix+".step"+std::to_string(steps)+".edges";save(state,path);saved.push_back(path);
  if(result.best==0){stop="valid_target_found";break;}
  if(steps>=maxsteps){stop="strict_improvement_step_limit";break;}
  if(double(clock()-start)/CLOCKS_PER_SEC>=budget){stop="cpu_budget_after_complete_neighborhood";break;}
 }
 std::ofstream o(prefix+".json");o<<"{\"source\":\""<<source<<"\",\"n\":"<<n<<",\"m\":"<<m<<",\"scope\":\"unrestricted degree-preserving simple-graph two-edge switches; deterministic steepest strict descent\",\"seed_bad_pairs\":"<<initial<<",\"final_bad_pairs\":"<<score(state)<<",\"accepted_strict_steps\":"<<steps<<",\"maximum_steps\":"<<maxsteps<<",\"cpu_budget_seconds\":"<<budget<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"stop_reason\":\""<<stop<<"\",\"threads\":1,\"saved_candidates\":[";
 for(unsigned i=0;i<saved.size();i++){if(i)o<<',';o<<'"'<<saved[i]<<'"';}o<<"],\"neighborhoods\":[";
 for(unsigned i=0;i<scans.size();i++){if(i)o<<',';const auto&r=scans[i];o<<"{\"index\":"<<i<<",\"seed_bad_pairs\":"<<r.before<<",\"complete\":"<<(r.complete?"true":"false")<<",\"unordered_edge_pairs\":"<<r.pairs<<",\"disjoint_edge_pairs\":"<<r.disjoint<<",\"existing_edge_rejections\":"<<r.blocked<<",\"valid_distinct_switches\":"<<r.valid<<",\"best_distinct_neighbor_bad_pairs\":"<<r.best<<",\"best_change\":";changejson(o,r.move);o<<",\"cpu_seconds\":"<<r.cpu<<",\"bad_pair_histogram\":{";bool comma=false;for(auto [energy,num]:r.hist){if(comma)o<<',';comma=true;o<<'"'<<energy<<"\":"<<num;}o<<"}}";}
 o<<"]}\n";
 std::cout<<"n "<<n<<" initial "<<initial<<" final "<<score(state)<<" accepted "<<steps<<" scans "<<scans.size()<<" stop "<<stop<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
 return 0;
}

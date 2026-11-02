// Bounded, nonexhaustive construction diagnostic. Positive objective is not a target graph.
// New neighborhood: alternating cycles on 4--7 disjoint edges, mixed with 2-switches.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using Graph=std::array<uint64_t,58>;
constexpr uint64_t all=(uint64_t(1)<<58)-1;
void toggle(Graph&g,int u,int v){g[u]^=uint64_t(1)<<v;g[v]^=uint64_t(1)<<u;}
int objective(const Graph&g,Graph&missing){
 int s=0;
 for(int u=0;u<58;++u){uint64_t cover=g[u]|(uint64_t(1)<<u),bits=g[u];
  while(bits){int v=__builtin_ctzll(bits);bits&=bits-1;cover|=g[v];}
  missing[u]=all&~cover;s+=__builtin_popcountll(missing[u]);}
 return s/2;
}
int bit(uint64_t bits,std::mt19937_64&rng){int j=rng()%__builtin_popcountll(bits);while(j--)bits&=bits-1;return __builtin_ctzll(bits);}
void save(const Graph&g,const std::string&path){std::ofstream out(path);out<<"58 232\n";for(int u=0;u<58;++u)for(int v=u+1;v<58;++v)if(g[u]>>v&1)out<<u<<' '<<v<<'\n';}
// k disjoint existing edges a_i b_i become a_i b_(i+1 mod k).
// Every endpoint loses one edge and gains one; new edges are absent and distinct.
bool propose(const Graph&g,const Graph&missing,int k,std::mt19937_64&rng,std::array<int,7>&a,std::array<int,7>&b){
 uint64_t used=0;
 if((rng()&1)==0){
  int u=rng()%58;for(int j=0;j<58&&!missing[u];++j)u=(u+1)%58;
  if(!missing[u])return false;
  int v=bit(missing[u],rng),x=bit(g[u],rng);
  a[0]=x;b[0]=bit(g[x]&~(uint64_t(1)<<u),rng);b[1]=v;a[1]=bit(g[v],rng);
  for(int z:{a[0],b[0],a[1],b[1]}){if(used>>z&1)return false;used|=uint64_t(1)<<z;}
 }else{
  a[0]=rng()%58;b[0]=bit(g[a[0]],rng);used=(uint64_t(1)<<a[0])|(uint64_t(1)<<b[0]);
  a[1]=rng()%58;b[1]=bit(g[a[1]],rng);
  if((used>>a[1]&1)||(used>>b[1]&1))return false;
  used|=(uint64_t(1)<<a[1])|(uint64_t(1)<<b[1]);
 }
 for(int i=2;i<k;++i){
  bool found=false;
  for(int tries=0;tries<8&&!found;++tries){a[i]=rng()%58;if(used>>a[i]&1)continue;uint64_t available=g[a[i]]&~used;if(!available)continue;b[i]=bit(available,rng);found=true;}
  if(!found)return false;
  used|=(uint64_t(1)<<a[i])|(uint64_t(1)<<b[i]);
 }
 for(int i=0;i<k;++i)if(g[a[i]]>>b[(i+1)%k]&1)return false;
 return true;
}
struct Stats{uint64_t proposals=0,legal=0,accepted=0,uphill=0;int max_delta=0;};
int main(int argc,char**argv){
 if(argc!=5){std::cerr<<"usage: input.edges total_seconds seed output_prefix\n";return 2;}
 double budget=std::stod(argv[2]);if(budget<=0||budget>75)return 3;
 uint64_t rngseed=std::stoull(argv[3]);std::string prefix=argv[4];std::mt19937_64 rng(rngseed);
 Graph start{};std::ifstream in(argv[1]);int n,m;if(!(in>>n>>m)||n!=58||m!=232)return 4;
 for(int i=0,u,v;i<m;++i){if(!(in>>u>>v)||u<0||u>=58||v<0||v>=58||u==v||(start[u]>>v&1))return 5;toggle(start,u,v);}
 for(auto x:start)if(__builtin_popcountll(x)!=8)return 6;
 Graph bestgraph=start,missing{},candidateMissing{};int initial=objective(start,missing),best=initial;
 save(bestgraph,prefix+".best.edges");
 std::ofstream output(prefix+".raw.json");output<<"{\n\"status\":\"nonexhaustive_construction_diagnostic\",\n\"mechanism\":\"alternating_cycles_k4_to_k7_and_k2_with_uphill_acceptance\",\n\"rng_seed\":"<<rngseed<<",\n\"wall_budget_seconds\":"<<budget<<",\n\"initial_uncovered_pairs\":"<<initial<<",\n\"rounds\":[\n";
 auto begin=std::chrono::steady_clock::now();auto elapsed=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();};
 int rounds=6;
 for(int round=0;round<rounds&&best>0;++round){
  Graph g=start;int current=objective(g,missing),roundbest=current,highest=current;Graph roundbestgraph=g;
  double tmax=round%3==0?1.8:(round%3==1?3.0:5.0),tmin=0.08;
  std::array<Stats,8>stats{};uint64_t proposals=0;double t=elapsed(),roundstart=t,roundend=budget*(round+1)/rounds;
  while(best>0){
   if((proposals&1023)==0){t=elapsed();if(t>=roundend)break;}
   // Every round cools geometrically; 40% proposals cross >=4-edge neighborhoods.
   double phase=std::min(1.0,(t-roundstart)/(roundend-roundstart));
   double temperature=tmax*std::pow(tmin/tmax,phase);
   int k=rng()%10<6?2:4+rng()%4;++proposals;++stats[k].proposals;
   std::array<int,7>a{},b{};if(!propose(g,missing,k,rng,a,b))continue;++stats[k].legal;
   for(int i=0;i<k;++i){toggle(g,a[i],b[i]);toggle(g,a[i],b[(i+1)%k]);}
   int candidate=objective(g,candidateMissing),delta=candidate-current;
   if(delta<=0||std::generate_canonical<double,53>(rng)<std::exp(-delta/temperature)){
    ++stats[k].accepted;if(delta>0){++stats[k].uphill;stats[k].max_delta=std::max(stats[k].max_delta,delta);}
    current=candidate;missing=candidateMissing;highest=std::max(highest,current);
    if(current<roundbest){roundbest=current;roundbestgraph=g;}
    if(current<best){best=current;bestgraph=g;save(bestgraph,prefix+".best.edges");std::cout<<"improved "<<best<<" at "<<elapsed()<<"s\n"<<std::flush;}
   }else for(int i=0;i<k;++i){toggle(g,a[i],b[i]);toggle(g,a[i],b[(i+1)%k]);}
  }
  save(g,prefix+".round"+std::to_string(round)+".final.edges");
  if(round)output<<",\n";
  output<<"{\"round\":"<<round<<",\"start\":\"brown57_plus_absolute_hub\",\"temperature_max\":"<<tmax<<",\"temperature_min\":"<<tmin<<",\"elapsed_seconds\":"<<elapsed()-roundstart<<",\"best_uncovered_pairs\":"<<roundbest<<",\"final_uncovered_pairs\":"<<current<<",\"highest_accepted_uncovered_pairs\":"<<highest<<",\"by_cycle_length\":{";
  bool first=true;for(int k:{2,4,5,6,7}){if(!first)output<<',';first=false;auto&s=stats[k];output<<'"'<<k<<"\":{\"proposals\":"<<s.proposals<<",\"legal\":"<<s.legal<<",\"accepted\":"<<s.accepted<<",\"uphill_accepted\":"<<s.uphill<<",\"max_accepted_uphill_delta\":"<<s.max_delta<<'}';}output<<"}}"<<std::flush;
  std::cout<<"round "<<round<<" final="<<current<<" best="<<roundbest<<" high="<<highest<<" elapsed="<<elapsed()<<"\n"<<std::flush;
 }
 output<<"],\n\"elapsed_seconds\":"<<elapsed()<<",\n\"best_uncovered_pairs\":"<<best<<",\n\"valid_target_claimed\":false}\n";
 return 0;
}

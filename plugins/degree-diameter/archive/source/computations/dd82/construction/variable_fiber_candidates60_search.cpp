// One bounded search in orbit 4, preserving every internal and cross degree.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <utility>
#include <vector>
using Edge=std::pair<int,int>;
using Adj=std::array<uint64_t,60>;
struct Block{int i,j;std::vector<Edge> edges;};
struct State{Adj adj{};std::vector<Block> blocks;};
struct Score{int bad,zero;int energy()const{return 4*bad+zero;}};
struct Progress{double cpu;long long valid;int bad,zero,energy;};
std::array<uint64_t,60> zero_targets{};
constexpr uint64_t all=(uint64_t(1)<<60)-1;
volatile std::sig_atomic_t interrupted=0;
void stop(int){interrupted=1;}
void remove(State&s,Edge e){assert(s.adj[e.first]>>e.second&1);s.adj[e.first]^=uint64_t(1)<<e.second;s.adj[e.second]^=uint64_t(1)<<e.first;}
void add(State&s,Edge e){assert(!(s.adj[e.first]>>e.second&1));s.adj[e.first]|=uint64_t(1)<<e.second;s.adj[e.second]|=uint64_t(1)<<e.first;}
Score score(const State&s){
 int bad=0,zero=0;
 for(int u=0;u<60;u++){
  uint64_t reach=s.adj[u]|(uint64_t(1)<<u),todo=s.adj[u];
  while(todo){int v=__builtin_ctzll(todo);todo&=todo-1;reach|=s.adj[v];}
  uint64_t missing=all&~reach;bad+=__builtin_popcountll(missing);zero+=__builtin_popcountll(missing&zero_targets[u]);
 }
 assert(bad%2==0&&zero%2==0);return {bad/2,zero/2};
}
void write(const std::string&path,const State&s){
 std::ofstream out(path);out<<"60 240\n";int count=0;
 for(int u=0;u<60;u++){assert(__builtin_popcountll(s.adj[u])==8);for(int v=u+1;v<60;v++)if(s.adj[u]>>v&1){out<<u<<' '<<v<<'\n';count++;}}
 assert(count==240);
}
int main(int argc,char**argv){
 assert(argc==4);std::signal(SIGTERM,stop);std::signal(SIGINT,stop);
 std::ifstream domain(argv[1]);int id;domain>>id;assert(id==4);int d[6],q[6][6],defect[6][6],block_index[6][6];
 for(int&i:d)domain>>i;for(auto&row:q)for(int&x:row)domain>>x;for(auto&row:defect)for(int&x:row)domain>>x;
 State state;
 for(int i=0;i<6;i++)for(int j=i;j<6;j++){
  block_index[i][j]=block_index[j][i]=-1;
  if((i==j?d[i]:q[i][j])>0){block_index[i][j]=block_index[j][i]=state.blocks.size();state.blocks.push_back({i,j,{}});}
 }
 std::ifstream input(argv[2]);int n,m;input>>n>>m;assert(n==60&&m==240);
 for(int k=0;k<m;k++){int u,v;input>>u>>v;add(state,{u,v});int bi=block_index[u/10][v/10];assert(bi>=0);state.blocks[bi].edges.push_back({u,v});}
 for(int u=0;u<60;u++)for(int j=0;j<6;j++)if(defect[u/10][j]==0)zero_targets[u]|=((uint64_t(1)<<10)-1)<<(10*j);
 const std::string prefix=argv[3];const double budget=27.0;clock_t start=clock();
 std::mt19937_64 rng(2026101204ULL);auto uniform=[&](){return (rng()>>11)*0x1.0p-53;};
 State best_energy=state,best_bad=state,best_zero=state;
 Score current=score(state),energy_score=current,bad_score=current,zero_score=current;
 const Score initial=current;
 long long trials=0,valid=0,accepted=0,internal_valid=0,bipartite_valid=0,resets=0;
 std::vector<Progress>progress;progress.push_back({0,0,current.bad,current.zero,current.energy()});
 int epoch=0,kick=0;double elapsed=0,temperature=8.8;
 while(!interrupted){
  if((trials&1023)==0){
   elapsed=double(clock()-start)/CLOCKS_PER_SEC;if(elapsed>=budget||bad_score.bad==0)break;
   int next_epoch=int(elapsed/3.0);
   if(next_epoch!=epoch){epoch=next_epoch;state=best_energy;current=energy_score;kick=24;resets++;}
   double fraction=(elapsed-3.0*epoch)/3.0;
   temperature=4*2.2*std::pow(0.06/2.2,fraction);
  }
  trials++;int bi=rng()%state.blocks.size();auto&b=state.blocks[bi];int count=b.edges.size();if(count<2)continue;
  int i=rng()%count,j=rng()%(count-1);if(j>=i)j++;
  Edge e=b.edges[i],f=b.edges[j];int a=e.first,c=e.second,x=f.first,y=f.second;
  if(b.i==b.j&&rng()%2)std::swap(x,y);
  if(a==x||a==y||c==x||c==y)continue;
  Edge ne=std::minmax(a,y),nf=std::minmax(x,c);
  if((state.adj[ne.first]>>ne.second&1)||(state.adj[nf.first]>>nf.second&1))continue;
  remove(state,e);remove(state,f);add(state,ne);add(state,nf);valid++;
  if(b.i==b.j)internal_valid++;else bipartite_valid++;
  Score next=score(state);int delta=next.energy()-current.energy();
  bool take=kick>0||delta<=0||uniform()<std::exp(-delta/temperature);
  if(take){
   accepted++;if(kick>0)kick--;b.edges[i]=ne;b.edges[j]=nf;current=next;
   if(current.energy()<energy_score.energy()){
    best_energy=state;energy_score=current;
    progress.push_back({double(clock()-start)/CLOCKS_PER_SEC,valid,current.bad,current.zero,current.energy()});
   }
   if(std::make_pair(current.bad,current.zero)<std::make_pair(bad_score.bad,bad_score.zero)){best_bad=state;bad_score=current;}
   if(std::make_pair(current.zero,current.bad)<std::make_pair(zero_score.zero,zero_score.bad)){best_zero=state;zero_score=current;}
  }else{remove(state,ne);remove(state,nf);add(state,e);add(state,f);}
 }
 elapsed=double(clock()-start)/CLOCKS_PER_SEC;
 write(prefix+".best_bad.edges",best_bad);write(prefix+".best_zero.edges",best_zero);write(prefix+".best_energy.edges",best_energy);
 std::ofstream out(prefix+".search.json");
 out<<"{\"orbit\":4,\"stop_reason\":\""<<(bad_score.bad==0?"target_found":interrupted?"interrupted":"cpu_budget")<<"\",\"complete_domain_exhaustion\":false,\"cpu_budget_seconds\":27,\"cpu_seconds\":"<<elapsed;
 out<<",\"random_seed\":2026101204,\"objective\":\"4*bad_pairs+bad_pairs_in_zero_defect_blocks\",\"annealing_epochs_seconds\":3,\"temperature_bad_pair_units\":[2.2,0.06],\"accepted_kicks_per_new_epoch\":24";
 out<<",\"trials\":"<<trials<<",\"valid_switches\":"<<valid<<",\"accepted_switches\":"<<accepted<<",\"internal_valid\":"<<internal_valid<<",\"bipartite_valid\":"<<bipartite_valid<<",\"restarts_from_best_energy\":"<<resets;
 auto print_score=[&](const char*name,Score s){out<<",\""<<name<<"\":{\"bad_pairs\":"<<s.bad<<",\"zero_block_bad_pairs\":"<<s.zero<<",\"energy\":"<<s.energy()<<'}';};
 print_score("seed",initial);print_score("best_bad",bad_score);print_score("best_zero",zero_score);print_score("best_energy",energy_score);
 out<<",\"energy_progress\":[";
 for(size_t i=0;i<progress.size();i++){if(i)out<<',';auto p=progress[i];out<<"{\"cpu\":"<<p.cpu<<",\"valid_switches\":"<<p.valid<<",\"bad_pairs\":"<<p.bad<<",\"zero_block_bad_pairs\":"<<p.zero<<",\"energy\":"<<p.energy<<'}';}
 out<<"]}\n";
 std::cout<<"orbit 4: seed "<<initial.bad<<" best "<<bad_score.bad<<" zero-block bad "<<bad_score.zero<<" valid switches "<<valid<<" CPU "<<elapsed<<'\n';
}

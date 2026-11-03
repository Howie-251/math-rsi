// Six fixed Petersen graphs, all fifteen inter-fiber matchings independent.
// One bounded repair experiment; score counts every unordered pair exactly.
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
using State=std::array<uint64_t,60>;
constexpr uint64_t ALL=(1ULL<<60)-1;
uint64_t fiber(int i){return 1023ULL<<(10*i);}
uint64_t reached(const State& s,int u){
  uint64_t r=s[u]|(1ULL<<u), a=s[u];
  while(a){int v=__builtin_ctzll(a);a&=a-1;r|=s[v];}
  return r;
}
int score(const State& s){int n=0;for(int u=0;u<60;u++)n+=60-__builtin_popcountll(reached(s,u));assert(!(n%2));return n/2;}
int pair_energy(const State& s,int u,int v){int c=__builtin_popcountll(s[u]&s[v]);return c*(c-1)/2+int(s[u]>>v&1)*c;}
int cycle_energy(const State& s){int e=-150;for(int u=0;u<60;u++)for(int v=u+1;v<60;v++)e+=pair_energy(s,u,v);return e;}
int cycle_delta(const State& a,const State& b){
  uint64_t changed=0;for(int u=0;u<60;u++)if(a[u]!=b[u])changed|=1ULL<<u;
  int delta=0;uint64_t todo=changed;
  while(todo){int u=__builtin_ctzll(todo);todo&=todo-1;
    for(int v=0;v<60;v++)if(v!=u&&(!(changed>>v&1)||v>u))delta+=pair_energy(b,u,v)-pair_energy(a,u,v);
  }return delta;
}
void switch_edges(State& s,int a,int b,int c,int d){
  assert(a/10==c/10&&b/10==d/10&&a/10!=b/10&&a!=c&&b!=d);
  assert((s[a]>>b&1)&&(s[c]>>d&1)&&!(s[a]>>d&1)&&!(s[c]>>b&1));
  s[a]^=(1ULL<<b)|(1ULL<<d);s[c]^=(1ULL<<b)|(1ULL<<d);
  s[b]^=(1ULL<<a)|(1ULL<<c);s[d]^=(1ULL<<a)|(1ULL<<c);
}
void random_move(State& s,std::mt19937& rng){
  int i=rng()%6,j=rng()%5;if(j>=i)j++;
  int a=10*i+rng()%10,c=10*i+rng()%9;if(c>=a)c++;
  int b=__builtin_ctzll(s[a]&fiber(j)),d=__builtin_ctzll(s[c]&fiber(j));
  switch_edges(s,a,b,c,d);
}
bool guided_move(State& s,std::mt19937& rng){
  int u=rng()%60;
  for(int tries=0;tries<60;tries++,u=(u+1)%60){
    uint64_t missing=ALL&~reached(s,u);if(!missing)continue;
    int pick=rng()%__builtin_popcountll(missing);while(pick--)missing&=missing-1;
    int v=__builtin_ctzll(missing),i=u/10,j=v/10;assert(i!=j);
    int k=rng()%6;while(k==i||k==j)k=(k+1)%6;
    int a=__builtin_ctzll(s[u]&fiber(k));
    int b=__builtin_ctzll(s[a]&fiber(j)),c=__builtin_ctzll(s[v]&fiber(k));
    switch_edges(s,a,b,c,v);return true;
  }
  return false;
}
void save(const std::string& prefix,const State& s,int e,long long it,double cpu,bool cycles){
  std::ofstream o(prefix+".json");o<<"{\"n\":60,\"score\":"<<e<<",\"objective\":\""<<(cycles?"2*C4+3*T-150":"uncovered_pairs")<<"\",\"uncovered_pairs\":"<<score(s)<<",\"cycle_energy\":"<<cycle_energy(s)<<",\"iteration\":"<<it<<",\"cpu_seconds_at_discovery\":"<<cpu<<",\"edges\":[";
  bool first=true;for(int u=0;u<60;u++)for(int v=u+1;v<60;v++)if(s[u]>>v&1){if(!first)o<<',';first=false;o<<'['<<u<<','<<v<<']';}o<<"]}\n";
}
int main(int argc,char**argv){
  assert(argc==4||argc==5);bool cycles=argc==5;assert(!cycles||std::string(argv[4])=="cycle");std::ifstream f(argv[1]);int n,m;f>>n>>m;assert(n==60&&m==240);
  State cur{};for(int e=0,u,v;e<m;e++){f>>u>>v;assert(u>=0&&u<60&&v>u&&v<60);cur[u]|=1ULL<<v;cur[v]|=1ULL<<u;}
  for(int u=0;u<60;u++){assert(__builtin_popcountll(cur[u])==8);for(int j=0;j<6;j++)assert(__builtin_popcountll(cur[u]&fiber(j))==(j==u/10?3:1));}
  double budget=std::stod(argv[2]);std::string prefix=argv[3];std::mt19937 rng(20261011);
  int e=cycles?cycle_energy(cur):score(cur),initial=score(cur),best=e,best_missing=initial;State bests=cur;long long it=0,accepted=0;clock_t start=clock();double cpu=0;
  save(prefix+".initial",cur,e,0,0,cycles);save(prefix+".best",cur,e,0,0,cycles);
  std::cout<<"initial "<<e<<std::endl;
  constexpr long long CYCLE=100000;
  while(cpu<budget&&best){
    if(it&&it%CYCLE==0){cur=bests;for(int k=0;k<5;k++)random_move(cur,rng);e=cycles?cycle_energy(cur):score(cur);}
    State next=cur;
    if(rng()%2)guided_move(next,rng);else random_move(next,rng);
    // A coupled two-matching proposal occasionally crosses a single-switch barrier.
    if(rng()%10==0)random_move(next,rng);
    int ne=cycles?e+cycle_delta(cur,next):score(next);double temperature=4.0*std::pow(0.15/4.0,double(it%CYCLE)/CYCLE);
    if(ne<=e||std::generate_canonical<double,32>(rng)<std::exp((e-ne)/temperature)){cur=next;e=ne;accepted++;}
    it++;
    if(e<best||(e==best&&score(cur)<best_missing)){best=e;best_missing=score(cur);bests=cur;cpu=double(clock()-start)/CLOCKS_PER_SEC;save(prefix+".best",cur,e,it,cpu,cycles);std::cout<<"best "<<e<<" bad_pairs "<<best_missing<<" iteration "<<it<<" cpu "<<cpu<<std::endl;}
    if(it%4096==0){cpu=double(clock()-start)/CLOCKS_PER_SEC;if(cycles)assert(e==cycle_energy(cur));}
  }
  cpu=double(clock()-start)/CLOCKS_PER_SEC;
  std::ofstream o(prefix+".search.json");o<<"{\"seed\":20261011,\"scope\":\"All 15 independent matchings between six fixed Petersen fibers; no fixed root matchings or C5 symmetry\",\"objective\":\""<<(cycles?"2*C4+3*T-150":"uncovered_pairs")<<"\",\"best_objective\":"<<best<<",\"initial_uncovered_pairs\":"<<initial<<",\"best_uncovered_pairs\":"<<score(bests)<<",\"best_cycle_energy\":"<<cycle_energy(bests)<<",\"proposals\":"<<it<<",\"accepted\":"<<accepted<<",\"cpu_seconds\":"<<cpu<<",\"cpu_budget_seconds\":"<<budget<<",\"threads\":1,\"complete_enumeration\":false}\n";
  std::cout<<"finished "<<best<<" cpu "<<cpu<<" proposals "<<it<<std::endl;
}

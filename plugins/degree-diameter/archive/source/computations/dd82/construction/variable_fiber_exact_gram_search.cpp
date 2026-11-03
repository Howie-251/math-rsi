// One combined run in five fixed catalogue cores. Four Gram blocks stay exact.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <utility>
#include <vector>
using Edge=std::pair<int,int>;
using Adj=std::array<uint64_t,60>;
struct Block{int i,j,kind;std::vector<Edge> edges;}; // 0 matching, 1 columns, 2 cubic
struct State{Adj adj{};std::vector<Block> blocks;};
struct Score{int bad,zero;int energy()const{return 4*bad+zero;}};
struct Progress{double cpu;int bad,zero;};
std::array<uint64_t,60> zero_targets{};
constexpr uint64_t all=(uint64_t(1)<<60)-1;
void remove(State&s,Edge e){assert(s.adj[e.first]>>e.second&1);s.adj[e.first]^=uint64_t(1)<<e.second;s.adj[e.second]^=uint64_t(1)<<e.first;}
void add(State&s,Edge e){assert(!(s.adj[e.first]>>e.second&1));s.adj[e.first]|=uint64_t(1)<<e.second;s.adj[e.second]|=uint64_t(1)<<e.first;}
void gram(const State&s){
 for(int i=0;i<4;i++)for(int u=10*i;u<10*i+10;u++)for(int v=u+1;v<10*i+10;v++)
  assert(__builtin_popcountll(s.adj[u]&s.adj[v])+int(s.adj[u]>>v&1)==1);
}
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
 gram(s);std::ofstream out(path);out<<"60 240\n";int count=0;
 for(int u=0;u<60;u++){assert(__builtin_popcountll(s.adj[u])==8);for(int v=u+1;v<60;v++)if(s.adj[u]>>v&1){out<<u<<' '<<v<<'\n';count++;}}
 assert(count==240);
}
int main(int argc,char**argv){
 assert(argc==2);const std::string dir=argv[1];std::ifstream domain(dir+"/domain.txt");
 int ncores,d[6],q[6][6],defect[6][6];domain>>ncores;assert(ncores==5);
 for(int&i:d)domain>>i;
 for(auto&row:q)for(int&x:row)domain>>x;
 for(auto&row:defect)for(int&x:row)domain>>x;
 for(int u=0;u<60;u++)for(int j=0;j<6;j++)if(defect[u/10][j]==0)zero_targets[u]|=((uint64_t(1)<<10)-1)<<(10*j);
 clock_t started=clock();const double total_budget=27.0;
 std::ofstream out(dir+"/search.json");
 out<<"{\"objective\":\"4*bad_pairs+bad_pairs_in_zero_defect_blocks\",\"complete_domain_exhaustion\":false,\"combined_cpu_budget\":27,\"core_budget\":5.4,\"cores\":[";
 for(int cid=0;cid<ncores;cid++){
  State state;int bi[6][6];for(auto&row:bi)for(int&x:row)x=-1;
  for(int i=0;i<6;i++)for(int j=i;j<6;j++){
   int kind=-1;
   if(i==j&&i>=4)kind=2;
   else if(i<j&&q[i][j]==1)kind=0;
   else if((i==0&&j==5)||(i==1&&j==4))kind=1;
   if(kind>=0){bi[i][j]=state.blocks.size();state.blocks.push_back({i,j,kind,{}});}
  }
  assert(state.blocks.size()==11);
  const std::string prefix=dir+"/core"+std::to_string(cid);
  std::ifstream input(prefix+".seed.edges");int n,m;input>>n>>m;assert(n==60&&m==240);
  for(int k=0;k<m;k++){int u,v;input>>u>>v;add(state,{u,v});int b=bi[u/10][v/10];if(b>=0)state.blocks[b].edges.push_back({u,v});}
  gram(state);Score current=score(state),bestes=current,bestbs=current,bestzs=current,initial=current;
  State beste=state,bestb=state,bestz=state;
  std::mt19937_64 rng(2026101250ULL+cid);auto uniform=[&](){return (rng()>>11)*0x1.0p-53;};
  const clock_t core_start=clock();double elapsed=0,temperature=8.8;
  long long trials=0,valid=0,accepted=0,gram_checks=1,moves[3]={0,0,0};int epoch=0,kick=0,resets=0;
  std::vector<Progress> progress{{0,current.bad,current.zero}};
  while(true){
   if((trials&511)==0){
    elapsed=double(clock()-core_start)/CLOCKS_PER_SEC;
    if(elapsed>=total_budget/ncores||bestbs.bad==0)break;
    int next_epoch=int(elapsed/1.8);
    if(next_epoch!=epoch){epoch=next_epoch;state=beste;current=bestes;kick=16;resets++;}
    double fraction=(elapsed-1.8*epoch)/1.8;temperature=4*2.2*std::pow(0.06/2.2,fraction);
   }
   trials++;int bindex=rng()%state.blocks.size();auto&block=state.blocks[bindex];
   std::array<int,4> indices{};std::array<Edge,4> old{},next{};int size=0;
   if(block.kind==1){
    int a=rng()%10,b=rng()%9;if(b>=a)b++;a+=10*block.j;b+=10*block.j;
    for(size_t k=0;k<block.edges.size();k++){
     auto e=block.edges[k];if(e.second!=a&&e.second!=b)continue;
     assert(size<4);indices[size]=k;old[size]=e;next[size]={e.first,e.second==a?b:a};size++;
    }
    assert(size==4);
   }else{
    int count=block.edges.size(),i=rng()%count,j=rng()%(count-1);if(j>=i)j++;
    Edge e=block.edges[i],f=block.edges[j];int a=e.first,c=e.second,x=f.first,y=f.second;
    if(block.kind==2&&rng()%2)std::swap(x,y);
    if(a==x||a==y||c==x||c==y)continue;
    Edge ne=std::minmax(a,y),nf=std::minmax(x,c);
    if((state.adj[ne.first]>>ne.second&1)||(state.adj[nf.first]>>nf.second&1))continue;
    indices[0]=i;indices[1]=j;old[0]=e;old[1]=f;next[0]=ne;next[1]=nf;size=2;
   }
   for(int k=0;k<size;k++)remove(state,old[k]);
   for(int k=0;k<size;k++)add(state,next[k]);
   valid++;moves[block.kind]++;gram(state);gram_checks++;
   Score ns=score(state);int delta=ns.energy()-current.energy();
   bool take=kick>0||delta<=0||uniform()<std::exp(-delta/temperature);
   if(take){
    accepted++;if(kick>0)kick--;for(int k=0;k<size;k++)block.edges[indices[k]]=next[k];current=ns;
    if(current.energy()<bestes.energy()){
     beste=state;bestes=current;progress.push_back({double(clock()-core_start)/CLOCKS_PER_SEC,current.bad,current.zero});
    }
    if(std::make_pair(current.bad,current.zero)<std::make_pair(bestbs.bad,bestbs.zero)){bestb=state;bestbs=current;}
    if(std::make_pair(current.zero,current.bad)<std::make_pair(bestzs.zero,bestzs.bad)){bestz=state;bestzs=current;}
   }else{
    for(int k=0;k<size;k++)remove(state,next[k]);
    for(int k=0;k<size;k++)add(state,old[k]);
   }
  }
  elapsed=double(clock()-core_start)/CLOCKS_PER_SEC;
  write(prefix+".best_bad.edges",bestb);write(prefix+".best_zero.edges",bestz);write(prefix+".best_energy.edges",beste);
  if(cid)out<<',';
  out<<"{\"core_id\":"<<cid<<",\"cpu_seconds\":"<<elapsed<<",\"stop_reason\":\""<<(bestbs.bad==0?"target_found":"cpu_budget")<<"\",\"random_seed\":"<<2026101250ULL+cid;
  out<<",\"trials\":"<<trials<<",\"valid_switches\":"<<valid<<",\"accepted_switches\":"<<accepted<<",\"exact_Gram_checks\":"<<gram_checks;
  out<<",\"matching_moves\":"<<moves[0]<<",\"column_swap_moves\":"<<moves[1]<<",\"cubic_moves\":"<<moves[2]<<",\"returns_to_best_energy\":"<<resets;
  auto print_score=[&](const char*name,Score s){out<<",\""<<name<<"\":{\"bad_pairs\":"<<s.bad<<",\"zero_block_bad_pairs\":"<<s.zero<<",\"energy\":"<<s.energy()<<'}';};
  print_score("seed",initial);print_score("best_bad",bestbs);print_score("best_zero",bestzs);print_score("best_energy",bestes);
  out<<",\"best_energy_progress\":[";
  for(size_t k=0;k<progress.size();k++){if(k)out<<',';auto p=progress[k];out<<"{\"cpu\":"<<p.cpu<<",\"bad_pairs\":"<<p.bad<<",\"zero_block_bad_pairs\":"<<p.zero<<'}';}
  out<<"]}";out.flush();
  std::cout<<"core "<<cid<<" seed "<<initial.bad<<" best "<<bestbs.bad<<" zero "<<bestbs.zero<<" valid "<<valid<<" CPU "<<elapsed<<std::endl;
 }
 out<<"],\"combined_cpu_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<"}\n";
}

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
#include <vector>
using namespace std;
constexpr int N=33,D=4,EXT=33,STARTS=8,STEPS=100000;
using Edge=array<int,2>;
array<array<int,D>,N> adj;
array<uint64_t,N> near1;
vector<Edge> edges;
array<array<Edge,EXT>,STARTS> starts;
clock_t began;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
struct Score{int lack,slots,bad;};
bool linked(int a,int b){return (near1[a]>>b)&1;}
void replace_neighbor(int a,int old,int now){
 auto it=find(adj[a].begin(),adj[a].end(),old);assert(it!=adj[a].end());*it=now;
 near1[a]&=~(1ULL<<old);near1[a]|=1ULL<<now;
}
void change(const Edge&a,const Edge&b){
 replace_neighbor(a[0],a[1],b[0]);replace_neighbor(a[1],a[0],b[1]);
 replace_neighbor(b[0],b[1],a[0]);replace_neighbor(b[1],b[0],a[1]);
}
Score score(){
 uint8_t a2[N][N]={};array<uint64_t,N> exact2{};
 for(int u=0;u<N;u++)for(int v:adj[u])for(int w:adj[v]){a2[u][w]++;exact2[u]|=1ULL<<w;}
 int lack=0,slots=0,orderedbad=0;
 constexpr uint64_t ALL=(1ULL<<N)-1;
 for(int u=0;u<N;u++){
  uint64_t exact3=0;for(int v:adj[u])exact3|=exact2[v];
  uint64_t uncovered=ALL&~exact3;
  while(uncovered){int v=__builtin_ctzll(uncovered);uncovered&=uncovered-1;
   int upper=(u==v)+3*int(linked(u,v))+9*int(a2[u][v]);
   if(upper<27){lack+=27-upper;slots++;}
  }
  uint64_t ball=(1ULL<<u)|near1[u]|exact2[u]|exact3;
  orderedbad+=N-__builtin_popcountll(ball);
 }
 assert(orderedbad%2==0);return {lack,slots,orderedbad/2};
}
void init(int start){
 near1.fill(0);array<int,N>degrees{};edges.clear();
 auto add=[&](int u,int v){adj[u][degrees[u]++]=v;adj[v][degrees[v]++]=u;near1[u]|=1ULL<<v;near1[v]|=1ULL<<u;};
 for(int g=0;g<11;g++)for(int a=0;a<3;a++)for(int b=a+1;b<3;b++)add(3*g+a,3*g+b);
 for(auto e:starts[start]){assert(e[0]/3!=e[1]/3);assert(!linked(e[0],e[1]));edges.push_back(e);add(e[0],e[1]);}
 for(int d:degrees)assert(d==4);
}
void savebest(const Score&s,int start,int step,long scores){
 ofstream f("best.edges");f<<N<<' '<<66<<'\n';int count=0;
 for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){f<<u<<' '<<v<<'\n';count++;}
 assert(count==66);
 ofstream j("best.json");j<<"{\"n\":33,\"m\":66,\"degree\":4,\"target_controller_D\":3,\"capacity_deficit_ordered\":"<<s.lack<<",\"insufficient_capacity_ordered_slots\":"<<s.slots<<",\"bad_unordered_pairs_gt3\":"<<s.bad<<",\"start\":"<<start<<",\"step\":"<<step<<",\"scores_at_save\":"<<scores<<",\"partial_control_system_only\":true}\n";
}
void exact_matrix_file(const string&name){
 int a2[N][N]={},a3[N][N]={};
 for(int u=0;u<N;u++)for(int v:adj[u])for(int w:adj[v])a2[u][w]++;
 for(int u=0;u<N;u++)for(int v:adj[u])for(int w=0;w<N;w++)a3[u][w]+=a2[v][w];
 ofstream f(name);
 for(int u=0;u<N;u++){for(int v=0;v<N;v++)f<<int(u==v)+3*int(linked(u,v))+9*a2[u][v]+27*a3[u][v]<<' ';f<<'\n';}
}
bool propose(mt19937_64&rng,int&i,int&j,Edge&a,Edge&b){
 i=rng()%EXT;j=rng()%EXT;if(i==j)return false;
 a=edges[i];b=edges[j];if(rng()&1)swap(b[0],b[1]);
 return a[0]!=b[0]&&a[0]!=b[1]&&a[1]!=b[0]&&a[1]!=b[1]
     &&a[0]/3!=b[0]/3&&a[1]/3!=b[1]/3&&!linked(a[0],b[0])&&!linked(a[1],b[1]);
}
void commit(int i,int j,const Edge&a,const Edge&b){
 edges[i]={a[0],b[0]};edges[j]={a[1],b[1]};
 for(int k:{i,j})if(edges[k][0]>edges[k][1])swap(edges[k][0],edges[k][1]);
}
int main(int argc,char**argv){
 ifstream input("inputs.txt");int n,s,m;input>>n>>s>>m;assert(n==N&&s==STARTS&&m==EXT);
 for(auto&start:starts)for(auto&e:start)input>>e[0]>>e[1];
 if(string(argv[1])=="calibrate"){
  init(0);auto v=score();savebest(v,0,-1,1);exact_matrix_file("first.capacity.txt");
  ifstream src("best.edges");ofstream dst("first.edges");dst<<src.rdbuf();
  ofstream f("first.score.json");f<<"{\"lack\":"<<v.lack<<",\"slots\":"<<v.slots<<",\"bad\":"<<v.bad<<"}\n";return 0;
 }
 double budget=stod(argv[2]);began=clock();
 long proposals=0,legal=0,accepted=0,scores=0;int completed=0,cursor_start=0,cursor_step=-1;
 bool hit=false,limited=false;Score global{1000000000,1000000000,1000000000};
 mt19937_64 rng(20261027548ULL);uniform_real_distribution<double>U(0.,1.);
 ofstream log("starts.jsonl");
 // Recompute the inexpensive initial score only for starts1..7. Start0 uses
 // the exact score already calibrated and saved as JSON in the driver.
 ifstream cachedfile("first.cached.txt");Score cached;cachedfile>>cached.lack>>cached.slots>>cached.bad;
 for(int start=0;start<STARTS&&!limited&&!hit;start++){
  cursor_start=start;cursor_step=-1;init(start);Score current=start==0?cached:score();scores++;
  if(current.lack<global.lack){global=current;savebest(global,start,-1,scores);}
  if(current.lack==0){hit=true;break;}
  int startbest=current.lack;
  for(int step=0;step<STEPS;step++){
   cursor_step=step;
   if((step&1023)==0&&cpu()>budget){limited=true;break;}
   proposals++;int i,j;Edge a,b;if(!propose(rng,i,j,a,b))continue;
   legal++;change(a,b);Score trial=score();scores++;
   if(trial.lack<global.lack){global=trial;savebest(global,start,step,scores);}
   if(trial.lack==0){hit=true;current=trial;break;}
   startbest=min(startbest,trial.lack);
   double phase=double(step%20000)/19999.,temperature=36.*pow(.05,phase);
   if(trial.lack<=current.lack||U(rng)<exp(double(current.lack-trial.lack)/temperature)){commit(i,j,a,b);current=trial;accepted++;}
   else{Edge c{a[0],b[0]},d{a[1],b[1]};change(c,d);}
  }
  if(!hit&&!limited)completed++;
  log<<"{\"start\":"<<start<<",\"best_capacity_deficit\":"<<startbest<<",\"final_capacity_deficit\":"<<current.lack<<",\"CPU_seconds_cumulative\":"<<cpu()<<"}\n";log.flush();
 }
 string status=hit?"FOUND_CAPACITY_FEASIBLE_CONTROL":limited?"CPU_LIMIT_PREFIX_NO_FEASIBLE_CONTROL":"COMPLETE_8_START_PROFILE_NO_FEASIBLE_CONTROL";
 ofstream f("production_terminal.json");
 f<<"{\"status\":\""<<status<<"\",\"running\":false,\"found_capacity_feasible_control\":"<<(hit?"true":"false")<<",\"starts_scope\":8,\"starts_completed\":"<<completed<<",\"proposals\":"<<proposals<<",\"legal_switch_candidates\":"<<legal<<",\"exact_all_root_capacity_scores\":"<<scores<<",\"accepted_moves\":"<<accepted<<",\"best_capacity_deficit_ordered\":"<<global.lack<<",\"best_insufficient_ordered_slots\":"<<global.slots<<",\"best_bad_unordered_pairs_gt3\":"<<global.bad<<",\"production_CPU_seconds\":"<<cpu()<<",\"scope_exhausted\":"<<(!hit&&!limited?"true":"false")<<",\"entire_controller_family_exhausted\":false,\"first_score_reused\":true,\"cursor\":{\"start\":"<<cursor_start<<",\"step\":"<<cursor_step<<"}}\n";
 cout<<status<<" bestL="<<global.lack<<" CPU="<<cpu()<<'\n';
}

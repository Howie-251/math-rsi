#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
constexpr int N0=252,N=254,D=5,ST=8,STEPS=10000;
using Edge=array<int,2>; using Bits=array<uint64_t,4>;
struct State{array<int,4> ids,flip;};
array<array<int,D>,N> baseline,adj;
array<Bits,N> b1,b2,b3;
vector<Edge> source;
array<State,ST> starts;
string out;
clock_t began;
uint64_t proposals=0,legal=0,scores=0,accepted=0;
int best=100000000,best_start=-1,best_step=-1;
State best_state;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
bool legal_state(const State&s){array<bool,N0> used{};for(int id:s.ids){for(int v:source[id]){if(used[v])return false;used[v]=true;}}return true;}
void replace(int u,int old,int now){auto it=find(adj[u].begin(),adj[u].end(),old);assert(it!=adj[u].end());*it=now;}
void build(const State&s){
 adj=baseline;
 for(int k=0;k<4;k++){
  auto e=source[s.ids[k]]; if(s.flip[k])swap(e[0],e[1]);
  replace(e[0],e[1],N0);replace(e[1],e[0],N0+1);
  adj[N0][k]=e[0];adj[N0+1][k]=e[1];
 }
 adj[N0][4]=N0+1;adj[N0+1][4]=N0;
 for(int v=0;v<N;v++){b1[v].fill(0);b1[v][v/64]|=1ULL<<(v%64);for(int u:adj[v])b1[v][u/64]|=1ULL<<(u%64);}
}
int score(array<int,N>*deficits=nullptr){
 for(int v=0;v<N;v++){b2[v]=b1[v];for(int u:adj[v])for(int k=0;k<4;k++)b2[v][k]|=b1[u][k];}
 for(int v=0;v<N;v++){b3[v]=b2[v];for(int u:adj[v])for(int k=0;k<4;k++)b3[v][k]|=b2[u][k];}
 int total=0;
 for(int v=0;v<N;v++){Bits ball=b3[v];for(int u:adj[v])for(int k=0;k<4;k++)ball[k]|=b3[u][k];int reachable=0;for(auto w:ball)reachable+=__builtin_popcountll(w);int miss=N-reachable;total+=miss;if(deficits)(*deficits)[v]=miss;}
 assert(total%2==0);return total/2;
}
vector<Edge> edges_now(){vector<Edge> e;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)e.push_back({u,v});sort(e.begin(),e.end());assert(e.size()==635);return e;}
void save(int value,int start,int step,const State&s){
 best=value;best_start=start;best_step=step;best_state=s;
 auto edges=edges_now();ofstream f(out+"/best.edges");f<<N<<' '<<edges.size()<<'\n';for(auto e:edges)f<<e[0]<<' '<<e[1]<<'\n';
 ofstream j(out+"/best.json");j<<"{\"n\":254,\"m\":635,\"degree\":5,\"target_D\":4,\"bad_unordered_pairs\":"<<value<<",\"start\":"<<start<<",\"step\":"<<step<<",\"scores_at_save\":"<<scores<<",\"deleted_source_edge_ids\":[";
 for(int k=0;k<4;k++){if(k)j<<',';j<<s.ids[k];}j<<"],\"orientations\":[";for(int k=0;k<4;k++){if(k)j<<',';j<<s.flip[k];}j<<"],\"oriented_deleted_edges\":[";
 for(int k=0;k<4;k++){auto e=source[s.ids[k]];if(s.flip[k])swap(e[0],e[1]);if(k)j<<',';j<<'['<<e[0]<<','<<e[1]<<']';}
 j<<"],\"new_vertices\":[252,253],\"new_edge_rule\":\"for each oriented deletion [u,v], add [252,u],[253,v]; also add [252,253]\",\"diameter\":\"pending root independent check\"}\n";
}
int main(int argc,char**argv){
 assert(argc==3);out=argv[1];double budget=stod(argv[2]);began=clock();
 ifstream f(out+"/source.edges");int n,m;f>>n>>m;assert(n==N0&&m==630);array<int,N> deg{};
 for(int k=0;k<m;k++){int u,v;f>>u>>v;source.push_back({u,v});baseline[u][deg[u]++]=v;baseline[v][deg[v]++]=u;}
 for(int v=0;v<N0;v++)assert(deg[v]==D);
 ifstream ss(out+"/starts.txt");for(auto&s:starts){for(int&i:s.ids)ss>>i;for(int&i:s.flip)ss>>i;assert(legal_state(s));}
 ifstream ef(out+"/first.expected.edges");ef>>n>>m;assert(n==N&&m==635);vector<Edge> expected;
 for(int k=0;k<m;k++){Edge e;ef>>e[0]>>e[1];expected.push_back(e);}sort(expected.begin(),expected.end());
 ifstream df(out+"/first.expected.deficits");array<int,N> expected_deficits;for(int&i:expected_deficits)df>>i;
 ofstream rows(out+"/starts.jsonl");int completed=0,cursorstart=0,cursorstep=-1;bool hit=false,limited=false;
 State current_state=starts[0];int current=0;
 for(int st=0;st<ST;st++){
  cursorstart=st;cursorstep=-1;current_state=starts[st];build(current_state);array<int,N> deficits;current=score(&deficits);scores++;
  if(st==0){assert(edges_now()==expected);assert(deficits==expected_deficits);ofstream c(out+"/first.cpp_calibration.json");c<<"{\"status\":\"MATCH\",\"complete_adjacency_equal\":true,\"all254_radius4_deficits_equal\":true,\"first_score_reused\":true,\"bad_pairs\":"<<current<<"}\n";}
  if(current<best)save(current,st,-1,current_state);if(current==0){hit=true;break;}
  mt19937_64 rng(202610272540ULL+st);int localbest=current;uint64_t localaccepted=0;
  for(int step=0;step<STEPS;step++){
   cursorstep=step;if((step&127)==0&&cpu()>=budget){limited=true;goto finish;}
   proposals++;State trial=current_state;int k=rng()%4;
   if(rng()&1)trial.flip[k]^=1;else {trial.ids[k]=rng()%source.size();trial.flip[k]=rng()&1;}
   if(!legal_state(trial))continue;legal++;build(trial);int value=score();scores++;localbest=min(localbest,value);
   if(value<best){save(value,st,step,trial);if(value==0){current_state=trial;current=value;hit=true;goto finish;}}
   double fraction=double(step)/double(STEPS-1);double temp=3.0*pow(0.01/3.0,fraction);
   if(value<=current||generate_canonical<double,53>(rng)<exp(double(current-value)/temp)){current_state=trial;current=value;accepted++;localaccepted++;}
  }
  completed++;rows<<"{\"start\":"<<st<<",\"proposals\":10000,\"best_bad_pairs\":"<<localbest<<",\"final_bad_pairs\":"<<current<<",\"accepted\":"<<localaccepted<<",\"CPU_seconds_cumulative\":"<<cpu()<<"}\n";rows.flush();cout<<"START_DONE "<<st<<" best "<<localbest<<" global "<<best<<endl;
 }
 finish:
 string status=hit?"FOUND_D4":limited?"CPU_LIMIT_PROFILE_PREFIX_NO_D4":"COMPLETE_8_START_PROFILE_NO_D4";
 ofstream t(out+"/terminal.json");t<<"{\"status\":\""<<status<<"\",\"running\":false,\"found_D4\":"<<(hit?"true":"false")<<",\"starts_planned\":8,\"starts_completed\":"<<completed<<",\"proposals\":"<<proposals<<",\"legal_trials\":"<<legal<<",\"all_root_radius4_scores\":"<<scores<<",\"accepted\":"<<accepted<<",\"best_bad_pairs\":"<<best<<",\"production_CPU_seconds\":"<<cpu()<<",\"scope_exhausted\":"<<(!hit&&!limited?"true":"false")<<",\"entire_source_extension_family_exhausted\":false,\"cursor\":{\"start\":"<<cursorstart<<",\"step\":"<<cursorstep<<"},\"current_score\":"<<current<<",\"current_deleted_ids\":[";for(int k=0;k<4;k++){if(k)t<<',';t<<current_state.ids[k];}t<<"],\"current_orientations\":[";for(int k=0;k<4;k++){if(k)t<<',';t<<current_state.flip[k];}t<<"],\"worker_count\":1,\"restarts\":0,\"pending\":[\"root independent final best graph check\"]}\n";
 cout<<status<<" best "<<best<<" CPU "<<cpu()<<endl;
}

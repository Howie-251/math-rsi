// One diamond plus nine triangles; only cross-block edges may be switched.
// A^3 > 0 is a necessary condition for the proposed 837-vertex affine lift.
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <utility>
#include <vector>
using namespace std;
constexpr int N=31, FIXED=32, EXTERNAL=30;
struct Graph {
 array<array<int,4>,N> adj{};
 array<uint32_t,N> mask{};
 vector<pair<int,int>> edges;
 bool has(int u,int v)const {return (mask[u]>>v)&1U;}
 void rebuild(){
  array<int,N> degree{};mask.fill(0);
  for(auto [u,v]:edges){adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;mask[u]|=1U<<v;mask[v]|=1U<<u;}
  for(int d:degree)if(d!=4)throw runtime_error("nonregular graph");
 }
 void replace(int u,int oldv,int newv){
  for(int& v:adj[u])if(v==oldv){v=newv;mask[u]^=(1U<<oldv)|(1U<<newv);return;}
  throw runtime_error("missing edge");
 }
 void exchange(int k,int l,int a,int b,int c,int d){
  replace(a,b,c);replace(b,a,d);replace(c,d,a);replace(d,c,b);
  edges[k]={a,c};edges[l]={b,d};
 }
 int score()const {
  array<uint32_t,N> reach2{};
  for(int u=0;u<N;u++)for(int a:adj[u])reach2[u]|=mask[a];
  int zeros=0;
  for(int u=0;u<N;u++){
   uint32_t reach3=0;for(int a:adj[u])reach3|=reach2[a];
   zeros+=N-__builtin_popcount(reach3);
  }
  return zeros;
 }
};
int main(int argc,char** argv){
 if(argc!=4){cerr<<"usage: seconds seed output_prefix\n";return 2;}
 double budget=stod(argv[1]);unsigned long seed=stoul(argv[2]);string prefix=argv[3];
 mt19937_64 rng(seed);uniform_real_distribution<double> uniform(0,1);
 auto start=clock();auto elapsed=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 // Reserve a small margin below the external 120-second CPU hard limit.
 const double stop=budget-0.2;
 array<int,N> block{};vector<pair<int,int>> internal={{0,1},{0,2},{0,3},{1,2},{1,3}};
 for(int k=0;k<9;k++){
  int a=4+3*k;for(int i=a;i<a+3;i++)block[i]=k+1;
  internal.push_back({a,a+1});internal.push_back({a,a+2});internal.push_back({a+1,a+2});
 }
 vector<int> stubs;array<int,N> degree{};
 for(auto [u,v]:internal){degree[u]++;degree[v]++;}
 for(int u=0;u<N;u++)for(int k=degree[u];k<4;k++)stubs.push_back(u);
 if(internal.size()!=FIXED||stubs.size()!=2*EXTERNAL)throw runtime_error("bad specification");
 auto initial=[&](){
  while(true){
   auto ss=stubs;shuffle(ss.begin(),ss.end(),rng);Graph g;g.edges=internal;
   array<uint32_t,N> used{};bool valid=true;
   for(int k=0;k<(int)ss.size();k+=2){
    int a=ss[k],b=ss[k+1];
    if(block[a]==block[b]||((used[a]>>b)&1U)){valid=false;break;}
    used[a]|=1U<<b;used[b]|=1U<<a;g.edges.push_back({a,b});
   }
   if(valid){g.rebuild();return g;}
  }
 };
 Graph best;int bestscore=N*N;long long proposals=0,evaluations=0,accepted=0,starts=0;
 auto save=[&](const string& status){
  ofstream ef(prefix+".edges");ef<<N<<' '<<best.edges.size()<<'\n';
  for(auto [u,v]:best.edges)ef<<min(u,v)<<' '<<max(u,v)<<'\n';
  ofstream jf(prefix+".json");
  jf<<"{\"status\":\""<<status<<"\",\"scope\":\"fixed diamond plus nine triangles; cross-block 2-switches only; necessary lift condition\","
    <<"\"order\":31,\"degree\":4,\"fixed_internal_edges\":32,\"external_edges\":30,\"seed\":"<<seed
    <<",\"budget_cpu_seconds\":"<<budget<<",\"elapsed_cpu_seconds\":"<<elapsed()
    <<",\"proposals\":"<<proposals<<",\"evaluated_legal_switches\":"<<evaluations
    <<",\"accepted_switches\":"<<accepted<<",\"initializations\":"<<starts
    <<",\"zero_entries_A3\":"<<bestscore<<",\"target_lift_order\":837,\"target_lift_degree\":12,\"target_lift_diameter\":3}\n";
 };
 // One declared profile and seed, with ten scheduled 12-CPU-second segments.
 while(elapsed()<stop&&bestscore>0){
  Graph g=initial();int score=g.score();starts++;double local_start=elapsed();long long local=0;
  if(score<bestscore){bestscore=score;best=g;save("running");}
  while(elapsed()<stop&&elapsed()-local_start<12&&bestscore>0){
   proposals++;int k=FIXED+rng()%EXTERNAL,l=FIXED+rng()%EXTERNAL;
   auto [a,b]=g.edges[k];auto [c,d]=g.edges[l];if(rng()&1)swap(c,d);
   if(a==c||a==d||b==c||b==d||block[a]==block[c]||block[b]==block[d]||g.has(a,c)||g.has(b,d))continue;
   g.exchange(k,l,a,b,c,d);int fresh=g.score();evaluations++;local++;
   double phase=(local%30000)/30000.0;double temperature=3.5*pow(0.04,phase);
   if(fresh<=score||uniform(rng)<exp((score-fresh)/temperature)){score=fresh;accepted++;}
   else g.exchange(k,l,a,c,b,d);
   if(score<bestscore){
    bestscore=score;best=g;save(bestscore==0?"found_necessary_controller":"running");
    cout<<"best "<<bestscore<<" evaluations "<<evaluations<<" cpu_seconds "<<elapsed()<<endl;
   }
  }
 }
 save(bestscore==0?"found_necessary_controller":"budget_complete");
 cout<<"terminal best "<<bestscore<<" evaluations "<<evaluations<<" cpu_seconds "<<elapsed()<<endl;
}

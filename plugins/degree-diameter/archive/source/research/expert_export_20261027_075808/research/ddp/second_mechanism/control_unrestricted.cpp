// Unrestricted simple 4-regular controllers; A^3 > 0 is only a necessary lift condition.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <utility>
#include <vector>
using namespace std;
volatile sig_atomic_t interrupted=0;
void on_signal(int){interrupted=1;}
struct Graph {
 int n; vector<array<int,4>> adj; vector<pair<int,int>> edges;
 vector<vector<int>> matrix;
 explicit Graph(int n_):n(n_),adj(n_),matrix(n_,vector<int>(n_)){}
 bool has(int u,int v)const {for(int w:adj[u])if(w==v)return true;return false;}
 void rebuild(){
  vector<int> degree(n,0);
  for(auto [u,v]:edges){adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;}
  for(int d:degree)if(d!=4)throw runtime_error("nonregular input");
 }
 void replace(int u,int oldv,int newv){for(int& v:adj[u])if(v==oldv){v=newv;return;}throw runtime_error("missing edge");}
 int score(){
  for(auto& row:matrix)fill(row.begin(),row.end(),0);
  for(int u=0;u<n;u++)for(int a:adj[u])for(int b:adj[a])for(int v:adj[b])matrix[u][v]++;
  int zeros=0;for(auto& row:matrix)for(int x:row)zeros+=x==0;return zeros;
 }
 void switch_edges(int k,int l,int a,int b,int c,int d){
  replace(a,b,c);replace(b,a,d);replace(c,d,a);replace(d,c,b);
  edges[k]={a,c};edges[l]={b,d};
 }
};
int main(int argc,char** argv){
 if(argc==3 && string(argv[1])=="check"){
  ifstream f(argv[2]);int n,m;f>>n>>m;Graph g(n);
  for(int i=0,u,v;i<m;i++){f>>u>>v;g.edges.push_back({u,v});}
  g.rebuild();int zero=g.score();cout<<"{\"order\":"<<n<<",\"zero_entries\":"<<zero<<",\"A3\":[";
  for(int i=0;i<n;i++){if(i)cout<<',';cout<<'[';for(int j=0;j<n;j++){if(j)cout<<',';cout<<g.matrix[i][j];}cout<<']';}cout<<"]}\n";return 0;
 }
 if(argc!=5){cerr<<"usage: n seconds seed output_prefix | check input.edges\n";return 2;}
 int n=stoi(argv[1]);double budget=stod(argv[2]);unsigned long seed=stoul(argv[3]);string prefix=argv[4];
 mt19937_64 rng(seed);uniform_real_distribution<double> uniform(0,1);
 signal(SIGTERM,on_signal);signal(SIGINT,on_signal);
 auto start=chrono::steady_clock::now();auto elapsed=[&](){return chrono::duration<double>(chrono::steady_clock::now()-start).count();};
 Graph best(n);int bestscore=n*n;long long iterations=0,restarts=0;
 auto save=[&](const string& status){
  ofstream ef(prefix+".edges");ef<<n<<' '<<best.edges.size()<<'\n';for(auto [u,v]:best.edges)ef<<min(u,v)<<' '<<max(u,v)<<'\n';
  ofstream jf(prefix+".json");jf<<"{\"status\":\""<<status<<"\",\"scope\":\"unrestricted simple 4-regular controller; necessary condition only\",\"order\":"<<n<<",\"seed\":"<<seed<<",\"budget_seconds\":"<<budget<<",\"elapsed_seconds\":"<<elapsed()<<",\"iterations\":"<<iterations<<",\"restarts\":"<<restarts<<",\"zero_entries_A3\":"<<bestscore<<",\"A3\":[";
  best.score();for(int i=0;i<n;i++){if(i)jf<<',';jf<<'[';for(int j=0;j<n;j++){if(j)jf<<',';jf<<best.matrix[i][j];}jf<<']';}jf<<"]}\n";
 };
 while(elapsed()<budget&&!interrupted&&bestscore>0){
  Graph g(n);for(int u=0;u<n;u++)for(int s:{1,2})g.edges.push_back({u,(u+s)%n});g.rebuild();
  // Randomize without imposing or preserving any triangle blocks.
  for(int t=0;t<2000;t++){
   int k=rng()%g.edges.size(),l=rng()%g.edges.size();auto [a,b]=g.edges[k];auto [c,d]=g.edges[l];if(rng()&1)swap(c,d);
   if(a==c||a==d||b==c||b==d||g.has(a,c)||g.has(b,d))continue;g.switch_edges(k,l,a,b,c,d);
  }
  int score=g.score();restarts++;double restart_start=elapsed();long long local=0;
  while(elapsed()<budget && elapsed()-restart_start<12 && !interrupted && bestscore>0){
   int k=rng()%g.edges.size(),l=rng()%g.edges.size();auto [a,b]=g.edges[k];auto [c,d]=g.edges[l];if(rng()&1)swap(c,d);
   if(a==c||a==d||b==c||b==d||g.has(a,c)||g.has(b,d))continue;
   g.switch_edges(k,l,a,b,c,d);int fresh=g.score();iterations++;local++;
   double phase=(local%30000)/30000.0;double temp=3.5*pow(0.04,phase);
   if(fresh<=score||uniform(rng)<exp((score-fresh)/temp))score=fresh;
   else g.switch_edges(k,l,a,c,b,d);
   if(score<bestscore){bestscore=score;best=g;best.score();save(bestscore==0?"found_necessary_controller":"running");cout<<"order "<<n<<" best "<<bestscore<<" iterations "<<iterations<<" seconds "<<elapsed()<<endl;}
  }
 }
 save(bestscore==0?"found_necessary_controller":interrupted?"interrupted":"budget_complete");
 cout<<"terminal order "<<n<<" best "<<bestscore<<" iterations "<<iterations<<" seconds "<<elapsed()<<endl;
}

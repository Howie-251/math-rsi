// F2^3 affine-line controller profile. Necessary conditions only; no affine charts.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <utility>
#include <vector>
using namespace std;
volatile sig_atomic_t interrupted=0;
void on_signal(int){interrupted=1;}
struct Graph {
 int n; vector<array<int,6>> adj; vector<pair<int,int>> edges;vector<int>A2,A3;
 explicit Graph(int x):n(x),adj(x),A2(x*x),A3(x*x){}
 bool has(int u,int v)const {for(int w:adj[u])if(w==v)return true;return false;}
 void rebuild(){vector<int>degree(n);for(auto [u,v]:edges){if(u==v||degree[u]>=6||degree[v]>=6)throw runtime_error("invalid edges");adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;}for(int d:degree)if(d!=6)throw runtime_error("nonregular input");}
 void replace(int u,int oldv,int newv){for(int&v:adj[u])if(v==oldv){v=newv;return;}throw runtime_error("missing edge");}
 int score(){
  fill(A2.begin(),A2.end(),0);fill(A3.begin(),A3.end(),0);
  for(int u=0;u<n;u++)for(int a:adj[u])for(int b:adj[a]){A2[u*n+b]++;for(int v:adj[b])A3[u*n+v]++;}
  int deficit=0;
  // Adjacent entries always pass. Diagonal capacity requires the stronger union bound.
  for(int u=0;u<n;u++){
   deficit+=A3[u*n+u]==0;
   for(int v=u+1;v<n;v++)if(!has(u,v))deficit+=2*max(0,8-8*A3[u*n+v]-4*A2[u*n+v]);
  }
  return deficit;
 }
 void sw(int k,int l,int a,int b,int c,int d){replace(a,b,c);replace(b,a,d);replace(c,d,a);replace(d,c,b);edges[k]={a,c};edges[l]={b,d};}
};
void matrix(ostream&o,const vector<int>&A,int n){o<<'[';for(int i=0;i<n;i++){if(i)o<<',';o<<'[';for(int j=0;j<n;j++){if(j)o<<',';o<<A[i*n+j];}o<<']';}o<<']';}
int main(int argc,char**argv){
 if(argc==3&&string(argv[1])=="check"){
  ifstream f(argv[2]);int n,m;f>>n>>m;Graph g(n);for(int i=0,u,v;i<m;i++){f>>u>>v;g.edges.push_back({u,v});}g.rebuild();int s=g.score();cout<<"{\"order\":"<<n<<",\"score\":"<<s<<",\"A2\":";matrix(cout,g.A2,n);cout<<",\"A3\":";matrix(cout,g.A3,n);cout<<"}\n";return 0;
 }
 if(argc!=5){cerr<<"usage: n seconds seed output_prefix | check input.edges\n";return 2;}
 int n=stoi(argv[1]);double budget=stod(argv[2]);unsigned long seed=stoul(argv[3]);string prefix=argv[4];
 mt19937_64 rng(seed);uniform_real_distribution<double>uniform(0,1);signal(SIGTERM,on_signal);signal(SIGINT,on_signal);
 auto start=chrono::steady_clock::now();auto elapsed=[&](){return chrono::duration<double>(chrono::steady_clock::now()-start).count();};
 Graph best(n);int bestscore=8*n*n;long long iterations=0,restarts=0;
 auto save=[&](string status){
  best.score();int tzero=0,badpairs=0,capacitydeficit=0;for(int u=0;u<n;u++){tzero+=best.A3[u*n+u]==0;for(int v=u+1;v<n;v++)if(!best.has(u,v)&&2*best.A3[u*n+v]+best.A2[u*n+v]<2){badpairs++;capacitydeficit+=2*(8-8*best.A3[u*n+v]-4*best.A2[u*n+v]);}}
  ofstream ef(prefix+".edges");ef<<n<<' '<<best.edges.size()<<'\n';for(auto[u,v]:best.edges)ef<<min(u,v)<<' '<<max(u,v)<<'\n';
  ofstream jf(prefix+".json");jf<<"{\"status\":\""<<status<<"\",\"scope\":\"simple6regular F2^3 affine-line controller; necessary conditions only\",\"order\":"<<n<<",\"proposed_lift_order\":"<<8*n<<",\"seed\":"<<seed<<",\"budget_seconds\":"<<budget<<",\"elapsed_seconds\":"<<elapsed()<<",\"iterations\":"<<iterations<<",\"restarts\":"<<restarts<<",\"optimistic_missing_with_union_diagonal\":"<<bestscore<<",\"capacity_deficit\":"<<capacitydeficit<<",\"triangle_free_vertices\":"<<tzero<<",\"bad_unordered_nondiagonal_pairs\":"<<badpairs<<",\"A2\":";matrix(jf,best.A2,n);jf<<",\"A3\":";matrix(jf,best.A3,n);jf<<"}\n";
 };
 while(elapsed()<budget&&!interrupted&&bestscore>0){
  Graph g(n);for(int u=0;u<n;u++)for(int s:{1,2,3})g.edges.push_back({u,(u+s)%n});g.rebuild();
  for(int t=0;t<5000;t++){int k=rng()%g.edges.size(),l=rng()%g.edges.size();auto[a,b]=g.edges[k];auto[c,d]=g.edges[l];if(rng()&1)swap(c,d);if(a==c||a==d||b==c||b==d||g.has(a,c)||g.has(b,d))continue;g.sw(k,l,a,b,c,d);}
  int score=g.score();restarts++;double restart_start=elapsed();long long local=0;
  while(elapsed()<budget&&elapsed()-restart_start<15&&!interrupted&&bestscore>0){
   int k=rng()%g.edges.size(),l=rng()%g.edges.size();auto[a,b]=g.edges[k];auto[c,d]=g.edges[l];if(rng()&1)swap(c,d);if(a==c||a==d||b==c||b==d||g.has(a,c)||g.has(b,d))continue;
   g.sw(k,l,a,b,c,d);int fresh=g.score();iterations++;local++;
   double phase=(local%40000)/40000.0,temp=18.0*pow(0.015,phase);
   if(fresh<=score||uniform(rng)<exp((score-fresh)/temp))score=fresh;else g.sw(k,l,a,c,b,d);
   if(score<bestscore){bestscore=score;best=g;save(bestscore==0?"found_necessary_controller":"running");cout<<"order "<<n<<" best "<<bestscore<<" iterations "<<iterations<<" seconds "<<elapsed()<<endl;}
  }
 }
 save(bestscore==0?"found_necessary_controller":interrupted?"interrupted":"budget_complete");cout<<"terminal order "<<n<<" best "<<bestscore<<" iterations "<<iterations<<" seconds "<<elapsed()<<endl;
}

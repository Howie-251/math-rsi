#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
constexpr int Q=43,G=86,N=172,D=7;
int mod(int x){x%=Q;return x<0?x+Q:x;}
int mul(int a,int b){return mod(a%Q+(a/Q?-1:1)*(b%Q))+Q*((a/Q)^(b/Q));}
int inv(int a){return mod((a/Q?1:-1)*(a%Q))+Q*(a/Q);}
struct Pattern{int id,k,p0,p1,odd,dim;};
struct Trial{Pattern p;vector<int>x;int score=100000,miss0=0,miss1=0,diameter=0;};
array<array<int,D>,N> adj;
long long legal=0,illegal=0,initial_legal=0,optimization_legal=0;
clock_t started;
bool timeout=false,hit=false;
Trial best;
mt19937 rng(2026102623u);
ofstream logstream;
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
bool build(const Pattern&p,const vector<int>&x){
 vector<int>s[2],t;int at=0;
 for(int side=0;side<2;side++){
  int pairs=side?p.p1:p.p0;
  for(int i=0;i<pairs;i++){int a=x[at++];s[side].push_back(a);s[side].push_back(inv(a));}
  for(int i=0;i<p.k-2*pairs;i++)s[side].push_back(x[at++]+Q);
  set<int>check(s[side].begin(),s[side].end());
  if(int(check.size())!=p.k||check.count(0))return false;
 }
 int cross=D-p.k;
 for(int i=0;i<cross;i++)t.push_back((i?x[at++]:0)+(i>=cross-p.odd?Q:0));
 if(int(set<int>(t.begin(),t.end()).size())!=cross)return false;
 if(at!=p.dim)abort();
 for(int v=0;v<G;v++){
  int a=0,b=0;
  for(int z:s[0])adj[v][a++]=mul(v,z);
  for(int z:t)adj[v][a++]=G+mul(v,z);
  for(int z:s[1])adj[G+v][b++]=G+mul(v,z);
  for(int z:t)adj[G+v][b++]=mul(v,inv(z));
  if(a!=D||b!=D)abort();
 }
 return true;
}
int bfs(int root,int&diameter){
 array<int,N>dist;dist.fill(-1);array<int,N>queue;int head=0,tail=1;
 queue[0]=root;dist[root]=0;
 while(head<tail){int v=queue[head++];for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;queue[tail++]=w;}}
 int missing=0;for(int d:dist){missing+=d<0||d>3;diameter=max(diameter,d);}
 if(tail<N)diameter=N;
 return missing;
}
void save_best(){
 build(best.p,best.x);
 ofstream e("profile.best.edges");e<<N<<' '<<N*D/2<<'\n';
 for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)e<<u<<' '<<v<<'\n';
 ofstream f("profile.best.json");f<<"{\n\"pattern_id\":"<<best.p.id<<",\"internal_degree\":"<<best.p.k
 <<",\"pair_counts\":["<<best.p.p0<<','<<best.p.p1<<"],\"odd_cross\":"<<best.p.odd
 <<",\"field_values\":[";for(size_t i=0;i<best.x.size();i++)f<<(i?",":"")<<best.x[i];
 f<<"],\"n\":172,\"degree\":7,\"diameter\":"<<best.diameter<<",\"root_misses\":["<<best.miss0<<','<<best.miss1
 <<"],\"score\":"<<best.score<<",\"bad_unordered_pairs\":"<<43*best.score<<",\"legal_evaluation_index\":"<<legal<<"}\n";
}
bool evaluate(Trial&t,bool initial){
 if((legal+illegal)%2048==0&&cpu()>88){timeout=true;return false;}
 if(!build(t.p,t.x)){illegal++;return false;}
 legal++;if(initial)initial_legal++;else optimization_legal++;
 t.diameter=0;t.miss0=bfs(0,t.diameter);t.miss1=bfs(G,t.diameter);t.score=t.miss0+t.miss1;
 if(t.score<best.score){best=t;save_best();logstream<<"best "<<legal<<' '<<best.p.id<<' '<<best.score<<' '<<cpu()<<endl;}
 if(t.score==0)hit=true;
 return true;
}
vector<int> random_fields(const Pattern&p){
 vector<int>x(p.dim);for(int&v:x)v=rng()%Q;
 // The first internal reflection is an admissible common-translation anchor.
 int anchor=p.p0;int c=mod(-x[anchor]*22);int at=0;
 for(int side=0;side<2;side++){
  int pairs=side?p.p1:p.p0;
  at+=pairs;for(int i=0;i<p.k-2*pairs;i++,at++)x[at]=mod(x[at]+2*c);
 }
 int cross=D-p.k;
 for(int i=1;i<cross;i++,at++)if(i>=cross-p.odd)x[at]=mod(x[at]+2*c);
 if(at!=p.dim||x[anchor]!=0)abort();
 return x;
}
int main(){
 started=clock();logstream.open("profile.log");
 vector<Pattern>patterns;ifstream input("profile.patterns.txt");Pattern p;
 while(input>>p.id>>p.k>>p.p0>>p.p1>>p.odd>>p.dim)patterns.push_back(p);
 if(patterns.size()!=9)return 2;
 vector<Trial>seeds;
 for(auto p:patterns)for(int j=0;j<16&&!timeout&&!hit;j++){
  Trial t;t.p=p;do{t.x=random_fields(p);}while(!evaluate(t,true)&&!timeout);
  if(!timeout)seeds.push_back(t);
 }
 ofstream checkpoint("profile.initial.json");checkpoint<<"{\"legal\":"<<initial_legal<<",\"best_score\":"<<best.score<<",\"CPU_seconds\":"<<cpu()<<"}\n";checkpoint.close();
 int completed=0;
 for(auto seed:seeds){
  if(timeout||hit)break;Trial current=seed;
  for(int kick=0;kick<9&&!timeout&&!hit;kick++){
   if(kick){
    do{current=seed;for(int j=0;j<2;j++){int c;do{c=rng()%current.p.dim;}while(c==current.p.p0);current.x[c]=rng()%Q;}}
    while(!evaluate(current,false)&&!timeout);
   }
   for(int step=0;step<30&&!timeout&&!hit;step++){
    Trial next=current;
    for(int c=0;c<current.p.dim&&!timeout&&!hit;c++)if(c!=current.p.p0)
     for(int value=0;value<Q&&!timeout&&!hit;value++)if(value!=current.x[c]){
      Trial t=current;t.x[c]=value;if(evaluate(t,false)&&t.score<next.score)next=t;
     }
    if(next.score>=current.score)break;current=next;
   }
  }
  completed++;logstream<<"seed_done "<<completed<<' '<<legal<<' '<<best.score<<' '<<cpu()<<endl;
 }
 if(best.score<100000)save_best();
 ofstream f("profile.terminal.json");f<<"{\"status\":\""<<(hit?"HIT_D3":timeout?"BUDGET_STOP":"COMPLETE_BOUNDED_PROFILE")
 <<"\",\"patterns\":9,\"initial_legal_evaluations\":"<<initial_legal<<",\"optimization_legal_evaluations\":"<<optimization_legal
 <<",\"legal_evaluations\":"<<legal<<",\"illegal_evaluations\":"<<illegal<<",\"completed_seeds\":"<<completed
 <<",\"seeds\":"<<seeds.size()<<",\"best_score\":"<<best.score<<",\"CPU_seconds\":"<<cpu()<<",\"running\":false}\n";
 cout<<"status "<<(hit?"HIT":timeout?"BUDGET_STOP":"COMPLETE")<<" legal "<<legal<<" best "<<best.score<<" CPU "<<cpu()<<endl;
}

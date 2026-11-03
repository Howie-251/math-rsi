// Exact radius-five score for a graph with one movable degree deficit.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
constexpr int MAXN=651,W=11;
using Bits=array<unsigned long long,W>;
struct Graph{int n;array<array<int,5>,MAXN>adj;array<int,MAXN>deg{};int deficit=-1;};
struct Score{vector<int>bad;int total()const{return bad.size();}};
struct Move{int d,x,y;};
array<Bits,MAXN>b2,b3;
mt19937_64 rng(20261028);
volatile sig_atomic_t stopped=0;
void stop_signal(int){stopped=1;}
int choose(int k){return rng()%k;}
bool adjacent(const Graph&g,int x,int y){return find(g.adj[x].begin(),g.adj[x].begin()+g.deg[x],y)!=g.adj[x].begin()+g.deg[x];}
void add(Graph&g,int x,int y){g.adj[x][g.deg[x]++]=y;g.adj[y][g.deg[y]++]=x;}
void remove(Graph&g,int x,int y){for(auto[u,v]:{pair{x,y},pair{y,x}}){int i=find(g.adj[u].begin(),g.adj[u].begin()+g.deg[u],v)-g.adj[u].begin();g.adj[u][i]=g.adj[u][--g.deg[u]];}}
void apply(Graph&g,Move m){remove(g,m.x,m.y);add(g,m.d,m.x);g.deficit=m.y;}
void undo(Graph&g,Move m){remove(g,m.d,m.x);add(g,m.x,m.y);g.deficit=m.d;}
Score score(const Graph&g){
 for(int x=0;x<g.n;x++){
  b2[x].fill(0);b2[x][x/64]|=1ULL<<(x%64);
  for(int k=0;k<g.deg[x];k++){int y=g.adj[x][k];b2[x][y/64]|=1ULL<<(y%64);for(int j=0;j<g.deg[y];j++){int z=g.adj[y][j];b2[x][z/64]|=1ULL<<(z%64);}}
 }
 for(int x=0;x<g.n;x++){
  b3[x]=b2[x];for(int k=0;k<g.deg[x];k++){int y=g.adj[x][k];for(int j=0;j<W;j++)b3[x][j]|=b2[y][j];}
 }
 Score s;s.bad.reserve(256);
 for(int x=0;x<g.n;x++)for(int y=x+1;y<g.n;y++){
  bool hit=false;for(int j=0;j<W;j++)if(b2[x][j]&b3[y][j]){hit=true;break;}if(!hit)s.bad.push_back(x*g.n+y);
 }
 return s;
}
Move propose(const Graph&g,const Score&s){
 int d=g.deficit,x=-1;
 if(choose(100)<60&&!s.bad.empty()){
  array<int,MAXN>dd,q;dd.fill(99);dd[d]=0;int head=0,end=1;q[0]=d;
  while(head<end){int u=q[head++];for(int j=0;j<g.deg[u];j++){int v=g.adj[u][j];if(dd[v]==99){dd[v]=dd[u]+1;q[end++]=v;}}}
  int c=s.bad[choose(s.bad.size())],p=c/g.n,r=c%g.n;if(dd[r]<dd[p])swap(p,r);
  if(dd[p]<=4){x=r;int length=choose(5-dd[p]);for(int j=0;j<length;j++)x=g.adj[x][choose(g.deg[x])];}
 }
 if(x<0||x==d||adjacent(g,d,x))do{x=choose(g.n);}while(x==d||adjacent(g,d,x));
 return {d,x,g.adj[x][choose(g.deg[x])]};
}
void save(const string&prefix,const Graph&g,const Score&s,double cpu,long long steps){
 ofstream out(prefix+".json");out<<"{\"n\":"<<g.n<<",\"maximum_degree\":5,\"target_diameter\":5,\"exact_bad_unordered_pairs\":"<<s.total()<<",\"degree4_vertex\":"<<g.deficit<<",\"cpu_seconds\":"<<cpu<<",\"steps\":"<<steps<<"}\n";
 int m=0;for(int x=0;x<g.n;x++)m+=g.deg[x];ofstream e(prefix+".edges");e<<g.n<<" "<<m/2<<"\n";for(int x=0;x<g.n;x++)for(int j=0;j<g.deg[x];j++)if(x<g.adj[x][j])e<<x<<" "<<g.adj[x][j]<<"\n";
}
int main(int argc,char**argv){
 if(argc!=4){cerr<<"usage search INPUT_EDGES OUTPUT_PREFIX CPU_SECONDS\n";return 2;}
 signal(SIGTERM,stop_signal);signal(SIGINT,stop_signal);
 Graph g;ifstream in(argv[1]);int m;in>>g.n>>m;if(g.n>MAXN||g.n<1)return 2;
 for(int j=0;j<m;j++){int x,y;in>>x>>y;if(x==y||g.deg[x]>=5||g.deg[y]>=5||adjacent(g,x,y))return 2;add(g,x,y);}
 double limit=stod(argv[3]);int holes=0;for(int x=0;x<g.n;x++){if(g.deg[x]==4){holes++;g.deficit=x;}else if(g.deg[x]!=5)return 2;}
 if(limit>0&&(g.n!=651||holes!=1))return 2;
 string prefix=argv[2];clock_t start=clock();auto wall=chrono::steady_clock::now();auto elapsed=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 Score current=score(g),bestscore=current;Graph best=g;long long steps=0,accepted=0;vector<int>positive;
 if(limit<0){
  if(g.n!=651||holes!=1)return 2;
  int original=current.total(),improving=0,equal=0,worse=0,d=g.deficit;
  ofstream moves(prefix+".neighborhood.tsv");moves<<"x\ty\tbad_pairs\n";
  for(int x=0;x<g.n;x++)if(x!=d&&!adjacent(g,d,x)){
   auto neighbors=g.adj[x];int count=g.deg[x];
   for(int j=0;j<count;j++){
    Move p{d,x,neighbors[j]};apply(g,p);Score q=score(g);steps++;
    moves<<x<<"\t"<<p.y<<"\t"<<q.total()<<"\n";
    improving+=q.total()<original;equal+=q.total()==original;worse+=q.total()>original;
    if(q.total()<bestscore.total()){best=g;bestscore=q;}undo(g,p);
   }
  }
  double cpu=elapsed();save(prefix+".best",best,bestscore,cpu,steps);
  ofstream end(prefix+".terminal.json");end<<"{\"status\":\"COMPLETE_NEIGHBORHOOD\",\"neighbors\":"<<steps<<",\"source_bad_pairs\":"<<original<<",\"best_including_source\":"<<bestscore.total()<<",\"improving\":"<<improving<<",\"equal\":"<<equal<<",\"worse\":"<<worse<<",\"cpu_seconds\":"<<cpu<<"}\n";
  cout<<"complete neighborhood "<<steps<<" best "<<bestscore.total()<<" cpu "<<cpu<<endl;return 0;
 }
 if(limit>0)for(int i=0;i<256;i++){
  Move p=propose(g,current);apply(g,p);Score q=score(g);int delta=q.total()-current.total();if(delta>0)positive.push_back(delta);
  if(q.total()<bestscore.total()){best=g;bestscore=q;}undo(g,p);if(bestscore.total()==0)break;
 }
 sort(positive.begin(),positive.end());double temperature=positive.empty()?1:positive[positive.size()/2]/log(5.0);
 ofstream calibration(prefix+".calibration.json");calibration<<"{\"positive_deltas\":"<<positive.size()<<",\"median_positive_delta\":"<<(positive.empty()?0:positive[positive.size()/2])<<",\"initial_temperature\":"<<temperature<<"}\n";calibration.close();
 g=best;current=bestscore;int segment=-1;double last_log=-20;
 cout<<"initial exact badpairs "<<bestscore.total()<<" temperature "<<temperature<<endl;
 while(limit>0&&!stopped&&bestscore.total()>0){
  double cpu=elapsed();if(cpu>=limit)break;int next=min(5,int(cpu*6/limit));
  if(next!=segment){segment=next;g=best;current=bestscore;cout<<"segment "<<segment<<" cpu "<<cpu<<" best "<<bestscore.total()<<endl;}
  double phase=cpu*6/limit-segment,temp=temperature*pow(0.02,phase);
  Move p=propose(g,current);apply(g,p);Score q=score(g);steps++;int delta=q.total()-current.total();
  if(delta<=0||generate_canonical<double,53>(rng)<exp(-double(delta)/temp)){current=move(q);accepted++;}else undo(g,p);
  if(current.total()<bestscore.total()){best=g;bestscore=current;save(prefix+".best",best,bestscore,cpu,steps);cout<<"best "<<bestscore.total()<<" cpu "<<cpu<<" steps "<<steps<<endl;}
  if(cpu-last_log>=10){last_log=cpu;cout<<"progress cpu "<<cpu<<" current "<<current.total()<<" best "<<bestscore.total()<<" steps "<<steps<<endl;}
 }
 double cpu=elapsed();save(prefix+".best",best,bestscore,cpu,steps);save(prefix+".last",g,current,cpu,steps);
 string status=limit==0?"SCORED_ONLY":bestscore.total()==0?"FULL_DIAMETER_CANDIDATE":stopped?"INTERRUPTED":"BUDGET_EXHAUSTED";
 ofstream end(prefix+".terminal.json");end<<"{\"status\":\""<<status<<"\",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"best_bad_pairs\":"<<bestscore.total()<<",\"cpu_seconds\":"<<cpu<<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall).count()<<"}\n";
 cout<<"terminal "<<status<<" best "<<bestscore.total()<<" cpu "<<cpu<<endl;
}

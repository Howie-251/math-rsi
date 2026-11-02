// Joint six-matching search using a proved optimistic bad-pair lower bound.
// A zero lower bound is a filter hit, never a diameter certificate.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
constexpr int N=2810,K=6;
struct Pick{int edge;bool reverse;};
using State=array<Pick,K>;
struct Score{int old=0,nu=0,nv=0;vector<int> old_pairs,new_points;int total()const{return old+nu+nv;}};
vector<pair<int,int>> edges;
vector<vector<int>> incidence,critical;
vector<unsigned char> dist,a,b;
vector<uint32_t> seen;
uint32_t stamp=0;
mt19937_64 rng(20261027);
volatile sig_atomic_t stop_requested=0;
void stop_signal(int){stop_requested=1;}
int choose(int n){return int(rng()%n);}
pair<int,int> endpoints(Pick p){auto e=edges[p.edge];if(p.reverse)swap(e.first,e.second);return e;}
bool legal(const State&s){array<int,12>v;for(int i=0;i<K;i++){auto[x,y]=endpoints(s[i]);v[2*i]=x;v[2*i+1]=y;}sort(v.begin(),v.end());return adjacent_find(v.begin(),v.end())==v.end();}
Score evaluate(const State&s){
 fill(a.begin(),a.end(),5);fill(b.begin(),b.end(),5);
 for(Pick p:s){auto[x,y]=endpoints(p);const auto*dx=&dist[x*N];const auto*dy=&dist[y*N];for(int z=0;z<N;z++){a[z]=min(a[z],dx[z]);b[z]=min(b[z],dy[z]);}}
 Score out;out.old_pairs.reserve(600);out.new_points.reserve(50);
 for(int x=0;x<N;x++){
  if(a[x]>4&&b[x]>3){out.nu++;out.new_points.push_back(x);}
  if(b[x]>4&&a[x]>3){out.nv++;out.new_points.push_back(N+x);}
 }
 ++stamp;
 for(Pick p:s)for(int code:critical[p.edge]){
  if(seen[code]==stamp)continue;seen[code]=stamp;int x=code/N,y=code%N;
  if(a[x]+a[y]>3&&b[x]+b[y]>3&&a[x]+b[y]>2&&b[x]+a[y]>2){out.old++;out.old_pairs.push_back(code);}
 }
 return out;
}
Pick at_vertex(int v,int side){int eid=incidence[v][choose(incidence[v].size())];bool reverse=(edges[eid].second==v);if(side==1)reverse=!reverse;return {eid,reverse};}
int walk(int x,int length){for(int k=0;k<length;k++){auto[u,v]=edges[incidence[x][choose(incidence[x].size())]];x=(u==x?v:u);}return x;}
bool repair_one_pair(State&t,const State&s,int slot,int x,int y){
 if(dist[x*N+y]<4)return false;
 int ax=5,ay=5,bx=5,by=5;
 for(int j=0;j<K;j++)if(j!=slot){auto[p,q]=endpoints(s[j]);ax=min(ax,int(dist[p*N+x]));ay=min(ay,int(dist[p*N+y]));bx=min(bx,int(dist[q*N+x]));by=min(by,int(dist[q*N+y]));}
 // Each component specifies an endpoint whose new route to this pair,
 // together with an unchanged endpoint, has length at most five in G.
 vector<array<int,3>>balls;
 auto add=[&](int center,int radius,int side){if(radius>=0)balls.push_back({center,radius,side});};
 add(x,3-ay,0);add(y,3-ax,0);add(x,2-by,0);add(y,2-bx,0);
 add(x,3-by,1);add(y,3-bx,1);add(x,2-ay,1);add(y,2-ax,1);
 if(balls.empty())return false;
 auto[center,radius,side]=balls[choose(balls.size())];t[slot]=at_vertex(walk(center,choose(radius+1)),side);return true;
}
State proposal(const State&s,const Score&score){
 State t=s;int slot=choose(K),mode=choose(100);
 if(mode<15){t[slot].reverse=!t[slot].reverse;return t;}
 if(mode<40){t[slot]={choose(edges.size()),bool(choose(2))};return t;}
 if(mode<60){auto[x,y]=endpoints(s[slot]);int side=choose(2);t[slot]=at_vertex(side?y:x,side);return t;}
 if(mode<85){
  if(!score.old_pairs.empty()){
   int c=score.old_pairs[choose(score.old_pairs.size())],x=c/N,y=c%N;
   if(!repair_one_pair(t,s,slot,x,y)){
    int slot2=choose(K-1);if(slot2>=slot)slot2++;int side=choose(2);
    t[slot]=at_vertex(x,side);t[slot2]=at_vertex(y,side);
   }
  }else if(!score.new_points.empty()){
   int c=score.new_points[choose(score.new_points.size())];t[slot]=at_vertex(walk(c%N,3),c/N);
  }else t[slot]={choose(edges.size()),bool(choose(2))};
  return t;
 }
 int slot2=choose(K-1);if(slot2>=slot)slot2++;
 if(!score.old_pairs.empty()){
  int c=score.old_pairs[choose(score.old_pairs.size())],x=c/N,y=c%N,side=choose(2);
  if(choose(2))x=walk(x,1);if(choose(2))y=walk(y,1);
  t[slot]=at_vertex(x,side);t[slot2]=at_vertex(y,side);
 }else{
  t[slot]={choose(edges.size()),bool(choose(2))};t[slot2]={choose(edges.size()),bool(choose(2))};
 }
 return t;
}
void save(const string&prefix,const State&s,const Score&score,double cpu,long long steps){
 ofstream out(prefix+".json");out<<"{\"n\":2812,\"degree\":7,\"target_diameter\":5,\"optimistic_bad_pair_lower_bound\":"<<score.total()<<",\"mandatory_old_old\":"<<score.old<<",\"new_root_missing_lower_bounds\":["<<score.nu<<","<<score.nv<<"],\"cpu_seconds\":"<<cpu<<",\"steps\":"<<steps<<",\"matching\":[";
 for(int i=0;i<K;i++){auto[x,y]=endpoints(s[i]);if(i)out<<",";out<<"["<<x<<","<<y<<"]";}out<<"]}\n";
 set<pair<int,int>>graph(edges.begin(),edges.end());for(Pick p:s){auto[x,y]=endpoints(p);graph.erase(minmax(x,y));graph.insert({x,N});graph.insert({y,N+1});}graph.insert({N,N+1});
 ofstream e(prefix+".edges");e<<N+2<<" "<<graph.size()<<"\n";for(auto[x,y]:graph)e<<x<<" "<<y<<"\n";
}
int main(int argc,char**argv){
 if(argc!=7){cerr<<"usage: search BASE DIST PAIRS SEEDS OUTPUT_PREFIX CPU_SECONDS\n";return 2;}
 signal(SIGTERM,stop_signal);signal(SIGINT,stop_signal);
 ifstream in(argv[1]);int n,m;in>>n>>m;if(n!=N||m!=9835)return 2;edges.resize(m);incidence.resize(N);
 for(int e=0;e<m;e++){auto&[x,y]=edges[e];in>>x>>y;incidence[x].push_back(e);incidence[y].push_back(e);}
 dist.resize(N*N);ifstream raw(argv[2],ios::binary);raw.read((char*)dist.data(),dist.size());if(raw.gcount()!=N*N)return 2;
 ifstream cp(argv[3]);long long total;int cn,cm;cp>>cn>>cm>>total;if(cn!=N||cm!=m)return 2;critical.resize(m);long long actual=0;
 for(int e=0;e<m;e++){int eid,count;cp>>eid>>count;if(eid!=e)return 2;critical[e].resize(count);for(int&x:critical[e])cp>>x;actual+=count;}if(actual!=total)return 2;
 a.resize(N);b.resize(N);seen.resize(N*N);vector<State>seeds;
 ifstream sin(argv[4]);int ns;sin>>ns;for(int i=0;i<ns;i++){State s;for(Pick&p:s){int x,y;sin>>x>>y;auto key=minmax(x,y);auto it=lower_bound(edges.begin(),edges.end(),pair<int,int>(key));if(it==edges.end()||*it!=pair<int,int>(key))return 2;p={int(it-edges.begin()),x>y};}if(!legal(s))return 2;seeds.push_back(s);}
 string prefix=argv[5];double limit=stod(argv[6]);clock_t start=clock();auto wall_start=chrono::steady_clock::now();auto elapsed=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 State best=seeds.front();Score bs=evaluate(best);ofstream regression(prefix+".seed_scores.jsonl");
 for(int i=0;i<ns;i++){Score q=evaluate(seeds[i]);regression<<"{\"seed\":"<<i<<",\"lower_bound\":"<<q.total()<<",\"old_old\":"<<q.old<<",\"new_old\":["<<q.nu<<","<<q.nv<<"]}\n";if(q.total()<bs.total()){best=seeds[i];bs=move(q);}}
 State current=best;Score cs=bs;long long steps=0,accepted=0,illegal=0;vector<int>positive;
 // CPU_SECONDS=0 is a scoring/regression invocation, with no mutation search.
 if(limit>0)for(int j=0;j<256;j++){
  State t=proposal(current,cs);if(!legal(t))continue;Score ts=evaluate(t);int delta=ts.total()-cs.total();if(delta>0)positive.push_back(delta);
  if(ts.total()<bs.total()){best=t;bs=ts;}if(bs.total()==0)break;
 }
 sort(positive.begin(),positive.end());double temperature=positive.empty()?1.0:positive[positive.size()/2]/log(5.0);
 ofstream calibration(prefix+".calibration.json");calibration<<"{\"positive_deltas\":"<<positive.size()<<",\"median_positive_delta\":"<<(positive.empty()?0:positive[positive.size()/2])<<",\"initial_temperature\":"<<temperature<<"}\n";calibration.close();
 current=best;cs=bs;int segment=-1;double last_log=-20;
 cout<<"initial lower bound "<<bs.total()<<" old "<<bs.old<<" new "<<bs.nu+bs.nv<<" temperature "<<temperature<<endl;
 while(limit>0&&!stop_requested&&bs.total()>0){
  double cpu=elapsed();if(cpu>=limit)break;
  int next_segment=min(5,int(cpu*6/limit));if(next_segment!=segment){segment=next_segment;current=(segment==3?seeds[7%ns]:best);cs=evaluate(current);cout<<"segment "<<segment<<" cpu "<<cpu<<" start "<<cs.total()<<endl;}
  double fraction=cpu*6/limit-segment;double temp=temperature*pow(0.02,fraction);
  State t=proposal(current,cs);steps++;if(!legal(t)){illegal++;continue;}Score ts=evaluate(t);int delta=ts.total()-cs.total();
  if(delta<=0||generate_canonical<double,53>(rng)<exp(-double(delta)/temp)){current=t;cs=move(ts);accepted++;}
  if(cs.total()<bs.total()){best=current;bs=cs;save(prefix+".best",best,bs,cpu,steps);cout<<"best "<<bs.total()<<" old "<<bs.old<<" new "<<bs.nu+bs.nv<<" cpu "<<cpu<<" steps "<<steps<<endl;}
  if(cpu-last_log>=10){last_log=cpu;cout<<"progress cpu "<<cpu<<" best "<<bs.total()<<" current "<<cs.total()<<" steps "<<steps<<endl;}
 }
 double cpu=elapsed();save(prefix+".best",best,bs,cpu,steps);save(prefix+".last",current,cs,cpu,steps);
 string status=limit==0?"SCORED_ONLY":bs.total()==0?"NECESSARY_FILTER_HIT":stop_requested?"INTERRUPTED":"BUDGET_EXHAUSTED";
 ofstream end(prefix+".terminal.json");end<<"{\"status\":\""<<status<<"\",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"illegal\":"<<illegal<<",\"best_lower_bound\":"<<bs.total()<<",\"cpu_seconds\":"<<cpu<<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall_start).count()<<"}\n";
 cout<<"terminal "<<status<<" lower bound "<<bs.total()<<" cpu "<<cpu<<endl;
}

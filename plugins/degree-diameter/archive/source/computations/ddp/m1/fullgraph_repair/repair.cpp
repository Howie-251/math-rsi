// Exact distance-four repair of a full graph via intersections of radius-two balls.
#include <algorithm>
#include <chrono>
#include <cmath>
#include <csignal>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t stop_requested=0;void stop_handler(int){stop_requested=1;}
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage INPUT_EDGES SECONDS SEED OUTPUT_PREFIX\n";return 2;}
 int n,m;ifstream in(argv[1]);in>>n>>m;if(!in||n<2)return 2;vector<vector<int>>adj(n);for(int i=0,u,v;i<m;i++){in>>u>>v;if(!in||u<0||v<0||u>=n||v>=n||u==v||find(adj[u].begin(),adj[u].end(),v)!=adj[u].end())return 2;adj[u].push_back(v);adj[v].push_back(u);}
 int deg=adj[0].size();for(auto&a:adj)if(a.size()!=size_t(deg))return 2;
 const int words=(n+63)/64;vector<unsigned long long>balls(n*words);vector<unsigned char>bad(n*n);vector<int>pos(n*n,-1);vector<pair<int,int>>badpairs;
 auto build=[&](int u){auto*b=&balls[u*words];fill(b,b+words,0);b[u/64]|=1ULL<<(u%64);for(int v:adj[u]){b[v/64]|=1ULL<<(v%64);for(int w:adj[v])b[w/64]|=1ULL<<(w%64);}};
 auto isbad=[&](int u,int v){for(int k=0;k<words;k++)if(balls[u*words+k]&balls[v*words+k])return false;return true;};
 auto setbad=[&](int u,int v,bool value){if(u>v)swap(u,v);int idx=u*n+v;if(bool(bad[idx])==value)return;bad[idx]=bad[v*n+u]=value;if(value){pos[idx]=badpairs.size();badpairs.emplace_back(u,v);}else{int at=pos[idx];auto last=badpairs.back();badpairs[at]=last;pos[last.first*n+last.second]=at;badpairs.pop_back();pos[idx]=-1;}};
 for(int u=0;u<n;u++)build(u);for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(isbad(u,v))setbad(u,v,true);
 double limit=stod(argv[2]);mt19937_64 rng(stoull(argv[3]));string prefix=argv[4];auto t0=chrono::steady_clock::now();auto sec=[&](){return chrono::duration<double>(chrono::steady_clock::now()-t0).count();};
 int best=badpairs.size();unsigned long long steps=0,accepted=0;auto save=[&](){ofstream f(prefix+".edges");f<<n<<" "<<m<<"\n";for(int u=0;u<n;u++)for(int v:adj[u])if(u<v)f<<u<<" "<<v<<"\n";ofstream j(prefix+".json");j<<"{\"n\":"<<n<<",\"degree\":"<<deg<<",\"target_diameter\":4,\"bad_unordered_pairs\":"<<badpairs.size()<<",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"seconds_at_best\":"<<sec()<<"}\n";};save();cout<<"initial "<<best<<endl;
 auto linked=[&](int u,int v){return find(adj[u].begin(),adj[u].end(),v)!=adj[u].end();};auto replace=[&](int u,int from,int to){auto it=find(adj[u].begin(),adj[u].end(),from);if(it==adj[u].end())throw runtime_error("missing edge");*it=to;};
 struct Change{int u,v;bool value;};vector<unsigned char>affected(n);vector<int>roots;vector<unsigned long long>old;vector<Change>changes;
 signal(SIGINT,stop_handler);signal(SIGTERM,stop_handler);
 while(best>0&&!stop_requested&&sec()<limit){
  int a,b,c,d;if(!badpairs.empty()&&rng()%10<7){auto [u,v]=badpairs[rng()%badpairs.size()];if(rng()%2)swap(u,v);a=adj[u][rng()%deg];int x=adj[v][rng()%deg];c=adj[x][rng()%deg];do{b=adj[a][rng()%deg];}while(b==u);do{d=adj[c][rng()%deg];}while(d==x);}else{a=rng()%n;b=adj[a][rng()%deg];c=rng()%n;d=adj[c][rng()%deg];}
  if(a==c||a==d||b==c||b==d||linked(a,c)||linked(b,d))continue;++steps;
  fill(affected.begin(),affected.end(),0);roots.clear();auto mark=[&](int u){if(!affected[u]){affected[u]=1;roots.push_back(u);}};for(int u:{a,b,c,d}){mark(u);for(int v:adj[u])mark(v);}old.clear();for(int u:roots)old.insert(old.end(),balls.begin()+u*words,balls.begin()+(u+1)*words);
  replace(a,b,c);replace(b,a,d);replace(c,d,a);replace(d,c,b);for(int u:roots)build(u);
  int delta=0;changes.clear();for(int u:roots)for(int v=0;v<n;v++)if(u!=v&&(!affected[v]||u<v)){bool nb=isbad(u,v);if(nb!=bool(bad[u*n+v])){delta+=nb?1:-1;changes.push_back({u,v,nb});}}
  double temp=1.8*pow(.04,double(steps%50000)/50000.);
  if(delta<=0||generate_canonical<double,53>(rng)<exp(-double(delta)/temp)){++accepted;for(auto ch:changes)setbad(ch.u,ch.v,ch.value);if(int(badpairs.size())<best){best=badpairs.size();save();cout<<"best "<<best<<" steps "<<steps<<" sec "<<sec()<<endl;}}
  else{replace(a,c,b);replace(b,d,a);replace(c,a,d);replace(d,b,c);for(size_t i=0;i<roots.size();i++)copy(old.begin()+i*words,old.begin()+(i+1)*words,balls.begin()+roots[i]*words);}
  // A periodic exact rebuild diagnoses the incremental implementation, not graph acceptance.
  if(steps%20000==0){for(int u=0;u<n;u++){vector<unsigned long long>saved(balls.begin()+u*words,balls.begin()+(u+1)*words);build(u);if(!equal(saved.begin(),saved.end(),balls.begin()+u*words))throw runtime_error("ball cache mismatch");}int count=0;for(int u=0;u<n;u++)for(int v=u+1;v<n;v++){bool z=isbad(u,v);if(z!=bool(bad[u*n+v]))throw runtime_error("bad cache mismatch");count+=z;}if(count!=int(badpairs.size()))throw runtime_error("count mismatch");}
 }
 ofstream t(prefix+".terminal.json");t<<"{\"status\":\""<<(best==0?"CANDIDATE_COVERED":stop_requested?"STOPPED":"BUDGET_EXHAUSTED")<<"\",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"seconds\":"<<sec()<<",\"best_bad_pairs\":"<<best<<"}\n";cout<<"terminal "<<best<<" steps "<<steps<<" sec "<<sec()<<endl;
}

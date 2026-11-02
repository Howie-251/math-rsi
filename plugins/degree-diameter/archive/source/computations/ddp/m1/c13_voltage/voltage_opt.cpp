#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <csignal>
#include <fstream>
#include <iostream>
#include <map>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t stop_requested=0;
void handle_stop(int){stop_requested=1;}
struct Edge{int u,v,z,su,sv;};
struct Form{vector<pair<int,int>> terms;};
struct Lift{
 vector<Edge>edges;array<array<int,7>,702>adj{};
 array<unsigned,702>seen{};unsigned stamp=0;
 vector<vector<Form>>routes;
 void change(int eid,int z){auto&e=edges[eid];e.z=z;
  for(int x=0;x<13;x++){adj[e.u*13+x][e.su]=e.v*13+(x+z)%13;adj[e.v*13+x][e.sv]=e.u*13+(x-z+13)%13;}
 }
 int evaluate(vector<int>*missing=nullptr){
  if(missing)missing->clear();int score=0;array<int,702>q;
  for(int root=0;root<54;root++){
   ++stamp;int end=1,head=0;q[0]=root*13;seen[q[0]]=stamp;
   for(int depth=0;depth<4&&end<702;depth++){
    int end_this_depth=end;
    while(head<end_this_depth){int u=q[head++];for(int v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;q[end++]=v;}}
   }
   score+=702-end;
   if(missing)for(int v=0;v<702;v++)if(seen[v]!=stamp)missing->push_back(root*702+v);
  }return score;
 }
 void save(const string&prefix,int score,unsigned long long steps,unsigned long long accepted,double elapsed){
  auto original=[](int v){int b=v/13,x=v%13;return (b/27)*351+x*27+b%27;};
  set<pair<int,int>>es;for(int u=0;u<702;u++)for(int v:adj[u])if(u<v){int a=original(u),b=original(v);if(a>b)swap(a,b);es.emplace(a,b);}
  ofstream e(prefix+".edges");e<<702<<" "<<es.size()<<"\n";for(auto[u,v]:es)e<<u<<" "<<v<<"\n";
  ofstream j(prefix+".json");j<<"{\"n\":702,\"degree\":7,\"target_diameter\":4,\"base_vertices\":54,\"base_edges\":189,\"fiber_size\":13,\"representative_missing_sum\":"<<score<<",\"implied_bad_unordered_pairs\":"<<13*score/2<<",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"seconds_at_best\":"<<elapsed<<",\"edge_voltages\":[";
  for(int i=0;i<(int)edges.size();i++){auto&t=edges[i];j<<(i?",":"")<<"["<<t.u<<","<<t.v<<","<<t.z<<"]";}j<<"]}\n";
 }
};
int main(int argc,char**argv){
 if(argc!=7){cerr<<"usage BASE ROUTES SECONDS SEED PREFIX TEMPERATURE (negative=measureonly)\n";return 2;}
 Lift L;ifstream input(argv[1]);int bases,edgecount,p;input>>bases>>edgecount>>p;if(!input||bases!=54||edgecount!=189||p!=13)return 2;
 array<int,54>degree{};set<pair<int,int>>pairs;
 for(int i=0;i<edgecount;i++){int u,v,z;input>>u>>v>>z;if(u<0||v>=54||u>=v||z<0||z>=13||!pairs.emplace(u,v).second||degree[u]>=7||degree[v]>=7)return 2;L.edges.push_back({u,v,z,degree[u]++,degree[v]++});L.change(i,z);}
 for(int d:degree)if(d!=7)return 2;if(!input)return 2;
 ifstream routes(argv[2]);int count;routes>>count;if(count!=2916)return 2;L.routes.resize(2916);
 for(int i=0;i<count;i++){int u,v,k;routes>>u>>v>>k;auto&bucket=L.routes[u*54+v];bucket.resize(k);for(auto&form:bucket){int len;routes>>len;for(int t=0;t<len;t++){int eid,c;routes>>eid>>c;form.terms.emplace_back(eid,c);}}}if(!routes)return 2;
 double limit=stod(argv[3]),initial_temp=stod(argv[6]);mt19937_64 rng(stoull(argv[4]));string prefix=argv[5];
 signal(SIGTERM,handle_stop);signal(SIGINT,handle_stop);
 auto t0=chrono::steady_clock::now();auto sec=[&](){return chrono::duration<double>(chrono::steady_clock::now()-t0).count();};
 vector<int>missing,new_missing;int score=L.evaluate(&missing),best=score;L.save(prefix+".baseline",score,0,0,sec());
 cout<<"initial_missing "<<score<<" badpairs "<<13*score/2<<endl;
 if(initial_temp<0){
  vector<int>deltas,positive;map<int,int>hist;int improving=0,equal=0;unsigned long long tested=0;
  L.save(prefix+".best",score,0,0,sec());
  for(int eid=0;eid<189&&!stop_requested;eid++){int old=L.edges[eid].z;for(int delta=1;delta<13&&!stop_requested;delta++){
   L.change(eid,(old+delta)%13);int ns=L.evaluate();int d=ns-score;deltas.push_back(d);hist[d]++;tested++;if(d>0)positive.push_back(d);if(d==0)equal++;if(d<0)improving++;
   if(ns<best){best=ns;L.save(prefix+".best",ns,tested,0,sec());cout<<"neighborhood_best "<<best<<" edge "<<eid<<" change "<<delta<<endl;}
  }L.change(eid,old);}
  sort(deltas.begin(),deltas.end());sort(positive.begin(),positive.end());
  double recommended=positive.empty()?1.0:positive[(positive.size()-1)/10]/log(5.0);
  ofstream j(prefix+".neighborhood.json");j<<"{\"status\":\""<<(tested==2268?"COMPLETE":"STOPPED")<<"\",\"tested\":"<<tested<<",\"baseline_missing\":"<<score<<",\"minimum_missing\":"<<best<<",\"improving_moves\":"<<improving<<",\"equal_moves\":"<<equal<<",\"delta_min\":"<<deltas.front()<<",\"delta_median\":"<<deltas[deltas.size()/2]<<",\"delta_max\":"<<deltas.back()<<",\"positive_delta_p10\":"<<(positive.empty()?0:positive[(positive.size()-1)/10])<<",\"recommended_initial_temperature\":"<<recommended<<",\"elapsed_seconds\":"<<sec()<<",\"delta_histogram\":{";
  bool comma=false;for(auto[d,c]:hist){j<<(comma?",":"")<<"\""<<d<<"\":"<<c;comma=true;}j<<"}}\n";
  cout<<"neighborhood_complete "<<tested<<" min_delta "<<deltas.front()<<" median_delta "<<deltas[deltas.size()/2]<<" temp "<<recommended<<" seconds "<<sec()<<endl;return 0;
 }
 array<int,13>inverse{};for(int a=1;a<13;a++)for(int b=1;b<13;b++)if(a*b%13==1)inverse[a]=b;
 unsigned long long steps=0,accepted=0,guided=0,joint=0,random_moves=0;
 vector<int>best_voltage;for(auto&e:L.edges)best_voltage.push_back(e.z);
 L.save(prefix+".best",score,steps,accepted,sec());
 auto propose_guided=[&](const set<int>&protected_edges,vector<pair<int,int>>&old,set<int>&used_route){
  for(int trial=0;trial<12;trial++){
   int bad=missing[rng()%missing.size()],root=bad/702,target=bad%702,base=target/13,wanted=target%13;
   auto&bucket=L.routes[root*54+base];auto&form=bucket[rng()%bucket.size()];if(form.terms.empty())continue;
   int value=0;vector<pair<int,int>>eligible;for(auto[e,c]:form.terms){value+=c*L.edges[e].z;if(!protected_edges.count(e))eligible.emplace_back(e,c);}
   value%=13;if(value==wanted||eligible.empty())continue;
   auto[e,c]=eligible[rng()%eligible.size()];int change=((wanted-value+13)*inverse[c])%13;
   old.emplace_back(e,L.edges[e].z);L.change(e,(L.edges[e].z+change)%13);
   for(auto[f,d]:form.terms)used_route.insert(f);return true;
  }return false;
 };
 while(best>0&&!stop_requested&&sec()<limit){
  ++steps;vector<pair<int,int>>old;set<int>protected_edges;int kind=rng()%10;
  if(kind<9&&!missing.empty()){
   bool ok=propose_guided({},old,protected_edges);
   if(ok){guided++;if(kind>=7){set<int>second;bool ok2=propose_guided(protected_edges,old,second);joint+=ok2;}}
  }
  if(old.empty()){int e=rng()%189;old.emplace_back(e,L.edges[e].z);L.change(e,(L.edges[e].z+1+rng()%12)%13);random_moves++;}
  int ns=L.evaluate(&new_missing);double temp=initial_temp*pow(.02,min(1.0,sec()/limit));
  if(ns<=score||generate_canonical<double,53>(rng)<exp(double(score-ns)/temp)){
   accepted++;score=ns;missing.swap(new_missing);
   if(score<best){best=score;best_voltage.clear();for(auto&e:L.edges)best_voltage.push_back(e.z);L.save(prefix+".best",best,steps,accepted,sec());cout<<"best "<<best<<" badpairs "<<13*best/2<<" steps "<<steps<<" sec "<<sec()<<endl;}
  }else for(auto it=old.rbegin();it!=old.rend();++it)L.change(it->first,it->second);
 }
 L.save(prefix+".last",score,steps,accepted,sec());
 ofstream t(prefix+".terminal.json");t<<"{\"status\":\""<<(best==0?"CANDIDATE_COVERED":stop_requested?"STOPPED":"BUDGET_EXHAUSTED")<<"\",\"steps\":"<<steps<<",\"accepted\":"<<accepted<<",\"guided_proposals\":"<<guided<<",\"joint_proposals\":"<<joint<<",\"random_proposals\":"<<random_moves<<",\"best_missing\":"<<best<<",\"best_bad_unordered_pairs\":"<<13*best/2<<",\"last_missing\":"<<score<<",\"initial_temperature\":"<<initial_temp<<",\"final_temperature\":"<<initial_temp*.02<<",\"elapsed_seconds\":"<<sec()<<"}\n";
 cout<<"terminal best "<<best<<" last "<<score<<" accepted "<<accepted<<" steps "<<steps<<" seconds "<<sec()<<endl;
}

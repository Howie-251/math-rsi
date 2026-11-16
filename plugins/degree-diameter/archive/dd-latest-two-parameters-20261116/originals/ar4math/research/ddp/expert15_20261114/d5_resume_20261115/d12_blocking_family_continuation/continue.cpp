#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
struct Budget{double end=1e100;bool stopped=false;bool check(){if(stopped||cpu()>=end){stopped=true;return false;}return true;}};
using Bits=vector<uint64_t>;
int count_(const Bits&a){int n=0;for(auto w:a)n+=__builtin_popcountll(w);return n;}
bool empty_(const Bits&a){for(auto w:a)if(w)return false;return true;}
bool bit(const Bits&a,int i){return a[i/64]>>(i%64)&1;}
void clear_(Bits&a,int i){a[i/64]&=~(uint64_t(1)<<(i%64));}
template<class T>vector<T>readbin(const string&p,size_t n){ifstream f(p,ios::binary|ios::ate);if(!f||f.tellg()!=streampos(n*sizeof(T)))throw runtime_error("binary size "+p);vector<T>x(n);f.seekg(0);f.read((char*)x.data(),n*sizeof(T));return x;}
string ints(const vector<int>&a){ostringstream o;o<<'[';for(size_t i=0;i<a.size();i++){if(i)o<<',';o<<a[i];}o<<']';return o.str();}
struct Plane{int id;vector<int>pins;vector<uint64_t>providers;array<uint64_t,2>full{};vector<array<uint64_t,2>>cover;};
Plane plane_(int id,const vector<vector<int>>&global){Plane p;p.id=id;for(auto&r:global)p.pins.insert(p.pins.end(),r.begin(),r.end());sort(p.pins.begin(),p.pins.end());p.pins.erase(unique(p.pins.begin(),p.pins.end()),p.pins.end());assert(p.pins.size()<=56&&global.size()<=91);p.cover.resize(p.pins.size());
 for(size_t j=0;j<global.size();j++){uint64_t mask=0;for(int v:global[j]){int k=lower_bound(p.pins.begin(),p.pins.end(),v)-p.pins.begin();mask|=uint64_t(1)<<k;p.cover[k][j/64]|=uint64_t(1)<<(j%64);}assert(mask);p.providers.push_back(mask);p.full[j/64]|=uint64_t(1)<<(j%64);}return p;}
struct Core{
 Plane&p;Budget&budget;int cap;long long nodes=0,leaves=0,nonminimal=0;function<bool(uint64_t)>visit;
 Core(Plane&pp,Budget&bb,int c,function<bool(uint64_t)>v):p(pp),budget(bb),cap(c),visit(v){}
 bool dfs(uint64_t chosen,uint64_t forbidden,array<uint64_t,2>covered){
  nodes++;if(!budget.check())return true;
  if(covered==p.full){uint64_t essential=0;for(auto row:p.providers){uint64_t q=row&chosen;if(q&&!(q&(q-1)))essential|=q;}if(essential!=chosen){nonminimal++;return false;}leaves++;return visit(chosen);}
  int used=__builtin_popcountll(chosen);if(used>=cap)return false;
  uint64_t options=0;int best=100;
  for(size_t j=0;j<p.providers.size();j++)if(!(covered[j/64]>>(j%64)&1)){uint64_t q=p.providers[j]&~forbidden;int n=__builtin_popcountll(q);if(!n)return false;if(n<best){best=n;options=q;}}
  int uncovered=__builtin_popcountll(p.full[0]&~covered[0])+__builtin_popcountll(p.full[1]&~covered[1]);int gain=0;
  for(size_t k=0;k<p.pins.size();k++)if(!((forbidden|chosen)>>k&1))gain=max(gain,__builtin_popcountll(p.cover[k][0]&~covered[0])+__builtin_popcountll(p.cover[k][1]&~covered[1]));
  if(!gain||(uncovered+gain-1)/gain>cap-used)return false;
  while(options){int k=__builtin_ctzll(options);uint64_t b=uint64_t(1)<<k;options&=options-1;
   auto next=covered;next[0]|=p.cover[k][0];next[1]|=p.cover[k][1];
   if(dfs(chosen|b,forbidden,next))return true;
   forbidden|=b;
  }return false;
 }
};
struct Tail{
 int nf,nt,nw,pw;Budget&budget;vector<Bits>providers,cover;vector<int>roworder;long long nodes=0,lastone=0;vector<int>solution;
 Tail(int f,int t,vector<Bits>rows,Budget&b):nf(f),nt(t),nw((f+63)/64),pw((t+63)/64),budget(b),providers(move(rows)),cover(f,Bits(pw)){
  roworder.resize(nt);iota(roworder.begin(),roworder.end(),0);sort(roworder.begin(),roworder.end(),[&](int a,int b){int x=count_(providers[a]),y=count_(providers[b]);return x==y?a<b:x<y;});
  for(int t=0;t<nt;t++)for(int w=0;w<nw;w++){uint64_t bits=providers[t][w];while(bits){int v=64*w+__builtin_ctzll(bits);bits&=bits-1;assert(v<nf);cover[v][t/64]|=uint64_t(1)<<(t%64);}}
 }
 bool dfs(Bits missing,Bits available,int remaining,vector<int>&selected){
  nodes++;if(!budget.check())return false;if(empty_(missing)){solution=selected;return true;}if(!remaining)return false;
  if(remaining==1){lastone++;Bits candidates=available;
   for(int t:roworder)if(bit(missing,t)){if(!budget.check())return false;bool any=false;for(int w=0;w<nw;w++){candidates[w]&=providers[t][w];any|=bool(candidates[w]);}if(!any)return false;}
   for(int w=0;w<nw;w++)if(candidates[w]){solution=selected;solution.push_back(64*w+__builtin_ctzll(candidates[w]));return true;}return false;
  }
  int missingn=count_(missing),gain=0;
  for(int v=0;v<nf;v++)if(bit(available,v)){if((v&255)==0&&!budget.check())return false;int n=0;for(int w=0;w<pw;w++)n+=__builtin_popcountll(missing[w]&cover[v][w]);gain=max(gain,n);if(gain==missingn)break;}
  if(!gain||int64_t(remaining)*gain<missingn)return false;
  int t=-1;for(int q:roworder)if(bit(missing,q)){t=q;break;}assert(t>=0);
  Bits candidates(nw);for(int w=0;w<nw;w++)candidates[w]=providers[t][w]&available[w];
  for(int w=0;w<nw;w++)while(candidates[w]){if(!budget.check())return false;int v=64*w+__builtin_ctzll(candidates[w]);candidates[w]&=candidates[w]-1;
   Bits next=missing,nextavail=available;for(int q=0;q<pw;q++)next[q]&=~cover[v][q];clear_(nextavail,v);selected.push_back(v);
   if(dfs(move(next),move(nextavail),remaining-1,selected))return true;selected.pop_back();if(budget.stopped)return false;
   clear_(available,v);
  }return false;
 }
 bool complete(const vector<int>&core,int cap){Bits available(nw,~uint64_t(0)),missing(pw,~uint64_t(0));if(nf%64)available.back()=(uint64_t(1)<<(nf%64))-1;if(nt%64)missing.back()=(uint64_t(1)<<(nt%64))-1;
  for(int v:core){clear_(available,v);for(int w=0;w<pw;w++)missing[w]&=~cover[v][w];}vector<int>selected;solution.clear();return dfs(move(missing),move(available),cap-int(core.size()),selected);
 }
};
void control(){
 Budget budget;vector<vector<int>>lines{{0,1},{1,2},{2,3},{3,4}};Plane p=plane_(0,lines);vector<Bits>rows(5,Bits(1));vector<vector<int>>raw{{0,5},{1,5},{2,6},{3,6},{4,5,6}};for(int t=0;t<5;t++)for(int v:raw[t])rows[t][0]|=1ULL<<v;Tail tail(7,5,rows,budget);set<uint64_t>got,expected;int checks=0,yes=0,no=0;
 auto callback=[&](uint64_t mask){got.insert(mask);vector<int>core;for(int v=0;v<5;v++)if(mask>>v&1)core.push_back(v);bool actual=tail.complete(core,4),brute=false;
  for(int extra=0;extra<(1<<7);extra++){if((uint64_t(extra)&mask)||__builtin_popcount(unsigned(extra))+int(core.size())>4)continue;bool ok=true;for(auto row:rows)if(!(row[0]&(uint64_t(extra)|mask)))ok=false;if(ok){brute=true;break;}}
  if(actual!=brute)throw runtime_error("toy tail differs from brute subset oracle");checks++;actual?yes++:no++;return false;};
 Core en(p,budget,4,callback);en.dfs(0,0,{});
 for(uint64_t s=0;s<(1ULL<<5);s++)if(__builtin_popcountll(s)<=4){bool ok=true;for(auto row:p.providers)if(!(row&s))ok=false;if(!ok)continue;bool minimal=true;for(int v=0;v<5;v++)if(s>>v&1){bool sub=true;for(auto row:p.providers)if(!(row&(s&~(1ULL<<v))))sub=false;if(sub)minimal=false;}if(minimal)expected.insert(s);}
 if(got!=expected||!yes||!no)throw runtime_error("toy minimal frontier oracle");
 cout<<"CONTROL_PASS minimal_blockers="<<got.size()<<" tail_oracle_checks="<<checks<<" SAT="<<yes<<" NO="<<no<<" no_solver=1"<<endl;
}
#include <filesystem>
struct Graph {
 vector<vector<int>> adj; int m=0; vector<int> stamp,depth,queue; int tag=0;
 Graph(const string&file){ifstream f(file);int n,a,b;f>>n>>m;if(n!=42403||m!=245949)throw runtime_error("source binding");adj.resize(n);int cnt=0;while(f>>a>>b){if(a<0||b<0||a>=n||b>=n||a==b)throw runtime_error("edge");adj[a].push_back(b);adj[b].push_back(a);cnt++;}if(cnt!=m)throw runtime_error("edgecount");for(auto&r:adj){sort(r.begin(),r.end());if(r.size()>12||adjacent_find(r.begin(),r.end())!=r.end())throw runtime_error("source simple/degree");}resize();}
 void resize(){stamp.resize(adj.size());depth.resize(adj.size());queue.resize(adj.size());}
 int bfs(const vector<int>&roots,int radius,array<int,5>*layers=nullptr){tag++;int h=0,t=0;if(layers)layers->fill(0);for(int r:roots){stamp[r]=tag;depth[r]=0;queue[t++]=r;if(layers)(*layers)[0]++;}while(h<t){int v=queue[h++];if(depth[v]==radius)continue;for(int w:adj[v])if(stamp[w]!=tag){stamp[w]=tag;depth[w]=depth[v]+1;queue[t++]=w;if(layers)(*layers)[depth[w]]++;}}return t;}
 void add(const vector<int>&pins){int n=adj.size();adj.push_back(pins);for(int v:pins){if(adj[v].size()>=12)throw runtime_error("selected saturated");adj[v].push_back(n);}m+=pins.size();resize();}
};
int main(int argc,char**argv){try{
 if(argc==2&&string(argv[1])=="--control"){control();return 0;}if(argc!=5)return 2;
 string out=argv[1],rawplanes=argv[2],source=argv[3];double start=cpu();Budget budget;budget.end=start+stod(argv[4]);Graph g(source);
 ifstream pf(rawplanes);int np;pf>>np;if(np!=754)throw runtime_error("plane domain");vector<int>planeids(np);vector<vector<vector<int>>>raw(np,vector<vector<int>>(91));
 for(int i=0;i<np;i++){pf>>planeids[i];for(auto&r:raw[i]){int n;pf>>n;r.resize(n);for(int&v:r)pf>>v;}}if(!pf)throw runtime_error("raw plane input");
 ofstream sequences(out+"/ADDITIONS.jsonl"),stepresults(out+"/STEP_RESULTS.jsonl"),allplanes(out+"/PER_PLANE.jsonl");int accepted=0;string terminal="MAX8_ACCEPTED";long long totalP=0;vector<vector<int>>allpins;
 for(int step=0;step<8;step++){
  double stepstart=cpu();int n=g.adj.size(),nt=n-41356;vector<int>ids,index(n,-1);for(int v=0;v<n;v++)if(g.adj[v].size()<12){index[v]=ids.size();ids.push_back(v);}int nf=ids.size(),nw=(nf+63)/64;vector<Plane>planes;int impossible=0;
  for(int i=0;i<np;i++){auto lines=raw[i];bool possible=true;for(auto&r:lines){vector<int>filtered;for(int v:r)if(v<n&&index[v]>=0)filtered.push_back(index[v]);r=move(filtered);if(r.empty())possible=false;}if(possible)planes.push_back(plane_(planeids[i],lines));else{impossible++;allplanes<<"{\"step\":"<<step<<",\"plane_id\":"<<planeids[i]<<",\"status\":\"IMPOSSIBLE_CURRENT_DEGREE\"}\n";}}
  sort(planes.begin(),planes.end(),[](const Plane&a,const Plane&b){return a.pins.size()==b.pins.size()?a.id<b.id:a.pins.size()<b.pins.size();});
  vector<Bits>rows(nt,Bits(nw));int rootsdone=0;long long providercount=0;
  for(int r=41356;r<n;r++){if(!budget.check())break;int reached=g.bfs(vector<int>{r},4);for(int q=0;q<reached;q++){int k=index[g.queue[q]];if(k>=0){rows[r-41356][k/64]|=1ULL<<(k%64);providercount++;}}rootsdone++;}
  if(rootsdone!=nt){terminal="UNKNOWN_PROVIDER_PREPARATION_LIMIT";stepresults<<"{\"step\":"<<step<<",\"source_n\":"<<n<<",\"status\":\""<<terminal<<"\",\"completed_provider_roots\":"<<rootsdone<<",\"required_provider_roots\":"<<nt<<"}\n";break;}
  Tail tail(nf,nt,move(rows),budget);bool hit=false;int hitplane=-1;vector<int>hitcore,hittail,hitpins;array<long long,13>hist{};int reachedplanes=0;long long thisP=0,completeP=0;array<int,5>layers{};int actualcovered=0;
  for(size_t pi=0;pi<planes.size();pi++){
   if(!budget.check())break;reachedplanes++;string status="ACTIVE";
   auto visit=[&](uint64_t mask){vector<int>core;for(size_t k=0;k<planes[pi].pins.size();k++)if(mask>>k&1)core.push_back(planes[pi].pins[k]);thisP++;totalP++;hist[core.size()]++;
    if(tail.complete(core,12)){hitplane=planes[pi].id;for(int k:core)hitcore.push_back(ids[k]);for(int k:tail.solution)hittail.push_back(ids[k]);hitpins=hitcore;hitpins.insert(hitpins.end(),hittail.begin(),hittail.end());sort(hitpins.begin(),hitpins.end());if(hitpins.size()>12||adjacent_find(hitpins.begin(),hitpins.end())!=hitpins.end())throw runtime_error("candidate size/simple");for(int v:hitpins)if(g.adj[v].size()>=12)throw runtime_error("capacity");actualcovered=g.bfs(hitpins,4,&layers);if(actualcovered!=n)throw runtime_error("provider candidate fails complete actual current R4");hit=true;status="HIT_ACTUAL_R4_PASS";return true;}
    if(budget.stopped){status="UNKNOWN_LIMIT";return true;}completeP++;return false;};
   Core en(planes[pi],budget,12,visit);en.dfs(0,0,{});if(!hit)status=budget.stopped?"UNKNOWN_LIMIT":"EXHAUSTED";
   allplanes<<"{\"step\":"<<step<<",\"plane_id\":"<<planes[pi].id<<",\"available_pins\":"<<planes[pi].pins.size()<<",\"status\":\""<<status<<"\",\"core_nodes\":"<<en.nodes<<",\"minimal_blockers\":"<<en.leaves<<"}\n";
   if(hit||budget.stopped){for(size_t j=pi+1;j<planes.size();j++)allplanes<<"{\"step\":"<<step<<",\"plane_id\":"<<planes[j].id<<",\"status\":\"NOT_REACHED\"}\n";break;}
  }
  if(hit){
   int newv=n;g.add(hitpins);accepted++;allpins.push_back(hitpins);
   sequences<<"{\"step\":"<<step<<",\"source_n\":"<<n<<",\"source_m\":"<<g.m-int(hitpins.size())<<",\"new_vertex\":"<<newv<<",\"order\":"<<g.adj.size()<<",\"size\":"<<g.m<<",\"plane_id\":"<<hitplane<<",\"core\":"<<ints(hitcore)<<",\"tail\":"<<ints(hittail)<<",\"pins\":"<<ints(hitpins)<<",\"actual_R4_covered\":"<<actualcovered<<",\"R4_layers\":[";for(int k=0;k<5;k++){if(k)sequences<<',';sequences<<layers[k];}sequences<<"],\"max_degree\":12,\"old_edges_retained\":true,\"current_free_count\":"<<nf<<",\"peripheral_targets\":"<<nt<<",\"provider_roots_completed\":"<<rootsdone<<",\"provider_positive_bits\":"<<providercount<<",\"CPU\":"<<cpu()-stepstart<<"}\n";sequences.flush();
  }else terminal=budget.stopped?"UNKNOWN_WHOLE_CPU_LIMIT":"COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN";
  stepresults<<"{\"step\":"<<step<<",\"source_n\":"<<n<<",\"status\":\""<<(hit?"ACCEPTED_ACTUAL_R4_PASS":terminal)<<"\",\"all754_planes_in_domain\":true,\"degree_impossible_planes\":"<<impossible<<",\"reached_planes\":"<<reachedplanes<<",\"P_tail_checks\":"<<thisP<<",\"exhausted_tails\":"<<completeP<<",\"tail_nodes\":"<<tail.nodes<<",\"blocker_hist\":[";for(int k=0;k<13;k++){if(k)stepresults<<',';stepresults<<hist[k];}stepresults<<"],\"CPU\":"<<cpu()-stepstart<<"}\n";stepresults.flush();
  cout<<"STEP "<<step<<" source="<<n<<" accepted="<<hit<<" plane="<<hitplane<<" P="<<thisP<<" CPU="<<cpu()-stepstart<<" whole="<<cpu()-start<<endl;
  if(!hit)break;if(!budget.check()){terminal="UNKNOWN_WHOLE_CPU_LIMIT_AFTER_ACCEPTED_GRAPH";break;}
 }
 string edgefile="graph_d12_D5_n"+to_string(g.adj.size())+".edges";ofstream edges(out+"/"+edgefile);edges<<g.adj.size()<<' '<<g.m<<'\n';long long ec=0;int maxd=0;for(int u=0;u<int(g.adj.size());u++){maxd=max(maxd,int(g.adj[u].size()));for(int v:g.adj[u])if(u<v){edges<<u<<' '<<v<<'\n';ec++;}}if(ec!=g.m||maxd>12)throw runtime_error("final edgecount/degree");edges.close();
 ofstream result(out+"/NATIVE_RESULT.json");result<<"{\"status\":\""<<terminal<<"\",\"running\":false,\"source_n\":42403,\"accepted_new_graphs\":"<<accepted<<",\"final_n\":"<<g.adj.size()<<",\"final_m\":"<<g.m<<",\"max_degree\":"<<maxd<<",\"final_edgefile\":\""<<edgefile<<"\",\"P_tail_checks\":"<<totalP<<",\"native_CPU\":"<<cpu()-start<<",\"providers_recomputed_from_current_full_graph\":true,\"all754_original_planes_in_domain_each_step\":true,\"tail_all_current_free_except_core\":true,\"old_edges_retained\":true,\"source_D5_inherited\":true,\"complete_Lean\":false,\"further_continuation_authorized\":false}\n";
 cout<<"FINAL "<<terminal<<" accepted="<<accepted<<" n="<<g.adj.size()<<" CPU="<<cpu()-start<<endl;return 0;
 }catch(const exception&e){cerr<<"ERROR "<<e.what()<<endl;return 1;}}

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
int main(int argc,char**argv){try{if(argc==2&&string(argv[1])=="--control"){control();return 0;}if(argc!=5)return 2;
 double start=cpu();string out=argv[1],joint=argv[2],data=argv[3];Budget budget;budget.end=start+stod(argv[4]);ifstream pf(joint+"/planes.txt");int np,nf;pf>>np>>nf;assert(np==754&&nf==13857);vector<Plane>planes;
 for(int i=0;i<np;i++){int pid;pf>>pid;vector<vector<int>>lines(91);for(auto&r:lines){int n;pf>>n;r.resize(n);for(int&v:r){pf>>v;v--;assert(v>=0&&v<nf);}}planes.push_back(plane_(pid,lines));}assert(pf);
 sort(planes.begin(),planes.end(),[](const Plane&a,const Plane&b){return a.pins.size()==b.pins.size()?a.id<b.id:a.pins.size()<b.pins.size();});
 auto raw=readbin<uint64_t>(data+"/PERIPHERY_R4_FREE.u64le.bin",1046*217);vector<Bits>rows(1046,Bits(217));for(int t=0;t<1046;t++)copy(raw.begin()+size_t(t)*217,raw.begin()+size_t(t+1)*217,rows[t].begin());Tail tail(nf,1046,move(rows),budget);
 auto ids=readbin<uint32_t>(data+"/FREE_IDS.u32le.bin",nf);vector<string>status(np,"NOT_REACHED");vector<long long>pnodes(np),pleaves(np),pchecks(np),pcomplete(np),pincomplete(np);array<long long,13>hist{},rhist{};long long totalP=0,completeP=0;bool hit=false;int hitplane=-1;vector<int>hitindices;int reached=0;
 for(int pi=0;pi<np;pi++){if(!budget.check())break;reached++;double before=cpu();status[pi]="ACTIVE";
  ofstream(out+"/LIVE.json")<<"{\"status\":\"CORE_AND_TAIL_ACTIVE\",\"plane_id\":"<<planes[pi].id<<",\"plane_position\":"<<pi<<",\"P_checks_before\":"<<totalP<<",\"CPU\":"<<cpu()-start<<"}\n";
  auto visit=[&](uint64_t mask){vector<int>core;for(size_t k=0;k<planes[pi].pins.size();k++)if(mask>>k&1)core.push_back(planes[pi].pins[k]);hist[core.size()]++;rhist[12-core.size()]++;totalP++;pchecks[pi]++;
   if(tail.complete(core,12)){hit=true;hitplane=planes[pi].id;hitindices=core;hitindices.insert(hitindices.end(),tail.solution.begin(),tail.solution.end());sort(hitindices.begin(),hitindices.end());status[pi]="HIT";return true;}
   if(budget.stopped){pincomplete[pi]++;return true;}completeP++;pcomplete[pi]++;return false;};
  Core en(planes[pi],budget,12,visit);en.dfs(0,0,{});pnodes[pi]=en.nodes;pleaves[pi]=en.leaves;
  if(!hit)status[pi]=budget.stopped?"UNKNOWN_LIMIT":"EXHAUSTED";
  cout<<"PLANE "<<planes[pi].id<<" status="<<status[pi]<<" nlocal="<<planes[pi].pins.size()<<" blockers="<<en.leaves<<" Pchecks="<<pchecks[pi]<<" tail_complete="<<pcomplete[pi]<<" CPU="<<cpu()-before<<endl;
  if(hit||budget.stopped)break;
 }
 string result=hit?"COMPLETE_PROVIDER_COVER_FOUND":budget.stopped?"UNKNOWN_WHOLE_CPU_LIMIT":"COMPLETE_NO_IN_FIXED754_SUFFICIENT_PLANE_DOMAIN";
 if(hit){vector<int>pins;for(int k:hitindices)pins.push_back(ids[k]);ofstream(out+"/CANDIDATE.json")<<"{\"source_n\":42402,\"selected_indices\":"<<ints(hitindices)<<",\"pins\":"<<ints(pins)<<",\"open_plane_ids\":["<<hitplane<<"],\"status\":\"EXACT_FRONTIER_AND_PERIPHERY_PASS_ACTUAL_R4_PENDING\"}\n";}
 ofstream pr(out+"/PER_PLANE.jsonl");for(int i=0;i<np;i++)pr<<"{\"plane_id\":"<<planes[i].id<<",\"available_pins\":"<<planes[i].pins.size()<<",\"status\":\""<<status[i]<<"\",\"core_nodes\":"<<pnodes[i]<<",\"minimal_blockers\":"<<pleaves[i]<<",\"P_tail_checks\":"<<pchecks[i]<<",\"exhausted_tails\":"<<pcomplete[i]<<",\"incomplete_tails\":"<<pincomplete[i]<<"}\n";
 ofstream r(out+"/NATIVE_RESULT.json");r<<"{\"status\":\""<<result<<"\",\"running\":false,\"all754_planes_in_domain\":true,\"planes_reached\":"<<reached<<",\"P_tail_checks\":"<<totalP<<",\"exhausted_tails\":"<<completeP<<",\"tail_nodes\":"<<tail.nodes<<",\"last1_intersections\":"<<tail.lastone<<",\"hit_plane\":"<<hitplane<<",\"core_forbidden_passed_to_tail\":false,\"all_tail_sizes_enabled\":true,\"blocker_size_hist\":[";for(int i=0;i<13;i++){if(i)r<<',';r<<hist[i];}r<<"],\"tail_budget_hist\":[";for(int i=0;i<13;i++){if(i)r<<',';r<<rhist[i];}r<<"],\"native_CPU\":"<<cpu()-start<<",\"new_graphs\":0,\"actual_R4_checks\":0}\n";
 cout<<"FINAL "<<result<<" Pchecks="<<totalP<<" nativeCPU="<<cpu()-start<<endl;return 0;
 }catch(const exception&e){cerr<<"ERROR "<<e.what()<<endl;return 1;}}

#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
using State=array<int,5>;
struct Eq{array<int,5>a;int b;};
struct Rule{int phase,odd,dependent;vector<int>free;vector<Eq>eq;State first;};
int mod(int x,int m){x%=m;return x<0?x+m:x;}
int mul(int a,int b){int x=a%32,s=a/32,y=b%32,t=b/32;return mod(x+(s?-y:y)+16*s*t,32)+32*(s^t);}
int inv(int a){return a<32?mod(-a,32):mod(a%32+16,32)+32;}
int inv16(int a){for(int x=1;x<16;x+=2)if(a*x%16==1)return x;assert(false);return 0;}
State derive(State s,const Rule&r,int center){
 if(r.dependent){auto&e=r.eq[0];int rhs=e.b;for(int i=0;i<5;i++)if(i!=r.odd)rhs-=e.a[i]*s[i];assert(rhs%2==0);s[r.odd]=mod(rhs/2*inv16(e.a[r.odd]/2),16)+16*center;}
 for(auto&e:r.eq){int z=0;for(int i=0;i<5;i++)z+=e.a[i]*s[i];assert(mod(z,32)==e.b);}
 return s;
}
array<int,5>codes(const State&s,const Rule&r){array<int,5>c;for(int i=0;i<5;i++)c[i]=s[i]+32*((r.phase>>i)&1);return c;}
bool legal(const State&s,const Rule&r){auto c=codes(s,r);if(c[0]==0||c[0]==16||c[1]==0||c[1]==16)return false;set<int>cross{0,c[2],c[3],c[4]};return cross.size()==4;}
int value(const State&s,const Rule&r,int p){return r.dependent?(p==4?s[r.odd]/16:s[r.free[p]]):s[p];}
State change(State s,const Rule&r,int p,int v){int center=s[r.odd]/16;if(r.dependent){if(p==4)center=v;else s[r.free[p]]=v;}else s[p]=v;return derive(s,r,center);}
vector<pair<int,int>>edges(const State&s,const Rule&r){
 auto c=codes(s,r);set<pair<int,int>>es;
 auto add=[&](int u,int v){if(u>v)swap(u,v);assert(u!=v);es.insert({u,v});};
 for(int g=0;g<64;g++){add(g,mul(g,c[0]));add(64+g,64+mul(g,c[1]));add(g,64+g);for(int i=2;i<5;i++)add(g,64+mul(g,c[i]));}
 assert(es.size()==384);return vector<pair<int,int>>(es.begin(),es.end());
}
struct Score{int sum;array<int,2>miss;array<array<int,128>,2>dist;};
Score evaluate(const State&s,const Rule&r){
 auto c=codes(s,r);int a=c[0],b=c[1];array<int,4>h{0,c[2],c[3],c[4]},hi;for(int i=0;i<4;i++)hi[i]=inv(h[i]);
 Score z{};z.sum=0;
 for(int side=0;side<2;side++){
  auto&d=z.dist[side];d.fill(-1);array<int,128>q{};int end=1;q[0]=64*side;d[q[0]]=0;
  for(int head=0;head<end;head++){
   int u=q[head],g=u%64,j=u/64;if(d[u]==3)continue;
   auto add=[&](int v){if(d[v]<0){d[v]=d[u]+1;q[end++]=v;}};
   int t=j?b:a;add(j*64+mul(g,t));add(j*64+mul(g,inv(t)));
   for(int k=0;k<4;k++)add(j?mul(g,hi[k]):64+mul(g,h[k]));
  }
  z.miss[side]=128-end;z.sum+=z.miss[side];
 }
 return z;
}
volatile sig_atomic_t stopped=0;void stop_handler(int){stopped=1;}
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage RULES FIRST_EXPECTED CPU_LIMIT SEED\n";return 2;}
 ifstream input(argv[1]);int nr;input>>nr;vector<Rule>rules(nr);
 for(auto&r:rules){int ne;input>>r.phase>>r.odd>>r.dependent>>ne;r.eq.resize(ne);for(auto&e:r.eq){for(int&v:e.a)input>>v;input>>e.b;}for(int&v:r.first)input>>v;for(int i=0;i<5;i++)if(i!=r.odd)r.free.push_back(i);assert(legal(r.first,r));assert(derive(r.first,r,r.first[r.odd]/16)==r.first);}
 assert(input&&nr==14);
 ifstream expected(argv[2]);int m;expected>>m;vector<pair<int,int>>expected_edges(m);for(auto&[u,v]:expected_edges)expected>>u>>v;
 auto efirst=edges(rules[0].first,rules[0]);assert(efirst==expected_edges);
 array<array<int,128>,2>expected_dist;for(auto&row:expected_dist)for(int&v:row)expected>>v;assert(expected);
 double limit=stod(argv[3]);mt19937_64 rng(stoull(argv[4]));clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 signal(SIGINT,stop_handler);signal(SIGTERM,stop_handler);
 unsigned long long evaluations=0,raw=0,illegal=0,scans=0,moves=0,kicks=0,kick_legal_proposals=0;int completed_starts=0,segments=0,best=100000,best_rule=-1;State best_state{};Score best_score{};bool timeout=false,hit=false;int cursor_start=0,cursor_segment=0,cursor_step=0,cursor_parameter=0,cursor_value=0;
 auto save=[&](const State&s,const Rule&r,const Score&z,int start_id,int seg,int step){
  auto c=codes(s,r);ofstream f("best.json");f<<"{\"n\":128,\"m\":384,\"degree\":6,\"target_D\":3,\"phase_mask\":"<<r.phase<<",\"sum_root_deficits\":"<<z.sum<<",\"bad_unordered_pairs\":"<<32*z.sum<<",\"constrained_parameterization\":"<<(r.dependent?"true":"false")<<",\"root_misses\":["<<z.miss[0]<<","<<z.miss[1]<<"],\"x\":[";for(int i=0;i<5;i++)f<<(i?",":"")<<s[i];f<<"],\"codes_a_b_h1_h2_h3\":[";for(int i=0;i<5;i++)f<<(i?",":"")<<c[i];f<<"],\"start\":"<<start_id<<",\"segment\":"<<seg<<",\"step\":"<<step<<",\"evaluation\":"<<evaluations<<"}\n";
  auto es=edges(s,r);ofstream ef("best.edges");ef<<"128 "<<es.size()<<"\n";for(auto[u,v]:es)ef<<u<<" "<<v<<"\n";
 };
 auto scored=[&](const State&s,const Rule&r,int si,int seg,int step){Score z=evaluate(s,r);++evaluations;if(z.sum<best){best=z.sum;best_state=s;best_rule=si;best_score=z;save(s,r,z,si,seg,step);cout<<"best "<<best<<" badpairs "<<32*best<<" eval "<<evaluations<<endl;}if(!z.sum)hit=true;return z;};
 for(int si=0;si<nr&&!hit;si++){
  cursor_start=si;auto&r=rules[si];State cur=r.first;Score current=scored(cur,r,si,0,-1);
  if(si==0){assert(current.dist==expected_dist);ofstream cf("first.cpp_calibration.json");cf<<"{\"status\":\"MATCH\",\"edges_compared\":384,\"radius3_distance_entries_compared\":256,\"first_score_reused\":true,\"bad_unordered_pairs\":"<<32*current.sum<<"}\n";}
  for(int seg=0;seg<3&&!hit;seg++){
   cursor_segment=seg;++segments;
   for(int step=0;step<12&&!hit;step++){
    cursor_step=step;State next=cur;int next_score=current.sum;Score next_full=current;
    for(int p=0;p<5&&!hit;p++)for(int v=0;v<(r.dependent&&p==4?2:32)&&!hit;v++){
     cursor_parameter=p;cursor_value=v;
     if(v==value(cur,r,p))continue;
     if(stopped||cpu()>=limit){timeout=true;goto finish;}
     ++raw;State trial=change(cur,r,p,v);if(!legal(trial,r)){++illegal;continue;}
     Score z=scored(trial,r,si,seg,step);if(z.sum<next_score){next_score=z.sum;next=trial;next_full=z;}
    }
    ++scans;if(hit)break;
    if(next_score>=current.sum)break;
    cur=next;current=next_full;assert(current.sum==next_score);++moves;
   }
   if(seg<2&&!hit){
    array<int,5>pp{0,1,2,3,4};shuffle(pp.begin(),pp.end(),rng);
    for(int k=0;k<2;k++){
     int p=pp[k],range=r.dependent&&p==4?2:32;vector<int>vv;
     for(int v=0;v<range;v++)if(v!=value(cur,r,p)){State trial=change(cur,r,p,v);++kick_legal_proposals;if(legal(trial,r))vv.push_back(v);}
     assert(!vv.empty());cur=change(cur,r,p,vv[rng()%vv.size()]);
    }
    ++kicks;current=scored(cur,r,si,seg,12);
   }
  }
  ++completed_starts;
 }
 finish:
 double used=cpu();ofstream f("search.terminal.json");
 f<<"{\"status\":\""<<(hit?"CANDIDATE_D3":timeout?"BUDGET_OR_SIGNAL_STOP":"COMPLETE_14_PHASE_PROFILE_NO_D3")<<"\",\"running\":false,\"found_D3\":"<<(hit?"true":"false")<<",\"phase_starts_scope\":14,\"starts_completed\":"<<completed_starts<<",\"segments_entered\":"<<segments<<",\"legal_score_evaluations\":"<<evaluations<<",\"raw_neighbor_proposals\":"<<raw<<",\"illegal_neighbor_proposals\":"<<illegal<<",\"complete_neighborhoods\":"<<scans<<",\"strict_moves\":"<<moves<<",\"two_distinct_parameter_kicks\":"<<kicks<<",\"kick_legality_proposals\":"<<kick_legal_proposals<<",\"best_sum_root_deficits\":"<<best<<",\"best_bad_unordered_pairs\":"<<32*best<<",\"production_CPU_seconds\":"<<used<<",\"scope_exhausted\":"<<(!timeout&&!hit?"true":"false")<<",\"entire_Q64_family_exhausted\":false,\"restarts\":0,\"cursor\":{\"start\":"<<cursor_start<<",\"segment\":"<<cursor_segment<<",\"step\":"<<cursor_step<<",\"parameter\":"<<cursor_parameter<<",\"value\":"<<cursor_value<<"},\"pending\":[\"root independent final saved-edge verification\"]}\n";
 cout<<"terminal "<<best<<" evaluations "<<evaluations<<" cpu "<<used<<endl;
}

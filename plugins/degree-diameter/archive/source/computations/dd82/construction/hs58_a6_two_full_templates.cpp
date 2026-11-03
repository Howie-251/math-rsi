// Exhaust the proved necessary a6/E2 old-addition templates, not graphs/H.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
using Mask=uint64_t;
using Edge=pair<int,int>;
using Core=array<Edge,6>;
constexpr Mask ALL=(Mask(1)<<50)-1;
array<Mask,50> Q;
clock_t began;
bool complete=true;
Edge edge(int x,int y){return minmax(x,y);}
int pop(Mask m){return __builtin_popcountll(m);}
Mask bit(int x){return Mask(1)<<x;}
void add(array<Mask,50>&g,int x,int y){g[x]|=bit(y);g[y]|=bit(x);}
void del(array<Mask,50>&g,int x,int y){g[x]&=~bit(y);g[y]&=~bit(x);}
vector<int> members(Mask m){vector<int>v;while(m){int x=__builtin_ctzll(m);m&=m-1;v.push_back(x);}return v;}
void array_json(ostream&o,const vector<int>&v){o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';}
void core_json(ostream&o,const Core&A){o<<'[';for(int i=0;i<6;++i){if(i)o<<',';o<<'['<<A[i].first<<','<<A[i].second<<']';}o<<']';}
struct Record{Core A;Mask Z;};
struct Result{
 string name;int t,u,v,w;long raw=0, endpoint_compatible=0, partner_pairs=0,row_pass=0,oldzero_pass=0;
 int max_partner_candidates=0;
 array<array<long,50>,50> first_failure{};
 vector<Record> records;
};

Result run(string name,int t,int u,int v,int w){
 Result r;r.name=name;r.t=t;r.u=u;r.v=v;r.w=w;
 Mask P=bit(t)|bit(u)|bit(v)|bit(w), full=bit(t)|bit(u);
 auto M0=Q;del(M0,t,u);del(M0,v,w);
 auto T=members(Q[t]&~bit(u)),U=members(Q[u]&~bit(t));
 assert(T.size()==6&&U.size()==6);
 Mask TM=Q[t]&~bit(u),UM=Q[u]&~bit(t);
 assert(!(TM&UM));
 for(int x:members(TM|UM))assert(!(Q[x]&(TM|UM)));
 for(int tm=0;tm<64;++tm)if(__builtin_popcount(unsigned(tm))==4)
 for(int um=0;um<64;++um)if(__builtin_popcount(unsigned(um))==4){
  vector<int> L,R;
  for(int i=0;i<6;++i){if(tm&(1<<i))L.push_back(T[i]);if(um&(1<<i))R.push_back(U[i]);}
  Mask S=0;for(int x:L)S|=bit(x);for(int x:R)S|=bit(x);
  vector<int> cv,cw;
  if(!(S&P)){
   auto candidates=[&](int partner){
    vector<int> ret;
    for(int q=0;q<50;++q){
     if((bit(q)&(P|S))||(Q[q]&S)||(Q[q]&bit(partner)))continue;
     // Lost q--opposite-full path has no new intermediary or A at its full end.
     if((bit(q)&TM)&&!(Q[partner]&bit(u)))continue;
     if((bit(q)&UM)&&!(Q[partner]&bit(t)))continue;
     ret.push_back(q);
    }
    return ret;
   };
   cv=candidates(v);cw=candidates(w);
   r.max_partner_candidates=max(r.max_partner_candidates,int(max(cv.size(),cw.size())));
   assert(cv.size()<=8&&cw.size()<=8);
  }
  do{
   ++r.raw;
   if((r.raw&1023)==0&&double(clock()-began)/CLOCKS_PER_SEC>4.7){complete=false;return r;}
   if(S&P)continue;
   ++r.endpoint_compatible;
   Core baseA;
   for(int i=0;i<4;++i){baseA[i]=edge(L[i],R[i]);assert(!(Q[L[i]]&bit(R[i])));}
   for(int qv:cv)for(int qw:cw){
    if(qv==qw)continue;
    ++r.partner_pairs;
    Mask Z=S|bit(qv)|bit(qw);assert(pop(Z)==10);
    Core A=baseA;A[4]=edge(v,qv);A[5]=edge(w,qw);sort(A.begin(),A.end());
    auto M=M0;for(auto [x,y]:A)add(M,x,y);
    bool row_ok=true;
    for(int q:members(Z))if(pop(M[q]&Z)>pop(M[q]&full)){row_ok=false;break;}
    if(!row_ok)continue;
    ++r.row_pass;
    bool old_ok=true;
    for(int q:members(Z)){
     Mask covered=bit(q)|M[q];
     for(int x:members(M[q]))covered|=M[x];
     if(covered!=ALL){int miss=__builtin_ctzll(ALL&~covered);++r.first_failure[q][miss];old_ok=false;break;}
    }
    if(!old_ok)continue;
    ++r.oldzero_pass;
    for(int x=0;x<50;++x){int p=pop(M[x]);assert(p==(full&bit(x)?6:Z&bit(x)?8:7));}
    r.records.push_back({A,Z});
   }
  }while(next_permutation(R.begin(),R.end()));
 }
 assert(r.raw==5400);
 return r;
}

int main(int argc,char**argv){
 assert(argc==2);began=clock();auto wall=chrono::steady_clock::now();
 for(int i=0;i<5;++i)for(int j=0;j<5;++j){
  add(Q,5*i+j,5*i+(j+1)%5);add(Q,25+5*i+j,25+5*i+(j+2)%5);
  for(int k=0;k<5;++k)add(Q,5*i+j,25+5*k+(i*k+j)%5);
 }
 for(int x=0;x<50;++x){assert(pop(Q[x])==7);for(int y=x+1;y<50;++y)assert(pop(Q[x]&Q[y])==((Q[x]&bit(y))?0:1));}
 vector<Result> results;
 for(auto config:vector<array<int,4>>{{0,1,10,11},{10,11,0,1},{0,1,2,3},{2,3,0,1}}){
  auto[t,u,v,w]=config;
  string name=(v>=10||t>=10?"no_cross":"cross");name+="_full_"+to_string(t)+"_"+to_string(u);
  assert(Q[t]&bit(u));assert(Q[v]&bit(w));
  results.push_back(run(name,t,u,v,w));if(!complete)break;
 }
 ofstream out(argv[1]);
 out<<"{\"complete\":"<<(complete?"true":"false")<<",\"cpu_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC
    <<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall).count()<<",\"domains\":[";
 for(size_t j=0;j<results.size();++j){
  if(j)out<<',';auto&r=results[j];
  out<<"{\"name\":\""<<r.name<<"\",\"full_edge\":["<<r.t<<','<<r.u<<"],\"other_deleted_edge\":["<<r.v<<','<<r.w
     <<"],\"raw_T4_U4_bijections\":"<<r.raw<<",\"D_endpoint_compatible\":"<<r.endpoint_compatible
     <<",\"partner_pairs\":"<<r.partner_pairs<<",\"zero_row_capacity_pass\":"<<r.row_pass
     <<",\"old_zero_coverage_pass\":"<<r.oldzero_pass<<",\"max_partner_candidate_count\":"<<r.max_partner_candidates
     <<",\"first_failed_old_zero_pairs\":[";
  bool comma=false;for(int q=0;q<50;++q)for(int x=0;x<50;++x)if(r.first_failure[q][x]){
   if(comma)out<<',';comma=true;out<<"["<<q<<','<<x<<','<<r.first_failure[q][x]<<']';}
  out<<"],\"templates\":[";
  for(size_t k=0;k<r.records.size();++k){if(k)out<<',';out<<"{\"additions\":";core_json(out,r.records[k].A);
   out<<",\"zeros\":";array_json(out,members(r.records[k].Z));out<<'}';}
  out<<"]}";
 }
 out<<"]}\n";
 cout<<"complete="<<complete<<" cpu="<<double(clock()-began)/CLOCKS_PER_SEC<<'\n';
 for(auto&r:results)cout<<r.name<<" raw="<<r.raw<<" partners="<<r.partner_pairs<<" row="<<r.row_pass<<" oldzero="<<r.oldzero_pass<<'\n';
}

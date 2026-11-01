#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
#include <sys/resource.h>
using namespace std;
int bits(int x){int n=0;while(x){x&=x-1;++n;}return n;}
int moved(int mask,const array<int,7>&p){int ans=0;for(int i=0;i<7;i++)if(mask&(1<<i))ans|=1<<p[i];return ans;}
struct Job{int id,shape,quad;};struct Row{int D,Q,m,W,M;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();vector<int>T,reds,pairs;array<int,128>rank{};rank.fill(-1);
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)T.push_back((1<<i)|(1<<j)|(1<<k));
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)for(int l=k+1;l<7;l++)reds.push_back((1<<i)|(1<<j)|(1<<k)|(1<<l));
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)pairs.push_back((1<<i)|(1<<j));
 int rr=0;for(int mask=0;mask<128;mask++)if(bits(mask)==3)rank[mask]=rr++;
 vector<Job>jobs;array<set<int>,2>quadReps;
 for(int shape=0;shape<2;shape++){
  vector<array<int,7>>aut;array<int,7>p={0,1,2,3,4,5,6};int f1=3,f2=shape==0?6:12;
  do{int a=moved(f1,p),b=moved(f2,p);if((a==f1&&b==f2)||(a==f2&&b==f1))aut.push_back(p);}while(next_permutation(p.begin(),p.end()));assert(aut.size()==48);
  for(int q:reds){int rep=q;for(auto p:aut)rep=min(rep,moved(q,p));quadReps[shape].insert(rep);}
  assert(quadReps[shape].size()==(shape==0?6:5));for(int q:quadReps[shape])jobs.push_back({int(jobs.size()),shape,q});
 }
 assert(jobs.size()==11);ifstream jfile(dir+"/JOBS.tsv");for(auto j:jobs){int id,shape,q;assert(jfile>>id>>shape>>q);assert(id==j.id&&shape==j.shape&&q==j.quad);}int extra;assert(!(jfile>>extra));
 unordered_map<uint64_t,Row>records;records.reserve(700000);ifstream in(dir+"/NECESSARY.tsv");int job,D,Q,m,W,M;unsigned packed;
 while(in>>job>>packed>>D>>Q>>m>>W>>M){assert(job>=0&&job<11);assert(D==W-M&&D>0&&m<=11);assert(records.emplace((uint64_t(job)<<32)|packed,Row{D,Q,m,W,M}).second);}
 assert(in.eof());size_t original=records.size();long total=0;int minD=100000,maxCost=0;
 ofstream report(dir+"/INDEPENDENT_CHECK.json");report<<"{\"scope\":\"independent multiplicity-vector domain; 4-red-complement candidates; complete source-key equality and exact W/M/D plus own stored witness\",\"all_70_quad_positions_checked\":true,\"jobs\":[";
 for(auto j:jobs){
  int I1=127^3,I2=127^(j.shape==0?6:12);array<int,7>c{},quadinc{},a{};array<int,35>mult{};array<unsigned,35>covered{};
  unsigned base=0;for(int pidx=0;pidx<21;pidx++){int pair=pairs[pidx];if((pair&I1)==pair||(pair&I2)==pair||(pair&j.quad)==pair)base|=1u<<pidx;}
  for(int v=0;v<7;v++){c[v]=int(I1&(1<<v)?1:0)+int(I2&(1<<v)?1:0);quadinc[v]=int(j.quad&(1<<v)?1:0);}
  for(int t=0;t<35;t++)for(int pidx=0;pidx<21;pidx++)if((T[t]&pairs[pidx])==pairs[pidx])covered[t]|=1u<<pidx;
  long count=0,degreeLeaves=0;int localD=100000,localCost=0;
  function<void(int,int,unsigned)> visit=[&](int pos,int left,unsigned paircover){
   if(!left){
    ++degreeLeaves;if(paircover!=(1u<<21)-1)return;
    array<int,7>u{};int sumu=0;for(int v=0;v<7;v++){u[v]=8-c[v]-a[v]-quadinc[v];assert(u[v]>=0);assert(4*u[v]+2*a[v]+quadinc[v]>=17);sumu+=u[v];}assert(sumu==27);
    vector<int>expanded,distinct;for(int t=0;t<35;t++)if(mult[t]){distinct.push_back(T[t]);for(int k=0;k<mult[t];k++)expanded.push_back(T[t]);}assert(expanded.size()==5);sort(expanded.begin(),expanded.end());unsigned enc=0;for(int k=0;k<5;k++)enc|=unsigned(rank[expanded[k]])<<(6*k);
    uint64_t key=(uint64_t(j.id)<<32)|enc;auto entry=records.find(key);assert(entry!=records.end());auto r=entry->second;
    int ww=0,mm=0,bestcost=99;
    for(int red:reds){
     int blue=127^red,redCost=0;for(int v=0;v<7;v++)if(red&(1<<v))redCost+=u[v];
     bool excluded=false;for(int t:distinct)if((t&blue)==t)excluded=true;
     int weight=excluded?0:max(0,redCost-15),misses=0;for(int t:distinct)if((t&red)==t)++misses;if((j.quad&red)==j.quad)++misses;
     ww+=weight;mm+=weight*misses;
     if(!excluded&&!misses)bestcost=min(bestcost,27-redCost);
    }
    assert(ww==r.W&&mm==r.M&&ww-mm==r.D&&ww>mm&&bestcost==r.m&&bestcost<=11);
    assert(bits(r.Q)==3);int witnessCost=0;for(int v=0;v<7;v++)if(r.Q&(1<<v))witnessCost+=u[v];assert(witnessCost==r.m);
    vector<int>all=distinct;all.push_back(j.quad);all.push_back(I1);all.push_back(I2);for(int t:all)assert((t&r.Q)!=0&&(t&r.Q)!=t);
    // Expand and classify every one of the 35 indexed P-traces directly.
    vector<int>source={I1,I2};source.insert(source.end(),expanded.begin(),expanded.end());source.push_back(j.quad);
    for(int v=0;v<7;v++){assert(c[v]+a[v]+quadinc[v]+u[v]==8);for(int k=0;k<u[v];k++)source.push_back(1<<v);}assert(source.size()==35);
    array<int,5>positive{},negative{};int proper=0;
    for(int trace:source){int freeSize=5-bits(trace);if((trace&r.Q)&&(trace&(127^r.Q)))++proper;else if((trace&r.Q)==trace)++positive[freeSize];else ++negative[freeSize];}
    assert(proper==8&&positive[4]==r.m&&negative[4]==27-r.m);for(int k=0;k<4;k++)assert(positive[k]==0&&negative[k]==0);
    records.erase(entry);count++;localD=min(localD,r.D);localCost=max(localCost,bestcost);return;
   }
   if(pos==35)return;
   // Enumerate multiplicities at this triple, rather than five sorted indices.
   for(int k=0;k<=left;k++){
    bool feasible=true;for(int v=0;v<7;v++){
     int now=a[v]+((T[pos]&(1<<v))?k:0),privateUpper=8-c[v]-quadinc[v]-now;
     // Future triple incidence only decreases this outside-star upper capacity.
     if(privateUpper<0||4*privateUpper+2*now+quadinc[v]<17)feasible=false;
    }
    if(!feasible)continue;
    mult[pos]=k;for(int v=0;v<7;v++)if(T[pos]&(1<<v))a[v]+=k;
    visit(pos+1,left-k,k?paircover|covered[pos]:paircover);
    for(int v=0;v<7;v++)if(T[pos]&(1<<v))a[v]-=k;
   }
   mult[pos]=0;
  };
  visit(0,5,base);total+=count;minD=min(minD,localD);maxCost=max(maxCost,localCost);
  if(j.id)report<<',';report<<"{\"id\":"<<j.id<<",\"shape\":"<<j.shape<<",\"quad\":"<<j.quad<<",\"degree_feasible_leaves\":"<<degreeLeaves<<",\"necessary\":"<<count<<",\"minimum_D\":"<<localD<<",\"maximum_minimum_cost\":"<<localCost<<"}";
  assert(double(clock()-start)/CLOCKS_PER_SEC<20);
 }
 assert(records.empty());assert(total==long(original));rusage usage{};getrusage(RUSAGE_SELF,&usage);
#ifdef __APPLE__
 uint64_t peakBytes=usage.ru_maxrss;
#else
 uint64_t peakBytes=uint64_t(usage.ru_maxrss)*1024;
#endif
 assert(peakBytes<(uint64_t(1)<<30));
 report<<"],\"PASS\":true,\"full_keyset_equal\":true,\"all_W_M_D_and_witnesses_equal\":true,\"sources\":"<<total<<",\"source_index_classifications\":"<<35*total<<",\"minimum_D\":"<<minD<<",\"maximum_minimum_cost\":"<<maxCost<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"peak_rss_bytes\":"<<peakBytes<<"}\n";
 cout<<"PASS complete keys="<<total<<" minD="<<minD<<" maxcost="<<maxCost<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

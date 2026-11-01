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
int moveMask(int mask,const array<int,7>&p){int out=0;for(int i=0;i<7;i++)if(mask&(1<<i))out|=1<<p[i];return out;}
struct Row{int D,Q,m,W,M;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();vector<int>tri,reds,pairs,quads;array<int,128>rank{};rank.fill(-1);
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)tri.push_back((1<<i)|(1<<j)|(1<<k));
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)for(int l=k+1;l<7;l++)reds.push_back((1<<i)|(1<<j)|(1<<k)|(1<<l));
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)pairs.push_back((1<<i)|(1<<j));
 int rank3=0;for(int m=0;m<128;m++){if(bits(m)==3)rank[m]=rank3++;if(bits(m)==4)quads.push_back(m);}
 vector<array<int,7>>group;array<int,7>perm={0,1,2,3,4,5,6};do{if(moveMask(31,perm)==31)group.push_back(perm);}while(next_permutation(perm.begin(),perm.end()));assert(group.size()==240);
 vector<array<int,35>>action;for(auto p:group){array<int,35>a{};for(int k=0;k<35;k++)a[k]=moveMask(quads[k],p);action.push_back(a);}
 set<array<int,3>>repSet;
 for(int a=0;a<35;a++)for(int b=a;b<35;b++)for(int c=b;c<35;c++){
  array<int,3>rep={quads[a],quads[b],quads[c]};for(auto act:action){array<int,3>image={act[a],act[b],act[c]};sort(image.begin(),image.end());rep=min(rep,image);}repSet.insert(rep);
 }
 assert(repSet.size()==101);vector<array<int,3>>jobs(repSet.begin(),repSet.end());ifstream jf(dir+"/JOBS.tsv");for(int j=0;j<101;j++){int id,q0,q1,q2;assert(jf>>id>>q0>>q1>>q2);assert(id==j&&(array<int,3>{q0,q1,q2})==jobs[j]);}int extra;assert(!(jf>>extra));
 unordered_map<uint64_t,Row>records;records.reserve(400000);ifstream in(dir+"/NECESSARY.tsv");int id,D,Q,m,W,M;unsigned packed;
 while(in>>id>>packed>>D>>Q>>m>>W>>M){assert(id>=0&&id<101);assert(D==W-M&&D>0&&m<=11);assert(records.emplace((uint64_t(id)<<32)|packed,Row{D,Q,m,W,M}).second);}assert(in.eof());size_t original=records.size();
 long total=0;int minD=100000,maxCost=0;ofstream out(dir+"/INDEPENDENT_CHECK.json");out<<"{\"scope\":\"independent S7-filter group/quad canonical keys; multiplicity-vector P3 domain; red-complement weights; complete necessary-key and35-trace checks\",\"all101_quad_jobs_independently_recovered\":true,\"jobs\":[";
 for(int job=0;job<101;job++){
  auto qs=jobs[job];array<int,7>c{},b{},a{};array<int,35>mult{};array<unsigned,35>pairmask{};unsigned base=0;
  for(int v=0;v<7;v++){c[v]=int(v<5);for(int q:qs)b[v]+=int(q&(1<<v)?1:0);}
  for(int p=0;p<21;p++){bool cov=(pairs[p]&31)==pairs[p];for(int q:qs)cov=cov||((pairs[p]&q)==pairs[p]);if(cov)base|=1u<<p;}
  for(int t=0;t<35;t++)for(int p=0;p<21;p++)if((tri[t]&pairs[p])==pairs[p])pairmask[t]|=1u<<p;
  long count=0,leaves=0;int localD=100000,localCost=0;
  function<void(int,int,unsigned)> visit=[&](int pos,int left,unsigned cover){
   if(!left){
    ++leaves;if(cover!=(1u<<21)-1)return;
    array<int,7>u{};int sumu=0;for(int v=0;v<7;v++){u[v]=8-c[v]-a[v]-b[v];assert(u[v]>=0&&4*u[v]+2*a[v]+b[v]>=17);sumu+=u[v];}assert(sumu==27);
    vector<int>expanded,distinct;for(int t=0;t<35;t++)if(mult[t]){distinct.push_back(tri[t]);for(int k=0;k<mult[t];k++)expanded.push_back(tri[t]);}assert(expanded.size()==4);sort(expanded.begin(),expanded.end());unsigned packed=0;for(int k=0;k<4;k++)packed|=unsigned(rank[expanded[k]])<<(6*k);
    uint64_t key=(uint64_t(job)<<32)|packed;auto it=records.find(key);assert(it!=records.end());auto r=it->second;vector<int>allHigh=distinct;for(int q:qs)allHigh.push_back(q);sort(allHigh.begin(),allHigh.end());allHigh.erase(unique(allHigh.begin(),allHigh.end()),allHigh.end());
    int ww=0,mm=0,best=99;
    for(int red:reds){int blue=127^red,redCost=0;for(int v=0;v<7;v++)if(red&(1<<v))redCost+=u[v];bool excluded=false;for(int T:distinct)excluded=excluded||((T&blue)==T);int weight=excluded?0:max(0,redCost-15),miss=0;for(int T:allHigh)miss+=int((T&red)==T);ww+=weight;mm+=weight*miss;if(!excluded&&!miss)best=min(best,27-redCost);}
    assert(ww==r.W&&mm==r.M&&ww-mm==r.D&&ww>mm&&best==r.m&&best<=11);
    assert(bits(r.Q)==3);int cost=0;for(int v=0;v<7;v++)if(r.Q&(1<<v))cost+=u[v];assert(cost==r.m);
    vector<int>source={31};source.insert(source.end(),expanded.begin(),expanded.end());for(int q:qs)source.push_back(q);
    for(int v=0;v<7;v++){assert(c[v]+a[v]+b[v]+u[v]==8);for(int k=0;k<u[v];k++)source.push_back(1<<v);}assert(source.size()==35);
    array<int,5>positive{},negative{};int proper=0;
    for(int T:source){int free=5-bits(T);if((T&r.Q)&&(T&(127^r.Q)))++proper;else if((T&r.Q)==T)++positive[free];else ++negative[free];}
    assert(proper==8&&positive[4]==r.m&&negative[4]==27-r.m);for(int k=0;k<4;k++)assert(positive[k]==0&&negative[k]==0);
    records.erase(it);++count;localD=min(localD,r.D);localCost=max(localCost,best);return;
   }
   if(pos==35)return;
   for(int k=0;k<=left;k++){
    bool possible=true;for(int v=0;v<7;v++){int av=a[v]+((tri[pos]&(1<<v))?k:0),upper=8-c[v]-b[v]-av;if(upper<0||4*upper+2*av+b[v]<17)possible=false;}if(!possible)continue;
    mult[pos]=k;for(int v=0;v<7;v++)if(tri[pos]&(1<<v))a[v]+=k;
    visit(pos+1,left-k,k?cover|pairmask[pos]:cover);
    for(int v=0;v<7;v++)if(tri[pos]&(1<<v))a[v]-=k;
   }
   mult[pos]=0;
  };
  visit(0,4,base);total+=count;minD=min(minD,localD);maxCost=max(maxCost,localCost);if(job)out<<',';out<<"{\"id\":"<<job<<",\"degree_feasible\":"<<leaves<<",\"necessary\":"<<count<<",\"minimum_D\":"<<localD<<",\"maximum_minimum_cost\":"<<localCost<<"}";assert(double(clock()-start)/CLOCKS_PER_SEC<20);
 }
 assert(records.empty()&&total==long(original));rusage usage{};getrusage(RUSAGE_SELF,&usage);
#ifdef __APPLE__
 uint64_t peakBytes=usage.ru_maxrss;
#else
 uint64_t peakBytes=uint64_t(usage.ru_maxrss)*1024;
#endif
 assert(peakBytes<(uint64_t(1)<<30));out<<"],\"PASS\":true,\"full_source_keyset_equal\":true,\"all_W_M_D_and_witnesses_equal\":true,\"sources\":"<<total<<",\"source_index_classifications\":"<<35*total<<",\"minimum_D\":"<<minD<<",\"maximum_minimum_cost\":"<<maxCost<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"peak_rss_bytes\":"<<peakBytes<<"}\n";
 cout<<"PASS sources="<<total<<" minD="<<minD<<" maxcost="<<maxCost<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

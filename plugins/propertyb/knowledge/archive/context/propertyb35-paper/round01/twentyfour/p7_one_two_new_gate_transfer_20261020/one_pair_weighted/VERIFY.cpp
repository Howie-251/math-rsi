#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <sys/resource.h>
using namespace std;
int bits(int x){int n=0;while(x){x&=x-1;++n;}return n;}
int moveMask(int m,const array<int,7>&p){int v=0;for(int i=0;i<7;i++)if(m&(1<<i))v|=1<<p[i];return v;}
struct Job{int cas;vector<int>quad;};struct Row{int D,Q,m,t,W,M;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();vector<int>tri,redsets,pairs,quads;array<int,128>trank{},prank{};trank.fill(-1);prank.fill(-1);
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)tri.push_back((1<<i)|(1<<j)|(1<<k));
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++)for(int l=k+1;l<7;l++)redsets.push_back((1<<i)|(1<<j)|(1<<k)|(1<<l));
 int nt=0,np=0;for(int m=0;m<128;m++){if(bits(m)==3)trank[m]=nt++;if(bits(m)==2){prank[m]=np++;pairs.push_back(m);}if(bits(m)==4)quads.push_back(m);}
 vector<vector<int>>internals={{31},{124,121},{124,115}};vector<Job>jobs;
 for(int cas=0;cas<3;cas++){
  vector<array<int,7>>group;array<int,7>p={0,1,2,3,4,5,6};auto expected=internals[cas];sort(expected.begin(),expected.end());
  do{vector<int>im;for(int I:internals[cas])im.push_back(moveMask(I,p));sort(im.begin(),im.end());if(im==expected)group.push_back(p);}while(next_permutation(p.begin(),p.end()));assert(group.size()==(cas==0?240:48));
  vector<array<int,35>>actions;for(auto p:group){array<int,35>a{};for(int k=0;k<35;k++)a[k]=moveMask(quads[k],p);actions.push_back(a);}
  set<vector<int>>reps;vector<int>idx;long raw=0;int nq=cas==0?4:2;
  function<void(int)>build=[&](int first){if(int(idx.size())<nq){for(int k=first;k<35;k++){idx.push_back(k);build(k);idx.pop_back();}return;}++raw;vector<int>best;for(int k:idx)best.push_back(quads[k]);for(auto action:actions){vector<int>image;for(int k:idx)image.push_back(action[k]);sort(image.begin(),image.end());best=min(best,image);}reps.insert(best);};
  build(0);assert(raw==(cas==0?73815:630));assert(reps.size()==(cas==0?615:(cas==1?46:41)));for(auto q:reps)jobs.push_back({cas,q});
 }
 assert(jobs.size()==702);ifstream jf(dir+"/JOBS.tsv");for(int j=0;j<702;j++){int id,cas,nq;assert(jf>>id>>cas>>nq);assert(id==j&&cas==jobs[j].cas&&nq==int(jobs[j].quad.size()));for(int q:jobs[j].quad){int stored;assert(jf>>stored);assert(stored==q);}}int extra;assert(!(jf>>extra));
 unordered_map<uint64_t,Row>records;records.reserve(1700000);ifstream in(dir+"/NECESSARY.tsv");int job,J,D,Q,m,t,W,M;unsigned packed;
 while(in>>job>>packed>>J>>D>>Q>>m>>t>>W>>M){assert(job>=0&&job<702&&prank[J]>=0&&m+t<=11&&D>0&&D==W-M);uint64_t key=(uint64_t(job)<<32)|(uint64_t(packed)<<5)|prank[J];assert(records.emplace(key,Row{D,Q,m,t,W,M}).second);}assert(in.eof());size_t original=records.size();long total=0;int minD=100000;array<long,3>bycase{};map<pair<int,int>,long>signatures;
 ofstream out(dir+"/INDEPENDENT_CHECK.json");out<<"{\"scope\":\"independent full quad canonical jobs; P3 multiplicity-vector domain, J-first outer loop; four-red complement weights; full exact source keys and35-index classification\",\"all702_jobs_independently_recovered\":true,\"jobs\":[";
 for(int jobid=0;jobid<702;jobid++){
  auto spec=jobs[jobid];auto internal=internals[spec.cas];int totalT=spec.cas==0?2:3;array<int,7>c{},b{};for(int v=0;v<7;v++){for(int I:internal)c[v]+=int(I&(1<<v)?1:0);for(int q:spec.quad)b[v]+=int(q&(1<<v)?1:0);}
  long count=0,leaves=0;int localD=100000;
  for(int J:pairs){
   array<int,7>a{},s{};for(int v=0;v<7;v++)s[v]=int(J&(1<<v)?1:0);array<int,35>mult{};array<unsigned,35>paircov{};unsigned base=0;
   for(int k=0;k<21;k++){int pair=pairs[k];bool cov=(pair&J)==pair;for(int I:internal)cov=cov||((pair&I)==pair);for(int q:spec.quad)cov=cov||((pair&q)==pair);if(cov)base|=1u<<k;}
   for(int k=0;k<35;k++)for(int z=0;z<21;z++)if((tri[k]&pairs[z])==pairs[z])paircov[k]|=1u<<z;
   function<void(int,int,unsigned)>visit=[&](int pos,int left,unsigned cover){
    if(!left){
     ++leaves;if(cover!=(1u<<21)-1)return;array<int,7>u{};int sumu=0;for(int v=0;v<7;v++){u[v]=8-c[v]-a[v]-b[v]-s[v];assert(u[v]>=0&&4*u[v]+2*a[v]+b[v]+3*s[v]>=17);sumu+=u[v];}assert(sumu==27);
     vector<int>expanded,distinct;for(int k=0;k<35;k++)if(mult[k]){distinct.push_back(tri[k]);for(int r=0;r<mult[k];r++)expanded.push_back(tri[k]);}assert(expanded.size()==size_t(totalT));sort(expanded.begin(),expanded.end());unsigned enc=0;for(int k=0;k<totalT;k++)enc|=unsigned(trank[expanded[k]])<<(6*k);
     uint64_t key=(uint64_t(jobid)<<32)|(uint64_t(enc)<<5)|prank[J];auto it=records.find(key);assert(it!=records.end());Row r=it->second;
     vector<int>allhigh=distinct;allhigh.insert(allhigh.end(),spec.quad.begin(),spec.quad.end());sort(allhigh.begin(),allhigh.end());allhigh.erase(unique(allhigh.begin(),allhigh.end()),allhigh.end());
     int ww=0,mm=0,bestscore=99;
     for(int red:redsets){
      int blue=127^red;bool exclude=(J&red)==0;for(int T:distinct)exclude=exclude||((T&blue)==T);if(exclude)continue;
      int redCost=0;for(int v=0;v<7;v++)if(red&(1<<v))redCost+=u[v];int redJ=int((J&red)==J),weight=max(0,redCost-15-redJ),miss=0;for(int T:allhigh)miss+=int((T&red)==T);ww+=weight;mm+=weight*miss;if(!miss)bestscore=min(bestscore,27-redCost+redJ);
     }
     assert(ww==r.W&&mm==r.M&&ww-mm==r.D&&ww>mm&&bestscore==r.m+r.t&&bestscore<=11);
     assert(bits(r.Q)==3&&(r.Q&J)!=J);int cost=0;for(int v=0;v<7;v++)if(r.Q&(1<<v))cost+=u[v];assert(cost==r.m&&int(!(r.Q&J))==r.t);
     vector<int>source=internal;source.insert(source.end(),expanded.begin(),expanded.end());source.insert(source.end(),spec.quad.begin(),spec.quad.end());source.push_back(J);for(int v=0;v<7;v++){assert(c[v]+a[v]+b[v]+s[v]+u[v]==8);for(int z=0;z<u[v];z++)source.push_back(1<<v);}assert(source.size()==35);
     array<int,5>positive{},negative{};int proper=0,freeInc=0;for(int T:source){int free=5-bits(T);freeInc+=free;if((T&r.Q)&&(T&(127^r.Q)))++proper;else if((T&r.Q)==T)++positive[free];else ++negative[free];}
     assert(freeInc==119&&proper==8-r.t&&positive[4]==r.m&&negative[3]==r.t&&negative[4]==27-r.m);for(int k=0;k<4;k++)assert(positive[k]==0);for(int k=0;k<3;k++)assert(negative[k]==0);
     signatures[{r.m,r.t}]++;records.erase(it);++count;localD=min(localD,r.D);return;
    }
    if(pos==35)return;
    for(int z=0;z<=left;z++){
     bool possible=true;for(int v=0;v<7;v++){int av=a[v]+((tri[pos]&(1<<v))?z:0),upper=8-c[v]-av-b[v]-s[v];if(upper<0||4*upper+2*av+b[v]+3*s[v]<17)possible=false;}if(!possible)continue;
     mult[pos]=z;for(int v=0;v<7;v++)if(tri[pos]&(1<<v))a[v]+=z;
     visit(pos+1,left-z,z?cover|paircov[pos]:cover);
     for(int v=0;v<7;v++)if(tri[pos]&(1<<v))a[v]-=z;
    }
    mult[pos]=0;
   };
   visit(0,totalT,base);
  }
  total+=count;bycase[spec.cas]+=count;minD=min(minD,localD);if(jobid)out<<',';out<<"{\"id\":"<<jobid<<",\"case\":"<<spec.cas<<",\"degree_feasible_leaves\":"<<leaves<<",\"necessary\":"<<count<<",\"minimum_D\":"<<localD<<"}";assert(double(clock()-start)/CLOCKS_PER_SEC<25);
 }
 assert(records.empty()&&total==long(original));rusage usage{};getrusage(RUSAGE_SELF,&usage);
#ifdef __APPLE__
 uint64_t peakBytes=usage.ru_maxrss;
#else
 uint64_t peakBytes=uint64_t(usage.ru_maxrss)*1024;
#endif
 assert(peakBytes<(uint64_t(1)<<30));out<<"],\"PASS\":true,\"full_keyset_equal\":true,\"all_W_M_D_own_witnesses_and35_traces_checked\":true,\"sources\":"<<total<<",\"by_case\":["<<bycase[0]<<','<<bycase[1]<<','<<bycase[2]<<"],\"source_index_classifications\":"<<35*total<<",\"minimum_D\":"<<minD<<",\"witness_signature_counts\":[";bool first=true;for(auto[x,n]:signatures){if(!first)out<<',';first=false;out<<'['<<x.first<<','<<x.second<<','<<n<<']';}out<<"],\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"peak_rss_bytes\":"<<peakBytes<<"}\n";
 cout<<"PASS sources="<<total<<" minD="<<minD<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <unordered_set>
#include <vector>
using namespace std;
int pc(int x){return __builtin_popcount((unsigned)x);}
struct Job{int id,cas,q1,q2,q3,orbit;};
struct Rec{uint64_t J;uint16_t job;uint8_t blue,gate,m4,m3,t,b;};
static_assert(sizeof(Rec)==16);
int moveMask(int m,const array<int,7>&p){int out=0;for(int v=0;v<7;v++)if(m>>v&1)out|=1<<p[v];return out;}
bool accepts(int g,int a,int d,int n,int t,int b){int m=a+d;
 if(g==1)return m==0;
 if(g==2)return n==1&&d==0&&a<=4;
 if(n)return false;
 switch(g){
 case 3:return m<=4;
 case 4:return m<=5&&t<=3;
 case 5:return m<=6&&d<=3&&t<=1;
 case 6:return m<=7&&d<=2&&t<=1;
 case 7:return m<=7&&d<=4&&t==0;
 case 8:return m==8&&d<=1&&t<=2&&b<=19;
 case 9:return d==0&&a<=7&&t<=4&&b<=35;
 case 10:return d==0&&a<=6&&t<=6&&b<=35;
 case 11:return d==0&&a<=5&&t<=10&&b<=32;
 case 12:return d==0&&a==8&&((t<=4&&b<=17)||(t<=3&&b<=20));
 case 13:return d==0&&a==9&&t<=3;
 case 14:return d==0&&a==10&&t<=2;
 case 15:return d==0&&a<=11&&t==0&&b<=17;
 default:return false;}}
int main(int argc,char**argv){assert(argc==2);string dir=argv[1];clock_t start=clock();
 vector<Job>jobs;ifstream ji(dir+"/JOBS.tsv");Job temp;while(ji>>temp.id>>temp.cas>>temp.q1>>temp.q2>>temp.q3>>temp.orbit)jobs.push_back(temp);assert(jobs.size()==630);
 vector<int>pairs,quads;array<array<int,7>,7> edge{};for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){edge[i][j]=edge[j][i]=pairs.size();pairs.push_back((1<<i)|(1<<j));}assert(pairs.size()==21);
 // Reordering between this vertex-first pair list and numeric masks is explicit.
 vector<int>numeric=pairs;sort(numeric.begin(),numeric.end());array<int,21>numericIndex{};for(int k=0;k<21;k++)numericIndex[k]=find(numeric.begin(),numeric.end(),pairs[k])-numeric.begin();
 for(int m=0;m<128;m++)if(pc(m)==4)quads.push_back(m);
 for(int cas=0;cas<2;cas++){
  vector<int>Is={124,cas==0?122:115};vector<array<int,7>>group;array<int,7>p{0,1,2,3,4,5,6};
  do{vector<int>image;for(int I:Is)image.push_back(moveMask(I,p));sort(image.begin(),image.end());vector<int>sortedIs=Is;sort(sortedIs.begin(),sortedIs.end());if(image==sortedIs)group.push_back(p);}while(next_permutation(p.begin(),p.end()));assert(group.size()==48);
  map<array<int,3>,int> census;
  for(int i=0;i<35;i++)for(int j=i;j<35;j++)for(int k=j;k<35;k++){array<int,3>best{128,128,128};for(auto p:group){array<int,3> image{moveMask(quads[i],p),moveMask(quads[j],p),moveMask(quads[k],p)};sort(image.begin(),image.end());best=min(best,image);}census[best]++;}
  int nj=0,images=0;for(Job j:jobs)if(j.cas==cas){assert(census.count((array<int,3>{j.q1,j.q2,j.q3}))&&census[(array<int,3>{j.q1,j.q2,j.q3})]==j.orbit);nj++;images+=j.orbit;}assert(nj==int(census.size())&&images==7770);
 }
 ifstream in(dir+"/NECESSARY.bin",ios::binary);Rec pending{};bool has=bool(in.read((char*)&pending,sizeof pending));long total=0,traceRoles=0;array<long,16>gateCounts{};ofstream out(dir+"/INDEPENDENT_CHECK.json");out<<"{\"jobs\":[";
 for(Job job:jobs){
  vector<int>Is={124,job.cas==0?122:115};array<int,7>c{},h{},cap{};for(int v=0;v<7;v++){for(int I:Is)c[v]+=bool(I>>v&1);for(int q:{job.q1,job.q2,job.q3})h[v]+=bool(q>>v&1);cap[v]=-1;
   for(int s=0;s<=7;s++){int u=8-c[v]-h[v]-s;if(u>=0&&4*u+3*s+h[v]>=17)cap[v]=s;}}
  unordered_set<uint64_t> expected;long source=0;
  while(has&&pending.job==job.id){
   Rec r=pending;assert(expected.insert(r.J).second);source++;array<int,21>m{};array<int,7>s{},u{};int countJ=0;
   for(int k=0;k<21;k++){m[k]=(r.J>>(3*k))&7;countJ+=m[k];for(int v=0;v<7;v++)if(numeric[k]>>v&1)s[v]+=m[k];}assert(countJ==4);
   for(int v=0;v<7;v++){u[v]=8-c[v]-h[v]-s[v];assert(u[v]>=0&&4*u[v]+3*s[v]+h[v]>=17);}
   for(int P:numeric){bool cov=false;for(int I:Is)cov|=(P&I)==P;for(int q:{job.q1,job.q2,job.q3})cov|=(P&q)==P;for(int k=0;k<21;k++)if(m[k]&&numeric[k]==P)cov=true;assert(cov);}
   vector<pair<int,int>>stubs;for(int I:Is)stubs.push_back({I,0});for(int q:{job.q1,job.q2,job.q3})stubs.push_back({q,1});for(int k=0;k<21;k++)for(int a=0;a<m[k];a++)stubs.push_back({numeric[k],3});for(int v=0;v<7;v++)for(int a=0;a<u[v];a++)stubs.push_back({1<<v,4});assert(stubs.size()==35);
   array<int,5>positive{},negative{};assert(r.blue&&pc(r.blue)<=4);
   for(auto [P,k]:stubs){int blue=pc(P&r.blue);if(!blue)negative[k]++;else if(blue==pc(P))positive[k]++;traceRoles++;}
   assert(positive[0]==0&&negative[0]==0&&positive[1]==0&&positive[2]==0&&negative[2]==0);
   assert(positive[4]==r.m4&&positive[3]==r.m3&&negative[3]==r.t&&negative[4]==r.b);
   assert(accepts(r.gate,r.m4,r.m3,negative[1],r.t,r.b));gateCounts[r.gate]++;
   has=bool(in.read((char*)&pending,sizeof pending));
  }
  array<array<int,7>,7>lower{};bool possible=true;for(int i=0;i<7;i++)if(cap[i]<0)possible=false;
  for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){int P=(1<<i)|(1<<j);bool covered=false;for(int I:Is)covered|=(P&I)==P;for(int q:{job.q1,job.q2,job.q3})covered|=(P&q)==P;lower[i][j]=!covered;}
  array<int,7>used{};array<array<int,7>,7>matrix{};long regenerated=0;
  function<void(int,int)>row;
  row=[&](int v,int left){
   if(v==7){if(left)return;uint64_t key=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){assert(matrix[i][j]<8);int num=lower_bound(numeric.begin(),numeric.end(),(1<<i)|(1<<j))-numeric.begin();key|=uint64_t(matrix[i][j])<<(3*num);}assert(expected.erase(key)==1);regenerated++;return;}
   function<void(int,int)>star=[&](int w,int available){
    if(w==7){row(v+1,available);return;}
    int high=min({available,cap[v]-used[v],cap[w]-used[w]});
    for(int k=lower[v][w];k<=high;k++){matrix[v][w]=k;used[v]+=k;used[w]+=k;star(w+1,available-k);used[v]-=k;used[w]-=k;}
   };
   star(v+1,left);
  };
  if(possible)row(0,4);assert(expected.empty()&&source==regenerated);total+=source;
  if(job.id)out<<',';out<<"{\"id\":"<<job.id<<",\"source_keys\":"<<source<<",\"regenerated_keys\":"<<regenerated<<"}";
  assert(double(clock()-start)/CLOCKS_PER_SEC<30);
 }
 assert(!has&&in.eof());assert(traceRoles==35*total);
 out<<"],\"status\":\"PASS\",\"complete_domain_key_equality\":true,\"source_total\":"<<total<<",\"reclassified_original_trace_roles\":"<<traceRoles<<",\"gate_counts\":[";for(int k=0;k<16;k++){if(k)out<<',';out<<gateCounts[k];}out<<"],\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"PASS complete domain keys="<<total<<" source roles="<<traceRoles<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

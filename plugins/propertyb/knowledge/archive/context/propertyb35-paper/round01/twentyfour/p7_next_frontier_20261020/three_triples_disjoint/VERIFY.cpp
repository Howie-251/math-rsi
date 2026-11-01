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
#include <unordered_set>
#include <vector>
using namespace std;
int pc(int m){return __builtin_popcount((unsigned)m);}
struct Job{int id;array<int,3>T;int orbit;};
struct Rec{uint64_t J;uint16_t job;uint8_t blue,tag,m4,m3,t,b;};
static_assert(sizeof(Rec)==16);
int moveMask(int m,array<int,7>p){int r=0;for(int v=0;v<7;v++)if(m>>v&1)r|=1<<p[v];return r;}
bool accepts(int g,int a,int d,int n2,int t,int b){int m=a+d;
 switch(g){
 case 1:return m==0;
 case 2:return n2==1&&d==0&&a<=4;
 case 16:return n2<=2&&m<=2;
 case 17:return d==0&&a<=4&&n2<=3;
 case 18:return d==0&&a<=3&&n2<=3&&t<=(4-n2)*16-1;
 case 19:return n2==1&&m<=5&&d<=3&&t<=2;
 case 20:return n2==1&&m<=5&&t==0;
 }
 if(n2)return false;
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
 default:return false;
 }}
int main(int argc,char**argv){assert(argc==2);string dir=argv[1];clock_t start=clock();
 vector<Job>jobs;ifstream js(dir+"/JOBS.tsv");Job j;while(js>>j.id>>j.T[0]>>j.T[1]>>j.T[2]>>j.orbit)jobs.push_back(j);assert(jobs.size()==64);
 vector<int>triples,numeric;for(int m=0;m<128;m++){if(pc(m)==3)triples.push_back(m);if(pc(m)==2)numeric.push_back(m);}
 // Independently build the 48-element action from block permutations on 0123 and 456.
 vector<array<int,7>>group;array<int,4>a{0,1,2,3};do{int block=(1<<a[0])|(1<<a[1]);if(block!=3&&block!=12)continue;array<int,3>b{4,5,6};do{array<int,7>p{a[0],a[1],a[2],a[3],b[0],b[1],b[2]};assert((moveMask(124,p)==124&&moveMask(115,p)==115)||(moveMask(124,p)==115&&moveMask(115,p)==124));group.push_back(p);}while(next_permutation(b.begin(),b.end()));}while(next_permutation(a.begin(),a.end()));assert(group.size()==48);
 // Ordered high triples, followed by set insertion, independently recover all unordered keys.
 set<array<int,3>>all,valid;for(int A:triples)for(int B:triples)for(int C:triples){array<int,3>h{A,B,C};sort(h.begin(),h.end());all.insert(h);bool ok=true;for(int v=4;v<7;v++)if(bool(A>>v&1)+bool(B>>v&1)+bool(C>>v&1)>1)ok=false;if(ok)valid.insert(h);}assert(all.size()==7770&&valid.size()==1266);
 map<array<int,3>,int>census;for(auto h:valid){array<int,3>best{128,128,128};for(auto p:group){array<int,3>im{moveMask(h[0],p),moveMask(h[1],p),moveMask(h[2],p)};sort(im.begin(),im.end());best=min(best,im);}census[best]++;}assert(census.size()==64);int orbitTotal=0;for(Job q:jobs){assert(census.count(q.T)&&census[q.T]==q.orbit);census.erase(q.T);orbitTotal+=q.orbit;}assert(census.empty()&&orbitTotal==1266);
 ifstream in(dir+"/NECESSARY.bin",ios::binary);Rec pending{};bool has=bool(in.read((char*)&pending,sizeof pending));long total=0,roles=0;array<long,21>gc{};ofstream out(dir+"/INDEPENDENT_CHECK.json");out<<"{\"jobs\":[";
 for(Job job:jobs){array<int,7>h{},c{},cap{};for(int v=0;v<7;v++){c[v]=v<4?1:2;for(int T:job.T)h[v]+=bool(T>>v&1);cap[v]=-1;for(int s=0;s<=8;s++){int u=8-c[v]-h[v]-s;bool ok=u>=0&&4*u+3*s+2*h[v]>=17;if(v>=4)ok&=h[v]+s<=1;if(ok)cap[v]=s;}}
  unordered_set<uint64_t>expected;long source=0;
  while(has&&pending.job==job.id){Rec r=pending;assert(expected.insert(r.J).second);source++;array<int,7>sd{},u{};array<int,21>m{};int sum=0;for(int k=0;k<21;k++){m[k]=(r.J>>(3*k))&7;sum+=m[k];for(int v=0;v<7;v++)if(numeric[k]>>v&1)sd[v]+=m[k];}assert(sum==7);for(int v=0;v<7;v++){u[v]=8-c[v]-h[v]-sd[v];assert(u[v]>=0&&4*u[v]+3*sd[v]+2*h[v]>=17);if(v>=4)assert(h[v]+sd[v]<=1);}
   for(int P:numeric){bool cov=(P&124)==P||(P&115)==P;for(int T:job.T)cov|=(P&T)==P;int k=lower_bound(numeric.begin(),numeric.end(),P)-numeric.begin();cov|=m[k]>0;assert(cov);}
   vector<int>stubs={124,115};for(int T:job.T)stubs.push_back(T);for(int k=0;k<21;k++)for(int z=0;z<m[k];z++)stubs.push_back(numeric[k]);for(int v=0;v<7;v++)for(int z=0;z<u[v];z++)stubs.push_back(1<<v);assert(stubs.size()==35);
   array<int,6>positive{},negative{};assert(r.blue&&pc(r.blue)<=4);for(int S:stubs){int blue=pc(S&r.blue),free=5-pc(S);if(!blue){assert(free>0);negative[free]++;}else if(blue==pc(S)){assert(free>0);positive[free]++;}roles++;}
   assert(positive[1]==0&&positive[2]==0&&negative[1]==0);assert(positive[4]==r.m4&&positive[3]==r.m3&&negative[3]==r.t&&negative[4]==r.b);assert(accepts(r.tag,r.m4,r.m3,negative[2],r.t,r.b));gc[r.tag]++;has=bool(in.read((char*)&pending,sizeof pending));
  }
  // Different constructor: choose each vertex's whole forward star, with lower bounds not prefilled.
  array<array<int,7>,7>lower{},matrix{};for(int v=0;v<7;v++)for(int w=v+1;w<7;w++){int P=(1<<v)|(1<<w);bool cov=(P&124)==P||(P&115)==P;for(int T:job.T)cov|=(P&T)==P;lower[v][w]=!cov;}
  array<int,7>used{};bool possible=true;for(int v=0;v<7;v++)if(cap[v]<0)possible=false;long regenerated=0;
  function<void(int,int)>row;row=[&](int v,int left){if(v==7){if(left)return;uint64_t key=0;for(int i=0;i<7;i++)for(int k=i+1;k<7;k++){int m=matrix[i][k];assert(m<=7);int loc=lower_bound(numeric.begin(),numeric.end(),(1<<i)|(1<<k))-numeric.begin();key|=uint64_t(m)<<(3*loc);}assert(expected.erase(key)==1);regenerated++;return;}
   function<void(int,int)>star;star=[&](int w,int rest){if(w==7){row(v+1,rest);return;}int hi=min({rest,cap[v]-used[v],cap[w]-used[w]});for(int m=lower[v][w];m<=hi;m++){matrix[v][w]=m;used[v]+=m;used[w]+=m;star(w+1,rest-m);used[v]-=m;used[w]-=m;}};star(v+1,left);};
  if(possible)row(0,7);assert(expected.empty()&&source==regenerated);total+=source;if(job.id)out<<',';out<<"{\"id\":"<<job.id<<",\"source_keys\":"<<source<<",\"regenerated_keys\":"<<regenerated<<"}";assert(double(clock()-start)/CLOCKS_PER_SEC<12);
 }
 assert(!has&&in.eof()&&roles==35*total);out<<"],\"status\":\"PASS\",\"complete_domain_key_equality\":true,\"all_high_multisets\":7770,\"conditional_high_multisets\":1266,\"high_orbits\":64,\"source_total\":"<<total<<",\"reclassified_original_trace_roles\":"<<roles<<",\"gate_counts\":[";for(int g=0;g<21;g++){if(g)out<<',';out<<gc[g];}out<<"],\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"PASS keys="<<total<<" roles="<<roles<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

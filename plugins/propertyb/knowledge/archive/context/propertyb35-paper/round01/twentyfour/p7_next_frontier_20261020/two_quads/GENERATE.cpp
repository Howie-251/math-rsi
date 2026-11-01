#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
int pc(int x){return __builtin_popcount((unsigned)x);}
struct Job{int id,cas,q1,q2,orbit;};
struct Rec{uint64_t J;uint16_t job;uint8_t blue,gate,m4,m3,t,b;};
static_assert(sizeof(Rec)==16);
int gate(int m4,int m3,int n1,int t,int b){
 int m=m4+m3;
 if(m==0)return 1;
 if(n1){if(n1==1&&m3==0&&m4<=4)return 2;return 0;}
 if(m<=4)return 3;
 if(m<=5&&t<=3)return 4;
 if(m<=6&&m3<=3&&t<=1)return 5;
 if(m<=7&&m3<=2&&t<=1)return 6;
 if(m<=7&&m3<=4&&t==0)return 7;
 if(m==8&&m3<=1&&t<=2&&b<=19)return 8;
 if(m3)return 0;
 if(m4<=7&&t<=4&&b<=35)return 9;
 if(m4<=6&&t<=6&&b<=35)return 10;
 if(m4<=5&&t<=10&&b<=32)return 11;
 if(m4==8&&((t<=4&&b<=17)||(t<=3&&b<=20)))return 12;
 if(m4==9&&t<=3)return 13;
 if(m4==10&&t<=2)return 14;
 if(m4<=11&&t==0&&b<=17)return 15;
 return 0;
}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];int maxjobs=stoi(argv[2]);
 vector<Job>jobs;ifstream ji(dir+"/JOBS.tsv");Job z;while(ji>>z.id>>z.cas>>z.q1>>z.q2>>z.orbit)jobs.push_back(z);
 assert(jobs.size()==87);vector<int>pairs;for(int m=0;m<128;m++)if(pc(m)==2)pairs.push_back(m);assert(pairs.size()==21);
 vector<int>Qs;for(int k=1;k<=4;k++)for(int q=1;q<127;q++)if(pc(q)==k)Qs.push_back(q);
 ofstream data(dir+"/NECESSARY.bin",ios::binary), summary(dir+"/GENERATION.json"), failure(dir+"/NONGATED.tsv");
 clock_t start=clock();long total=0,fail=0;array<long,16> gc{};bool complete=true;
 summary<<"{\"inventory\":[7,0,2],\"n1\":24,\"jobs\":[";
 for(Job job:jobs){
  if(job.id>=maxjobs){complete=false;break;}
  vector<int>Is={124,job.cas==0?122:115};array<int,7>c{},h{},cap{},u{},sd{};array<int,21>mult{};
  for(int v=0;v<7;v++){for(int I:Is)c[v]+=!!(I>>v&1);h[v]=!!(job.q1>>v&1)+!!(job.q2>>v&1);cap[v]=min(8-c[v]-h[v],15-4*c[v]-3*h[v]);}
  bool initial=true;for(int v=0;v<7;v++)if(cap[v]<0)initial=false;
  int mandatory=0;
  for(int p=0;p<21;p++){
   int P=pairs[p];bool cov=false;for(int I:Is)cov|=(P&I)==P;for(int q:{job.q1,job.q2})cov|=(P&q)==P;
   if(!cov){mult[p]=1;mandatory++;for(int v=0;v<7;v++)if(P>>v&1)sd[v]++;}
  }
  for(int v=0;v<7;v++)if(sd[v]>cap[v])initial=false;
  long necessary=0,nongated=0;array<long,16>local{};
  vector<int>validQ;for(int Q:Qs){bool ok=true;for(int I:Is)if(!(Q&I)||(Q&I)==I)ok=false;for(int q:{job.q1,job.q2})if((q&Q)==q)ok=false;if(ok)validQ.push_back(Q);}
  function<void(int,int)>rec=[&](int p,int left){
   if(p==21){if(left)return;
    ++necessary;for(int v=0;v<7;v++){u[v]=8-c[v]-h[v]-sd[v];assert(u[v]>=0&&sd[v]+3*h[v]<=15-4*c[v]);}
    int bestQ=0,bestG=0,bm4=0,bm3=0,bt=0,bb=0;
    for(int Q:validQ){int m4=0,m3=0,t=0,n1=0;for(int v=0;v<7;v++)if(Q>>v&1)m4+=u[v];for(int k=0;k<21;k++){if((pairs[k]&Q)==pairs[k])m3+=mult[k];if(!(pairs[k]&Q))t+=mult[k];}for(int q:{job.q1,job.q2})if(!(q&Q))n1++;int b=24-m4;int g=gate(m4,m3,n1,t,b);if(g){bestQ=Q;bestG=g;bm4=m4;bm3=m3;bt=t;bb=b;break;}}
    uint64_t packed=0;for(int k=0;k<21;k++){assert(mult[k]<8);packed|=uint64_t(mult[k])<<(3*k);}
    Rec r{packed,uint16_t(job.id),uint8_t(bestQ),uint8_t(bestG),uint8_t(bm4),uint8_t(bm3),uint8_t(bt),uint8_t(bb)};data.write((char*)&r,sizeof r);
    if(bestG)local[bestG]++;else{nongated++;failure<<job.id<<' '<<packed<<'\n';}
    return;
   }
   int P=pairs[p],a=__builtin_ctz((unsigned)P),b=__builtin_ctz((unsigned)(P&(P-1)));
   int kmax=min({left,cap[a]-sd[a],cap[b]-sd[b]});if(kmax<0)return;
   for(int k=0;k<=kmax;k++){mult[p]+=k;sd[a]+=k;sd[b]+=k;rec(p+1,left-k);sd[a]-=k;sd[b]-=k;mult[p]-=k;}
  };
  if(initial&&mandatory<=7)rec(0,7-mandatory);
  total+=necessary;fail+=nongated;for(int k=0;k<16;k++)gc[k]+=local[k];
  if(job.id)summary<<',';summary<<"{\"id\":"<<job.id<<",\"case\":"<<job.cas<<",\"quads\":["<<job.q1<<','<<job.q2<<"],\"orbit_size\":"<<job.orbit<<",\"mandatory_pairs\":"<<mandatory<<",\"necessary\":"<<necessary<<",\"nongated\":"<<nongated<<"}";
  if(double(clock()-start)/CLOCKS_PER_SEC>60){complete=false;break;}
 }
 summary<<"],\"complete\":"<<(complete?"true":"false")<<",\"necessary_total\":"<<total<<",\"nongated_total\":"<<fail<<",\"gate_counts\":[";for(int k=0;k<16;k++){if(k)summary<<',';summary<<gc[k];}summary<<"],\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"complete="<<complete<<" necessary="<<total<<" nongated="<<fail<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
 return complete?0:2;
}

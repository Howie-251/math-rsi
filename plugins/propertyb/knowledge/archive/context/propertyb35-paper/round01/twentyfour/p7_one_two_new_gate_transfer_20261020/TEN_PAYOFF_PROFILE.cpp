#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int pc(int a){return __builtin_popcount((unsigned)a);}
int main(int argc,char**argv){
 assert(argc==2);clock_t start=clock();vector<int> pairs,tri,quad,Q;
 for(int m=0;m<128;m++){if(pc(m)==2)pairs.push_back(m);if(pc(m)==3)tri.push_back(m);if(pc(m)==4)quad.push_back(m);if(pc(m)==2||pc(m)==3)Q.push_back(m);}
 ofstream out(argv[1]);out<<"{\"scope\":\"I2 inventory (2,1,3); all labelled higher multisets and two-pair multisets; u/PL/Ppair necessary domain; own blue sets of size2/3; pure signed gates only\",\"shapes\":[";
 long total=0;bool complete=true;
 for(int shape=0;shape<2;shape++){
  int i1=127^3,i2=127^(shape==0?6:12);array<int,7>c{};for(int v=0;v<7;v++)c[v]=((i1>>v)&1)+((i2>>v)&1);
  long highseen=0,necessary=0,old=0,nine=0,ten=0,fail=0;array<long,4>paironly{};vector<int> first;
  for(int a=0;a<35;a++)for(int b=a;b<35;b++)for(int d=b;d<35;d++)for(int t:tri){
   vector<int> H={quad[a],quad[b],quad[d],t};array<int,7>h{},w{};bool ok=true;
   for(int T:H)for(int v=0;v<7;v++)if((T>>v)&1){h[v]++;w[v]+=pc(T)-1;}
   for(int v=0;v<7;v++)if(h[v]+c[v]>8||w[v]>15-4*c[v])ok=false;
   if(!ok)continue;
   vector<int> uncovered;for(int e:pairs){bool cov=(e&i1)==e||(e&i2)==e;for(int T:H)cov=cov||((e&T)==e);if(!cov)uncovered.push_back(e);}
   if(uncovered.size()>2)continue;highseen++;
   for(int j=0;j<21;j++)for(int k=j;k<21;k++){
    int e=pairs[j],f=pairs[k];if(uncovered.size()&&(!((uncovered[0]==e)||(uncovered[0]==f))))continue;
    if(uncovered.size()==2&&uncovered[1]!=e&&uncovered[1]!=f)continue;
    array<int,7>s{},u{};ok=true;
    for(int v=0;v<7;v++){s[v]=((e>>v)&1)+((f>>v)&1);u[v]=8-c[v]-h[v]-s[v];if(u[v]<0||s[v]+w[v]>15-4*c[v])ok=false;}
    if(!ok)continue;necessary++;int best=4,bestpair=4,bestQ=0,bestm=0,bestT=0,bestB=0;
    for(int blue:Q){
     if(!(blue&i1)||!(blue&i2))continue;
     bool proper=true;for(int T:H)if(!(T&blue)||(T&blue)==T)proper=false;
     if(!proper||(e&blue)==e||(f&blue)==f)continue;
     int m=0;for(int v=0;v<7;v++)if((blue>>v)&1)m+=u[v];
     int T=int(!(e&blue))+int(!(f&blue)),B=27-m;
     int gate=4;
     if((m<=5)||(m<=6&&T<=6&&B<=35)||(m<=7&&T<=4&&B<=35)||(m==8&&((T<=3&&B<=20)||(T<=4&&B<=17)))||(m==9&&T<=3&&T+B<=20)||(m<=11&&T==0&&B<=17))gate=0;
     else if(m==9&&T<=3)gate=1;
     else if(m==10&&T<=2&&B<=18)gate=2;
     if(pc(blue)==2)bestpair=min(bestpair,gate);
     if(gate<best){best=gate;bestQ=blue;bestm=m;bestT=T;bestB=B;}
    }
    if(bestpair<3)paironly[bestpair]++;else paironly[3]++;
    if(best==0)old++;else if(best==1)nine++;else if(best==2)ten++;else{fail++;if(first.empty()){first=H;first.push_back(e);first.push_back(f);}}
   }
   if(double(clock()-start)/CLOCKS_PER_SEC>20){complete=false;goto done;}
  }
  done:
  assert(necessary==old+nine+ten+fail);total+=necessary;
  if(shape)out<<',';
  out<<"{\"missing_shape\":"<<shape<<",\"high_pruned_families\":"<<highseen<<",\"necessary\":"<<necessary<<",\"old\":"<<old<<",\"new_nine_any_B\":"<<nine<<",\"new_ten\":"<<ten<<",\"nongated\":"<<fail<<",\"pair_only_by_same_order\":["<<paironly[0]<<','<<paironly[1]<<','<<paironly[2]<<','<<paironly[3]<<"],\"first_nongated_masks\":[";
  for(int z=0;z<(int)first.size();z++){if(z)out<<',';out<<first[z];}out<<"]}";
  if(!complete)break;
 }
 out<<"],\"complete\":"<<(complete?"true":"false")<<",\"necessary_total\":"<<total<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"complete="<<complete<<" total="<<total<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int pc(int a){return __builtin_popcount((unsigned)a);}
int main(int argc,char**argv){
 assert(argc==2||argc==3);string mode=argc==3?argv[2]:"dedup";assert(mode=="raw"||mode=="dedup"||mode=="exclude");bool exclude_equals=mode=="exclude";vector<int> triples,pairs;for(int m=0;m<128;m++){if(pc(m)==3)triples.push_back(m);if(pc(m)==2)pairs.push_back(m);}
 int I1=127^3,I2=127^12,quad=(1<<0)|(1<<1)|(1<<4)|(1<<5);array<int,7>c{};for(int v=0;v<7;v++)c[v]=int((I1>>v)&1)+int((I2>>v)&1);
 long raw=0,necessary=0,weightedgood=0,fail=0;int maxmin=0,marginmin=100000;vector<int> first_weight_bad,first_real_bad;array<int,7>bad_u{};clock_t start=clock();
 for(int a=0;a<35;a++)for(int b=a;b<35;b++)for(int d=b;d<35;d++)for(int e=d;e<35;e++)for(int f=e;f<35;f++){
  raw++;vector<int> H={triples[a],triples[b],triples[d],triples[e],triples[f],quad};array<int,7>h{},w{},u{};bool ok=true;
  for(int T:H)for(int v=0;v<7;v++)if((T>>v)&1){h[v]++;w[v]+=pc(T)-1;}
  for(int v=0;v<7;v++){u[v]=8-c[v]-h[v];if(u[v]<0||w[v]>15-4*c[v])ok=false;}if(!ok)continue;
  for(int p:pairs){bool covered=(p&I1)==p||(p&I2)==p;for(int T:H)covered=covered||((p&T)==p);if(!covered){ok=false;break;}}if(!ok)continue;
  necessary++;int totalW=0,blockW=0,mincost=99;vector<int> distinctH;for(int T:H){bool exists=false;for(int S:distinctH)exists=exists||(S==T);if(!exists)distinctH.push_back(T);}
  for(int Q:triples){int cost=0;for(int v=0;v<7;v++)if((Q>>v)&1)cost+=u[v];int wt=max(0,12-cost),blocks=0;if(exclude_equals)for(int T:distinctH)if(Q==T)wt=0;totalW+=wt;
   for(int T:(mode=="raw"?H:distinctH))if(!(T&Q)||(T&Q)==T)blocks++;
   blockW+=wt*blocks;if(!blocks)mincost=min(mincost,cost);
  }
  maxmin=max(maxmin,mincost);marginmin=min(marginmin,totalW-blockW);
  if(totalW>blockW)weightedgood++;else if(first_weight_bad.empty()){first_weight_bad=H;bad_u=u;}
  if(mincost>11){fail++;if(first_real_bad.empty())first_real_bad=H;}
 }
 ofstream out(argv[1]);out<<"{\"scope\":\"one labelled P4 representative0145 under disjoint missing01,23; all five-P3 multisets; u/PL/Ppair necessary filters; no exterior layouts\",\"mode\":\""<<mode<<"\",\"exclude_whole_positive_triples_from_weights\":"<<(exclude_equals?"true":"false")<<",\"raw\":"<<raw<<",\"necessary\":"<<necessary<<",\"max_minimum_proper_cost\":"<<maxmin<<",\"cost11_failed\":"<<fail<<",\"positive_deficit_union_strict\":"<<weightedgood<<",\"minimum_weighted_margin\":"<<marginmin<<",\"first_weighted_failure_masks\":[";
 for(int i=0;i<(int)first_weight_bad.size();i++){if(i)out<<',';out<<first_weight_bad[i];}out<<"],\"first_weighted_failure_u\":[";for(int i=0;i<7;i++){if(i)out<<',';out<<bad_u[i];}out<<"],\"first_cost_failure_masks\":[";for(int i=0;i<(int)first_real_bad.size();i++){if(i)out<<',';out<<first_real_bad[i];}out<<"],\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"raw="<<raw<<" necessary="<<necessary<<" fail="<<fail<<" maxmin="<<maxmin<<" weighted="<<weightedgood<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

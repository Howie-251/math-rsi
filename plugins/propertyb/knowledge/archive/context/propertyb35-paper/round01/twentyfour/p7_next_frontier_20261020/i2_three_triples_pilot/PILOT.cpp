#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;
int pc(int x){return __builtin_popcount((unsigned)x);}
int gate(int m4,int m3,int n2,int t,int b){
 int m=m4+m3;if(!m)return 1;
 if(n2==1&&m3==0&&m4<=4)return 2;
 if(n2<=2&&m<=2)return 16;
 if(!m3&&m4<=3&&n2<=3&&t<=(4-n2)*16-1)return 18;
 if(!m3&&m4<=4&&n2<=3)return 17; // CONDITIONAL: IN-REVIEW fourP4/threeN2 gate.
 if(n2)return 0;
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
int main(int argc,char**argv){assert(argc==2);ofstream out(argv[1]);vector<int>ps;for(int p=0;p<128;p++)if(pc(p)==2)ps.push_back(p);
 vector<vector<int>>jobs={{112,7,11},{7,11,13}}; // C=456 plus two O triples; three distinct O triples.
 out<<"{\"scope\":\"TWO_FIXED_DISJOINT_MISSING_JOBS_CONDITIONAL_ON_GATE17\",\"jobs\":[";
 clock_t begin=clock();long totalroles=0;
 for(int job=0;job<2;job++){
  vector<int>hs=jobs[job];array<int,7>h{},c{},cap{},sd{},u{};array<int,21>j{};
  for(int v=0;v<7;v++){c[v]=v<4?1:2;for(int T:hs)h[v]+=!!(T>>v&1);cap[v]=min(8-c[v]-h[v],15-4*c[v]-2*h[v]);if(v>=4)cap[v]=min(cap[v],1-h[v]);assert(cap[v]>=0);}
  int base=0;for(int k=0;k<21;k++){int P=ps[k];bool cov=(P&124)==P||(P&115)==P;for(int T:hs)cov|=(P&T)==P;if(!cov){j[k]=1;base++;for(int v=0;v<7;v++)if(P>>v&1)sd[v]++;}}
  long count=0,fail=0;array<long,19>gc{};bool havefirst=false;array<int,21>first{};
  function<void(int,int)>rec=[&](int k,int left){if(k==21){if(left)return;count++;for(int v=0;v<7;v++)u[v]=8-c[v]-h[v]-sd[v];
   bool ok=false;for(int sz=1;sz<=4&&!ok;sz++)for(int Q=1;Q<127&&!ok;Q++){if(pc(Q)!=sz)continue;bool valid=(Q&124)&&(Q&124)!=124&&(Q&115)&&(Q&115)!=115;for(int T:hs)if((Q&T)==T)valid=false;if(!valid)continue;
    int m4=0,m3=0,n2=0,t=0;for(int v=0;v<7;v++)if(Q>>v&1)m4+=u[v];for(int p=0;p<21;p++){if((ps[p]&Q)==ps[p])m3+=j[p];if(!(ps[p]&Q))t+=j[p];}for(int T:hs)n2+=!(T&Q);int b=23-m4;int tag=gate(m4,m3,n2,t,b);if(!tag)continue;
    // Rebuild the whole 35 indexed P traces; recompute each signed size directly.
    vector<int>source={124,115};source.insert(source.end(),hs.begin(),hs.end());for(int p=0;p<21;p++)for(int z=0;z<j[p];z++)source.push_back(ps[p]);for(int v=0;v<7;v++)for(int z=0;z<u[v];z++)source.push_back(1<<v);assert(source.size()==35);
    array<int,6>pos{},neg{};for(int S:source){int bcnt=pc(S&Q),rsz=5-pc(S);if(!bcnt){assert(rsz>0);neg[rsz]++;}else if(bcnt==pc(S)){assert(rsz>0);pos[rsz]++;}totalroles++;}
    assert(pos[4]==m4&&pos[3]==m3&&pos[1]==0&&pos[2]==0&&neg[1]==0&&neg[2]==n2&&neg[3]==t&&neg[4]==b);gc[tag]++;ok=true;
   }
   if(!ok){fail++;if(!havefirst){first=j;havefirst=true;}}return;}
   int P=ps[k],a=__builtin_ctz((unsigned)P),b=__builtin_ctz((unsigned)(P&(P-1)));int mx=min({left,cap[a]-sd[a],cap[b]-sd[b]});for(int x=0;x<=mx;x++){j[k]+=x;sd[a]+=x;sd[b]+=x;rec(k+1,left-x);sd[a]-=x;sd[b]-=x;j[k]-=x;}
  };
  bool initial=base<=7;for(int v=0;v<7;v++)initial&=sd[v]<=cap[v];if(initial)rec(0,7-base);
  if(job)out<<',';out<<"{\"triple_masks\":["<<hs[0]<<','<<hs[1]<<','<<hs[2]<<"],\"necessary_J\":"<<count<<",\"nongated\":"<<fail<<",\"gate_counts\":[";for(int g=0;g<19;g++){if(g)out<<',';out<<gc[g];}out<<"],\"first_nongated_J\":[";if(havefirst)for(int k=0;k<21;k++){if(k)out<<',';out<<first[k];}out<<"]}";
 }
 out<<"],\"reclassified_original_roles\":"<<totalroles<<",\"cpu_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
}

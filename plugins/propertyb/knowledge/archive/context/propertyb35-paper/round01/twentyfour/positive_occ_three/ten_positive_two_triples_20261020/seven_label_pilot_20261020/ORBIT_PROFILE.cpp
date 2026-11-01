#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <sys/resource.h>
#include <unordered_set>
#include <vector>
using namespace std;
using U64=uint64_t;
array<pair<int,int>,21> edges;
int edgeIndex[7][7];
array<int,21> g{};
array<int,7> degree{};
vector<array<uint8_t,21>> actions;
unordered_set<U64> seen;
array<U64,15> leaves{},covered{};
U64 nodes=0,leafCount=0,repCount=0;
bool stopped=false;
double cpuLimit;U64 repLimit=0;clock_t startCpu;
ofstream reps;
double seconds(){return double(clock()-startCpu)/CLOCKS_PER_SEC;}
U64 peakBytes(){rusage r{};getrusage(RUSAGE_SELF,&r);
#ifdef __APPLE__
return U64(r.ru_maxrss);
#else
return U64(r.ru_maxrss)*1024;
#endif
}
void checkLimit(){if(seconds()>=cpuLimit || peakBytes()>(U64(1)<<30) || (repLimit && repCount>=repLimit))stopped=true;}
U64 encode(){U64 c=0;for(int k=0;k<21;k++)c|=U64(g[k])<<(3*k);return c;}
void leaf(int E){
 if(E<11||E>14)return;
 ++leafCount;++leaves[E];
 U64 code=encode();
 if(seen.find(code)==seen.end()){
  vector<pair<int,int>> positive;
  for(int k=0;k<21;k++)if(g[k])positive.push_back({k,g[k]});
  array<U64,5040> images{};int a=0;
  for(auto &p:actions){U64 image=0;for(auto [k,m]:positive)image|=U64(m)<<(3*p[k]);images[a++]=image;}
  sort(images.begin(),images.end());auto last=unique(images.begin(),images.end());
  U64 orbit=last-images.begin();assert(orbit>0&&5040%orbit==0);
  for(auto it=images.begin();it!=last;++it){bool fresh=seen.insert(*it).second;assert(fresh);}
  ++repCount;covered[E]+=orbit;
  reps<<"{\"code\":\""<<code<<"\",\"E\":"<<E<<",\"orbit_size\":"<<orbit<<",\"vector\":[";
  for(int k=0;k<21;k++){if(k)reps<<',';reps<<g[k];}reps<<"]}\n";
  checkLimit();
 }
 if((leafCount&16383)==0)checkLimit();
}
void row(int v,int E);
void star(int v,int j,int E){
 if(stopped)return;
 if(j==7){row(v+1,E);return;}
 int k=edgeIndex[v][j];int bound=min({4-degree[v],4-degree[j],14-E});
 for(int m=0;m<=bound&&!stopped;m++){
  g[k]=m;degree[v]+=m;degree[j]+=m;
  star(v,j+1,E+m);
  degree[v]-=m;degree[j]-=m;
 }
 g[k]=0;
}
void row(int v,int E){
 if(stopped)return;++nodes;
 if(v==6){leaf(E);return;}
 int capacity=0;for(int i=v;i<7;i++)capacity+=4-degree[i];
 if(E+capacity/2<11)return;
 star(v,v+1,E);
}
int main(int argc,char**argv){
 cpuLimit=argc>1?stod(argv[1]):5;string prefix=argc>2?argv[2]:"ORBIT_PREFIX5";
 if(argc>3)repLimit=stoull(argv[3]);
 int k=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){edges[k]={i,j};edgeIndex[i][j]=edgeIndex[j][i]=k++;}
 array<int,7> p={0,1,2,3,4,5,6};
 do{array<uint8_t,21>a;for(int e=0;e<21;e++)a[e]=edgeIndex[p[edges[e].first]][p[edges[e].second]];actions.push_back(a);}while(next_permutation(p.begin(),p.end()));
 assert(actions.size()==5040);
 startCpu=clock();seen.max_load_factor(1.0f);seen.reserve(10056542);
 reps.open(prefix+"_REPS.jsonl");row(0,0);reps.close();
 bool complete=!stopped;
 const U64 expected[4]={5229168,3535448,1198218,93708};
 if(complete){for(int e=11;e<=14;e++){assert(leaves[e]==expected[e-11]);assert(covered[e]==expected[e-11]);}assert(seen.size()==10056542);}
 ofstream summary(prefix+"_SUMMARY.json");
 summary<<"{\"complete\":"<<(complete?"true":"false")<<",\"cpu_seconds\":"<<seconds()<<",\"peak_rss_bytes\":"<<peakBytes()<<",\"enumerated_labelled_leaves\":"<<leafCount<<",\"seen_unique_orbit_images\":"<<seen.size()<<",\"representatives\":"<<repCount<<",\"recursive_row_nodes\":"<<nodes<<",\"cpu_limit\":"<<cpuLimit<<",\"by_E\":[";
 for(int e=11;e<=14;e++){if(e>11)summary<<',';summary<<"{\"E\":"<<e<<",\"enumerated_leaves\":"<<leaves[e]<<",\"covered_orbit_images\":"<<covered[e]<<",\"expected_DP\":"<<expected[e-11]<<"}";}
 summary<<"]}\n";summary.close();
 cout<<"complete="<<complete<<" leaves="<<leafCount<<" seen="<<seen.size()<<" reps="<<repCount<<" cpu="<<seconds()<<" peak_bytes="<<peakBytes()<<"\n";
}

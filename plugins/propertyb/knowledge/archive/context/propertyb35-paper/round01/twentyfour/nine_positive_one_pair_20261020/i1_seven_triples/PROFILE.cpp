#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int pc(int x){return __builtin_popcount((unsigned)x);}
int main(int argc,char**argv){
 assert(argc>=2);string dir=argv[1]; long limit=argc>2?stol(argv[2]):0;
 vector<int>tr,pairs;for(int x=0;x<128;x++){if(pc(x)==3)tr.push_back(x);if(pc(x)==2)pairs.push_back(x);}
 array<unsigned,128>pairbits{};for(int x=0;x<128;x++)for(int j=0;j<21;j++)if((pairs[j]&x)==pairs[j])pairbits[x]|=1u<<j;
 const unsigned allpairs=(1u<<21)-1; const int C=31;vector<int>Klist={99,39,15};
 clock_t start=clock();bool failure=false,limited=false;long leaves=0,necessary=0;int globalmin=100;
 ofstream out(dir+(limit?"/PILOT.json":"/PROFILE.json"));out<<"{\"scope\":\"I1 (0,7,1), C01234, K intersection2/3/4; full nonnegative PL/Ppair necessary domain; stop first nongated\",\"jobs\":[";
 for(int job=0;job<3;job++){
  int K=Klist[job];array<int,7>a{},u{},cap{};array<int,7>choice{};long nj=0,lj=0,tags[3]={};int mincount=100;bool finished=true;
  for(int v=0;v<7;v++)cap[v]=(15-4*int(v<5)-3*int(K>>v&1))/2;
  function<void(int,int,unsigned)>rec=[&](int depth,int first,unsigned cover){
   if(failure||limited)return;
   if(depth==7){
    ++leaves;++lj;if(limit && leaves>limit){limited=true;finished=false;return;}
    if(cover!=allpairs)return;
    for(int v=0;v<7;v++)u[v]=8-int(v<5)-a[v]-int(K>>v&1);
    ++necessary;++nj;int tag=-1,count=0,bestproper=100,bestone=100;
    for(int Q:pairs){if(!(Q&C)||!(Q&K))continue;bool ok=true;for(int j:choice)if(!(Q&tr[j])){ok=false;break;}if(ok){tag=0;++count;}}
    for(int Q:tr){if(!(Q&K))continue;int misses=0;bool full=false;for(int j:choice){misses+=!(Q&tr[j]);full|=Q==tr[j];}if(full)continue;int m=0;for(int v=0;v<7;v++)if(Q>>v&1)m+=u[v];
     if(misses==0){bestproper=min(bestproper,m);if(m<=11){if(tag<0)tag=1;++count;}}
     if(misses==1){bestone=min(bestone,m);if(m<=9){if(tag<0)tag=2;++count;}}
    }
    if(tag<0){failure=true;finished=false;ofstream f(dir+"/FAILURE.json");f<<"{\"job\":"<<job<<",\"C\":31,\"K\":"<<K<<",\"triples\":[";for(int k=0;k<7;k++){if(k)f<<',';f<<tr[choice[k]];}f<<"],\"u\":[";for(int v=0;v<7;v++){if(v)f<<',';f<<u[v];}f<<"],\"best_proper_m\":"<<bestproper<<",\"best_one_m\":"<<bestone<<",\"necessary_before_stop\":"<<necessary<<"}\n";return;}
    ++tags[tag];mincount=min(mincount,count);globalmin=min(globalmin,count);return;
   }
   for(int j=first;j<35;j++){
    int T=tr[j];bool ok=true;for(int v=0;v<7;v++)if((T>>v&1)&&a[v]>=cap[v])ok=false;if(!ok)continue;
    choice[depth]=j;for(int v=0;v<7;v++)a[v]+=int(T>>v&1);rec(depth+1,j,cover|pairbits[T]);for(int v=0;v<7;v++)a[v]-=int(T>>v&1);if(failure||limited)return;
   }
  };
  rec(0,0,pairbits[C]|pairbits[K]);
  if(job)out<<',';out<<"{\"job\":"<<job<<",\"K\":"<<K<<",\"complete\":"<<(finished?"true":"false")<<",\"PL_legal_leaves\":"<<lj<<",\"necessary\":"<<nj<<",\"tags_pair_proper3_oneMiss3\":["<<tags[0]<<','<<tags[1]<<','<<tags[2]<<"],\"minimum_accepted_menu_count\":"<<mincount<<"}";
  cerr<<"job "<<job<<" leaves "<<lj<<" necessary "<<nj<<" cpu "<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";if(failure||limited)break;
 }
 out<<"],\"complete\":"<<(!failure&&!limited?"true":"false")<<",\"failure\":"<<(failure?"true":"false")<<",\"limited\":"<<(limited?"true":"false")<<",\"leaves\":"<<leaves<<",\"necessary\":"<<necessary<<",\"minimum_accepted_menu_count\":"<<globalmin<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 return failure?2:0;
}

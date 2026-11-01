#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int size(int s){int n=0;while(s){n+=s&1;s>>=1;}return n;}
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();vector<int>T,reds4,reds5;
 for(int s=0;s<128;s++){if(size(s)==3)T.push_back(s);if(size(s)==4)reds4.push_back(s);if(size(s)==5)reds5.push_back(s);}
 long binom[42][8]={};for(int n=0;n<=41;n++){binom[n][0]=1;for(int k=1;k<=7;k++)binom[n][k]=n?binom[n-1][k-1]+binom[n-1][k]:0;}
 long all=0,roles=0;ofstream result(dir+"/INDEPENDENT_RESULT.json");result<<"{\"status\":\"PASS\",\"method\":\"multiplicity recursion, direct star capacity, original P pair coverage, red complements; full combinatorial-rank bitset equality\",\"jobs\":[";
 vector<int>Ks={99,39,15};
 for(int job=0;job<3;job++){
  int K=Ks[job];array<int,7>freq{},u{};array<int,35>mult{};long cnt=0,originalRoles=0;array<long,4>tags{};
  ifstream in(dir+"/DOMAIN_"+to_string(job)+".bits",ios::binary);vector<unsigned char> unseen((22481940+7)/8);in.read((char*)unseen.data(),unseen.size());assert(in.gcount()==(long)unseen.size());assert(in.peek()==EOF);
  function<void(int,int)> walk=[&](int j,int remaining){
   if(remaining==0){
    vector<int>H;array<int,7>degree{};
    for(int v=0;v<7;v++){u[v]=8-int(v<5)-freq[v]-int(K>>v&1);if(u[v]<0||4*u[v]+2*freq[v]+int(K>>v&1)<17)return;}
    for(int k=0;k<35;k++)for(int r=0;r<mult[k];r++)H.push_back(T[k]);assert(H.size()==7);
    for(int i=0;i<7;i++)for(int l=i+1;l<7;l++){
     bool covered=(i<5&&l<5)||((K>>i&1)&&(K>>l&1));for(int s:H)covered|=(s>>i&1)&&(s>>l&1);if(!covered)return;
    }
    int idx=0;long rank=0;for(int k=0;k<35;k++)for(int r=0;r<mult[k];r++){rank+=binom[k+idx][idx+1];++idx;}
    assert(unseen[rank/8]&(1u<<(rank%8)));unseen[rank/8]&=~(1u<<(rank%8));++cnt;
    int Q=0,tag=-1;
    // Single-blue structural rule first, independently of the primary priority.
    for(int v=0;v<5&&!Q;v++)if((K>>v&1)&&freq[v]>=3){Q=1<<v;tag=3;}
    for(int R:reds5){if(Q)break;int B=127^R;bool good=(31&B)&&(K&B);for(int s:H)good&=bool(s&B);if(good){Q=B;tag=0;}}
    for(int R:reds4){if(Q)break;int B=127^R;if(!(K&B))continue;int miss=0;bool pos2=false;for(int s:H){miss+=((s&R)==s);pos2|=((s&B)==s);}if(pos2)continue;
     int m=26;for(int v=0;v<7;v++)if(R>>v&1)m-=u[v];
     if((miss==0&&m<=11)||(miss==1&&m<=9)){Q=B;tag=miss?2:1;}
    }
    assert(Q&&tag>=0);++tags[tag];
    // Reconstruct all 35 indexed original traces, then classify the sole risk.
    vector<int>source={31,K};source.insert(source.end(),H.begin(),H.end());for(int v=0;v<7;v++)for(int r=0;r<u[v];r++)source.push_back(1<<v);assert(source.size()==35);
    int proper=0,p4=0,n2=0,n4=0;
    for(int s:source){++originalRoles;for(int v=0;v<7;v++)degree[v]+=bool(s>>v&1);bool blue=s&Q,red=s&(127^Q);
     if(blue&&red){++proper;continue;}int outside=5-size(s);if(blue){assert(outside==4);++p4;}else if(outside==2)++n2;else{assert(outside==4);++n4;}
    }
    for(int v=0;v<7;v++)assert(degree[v]==8);assert(p4+n4==26&&proper+p4+n2+n4==35);
    if(tag==3)assert(p4<=3&&n2<=4&&size(Q)==1);
    if(tag==0)assert(p4<=7&&n2==0&&size(Q)==2);
    if(tag==1)assert(p4<=11&&n2==0&&size(Q)==3);
    if(tag==2)assert(p4<=9&&n2==1&&size(Q)==3&&n4<=21);
    return;
   }
   if(j==35)return;
   // Distinct type multiplicities, not seven nondecreasing triple positions.
   int s=T[j],cap=remaining;
   for(int v=0;v<7;v++)if(s>>v&1){int upper=8-int(v<5)-freq[v]-int(K>>v&1);int space=(4*upper+2*freq[v]+int(K>>v&1)-17)/2;cap=min(cap,max(-1,space));}
   if(cap<0)return;
   for(int r=0;r<=cap;r++){
    mult[j]=r;for(int v=0;v<7;v++)freq[v]+=r*int(s>>v&1);walk(j+1,remaining-r);for(int v=0;v<7;v++)freq[v]-=r*int(s>>v&1);
   }
   mult[j]=0;
  };
  walk(0,7);for(unsigned char x:unseen)assert(x==0);
  all+=cnt;roles+=originalRoles;if(job)result<<',';result<<"{\"job\":"<<job<<",\"K\":"<<K<<",\"necessary\":"<<cnt<<",\"full_key_equality\":true,\"original_trace_roles\":"<<originalRoles<<",\"own_priority_single_pair_proper3_oneMiss3\":["<<tags[3]<<','<<tags[0]<<','<<tags[1]<<','<<tags[2]<<"]}";
  cerr<<"job "<<job<<" count "<<cnt<<" cpu "<<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
 }
 result<<"],\"necessary\":"<<all<<",\"original_trace_roles\":"<<roles<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}

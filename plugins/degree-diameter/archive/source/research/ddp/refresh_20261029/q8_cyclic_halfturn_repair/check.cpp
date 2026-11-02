#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sys/resource.h>
#include <unistd.h>
#include <vector>
using namespace std;
using U=unsigned long long;
array<int,8> pi={1,3,6,0,5,7,2,4};
array<int,8> first={1,1,1,2,1,1,3,2};
ofstream logf;
long long tested=0;
int hit=-1;
double started;

bool test(const array<int,8>&delta,bool detailed){
 array<int,64>sig{},inv{};array<U,64>G{};
 for(int u=0;u<64;u++){int a=u/8,l=u%8;sig[u]=8*((a+delta[l])%8)+pi[l];inv[sig[u]]=u;}
 for(int u=0;u<64;u++){
  assert(sig[u]!=u&&sig[sig[u]]!=u);
  G[u]=(1ULL<<(u^1))|(1ULL<<(u^2))|(1ULL<<(u^4))|(1ULL<<sig[u])|(1ULL<<inv[u]);
  assert(__builtin_popcountll(G[u])==5);
  int x=u,steps=(u%8==2||u%8==6)?2:3;
  for(int j=0;j<steps;j++)x=sig[x];
  assert(x==8*((u/8+4)%8)+u%8);
 }
 for(int u=0;u<64;u++)for(int v=0;v<64;v++)assert(bool(G[u]>>v&1)==bool(G[v]>>u&1));
 int bad=-1,missing=-1,reached=0;array<U,8>balls{};
 for(int root=0;root<8;root++){
  U reach=1ULL<<root;
  for(int step=0;step<3;step++){U next=reach,scan=reach;while(scan){int u=__builtin_ctzll(scan);scan&=scan-1;next|=G[u];}reach=next;}
  balls[root]=reach;
  if(reach!=~U(0)&&bad<0){bad=root;missing=__builtin_ctzll(~reach);reached=__builtin_popcountll(reach);}
  if(bad>=0&&!detailed)break;
 }
 logf<<"{\"case\":"<<tested<<",\"delta\":[";
 for(int i=0;i<8;i++)logf<<(i?",":"")<<delta[i];
 logf<<"],\"bad_root\":"<<bad<<",\"first_missing\":"<<missing<<",\"reached_at_bad_root\":"<<reached<<",\"all_halfturns_preserved\":true}\n";
 if(detailed){
  ofstream detail("FIRST_CANDIDATE.json");detail<<"{\"root_reach_sizes\":[";
  for(int i=0;i<8;i++)detail<<(i?",":"")<<__builtin_popcountll(balls[i]);
  detail<<"],\"root0_phase_sets\":[";
  for(int l=0;l<8;l++){detail<<(l?",":"")<<"[";bool comma=false;for(int a=0;a<8;a++)if(balls[0]>>(8*a+l)&1){detail<<(comma?",":"")<<a;comma=true;}detail<<"]";}
  detail<<"]}\n";
 }
 if(bad<0){
  hit=tested;
  ofstream out("K64.edges");out<<"64 160\n";
  for(int u=0;u<64;u++)for(int v=u+1;v<64;v++)if(G[u]>>v&1)out<<u<<" "<<v<<"\n";
  ofstream p("HIT_PARAMETERS.json");p<<"{\"pi\":[";
  for(int i=0;i<8;i++)p<<(i?",":"")<<pi[i];
  p<<"],\"delta\":[";for(int i=0;i<8;i++)p<<(i?",":"")<<delta[i];
  p<<"],\"deck_translation_aut\":true,\"representative_roots_checked\":8,\"all_representatives_R3_pass\":true}\n";
 }
 tested++;
 return bad<0;
}

int main(){
 rlimit lim{30,31};setrlimit(RLIMIT_CPU,&lim);started=double(clock())/CLOCKS_PER_SEC;
 ofstream("HANDLE.json")<<"{\"status\":\"RUNNING\",\"pid\":"<<getpid()<<"}\n";
 logf.open("CASES.jsonl");bool found=test(first,true);
 if(!found)for(int a=1;a<8&&!found;a++)for(int b=1;b<8&&!found;b++)for(int c=1;c<8&&!found;c++)if(c!=4)
  for(int d=1;d<8&&!found;d++)for(int e=1;e<8&&!found;e++){
   array<int,8>delta={a,b,c,(20-a-b)%8,d,e,(12-c)%8,(20-d-e)%8};
   if(delta==first)continue;
   found=test(delta,false);
  }
 logf.close();
 ofstream out("RESULT.json");out<<"{\"status\":\""<<(found?"K64_D3_HIT":"COMPLETE_HALF_TURN_FAMILY_NO_HIT")<<"\",\"frozen_cases\":14406,\"tested_cases\":"<<tested<<",\"untried\":"<<14406-tested<<",\"hit_case\":"<<hit<<",\"auxiliary_positive_graphs\":"<<(found?1:0)<<",\"main1088_graphs\":0,\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-started<<",\"pid\":"<<getpid()<<"}\n";
 ofstream("HANDLE.json")<<"{\"status\":\"TERMINAL\",\"pid\":"<<getpid()<<"}\n";
 cout<<"tested="<<tested<<" hit="<<hit<<" CPU="<<double(clock())/CLOCKS_PER_SEC-started<<"\n";
}

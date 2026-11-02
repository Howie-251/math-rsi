#include <algorithm>
#include <array>
#include <csignal>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Mask=uint64_t;
using Labels=array<int,6>;
using Masks=array<Mask,7>;
struct Counts {long long raw=0,hh=0,bb=0,bh=0,blockzero=0,headzero=0;int minBB=449;};
constexpr long long PER_Y=640LL*641/2,TOTAL=64*PER_Y,HH_TOTAL=5693310;
volatile sig_atomic_t stopped=0;
void signal_stop(int){stopped=1;}
int fm(int a,int b){int c=0;while(b){if(b&1)c^=a;b>>=1;a<<=1;if(a&64)a^=0x43;}return c;}
struct Engine{
 static constexpr int q=64,m=21,L=1344,B=448,n=1856;
 array<array<unsigned char,64>,64>mul{};array<int,21>power{};
 array<Mask,64>hm{},km{};vector<unsigned short>product;
 vector<int>inverse,pairs;vector<Masks>kwh;
 vector<vector<int>>adj;vector<int>dist,queue;
 Engine():product(L*L),inverse(L),kwh(L),adj(n),dist(n),queue(n){
  for(int x=0;x<64;x++)for(int y=0;y<64;y++)mul[x][y]=fm(x,y);
  power[0]=1;for(int i=1;i<21;i++)power[i]=mul[power[i-1]][8];
  if(set<int>(power.begin(),power.end()).size()!=21||mul[power[20]][8]!=1)throw runtime_error("bad action");
  for(int x=0;x<64;x++)for(int j=0;j<21;j++){km[x]|=Mask(1)<<mul[power[j]][x];if(j%7==0)hm[x]|=Mask(1)<<mul[power[j]][x];}
  for(int a=0;a<L;a++)for(int b=0;b<L;b++)product[a*L+b]=((a%64)^mul[power[a/64]][b%64])+64*((a/64+b/64)%21);
  for(int a=0;a<L;a++){
   int j=(21-a/64)%21;inverse[a]=mul[power[j]][a%64]+64*j;
   if(product[a*L+inverse[a]]||product[inverse[a]*L+a])throw runtime_error("inverse mismatch");
   if(a<inverse[a])pairs.push_back(a);
   for(int j=0;j<21;j++)kwh[a][(a/64+j)%7]|=Mask(1)<<mul[power[j]][a%64];
  }
  if(pairs.size()!=640)throw runtime_error("wrong quotient pair count");
 }
 bool hh(const Labels&S){Mask z=1;for(int s:S)z|=km[s%64];return z==~Mask(0);}
 Masks bb(const Labels&S){
  // HW3H + KW1H + HW1K. Right H preserves x and i mod 7.
  Masks masks{};Mask common=1;
  for(int s:S)common|=hm[s%64];
  for(int j=0;j<7;j++){masks[j]=common|kwh[0][j];for(int s:S)masks[j]|=kwh[s][j];}
  masks[0]|=hm[0];
  for(int a:S){masks[(a/64)%7]|=hm[a%64];
   for(int b:S){int ab=product[a*L+b];masks[(ab/64)%7]|=hm[ab%64];
    for(int c:S){int abc=product[ab*L+c];masks[(abc/64)%7]|=hm[abc%64];}
   }
  }
  return masks;
 }
 int missing(const Masks&a){int z=448;for(Mask v:a)z-=__builtin_popcountll(v);return z;}
 void build(const Labels&S){
  for(auto&v:adj)v.clear();
  auto edge=[&](int a,int b){if(a!=b){adj[a].push_back(b);adj[b].push_back(a);}};
  for(int a=0;a<L;a++){edge(a,L+a%64+64*((a/64)%7));for(int s:S){int b=product[a*L+s];if(a<b)edge(a,b);}}
  for(int b=0;b<B;b++)edge(L+b,L+B+b%64);
  for(auto&v:adj){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());}
 }
 array<int,3>bfs(int root){
  fill(dist.begin(),dist.end(),-1);int read=0,end=1;queue[0]=root;dist[root]=0;
  while(read<end){int a=queue[read++];if(dist[a]==5)continue;for(int b:adj[a])if(dist[b]<0){dist[b]=dist[a]+1;queue[end++]=b;}}
  array<int,3>miss{};for(int a=0;a<n;a++)if(dist[a]<0)miss[a<L?0:a<L+B?1:2]++;return miss;
 }
 Masks block_bfs_masks(){bfs(L);Masks masks{};for(int b=0;b<B;b++)if(dist[L+b]>=0)masks[b/64]|=Mask(1)<<(b%64);return masks;}
 void edges(string file){ofstream f(file);long long ne=0;for(int a=0;a<n;a++)for(int b:adj[a])if(a<b)ne++;f<<n<<" "<<ne<<"\n";for(int a=0;a<n;a++)for(int b:adj[a])if(a<b)f<<a<<" "<<b<<"\n";}
 void sample(string prefix,const Labels&S,long long cursor,int y,int ia,int ib,bool expand){
  auto masks=bb(S);ofstream f(prefix+".json");
  f<<"{\"candidate_cursor\":"<<cursor<<",\"y\":"<<y<<",\"pair_indices\":["<<ia<<","<<ib<<"],\"quotient_S_ids\":[";
  for(int i=0;i<6;i++)f<<(i?",":"")<<S[i];f<<"],\"quotient_S_coordinates\":[";
  for(int i=0;i<6;i++)f<<(i?",":"")<<"["<<S[i]%64<<","<<S[i]/64<<"]";
  f<<"],\"BB_missing\":"<<missing(masks)<<",\"BB_masks\":[";for(int i=0;i<7;i++)f<<(i?",":"")<<masks[i];f<<"]";
  if(expand){build(S);auto bm=bfs(L),hm=bfs(L+B);f<<",\"block_root_target_missing\":["<<bm[0]<<","<<bm[1]<<","<<bm[2]<<"],\"head_root_target_missing\":["<<hm[0]<<","<<hm[1]<<","<<hm[2]<<"]";edges(prefix+".quotient.edges");}
  f<<"}\n";
 }
};
int main(int argc,char**argv){try{
 clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 Engine e;
 if(argc==9&&string(argv[1])=="check"){
  Labels S;for(int j=0;j<6;j++)S[j]=stoi(argv[j+2]);auto masks=e.bb(S);e.build(S);
  if(masks!=e.block_bfs_masks())throw runtime_error("BB formula versus quotient BFS mismatch");
  e.sample(argv[8],S,-1,-1,-1,-1,true);cout<<"check BB_missing "<<e.missing(masks)<<" cpu "<<cpu()<<endl;return 0;
 }
 if(argc!=5)throw runtime_error("CPU_LIMIT HH_PROFILE_COUNT START_CURSOR PREFIX");
 double limit=stod(argv[1]);long long target=stoll(argv[2]),first=stoll(argv[3]);string prefix=argv[4];
 signal(SIGINT,signal_stop);signal(SIGTERM,signal_stop);
 ofstream pp(prefix+".quotient_pairs.json");pp<<"[";for(int j=0;j<640;j++)pp<<(j?",":"")<<"["<<e.pairs[j]%64<<","<<e.pairs[j]/64<<"]";pp<<"]\n";pp.close();
 long long cursor=0,next=first,raw=0,hh=0,skipped=0,bbpass=0,bhpass=0,blockzero=0,headzero=0;
 int bestBB=449;Labels bestS{},firstS{};int bestY=-1,bestA=-1,bestB=-1,firstY=-1,firstA=-1,firstB=-1;long long bestCursor=-1,firstCursor=-1;
 map<int,long long>hist;double hhCPU=0,bbCPU=0,bfsCPU=0;bool done=false;
 array<Counts,64>by_y{};
 ofstream survivors(prefix+".BH_survivors.jsonl");
 double setup=cpu();
 for(int y=0;y<64&&!done;y++)for(int a=0;a<640&&!done;a++)for(int b=a;b<640;b++,cursor++){
  if(cursor<first)continue;
  if(stopped||cpu()>=limit){done=true;break;}
  Labels S={1,y,e.pairs[a],e.inverse[e.pairs[a]],e.pairs[b],e.inverse[e.pairs[b]]};raw++;next=cursor+1;auto&ct=by_y[y];ct.raw++;
  clock_t t=clock();bool pass=e.hh(S);hhCPU+=double(clock()-t)/CLOCKS_PER_SEC;
  if(!pass){skipped++;continue;}
  hh++;ct.hh++;
  if(firstCursor<0){firstCursor=cursor;firstY=y;firstA=a;firstB=b;firstS=S;}
  t=clock();auto masks=e.bb(S);int miss=e.missing(masks);bbCPU+=double(clock()-t)/CLOCKS_PER_SEC;hist[miss]++;ct.minBB=min(ct.minBB,miss);
  if(miss<bestBB){bestBB=miss;bestS=S;bestY=y;bestA=a;bestB=b;bestCursor=cursor;}
  if(miss==0){bbpass++;ct.bb++;t=clock();e.build(S);auto bm=e.bfs(Engine::L),hm=e.bfs(Engine::L+Engine::B);
   bool bz=bm[0]+bm[1]+bm[2]==0,hz=hm[0]+hm[1]+hm[2]==0;blockzero+=bz;headzero+=hz;ct.blockzero+=bz;ct.headzero+=hz;
   if(bz&&hz){bhpass++;ct.bh++;
    unsigned allowed=0;for(int bits=0;bits<16;bits++){
     int p0=bits&1,p1=(bits>>1)&1,p2=(bits>>2)&1,p3=(bits>>3)&1;
     if(y==0&&p1!=1)continue;if(y==1&&p0==p1)continue;if(a==b&&p2==p3)continue;allowed|=1u<<bits;
    }
    survivors<<"{\"candidate_cursor\":"<<cursor<<",\"y\":"<<y<<",\"pair_indices\":["<<a<<","<<b<<"],\"quotient_S_ids\":[";
    for(int z=0;z<6;z++)survivors<<(z?",":"")<<S[z];survivors<<"],\"quotient_S_coordinates\":[";
    for(int z=0;z<6;z++)survivors<<(z?",":"")<<"["<<S[z]%64<<","<<S[z]/64<<"]";
    survivors<<"],\"legal_lift_parity_mask\":"<<allowed<<",\"parity_bit_order\":[\"involution_1\",\"involution_y\",\"pair_a\",\"pair_b\"],\"block_and_head_roots_full\":true,\"original_leaf_leaf_checked\":false}\n";
   }
   bfsCPU+=double(clock()-t)/CLOCKS_PER_SEC;
  }
  if(hh==target){done=true;break;}
 }
 double loop=cpu()-setup;
 double raw_overhead=max(0.0,loop-hhCPU-bbCPU-bfsCPU);
 double estimate=setup+TOTAL*(hhCPU+raw_overhead)/max(1LL,raw)+HH_TOTAL*bbCPU/max(1LL,hh);
 if(firstCursor>=0)e.sample(prefix+".first_HH",firstS,firstCursor,firstY,firstA,firstB,false);
 if(bestCursor>=0)e.sample(prefix+".best_BB",bestS,bestCursor,bestY,bestA,bestB,false);
 string status=hh==target?"PROFILE_COMPLETE_STOPPED":next==TOTAL?"COMPLETE_QUOTIENT_RANGE":stopped?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 ofstream f(prefix+".terminal.json");f<<"{\"status\":\""<<status<<"\",\"scope\":\"GF64 C21 quotient frontend only; no C42 lift search\",\"raw_total\":"<<TOTAL<<",\"HH_total_from_scope\":"<<HH_TOTAL<<",\"start_cursor\":"<<first<<",\"next_candidate_cursor\":"<<next<<",\"raw_visited\":"<<raw<<",\"HH_pass\":"<<hh<<",\"HH_skipped\":"<<skipped<<",\"BB_pass\":"<<bbpass<<",\"BH_full_pass\":"<<bhpass<<",\"block_root_zero_among_BB_pass\":"<<blockzero<<",\"head_root_zero_among_BB_pass\":"<<headzero<<",\"minimum_BB_missing\":"<<bestBB<<",\"cpu_seconds\":"<<cpu()<<",\"setup_cpu_seconds\":"<<setup<<",\"loop_cpu_seconds\":"<<loop<<",\"HH_filter_cpu_seconds\":"<<hhCPU<<",\"BB_formula_cpu_seconds\":"<<bbCPU<<",\"conditional_BH_BFS_cpu_seconds\":"<<bfsCPU<<",\"raw_timing_and_loop_overhead_cpu_seconds\":"<<raw_overhead<<",\"estimated_full_HH_BB_cpu_seconds\":"<<estimate<<",\"estimate_excludes_unobserved_BH_or_lift_cost\":true,\"BB_missing_histogram\":{";
 bool comma=false;for(auto[k,v]:hist){f<<(comma?",":"")<<"\""<<k<<"\":"<<v;comma=true;}f<<"},\"BH_survivors_file\":\""<<prefix<<".BH_survivors.jsonl\",\"per_y\":{";
 for(int y=0;y<64;y++){auto&ct=by_y[y];f<<(y?",":"")<<"\""<<y<<"\":{\"raw_visited\":"<<ct.raw<<",\"HH_pass\":"<<ct.hh<<",\"HH_skipped\":"<<ct.raw-ct.hh<<",\"BB_pass\":"<<ct.bb<<",\"BH_full_pass\":"<<ct.bh<<",\"block_root_zero_among_BB_pass\":"<<ct.blockzero<<",\"head_root_zero_among_BB_pass\":"<<ct.headzero<<",\"minimum_BB_missing\":"<<(ct.hh?to_string(ct.minBB):"null")<<",\"raw_total_for_y\":"<<PER_Y<<"}";}
 f<<"},\"next_parameters\":";
 if(next<TOTAL){long long rem=next%PER_Y;int a=0;while(rem>=640-a){rem-=640-a;a++;}f<<"{\"y\":"<<next/PER_Y<<",\"pair_a\":"<<a<<",\"pair_b\":"<<a+rem<<"}";}else f<<"null";
 f<<"}\n";
 cout<<"terminal "<<status<<" raw "<<raw<<" HH "<<hh<<" BB "<<bbpass<<" BH "<<bhpass<<" minBB "<<bestBB<<" next "<<next<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<endl;return 2;}}

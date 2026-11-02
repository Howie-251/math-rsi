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
using Mask=uint64_t;using Labels=array<int,6>;using Masks=array<Mask,7>;
constexpr long long PER=1299LL*1298/2,TOTAL=6*PER,HH_TOTAL=4484088;
const array<array<int,2>,6>FIRST={{{1,0},{1,1},{3,0},{3,1},{7,0},{7,1}}};
volatile sig_atomic_t stopped=0;void stop_signal(int){stopped=1;}
int fm(int a,int b){int c=0;while(b){if(b&1)c^=a;b>>=1;a<<=1;if(a&64)a^=0x43;}return c;}
struct Engine{
 static constexpr int q=64,L=2688,B=448,n=3200;
 array<array<unsigned char,64>,64>mul{};array<int,21>power{};array<int,64>frob{};
 array<array<unsigned char,64>,42>action{};array<array<int,42>,42>kprod{};
 array<Mask,64>hm{},km{};vector<unsigned short>right;
 vector<int>inverse,pairs,queue;vector<Masks>kwh;vector<array<unsigned short,7>>adj;
 vector<unsigned>seen;unsigned stamp=0;
 Engine():right(L*L),inverse(L),queue(n),kwh(L),adj(n),seen(n){
  for(int x=0;x<64;x++)for(int y=0;y<64;y++)mul[x][y]=fm(x,y);
  power[0]=1;for(int a=1;a<21;a++)power[a]=mul[power[a-1]][8];
  for(int x=0;x<64;x++){int z=mul[x][x];z=mul[z][z];frob[x]=mul[z][z];}
  for(int x=0;x<64;x++)if(frob[frob[x]]!=x)throw runtime_error("bad Frobenius");
  for(int k=0;k<42;k++)for(int x=0;x<64;x++){
   action[k][x]=mul[power[k%21]][k<21?x:frob[x]];km[x]|=Mask(1)<<action[k][x];if(k%7==0)hm[x]|=Mask(1)<<action[k][x];
  }
  for(int k=0;k<42;k++)for(int l=0;l<42;l++)kprod[k][l]=(k%21+(k<21?1:8)*(l%21))%21+21*((k/21+l/21)%2);
  for(int s=0;s<L;s++)for(int a=0;a<L;a++)right[s*L+a]=((a%64)^action[a/64][s%64])+64*kprod[a/64][s/64];
  int involutions=0;array<int,3>classes{};
  for(int a=0;a<L;a++){
   int k=a/64,e=k/21,b=(21-((e?8:1)*(k%21))%21)%21,ki=b+21*e;
   inverse[a]=action[ki][a%64]+64*ki;
   if(product(a,inverse[a])||product(inverse[a],a)||product(0,a)!=a||product(a,0)!=a)throw runtime_error("semilinear inverse/identity mismatch");
   if(a&&a==inverse[a])involutions++;
   if(a<inverse[a]){pairs.push_back(a);int orbit=__builtin_popcountll(km[a%64]);classes[orbit==1?0:orbit==21?1:2]++;}
   for(int k=0;k<42;k++)kwh[a][kprod[k][a/64]%7]|=Mask(1)<<action[k][a%64];
  }
  if(involutions!=87||pairs.size()!=1300||classes!=array<int,3>{19,420,861})throw runtime_error("wrong semilinear inverse-pair classification");
  for(int a=0;a<L;a++)adj[a][0]=L+a%64+64*((a/64)%7);
  for(int b=0;b<7;b++)for(int x=0;x<64;x++){
   int u=L+x+64*b;for(int j=0;j<6;j++)adj[u][j]=x+64*(b+7*j);adj[u][6]=L+B+x;
  }
  for(int x=0;x<64;x++)for(int b=0;b<7;b++)adj[L+B+x][b]=L+x+64*b;
 }
 int product(int a,int b)const{return right[b*L+a];}
 bool legal(const Labels&S){set<int>v(S.begin(),S.end());if(v.size()!=6||v.count(0))return false;for(int s:S)if(s<0||s>=L||!v.count(inverse[s])||s==inverse[s])return false;return true;}
 Labels make(int a,int b,int c){return {a,inverse[a],b,inverse[b],c,inverse[c]};}
 bool hh(const Labels&S){Mask z=1;for(int s:S)z|=km[s%64];return z==~Mask(0);}
 Masks bb(const Labels&S){Masks masks{};Mask common=1;for(int s:S)common|=hm[s%64];
  for(int b=0;b<7;b++){masks[b]=common|kwh[0][b];for(int s:S)masks[b]|=kwh[s][b];}
  masks[0]|=hm[0];
  for(int a:S){masks[(a/64)%7]|=hm[a%64];for(int b:S){int ab=product(a,b);masks[(ab/64)%7]|=hm[ab%64];for(int c:S){int abc=product(ab,c);masks[(abc/64)%7]|=hm[abc%64];}}}
  return masks;
 }
 int missing(const Masks&m){int z=B;for(Mask a:m)z-=__builtin_popcountll(a);return z;}
 void build(const Labels&S){for(int j=0;j<6;j++){const unsigned short*t=&right[S[j]*L];for(int a=0;a<L;a++)adj[a][j+1]=t[a];}}
 int bfs(int root){++stamp;int read=0,end=1;queue[0]=root;seen[root]=stamp;
  for(int depth=0;depth<5&&read<end&&end<n;depth++){int boundary=end;while(read<boundary){int a=queue[read++];for(int b:adj[a])if(seen[b]!=stamp){seen[b]=stamp;queue[end++]=b;}}}return n-end;
 }
 array<int,3>roots(){return {bfs(0),bfs(L),bfs(L+B)};}
 Masks bfs_block_masks(){bfs(L);Masks out{};for(int b=0;b<B;b++)if(seen[L+b]==stamp)out[b/64]|=Mask(1)<<(b%64);return out;}
 long long bad(const array<int,3>&a){return (2688LL*a[0]+448LL*a[1]+64LL*a[2])/2;}
 void save(string prefix,const Labels&S,long long cursor,int branch,array<int,2>pair_indices,bool full){
  auto masks=bb(S);ofstream f(prefix+".json");f<<"{\"group\":\"GF64 semidirect (C21 semidirect C2), Frob8\",\"n\":3200,\"degree\":7,\"candidate_cursor\":"<<cursor<<",\"first_branch\":"<<branch<<",\"other_pair_indices_in_1300_table\":["<<pair_indices[0]<<","<<pair_indices[1]<<"],\"S_ids\":[";
  for(int j=0;j<6;j++)f<<(j?",":"")<<S[j];f<<"],\"S_coordinates\":[";for(int j=0;j<6;j++)f<<(j?",":"")<<"["<<S[j]%64<<","<<(S[j]/64)%21<<","<<S[j]/1344<<"]";
  f<<"],\"HH_pass\":"<<(hh(S)?"true":"false")<<",\"BB_missing\":"<<missing(masks)<<",\"BB_masks\":[";for(int b=0;b<7;b++)f<<(b?",":"")<<masks[b];f<<"]";
  if(full){build(S);if(masks!=bfs_block_masks())throw runtime_error("semilinear BB formula/BFS mismatch");auto a=roots();f<<",\"root_missing_leaf_block_head\":["<<a[0]<<","<<a[1]<<","<<a[2]<<"],\"bad_unordered_pairs\":"<<bad(a);
   ofstream edge(prefix+".edges");edge<<n<<" 11200\n";int ne=0;for(int u=0;u<n;u++)for(int v:adj[u])if(u<v){edge<<u<<" "<<v<<"\n";ne++;}if(ne!=11200)throw runtime_error("wrong edge count");
  }f<<"}\n";
 }
};
struct Counts{long long raw=0,invalid=0,hh=0,bb=0,scored=0,hbzero=0;int minBB=449;long long best=numeric_limits<long long>::max();array<int,3>minRoot={3201,3201,3201};array<long long,3>zeroRoot{};};
int main(int argc,char**argv){try{
 clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};Engine e;
 if(argc==6&&string(argv[1])=="check"){
  auto S=e.make(stoi(argv[2]),stoi(argv[3]),stoi(argv[4]));if(!e.legal(S))throw runtime_error("bad preflight generators");e.save(argv[5],S,-1,-1,{-1,-1},true);cout<<"preflight saved cpu "<<cpu()<<endl;return 0;
 }
 if(argc!=5)throw runtime_error("CPU_LIMIT HH_PROFILE_TARGET START_CURSOR PREFIX");double limit=stod(argv[1]);long long target=stoll(argv[2]),first=stoll(argv[3]);string prefix=argv[4];
 signal(SIGINT,stop_signal);signal(SIGTERM,stop_signal);
 ofstream pf(prefix+".inverse_pairs.json");pf<<"[";for(size_t j=0;j<e.pairs.size();j++){int g=e.pairs[j];pf<<(j?",":"")<<"["<<g%64<<","<<(g/64)%21<<","<<g/1344<<"]";}pf<<"]\n";
 array<Counts,6>counts;map<int,long long>bbhist;map<long long,long long>scorehist;
 long long cursor=0,next=first,hh=0,bb=0,raw=0,invalid=0;int minBB=449;long long best=numeric_limits<long long>::max();
 Labels minS{},bestS{};int minBranch=-1,bestBranch=-1;array<int,2>minIndices{},bestIndices{};long long minCursor=-1,bestCursor=-1;
 double hhCPU=0,bbCPU=0,bfsCPU=0;bool done=false,found=false;double setup=cpu();
 for(int branch=0;branch<6&&!done;branch++){
  int a=1+64*(FIRST[branch][0]+21*FIRST[branch][1]),fixed=min(a,e.inverse[a]);vector<int>indices;
  for(int j=0;j<1300;j++)if(e.pairs[j]!=fixed)indices.push_back(j);if(indices.size()!=1299)throw runtime_error("fixed first pair absent");
  for(int j=0;j<1299&&!done;j++)for(int k=j+1;k<1299;k++,cursor++){
   if(cursor<first)continue;if(stopped||cpu()>=limit){done=true;break;}
   auto S=e.make(a,e.pairs[indices[j]],e.pairs[indices[k]]);auto&ct=counts[branch];ct.raw++;raw++;next=cursor+1;
   if(!e.legal(S)){ct.invalid++;invalid++;continue;}
   clock_t t=clock();bool hp=e.hh(S);hhCPU+=double(clock()-t)/CLOCKS_PER_SEC;if(!hp)continue;hh++;ct.hh++;
   t=clock();auto masks=e.bb(S);int miss=e.missing(masks);bbCPU+=double(clock()-t)/CLOCKS_PER_SEC;bbhist[miss]++;ct.minBB=min(ct.minBB,miss);
   if(miss<minBB){minBB=miss;minS=S;minBranch=branch;minIndices={indices[j],indices[k]};minCursor=cursor;}
   if(miss==0){bb++;ct.bb++;t=clock();e.build(S);auto m=e.roots();auto bad=e.bad(m);ct.scored++;scorehist[bad]++;ct.best=min(ct.best,bad);
    for(int z=0;z<3;z++){ct.minRoot[z]=min(ct.minRoot[z],m[z]);ct.zeroRoot[z]+=(m[z]==0);}ct.hbzero+=(m[1]==0&&m[2]==0);
    if(bad<best){best=bad;bestS=S;bestBranch=branch;bestIndices={indices[j],indices[k]};bestCursor=cursor;}
    bfsCPU+=double(clock()-t)/CLOCKS_PER_SEC;
    if(!bad){found=true;done=true;break;}
   }
   if(hh==target){done=true;break;}
  }
 }
 double loop=cpu()-setup,rawOverhead=max(0.0,loop-hhCPU-bbCPU-bfsCPU);
 double frontEstimate=setup+TOTAL*(hhCPU+rawOverhead)/max(1LL,raw)+HH_TOTAL*bbCPU/max(1LL,hh);
 if(minCursor>=0)e.save(prefix+".best_BB",minS,minCursor,minBranch,minIndices,false);
 if(bestCursor>=0)e.save(prefix+".best",bestS,bestCursor,bestBranch,bestIndices,true);
 string status=found?"CANDIDATE_D5":hh==target?"PROFILE_COMPLETE_STOPPED":next==TOTAL?"COMPLETE_NO_SOLUTION":stopped?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 ofstream f(prefix+".terminal.json");f<<"{\"status\":\""<<status<<"\",\"scope\":\"semilinear GF64 K=C21 semidirect C2 three inverse pairs only\",\"raw_total\":"<<TOTAL<<",\"HH_total_from_scope\":"<<HH_TOTAL<<",\"start_cursor\":"<<first<<",\"next_candidate_cursor\":"<<next<<",\"raw_visited\":"<<raw<<",\"invalid\":"<<invalid<<",\"HH_pass\":"<<hh<<",\"HH_skipped\":"<<raw-invalid-hh<<",\"BB_pass\":"<<bb<<",\"three_root_BFS_scored\":"<<bb<<",\"minimum_BB_missing\":"<<minBB<<",\"best_bad_pairs\":"<<(bestCursor>=0?to_string(best):"null")<<",\"setup_cpu_seconds\":"<<setup<<",\"loop_cpu_seconds\":"<<loop<<",\"HH_filter_cpu_seconds\":"<<hhCPU<<",\"BB_formula_cpu_seconds\":"<<bbCPU<<",\"conditional_three_root_BFS_cpu_seconds\":"<<bfsCPU<<",\"raw_timing_and_loop_overhead_cpu_seconds\":"<<rawOverhead<<",\"estimated_full_HH_BB_cpu_seconds\":"<<frontEstimate<<",\"estimated_full_BFS_cpu_using_prefix_rate\":"<<HH_TOTAL*bfsCPU/max(1LL,hh)<<",\"cpu_seconds\":"<<cpu()<<",\"per_first_branch\":[";
 for(int b=0;b<6;b++){auto&ct=counts[b];f<<(b?",":"")<<"{\"first_a\":"<<FIRST[b][0]<<",\"first_e\":"<<FIRST[b][1]<<",\"raw_visited\":"<<ct.raw<<",\"invalid\":"<<ct.invalid<<",\"HH_pass\":"<<ct.hh<<",\"HH_skipped\":"<<ct.raw-ct.invalid-ct.hh<<",\"BB_pass\":"<<ct.bb<<",\"three_root_BFS_scored\":"<<ct.scored<<",\"minimum_BB_missing\":"<<(ct.hh?to_string(ct.minBB):"null")<<",\"best_bad_pairs\":"<<(ct.scored?to_string(ct.best):"null")<<",\"minimum_root_missing\":[";
  for(int z=0;z<3;z++)f<<(z?",":"")<<(ct.scored?to_string(ct.minRoot[z]):"null");f<<"],\"root_zero_counts\":[";for(int z=0;z<3;z++)f<<(z?",":"")<<ct.zeroRoot[z];f<<"],\"head_block_zero\":"<<ct.hbzero<<"}";
 }f<<"],\"BB_missing_histogram\":{";bool comma=false;for(auto[k,v]:bbhist){f<<(comma?",":"")<<"\""<<k<<"\":"<<v;comma=true;}f<<"},\"score_histogram\":{";comma=false;for(auto[k,v]:scorehist){f<<(comma?",":"")<<"\""<<k<<"\":"<<v;comma=true;}f<<"},\"next_parameters\":";
 if(next<TOTAL){long long rem=next%PER;int j=0;while(rem>=1298-j){rem-=1298-j;j++;}f<<"{\"first_branch\":"<<next/PER<<",\"other_pair_list_index_j\":"<<j<<",\"other_pair_list_index_k\":"<<j+1+rem<<"}";}else f<<"null";
 f<<"}\n";cout<<"terminal "<<status<<" raw "<<raw<<" HH "<<hh<<" BB "<<bb<<" minBB "<<minBB<<" next "<<next<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<endl;return 2;}}

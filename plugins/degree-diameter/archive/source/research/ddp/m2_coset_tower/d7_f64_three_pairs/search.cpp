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
using U=unsigned short;
using Labels=array<int,6>;
const array<int,6>first_exponents={1,2,3,6,7,14};
volatile sig_atomic_t stopped=0;
void stop_signal(int){stopped=1;}
int field_mul(int a,int b){int c=0;while(b){if(b&1)c^=a;b>>=1;a<<=1;if(a&64)a^=0x43;}return c;}

struct Engine{
 static constexpr int q=64,d=7,m=42,L=2688,n=3200;
 array<array<unsigned char,64>,64>mul{};array<int,42>power{};
 array<int,64>orbit{};array<uint64_t,64>orbit_mask{};
 vector<int>inv;vector<U>right,queue;vector<array<U,7>>adj;vector<unsigned>seen;unsigned stamp=0;
 Engine():inv(L),right(L*L),queue(n),adj(n),seen(n){
  for(int a=0;a<64;a++)for(int b=0;b<64;b++)mul[a][b]=field_mul(a,b);
  orbit.fill(-1);set<int>primitive;int g=1;
  for(int k=0;k<63;k++){if(!primitive.insert(g).second)throw runtime_error("g not primitive");orbit[g]=k%3;g=mul[g][2];}
  if(g!=1||primitive.size()!=63)throw runtime_error("bad GF64 representation");
  power[0]=1;for(int k=1;k<42;k++)power[k]=mul[power[k-1]][8];
  if(set<int>(power.begin(),power.end()).size()!=21||power[21]!=1||mul[power[41]][8]!=1)throw runtime_error("bad action");
  for(int x=0;x<64;x++)for(int a:power)orbit_mask[x]|=uint64_t(1)<<mul[a][x];
  for(int s=0;s<L;s++)for(int a=0;a<L;a++)right[s*L+a]=(a%64)^mul[power[a/64]][s%64];
  for(int s=0;s<L;s++)for(int a=0;a<L;a++)right[s*L+a]+=64*((a/64+s/64)%42);
  for(int a=0;a<L;a++){int j=(42-a/64)%42;inv[a]=mul[power[j]][a%64]+64*j;}
  for(int a=0;a<L;a++)if(right[inv[a]*L+a]!=0||right[a*L+inv[a]]!=0||right[a]!=a||right[a*L]!=a)throw runtime_error("group inverse/identity mismatch");
  for(int i=0;i<42;i++)for(int x=0;x<64;x++)adj[x+64*i][0]=L+x+64*(i%7);
  for(int b=0;b<7;b++)for(int x=0;x<64;x++){int v=L+x+64*b;for(int k=0;k<6;k++)adj[v][k]=x+64*(b+7*k);adj[v][6]=3136+x;}
  for(int x=0;x<64;x++)for(int b=0;b<7;b++)adj[3136+x][b]=L+x+64*b;
 }
 bool legal(const Labels&S){for(int j=0;j<6;j++){
  if(S[j]<=0||S[j]>=L)return false;bool paired=false;
  for(int k=0;k<6;k++){if(j!=k&&S[j]==S[k])return false;if(S[k]==inv[S[j]])paired=true;}
  if(!paired)return false;
 }return true;}
 bool head_head(const Labels&S){uint64_t reached=1;for(int s:S)reached|=orbit_mask[s%64];return reached==~uint64_t(0);}
 void build(const Labels&S){for(int j=0;j<6;j++){const U*t=&right[S[j]*L];for(int a=0;a<L;a++)adj[a][j+1]=t[a];}}
 array<int,3>missing(){array<int,3>answer{};array<int,3>roots={0,L,3136};
  for(int k=0;k<3;k++){++stamp;int head=0,end=1;queue[0]=roots[k];seen[roots[k]]=stamp;
   for(int depth=0;depth<5&&head<end&&end<n;depth++){int boundary=end;while(head<boundary){int u=queue[head++];for(U v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}}}
   answer[k]=n-end;
  }return answer;
 }
 long long bad(const array<int,3>&a){return (2688LL*a[0]+448LL*a[1]+64LL*a[2])/2;}
 void save_json(string path,const Labels&S,const array<int,3>&a,int first_i,array<int,2>indices,long long cursor,double cpu){
  ofstream f(path);f<<"{\"degree\":7,\"field\":\"GF64/F2[t]/(t^6+t+1)\",\"primitive_g\":2,\"r\":8,\"m\":42,\"n\":3200,\"first_quotient\":"<<first_i<<",\"other_pair_indices\":["<<indices[0]<<","<<indices[1]<<"],\"candidate_cursor\":"<<cursor<<",\"S_ids\":[";
  for(int j=0;j<6;j++)f<<(j?",":"")<<S[j];f<<"],\"S_coordinates\":[";
  for(int j=0;j<6;j++)f<<(j?",":"")<<"["<<S[j]%64<<","<<S[j]/64<<"]";
  f<<"],\"root_orbit_sizes\":[2688,448,64],\"root_missing_leaf_block_head\":["<<a[0]<<","<<a[1]<<","<<a[2]<<"],\"bad_unordered_pairs\":"<<bad(a)<<",\"cpu_seconds\":"<<cpu<<"}\n";
 }
 void save(string prefix,const Labels&S,const array<int,3>&a,int first_i,array<int,2>indices,long long cursor,double cpu){
  vector<pair<int,int>>edges;for(int u=0;u<n;u++)for(int v:adj[u])if(u<v)edges.emplace_back(u,v);sort(edges.begin(),edges.end());
  if(edges.size()!=11200||adjacent_find(edges.begin(),edges.end())!=edges.end())throw runtime_error("invalid complete edge list");
  ofstream e(prefix+".edges");e<<n<<" "<<edges.size()<<"\n";for(auto[u,v]:edges)e<<u<<" "<<v<<"\n";
  save_json(prefix+".json",S,a,first_i,indices,cursor,cpu);
 }
};
struct Counts{
 long long raw=0,invalid=0,skippedHH=0,scored=0,best=numeric_limits<long long>::max(),headBlockZero=0,firstHeadCursor=-1;
 array<int,3>rootMin={3201,3201,3201};array<long long,3>rootZero{};map<long long,long long>hist;
};
void write_counts(ostream&o,const Counts&c){
 o<<"{\"raw_slots_visited\":"<<c.raw<<",\"invalid\":"<<c.invalid<<",\"skipped_HH\":"<<c.skippedHH<<",\"fully_scored\":"<<c.scored<<",\"best_bad_pairs\":"<<(c.scored?to_string(c.best):"null")<<",\"root_minimum_missing\":[";
 for(int j=0;j<3;j++)o<<(j?",":"")<<(c.scored?to_string(c.rootMin[j]):"null");o<<"],\"root_zero_counts\":[";
 for(int j=0;j<3;j++)o<<(j?",":"")<<c.rootZero[j];o<<"],\"head_and_block_zero_count\":"<<c.headBlockZero<<",\"first_head_zero_cursor\":"<<(c.firstHeadCursor<0?"null":to_string(c.firstHeadCursor))<<",\"score_histogram\":{";
 bool comma=false;for(auto[s,n]:c.hist){o<<(comma?",":"")<<"\""<<s<<"\":"<<n;comma=true;}o<<"}}";
}
int main(int argc,char**argv){try{
 if(argc>=2&&string(argv[1])=="check"){
  if(argc!=9)throw runtime_error("check S0 S1 S2 S3 S4 S5 PREFIX");Engine e;Labels S;for(int j=0;j<6;j++)S[j]=stoi(argv[j+2]);if(!e.legal(S)||!e.head_head(S))throw runtime_error("invalid sample S");e.build(S);auto a=e.missing();e.save(argv[8],S,a,-1,{-1,-1},-1,0);cout<<"bad "<<e.bad(a)<<" roots "<<a[0]<<" "<<a[1]<<" "<<a[2]<<"\n";return 0;
 }
 if(argc!=4)throw runtime_error("CPU_LIMIT PROFILE_COUNT PREFIX");double limit=stod(argv[1]);long long profile_count=stoll(argv[2]);string prefix=argv[3];clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 signal(SIGINT,stop_signal);signal(SIGTERM,stop_signal);Engine e;array<vector<int>,3>pairs;int zero_pairs=0;
 for(int g=1;g<Engine::L;g++)if(g<e.inv[g]){int c=e.orbit[g%64];if(c<0)zero_pairs++;else pairs[c].push_back(g);}
 if(zero_pairs!=20||pairs[0].size()!=420||pairs[1].size()!=420||pairs[2].size()!=420)throw runtime_error("wrong pair classes");
 ofstream pf(prefix+".inverse_pair_classes.json");pf<<"{";for(int k=0;k<3;k++){pf<<(k?",":"")<<"\""<<k<<"\":[";for(int j=0;j<420;j++)pf<<(j?",":"")<<"["<<pairs[k][j]%64<<","<<pairs[k][j]/64<<"]";pf<<"]";}pf<<"}\n";pf.close();
 constexpr long long per=420LL*420,total=6*per;array<Counts,6>counts;
 long long best=numeric_limits<long long>::max(),next=0,scored_total=0;bool found=false,profile_done=false,projected_over=false,first_head_saved=false;
 double setup_cpu=cpu();cout<<"setup cpu "<<setup_cpu<<" total_slots "<<total<<endl;
 for(long long cursor=0;cursor<total;cursor++){
  if(stopped||((cursor&255)==0&&cpu()>=limit))break;
  int branch=cursor/per,j=(cursor%per)/420,k=cursor%420,exponent=first_exponents[branch];
  int a=1+64*exponent,b=pairs[1][j],c=pairs[2][k];Labels S={a,e.inv[a],b,e.inv[b],c,e.inv[c]};auto&ct=counts[branch];ct.raw++;next=cursor+1;
  if(!e.legal(S))ct.invalid++;
  else if(!e.head_head(S))ct.skippedHH++;
  else{e.build(S);auto miss=e.missing();auto bad=e.bad(miss);ct.scored++;scored_total++;ct.hist[bad]++;
   for(int z=0;z<3;z++){ct.rootMin[z]=min(ct.rootMin[z],miss[z]);if(miss[z]==0)ct.rootZero[z]++;}
   if(miss[2]==0&&miss[1]==0)ct.headBlockZero++;
   string branch_prefix=prefix+".i"+to_string(exponent);
   if(miss[2]==0&&ct.firstHeadCursor<0){ct.firstHeadCursor=cursor;e.save_json(branch_prefix+".first_head_zero.json",S,miss,exponent,{j,k},cursor,cpu());}
   if(miss[2]==0&&!first_head_saved){first_head_saved=true;e.save_json(prefix+".first_head_zero.json",S,miss,exponent,{j,k},cursor,cpu());}
   if(bad<ct.best){ct.best=bad;e.save(branch_prefix+".best",S,miss,exponent,{j,k},cursor,cpu());}
   if(bad<best){best=bad;e.save(prefix+".best",S,miss,exponent,{j,k},cursor,cpu());cout<<"best "<<bad<<" i "<<exponent<<" cursor "<<cursor<<" roots "<<miss[0]<<" "<<miss[1]<<" "<<miss[2]<<" cpu "<<cpu()<<endl;}
   if(bad==0){found=true;break;}
  }
  if(!profile_done&&next>=profile_count){
   double used=cpu(),loop=used-setup_cpu,estimate=used+(total-next)*loop/max(1LL,scored_total);
   ofstream p(prefix+".profile.json");p<<"{\"raw_slots\":"<<next<<",\"fully_scored\":"<<scored_total<<",\"setup_cpu_seconds\":"<<setup_cpu<<",\"loop_cpu_seconds\":"<<loop<<",\"cpu_seconds\":"<<used<<",\"estimated_total_cpu_seconds\":"<<estimate<<",\"cpu_limit\":"<<limit<<",\"continue_with_same_process\":"<<(estimate<limit?"true":"false")<<"}\n";
   cout<<"profile slots "<<next<<" scored "<<scored_total<<" cpu "<<used<<" estimated_total "<<estimate<<" limit "<<limit<<endl;profile_done=true;
   if(estimate>=limit){projected_over=true;break;}
  }
  if(next%per==0)cout<<"branch_complete i "<<exponent<<" cursor "<<next<<" cpu "<<cpu()<<endl;
 }
 string status=found?"CANDIDATE_D5":next==total?"COMPLETE_NO_SOLUTION":projected_over?"PROFILE_ESTIMATE_EXCEEDS_BUDGET":stopped?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 ofstream out(prefix+".terminal.json");out<<"{\"status\":\""<<status<<"\",\"raw_slots_total\":"<<total<<",\"next_candidate_cursor\":"<<next<<",\"cpu_seconds\":"<<cpu()<<",\"best_bad_pairs\":"<<(scored_total?to_string(best):"null")<<",\"counts\":{";
 for(int z=0;z<6;z++){out<<(z?",":"")<<"\"i"<<first_exponents[z]<<"\":";write_counts(out,counts[z]);}out<<"},\"next_parameters\":";
 if(next<total)out<<"{\"first_i\":"<<first_exponents[next/per]<<",\"pair_B_index\":"<<(next%per)/420<<",\"pair_C_index\":"<<next%420<<"}";else out<<"null";
 out<<"}\n";cout<<"terminal "<<status<<" cursor "<<next<<" best "<<best<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<"\n";return 2;}}

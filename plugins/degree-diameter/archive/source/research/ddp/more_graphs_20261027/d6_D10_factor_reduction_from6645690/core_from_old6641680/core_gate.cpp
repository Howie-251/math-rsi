#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
#include <time.h>
using namespace std;
constexpr int P=1361,M=80,N=P*M;
int mod(long long x,int m){int r=x%m;return r<0?r+m:r;}
int power(int a,int k,int m){int r=1;for(;k;k>>=1,a=(long long)a*a%m)if(k&1)r=(long long)r*a%m;return r;}
double cpu(){timespec t;clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&t);return t.tv_sec+t.tv_nsec*1e-9;}
void write(const string&p,const string&t){ofstream f(p);f<<t<<'\n';assert(f.good());}
void write_counts(const string&p,const vector<uint64_t>&v){ofstream f(p,ios::binary);for(uint64_t x:v){unsigned char b[8];for(int k=0;k<8;k++)b[k]=(x>>(8*k))&255;f.write((char*)b,8);}assert(f.good());}
string arrayjson(const vector<uint64_t>&v){ostringstream o;o<<'[';for(size_t i=0;i<v.size();i++){if(i)o<<',';o<<v[i];}return o.str()+']';}
struct Dart{int n,j,inv;};
int main(int argc,char**argv){assert(argc==2);string out=argv[1];double total0=cpu();
 assert(4400%P==317&&83021%P==0&&83021*80==6641680);array<int,80>pw{};pw[0]=1;for(int j=1;j<80;j++)pw[j]=pw[j-1]*317%P;assert(pw[79]*317%P==1);
 array<Dart,7>d;d[0]={824,38,3};d[1]={625,3,4};d[2]={1089,58,5};for(int i=0;i<3;i++){int j=(80-d[i].j)%80;d[i+3]={mod(-d[i].n*pw[j],P),j,i};}d[6]={1109,40,6};
 array<int,3>original_inverse{41887,82429,9117};for(int i=0;i<3;i++)assert(d[i+3].n==original_inverse[i]%P);assert(74603%P==d[6].n);
 for(int i=0;i<7;i++){auto a=d[i],b=d[a.inv];assert((a.j+b.j)%80==0&&(a.n+pw[a.j]*b.n)%P==0);}
 vector<array<int,7>>adj(N);for(int u=0;u<N;u++){int j=u/P,n=u-j*P;for(int k=0;k<7;k++){int nn=n+pw[j]*d[k].n%P;if(nn>=P)nn-=P;adj[u][k]=((j+d[k].j)%80)*P+nn;}}
 vector<string> results;bool allpass=true;
 for(int rule=0;rule<2;rule++){
  int L=rule==0?6:7,D=rule==0?10:9;string name=rule==0?"degree6_D10_remove_h":"degree7_D9_keep_h";double start=cpu();write(out+"/checkpoint.json","{\"status\":\"RUNNING_CORE_BFS\",\"rule\":"+to_string(rule)+",\"completed_rules\":"+to_string(rule)+"}");
  vector<int>dist(N,-1),queue(N);int head=0,tail=1;queue[0]=0;dist[0]=0;int ecc=0;
  while(head<tail){int u=queue[head++];for(int k=0;k<L;k++){int v=adj[u][k];if(dist[v]<0){dist[v]=dist[u]+1;if(dist[v]>ecc)ecc=dist[v];queue[tail++]=v;}}}
  int missing=0,firstmissing=-1;vector<uint64_t>bh(ecc+1);for(int u=0;u<N;u++){if(dist[u]>=0)++bh[dist[u]];if(dist[u]<0||dist[u]>D){++missing;if(firstmissing<0)firstmissing=u;}}
  write(out+"/checkpoint.json","{\"status\":\"RUNNING_RAW_DP\",\"rule\":"+to_string(rule)+",\"completed_rules\":"+to_string(rule)+",\"core_radius_missing\":"+to_string(missing)+"}");
  vector<uint64_t>raw(N,0),dp((size_t)N*L,0),next((size_t)N*L,0),depth{1};raw[0]=1;
  for(int k=0;k<L;k++)++dp[(size_t)adj[0][k]*L+k];uint64_t expected=L;
  for(int length=1;length<=D;length++){
   uint64_t level=0;for(int u=0;u<N;u++){uint64_t s=0;for(int last=0;last<L;last++)s+=dp[(size_t)u*L+last];raw[u]+=s;level+=s;}assert(level==expected);depth.push_back(level);
   if(length==D)break;fill(next.begin(),next.end(),0);
   for(int u=0;u<N;u++){uint64_t total=0;for(int last=0;last<L;last++)total+=dp[(size_t)u*L+last];if(!total)continue;for(int k=0;k<L;k++){uint64_t ways=total-dp[(size_t)u*L+d[k].inv];next[(size_t)adj[u][k]*L+k]+=ways;}}
   dp.swap(next);expected*=L-1;
  }
  uint64_t mn=raw[0],mx=0,sum=0;int first=0,below=0;map<uint64_t,int>hist;
  for(int u=0;u<N;u++){if(raw[u]<mn){mn=raw[u];first=u;}if(raw[u]>mx)mx=raw[u];sum+=raw[u];++hist[raw[u]];below+=raw[u]<13;assert((raw[u]>0)==(dist[u]>=0&&dist[u]<=D));}
  assert(sum==(rule==0?14648437ULL:14108774ULL));write_counts(out+"/"+name+"_rawcounts.u64le.bin",raw);bool pass=missing==0&&mn>=13;allpass&=pass;
  ostringstream o;o<<"{\"rule\":\""<<name<<"\",\"degree_labels\":"<<L<<",\"target_radius\":"<<D<<",\"core_states\":"<<N<<",\"core_BFS_reached\":"<<tail<<",\"core_connected\":"<<(tail==N?"true":"false")<<",\"core_exact_D\":";if(tail==N)o<<ecc;else o<<"null";o<<",\"core_BFS_histogram\":"<<arrayjson(bh)<<",\"core_radius_missing\":"<<missing<<",\"first_core_radius_missing_id\":"<<firstmissing<<",\"minimum_raw_count\":"<<mn<<",\"maximum_raw_count\":"<<mx<<",\"first_minimum_slot\":"<<first<<",\"first_minimum_phase\":"<<first/P<<",\"first_minimum_normal1361\":"<<first%P<<",\"slots_below13\":"<<below<<",\"raw_prefix_count\":"<<sum<<",\"counts_by_word_length\":"<<arrayjson(depth)<<",\"raw_count_histogram\":{";bool comma=false;for(auto [count,n]:hist){if(comma)o<<',';comma=true;o<<'\"'<<count<<"\":"<<n;}o<<"},\"raw_counts_file\":\""<<name<<"_rawcounts.u64le.bin\",\"gate_passes\":"<<(pass?"true":"false")<<",\"CPU_seconds\":"<<cpu()-start<<",\"source_BFS\":0,\"target_BFS\":0,\"target_graphs\":0}";
  results.push_back(o.str());write(out+"/"+name+".json",o.str());write(out+"/checkpoint.json","{\"status\":\"RULE_COMPLETED\",\"completed_rules\":"+to_string(rule+1)+"}");cout<<name<<" min "<<mn<<" missing "<<missing<<" coreD "<<ecc<<endl;
 }
 ostringstream r;r<<"{\"status\":\""<<(allpass?"BOTH_NECESSARY_GATES_PASS":"NECESSARY_OBSTRUCTION_FOUND")<<"\",\"old_seed_order\":6641680,\"current6645690_source_bound\":false,\"core_order\":"<<N<<",\"target_small_factor\":13,\"hypothetical_target_order\":1415440,\"rules\":["<<results[0]<<','<<results[1]<<"],\"native_CPU_seconds\":"<<cpu()-total0<<",\"source_BFS\":0,\"core_BFS_runs\":2,\"target_BFS\":0,\"target_graphs\":0,\"target_settings_tested\":0,\"actual_target_D\":null}";write(out+"/NATIVE_RESULT.json",r.str());write(out+"/checkpoint.json","{\"status\":\"COMPLETE\",\"completed_rules\":2}");cout<<"complete "<<cpu()-total0<<endl;
}

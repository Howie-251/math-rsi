#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
int mod(long long a,int m){a%=m;return a<0?a+m:a;}
int pw(int a,int e,int m){int r=1;while(e){if(e&1)r=1LL*r*a%m;a=1LL*a*a%m;e>>=1;}return r;}
int crt(int a,int b,int q){for(int x=mod(a,21);x<21*q;x+=21)if(x%q==mod(b,q))return x;assert(false);return -1;}
struct Gen{int s,v;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();rlimit lim{10,10};setrlimit(RLIMIT_CPU,&lim);
 array<int,7>ids={3082,5577,17883,29904,40986,53484,55264};vector<Gen>source;for(int id:ids)source.push_back({id/2373,id%2373});
 assert(pw(44,24,2373)==1&&44%21==2&&pw(44%113,4,113)==112);
 for(auto g:source){Gen inverse{mod(-g.s,24),mod(-1LL*g.v*pw(44,mod(-g.s,24),2373),2373)};assert(find(ids.begin(),ids.end(),inverse.s*2373+inverse.v)!=ids.end());}
 array<Gen,3>positive={Gen{1,709},Gen{2,831},Gen{7,1272}};
 array<int,3>centered={-3,-21,-37};int shift=crt(0,36,113);assert(shift%21==0);
 for(int k=0;k<3;k++){auto g=positive[k];int y=mod(g.v+1LL*(pw(44,g.s,2373)-1)*shift,2373);assert(y%113==mod(centered[k],113)&&y%21==g.v%21);}
 assert(mod(1428+1LL*(pw(44,12,2373)-1)*shift,2373)==0);
 constexpr int q=137,M=21*q,N=24*M,A=695;assert(A==crt(2,10,q)&&pw(A,24,M)==1&&pw(10,4,q)==q-1);
 for(int t=1;t<10;t++)assert(pw(t,4,q)!=q-1);
 for(int n=114;n<q;n++)if(n%8==1){bool prime=true;for(int d=2;d*d<=n;d++)if(n%d==0)prime=false;assert(!prime);}
 array<Gen,7>gens;array<int,7>inv={3,4,5,0,1,2,6};array<int,3>expected={2326,390,1881};
 for(int k=0;k<3;k++){gens[k]={positive[k].s,crt(positive[k].v%21,centered[k],q)};assert(gens[k].v==expected[k]);gens[k+3]={mod(-gens[k].s,24),mod(-1LL*gens[k].v*pw(A,mod(-gens[k].s,24),M),M)};}
 gens[6]={12,0};array<int,7>factors,factors21;for(int k=0;k<7;k++){factors[k]=pw(A,gens[k].s,M);factors21[k]=pw(2,gens[k].s,21);}for(int k=0;k<7;k++){assert(mod(gens[k].s+gens[inv[k]].s,24)==0&&mod(1LL*gens[k].v*factors[inv[k]]+gens[inv[k]].v,M)==0);}
 ofstream recipe(dir+"/RECIPE.json");recipe<<"{\"law\":\"(i,y)*(j,v)=(i+jmod24,y*a^j+vmodM)\",\"source_n\":56952,\"source_M\":2373,\"source_action\":44,\"source_conjugating_shift\":"<<shift<<",\"source_centered_field113\":[-3,-21,-37],\"target_q\":137,\"target_M\":2877,\"target_action\":695,\"n\":69048,\"m\":241668,\"gens\":[";
 for(int k=0;k<7;k++){if(k)recipe<<',';recipe<<"{\"phase\":"<<gens[k].s<<",\"translation\":"<<gens[k].v<<",\"inverse_index\":"<<inv[k]<<'}';}recipe<<"],\"encoding\":\"2877*phase+translation\",\"source_BFS\":0}\n";recipe.close();
 array<int,504>count{};long long words=0;
 function<void(int,int,int,int)>dfs=[&](int i,int y,int last,int depth){
  count[21*i+y]++;words++;if(depth==7)return;
  for(int k=0;k<7;k++)if(last<0||k!=inv[last])dfs((i+gens[k].s)%24,(y*factors21[k]+gens[k].v%21)%21,k,depth+1);
 };
 dfs(0,0,-1,0);assert(words==391910);int minraw=*min_element(count.begin(),count.end());int firstmin=find(count.begin(),count.end(),minraw)-count.begin();
 ofstream cap(dir+"/CAPACITY.json");cap<<"{\"quotient_n\":504,\"NB_words_length0to7\":"<<words<<",\"minimum_raw_count\":"<<minraw<<",\"first_minimum_slot\":"<<firstmin<<",\"required_fiber_size\":137,\"passes\":"<<(minraw>=137?"true":"false")<<",\"counts\":[";for(int i=0;i<504;i++){if(i)cap<<',';cap<<count[i];}cap<<"]}\n";cap.close();
 if(minraw<137){ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\"QUOTIENT_RAW_CAPACITY_REJECTS_Q137_NO_GRAPH\",\"actual_graphs\":0,\"n_hypothetical\":69048,\"actual_D\":null,\"minimum_raw_count\":"<<minraw<<",\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}
 auto step=[&](int u,int k){int i=u/M,y=u%M;return M*((i+gens[k].s)%24)+mod(1LL*y*factors[k]+gens[k].v,M);};
 for(int u=0;u<N;u++){array<int,7>row;for(int k=0;k<7;k++){row[k]=step(u,k);assert(row[k]!=u&&step(row[k],inv[k])==u);}sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());}
 vector<int>dist(N,-1),queue(N);int lo=0,hi=1;queue[0]=0;dist[0]=0;int ecc=0;
 while(lo<hi){if((lo&4095)==0&&double(clock()-start)/CLOCKS_PER_SEC>9.8){ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\"UNKNOWN_CPU_LIMIT\",\"actual_graphs\":1,\"actual_D\":null}\n";return 0;}int u=queue[lo++];for(int k=0;k<7;k++){int v=step(u,k);if(dist[v]<0){dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);queue[hi++]=v;}}}
 bool connected=hi==N,hit=connected&&ecc<=7;vector<int>hist(ecc+1);int miss=0,first=-1;array<int,24>byphase{};
 ofstream missing(dir+"/R7_MISSING.json");missing<<"{\"root\":0,\"missing_vertex_ids\":[";bool comma=false;for(int v=0;v<N;v++){if(dist[v]>=0)hist[dist[v]]++;if(dist[v]<0||dist[v]>7){if(comma)missing<<',';comma=true;missing<<v;miss++;if(first<0)first=v;byphase[v/M]++;}}missing<<"]}\n";missing.close();
 ofstream distances(dir+"/identity_distances.u8.bin",ios::binary);for(int d:dist){unsigned char c=d<0?255:d;distances.write((char*)&c,1);}distances.close();
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"COMPLETE_D7_REQUIRES_PARENT_CHECK":connected?"SOLE_Q137_CAYLEY_CONTROL_FAILS_D7":"SOLE_Q137_CONTROL_DISCONNECTED")<<"\",\"actual_graphs\":1,\"n\":69048,\"m\":241668,\"Delta\":7,\"regular\":true,\"simple\":true,\"undirected\":true,\"connected\":"<<(connected?"true":"false")<<",\"reached\":"<<hi<<",\"actual_D\":";if(connected)out<<ecc;else out<<"null";out<<",\"diameter_scope\":\"OnefullidentityBFSandCayleyvertextransitivity\",\"root_R7_missing\":"<<miss<<",\"first_R7_missing\":";if(first<0)out<<"null";else out<<first;out<<",\"distance_histogram\":[";for(int i=0;i<=ecc;i++){if(i)out<<',';out<<hist[i];}out<<"],\"R7_missing_by_phase\":[";for(int i=0;i<24;i++){if(i)out<<',';out<<byphase[i];}out<<"],\"ordinary_bad_unordered_pairs\":null,\"source_q113_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 if(hit){ofstream edges(dir+"/graph_d7_D7_n69048.edges");edges<<N<<" 241668\n";int m=0;for(int u=0;u<N;u++)for(int k=0;k<7;k++){int v=step(u,k);if(u<v){edges<<u<<' '<<v<<'\n';m++;}}assert(m==241668);}
 cout<<"minraw="<<minraw<<" connected="<<connected<<" exactD="<<(connected?ecc:-1)<<" R7missing="<<miss<<" hit="<<hit<<" nativeCPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

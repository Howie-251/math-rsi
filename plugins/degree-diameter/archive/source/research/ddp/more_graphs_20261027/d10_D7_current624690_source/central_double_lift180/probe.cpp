#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
constexpr int Q=6941,H=180,N=Q*H;
int mod(long long a,int m){a%=m;return a<0?a+m:a;}
int pw(int a,int n,int m){int r=1;while(n){if(n&1)r=1LL*r*a%m;a=1LL*a*a%m;n>>=1;}return r;}
struct Gen{int v,j;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();rlimit lim{10,10};setrlimit(RLIMIT_CPU,&lim);
 auto expired=[&](){return double(clock()-start)/CLOCKS_PER_SEC>9.8;};
 assert(pw(316,90,Q)==1&&pw(316,45,Q)!=1&&pw(316,30,Q)!=1&&pw(316,18,Q)!=1);
 array<Gen,10>g;array<Gen,5>positive={Gen{35,35},Gen{509,5},Gen{4285,37},Gen{6911,49},Gen{3639,34}};
 array<int,10>inv={5,6,7,8,9,0,1,2,3,4};array<int,5>oldinverse={1058,4535,5926,4266,4593};
 for(int k=0;k<5;k++){g[k]=positive[k];g[k+5]={mod(-1LL*g[k].v*pw(316,180-g[k].j,Q),Q),180-g[k].j};assert(g[k+5].v==oldinverse[k]&&g[k+5].j==(90-g[k].j)+90);}
 array<int,H>powers;powers[0]=1;for(int i=1;i<H;i++)powers[i]=1LL*powers[i-1]*316%Q;
 int next[H][10],add[H][10];for(int i=0;i<H;i++)for(int k=0;k<10;k++){next[i][k]=(i+g[k].j)%H;add[i][k]=1LL*powers[i]*g[k].v%Q;}
 for(int k=0;k<10;k++){assert(g[k].j>0&&g[k].j<H&&next[g[k].j][inv[k]]==0&&mod(g[k].v+1LL*powers[g[k].j]*g[inv[k]].v,Q)==0);for(int l=0;l<k;l++)assert(g[k].j!=g[l].j);}
 ofstream recipe(dir+"/RECIPE.json");recipe<<"{\"group\":\"Z6941 semidirect316 C180\",\"law\":\"(v,I)*(c,j)=(v+316^I*c,I+j)\",\"normal_modulus\":6941,\"phase_order\":180,\"source_phase_order\":90,\"action\":316,\"n\":1249380,\"m\":6246900,\"encoding\":\"6941*phase+normal\",\"gens\":[";
 for(int k=0;k<10;k++){if(k)recipe<<',';recipe<<"{\"normal\":"<<g[k].v<<",\"phase\":"<<g[k].j<<",\"inverse_index\":"<<inv[k]<<'}';}recipe<<"],\"source_BFS\":0}\n";recipe.close();
 long long words=0,phase90words=0,targetwords=0;array<int,7>word{};vector<int>witness;bool interrupted=false;
 function<void(int,int,int,int)>dfs=[&](int i,int v,int last,int depth){
  if(interrupted)return;words++;if((words&16383)==0&&expired()){interrupted=true;return;}
  if(i==90){phase90words++;if(v==0){targetwords++;if(witness.empty())witness.assign(word.begin(),word.begin()+depth);}}
  if(depth==7)return;for(int k=0;k<10;k++)if(last<0||k!=inv[last]){word[depth]=k;int w=v+add[i][k];if(w>=Q)w-=Q;dfs(next[i][k],w,k,depth+1);}
 };
 dfs(0,0,-1,0);if(!interrupted)assert(words==5978711);
 ofstream gate(dir+"/KERNEL_GATE.json");gate<<"{\"target_normal\":0,\"target_phase\":90,\"complete\":"<<(!interrupted?"true":"false")<<",\"NB_words_length0to7\":"<<words<<",\"raw_phase90_prefixes\":"<<phase90words<<",\"exact_kernel_target_word_count\":"<<targetwords<<",\"passes\":"<<(!interrupted&&targetwords?"true":"false")<<",\"first_witness_dart_indices\":[";
 for(size_t i=0;i<witness.size();i++){if(i)gate<<',';gate<<witness[i];}gate<<"],\"first_witness_signed_generator_indices\":[";
 for(size_t i=0;i<witness.size();i++){if(i)gate<<',';gate<<(witness[i]<5?witness[i]+1:-(witness[i]-4));}gate<<"],\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";gate.close();
 if(interrupted||!targetwords){ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(interrupted?"UNKNOWN_CPU_LIMIT_DURING_KERNEL_GATE":"EXACT_SHORT_KERNEL_GATE_REJECTS_FIXED_DOUBLELIFT")<<"\",\"gate_complete\":"<<(!interrupted?"true":"false")<<",\"actual_graphs\":0,\"n_hypothetical\":1249380,\"actual_D\":null,\"kernel_target_word_count\":"<<targetwords<<",\"source_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}
 auto step=[&](int u,int k){int i=u/Q,v=u%Q,w=v+add[i][k];if(w>=Q)w-=Q;return Q*next[i][k]+w;};
 for(int u=0;u<N;u++)for(int k=0;k<10;k++){int v=step(u,k);assert(v!=u&&step(v,inv[k])==u);}
 vector<int>dist(N,-1),queue(N);int lo=0,hi=1,ecc=0;queue[0]=0;dist[0]=0;
 while(lo<hi){
  if((lo&4095)==0&&expired()){ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\"UNKNOWN_CPU_LIMIT_DURING_ACTUAL_BFS\",\"actual_graphs\":1,\"actual_D\":null,\"reached\":"<<hi<<"}\n";return 0;}
  int u=queue[lo++];for(int k=0;k<10;k++){int v=step(u,k);if(dist[v]<0){dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);queue[hi++]=v;}}
 }
 assert(hi==N);bool hit=ecc<=7;vector<int>hist(ecc+1);int missing=0,first=-1;
 ofstream miss(dir+"/R7_MISSING.json");miss<<"{\"root\":0,\"missing_vertex_ids\":[";bool comma=false;
 for(int u=0;u<N;u++){hist[dist[u]]++;if(dist[u]>7){if(comma)miss<<',';comma=true;miss<<u;missing++;if(first<0)first=u;}}miss<<"]}\n";miss.close();
 if(hit){ofstream edges(dir+"/graph_d10_D7_n1249380.edges");edges<<N<<" 6246900\n";long long count=0;for(int u=0;u<N;u++)for(int k=0;k<10;k++){int v=step(u,k);if(u<v){edges<<u<<' '<<v<<'\n';count++;}}assert(count==6246900);}
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"COMPLETE_D7_REQUIRES_PARENT_CHECK":"SOLE_CENTRAL_DOUBLELIFT_FAILS_D7")<<"\",\"gate_complete\":true,\"kernel_target_word_count\":"<<targetwords<<",\"actual_graphs\":1,\"n\":1249380,\"m\":6246900,\"Delta\":10,\"regular\":true,\"simple\":true,\"undirected\":true,\"connected\":true,\"identity_BFS_complete\":true,\"actual_D\":"<<ecc<<",\"global_D_scope\":\"OnefullidentityBFSandCayleyvertextransitivity\",\"root_R7_missing\":"<<missing<<",\"first_R7_missing\":";if(first<0)out<<"null";else out<<first;out<<",\"distance_histogram\":[";
 for(int i=0;i<=ecc;i++){if(i)out<<',';out<<hist[i];}out<<"],\"ordinary_bad_unordered_pairs\":null,\"source_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"exact_kernel_words="<<targetwords<<" actualD="<<ecc<<" R7miss="<<missing<<" hit="<<hit<<" nativeCPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
using M2=array<int,4>;using M4=array<int,16>;using V4=array<int,4>;
constexpr int M=9,L=81,N=24*M*L;
int mod(int x,int m){x%=m;return x<0?x+m:x;}
M2 mul(M2 a,M2 b){return{(a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,(a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3};}
V4 decode(int x){V4 v;for(int j=0;j<4;j++){v[j]=x%3;x/=3;}return v;}
int affine(M4 a,V4 c,int x){V4 v=decode(x);int out=0,pow=1;for(int i=0;i<4;i++){int z=c[i];for(int j=0;j<4;j++)z+=a[4*i+j]*v[j];out+=(z%3)*pow;pow*=3;}return out;}
int main(int argc,char**argv){
 string dir=argv[1];const double budget=stod(argv[2]);clock_t begin=clock();
 ifstream input(dir+"/input.txt");assert(input);array<M2,4>sl;array<int,4>phase;array<M4,4>chart;array<V4,4>direction;
 for(int k=0;k<4;k++){for(int&x:sl[k])input>>x;input>>phase[k];for(int&x:chart[k])input>>x;for(int&x:direction[k])input>>x;}
 M4 plain;V4 c;for(int&x:plain)input>>x;for(int&x:c)input>>x;
 vector<M2>group;const M2 I={1,0,0,1};group.push_back(I);
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int cc=0;cc<3;cc++)for(int d=0;d<3;d++){M2 x={a,b,cc,d};if(mod(a*d-b*cc,3)==1&&x!=I)group.push_back(x);}assert(group.size()==24);
 array<array<int,4>,24>gstep;for(int g=0;g<24;g++)for(int k=0;k<4;k++){M2 t=mul(group[g],sl[k]);auto it=find(group.begin(),group.end(),t);assert(it!=group.end());gstep[g][k]=it-group.begin();}
 array<array<array<int,3>,81>,4>line;
 for(int k=0;k<4;k++)for(int x=0;x<81;x++)for(int lambda=0;lambda<3;lambda++){V4 add;for(int j=0;j<4;j++)add[j]=(lambda*direction[k][j])%3;line[k][x][lambda]=affine(chart[k],add,x);}
 for(int k=0;k<4;k++)for(int x=0;x<81;x++)for(int y:line[k][x])assert(find(line[k^1][y].begin(),line[k^1][y].end(),x)!=line[k^1][y].end());
 array<int,81>gamma,invgamma;array<int,81>seen{};for(int x=0;x<81;x++){gamma[x]=affine(plain,c,x);seen[gamma[x]]++;invgamma[gamma[x]]=x;}for(int n:seen)assert(n==1);
 for(int x=0;x<81;x++)assert(gamma[gamma[x]]==x);
 auto power=[&](int k,int x){if(k>=0)while(k--)x=gamma[x];else while(k++)x=invgamma[x];return x;};
 ofstream combined(dir+"/NATIVE_RESULT.json");combined<<"{\"cases\":[";int done=0,hits=0;bool timedout=false;
 for(int extra:{2,3}){
  if(double(clock()-begin)/CLOCKS_PER_SEC>budget){timedout=true;break;}
  clock_t start=clock();array<int,4>pstep={1,-1,extra,-extra};array<array<int,81>,4>pimage;
  for(int k=0;k<4;k++)for(int x=0;x<81;x++){pimage[k][x]=power(pstep[k],x);assert(power(-pstep[k],pimage[k][x])==x);}
  vector<array<int,16>>adj(N);
  for(int g=0;g<24;g++)for(int z=0;z<9;z++)for(int x=0;x<81;x++){
   int u=81*(9*g+z)+x,pos=0;
   for(int k=0;k<4;k++){int cell=9*gstep[g][k]+mod(z+phase[k],9);for(int y:line[k][x])adj[u][pos++]=81*cell+y;}
   for(int k=0;k<4;k++)adj[u][pos++]=81*(9*g+mod(z+pstep[k],9))+pimage[k][x];
   assert(pos==16);sort(adj[u].begin(),adj[u].end());assert(adjacent_find(adj[u].begin(),adj[u].end())==adj[u].end()&&!binary_search(adj[u].begin(),adj[u].end(),u));
  }
  for(int u=0;u<N;u++)for(int v:adj[u])assert(binary_search(adj[v].begin(),adj[v].end(),u));
  int tested=0,failed=-1,missing=0,first=-1;array<int,5>layers{};vector<int>dist(N),queue(N);bool allpass=true;
  for(int fiberroot=0;fiberroot<81;fiberroot++){
   if(double(clock()-begin)/CLOCKS_PER_SEC>budget){timedout=true;allpass=false;break;}
   fill(dist.begin(),dist.end(),-1);int lo=0,hi=1;queue[0]=fiberroot;dist[fiberroot]=0;array<int,5>localLayers{};localLayers[0]=1;
   for(int d=0;d<4;d++){int end=hi;while(lo<end){int u=queue[lo++];for(int v:adj[u])if(dist[v]<0){dist[v]=d+1;queue[hi++]=v;}}localLayers[d+1]=hi-end;}
   tested++;
   if(hi<N){allpass=false;failed=fiberroot;missing=N-hi;first=find(dist.begin(),dist.end(),-1)-dist.begin();layers=localLayers;break;}
  }
  const bool hit=allpass&&tested==81;if(hit)hits++;
  string status=hit?"COMPLETE_D4_REQUIRES_PARENT_ACCEPTANCE":timedout?"UNKNOWN_NATIVE_CPU_LIMIT":"FIRST_FAILING_REPRESENTATIVE_REJECTS_D4";
  if(done++)combined<<',';
  string path=dir+"/power"+to_string(extra)+"_RESULT.json";ofstream out(path);
  auto write=[&](ostream&out){out<<"{\"extra_plain_power\":"<<extra<<",\"status\":\""<<status<<"\",\"n\":"<<N<<",\"m\":"<<8LL*N<<",\"degree\":16,\"simple\":true,\"undirected\":true,\"actual_controller_states\":216,\"full_adjacency_constructed\":true,\"R4_representatives_checked\":"<<tested<<",\"failed_source_fiber\":";
   if(failed>=0)out<<failed;else out<<"null";out<<",\"root_R4_missing_states\":"<<missing<<",\"first_missing_target\":";if(first>=0)out<<first;else out<<"null";
   out<<",\"failed_root_R4_layers\":[";for(int i=0;i<5;i++){if(i)out<<',';out<<layers[i];}out<<"],\"global_exact_D\":";if(hit)out<<4;else out<<"null";out<<",\"source9720_BFS_repeated\":0,\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<'}';};
  write(out);out<<'\n';write(combined);combined.flush();
  if(failed>=0){ofstream miss(dir+"/power"+to_string(extra)+"_missing_states.json");miss<<"{\"source_fiber\":"<<failed<<",\"missing_vertex_ids\":[";int count=0;for(int t=0;t<N;t++)if(dist[t]<0){if(count++)miss<<',';miss<<t;}miss<<"]}\n";}
  if(hit){ofstream edges(dir+"/graph_d16_D4_n17496_power"+to_string(extra)+".edges");edges<<N<<' '<<8LL*N<<'\n';long long count=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){edges<<u<<' '<<v<<'\n';count++;}assert(count==8LL*N);}
  cout<<"power "<<extra<<" "<<status<<" roots "<<tested<<" missing "<<missing<<" first "<<first<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
 }
 combined<<"],\"status\":\""<<(timedout?"UNKNOWN_NATIVE_CPU_LIMIT":hits?"POSITIVE_MODELS_REQUIRE_PARENT_ACCEPTANCE":"TWO_FIXED_MODELS_COMPLETE_NO_D4")<<"\",\"models_tested\":"<<done<<",\"unattempted\":"<<2-done<<",\"positive_models\":"<<hits<<",\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
 ofstream gfile(dir+"/SL2_ELEMENTS.json");gfile<<'[';for(int i=0;i<24;i++){if(i)gfile<<',';gfile<<'[';for(int j=0;j<4;j++){if(j)gfile<<',';gfile<<group[i][j];}gfile<<']';}gfile<<"]\n";
}

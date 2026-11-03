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
constexpr int Q=4201,H=25,G=Q*H,N=2*G;
int mod(long long a,int m){a%=m;return a<0?a+m:a;}
int pw(int a,int n,int m){int r=1;while(n){if(n&1)r=1LL*r*a%m;a=1LL*a*a%m;n>>=1;}return r;}
bool prime(int n){if(n<2)return false;for(int d=2;d*d<=n;d++)if(n%d==0)return false;return true;}
struct Case{
 int index,beta,image=0,D=-1,done=0;long long words=0;
 bool gatecomplete=false,graph=false,unknown=false,hit=false;
 array<int,2>ecc={-1,-1},miss={-1,-1},first={-1,-1};
 vector<vector<int>>hist=vector<vector<int>>(2);
 array<array<int,5>,2>coeff{};
};
void writecase(ostream&o,const Case&c){
 o<<"{\"index\":"<<c.index<<",\"beta\":"<<c.beta<<",\"thin_image_size\":"<<c.image<<",\"word_prefixes_visited\":"<<c.words<<",\"gate_complete\":"<<(c.gatecomplete?"true":"false")<<",\"actual_graph\":"<<(c.graph?"true":"false")<<",\"base_BFS_complete\":"<<c.done<<",\"status\":\""<<(c.unknown?"UNKNOWN_CPU_LIMIT":c.hit?"COMPLETE_D10_REQUIRES_PARENT_CHECK":!c.graph?"THIN_RESIDUE_IMAGE_REJECTS_D10":"ACTUAL_GRAPH_FAILS_D10")<<"\",\"actual_D\":";
 if(c.D<0)o<<"null";else o<<c.D;o<<",\"roots\":[";
 for(int b=0;b<c.done;b++){if(b)o<<',';o<<"{\"source_base\":"<<b<<",\"root_vertex\":"<<b*G<<",\"eccentricity\":"<<c.ecc[b]<<",\"R10_missing\":"<<c.miss[b]<<",\"first_R10_missing\":";if(c.first[b]<0)o<<"null";else o<<c.first[b];o<<",\"distance_histogram\":[";for(size_t j=0;j<c.hist[b].size();j++){if(j)o<<',';o<<c.hist[b][j];}o<<"]}";}
 o<<"],\"normal_dart_coefficients\":[";
 for(int b=0;b<2;b++){if(b)o<<',';o<<'[';for(int k=0;k<5;k++){if(k)o<<',';o<<c.coeff[b][k];}o<<']';}o<<"]}";
}
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();rlimit lim{10,10};setrlimit(RLIMIT_CPU,&lim);
 auto expired=[&](){return double(clock()-start)/CLOCKS_PER_SEC>9.78;};
 ifstream input(dir+"/THIN_INPUT.txt");int sourcebase,target;input>>sourcebase>>target;assert(input&&sourcebase==0&&target==34);
 assert(prime(Q)&&Q%25==1);for(int p=4052;p<Q;p++)if(p%25==1)assert(!prime(p));
 array<array<int,5>,2>phase={array<int,5>{1,24,0,9,5},array<int,5>{11,14,0,16,20}};array<int,5>rev={1,0,2,3,4};
 int nb[2][5],next[2][25][5];
 for(int b=0;b<2;b++)for(int k=0;k<5;k++){nb[b][k]=k<2?b:1-b;for(int i=0;i<25;i++)next[b][i][k]=(i+phase[b][k])%25;for(int l=0;l<k;l++)assert(nb[b][k]!=nb[b][l]||phase[b][k]!=phase[b][l]);}
 vector<int>roots;for(int beta=2;beta<Q;beta++)if(pw(beta,25,Q)==1&&pw(beta,5,Q)!=1)roots.push_back(beta);assert(roots.size()==20);
 ofstream rootout(dir+"/TARGET_ROOTS.json");rootout<<"{\"q\":4201,\"exact_order\":25,\"roots_ascending\":[";for(int i=0;i<20;i++){if(i)rootout<<',';rootout<<roots[i];}rootout<<"]}\n";rootout.close();
 vector<Case>cases;bool timeout=false,hit=false;int gatepass=0,graphs=0,BFS=0;
 ofstream stream(dir+"/CASES.jsonl");vector<int>dist(N),queue(N);
 for(int index=0;index<20&&!timeout&&!hit;index++){
  Case c;c.index=index;c.beta=roots[index];
  {ofstream cursor(dir+"/cursor.json");cursor<<"{\"index\":"<<index<<",\"beta\":"<<c.beta<<",\"stage\":\"EXACT_THIN_SLOT_IMAGE\"}\n";}
  array<int,25>powers;powers[0]=1;for(int i=1;i<25;i++)powers[i]=1LL*powers[i-1]*c.beta%Q;
  c.coeff[0]={0,0,0,1,mod(-1929,Q)};
  c.coeff[1]={178,mod(-178LL*powers[14],Q),0,mod(-powers[16],Q),mod(1929LL*powers[20],Q)};
  int add[2][25][5];
  for(int b=0;b<2;b++)for(int i=0;i<25;i++)for(int k=0;k<5;k++)add[b][i][k]=1LL*powers[i]*c.coeff[b][k]%Q;
  for(int b=0;b<2;b++)for(int k=0;k<5;k++){int to=nb[b][k],r=rev[k];assert((phase[b][k]+phase[to][r])%25==0&&mod(c.coeff[b][k]+1LL*powers[phase[b][k]]*c.coeff[to][r],Q)==0);}
  vector<unsigned char>image(Q);bool interrupted=false;
  function<void(int,int,int,int,int)>dfs=[&](int b,int i,int p,int back,int depth){
   if(interrupted)return;c.words++;if((c.words&16383)==0&&expired()){interrupted=true;return;}
   if(25*b+i==target)image[p]=1;if(depth==10)return;
   for(int k=0;k<5;k++)if(k!=back){int t=p+add[b][i][k];if(t>=Q)t-=Q;dfs(nb[b][k],next[b][i][k],t,rev[k],depth+1);}
  };
  dfs(sourcebase,0,0,-1,0);c.image=accumulate(image.begin(),image.end(),0);c.gatecomplete=!interrupted;
  if(interrupted){timeout=c.unknown=true;}
  else{
   assert(c.words==1747626);
   if(c.image==Q){
    gatepass++;graphs++;c.graph=true;
    {ofstream cursor(dir+"/cursor.json");cursor<<"{\"index\":"<<index<<",\"beta\":"<<c.beta<<",\"stage\":\"ACTUAL_GRAPH_TWO_BASE_BFS\"}\n";}
    auto step=[&](int u,int k){int b=u/G,e=u%G,i=e/Q,p=e%Q,t=p+add[b][i][k];if(t>=Q)t-=Q;return nb[b][k]*G+next[b][i][k]*Q+t;};
    for(int u=0;u<N&&!timeout;u++){if((u&8191)==0&&expired()){timeout=c.unknown=true;break;}int b=u/G;for(int k=0;k<5;k++){int v=step(u,k);assert(v!=u&&step(v,rev[k])==u);}}
    int globalD=0;
    for(int b=0;b<2&&!timeout;b++){
     fill(dist.begin(),dist.end(),-1);int lo=0,hi=1,ecc=0;queue[0]=b*G;dist[b*G]=0;
     while(lo<hi){if((lo&8191)==0&&expired()){timeout=c.unknown=true;break;}int u=queue[lo++];for(int k=0;k<5;k++){int v=step(u,k);if(dist[v]<0){dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);queue[hi++]=v;}}}
     if(timeout)break;assert(hi==N);c.done++;BFS++;c.ecc[b]=ecc;globalD=max(globalD,ecc);c.miss[b]=0;c.hist[b].assign(ecc+1,0);
     for(int v=0;v<N;v++){c.hist[b][dist[v]]++;if(dist[v]>10){c.miss[b]++;if(c.first[b]<0)c.first[b]=v;}}
    }
    if(!timeout){
     c.D=globalD;c.hit=globalD<=10;hit=c.hit;
     if(hit){
      ofstream edges(dir+"/graph_d5_D10_n210050.edges");edges<<N<<" 525125\n";long long edgecount=0;
      for(int u=0;u<N;u++)for(int k=0;k<5;k++){int v=step(u,k);if(u<v){edges<<u<<' '<<v<<'\n';edgecount++;}}assert(edgecount==525125);
      ofstream recipe(dir+"/HIT_RECIPE.json");recipe<<"{\"q\":4201,\"phase_order\":25,\"beta\":"<<c.beta<<",\"n\":210050,\"m\":525125,\"actual_D\":"<<globalD<<",\"law\":\"(v,I)*(c,j)=(v+beta^I*c,I+j)\",\"vertex_encoding\":\"base*105025+phase*4201+normal\",\"loops\":[[0,0,1],[1,178,11]],\"cross0to1\":[[0,0],[1,9],[-1929,5]],\"base_BFS_complete\":2}\n";
     }
    }
   }
  }
  cases.push_back(c);writecase(stream,c);stream<<'\n';stream.flush();
 }
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_D10_HIT_REQUIRES_PARENT_CHECK":timeout?"UNKNOWN_AGGREGATE_CPU_LIMIT":"ALL20_EMBEDDINGS_TERMINAL_NO_D10")<<"\",\"q\":4201,\"n_hypothetical\":210050,\"m_if_constructed\":525125,\"target_Delta\":5,\"target_D\":10,\"chosen_source_base\":"<<sourcebase<<",\"chosen_target_controller\":"<<target<<",\"embeddings_total\":20,\"embeddings_touched\":"<<cases.size()<<",\"embeddings_unattempted\":"<<20-cases.size()<<",\"gate_passers\":"<<gatepass<<",\"actual_graphs\":"<<graphs<<",\"complete_base_BFS\":"<<BFS<<",\"full_hits\":"<<int(hit)<<",\"cases\":[";
 for(size_t i=0;i<cases.size();i++){if(i)out<<',';writecase(out,cases[i]);}out<<"],\"source_BFS\":0,\"ordinary_bad_unordered_pairs\":null,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"touched="<<cases.size()<<" gates="<<gatepass<<" actualgraphs="<<graphs<<" baseBFS="<<BFS<<" hit="<<hit<<" timeout="<<timeout<<" nativeCPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

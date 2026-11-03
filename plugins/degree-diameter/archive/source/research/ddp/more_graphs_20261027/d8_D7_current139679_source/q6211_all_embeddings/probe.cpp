#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
constexpr int Q=6211,H=23,N=Q*H;
int mod(long long a,int m){a%=m;return a<0?a+m:a;}
int pw(int a,int n,int m){int r=1;while(n){if(n&1)r=1LL*r*a%m;a=1LL*a*a%m;n>>=1;}return r;}
bool prime(int n){for(int d=2;d*d<=n;d++)if(n%d==0)return false;return n>=2;}
struct Case{
 int index,beta,image=0,miss=-1,first=-1,D=-1,reached=0;long long words=0;
 bool gate_complete=false,graph=false,bfs=false,hit=false,unknown=false,connected=false;
 array<int,8>coeff{};vector<int>hist;
};
void writecase(ostream&o,const Case&c){
 o<<"{\"index\":"<<c.index<<",\"beta\":"<<c.beta<<",\"thin_image_size\":"<<c.image<<",\"word_prefixes_visited\":"<<c.words<<",\"gate_complete\":"<<(c.gate_complete?"true":"false")<<",\"actual_graph\":"<<(c.graph?"true":"false")<<",\"identity_BFS_complete\":"<<(c.bfs?"true":"false")<<",\"connected\":"<<(c.connected?"true":"false")<<",\"status\":\""<<(c.unknown?"UNKNOWN_CPU_LIMIT":c.hit?"COMPLETE_D7_REQUIRES_PARENT_CHECK":!c.graph?"THIN_RESIDUE_IMAGE_REJECTS_D7":"ACTUAL_GRAPH_FAILS_D7")<<"\",\"actual_D\":";
 if(c.D<0)o<<"null";else o<<c.D;o<<",\"root_R7_missing\":";if(c.miss<0)o<<"null";else o<<c.miss;
 o<<",\"first_R7_missing\":";if(c.first<0)o<<"null";else o<<c.first;o<<",\"distance_histogram\":[";
 for(size_t i=0;i<c.hist.size();i++){if(i)o<<',';o<<c.hist[i];}o<<"],\"dart_coefficients\":[";
 for(int i=0;i<8;i++){if(i)o<<',';o<<c.coeff[i];}o<<"]}";
}
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();rlimit lim{10,10};setrlimit(RLIMIT_CPU,&lim);
 auto expired=[&](){return double(clock()-start)/CLOCKS_PER_SEC>9.80;};
 assert(prime(Q)&&Q%23==1);for(int p=6074;p<Q;p++)if(p%23==1)assert(!prime(p));
 array<int,8>phase={1,8,7,20,22,15,16,3},inv={4,5,6,7,0,1,2,3};array<int,4>positive={0,1,-1391,-2844};
 assert(set<int>(phase.begin(),phase.end()).size()==8);
 int next[23][8];for(int i=0;i<23;i++)for(int k=0;k<8;k++)next[i][k]=(i+phase[k])%23;
 array<long long,23>raw{};long long rawwords=0;
 function<void(int,int,int)>rawdfs=[&](int i,int last,int depth){
  raw[i]++;rawwords++;if(depth==7)return;
  for(int k=0;k<8;k++)if(last<0||k!=inv[last])rawdfs(next[i][k],k,depth+1);
 };
 rawdfs(0,-1,0);assert(rawwords==1098057);int thin=min_element(raw.begin(),raw.end())-raw.begin();
 ofstream rawout(dir+"/RAW_PHASE_COUNTS.json");rawout<<"{\"NB_words_length0to7\":"<<rawwords<<",\"chosen_thin_phase\":"<<thin<<",\"minimum_raw_count\":"<<raw[thin]<<",\"tie_rule\":\"Smallestphase\",\"raw_counts\":[";
 for(int i=0;i<23;i++){if(i)rawout<<',';rawout<<raw[i];}rawout<<"]}\n";rawout.close();
 vector<int>roots;for(int b=2;b<Q;b++)if(pw(b,23,Q)==1)roots.push_back(b);assert(roots.size()==22);
 ofstream rootout(dir+"/TARGET_ROOTS.json");rootout<<"{\"q\":6211,\"roots_ascending\":[";for(int i=0;i<22;i++){if(i)rootout<<',';rootout<<roots[i];}rootout<<"]}\n";rootout.close();
 vector<Case>cases;bool timeout=false,hit=false;int gatepass=0,graphs=0,completedBFS=0;
 ofstream streaming(dir+"/CASES.jsonl");vector<int>dist(N),queue(N);
 for(int index=0;index<22&&!timeout&&!hit;index++){
  Case c;c.index=index;c.beta=roots[index];
  {ofstream cursor(dir+"/cursor.json");cursor<<"{\"index\":"<<index<<",\"beta\":"<<c.beta<<",\"stage\":\"THIN_PHASE_COMPLETE_IMAGE\"}\n";}
  array<int,23>powers;powers[0]=1;for(int i=1;i<23;i++)powers[i]=1LL*powers[i-1]*c.beta%Q;
  for(int k=0;k<4;k++){c.coeff[k]=mod(positive[k],Q);c.coeff[k+4]=mod(-1LL*powers[(23-phase[k])%23]*c.coeff[k],Q);}
  int add[23][8];for(int i=0;i<23;i++)for(int k=0;k<8;k++)add[i][k]=1LL*powers[i]*c.coeff[k]%Q;
  for(int k=0;k<8;k++)assert(next[phase[k]][inv[k]]==0&&mod(c.coeff[k]+1LL*powers[phase[k]]*c.coeff[inv[k]],Q)==0);
  vector<unsigned char>image(Q);bool interrupted=false;
  function<void(int,int,int,int)>dfs=[&](int i,int p,int last,int depth){
   if(interrupted)return;c.words++;if((c.words&16383)==0&&expired()){interrupted=true;return;}
   if(i==thin)image[p]=1;if(depth==7)return;
   for(int k=0;k<8;k++)if(last<0||k!=inv[last]){int t=p+add[i][k];if(t>=Q)t-=Q;dfs(next[i][k],t,k,depth+1);}
  };
  dfs(0,0,-1,0);c.image=accumulate(image.begin(),image.end(),0);c.gate_complete=!interrupted;
  if(interrupted){timeout=c.unknown=true;}
  else{
   assert(c.words==rawwords);
   if(c.image==Q){
    gatepass++;c.graph=true;graphs++;
    {ofstream cursor(dir+"/cursor.json");cursor<<"{\"index\":"<<index<<",\"beta\":"<<c.beta<<",\"stage\":\"ACTUAL_GRAPH_IDENTITY_BFS\"}\n";}
    auto step=[&](int u,int k){int i=u/Q,p=u%Q,t=p+add[i][k];if(t>=Q)t-=Q;return Q*next[i][k]+t;};
    for(int u=0;u<N&&!timeout;u++){
     if((u&4095)==0&&expired()){timeout=c.unknown=true;break;}
     for(int k=0;k<8;k++){int v=step(u,k);assert(v!=u&&step(v,inv[k])==u);}
    }
    if(!timeout){
     fill(dist.begin(),dist.end(),-1);int lo=0,hi=1;queue[0]=0;dist[0]=0;int ecc=0;
     while(lo<hi){
      if((lo&4095)==0&&expired()){timeout=c.unknown=true;break;}
      int u=queue[lo++];for(int k=0;k<8;k++){int v=step(u,k);if(dist[v]<0){dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);queue[hi++]=v;}}
     }
     c.reached=hi;
     if(!timeout){
      c.bfs=true;completedBFS++;c.connected=hi==N;assert(c.connected);c.D=ecc;c.hist.assign(ecc+1,0);c.miss=0;
      for(int v=0;v<N;v++){c.hist[dist[v]]++;if(dist[v]>7){c.miss++;if(c.first<0)c.first=v;}}
      c.hit=ecc<=7;hit=c.hit;
      if(hit){
       ofstream edges(dir+"/graph_d8_D7_n142853.edges");edges<<N<<" 571412\n";int edgecount=0;
       for(int u=0;u<N;u++)for(int k=0;k<8;k++){int v=step(u,k);if(u<v){edges<<u<<' '<<v<<'\n';edgecount++;}}assert(edgecount==571412);
       ofstream recipe(dir+"/HIT_RECIPE.json");recipe<<"{\"group\":\"Z6211 semidirectbeta C23\",\"beta\":"<<c.beta<<",\"law\":\"(p,i)*(c,j)=(p+beta^i*c,i+j)\",\"encoding\":\"6211*phase+normal\",\"positive_phases\":[1,8,7,20],\"positive_centered_coefficients\":[0,1,-1391,-2844],\"n\":142853,\"m\":571412,\"actual_D\":"<<ecc<<",\"gens\":[";
       for(int k=0;k<8;k++){if(k)recipe<<',';recipe<<"{\"phase\":"<<phase[k]<<",\"coefficient\":"<<c.coeff[k]<<",\"inverse_index\":"<<inv[k]<<'}';}recipe<<"]}\n";
       ofstream distances(dir+"/hit_identity_distances.u8.bin",ios::binary);for(int d:dist){unsigned char x=d;distances.write((char*)&x,1);}
      }
     }
    }
   }
  }
  cases.push_back(c);writecase(streaming,c);streaming<<'\n';streaming.flush();
 }
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_D7_HIT_REQUIRES_PARENT_CHECK":timeout?"UNKNOWN_CPU_LIMIT":"ALL22_EMBEDDINGS_TERMINAL_NO_D7")<<"\",\"q\":6211,\"n_hypothetical\":142853,\"m_if_constructed\":571412,\"target_Delta\":8,\"target_D\":7,\"chosen_thin_phase\":"<<thin<<",\"raw_minimum\":"<<raw[thin]<<",\"embeddings_total\":22,\"embeddings_touched\":"<<cases.size()<<",\"embeddings_unattempted\":"<<22-cases.size()<<",\"gate_passers\":"<<gatepass<<",\"actual_graphs\":"<<graphs<<",\"complete_identity_BFS\":"<<completedBFS<<",\"full_hits\":"<<int(hit)<<",\"cases\":[";
 for(size_t i=0;i<cases.size();i++){if(i)out<<',';writecase(out,cases[i]);}out<<"],\"source_BFS\":0,\"ordinary_bad_unordered_pairs\":null,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"thin="<<thin<<" rawmin="<<raw[thin]<<" touched="<<cases.size()<<" gates="<<gatepass<<" graphs="<<graphs<<" BFS="<<completedBFS<<" hit="<<hit<<" timeout="<<timeout<<" nativeCPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

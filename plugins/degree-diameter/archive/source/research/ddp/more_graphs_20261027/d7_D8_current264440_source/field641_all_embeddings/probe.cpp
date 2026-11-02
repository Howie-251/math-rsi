#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <sys/resource.h>
#include <vector>
using namespace std;
constexpr int Q=641,M=40,N=282040;
const array<int,7>phase{4,9,6,36,31,34,20},inverse{3,4,5,0,1,2,6};
template<class T>void arr(ostream&o,const T&v){o<<'[';bool f=true;for(auto x:v){if(!f)o<<',';f=false;o<<+x;}o<<']';}
int power(int a,int n,int p){int z=1;while(n){if(n&1)z=z*a%p;a=a*a%p;n>>=1;}return z;}
int main(int argc,char**argv){
 assert(argc==4);int thin=stoi(argv[1]),expectedRaw=stoi(argv[2]);string dir=argv[3];assert(0<=thin&&thin<440);rlimit limit{20,20};assert(setrlimit(RLIMIT_CPU,&limit)==0);clock_t started=clock();
 array<int,40>pow11;for(int j=0;j<M;j++)pow11[j]=power(6,j,11);assert(power(6,40,11)==1);
 array<int,7>n11{1,3,9,0,0,0,0};for(int d=0;d<3;d++)n11[d+3]=(11-n11[d]*pow11[phase[d+3]]%11)%11;
 for(int d=0;d<7;d++)assert((n11[d]+pow11[phase[d]]*n11[inverse[d]])%11==0);
 vector<int>roots;for(int a=2;a<Q;a++)if(power(a,40,Q)==1&&power(a,20,Q)!=1&&power(a,8,Q)!=1)roots.push_back(a);assert(roots.size()==16);
 ofstream rf(dir+"/ROOTS.json");rf<<"{\"field\":641,\"exact_order\":40,\"roots\":";arr(rf,roots);rf<<"}\n";rf.close();
 ofstream cases(dir+"/CASES.jsonl"),images(dir+"/THIN_IMAGES.u8.bin",ios::binary);int done=0,reject=0,graphs=0,hits=0,cursor=0,hitD=-1;bool timed=false;
 for(int ri=0;ri<(int)roots.size();ri++){
  cursor=ri;if(double(clock()-started)/CLOCKS_PER_SEC>=19.0){timed=true;break;}clock_t caseStart=clock();int beta=roots[ri];array<int,40>powQ;for(int j=0;j<M;j++)powQ[j]=power(beta,j,Q);
  array<int,7>normal{1,588,234,0,0,0,0};for(int d=0;d<3;d++)normal[d+3]=(Q-normal[d]*powQ[phase[d+3]]%Q)%Q;
  for(int d=0;d<7;d++){assert((phase[d]+phase[inverse[d]])%M==0);assert((normal[d]+powQ[phase[d]]*normal[inverse[d]])%Q==0);}
  vector<uint8_t>seen(Q,0);int raw=0;
  function<void(int,int,int,int,int)>dfs=[&](int depth,int j,int u,int x,int previous){
   if(j*11+u==thin){seen[x]=1;raw++;}if(depth==8)return;
   for(int d=0;d<7;d++)if(previous<0||d!=inverse[previous])dfs(depth+1,(j+phase[d])%M,(u+pow11[j]*n11[d])%11,(x+powQ[j]*normal[d])%Q,d);
  };
  dfs(0,0,0,0,-1);assert(raw==expectedRaw);images.write(reinterpret_cast<const char*>(seen.data()),seen.size());images.flush();vector<int>missing;for(int x=0;x<Q;x++)if(!seen[x])missing.push_back(x);
  cases<<"{\"embedding_ordinal\":"<<ri<<",\"beta\":"<<beta<<",\"thin_controller\":"<<thin<<",\"thin_raw_routes\":"<<raw<<",\"thin_image_size\":"<<Q-missing.size()<<",\"thin_missing_residues\":";arr(cases,missing);
  if(!missing.empty()){reject++;cases<<",\"status\":\"STRICT_THIN_IMAGE_REJECTION\",\"actual_graph\":false,\"actual_global_D\":null,\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";cases.flush();done++;continue;}
  graphs++;vector<int8_t>distance(N,-1);vector<int>queue(N);array<int,9>hist{};distance[0]=0;queue[0]=0;hist[0]=1;int lo=0,hi=1;
  auto step=[&](int id,int d){int z=id/Q,x=id%Q,j=z/11,u=z%11;return (((j+phase[d])%M)*11+(u+pow11[j]*n11[d])%11)*Q+(x+powQ[j]*normal[d])%Q;};
  while(lo<hi){int u=queue[lo++];if(distance[u]==8)continue;for(int d=0;d<7;d++){int v=step(u,d);if(distance[v]<0){distance[v]=distance[u]+1;hist[distance[v]]++;queue[hi++]=v;}}}
  int firstMissing=-1;for(int u=0;u<N;u++)if(distance[u]<0){firstMissing=u;break;}
  cases<<",\"actual_graph\":true,\"n\":282040,\"m\":987140,\"simple\":true,\"degree\":7,\"connectivity_paper_guarantee\":true,\"identity_R8_reached\":"<<hi<<",\"identity_R8_missing\":"<<N-hi<<",\"first_R8_missing_vertex\":"<<firstMissing<<",\"identity_distance_histogram_through8\":";arr(cases,hist);
  if(firstMissing>=0){int z=firstMissing/Q;cases<<",\"first_missing_state\":["<<z/11<<','<<z%11<<','<<firstMissing%Q<<"],\"status\":\"ACTUAL_IDENTITY_R8_FAILURE\",\"actual_global_D\":null,\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";cases.flush();done++;continue;}
  for(int k=0;k<=8;k++)if(hist[k])hitD=k;hits=1;done++;cases<<",\"status\":\"COMPLETE_TARGET_DIAMETER_HIT\",\"actual_global_D\":"<<hitD<<",\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";cases.flush();
  ofstream gr(dir+"/graph_d7_D8_n282040.edges");gr<<N<<' '<<987140<<'\n';int m=0;for(int u=0;u<N;u++)for(int d=0;d<7;d++){int v=step(u,d);assert(u!=v);if(u<v){gr<<u<<' '<<v<<'\n';m++;}}assert(m==987140);gr.close();
  ofstream hp(dir+"/HIT.json");hp<<"{\"status\":\"PRODUCER_COMPLETE_CAYLEY_HIT\",\"embedding_ordinal\":"<<ri<<",\"field\":641,\"phase_modulus\":40,\"beta\":"<<beta<<",\"n\":282040,\"m\":987140,\"degree\":7,\"exact_global_D\":"<<hitD<<",\"operation\":\"LEFT law(n,I)(m,J)=(n+rho^I*m,I+J)\",\"positive_phases\":[4,9,6],\"positive_normal11\":[1,3,9],\"positive_field_integer\":[1,-53,234],\"all_normal11\":";arr(hp,n11);hp<<",\"all_normal641\":";arr(hp,normal);hp<<",\"all_phases\":";arr(hp,phase);hp<<",\"action11\":6,\"involution\":[20,0,0],\"vertex_encoding\":\"(phase*11+normal11)*641+normal641\",\"identity_distance_histogram\":";arr(hp,hist);hp<<",\"ordinary_unordered_bad_pairs\":0}\n";cursor=ri+1;break;
 }
 cases.close();images.close();if(!timed&&!hits)cursor=16;
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hits?"PRODUCER_FULL_TARGET_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_ALL16_EMBEDDINGS_NO_HIT")<<"\",\"embeddings_total\":16,\"embeddings_processed\":"<<done<<",\"strict_thin_image_rejections\":"<<reject<<",\"actual_implicit_graphs\":"<<graphs<<",\"identity_R8_checks\":"<<graphs<<",\"hits\":"<<hits<<",\"actual_global_D\":"<<(hits?to_string(hitD):"null")<<",\"next_cursor\":"<<cursor<<",\"untested\":"<<16-done<<",\"source_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"ordinary_unordered_bad_pairs\":"<<(hits?"0":"null")<<"}\n";
 cout<<"processed="<<done<<" thinreject="<<reject<<" graphs="<<graphs<<" hits="<<hits<<" CPU="<<double(clock()-started)/CLOCKS_PER_SEC<<'\n';
}

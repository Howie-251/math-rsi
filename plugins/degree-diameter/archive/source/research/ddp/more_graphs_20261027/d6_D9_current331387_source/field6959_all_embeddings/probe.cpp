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
constexpr int Q=6959,M=49,N=340991;
const array<int,6>phase{1,36,45,48,13,4},inverse{3,4,5,0,1,2};
template<class T>void arr(ostream&o,const T&v){o<<'[';bool f=true;for(auto x:v){if(!f)o<<',';f=false;o<<+x;}o<<']';}
int power(int a,int n){int z=1;while(n){if(n&1)z=z*a%Q;a=a*a%Q;n>>=1;}return z;}
int main(int argc,char**argv){
 assert(argc==4);const int thin=stoi(argv[1]),rawExpected=stoi(argv[2]);const string dir=argv[3];assert(thin==23&&rawExpected==58581);rlimit limit{20,20};assert(setrlimit(RLIMIT_CPU,&limit)==0);clock_t started=clock();
 vector<int>roots;for(int a=2;a<Q;a++)if(power(a,49)==1&&power(a,7)!=1)roots.push_back(a);assert(roots.size()==42);
 ofstream rf(dir+"/ROOTS.json");rf<<"{\"field\":6959,\"exact_order\":49,\"roots\":";arr(rf,roots);rf<<"}\n";rf.close();
 ofstream cases(dir+"/CASES.jsonl"),imagefile(dir+"/THIN_IMAGES.u8.bin",ios::binary);int done=0,gatefail=0,graphs=0,hits=0,cursor=0,hitD=-1;bool timed=false;
 for(int ri=0;ri<(int)roots.size();ri++){
  cursor=ri;if(double(clock()-started)/CLOCKS_PER_SEC>=19.0){timed=true;break;}int beta=roots[ri];clock_t caseStart=clock();
  array<int,6>factor;for(int d=0;d<6;d++)factor[d]=power(beta,phase[d]);
  array<int,6>normal{0,1,1512,0,0,0};for(int d=0;d<3;d++)normal[d+3]=(Q-normal[d]*factor[d+3]%Q)%Q;
  for(int d=0;d<6;d++){assert((phase[d]+phase[inverse[d]])%M==0);assert(factor[d]*factor[inverse[d]]%Q==1);assert((normal[d]*factor[inverse[d]]+normal[inverse[d]])%Q==0);}
  vector<uint8_t>seen(Q,0);int wordcount=0;
  function<void(int,int,int,int)>dfs=[&](int depth,int j,int x,int prev){if(j==thin){seen[x]=1;wordcount++;}if(depth==9)return;for(int d=0;d<6;d++)if(prev<0||d!=inverse[prev])dfs(depth+1,(j+phase[d])%M,(x*factor[d]+normal[d])%Q,d);};
  dfs(0,0,0,-1);assert(wordcount==rawExpected);imagefile.write(reinterpret_cast<const char*>(seen.data()),seen.size());imagefile.flush();
  vector<int>missing;for(int x=0;x<Q;x++)if(!seen[x])missing.push_back(x);
  cases<<"{\"embedding_ordinal\":"<<ri<<",\"beta\":"<<beta<<",\"thin_phase\":23,\"thin_raw_routes\":"<<wordcount<<",\"thin_image_size\":"<<Q-missing.size()<<",\"thin_missing_residues\":";arr(cases,missing);
  if(!missing.empty()){gatefail++;cases<<",\"status\":\"STRICT_THIN_IMAGE_REJECTION\",\"actual_graph\":false,\"actual_global_D\":null,\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";cases.flush();done++;continue;}
  graphs++;vector<int8_t>distance(N,-1);vector<int>queue(N);array<int,10>hist{};distance[0]=0;queue[0]=0;hist[0]=1;int lo=0,hi=1;
  auto step=[&](int u,int d){int j=u/Q,x=u%Q;return ((j+phase[d])%M)*Q+(x*factor[d]+normal[d])%Q;};
  while(lo<hi){int u=queue[lo++];if(distance[u]==9)continue;for(int d=0;d<6;d++){int v=step(u,d);if(distance[v]<0){distance[v]=distance[u]+1;hist[distance[v]]++;queue[hi++]=v;}}}
  int firstMissing=-1;for(int u=0;u<N;u++)if(distance[u]<0){firstMissing=u;break;}
  cases<<",\"actual_graph\":true,\"n\":340991,\"m\":1022973,\"simple\":true,\"degree\":6,\"connectivity_paper_guarantee\":true,\"identity_R9_reached\":"<<hi<<",\"identity_R9_missing\":"<<N-hi<<",\"first_R9_missing_vertex\":"<<firstMissing<<",\"identity_distance_histogram_through9\":";arr(cases,hist);
  if(firstMissing>=0){cases<<",\"status\":\"ACTUAL_IDENTITY_R9_FAILURE\",\"actual_global_D\":null,\"first_missing_state\":["<<firstMissing/Q<<','<<firstMissing%Q<<"],\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";cases.flush();done++;continue;}
  for(int k=0;k<=9;k++)if(hist[k])hitD=k;hits=1;done++;cases<<",\"status\":\"COMPLETE_TARGET_DIAMETER_HIT\",\"actual_global_D\":"<<hitD<<",\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";cases.flush();
  ofstream gr(dir+"/graph_d6_D9_n340991.edges");gr<<N<<' '<<1022973<<'\n';int count=0;for(int u=0;u<N;u++)for(int d=0;d<6;d++){int v=step(u,d);assert(u!=v);if(u<v){gr<<u<<' '<<v<<'\n';count++;}}assert(count==1022973);gr.close();
  ofstream hp(dir+"/HIT.json");hp<<"{\"status\":\"PRODUCER_COMPLETE_CAYLEY_HIT\",\"embedding_ordinal\":"<<ri<<",\"field\":6959,\"phase_modulus\":49,\"beta\":"<<beta<<",\"n\":340991,\"m\":1022973,\"degree\":6,\"exact_global_D\":"<<hitD<<",\"operation\":\"RIGHT law(j,n)(k,t)=(j+k,n*beta^k+t)\",\"positive_generators\":[[1,0],[36,1],[45,1512]],\"all_phases\":";arr(hp,phase);hp<<",\"all_normals\":";arr(hp,normal);hp<<",\"vertex_encoding\":\"phase*6959+normal\",\"identity_distance_histogram\":";arr(hp,hist);hp<<",\"ordinary_unordered_bad_pairs\":0}\n";cursor=ri+1;break;
 }
 cases.close();imagefile.close();if(!timed&&!hits)cursor=42;
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hits?"PRODUCER_FULL_TARGET_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_ALL42_EMBEDDINGS_NO_HIT")<<"\",\"embeddings_total\":42,\"embeddings_processed\":"<<done<<",\"strict_thin_image_rejections\":"<<gatefail<<",\"actual_implicit_graphs\":"<<graphs<<",\"identity_R9_checks\":"<<graphs<<",\"hits\":"<<hits<<",\"actual_global_D\":"<<(hits?to_string(hitD):"null")<<",\"next_cursor\":"<<cursor<<",\"untested\":"<<42-done<<",\"source_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"ordinary_unordered_bad_pairs\":"<<(hits?"0":"null")<<"}\n";
 cout<<"processed="<<done<<" gatefail="<<gatefail<<" graphs="<<graphs<<" hits="<<hits<<" CPU="<<double(clock()-started)/CLOCKS_PER_SEC<<'\n';
}

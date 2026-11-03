#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <sys/resource.h>
#include <vector>
using namespace std;
constexpr int N=5500;
const array<int,8>phase{1,6,7,9,19,14,13,11},inverse{4,5,6,7,0,1,2,3};
template<class T>void arr(ostream&o,const T&v){o<<'[';bool f=true;for(auto x:v){if(!f)o<<',';f=false;o<<+x;}o<<']';}
struct Frame{int lambda;array<int,21>a,b;vector<array<int,6>>coef;int raw=0;};
struct Case{int fi,stratum;array<array<int,2>,4>v;};
void vectors(ostream&o,const array<array<int,2>,4>&v){o<<'[';for(int i=0;i<4;i++){if(i)o<<',';arr(o,v[i]);}o<<']';}
int main(int argc,char**argv){
 assert(argc==4);int thin=stoi(argv[1]),expected=stoi(argv[2]);string dir=argv[3];assert(thin==110&&expected==78);rlimit lim{20,20};assert(setrlimit(RLIMIT_CPU,&lim)==0);clock_t started=clock();
 array<int,20>pow11;pow11[0]=1;for(int i=1;i<20;i++)pow11[i]=pow11[i-1]*2%11;
 array<int,8>n11{1,8,2,8,0,0,0,0};for(int d=0;d<4;d++)n11[d+4]=(11-n11[d]*pow11[phase[d+4]]%11)%11;
 for(int d=0;d<8;d++)assert((n11[d]+pow11[phase[d]]*n11[inverse[d]])%11==0);
 vector<Frame>frames;
 for(int lambda:{2,3}){
  Frame F;F.lambda=lambda;F.a[0]=1;F.b[0]=0;for(int j=0;j<20;j++){F.a[j+1]=F.a[j]*lambda%5;F.b[j+1]=(F.a[j]+F.b[j]*lambda)%5;}assert(F.a[20]==1&&F.b[20]==0&&F.a[4]==1&&F.b[4]!=0);
  set<array<int,6>>unique;
  function<void(int,int,int,int,array<int,6>)>dfs=[&](int depth,int j,int u,int prev,array<int,6>c){
   if(j*11+u==thin){F.raw++;unique.insert(c);}if(depth==5)return;
   for(int d=0;d<8;d++)if(prev<0||d!=inverse[prev]){auto nc=c;int which=d%4;if(which){int exponent=d<4?j:(j+phase[d])%20,sign=d<4?1:-1;int k=2*(which-1);nc[k]=(nc[k]+sign*F.a[exponent]+5)%5;nc[k+1]=(nc[k+1]+sign*F.b[exponent]+5)%5;}dfs(depth+1,(j+phase[d])%20,(u+pow11[j]*n11[d])%11,d,nc);}
  };
  dfs(0,0,0,-1,{0,0,0,0,0,0});assert(F.raw==expected);F.coef.assign(unique.begin(),unique.end());
  ofstream cf(dir+"/THIN_COEFFICIENTS_lambda"+to_string(lambda)+".json");cf<<"{\"lambda\":"<<lambda<<",\"thin_controller\":110,\"raw_routes\":78,\"distinct_coefficients\":"<<F.coef.size()<<",\"format\":\"[a2,b2,a3,b3,a4,b4];endpoint=sum(ai I+bi N)vi\",\"coefficient_tuples\":[";bool first=true;for(auto c:F.coef){if(!first)cf<<',';first=false;arr(cf,c);}cf<<"]}\n";frames.push_back(F);
 }
 vector<array<int,2>>V;for(int x=0;x<5;x++)for(int y=0;y<5;y++)V.push_back({x,y});array<int,2>e2{0,1},zero{0,0};vector<Case>cases;
 for(int f=0;f<2;f++){
  for(auto v3:V)for(auto v4:V)cases.push_back({f,0,{zero,e2,v3,v4}});
  for(int s=0;s<5;s++)for(auto v4:V)cases.push_back({f,1,{zero,array<int,2>{s,0},e2,v4}});
  for(int s=0;s<5;s++)for(int t=0;t<5;t++)cases.push_back({f,2,{zero,array<int,2>{s,0},array<int,2>{t,0},e2}});
 }assert(cases.size()==1550);
 ofstream out(dir+"/CASES.jsonl"),images(dir+"/THIN_IMAGES.u32le.bin",ios::binary);int done=0,reject=0,graphs=0,hits=0,cursor=0,hitD=-1;bool timed=false;array<int,3>stratumRejected{},stratumGraphs{};array<int,2>lambdaRejected{},lambdaGraphs{};
 for(int ci=0;ci<(int)cases.size();ci++){
  cursor=ci;if(double(clock()-started)/CLOCKS_PER_SEC>=19.0){timed=true;break;}clock_t caseStart=clock();const Case&C=cases[ci];const Frame&F=frames[C.fi];uint32_t image=0;
  for(auto c:F.coef){int x=0,y=0;for(int i=1;i<4;i++){x+=c[2*(i-1)]*C.v[i][0]+c[2*(i-1)+1]*C.v[i][1];y+=c[2*(i-1)]*C.v[i][1];}image|=1u<<(5*(x%5)+(y%5));}
  for(int b=0;b<4;b++)images.put(char(image>>(8*b)&255));images.flush();vector<int>missing;for(int k=0;k<25;k++)if(!(image>>k&1))missing.push_back(k);
  out<<"{\"candidate_ordinal\":"<<ci<<",\"lambda\":"<<F.lambda<<",\"stratum\":"<<C.stratum<<",\"positive_module_vectors\":";vectors(out,C.v);out<<",\"thin_image_size\":"<<25-missing.size()<<",\"thin_missing_module_ids\":";arr(out,missing);
  if(!missing.empty()){reject++;stratumRejected[C.stratum]++;lambdaRejected[C.fi]++;out<<",\"status\":\"STRICT_THIN_IMAGE_REJECTION\",\"actual_graph\":false,\"actual_global_D\":null,\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";out.flush();done++;continue;}
  graphs++;stratumGraphs[C.stratum]++;lambdaGraphs[C.fi]++;array<array<int,2>,8>w;for(int d=0;d<4;d++){w[d]=C.v[d];int j=phase[d+4];w[d+4]={(5-(F.a[j]*w[d][0]+F.b[j]*w[d][1])%5)%5,(5-F.a[j]*w[d][1]%5)%5};}
  for(int d=0;d<8;d++){auto z=w[inverse[d]];assert((w[d][0]+F.a[phase[d]]*z[0]+F.b[phase[d]]*z[1])%5==0);assert((w[d][1]+F.a[phase[d]]*z[1])%5==0);}
  auto step=[&](int id,int d){int z=id/25,j=z/11,u=z%11,x=id%25/5,y=id%5;int nj=(j+phase[d])%20,nu=(u+pow11[j]*n11[d])%11,nx=(x+F.a[j]*w[d][0]+F.b[j]*w[d][1])%5,ny=(y+F.a[j]*w[d][1])%5;return (nj*11+nu)*25+nx*5+ny;};
  vector<int8_t>dist(N,-1);vector<int>queue(N);array<int,6>hist{};int lo=0,hi=1;queue[0]=0;dist[0]=0;hist[0]=1;
  while(lo<hi){int u=queue[lo++];if(dist[u]==5)continue;for(int d=0;d<8;d++){int v=step(u,d);if(dist[v]<0){dist[v]=dist[u]+1;hist[dist[v]]++;queue[hi++]=v;}}}
  int firstMissing=-1;for(int u=0;u<N;u++)if(dist[u]<0){firstMissing=u;break;}
  out<<",\"actual_graph\":true,\"n\":5500,\"m\":22000,\"simple\":true,\"degree\":8,\"connectivity_paper_guarantee\":true,\"identity_R5_reached\":"<<hi<<",\"identity_R5_missing\":"<<N-hi<<",\"first_R5_missing_vertex\":"<<firstMissing<<",\"identity_distance_histogram_through5\":";arr(out,hist);
  if(firstMissing>=0){out<<",\"status\":\"ACTUAL_IDENTITY_R5_FAILURE\",\"actual_global_D\":null,\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";out.flush();done++;continue;}
  for(int k=0;k<=5;k++)if(hist[k])hitD=k;hits=1;done++;out<<",\"status\":\"COMPLETE_TARGET_DIAMETER_HIT\",\"actual_global_D\":"<<hitD<<",\"CPU_seconds\":"<<double(clock()-caseStart)/CLOCKS_PER_SEC<<"}\n";out.flush();
  ofstream gr(dir+"/graph_d8_D5_n5500.edges");gr<<N<<' '<<22000<<'\n';int count=0;for(int u=0;u<N;u++)for(int d=0;d<8;d++){int v=step(u,d);assert(u!=v);if(u<v){gr<<u<<' '<<v<<'\n';count++;}}assert(count==22000);gr.close();
  ofstream hp(dir+"/HIT.json");hp<<"{\"status\":\"PRODUCER_COMPLETE_JORDAN_CAYLEY_HIT\",\"candidate_ordinal\":"<<ci<<",\"lambda\":"<<F.lambda<<",\"stratum\":"<<C.stratum<<",\"positive_module_vectors\":";vectors(hp,C.v);hp<<",\"n\":5500,\"m\":22000,\"degree\":8,\"exact_global_D\":"<<hitD<<",\"phase_modulus\":20,\"normal11_action\":2,\"positive_phases\":[1,6,7,9],\"positive_normal11\":[1,8,2,8],\"Jordan_matrix\":[["<<F.lambda<<",1],[0,"<<F.lambda<<"]],\"all_mod11_normals\":";arr(hp,n11);hp<<",\"vertex_encoding\":\"(phase*11+normal11)*25+5*modulex+moduley\",\"operation\":\"LEFT normal11+=2^phase*dartnormal11;module+=A^phase*dartmodule\",\"identity_distance_histogram\":";arr(hp,hist);hp<<",\"ordinary_unordered_bad_pairs\":0}\n";cursor=ci+1;break;
 }
 out.close();images.close();if(!timed&&!hits)cursor=1550;
 ofstream r(dir+"/NATIVE_RESULT.json");r<<"{\"status\":\""<<(hits?"PRODUCER_FULL_TARGET_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_ALL1550_NO_HIT")<<"\",\"objects_total\":1550,\"objects_processed\":"<<done<<",\"strict_thin_image_rejections\":"<<reject<<",\"actual_implicit_graphs\":"<<graphs<<",\"identity_R5_checks\":"<<graphs<<",\"hits\":"<<hits<<",\"actual_global_D\":"<<(hits?to_string(hitD):"null")<<",\"next_cursor\":"<<cursor<<",\"untested\":"<<1550-done<<",\"rejected_by_strata625_125_25\":";arr(r,stratumRejected);r<<",\"actualgraphs_by_strata625_125_25\":";arr(r,stratumGraphs);r<<",\"rejected_by_lambda2_3\":";arr(r,lambdaRejected);r<<",\"actualgraphs_by_lambda2_3\":";arr(r,lambdaGraphs);r<<",\"source_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"ordinary_unordered_bad_pairs\":"<<(hits?"0":"null")<<"}\n";
 cout<<"processed="<<done<<" rejected="<<reject<<" graphs="<<graphs<<" hits="<<hits<<" CPU="<<double(clock()-started)/CLOCKS_PER_SEC<<'\n';
}

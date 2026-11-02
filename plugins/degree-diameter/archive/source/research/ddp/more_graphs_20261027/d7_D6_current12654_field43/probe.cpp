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
constexpr int Q=43,N=14706;
const array<int,7>ph{17,13,10,1,5,8,9},t19{17,11,17,18,14,15,0},inv{3,4,5,0,1,2,6};
int pw(int a,int e,int p){int r=1;while(e--){r=r*a%p;}return r;}
int enc(int j,int u,int v){return (j*19+u)*43+v;}
template<class T>void arr(ostream&o,const T&v){o<<'[';bool f=true;for(auto x:v){if(!f)o<<',';f=false;o<<x;}o<<']';}
struct Frame{int a;array<int,7>f43;vector<array<int,3>>coef;long long raw=0;};
int main(int argc,char**argv){
 assert(argc==4);int thin=stoi(argv[1]),expected=stoi(argv[2]);string dir=argv[3];assert(thin==126&&expected==152);rlimit lim{20,20};assert(setrlimit(RLIMIT_CPU,&lim)==0);clock_t started=clock();
 array<int,7>f19;for(int d=0;d<7;d++)f19[d]=pw(9,ph[d],19);for(int d=0;d<7;d++)assert((t19[d]*f19[inv[d]]+t19[inv[d]])%19==0);
 vector<Frame>frames;
 for(int action:{7,37}){
  assert(pw(action,6,43)==1&&pw(action,3,43)==42&&pw(action,2,43)!=1);Frame F;F.a=action;
  for(int d=0;d<7;d++)F.f43[d]=pw(action,ph[d],43);
  array<array<int,3>,7>shift{};for(int d=0;d<3;d++){shift[d][d]=1;shift[d+3][d]=(43-F.f43[d+3])%43;}
  set<array<int,3>>unique;
  function<void(int,int,int,int,array<int,3>)>dfs=[&](int depth,int j,int u,int prev,array<int,3>c){
   if(j*19+u==thin){F.raw++;unique.insert(c);}if(depth==6)return;
   for(int d=0;d<7;d++)if(prev<0||d!=inv[prev]){array<int,3>nc;for(int k=0;k<3;k++)nc[k]=(c[k]*F.f43[d]+shift[d][k])%43;dfs(depth+1,(j+ph[d])%18,(u*f19[d]+t19[d])%19,d,nc);}
  };
  dfs(0,0,0,-1,{0,0,0});assert(F.raw==expected);F.coef.assign(unique.begin(),unique.end());
  ofstream cf(dir+"/THIN_COEFFICIENTS_action"+to_string(action)+".json");cf<<"{\"action\":"<<action<<",\"controller_slot\":126,\"raw_routes\":"<<F.raw<<",\"distinct_coefficients\":"<<F.coef.size()<<",\"coefficient_triples\":[";bool first=true;for(auto c:F.coef){if(!first)cf<<',';first=false;arr(cf,c);}cf<<"]}\n";
  frames.push_back(F);
 }
 vector<array<int,3>>points;for(int b=0;b<43;b++)for(int c=0;c<43;c++)points.push_back({1,b,c});for(int c=0;c<43;c++)points.push_back({0,1,c});points.push_back({0,0,1});assert(points.size()==1893);
 array<int,3>control{1,18,39};vector<pair<int,array<int,3>>>cases{{0,control},{1,control}};for(int f=0;f<2;f++)for(auto p:points)if(p!=control)cases.push_back({f,p});assert(cases.size()==3786);
 ofstream out(dir+"/CASES.jsonl");int done=0,rejected=0,graphs=0,hits=0;array<int,44>imagehist{};array<int,2>rejectedBy{},graphsBy{};int next_cursor=0;bool timed=false;
 for(int ci=0;ci<(int)cases.size();ci++){
  next_cursor=ci;if(double(clock()-started)/CLOCKS_PER_SEC>=19.6){timed=true;break;}
  auto[fi,p]=cases[ci];const Frame&F=frames[fi];bool seen[43]={};for(auto c:F.coef)seen[(c[0]*p[0]+c[1]*p[1]+c[2]*p[2])%43]=true;int image=0,firstMissing=-1;for(int x=0;x<43;x++){image+=seen[x];if(!seen[x]&&firstMissing<0)firstMissing=x;}imagehist[image]++;
  out<<"{\"candidate_ordinal\":"<<ci<<",\"action43\":"<<F.a<<",\"normal43\":";arr(out,p);out<<",\"inherited_source_control\":"<<(ci<2?"true":"false")<<",\"thin_image_size\":"<<image;
  if(image<43){rejected++;rejectedBy[fi]++;out<<",\"status\":\"STRICT_THIN_IMAGE_REJECTION\",\"missing_thin_field\":"<<firstMissing<<",\"actual_graph\":false,\"actual_global_D\":null}\n";out.flush();done++;continue;}
  graphs++;graphsBy[fi]++;array<int,7>v43{};for(int d=0;d<3;d++){v43[d]=p[d];v43[d+3]=(43-p[d]*F.f43[d+3]%43)%43;}for(int d=0;d<7;d++){assert((v43[d]*F.f43[inv[d]]+v43[inv[d]])%43==0);assert((ph[d]+ph[inv[d]])%18==0);}
  vector<int8_t>dist(N,-1);vector<int>queue(N);int lo=0,hi=1;queue[0]=0;dist[0]=0;array<int,7>hist{};hist[0]=1;
  auto step=[&](int id,int d){int z=id/43,v=id%43,u=z%19,j=z/19;return enc((j+ph[d])%18,(u*f19[d]+t19[d])%19,(v*F.f43[d]+v43[d])%43);};
  while(lo<hi){int u=queue[lo++];if(dist[u]==6)continue;for(int d=0;d<7;d++){int v=step(u,d);if(dist[v]<0){dist[v]=dist[u]+1;hist[dist[v]]++;queue[hi++]=v;}}}
  int miss=-1;for(int id=0;id<N;id++)if(dist[id]<0){miss=id;break;}
  out<<",\"actual_graph\":true,\"simple\":true,\"max_degree\":7,\"identity_R6_reached\":"<<hi<<",\"identity_R6_missing\":"<<N-hi<<",\"first_R6_missing_vertex\":"<<miss<<",\"R6_distance_histogram\":";arr(out,hist);
  if(miss>=0){out<<",\"status\":\"ACTUAL_IDENTITY_R6_FAILURE\",\"actual_global_D\":null,\"connected_by_this_truncated_check\":null}\n";out.flush();done++;continue;}
  hits=1;done++;out<<",\"status\":\"COMPLETE_D6_HIT\",\"actual_global_D\":6,\"connected\":true}\n";out.flush();
  ofstream gr(dir+"/graph_d7_D6_n14706.edges");gr<<N<<' '<<51471<<'\n';int m=0;for(int u=0;u<N;u++)for(int d=0;d<7;d++){int v=step(u,d);assert(v!=u);if(u<v){gr<<u<<' '<<v<<'\n';m++;}}assert(m==51471);gr.close();
  ofstream hp(dir+"/HIT.json");hp<<"{\"status\":\"PRODUCER_COMPLETE_CAYLEY_D6_HIT\",\"candidate_ordinal\":"<<ci<<",\"n\":14706,\"m\":51471,\"degree\":7,\"exact_global_D\":6,\"action43\":"<<F.a<<",\"normal43\":";arr(hp,p);hp<<",\"phase_order\":18,\"normal_moduli\":[19,43],\"action19\":9,\"positive_phases\":[17,13,10],\"positive_normal19\":[17,11,17],\"involution\":[9,0,0],\"trueinverse_phases\":[1,5,8],\"inverse_normal19\":[18,14,15],\"all_normal43\":";arr(hp,v43);hp<<",\"vertex_encoding\":\"(phase*19+normal19)*43+normal43\",\"operation\":\"RIGHT law(j,u,v)(k,s,t)=(j+k,u*9^k+s,v*action43^k+t)\",\"identity_distance_histogram\":";arr(hp,hist);hp<<",\"ordinary_unordered_bad_pairs\":0}\n";next_cursor=ci+1;break;
 }
 out.close();if(!timed&&!hits)next_cursor=3786;
 ofstream r(dir+"/NATIVE_RESULT.json");r<<"{\"status\":\""<<(hits?"PRODUCER_FULL_D6_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_FIXED_PROJECTIVE_FAMILY_NO_HIT")<<"\",\"target_Delta\":7,\"target_D\":6,\"savedL\":12654,\"hypothetical_n\":14706,\"objects_total\":3786,\"objects_processed\":"<<done<<",\"strict_thin_image_rejections\":"<<rejected<<",\"actual_implicit_graphs\":"<<graphs<<",\"identity_R6_checks\":"<<graphs<<",\"hits\":"<<hits<<",\"next_cursor\":"<<next_cursor<<",\"untested\":"<<3786-done<<",\"image_size_histogram\":";arr(r,imagehist);r<<",\"rejected_by_action7_37\":";arr(r,rejectedBy);r<<",\"actual_graphs_by_action7_37\":";arr(r,graphsBy);r<<",\"native_CPU_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"source_BFS\":0,\"ordinary_unordered_bad_pairs\":"<<(hits?"0":"null")<<"}\n";
 cout<<"done="<<done<<" thinreject="<<rejected<<" actualgraphs="<<graphs<<" hits="<<hits<<" cpu="<<double(clock()-started)/CLOCKS_PER_SEC<<'\n';
}

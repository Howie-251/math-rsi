#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
using M2=array<int,4>;using M4=array<int,16>;using V4=array<int,4>;
constexpr int OLD=9720;
clock_t started;
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
int mod(int x,int p){x%=p;return x<0?x+p:x;}
M2 mul(M2 a,M2 b){return{mod(a[0]*b[0]+a[1]*b[2],3),mod(a[0]*b[1]+a[1]*b[3],3),mod(a[2]*b[0]+a[3]*b[2],3),mod(a[2]*b[1]+a[3]*b[3],3)};}
int affine(M4 a,V4 c,int x){
 V4 v;for(int j=0;j<4;j++){v[j]=x%3;x/=3;}
 int out=0,pow=1;for(int i=0;i<4;i++){int z=c[i];for(int j=0;j<4;j++)z+=a[4*i+j]*v[j];out+=mod(z,3)*pow;pow*=3;}return out;
}
void ints(ostream&o,const vector<int>&v){o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';}
int main(){
 started=clock();ifstream input("INPUT.txt");assert(input);
 array<M2,4>sl;array<int,4>phase;array<M4,4>chart;array<V4,4>direction;
 for(int k=0;k<4;k++){for(int&x:sl[k])input>>x;input>>phase[k];for(int&x:chart[k])input>>x;for(int&x:direction[k])input>>x;}
 M4 plain;V4 shift;for(int&x:plain)input>>x;for(int&x:shift)input>>x;
 const M2 I={1,0,0,1},A={0,1,2,2},B={0,1,2,1};
 vector<M2>group{I};for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)for(int d=0;d<3;d++){
  M2 x={a,b,c,d};if(mod(a*d-b*c,3)==1&&x!=I)group.push_back(x);
 }assert(group.size()==24);
 auto index=[&](M2 x){auto it=find(group.begin(),group.end(),x);assert(it!=group.end());return int(it-group.begin());};
 array<array<int,4>,24>next;
 for(int g=0;g<24;g++)for(int k=0;k<4;k++)next[g][k]=index(mul(group[g],sl[k]));
 array<array<array<int,3>,81>,4>line;
 for(int k=0;k<4;k++)for(int x=0;x<81;x++)for(int t=0;t<3;t++){
  V4 add;for(int j=0;j<4;j++)add[j]=mod(t*direction[k][j],3);line[k][x][t]=affine(chart[k],add,x);
 }
 array<int,81>gamma;for(int x=0;x<81;x++)gamma[x]=affine(plain,shift,x);
 for(int x=0;x<81;x++)assert(gamma[gamma[x]]==x);assert(gamma[37]==37);
 vector<vector<int>>adj(OLD);
 for(int g=0;g<24;g++)for(int z=0;z<5;z++)for(int x=0;x<81;x++){
  int u=81*(5*g+z)+x;
  for(int k=0;k<4;k++)for(int y:line[k][x])adj[u].push_back(81*(5*next[g][k]+mod(z+phase[k],5))+y);
  for(int dz:{1,-1})adj[u].push_back(81*(5*g+mod(z+dz,5))+gamma[x]);
  sort(adj[u].begin(),adj[u].end());assert(adj[u].size()==14);
  assert(adjacent_find(adj[u].begin(),adj[u].end())==adj[u].end());assert(!binary_search(adj[u].begin(),adj[u].end(),u));
 }
 for(int u=0;u<OLD;u++)for(int v:adj[u])assert(binary_search(adj[v].begin(),adj[v].end(),u));
 vector<pair<int,int>>matching;vector<int>endpoints,bpowers;M2 power=I;
 for(int k=0;k<6;k++){
  assert(k==0||power!=I);int g=index(power);bpowers.push_back(g);
  matching.push_back({81*(5*g)+37,81*(5*g+1)+37});power=mul(power,B);
 }assert(power==I);assert(find(bpowers.begin(),bpowers.end(),index(A))==bpowers.end());
 matching.push_back({81*(5*index(A)+2)+37,81*(5*index(A)+3)+37});
 for(auto [u,v]:matching){
  assert(binary_search(adj[u].begin(),adj[u].end(),v));endpoints.push_back(u);endpoints.push_back(v);
 }
 auto unique=endpoints;sort(unique.begin(),unique.end());assert(adjacent_find(unique.begin(),unique.end())==unique.end());
 ofstream params("PARAMETERS.json");params<<"{\"source_n\":9720,\"source_m\":68040,\"B_order\":6,\"A_outside_B_subgroup\":true,\"fixed_fiber\":[1,0,1,1],\"fixed_fiber_code\":37,\"B_power_SLindices\":";ints(params,bpowers);
 params<<",\"A_SLindex\":"<<index(A)<<",\"removed_matching\":[";
 for(size_t i=0;i<matching.size();++i){if(i)params<<',';params<<'['<<matching[i].first<<','<<matching[i].second<<']';}
 params<<"],\"hub_endpoint_labels\":";ints(params,endpoints);params<<",\"prospective_n\":9721,\"prospective_m\":68047,\"prospective_degree_bound\":14}\n";params.close();
 for(auto [u,v]:matching){adj[u].erase(lower_bound(adj[u].begin(),adj[u].end(),v));adj[v].erase(lower_bound(adj[v].begin(),adj[v].end(),u));}
 vector<int>dist(OLD,-1),queue(OLD);int lo=0,hi=0;
 for(int u:endpoints){dist[u]=0;queue[hi++]=u;assert(adj[u].size()==13);}
 vector<int>layers{hi};
 for(int d=0;d<3;d++){int end=hi;while(lo<end){int u=queue[lo++];for(int v:adj[u])if(dist[v]<0){dist[v]=d+1;queue[hi++]=v;}}layers.push_back(hi-end);}
 vector<int>missing;for(int t=0;t<OLD;t++)if(dist[t]<0)missing.push_back(t);
 ofstream gate("GATE_RESULT.json");gate<<"{\"status\":\""<<(missing.empty()?"COMPLETE_ENDPOINT_R3_PASS":"COMPLETE_ENDPOINT_R3_FAIL")<<"\",\"graph\":\"source_minus_frozen7_edges\",\"source_n\":9720,\"removed_edges\":7,\"endpoint_count\":14,\"R3_covered\":"<<hi<<",\"R3_missing\":"<<missing.size()<<",\"layers\":";ints(gate,layers);
 gate<<",\"first_missing_target\":";if(missing.empty())gate<<"null";else gate<<missing[0];
 gate<<",\"minimum_endpoint_distance_lower_bound_if_missing\":4,\"CPU_seconds\":"<<cpu()<<"}\n";gate.close();
 if(!missing.empty()){
  ofstream miss("MISSING_TARGETS.json");miss<<"{\"missing_vertex_ids\":";ints(miss,missing);miss<<"}\n";
  int t=missing[0],fiber=t%81,cell=t/81;V4 v;for(int j=0;j<4;j++){v[j]=fiber%3;fiber/=3;}
  ofstream result("RESULT.json");result<<"{\"status\":\"FIXED_MATCHING_HUB_REJECTED_ENDPOINT_R3_GATE\",\"source_n\":9720,\"source_m\":68040,\"source_degree\":14,\"matching_edges\":7,\"distinct_endpoints\":14,\"source_D4_BFS_repeated\":0,\"modified_old_multisource_R3_BFS\":1,\"endpoint_R3_covered\":"<<hi<<",\"endpoint_R3_missing\":"<<missing.size()<<",\"first_missing_target\":"<<t<<",\"first_missing_SLindex\":"<<cell/5<<",\"first_missing_Z5\":"<<cell%5<<",\"first_missing_fiber\":["<<v[0]<<','<<v[1]<<','<<v[2]<<','<<v[3]<<"],\"candidate9721_graph_generated\":false,\"candidate_allroot_BFS\":0,\"new_graphs\":0,\"other_combinations_tested\":0,\"CPU_seconds\":"<<cpu()<<"}\n";
  cout<<"FAIL endpointR3 covered="<<hi<<" missing="<<missing.size()<<" first="<<t<<" CPU="<<cpu()<<'\n';return 0;
 }
 adj.emplace_back();for(int u:endpoints){adj[u].push_back(OLD);adj[OLD].push_back(u);}for(auto&v:adj)sort(v.begin(),v.end());
 for(auto&v:adj)assert(v.size()==14);
 dist.resize(OLD+1);queue.resize(OLD+1);int roots=0,failed_root=-1,failed_target=-1;bool expired=false;
 for(int r=0;r<=OLD;r++){
  if(cpu()>23){expired=true;break;}
  fill(dist.begin(),dist.end(),-1);dist[r]=0;queue[0]=r;lo=0;hi=1;
  for(int d=0;d<4;d++){int end=hi;while(lo<end){int u=queue[lo++];for(int v:adj[u])if(dist[v]<0){dist[v]=d+1;queue[hi++]=v;}}}
  roots++;if(hi!=OLD+1){failed_root=r;failed_target=find(dist.begin(),dist.end(),-1)-dist.begin();break;}
 }
 bool hit=roots==OLD+1&&failed_root<0&&!expired;
 ofstream result("RESULT.json");result<<"{\"status\":\""<<(hit?"COMPLETE9721_D4_HIT_NEEDS_INDEPENDENT_CHECK":expired?"PARTIAL_UNKNOWN_CPU_LIMIT":"FIXED_MATCHING_HUB_REJECTED_OLD_PAIR_D4")<<"\",\"n\":9721,\"m\":68047,\"degree\":14,\"candidate9721_graph_generated\":true,\"candidate_allroot_BFS\":"<<roots<<",\"failed_root\":"<<failed_root<<",\"failed_target\":"<<failed_target<<",\"source_D4_BFS_repeated\":0,\"new_graphs\":"<<(hit?1:0)<<",\"other_combinations_tested\":0,\"CPU_seconds\":"<<cpu()<<"}\n";
 if(hit){ofstream edges("graph_d14_D4_n9721.edges");edges<<"9721 68047\n";int m=0;for(int u=0;u<=OLD;u++)for(int v:adj[u])if(u<v){edges<<u<<' '<<v<<'\n';m++;}assert(m==68047);}
 cout<<"candidate roots="<<roots<<" hit="<<hit<<" expired="<<expired<<" CPU="<<cpu()<<'\n';
}

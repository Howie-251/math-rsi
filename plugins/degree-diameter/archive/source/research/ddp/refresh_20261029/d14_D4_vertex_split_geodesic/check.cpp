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
 ofstream records("ROOT_RESULTS.jsonl");
 vector<int> dist(OLD),queue(OLD);vector<unsigned> first(OLD);int checked=0,singletons=0,fullfail=0,passing_root=-1;unsigned passing=0;bool expired=false;
 for(int root=0;root<81;root++){
  if(cpu()>6){expired=true;break;}
  fill(dist.begin(),dist.end(),-1);fill(first.begin(),first.end(),0u);int lo=1,hi=1;queue[0]=root;dist[root]=0;
  for(int j=0;j<14;j++){int n=adj[root][j];assert(dist[n]<0);dist[n]=1;first[n]=1u<<j;queue[hi++]=n;}
  for(int d=1;d<4;d++){int end=hi;while(lo<end){int u=queue[lo++];for(int v:adj[u]){
    if(dist[v]<0){dist[v]=d+1;first[v]=first[u];queue[hi++]=v;}
    else if(dist[v]==d+1)first[v]|=first[u];
  }}}
  vector<unsigned> supports;array<bool,16384> seen{};int targets4=0,firstsingleton=-1,minsize=15;
  for(int t=0;t<OLD;t++)if(dist[t]==4){targets4++;assert(first[t]);unsigned s=first[t];int size=__builtin_popcount(s);minsize=min(minsize,size);if(size==1&&firstsingleton<0)firstsingleton=t;if(!seen[s]){seen[s]=true;supports.push_back(s);}}
  sort(supports.begin(),supports.end(),[](unsigned a,unsigned b){int x=__builtin_popcount(a),y=__builtin_popcount(b);return x==y?a<b:x<y;});
  long long tested=0;unsigned solution=0;
  if(firstsingleton>=0)singletons++;
  else {
   for(unsigned bits=0;bits<8192;bits++){
    if((bits&255u)==0u&&cpu()>6){expired=true;break;}
    tested++;unsigned colorA=1u|(bits<<1),colorB=16383u^colorA;
    if(__builtin_popcount(colorA)>13||__builtin_popcount(colorB)>13)continue;
    bool ok=true;for(unsigned s:supports)if(!(s&colorA)||!(s&colorB)){ok=false;break;}
    if(ok){solution=colorA;break;}
   }
   if(!solution&&!expired)fullfail++;
  }
  records<<"{\"root_fiber\":"<<root<<",\"root_label\":"<<root<<",\"degree\":14,\"distance4_targets\":"<<targets4<<",\"distinct_geodesic_supports\":"<<supports.size()<<",\"minimum_support_size\":"<<minsize<<",\"first_singleton_target\":"<<firstsingleton<<",\"first_singleton_support\":"<<(firstsingleton>=0?first[firstsingleton]:0u)<<",\"singleton_neighbor_label\":"<<(firstsingleton>=0?adj[root][__builtin_ctz(first[firstsingleton])]:-1)<<",\"partition_assignments_tested\":"<<tested<<",\"passing_colorA_mask\":"<<solution<<",\"complete_negative\":"<<(!solution&&!expired?"true":"false")<<"}\n";records.flush();
  if(!expired)checked++;
  if(solution){passing_root=root;passing=solution;break;}
  if(expired)break;
 }
 if(passing_root>=0){
  vector<int>Aneighbors,Bneighbors;for(int j=0;j<14;j++)((passing&(1u<<j))?Aneighbors:Bneighbors).push_back(adj[passing_root][j]);
  ofstream hit("PASSING_PARTITION.json");hit<<"{\"root\":"<<passing_root<<",\"colorA_mask\":"<<passing<<",\"neighbors_A\":";ints(hit,Aneighbors);hit<<",\"neighbors_B\":";ints(hit,Bneighbors);hit<<",\"source_n\":9720,\"candidate_generated\":false,\"old_old_candidate_distances_checked\":false}\n";
 }
 ofstream result("RESULT.json");result<<"{\"status\":\""<<(passing_root>=0?"PASSING_GEODESIC_GATE_NEEDS_OLD_PAIR_CHECK":expired?"PARTIAL_UNKNOWN_CPU_LIMIT":"COMPLETE_ALL_CURRENT9720_ADJACENT_VERTEX_SPLITS_EXCLUDED")<<"\",\"source_n\":9720,\"source_m\":68040,\"source_degree\":14,\"representative_roots_total\":81,\"representative_roots_completed\":"<<checked<<",\"singleton_rejected_roots\":"<<singletons<<",\"full_partition_rejected_roots\":"<<fullfail<<",\"passing_root\":"<<passing_root<<",\"new_graphs\":0,\"candidate_graphs_generated\":0,\"old_old_candidate_BFS\":0,\"SAT_calls\":0,\"CPU_seconds\":"<<cpu()<<"}\n";
 cout<<"roots="<<checked<<" singleton="<<singletons<<" partitionfail="<<fullfail<<" passingroot="<<passing_root<<" CPU="<<cpu()<<'\n';
}

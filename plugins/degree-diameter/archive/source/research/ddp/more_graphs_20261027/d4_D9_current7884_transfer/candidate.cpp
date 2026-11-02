#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Dart{int to,a,h;};
int main(int argc,char**argv){
 const clock_t start=clock();string dir=argv[1];const int P=109,M=36,R=4,G=P*M,N=3*G;
 int rp[M];rp[0]=1;for(int j=1;j<M;j++)rp[j]=rp[j-1]*R%P;assert(rp[M-1]*R%P==1);
 array<vector<Dart>,3>base;
 auto link=[&](int u,int v,int a,int h){
  base[u].push_back({v,a,h});
  base[v].push_back({u,(P-rp[(M-h)%M]*a%P)%P,(M-h)%M});
 };
 link(0,1,0,0);link(0,2,0,0);link(1,2,1,6);link(0,1,29,10);link(0,1,92,14);
 base[2].push_back({2,0,3});base[2].push_back({2,0,M-3});
 vector<array<int,4>>adj(N);
 for(int v=0;v<3;v++){assert(base[v].size()==4);
  for(int j=0;j<M;j++)for(int i=0;i<P;i++){
   int u=v*G+j*P+i;
   for(int k=0;k<4;k++){auto e=base[v][k];adj[u][k]=e.to*G+((j+e.h)%M)*P+(i+rp[j]*e.a)%P;}
   auto a=adj[u];sort(a.begin(),a.end());assert(adjacent_find(a.begin(),a.end())==a.end()&&find(a.begin(),a.end(),u)==a.end());
  }
 }
 for(int u=0;u<N;u++)for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());
 vector<int>eccs;int checked=0,fail=-1,connected=0,miss=0,witnessTarget=-1;
 for(int rootbase=0;rootbase<3;rootbase++){
  vector<int>d(N,-1),parent(N,-1),q(N);int lo=0,hi=0,root=rootbase*G;d[root]=0;q[hi++]=root;
  while(lo<hi){int u=q[lo++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;parent[v]=u;q[hi++]=v;}}
  connected=hi;int ecc=*max_element(d.begin(),d.end());++checked;eccs.push_back(ecc);
  vector<int>hist(max(1,ecc+1));for(int z:d)if(z>=0)hist[z]++;
  ofstream details(dir+"/root"+to_string(rootbase)+"_check.json");
  details<<"{\"root_base\":"<<rootbase<<",\"root\":"<<root<<",\"visited\":"<<hi<<",\"eccentricity\":"<<ecc<<",\"distance_histogram\":[";
  for(size_t z=0;z<hist.size();z++){if(z)details<<',';details<<hist[z];}
  details<<"]}\n";
  miss=count_if(d.begin(),d.end(),[](int z){return z<0||z>9;});
  if(miss){
   fail=rootbase;
   ofstream slots(dir+"/root"+to_string(rootbase)+"_missing_by_slot.json");
   slots<<"{\"root_base\":"<<rootbase<<",\"radius\":9,\"slots\":[";
   for(int v=0;v<3;v++)for(int j=0;j<M;j++){
    if(v||j)slots<<',';slots<<"{\"end_base\":"<<v<<",\"phase\":"<<j<<",\"missing_field_elements\":[";
    bool first=true;for(int i=0;i<P;i++){int u=v*G+j*P+i;if(d[u]<0||d[u]>9){if(!first)slots<<',';first=false;slots<<i;}}
    slots<<"]}";
   }
   slots<<"]}\n";
   for(int u=0;u<N;u++)if(d[u]>9){witnessTarget=u;break;}
   ofstream path(dir+"/FIRST_FAILED_ROOT_WITNESS.json");
   path<<"{\"root\":"<<root<<",\"root_base\":"<<rootbase<<",\"target\":"<<witnessTarget;
   if(witnessTarget>=0){
    vector<int>route;for(int v=witnessTarget;v>=0;v=parent[v])route.push_back(v);reverse(route.begin(),route.end());
    path<<",\"end_base\":"<<witnessTarget/G<<",\"phase\":"<<(witnessTarget%G)/P<<",\"field_element\":"<<witnessTarget%P<<",\"exact_distance\":"<<d[witnessTarget]<<",\"exact_path\":[";
    for(size_t z=0;z<route.size();z++){if(z)path<<',';path<<route[z];}path<<']';
   }
   path<<"}\n";break;
  }
 }
 bool pass=checked==3&&fail<0;
 if(pass){ofstream edges(dir+"/graph_d4_D9_n11772.edges");edges<<N<<' '<<2*N<<'\n';for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)edges<<u<<' '<<v<<'\n';}
 ofstream out(dir+"/CANDIDATE_RESULT.json");
 out<<"{\"status\":\""<<(pass?"THREE_ORBIT_ROOTS_COMPLETE_HIT":"FIRST_ORBIT_ROOT_FAILED_STOP")
  <<"\",\"candidate_n\":"<<N<<",\"candidate_m\":"<<2*N<<",\"degree\":4,\"simple\":true,\"undirected\":true,\"connected\":"<<(connected==N?"true":"false")
  <<",\"orbit_roots_checked\":"<<checked<<",\"root_eccentricities\":[";
 for(size_t z=0;z<eccs.size();z++){if(z)out<<',';out<<eccs[z];}
 out<<"],\"failed_root_base\":"<<fail<<",\"failed_root_radius9_missing\":"<<(pass?0:miss)
  <<",\"full_D9\":"<<(pass?"true":"false")<<",\"actual_global_D\":";
 if(pass)out<<*max_element(eccs.begin(),eccs.end());else out<<"null";
 out<<",\"ordinary_bad_unordered_pairs\":"<<(pass?"0":"null")<<",\"edgefile_exported\":"<<(pass?"true":"false")
  <<",\"source_BFS\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<(pass?"HIT":"FAILED")<<" roots "<<checked<<" miss "<<miss<<endl;
}

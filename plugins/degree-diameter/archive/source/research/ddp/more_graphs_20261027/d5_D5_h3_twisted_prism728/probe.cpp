#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1],source=argv[2];clock_t begin=clock();rlimit limit{3,3};setrlimit(RLIMIT_CPU,&limit);
 ifstream f(source);int n,m;f>>n>>m;assert(n==364&&m==714);vector<vector<int>>a(728);
 for(int i=0,u,v;i<m;i++){f>>u>>v;assert(u>=0&&u<v&&v<n);for(int s=0;s<2;s++){a[u+s*n].push_back(v+s*n);a[v+s*n].push_back(u+s*n);}}
 ifstream pf(dir+"/pi.txt");array<int,364>pi,seen{};for(int&x:pi){pf>>x;assert(x>=0&&x<n);seen[x]++;}assert(pf);for(int i=0;i<n;i++)assert(seen[i]==1&&pi[pi[i]]==i);
 for(int i=0;i<n;i++){a[i].push_back(n+pi[i]);a[n+pi[i]].push_back(i);}
 int edges=0,maxdeg=0;array<int,6>degrees{};
 for(int u=0;u<728;u++){sort(a[u].begin(),a[u].end());assert(adjacent_find(a[u].begin(),a[u].end())==a[u].end());assert(!binary_search(a[u].begin(),a[u].end(),u));assert(a[u].size()<=5);degrees[a[u].size()]++;maxdeg=max(maxdeg,(int)a[u].size());for(int v:a[u]){assert(find(a[v].begin(),a[v].end(),u)!=a[v].end());if(u<v)edges++;}}
 assert(edges==1792&&degrees[4]==56&&degrees[5]==672);
 array<int,728>d,q;array<int,6>layers{};int roots=0,failroot=-1,failtarget=-1,missing=0;bool timeout=false;
 for(int root=0;root<728;root++){
  if(double(clock()-begin)/CLOCKS_PER_SEC>2.9){timeout=true;break;}
  d.fill(-1);int lo=0,hi=1;q[0]=root;d[root]=0;layers={1,0,0,0,0,0};
  for(int dep=0;dep<5;dep++){int end=hi;while(lo<end){int u=q[lo++];for(int v:a[u])if(d[v]<0){d[v]=dep+1;q[hi++]=v;}}layers[dep+1]=hi-end;}
  roots++;for(int t=0;t<728;t++)if(d[t]<0){assert(root/364!=t/364);if(failtarget<0)failtarget=t;missing++;}
  if(missing){failroot=root;break;}
 }
 bool hit=!timeout&&failroot<0&&roots==728;
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"COMPLETE_D5_REQUIRES_PARENT_CHECK":timeout?"UNKNOWN_CPU_LIMIT":"ONE_REFLECTION_PRISM_HAS_EXACT_D6")<<"\",\"n\":728,\"m\":"<<edges<<",\"max_degree\":"<<maxdeg<<",\"degree_histogram\":{\"4\":"<<degrees[4]<<",\"5\":"<<degrees[5]<<"},\"simple\":true,\"undirected\":true,\"old_edges_retained\":true,\"modified_graph_roots_R5_checked\":"<<roots<<",\"source364_roots_BFS_repeated\":0,\"failed_root\":";
 if(failroot<0)out<<"null";else out<<failroot;out<<",\"first_missing_cross_target\":";if(failtarget<0)out<<"null";else out<<failtarget;
 out<<",\"failed_root_cross_R5_missing\":"<<missing<<",\"layers\":[";for(int i=0;i<6;i++){if(i)out<<',';out<<layers[i];}out<<"],\"actual_D\":";if(timeout)out<<"null";else out<<(hit?5:6);out<<",\"diameter_scope\":\""<<(hit?"All728actualgraphrootsR5plusMoorelowerbound":"FirstactualcrossR5failureplusinheritedglobalupper6")<<"\",\"ordinary_bad_unordered_pairs\":null,\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
 if(hit){ofstream e(dir+"/graph_d5_D5_n728.edges");e<<728<<' '<<edges<<'\n';for(int u=0;u<728;u++)for(int v:a[u])if(u<v)e<<u<<' '<<v<<'\n';}
 cout<<(hit?"HIT":timeout?"UNKNOWN":"EXACT_D6")<<" roots="<<roots<<" crossmissing="<<missing<<" first="<<failtarget<<endl;
}

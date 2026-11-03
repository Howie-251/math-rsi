#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
using Row=array<int,3>;using Pair=array<int,2>;
struct Object{int edge;array<int,4>pins;};
struct Check{int status,target,ecc,reached;};
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1],source=argv[2];clock_t begin=clock();rlimit limit{10,10};setrlimit(RLIMIT_CPU,&limit);
 auto expired=[&](){return double(clock()-begin)/CLOCKS_PER_SEC>9.78;};
 ifstream in(source);int n,m;in>>n>>m;assert(n==1250&&m==1875);vector<Pair>edges(m);array<Row,1250>old;array<int,1250>degree{};for(auto&r:old)r={-1,-1,-1};
 for(int i=0;i<m;i++){in>>edges[i][0]>>edges[i][1];int u=edges[i][0],v=edges[i][1];assert(0<=u&&u<v&&v<n&&degree[u]<3&&degree[v]<3);old[u][degree[u]++]=v;old[v][degree[v]++]=u;if(i)assert(edges[i-1]<edges[i]);}
 for(int d:degree)assert(d==3);assert((edges[0]==Pair{0,1}));
 vector<Object>objects;int shared=0,disjoint=0;
 const array<array<int,4>,3>partitions={array<int,4>{0,1,2,3},array<int,4>{0,2,1,3},array<int,4>{0,3,1,2}};
 for(int e=1;e<m;e++){
  array<int,4>endpoints={0,1,edges[e][0],edges[e][1]};set<array<int,4>>canonical;
  for(auto perm:partitions){Pair a={endpoints[perm[0]],endpoints[perm[1]]},b={endpoints[perm[2]],endpoints[perm[3]]};sort(a.begin(),a.end());sort(b.begin(),b.end());if(a[0]==a[1]||b[0]==b[1])continue;if(b<a)swap(a,b);canonical.insert({a[0],a[1],b[0],b[1]});}
  bool touch=edges[e][0]<=1||edges[e][1]<=1;assert(canonical.size()==size_t(touch?1:3));
  for(auto pins:canonical){objects.push_back({e,pins});if(touch)shared++;else disjoint++;}
 }
 assert(objects.size()==5614&&shared==4&&disjoint==5610);
 ofstream frozen(dir+"/FROZEN_OBJECTS.json");frozen<<"{\"source_n\":1250,\"source_m\":1875,\"anchor\":[0,1],\"objects_total\":5614,\"disjoint_objects\":5610,\"shared_endpoint_objects\":4,\"nonisomorphic_claim\":false,\"objects\":[";
 for(int i=0;i<5614;i++){auto o=objects[i];if(i)frozen<<',';frozen<<"{\"id\":"<<i<<",\"second_edge_id\":"<<o.edge<<",\"second_edge\":["<<edges[o.edge][0]<<','<<edges[o.edge][1]<<"],\"pins_x\":["<<o.pins[0]<<','<<o.pins[1]<<"],\"pins_y\":["<<o.pins[2]<<','<<o.pins[3]<<"]}";}frozen<<"]}\n";frozen.close();
 array<Row,1252>adj;array<int,1252>dist,queue;int currentN=1251;long long Anew=0,Aold=0,Bnew=0,Bold=0;
 auto reset=[&](){copy(old.begin(),old.end(),adj.begin());adj[1250]={-1,-1,-1};adj[1251]={-1,-1,-1};};
 auto cut=[&](Pair e){for(int k=0;k<2;k++){int u=e[k],v=e[1-k];auto it=find(adj[u].begin(),adj[u].end(),v);assert(it!=adj[u].end());*it=-1;}};
 auto spoke=[&](int v,int helper){auto it=find(adj[v].begin(),adj[v].end(),-1);assert(it!=adj[v].end());*it=helper;};
 auto localvalid=[&](vector<int>vertices){sort(vertices.begin(),vertices.end());vertices.erase(unique(vertices.begin(),vertices.end()),vertices.end());for(int u:vertices){auto r=adj[u];sort(r.begin(),r.end());for(int v:r)if(v>=0){assert(v!=u&&find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());}assert(adjacent_find(r.begin(),r.end())==r.end());}};
 auto check=[&](int root)->Check{
  if(expired())return{-1,-1,0,0};fill(dist.begin(),dist.end(),-1);int lo=0,hi=1;queue[0]=root;dist[root]=0;int ecc=0;
  for(int depth=0;depth<10;depth++){int end=hi;while(lo<end){int u=queue[lo++];for(int v:adj[u])if(v>=0&&dist[v]<0){dist[v]=depth+1;queue[hi++]=v;}}if(hi>end)ecc=depth+1;}
  if(hi==currentN)return{1,-1,ecc,hi};int target=find(dist.begin(),dist.begin()+currentN,-1)-dist.begin();return{0,target,ecc,hi};
 };
 auto savegraph=[&](string name,int countN,int countM){ofstream out(dir+"/"+name);out<<countN<<' '<<countM<<'\n';int c=0;for(int u=0;u<countN;u++)for(int v:adj[u])if(v>=0&&u<v){out<<u<<' '<<v<<'\n';c++;}assert(c==countM);};
 reset();cut(edges[0]);spoke(0,1250);spoke(1,1250);adj[1250]={0,1,-1};localvalid({0,1,1250});currentN=1251;
 int Astatus=1,Aroot=-1,Atarget=-1,Amax=0;string Astage="NEW_ROOT";
 Anew++;Check a=check(1250);if(a.status!=1){Astatus=a.status;Aroot=1250;Atarget=a.target;}else{Amax=a.ecc;Astage="OLD_OLD";for(int r=0;r<1250;r++){Aold++;a=check(r);if(a.status!=1){Astatus=a.status;Aroot=r;Atarget=a.target;break;}Amax=max(Amax,a.ecc);}}
 bool hit=Astatus==1,timeout=Astatus<0;int hitN=hit?1251:0,hitObject=-1;
 if(hit){savegraph("graph_d3_D10_n1251.edges",1251,1876);ofstream params(dir+"/HIT_PARAMETERS.json");params<<"{\"kind\":\"A_SINGLE_SUBDIVISION\",\"deleted_edges\":[[0,1]],\"new_vertex\":1250,\"pins\":[0,1],\"n\":1251,\"m\":1876,\"max_degree\":3,\"actual_D\":"<<Amax<<",\"all_modified_roots_checked\":1251}\n";}
 ofstream aout(dir+"/A_RESULT.json");aout<<"{\"status\":\""<<(Astatus==1?"COMPLETE_D10_REQUIRES_PARENT_CHECK":Astatus<0?"UNKNOWN_CPU_LIMIT":"ALL_SINGLE_EDGE_SUBDIVISIONS_EXCLUDED_BY_EDGEVT")<<"\",\"n\":1251,\"m\":1876,\"max_degree\":3,\"simple\":true,\"new_vertex_degree\":2,\"first_bad_stage\":\""<<Astage<<"\",\"first_bad_root\":"<<Aroot<<",\"first_bad_target\":"<<Atarget<<",\"cutoff_lower_bound\":"<<(Astatus==0?11:0)<<",\"actual_D\":";if(Astatus<0)aout<<"null";else aout<<(Astatus==1?Amax:11);aout<<",\"diameter_evidence\":\"Allrootsifpositive,otherwiseR10witnessplusinheritedupper11\",\"new_root_R10_checks\":"<<Anew<<",\"old_root_R10_checks\":"<<Aold<<",\"ordinary_bad_unordered_pairs\":null,\"source_BFS\":0}\n";aout.close();
 int touched=0,failed=0,unknown=0;long long xfail=0,yfail=0,oldfail=0;ofstream stream(dir+"/B_CASES.jsonl");
 for(int i=0;i<5614&&!hit&&!timeout;i++){
  auto o=objects[i];{ofstream cursor(dir+"/cursor.json");cursor<<"{\"stage\":\"B_MODIFIED_GRAPH\",\"object_id\":"<<i<<",\"second_edge_id\":"<<o.edge<<"}\n";}
  if(expired()){timeout=true;break;}touched++;reset();cut(edges[0]);cut(edges[o.edge]);for(int j=0;j<2;j++)spoke(o.pins[j],1250);for(int j=2;j<4;j++)spoke(o.pins[j],1251);adj[1250]={o.pins[0],o.pins[1],1251};adj[1251]={o.pins[2],o.pins[3],1250};
  localvalid({0,1,edges[o.edge][0],edges[o.edge][1],1250,1251});currentN=1252;
  int status=1,badroot=-1,badtarget=-1,maxdist=0;string stage="NEW_X";Bnew++;Check b=check(1250);
  if(b.status!=1){status=b.status;badroot=1250;badtarget=b.target;if(status==0)xfail++;}
  else{maxdist=b.ecc;stage="NEW_Y";Bnew++;b=check(1251);if(b.status!=1){status=b.status;badroot=1251;badtarget=b.target;if(status==0)yfail++;}else{maxdist=max(maxdist,b.ecc);stage="OLD_OLD";for(int root=0;root<1250;root++){Bold++;b=check(root);if(b.status!=1){status=b.status;badroot=root;badtarget=b.target;if(status==0)oldfail++;break;}maxdist=max(maxdist,b.ecc);}}}
  if(status==0)failed++;if(status<0){timeout=true;unknown++;}
  stream<<"{\"object_id\":"<<i<<",\"second_edge_id\":"<<o.edge<<",\"status\":\""<<(status==1?"COMPLETE_D10_REQUIRES_PARENT_CHECK":status<0?"UNKNOWN_CPU_LIMIT":"MODIFIED_R10_COUNTEREXAMPLE")<<"\",\"first_bad_stage\":\""<<stage<<"\",\"first_bad_root\":"<<badroot<<",\"first_bad_target\":"<<badtarget<<",\"distance_lower_bound\":"<<(status==0?11:0)<<",\"actual_D\":";if(status==1)stream<<maxdist;else stream<<"null";stream<<"}\n";stream.flush();
  if(status==1){
   hit=true;hitN=1252;hitObject=i;savegraph("graph_d3_D10_n1252.edges",1252,1878);
   ofstream params(dir+"/HIT_PARAMETERS.json");params<<"{\"kind\":\"B_TWO_CUT_TWO_HELPERS\",\"object_id\":"<<i<<",\"deleted_edges\":[[0,1],["<<edges[o.edge][0]<<','<<edges[o.edge][1]<<"]],\"new_vertices\":[1250,1251],\"pins_x\":["<<o.pins[0]<<','<<o.pins[1]<<"],\"pins_y\":["<<o.pins[2]<<','<<o.pins[3]<<"],\"newhelperedge\":[1250,1251],\"n\":1252,\"m\":1878,\"max_degree\":3,\"actual_D\":"<<maxdist<<",\"all_modified_roots_checked\":1252}\n";
  }
 }
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_D10_HIT_REQUIRES_PARENT_CHECK":timeout?"UNKNOWN_AGGREGATE_CPU_LIMIT":"A_AND_ALL5614_B_OBJECTS_COMPLETE_NO_D10")<<"\",\"source_n\":1250,\"source_m\":1875,\"A_status\":"<<Astatus<<",\"A_actual_D\":";if(Astatus<0)out<<"null";else out<<(Astatus==1?Amax:11);out<<",\"B_objects_total\":5614,\"B_objects_touched\":"<<touched<<",\"B_objects_failed\":"<<failed<<",\"B_objects_unknown\":"<<unknown<<",\"B_objects_unattempted\":"<<5614-touched<<",\"B_new_x_failures\":"<<xfail<<",\"B_new_y_failures\":"<<yfail<<",\"B_old_old_failures\":"<<oldfail<<",\"A_newroot_BFS\":"<<Anew<<",\"A_oldroot_BFS\":"<<Aold<<",\"B_newroot_BFS\":"<<Bnew<<",\"B_oldroot_BFS\":"<<Bold<<",\"hit_n\":";if(hit)out<<hitN;else out<<"null";out<<",\"hit_object_id\":";if(hitObject<0)out<<"null";else out<<hitObject;out<<",\"source_old_BFS\":0,\"ordinary_bad_unordered_pairs\":null,\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
 cout<<"A="<<Astatus<<" Btouched="<<touched<<" Bfailed="<<failed<<" Bunknown="<<unknown<<" Bunattempted="<<5614-touched<<" hitN="<<hitN<<" hitObject="<<hitObject<<" timeout="<<timeout<<" nativeCPU="<<double(clock()-begin)/CLOCKS_PER_SEC<<endl;
}

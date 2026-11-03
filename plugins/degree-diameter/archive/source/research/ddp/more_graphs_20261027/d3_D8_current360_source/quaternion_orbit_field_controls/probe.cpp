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
using Mat=array<int,4>;using Vec=array<int,2>;
int mod(int a,int q){a%=q;return a<0?a+q:a;}
struct Voltage{Vec v;int h;};
struct Link{int u,v;Voltage a;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t start=clock();rlimit lim{10,10};setrlimit(RLIMIT_CPU,&lim);
 ifstream input(dir+"/INPUT.txt");assert(input);int q,D;input>>q>>D;assert(q==7&&D==10);int Q=q*q,G=8*Q,N=5*G;
 array<Mat,8>rho;for(auto&m:rho)for(int&x:m)input>>x;int mt[8][8];for(auto&row:mt)for(int&x:row)input>>x;array<int,8>inv;
 for(int a=0;a<8;a++){inv[a]=-1;for(int b=0;b<8;b++)if(mt[a][b]==0)inv[a]=b;assert(inv[a]>=0);}
 auto act=[&](int h,Vec v){return Vec{mod(rho[h][0]*v[0]+rho[h][1]*v[1],q),mod(rho[h][2]*v[0]+rho[h][3]*v[1],q)};};
 auto inverse=[&](Voltage a){auto v=act(inv[a.h],a.v);return Voltage{Vec{mod(-v[0],q),mod(-v[1],q)},inv[a.h]};};
 vector<Link>links(6);for(auto&l:links)input>>l.u>>l.v>>l.a.v[0]>>l.a.v[1]>>l.a.h;
 array<pair<int,Voltage>,3>semis;for(auto&s:semis)input>>s.first>>s.second.v[0]>>s.second.v[1]>>s.second.h;assert(input);
 auto groupstep=[&](int e,Voltage a){int h=e/Q,code=e%Q;Vec v={code/q,code%q},w=act(h,a.v);return Q*mt[h][a.h]+q*mod(v[0]+w[0],q)+mod(v[1]+w[1],q);};
 vector<vector<int>>adj(N);auto edge=[&](int u,int v){assert(u!=v);adj[u].push_back(v);adj[v].push_back(u);};
 for(auto l:links){auto back=inverse(l.a);for(int e=0;e<G;e++){int t=groupstep(e,l.a);assert(groupstep(t,back)==e);edge(l.u*G+e,l.v*G+t);}}
 for(auto s:semis){auto back=inverse(s.second);assert(back.h==s.second.h&&back.v==s.second.v);for(int e=0;e<G;e++){int t=groupstep(e,s.second);assert(groupstep(t,s.second)==e);if(e<t)edge(s.first*G+e,s.first*G+t);}}
 long long arcs=0;for(int u=0;u<N;u++){sort(adj[u].begin(),adj[u].end());assert(adj[u].size()==3&&adjacent_find(adj[u].begin(),adj[u].end())==adj[u].end());for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());arcs+=3;}assert(N==1960&&arcs/2==2940);
 vector<int>orbit(Q,-1);vector<vector<int>>orbits;orbit[0]=0;orbits.push_back({0});
 for(int v=1;v<Q;v++)if(orbit[v]<0){vector<int>members;for(int h=0;h<8;h++){auto w=act(h,Vec{v/q,v%q});members.push_back(q*w[0]+w[1]);}sort(members.begin(),members.end());assert(unique(members.begin(),members.end())==members.end());int id=orbits.size();for(int x:members){assert(orbit[x]<0);orbit[x]=id;}orbits.push_back(members);}
 assert(orbits.size()==7);vector<int>dist(N),queue(N);int globalD=0,firstbad=-1,firsttarget=-1,firstmissing=0;vector<int>badVertices;vector<vector<int>>histograms;array<int,5>eccs{},misses{};
 for(int b=0;b<5;b++){
  if(double(clock()-start)/CLOCKS_PER_SEC>9.8){ofstream o(dir+"/NATIVE_RESULT.json");o<<"{\"status\":\"UNKNOWN_CPU_LIMIT\",\"actual_graphs\":1,\"BFS_complete\":"<<b<<"}\n";return 0;}
  fill(dist.begin(),dist.end(),-1);int lo=0,hi=1;queue[0]=b*G;dist[b*G]=0;int ecc=0;
  while(lo<hi){int u=queue[lo++];for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);queue[hi++]=v;}}
  assert(hi==N);globalD=max(globalD,ecc);eccs[b]=ecc;vector<int>hist(ecc+1);int missing=0;
  for(int v=0;v<N;v++){hist[dist[v]]++;if(dist[v]>D)missing++;}misses[b]=missing;histograms.push_back(hist);
  if(firstbad<0&&missing){firstbad=b;firstmissing=missing;for(int v=0;v<N;v++)if(dist[v]>D)badVertices.push_back(v);firsttarget=badVertices.front();}
 }
 if(firstbad>=0){
  vector<vector<int>>joint(40,vector<int>(orbits.size()));vector<int>ocount(orbits.size()),ccount(40);
  for(int v:badVertices){int b=v/G,e=v%G,h=e/Q,n=e%Q,c=8*b+h,o=orbit[n];joint[c][o]++;ocount[o]++;ccount[c]++;}
  ofstream f(dir+"/FIRST_BAD_ROOT_Q7.json");f<<"{\"source_base\":"<<firstbad<<",\"source_vertex\":"<<firstbad*G<<",\"target_D\":10,\"missing\":"<<firstmissing<<",\"first_missing_vertex\":"<<firsttarget<<",\"missing_vertices\":[";
  for(size_t i=0;i<badVertices.size();i++){if(i)f<<',';f<<badVertices[i];}f<<"],\"normal_orbit_members_as_qx_plus_y\":[";
  for(size_t i=0;i<orbits.size();i++){if(i)f<<',';f<<'[';for(size_t j=0;j<orbits[i].size();j++){if(j)f<<',';f<<orbits[i][j];}f<<']';}f<<"],\"missing_by_normal_orbit\":[";
  for(size_t i=0;i<ocount.size();i++){if(i)f<<',';f<<ocount[i];}f<<"],\"missing_by_controller\":[";
  for(int c=0;c<40;c++){if(c)f<<',';f<<ccount[c];}f<<"],\"joint_controller_normal_orbit\":[";
  for(int c=0;c<40;c++){if(c)f<<',';f<<'[';for(size_t o=0;o<orbits.size();o++){if(o)f<<',';f<<joint[c][o];}f<<']';}f<<"]}\n";
 }
 bool hit=globalD<=D;if(hit){ofstream e(dir+"/graph_d3_D10_n1960.edges");e<<N<<" 2940\n";int count=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){e<<u<<' '<<v<<'\n';count++;}assert(count==2940);}
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"COMPLETE_Q7_D10_REQUIRES_PARENT_CHECK":"SOLE_Q7_CONTROL_FAILS_D10")<<"\",\"q\":7,\"target_Delta\":3,\"target_D\":10,\"savedL\":1250,\"n\":1960,\"m\":2940,\"simple\":true,\"undirected\":true,\"regular_degree\":3,\"connected\":true,\"actual_D\":"<<globalD<<",\"BFS_complete\":5,\"diameter_scope\":\"Fivebaseidentityrootsandleftdeckactioncoverallvertices\",\"roots\":[";
 for(int b=0;b<5;b++){if(b)out<<',';out<<"{\"source_base\":"<<b<<",\"root_vertex\":"<<b*G<<",\"eccentricity\":"<<eccs[b]<<",\"R10_missing\":"<<misses[b]<<",\"distance_histogram\":[";for(size_t i=0;i<histograms[b].size();i++){if(i)out<<',';out<<histograms[b][i];}out<<"]}";}
 out<<"],\"normal_orbits_nonzero\":6,\"ordinary_bad_unordered_pairs\":null,\"source360_BFS\":0,\"new_lower_bounds\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 cout<<"q7 exactD="<<globalD<<" roots5 firstbadbase="<<firstbad<<" firstmiss="<<firstmissing<<" hit="<<hit<<" nativeCPU="<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
}

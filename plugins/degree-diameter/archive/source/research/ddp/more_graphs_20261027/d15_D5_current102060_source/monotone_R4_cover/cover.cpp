#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=102060,W=(N+63)/64;
template<class T>void binary(const string&path,const vector<T>&v){ofstream f(path,ios::binary);f.write(reinterpret_cast<const char*>(v.data()),v.size()*sizeof(T));}
int main(int argc,char**argv){
 clock_t start=clock();string mode=argv[1],source=argv[2],dir=argv[3];
 vector<vector<int>>adj(N);ifstream in(source);assert(in);string line;vector<int>seenrow(N);int rows=0;long long arcs=0;
 while(getline(in,line)){if(line.empty()||line[0]=='#')continue;istringstream ss(line);int u,v;assert(ss>>u);assert(u>=0&&u<N&&!seenrow[u]);seenrow[u]=1;rows++;while(ss>>v){assert(v>=0&&v<N);adj[u].push_back(v);arcs++;}}
 assert(rows==N&&arcs==1530090);
 vector<int>pins;ifstream pf(dir+(mode=="build"?"/eligible.txt":"/PINS.txt"));int v;while(pf>>v)pins.push_back(v);
 if(mode=="build"){
  const int R=pins.size(),TW=(R+63)/64;assert(R==810);const double limit=stod(argv[4]);
  vector<uint64_t>balls(size_t(R)*W),transpose(size_t(N)*TW);vector<uint16_t>support(N);vector<int>seen(N),q(N),sizes(R);long long scans=0;int completed=0;
  for(int r=0;r<R;r++){
   if(double(clock()-start)/CLOCKS_PER_SEC>limit)break;
   int root=pins[r];assert(adj[root].size()==14);int lo=0,hi=1;q[0]=root;seen[root]=r+1;
   auto mark=[&](int t){balls[size_t(r)*W+t/64]|=uint64_t(1)<<(t%64);transpose[size_t(t)*TW+r/64]|=uint64_t(1)<<(r%64);support[t]++;};
   mark(root);
   for(int depth=0;depth<4;depth++){
    int end=hi;
    while(lo<end){int u=q[lo++];scans+=adj[u].size();for(int t:adj[u])if(seen[t]!=r+1){seen[t]=r+1;q[hi++]=t;mark(t);}}
   }
   sizes[r]=hi;completed++;
  }
  if(completed!=R){ofstream out(dir+"/NATIVE_PREFLIGHT.json");out<<"{\"status\":\"UNKNOWN_PARTIAL_R4_CPU_LIMIT\",\"completed\":"<<completed<<",\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}
  vector<int>order(R);iota(order.begin(),order.end(),0);auto compare=[&](int a,int b){return memcmp(balls.data()+size_t(a)*W,balls.data()+size_t(b)*W,W*sizeof(uint64_t))<0;};sort(order.begin(),order.end(),compare);
  vector<int>representative(R);int unique=0;
  for(int a=0;a<R;){int b=a+1,rep=order[a];while(b<R&&memcmp(balls.data()+size_t(order[a])*W,balls.data()+size_t(order[b])*W,W*sizeof(uint64_t))==0){rep=min(rep,order[b]);b++;}for(int j=a;j<b;j++)representative[order[j]]=rep;unique++;a=b;}
  binary(dir+"/radius4.u64le.bin",balls);binary(dir+"/target_rows.u64le.bin",transpose);binary(dir+"/target_support.u16le.bin",support);
  vector<uint32_t>csr;csr.reserve(2+N+1+arcs);csr.push_back(N);csr.push_back(arcs);uint32_t off=0;csr.push_back(0);for(const auto&a:adj){off+=a.size();csr.push_back(off);}for(const auto&a:adj)for(int t:a)csr.push_back(t);binary(dir+"/source.csr.u32le.bin",csr);
  int covered=count_if(support.begin(),support.end(),[](int x){return x>0;});vector<int>hist(N+1);for(int x:sizes)hist[x]++;
  ofstream out(dir+"/NATIVE_PREFLIGHT.json");out<<"{\"status\":\"ALL810_R4_COMPLETE\",\"n\":"<<N<<",\"m\":765045,\"eligible\":810,\"words_per_ball\":"<<W<<",\"words_per_target_row\":"<<TW<<",\"completed\":"<<completed<<",\"scanned_arcs_layers0to3\":"<<scans<<",\"all_union\":"<<covered<<",\"minimum_target_support\":"<<*min_element(support.begin(),support.end())<<",\"maximum_target_support\":"<<*max_element(support.begin(),support.end())<<",\"ball_size_min\":"<<*min_element(sizes.begin(),sizes.end())<<",\"ball_size_max\":"<<*max_element(sizes.begin(),sizes.end())<<",\"unique_ball_rows\":"<<unique<<",\"duplicate_ball_rows\":"<<R-unique<<",\"ball_sizes\":[";
  for(int i=0;i<R;i++){if(i)out<<',';out<<sizes[i];}out<<"],\"duplicate_representatives\":[";for(int i=0;i<R;i++){if(i)out<<',';out<<representative[i];}out<<"],\"union_missing_first20\":[";
  int count=0;for(int i=0;i<N&&count<20;i++)if(!support[i]){if(count++)out<<',';out<<i;}out<<"],\"source_BFS_allroots\":0,\"truncated_radius4_roots\":810,\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
  cout<<"ALL810 R4 union "<<covered<<" support "<<*min_element(support.begin(),support.end())<<".."<<*max_element(support.begin(),support.end())<<" ball "<<*min_element(sizes.begin(),sizes.end())<<".."<<*max_element(sizes.begin(),sizes.end())<<" duplicate "<<R-unique<<" scans "<<scans<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
 }else{
  assert(mode=="candidate"&&!pins.empty()&&pins.size()<=15);sort(pins.begin(),pins.end());assert(adjacent_find(pins.begin(),pins.end())==pins.end());for(int x:pins)assert(x>=0&&x<N&&adj[x].size()==14);
  vector<int>dist(N+1,-1),q(N+1);int lo=0,hi=1;dist[N]=0;q[0]=N;
  while(lo<hi){int u=q[lo++];if(u==N){for(int t:pins)if(dist[t]<0){dist[t]=1;q[hi++]=t;}}else{for(int t:adj[u])if(dist[t]<0){dist[t]=dist[u]+1;q[hi++]=t;}}}
  int ecc=*max_element(dist.begin(),dist.end());assert(hi==N+1&&ecc<=5);
  vector<int>hist(ecc+1);for(int d:dist)hist[d]++;
  ofstream edges(dir+"/graph_d15_D5_n102061.edges");edges<<N+1<<' '<<765045+pins.size()<<'\n';long long count=0;for(int u=0;u<N;u++)for(int t:adj[u])if(u<t){edges<<u<<' '<<t<<'\n';count++;}assert(count==765045);for(int x:pins)edges<<x<<' '<<N<<'\n';edges.close();
  ofstream out(dir+"/CANDIDATE_CHECK.json");out<<"{\"status\":\"COMPLETE102061_EXTENSION_REQUIRES_PARENT_ACCEPTANCE\",\"n\":"<<N+1<<",\"m\":"<<765045+pins.size()<<",\"Delta\":15,\"source_edges_all_retained\":true,\"simple\":true,\"newroot\":"<<N<<",\"newroot_visited\":"<<hi<<",\"newroot_eccentricity\":"<<ecc<<",\"source_allroot_BFS\":0,\"newroot_distance_histogram\":[";for(size_t i=0;i<hist.size();i++){if(i)out<<',';out<<hist[i];}out<<"],\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
  cout<<"HIT n "<<N+1<<" m "<<765045+pins.size()<<" root ecc "<<ecc<<" CPU "<<double(clock()-start)/CLOCKS_PER_SEC<<endl;
 }
}

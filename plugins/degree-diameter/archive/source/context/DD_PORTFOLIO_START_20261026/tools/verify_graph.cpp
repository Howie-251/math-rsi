// Finite baseline checker written for this handoff, not a research searcher.
// Input: first line n m; then exactly m unordered edges, vertices 0..n-1.
#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
int main(int argc,char**argv){
 try {
  if(argc!=4)throw std::runtime_error("usage: verify_graph FILE MAX_DEGREE MAX_DIAMETER");
  int cap=std::stoi(argv[2]),D=std::stoi(argv[3]);
  std::ifstream f(argv[1]); if(!f)throw std::runtime_error("cannot open input");
  int n; long long m; if(!(f>>n>>m)||n<1||m<0)throw std::runtime_error("bad n m header");
  auto start=std::chrono::steady_clock::now();
  std::vector<std::vector<int>> adj(n); std::set<std::pair<int,int>> seen;
  for(long long k=0;k<m;k++){
   int u,v; if(!(f>>u>>v)||u<0||v<0||u>=n||v>=n||u==v)throw std::runtime_error("invalid/missing edge");
   if(u>v)std::swap(u,v);
   if(!seen.emplace(u,v).second)throw std::runtime_error("duplicate edge");
   adj[u].push_back(v);adj[v].push_back(u);
  }
  std::string tail;if(f>>tail)throw std::runtime_error("extra input after declared edges");
  int lo=n,hi=0;for(auto&s:adj){lo=std::min(lo,(int)s.size());hi=std::max(hi,(int)s.size());}
  std::vector<int> dist(n),q(n);std::map<int,long long> histogram;
  long long bad=0,unreachable=0;int diameter=0;
  for(int s=0;s<n;s++){
   std::fill(dist.begin(),dist.end(),-1);int head=0,end=0;q[end++]=s;dist[s]=0;
   while(head<end){int u=q[head++];for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;q[end++]=v;}}
   for(int v=0;v<n;v++){
    histogram[dist[v]]++;if(dist[v]>=0)diameter=std::max(diameter,dist[v]);
    if(v>s && dist[v]<0)unreachable++;
    if(v>s && (dist[v]<0||dist[v]>D))bad++;
   }
  }
  bool ok=hi<=cap && bad==0;
  double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<"{\"n\":"<<n<<",\"m\":"<<m<<",\"min_degree\":"<<lo<<",\"max_degree\":"<<hi
  <<",\"diameter\":"<<(unreachable?-1:diameter)<<",\"unreachable_unordered_pairs\":"<<unreachable
  <<",\"bad_unordered_pairs\":"<<bad<<",\"roots_checked\":"<<n<<",\"valid\":"<<(ok?"true":"false")
  <<",\"seconds\":"<<sec<<",\"ordered_distance_histogram\":{";
  bool first=true;for(auto [k,v]:histogram){if(!first)std::cout<<",";first=false;std::cout<<"\""<<k<<"\":"<<v;}
  std::cout<<"}}\n";return ok?0:1;
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}
}

// Independent complete single-edge damage check: remove one edge and run every-source BFS.
// Seven representatives come from the two internal and five cross voltages.
#include <algorithm>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main(int argc,char**argv){
 try{
  if(argc!=5)throw runtime_error("usage: BASELINE DISTANCES_U8 CRITICAL_PAIRS OUTPUT_JSON");
  auto start=chrono::steady_clock::now();clock_t cpu_start=clock();
  ifstream input(argv[1]);int n,m;if(!(input>>n>>m)||n!=2810||m!=9835)throw runtime_error("baseline header");
  vector<pair<int,int>>edges(m);vector<vector<pair<int,int>>>adj(n);map<pair<int,int>,int>edge_ids;
  for(int e=0;e<m;++e){auto&[a,b]=edges[e];if(!(input>>a>>b))throw runtime_error("missing edge");
   adj[a].emplace_back(b,e);adj[b].emplace_back(a,e);edge_ids[edges[e]]=e;}
  vector<unsigned char> baseline(size_t(n)*n);ifstream raw(argv[2],ios::binary);
  raw.read(reinterpret_cast<char*>(baseline.data()),baseline.size());
  if(raw.gcount()!=static_cast<streamsize>(baseline.size())||raw.peek()!=EOF)throw runtime_error("distance file size");
  ifstream pairs(argv[3]);int pn,pm;long long total;
  if(!(pairs>>pn>>pm>>total)||pn!=n||pm!=m)throw runtime_error("pair-list header");
  vector<vector<int>>expected(m);long long count_read=0;
  for(int e=0;e<m;++e){int id,count;if(!(pairs>>id>>count)||id!=e||count<0)throw runtime_error("pair-list line");
   expected[e].resize(count);for(int& code:expected[e])if(!(pairs>>code))throw runtime_error("missing pair code");count_read+=count;}
  string extra;if(count_read!=total||(pairs>>extra))throw runtime_error("pair-list incidence total");
  vector<pair<int,int>> representatives={{0,1176},{1405,2552},{0,1405},{0,1817},{0,2743},{0,1591},{0,1450}};
  vector<string>names={"internal_A","internal_B","cross_identity","cross_412","cross_1338","cross_186","cross_45"};
  ofstream out(argv[4]);out<<"{\"method\":\"single-edge deletion and every-source BFS\",\"representatives\":[";
  vector<int>dist(n),queue(n);bool all_equal=true;
  for(size_t index=0;index<representatives.size();++index){
   auto rep=representatives[index];auto it=edge_ids.find(rep);if(it==edge_ids.end())throw runtime_error("representative edge absent");
   int deleted=it->second;auto one_start=chrono::steady_clock::now();clock_t one_cpu=clock();
   vector<int>actual;map<int,long long>bad_by_original_distance;long long unreachable=0;int diameter=0;
   for(int root=0;root<n;++root){
    fill(dist.begin(),dist.end(),-1);int head=0,end=1;queue[0]=root;dist[root]=0;
    while(head<end){int u=queue[head++];for(auto[v,e]:adj[u])if(e!=deleted&&dist[v]<0){dist[v]=dist[u]+1;queue[end++]=v;}}
    for(int target=root+1;target<n;++target){
     if(dist[target]<0)++unreachable;else diameter=max(diameter,dist[target]);
     if(dist[target]>=0&&dist[target]<=5)continue;
     int dg=baseline[size_t(root)*n+target];bad_by_original_distance[dg]++;
     if(dg<=5)actual.push_back(root*n+target);
    }
   }
   bool equal=actual==expected[deleted];all_equal &= equal;
   if(index)out<<",";
   out<<"{\"orbit\":\""<<names[index]<<"\",\"eid\":"<<deleted<<",\"edge\":["<<rep.first<<","<<rep.second
      <<"],\"roots_checked\":"<<n<<",\"exported_critical_upto5_count\":"<<expected[deleted].size()
      <<",\"bfs_critical_upto5_count\":"<<actual.size()<<",\"full_pair_list_equal\":"<<(equal?"true":"false")
      <<",\"deleted_graph_diameter\":"<<(unreachable?-1:diameter)<<",\"unreachable_unordered_pairs\":"<<unreachable
      <<",\"new_bad_pairs_by_original_distance\":{";
   bool comma=false;for(auto[d,count]:bad_by_original_distance){if(comma)out<<",";comma=true;out<<"\""<<d<<"\":"<<count;}
   out<<"},\"cpu_seconds\":"<<double(clock()-one_cpu)/CLOCKS_PER_SEC
      <<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-one_start).count()<<"}";out.flush();
   cout<<names[index]<<" eid="<<deleted<<" count="<<actual.size()<<" exact="<<equal<<endl;
  }
  out<<"],\"all_seven_exact\":"<<(all_equal?"true":"false")
     <<",\"total_cpu_seconds\":"<<double(clock()-cpu_start)/CLOCKS_PER_SEC
     <<",\"total_wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
  if(!all_equal)return 1;
 }catch(const exception& e){cerr<<e.what()<<"\n";return 2;}
 return 0;
}

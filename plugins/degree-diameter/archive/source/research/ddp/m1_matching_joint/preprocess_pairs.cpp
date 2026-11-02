// Export all distance-five pairs whose every shortest path uses each edge.
// Reuses the saved baseline distance matrix. No graph or parameter search.
#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main(int argc,char**argv){
 try {
  if(argc!=6)throw runtime_error("usage: EDGES DISTANCES_U8 OLD_COUNTS OUTPUT_PAIRS OUTPUT_JSON");
  auto start=chrono::steady_clock::now();clock_t cpu_start=clock();
  ifstream in(argv[1]);int n,m;if(!(in>>n>>m)||n!=2810||m!=9835)throw runtime_error("unexpected baseline size");
  vector<pair<int,int>> edges(m);vector<vector<pair<int,int>>>adj(n);
  for(int eid=0;eid<m;++eid){
   auto& [u,v]=edges[eid];if(!(in>>u>>v)||u<0||u>=v||v>=n)throw runtime_error("invalid edge");
   adj[u].emplace_back(v,eid);adj[v].emplace_back(u,eid);
  }
  string extra;if(in>>extra)throw runtime_error("extra edge input");
  for(auto& row:adj)if(row.size()!=7)throw runtime_error("baseline degree is not seven");
  vector<unsigned char> distances(size_t(n)*n);
  ifstream raw(argv[2],ios::binary);raw.read(reinterpret_cast<char*>(distances.data()),distances.size());
  if(raw.gcount()!=static_cast<streamsize>(distances.size())||raw.peek()!=EOF)throw runtime_error("wrong distance matrix size");
  vector<vector<int>> critical(m);vector<array<int,5>>common(n);vector<int>length(n);
  long long distance_five_pairs=0;
  for(int root=0;root<n;++root){
   auto* d=distances.data()+size_t(root)*n;
   array<vector<int>,6>layers;
   for(int v=0;v<n;++v){if(d[v]>5)throw runtime_error("baseline distance exceeds five");layers[d[v]].push_back(v);}
   if(layers[0]!=vector<int>{root})throw runtime_error("incorrect diagonal distance");
   length[root]=0;
   for(int depth=1;depth<=5;++depth)for(int v:layers[depth]){
    bool first=true;
    for(auto [u,eid]:adj[v])if(d[u]+1==depth){
     if(first){
      length[v]=length[u];copy_n(common[u].begin(),length[u],common[v].begin());
      common[v][length[v]++]=eid;first=false;
     }else{
      int keep=0;
      for(int k=0;k<length[v];++k){
       int e=common[v][k];bool present=e==eid;
       for(int j=0;j<length[u]&&!present;++j)present=common[u][j]==e;
       if(present)common[v][keep++]=e;
      }
      length[v]=keep;
     }
    }
    if(first)throw runtime_error("no shortest-path predecessor");
    if(depth==5 && root<v){
     ++distance_five_pairs;int code=root*n+v;
     for(int j=0;j<length[v];++j)critical[common[v][j]].push_back(code);
    }
   }
  }
  ifstream old(argv[3]);long long total=0;map<int,int>histogram;
  for(int eid=0;eid<m;++eid){
   int u,v,count;if(!(old>>u>>v>>count)||make_pair(u,v)!=edges[eid]||count!=(int)critical[eid].size())
    throw runtime_error("exported pair count disagrees with previous per-edge count");
   if(!is_sorted(critical[eid].begin(),critical[eid].end())||adjacent_find(critical[eid].begin(),critical[eid].end())!=critical[eid].end())
    throw runtime_error("pair list not strictly increasing");
   total+=critical[eid].size();histogram[critical[eid].size()]++;
  }
  if(old>>extra)throw runtime_error("extra previous-count input");
  ofstream output(argv[4]);if(!output)throw runtime_error("cannot write pair lists");
  output<<n<<" "<<m<<" "<<total<<"\n";
  for(int eid=0;eid<m;++eid){output<<eid<<" "<<critical[eid].size();for(int code:critical[eid])output<<" "<<code;output<<"\n";}
  output.close();
  double cpu=double(clock()-cpu_start)/CLOCKS_PER_SEC;
  double wall=chrono::duration<double>(chrono::steady_clock::now()-start).count();
  ofstream summary(argv[5]);summary<<"{\"status\":\"COMPLETE\",\"n\":"<<n<<",\"m\":"<<m
   <<",\"total_incidences\":"<<total<<",\"distance5_unordered_pairs\":"<<distance_five_pairs
   <<",\"all_previous_edge_counts_equal\":true,\"all_lists_sorted_unique\":true,\"critical5_count_histogram\":{";
  bool comma=false;for(auto [count,frequency]:histogram){if(comma)summary<<",";comma=true;summary<<"\""<<count<<"\":"<<frequency;}
  summary<<"},\"cpu_seconds\":"<<cpu<<",\"wall_seconds\":"<<wall<<"}\n";
  cout<<"COMPLETE n="<<n<<" m="<<m<<" total_incidences="<<total<<" cpu="<<cpu<<" wall="<<wall<<endl;
 }catch(const exception& e){cerr<<e.what()<<"\n";return 2;}
 return 0;
}

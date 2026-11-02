// Exact common-edge DP over all walks of length at most k, k=0,...,5.
// Exports all single-edge deletion failures at threshold five. No search.
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
 try{
  if(argc!=7)throw runtime_error("usage: EDGES DISTANCES_U8 OLD_CRITICAL5 OUTPUT_PAIRS OUTPUT_JSON CPU_LIMIT");
  auto start=chrono::steady_clock::now();clock_t cpu_start=clock();
  auto cpu=[&](){return double(clock()-cpu_start)/CLOCKS_PER_SEC;};double limit=stod(argv[6]);
  ifstream input(argv[1]);int n,m;if(!(input>>n>>m)||n!=2810||m!=9835)throw runtime_error("baseline size");
  vector<pair<int,int>>edges(m);vector<vector<pair<int,int>>>adj(n);
  for(int eid=0;eid<m;++eid){auto&[u,v]=edges[eid];if(!(input>>u>>v)||u<0||u>=v||v>=n)throw runtime_error("invalid edge");
   adj[u].emplace_back(v,eid);adj[v].emplace_back(u,eid);}
  vector<unsigned char>matrix(size_t(n)*n);ifstream raw(argv[2],ios::binary);
  raw.read(reinterpret_cast<char*>(matrix.data()),matrix.size());
  if(raw.gcount()!=static_cast<streamsize>(matrix.size())||raw.peek()!=EOF)throw runtime_error("matrix size");
  vector<vector<int>>critical(m);vector<array<int,5>>previous(n),current(n);
  vector<int>previous_size(n),current_size(n);map<int,long long>incidences_by_original_distance;
  for(int root=0;root<n;++root){
   if(cpu()>limit){ofstream status(argv[5]);status<<"{\"status\":\"CPU_LIMIT\",\"roots_completed\":"<<root<<",\"cpu_seconds\":"<<cpu()<<"}\n";
    cerr<<"CPU_LIMIT after roots="<<root<<endl;return 3;}
   const auto* distance=matrix.data()+size_t(root)*n;
   if(distance[root]!=0)throw runtime_error("matrix diagonal");
   fill(previous_size.begin(),previous_size.end(),0);
   // Reachability at layer k is exactly distance[v]<=k. In particular an
   // unreachable empty slot never participates as a reachable empty set.
   for(int k=1;k<=5;++k){
    for(int v=0;v<n;++v){
     if(distance[v]>k){current_size[v]=0;continue;}
     bool first=distance[v]>k-1;
     if(!first){
      current_size[v]=previous_size[v];
      copy_n(previous[v].begin(),previous_size[v],current[v].begin());
      if(current_size[v]==0)continue; // A reachable empty carry forces empty intersection.
     }
     for(auto[u,eid]:adj[v])if(distance[u]<=k-1){
      if(first){
       current_size[v]=previous_size[u];copy_n(previous[u].begin(),previous_size[u],current[v].begin());
       bool already=false;for(int j=0;j<current_size[v];++j)already|=current[v][j]==eid;
       if(!already)current[v][current_size[v]++]=eid;
       first=false;
      }else{
       int keep=0;
       for(int j=0;j<current_size[v];++j){
        int e=current[v][j];bool present=e==eid;
        for(int t=0;t<previous_size[u]&&!present;++t)present=previous[u][t]==e;
        if(present)current[v][keep++]=e;
       }
       current_size[v]=keep;
      }
      if(current_size[v]==0)break;
     }
     if(first)throw runtime_error("no reachable predecessor family");
    }
    previous.swap(current);previous_size.swap(current_size);
   }
   for(int target=root+1;target<n;++target){
    if(distance[target]>5)throw runtime_error("baseline exceeds diameter five");
    int code=root*n+target;
    for(int j=0;j<previous_size[target];++j)critical[previous[target][j]].push_back(code);
    incidences_by_original_distance[distance[target]]+=previous_size[target];
   }
  }
  // The old distance-five lists must be exactly the corresponding slice.
  ifstream old(argv[3]);int on,om;long long old_total;
  if(!(old>>on>>om>>old_total)||on!=n||om!=m)throw runtime_error("old pair header");
  for(int eid=0;eid<m;++eid){
   int id,count;if(!(old>>id>>count)||id!=eid)throw runtime_error("old pair row");vector<int>old_list(count);
   for(int& value:old_list)if(!(old>>value))throw runtime_error("old pair data");
   vector<int>slice;for(int code:critical[eid])if(matrix[code]==5)slice.push_back(code);
   if(slice!=old_list)throw runtime_error("distance-five slice differs from original export");
  }
  long long total=0;map<int,int>hist;
  for(auto& row:critical){
   if(!is_sorted(row.begin(),row.end())||adjacent_find(row.begin(),row.end())!=row.end())throw runtime_error("unsorted/duplicate pair");
   total+=row.size();hist[row.size()]++;
  }
  ofstream output(argv[4]);if(!output)throw runtime_error("cannot write output");output<<n<<" "<<m<<" "<<total<<"\n";
  for(int eid=0;eid<m;++eid){output<<eid<<" "<<critical[eid].size();for(int code:critical[eid])output<<" "<<code;output<<"\n";}output.close();
  ofstream out(argv[5]);out<<"{\"status\":\"COMPLETE\",\"n\":"<<n<<",\"m\":"<<m<<",\"total_incidences\":"<<total
   <<",\"all_distance5_slices_equal_previous_export\":true,\"all_lists_sorted_unique\":true,\"count_histogram\":{";
  bool comma=false;for(auto[count,frequency]:hist){if(comma)out<<",";comma=true;out<<"\""<<count<<"\":"<<frequency;}
  out<<"},\"incidences_by_original_distance\":{";comma=false;
  for(auto[d,count]:incidences_by_original_distance){if(comma)out<<",";comma=true;out<<"\""<<d<<"\":"<<count;}
  double used=cpu(),wall=chrono::duration<double>(chrono::steady_clock::now()-start).count();
  out<<"},\"cpu_seconds\":"<<used<<",\"wall_seconds\":"<<wall<<"}\n";
  cout<<"COMPLETE total_incidences="<<total<<" cpu="<<used<<" wall="<<wall<<endl;
 }catch(const exception& e){cerr<<e.what()<<"\n";return 2;}
 return 0;
}

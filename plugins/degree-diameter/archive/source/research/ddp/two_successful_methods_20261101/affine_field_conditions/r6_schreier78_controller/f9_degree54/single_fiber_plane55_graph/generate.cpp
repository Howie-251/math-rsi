#include <algorithm>
#include <array>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
void need(bool x,const string&s){if(!x)throw runtime_error(s);}
int main(int argc,char**argv){try{
 need(argc==4,"source, ordered interface, output directory arguments required");
 double started=double(clock())/CLOCKS_PER_SEC;
 const int source_n=56862,n=56943,source_m=1535274,m=1539648;
 string out=argv[3];
 array<int,81> centers{};array<array<int,54>,81> predicted{};
 ifstream pins(argv[2]);need(bool(pins),"ordered interface exists");
 for(int j=0;j<81;j++){
  int index,label;need(bool(pins>>index>>centers[j]>>label),"complete center recipe");
  need(index==j&&label==source_n+j,"exact ordered new label");
  for(int k=0;k<54;k++)need(bool(pins>>predicted[j][k]),"complete pin recipe");
  need(is_sorted(predicted[j].begin(),predicted[j].end()),"sorted pins");
  need(adjacent_find(predicted[j].begin(),predicted[j].end())==predicted[j].end(),"distinct54pins");
 }
 int extra;need(!(pins>>extra)&&pins.eof(),"no trailing interface rows");
 vector<int> center_index(source_n,-1),degree(n),load(source_n);
 for(int j=0;j<81;j++){need(0<=centers[j]&&centers[j]<729,"center fiber0");need(center_index[centers[j]]==-1,"distinct centers");center_index[centers[j]]=j;}
 array<vector<int>,81> actual;
 vector<pair<int,int>> edges;edges.reserve(m);
 ifstream source(argv[1]);need(bool(source),"complete immutable source exists");
 pair<int,int> previous={-1,-1};int a,b;
 while(source>>a>>b){
  need(0<=a&&a<b&&b<source_n,"source proper endpoints");need(previous<pair<int,int>{a,b},"source sorted literal stream");previous={a,b};
  edges.push_back({a,b});degree[a]++;degree[b]++;
  if(center_index[a]>=0)actual[center_index[a]].push_back(b);
  if(center_index[b]>=0)actual[center_index[b]].push_back(a);
 }
 need(source.eof()&&edges.size()==source_m,"source complete1535274edge body");
 for(int v=0;v<source_n;v++)need(degree[v]==54,"source literal degree54");
 for(int j=0;j<81;j++){
  sort(actual[j].begin(),actual[j].end());need(actual[j].size()==54,"actual source center degree54");
  need(equal(actual[j].begin(),actual[j].end(),predicted[j].begin()),"every declared pin equals actual immutable sourceN54");
 }
 ofstream prefix(out+"/PREFIX_LOADS.csv");
 prefix<<"j,new_label,center_old_label,pins,min_old_pin_degree_before,max_old_pin_degree_before,max_old_pin_load_after,current_vertices,current_edges,old_only_current_R2_certificate\n";
 int distinct_pins=0;
 for(int j=0;j<81;j++){
  int lo=100,hi=0;
  for(int v:actual[j]){
   lo=min(lo,degree[v]);hi=max(hi,degree[v]);
   need(load[v]==0&&degree[v]==54,"actual current prefix spare pin");
   load[v]++;degree[v]++;degree[source_n+j]++;distinct_pins++;
   edges.push_back({v,source_n+j});
  }
  need(degree[source_n+j]==54,"new literal degree54");
  prefix<<j<<','<<source_n+j<<','<<centers[j]<<",54,"<<lo<<','<<hi<<",1,"<<source_n+j+1<<','<<source_m+54*(j+1)<<",IMMUTABLE_SOURCE_D3_AND_PREVIOUS_CLONE_DETOUR\n";
 }
 need(distinct_pins==4374&&edges.size()==m,"all4374added edges");
 int d54=0,d55=0,loaded=0;
 for(int v=0;v<n;v++){d54+=degree[v]==54;d55+=degree[v]==55;need(degree[v]==54||degree[v]==55,"final degree cap55");}
 for(int v=0;v<source_n;v++){need(load[v]<=1,"old load at most1");loaded+=load[v]==1;}
 need(d54==52569&&d55==4374&&loaded==4374,"predicted degree/load histograms");
 sort(edges.begin(),edges.end());need(adjacent_find(edges.begin(),edges.end())==edges.end(),"complete simple edge list");
 FILE*f=fopen((out+"/graph_d55_D3_n56943.edges").c_str(),"w");need(f!=nullptr,"output opened");
 for(auto [u,v]:edges)fprintf(f,"%d %d\n",u,v);need(fclose(f)==0,"complete output closed");
 cout<<"{\"status\":\"PRODUCTION_PASS\",\"vertices\":"<<n<<",\"edges\":"<<m
 <<",\"retained_source_edges\":"<<source_m<<",\"new_vertices\":81,\"added_edges\":4374,\"new_new_edges\":0,\"ordered_centers\":81,\"literal_immutable_N54_bindings\":81,\"distinct_old_pins\":"<<loaded
 <<",\"max_old_pin_load\":1,\"degree_histogram\":{\"54\":"<<d54<<",\"55\":"<<d55
 <<"},\"actual_current_prefix_degree_checks\":81,\"all_prefix_D3\":\"Old-only source paths and previous-clone detours; PROOF.md\",\"sorted_simple_full_edge_file\":true,\"BFS_solver_Lean_runs\":0,\"generation_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-started<<"}\n";
 return 0;
 }catch(const exception&e){cerr<<"PRODUCTION_FAIL: "<<e.what()<<'\n';return 2;}}

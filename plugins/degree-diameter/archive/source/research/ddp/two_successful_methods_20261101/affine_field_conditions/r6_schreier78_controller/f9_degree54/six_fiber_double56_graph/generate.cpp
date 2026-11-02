#include <algorithm>
#include <array>
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
 need(argc==4,"source, ordered interface, output directory required");
 double started=double(clock())/CLOCKS_PER_SEC;
 constexpr int SN=56862,SM=1535274,C=486,COPIES=2,CN=972,N=57834,M=1587762;
 const array<int,6> U={0,1,2,3,9,15};string out=argv[3];
 array<int,C> centers{};array<array<int,54>,C> predicted{};ifstream pins(argv[2]);need(bool(pins),"interface exists");
 for(int i=0;i<C;i++){
  int index,ui,a,b;need(bool(pins>>index>>ui>>a>>b>>centers[i]),"complete ordered center recipe");
  need(index==i&&ui==i/81&&a==(i%81)/9&&b==i%9,"exact uIndex,a,b order");
  need(0<=centers[i]&&centers[i]<SN&&centers[i]/729==U[ui],"actual original source center fiber");
  need(centers[i]%9==a&&centers[i]/9%9==b,"source coordinate labels");
  for(int k=0;k<54;k++)need(bool(pins>>predicted[i][k]),"complete pin row");
  need(is_sorted(predicted[i].begin(),predicted[i].end()),"sorted immutable pins");
  need(adjacent_find(predicted[i].begin(),predicted[i].end())==predicted[i].end(),"distinct54pins");
 }
 int extra;need(!(pins>>extra)&&pins.eof(),"no trailing input rows");
 vector<int> center_index(SN,-1),degree(N),load(SN),base_load(SN);array<vector<int>,C> actual;
 for(int i=0;i<C;i++){need(center_index[centers[i]]==-1,"distinct486centers");center_index[centers[i]]=i;}
 vector<pair<int,int>> edges;edges.reserve(M);ifstream source(argv[1]);need(bool(source),"immutable original source exists");
 pair<int,int> previous={-1,-1};int a,b;
 while(source>>a>>b){
  need(0<=a&&a<b&&b<SN,"source proper endpoints");need(previous<pair<int,int>{a,b},"source sorted simple stream");previous={a,b};
  edges.emplace_back(a,b);++degree[a];++degree[b];
  if(center_index[a]>=0)actual[center_index[a]].push_back(b);
  if(center_index[b]>=0)actual[center_index[b]].push_back(a);
 }
 need(source.eof()&&edges.size()==SM,"complete1535274old body");
 for(int v=0;v<SN;v++)need(degree[v]==54,"source literal regular54");
 ofstream saved(out+"/ORDERED_SOURCE_PINS.tsv");
 for(int i=0;i<C;i++){
  sort(actual[i].begin(),actual[i].end());need(actual[i].size()==54,"literal source N54");
  need(equal(actual[i].begin(),actual[i].end(),predicted[i].begin()),"declared pins equal actual immutable source N54");
  saved<<i<<' '<<centers[i];
  for(int v:actual[i]){need(++base_load[v]==1,"base neighborhoods disjoint");saved<<' '<<v;}
  saved<<'\n';
 }
 saved.close();need(bool(saved),"actual source pins closed");
 need(count(base_load.begin(),base_load.end(),1)==26244,"base pin union26244");
 ofstream prefix(out+"/PREFIX_LOADS.csv");
 prefix<<"j,copy,base_index,u_index,controller,a,b,new_label,center_old_label,pins,min_old_pin_degree_before,max_old_pin_degree_before,max_old_pin_load_after,current_vertices,current_edges,current_R2_basis\n";
 for(int copy=0;copy<COPIES;copy++)for(int i=0;i<C;i++){
  int j=C*copy+i,label=SN+j,lo=100,hi=0;
  for(int v:actual[i]){
   lo=min(lo,degree[v]);hi=max(hi,degree[v]);
   need(base_load[v]==1&&load[v]==copy&&degree[v]==54+copy,"actual current spare pin at prefix");
   ++load[v];++degree[v];++degree[label];edges.emplace_back(v,label);
  }
  need(degree[label]==54,"new vertex literal degree54");
  prefix<<j<<','<<copy<<','<<i<<','<<i/81<<','<<U[i/81]<<','<<(i%81)/9<<','<<i%9<<','<<label<<','<<centers[i]<<",54,"<<lo<<','<<hi<<','<<copy+1<<','<<label+1<<','<<SM+54*(j+1)<<",IMMUTABLE_SOURCE_WALK_AND_EARLIER_CLONE_DETOUR\n";
 }
 prefix.close();need(bool(prefix),"prefix table closed");
 int d54=0,d56=0,load0=0,load2=0;
 for(int v=0;v<N;v++){d54+=degree[v]==54;d56+=degree[v]==56;need(degree[v]==54||degree[v]==56,"final degree54or56");}
 for(int v=0;v<SN;v++){need(load[v]==2*base_load[v],"every source load equals twice base load");load0+=load[v]==0;load2+=load[v]==2;}
 need(d54==31590&&d56==26244&&load0==30618&&load2==26244,"exact degree and source load histograms");
 need(edges.size()==M,"exact1587762edges");sort(edges.begin(),edges.end());need(adjacent_find(edges.begin(),edges.end())==edges.end(),"complete simple edge list");
 FILE*f=fopen((out+"/graph_d56_D3_n57834.edges").c_str(),"w");need(f!=nullptr,"output opened");
 for(auto [u,v]:edges)fprintf(f,"%d %d\n",u,v);need(fclose(f)==0,"complete file closed");
 cout<<"{\"status\":\"PRODUCER_PASS_AWAIT_FRESH_INDEPENDENT_ACCEPTANCE\",\"vertices\":57834,\"edges\":1587762,\"retained_source_edges\":1535274,\"new_vertices\":972,\"added_edges\":52488,\"new_new_edges\":0,\"ordered_base_centers\":486,\"literal_immutable_N54_bindings\":486,\"distinct_base_pins\":26244,\"copies\":2,\"source_load_histogram\":{\"0\":30618,\"2\":26244},\"degree_histogram\":{\"54\":31590,\"56\":26244},\"actual_current_prefix_degree_checks\":972,\"current_R2_BFS_runs\":0,\"all_prefix_D3\":\"Original source Walk and earlier clone detours;PROOF.md\",\"sorted_simple_full_edge_file\":true,\"edge_file_closed\":true,\"source55_graph_read\":false,\"field_revalidations\":0,\"BFS_solver_Lean_runs\":0,\"generation_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-started<<"}\n";
 return 0;
 }catch(const exception&e){cerr<<"PRODUCTION_FAIL: "<<e.what()<<'\n';return 2;}}

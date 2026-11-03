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
 need(argc==4,"source, fixed interface, output directory required");double start=double(clock())/CLOCKS_PER_SEC;
 constexpr int SN=56862,SM=1535274,C=810,PINS=43740,KMAX=5,MAXN=60912;
 const array<int,10>U={31,32,44,45,59,60,61,72,73,74};string out=argv[3];
 array<int,C>center{};array<array<int,54>,C>predicted{};ifstream input(argv[2]);need(bool(input),"fixed interface input exists");
 for(int i=0;i<C;i++){
  int index,ui,a,b;need(bool(input>>index>>ui>>a>>b>>center[i]),"complete ordered center row");
  need(index==i&&ui==i/81&&a==(i%81)/9&&b==i%9,"exact Uindex,a,b order");
  need(0<=center[i]&&center[i]<SN&&center[i]/729==U[ui]&&center[i]%9==a&&center[i]/9%9==b,"original source center label");
  for(int j=0;j<54;j++)need(bool(input>>predicted[i][j]),"complete54pin row");
  need(is_sorted(predicted[i].begin(),predicted[i].end()),"sorted predicted pin row");
  need(adjacent_find(predicted[i].begin(),predicted[i].end())==predicted[i].end(),"predicted54distinct pins");
 }
 int extra;need(!(input>>extra)&&input.eof(),"no extra input tokens");
 vector<int>center_index(SN,-1),degree(MAXN),load(SN),base_load(SN);array<vector<int>,C>actual;
 for(int i=0;i<C;i++){need(center_index[center[i]]==-1,"810distinct centers");center_index[center[i]]=i;}
 vector<pair<int,int>>edges;edges.reserve(SM+KMAX*PINS);ifstream source(argv[1]);need(bool(source),"original source exists");
 pair<int,int>previous={-1,-1};int a,b;
 while(source>>a>>b){need(0<=a&&a<b&&b<SN&&previous<pair<int,int>{a,b},"proper sorted simple source");previous={a,b};
  edges.emplace_back(a,b);++degree[a];++degree[b];if(center_index[a]>=0)actual[center_index[a]].push_back(b);if(center_index[b]>=0)actual[center_index[b]].push_back(a);}
 need(source.eof()&&edges.size()==SM,"one complete literal source parse");for(int v=0;v<SN;v++)need(degree[v]==54,"source regular54");
 ofstream saved(out+"/ORDERED_SOURCE_PINS.tsv");array<int,78>fiber_count{};
 for(int i=0;i<C;i++){sort(actual[i].begin(),actual[i].end());need(actual[i].size()==54&&equal(actual[i].begin(),actual[i].end(),predicted[i].begin()),"all810actual immutableN54rows equal formula");
  saved<<i<<' '<<center[i];for(int v:actual[i]){need(++base_load[v]==1,"base pin rows pairwise disjoint");++fiber_count[v/729];saved<<' '<<v;}saved<<'\n';}
 saved.close();need(bool(saved),"actual pin table closed");need(count(base_load.begin(),base_load.end(),1)==PINS,"43740distinct base pins");
 int fullfibers=0;for(int n:fiber_count){need(n==0||n==729,"exact complete target fibers");fullfibers+=n==729;}need(fullfibers==60,"60complete target fibers");
 {ofstream pre(out+"/BASE_PRECHECK_RESULT.json");pre<<"{\"status\":\"PASS_810_LITERAL_SOURCE_FULLN54_BINDING_AND_43740_DISJOINT_PINS\",\"source_parses\":1,\"source_edges\":1535274,\"base_centers\":810,\"source_neighbor_size\":54,\"distinct_base_pins\":43740,\"complete_target_fibers\":60,\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";}
 cout<<"BASE_PRECHECK_PASS centers810 pins43740 sourceparse1\n"<<flush;
 ofstream prefix(out+"/PREFIX_LOADS.csv");prefix<<"j,copy,base_index,u_index,controller,a,b,newlabel,center,pins,pin_degree_before,pin_degree_after,old_pin_load_after,current_vertices,current_edges,current_R2_basis\n";
 for(int copy=0;copy<KMAX;copy++){
  for(int i=0;i<C;i++){int j=C*copy+i,label=SN+j;for(int v:actual[i]){need(base_load[v]==1&&load[v]==copy&&degree[v]==54+copy,"actual prefix old pin load and degree");++load[v];++degree[v];++degree[label];edges.emplace_back(v,label);}
   need(degree[label]==54,"new clone degree54");prefix<<j<<','<<copy<<','<<i<<','<<i/81<<','<<U[i/81]<<','<<(i%81)/9<<','<<i%9<<','<<label<<','<<center[i]<<",54,"<<54+copy<<','<<55+copy<<','<<copy+1<<','<<label+1<<','<<SM+54*(j+1)<<",IMMUTABLE_SOURCE_WALK_AND_EARLIER_CLONE_DETOUR\n";}
  int k=copy+1,n=SN+C*k,m=SM+PINS*k,cap=54+k,d54=0,dcap=0,load0=0,loadk=0;
  for(int v=0;v<n;v++){need(degree[v]==54||degree[v]==cap,"each case degree54or54plusk");d54+=degree[v]==54;dcap+=degree[v]==cap;}
  for(int v=0;v<SN;v++){need(load[v]==k*base_load[v],"each old load0ork");load0+=load[v]==0;loadk+=load[v]==k;}
  need(d54==13122+C*k&&dcap==PINS&&load0==13122&&loadk==PINS&&edges.size()==m,"exact case order edges degrees loads");
  sort(edges.begin(),edges.end());need(adjacent_find(edges.begin(),edges.end())==edges.end(),"each case literal simple");
  string stem="d"+to_string(cap)+"_D3_n"+to_string(n),casepath=out+"/cases/d"+to_string(cap)+"_n"+to_string(n);
  FILE*f=fopen((out+"/graphs/"+stem+".edges").c_str(),"w");need(f!=nullptr,"case file open");for(auto[u,v]:edges)fprintf(f,"%d %d\n",u,v);need(fclose(f)==0,"complete case file closed");prefix.flush();need(bool(prefix),"prefix rows flushed");
  {ofstream r(casepath+"/RESULT.json");r<<"{\"status\":\"COMPLETE_CASE_FILE_CLOSED_AWAIT_FRESH_INDEPENDENT_ACCEPTANCE\",\"k\":"<<k<<",\"degree_cap\":"<<cap<<",\"n\":"<<n<<",\"m\":"<<m<<",\"old_edges_retained\":1535274,\"new_vertices\":"<<C*k<<",\"new_edges\":"<<PINS*k<<",\"new_new_edges\":0,\"base_centers\":810,\"literal_baseN54_bindings\":810,\"degree_histogram\":{\"54\":"<<d54<<",\""<<cap<<"\":"<<dcap<<"},\"source_load_histogram\":{\"0\":13122,\""<<k<<"\":43740},\"prefix_degree_checks\":"<<C*k<<",\"sorted_simple_complete_file\":true,\"file_closed\":true,\"BFS_solver_Lean_runs\":0,\"source_parse_count_for_batch\":1,\"graph_file\":\"../../graphs/"<<stem<<".edges\",\"accepted_counts_changed\":false}\n";}
  {ofstream r(casepath+"/TERMINAL.json");r<<"{\"status\":\"CASE_COMPLETE_READY_FOR_FRESH_INDEPENDENT_ACCEPTANCE\",\"running\":false,\"k\":"<<k<<",\"n\":"<<n<<",\"m\":"<<m<<",\"file_closed\":true,\"accepted_counts_changed\":false}\n";}
  cout<<"CASE_READY k="<<k<<" degree="<<cap<<" n="<<n<<" m="<<m<<" file=graphs/"<<stem<<".edges\n"<<flush;
 }
 prefix.close();need(bool(prefix),"all4050prefix rows closed");cout<<"{\"status\":\"FIVE_FIXED_CASES_PRODUCED_SOURCE_PARSED_ONCE\",\"source_parse_count\":1,\"base_centers\":810,\"distinct_base_pins\":43740,\"complete_files\":5,\"max_clones\":4050,\"max_prefix_degree_checks\":4050,\"k6_produced\":false,\"BFS_solver_Lean_runs\":0,\"generation_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
 return 0;
 }catch(const exception&e){cerr<<"PRODUCTION_FAIL: "<<e.what()<<'\n';return 2;}}

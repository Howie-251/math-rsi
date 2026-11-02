#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
const int OLDN=56862, NEWN=56943;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
int mul9(int a,int b){return (a%3*(b%3)+2*(a/3)*(b/3))%3+3*((a%3*(b/3)+a/3*(b%3))%3);}
int main(int argc,char**argv){try{
 need(argc==3,"source and newedge filenames required");double start=double(clock())/CLOCKS_PER_SEC;
 vector<vector<int>>source(OLDN),adj(NEWN);for(auto&x:source)x.reserve(54);for(auto&x:adj)x.reserve(55);
 vector<pair<int,int>>oldedges;oldedges.reserve(1535274);ifstream oldin(argv[1]);need(bool(oldin),"accepted source file readable");int a,b;
 while(oldin>>a>>b){need(0<=a&&a<b&&b<OLDN,"source labels");source[a].push_back(b);source[b].push_back(a);oldedges.push_back({a,b});}
 need(oldin.eof()&&oldedges.size()==1535274,"complete accepted source read");
 array<int,81>centers{};vector<int>load(OLDN,0);ofstream bindings("CENTER_PIN_BINDING.tsv");bindings<<"j\tnewlabel\tcenter\tsource_degree\n";
 for(int aa=0;aa<9;aa++)for(int bb=0;bb<9;bb++){
  int j=9*aa+bb,c=aa+9*bb+81*mul9(4,aa);centers[j]=c;
  sort(source[c].begin(),source[c].end());need(source[c].size()==54,"center sourceN54");for(int p:source[c])load[p]++;
  bindings<<j<<'\t'<<OLDN+j<<'\t'<<c<<"\t54\n";
 }
 int used=0,maxload=0;array<int,78>pinlayers{};
 for(int v=0;v<OLDN;v++){if(load[v]){used++;pinlayers[v/729]++;}maxload=max(maxload,load[v]);}
 need(used==4374&&maxload==1,"81pairwise disjoint immutableN54");
 int sixlayers=0;for(int n:pinlayers)if(n){need(n==729,"full neighboring fiber pin partition");sixlayers++;}need(sixlayers==6,"exactly six pin fibers");
 // The source is already accepted. No old root, old controller, field-law or route checks are run.
 ifstream in(argv[2]);need(bool(in),"new literal file readable");pair<int,int>prev={-1,-1};size_t oldindex=0;int added=0;long long edges=0;
 while(in>>a>>b){
  need(0<=a&&a<b&&b<NEWN,"new labels and no loops");need(prev<pair<int,int>{a,b},"new global strict order/simple");prev={a,b};
  if(b<OLDN){need(oldindex<oldedges.size()&&oldedges[oldindex]==pair<int,int>{a,b},"exact retained old edge body");oldindex++;}
  else {need(a<OLDN,"no new-new edge");int j=b-OLDN;need(binary_search(source[centers[j]].begin(),source[centers[j]].end(),a),"new edge immutable fullN membership");added++;}
  adj[a].push_back(b);adj[b].push_back(a);edges++;
 }
 need(in.eof()&&oldindex==oldedges.size(),"entire source retained exactly");need(edges==1539648&&added==4374,"new exact edge totals");
 array<int,2>dh{};
 for(int v=0;v<NEWN;v++){
  int expected=v<OLDN?54+load[v]:54;need(int(adj[v].size())==expected,"new full literal degree formula");need(expected==54||expected==55,"degree cap55");dh[expected-54]++;
 }
 need(dh[0]==52569&&dh[1]==4374,"degree histogram");
 for(int j=0;j<81;j++){sort(adj[OLDN+j].begin(),adj[OLDN+j].end());need(adj[OLDN+j]==source[centers[j]],"every new literalN exactly sourceN54");}
 double binding=double(clock())/CLOCKS_PER_SEC-start;
 vector<int>marks(NEWN,0),dist(NEWN),queue(NEWN);ofstream csv("NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv");csv<<"newroot,center,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable\n";
 for(int j=0;j<81;j++){
  int root=OLDN+j,stamp=j+1,head=0,tail=1;queue[0]=root;dist[root]=0;marks[root]=stamp;array<int,4>actual={1,0,0,0};
  while(head<tail){int v=queue[head++];if(dist[v]==3)continue;for(int w:adj[v])if(marks[w]!=stamp){marks[w]=stamp;dist[w]=dist[v]+1;queue[tail++]=w;actual[dist[w]]++;}}
  array<int,4>pred={1,54,2477,54411};need(tail==NEWN&&actual==pred,"new-root exact distance prediction");
  csv<<root<<','<<centers[j];for(int z:pred)csv<<','<<z;for(int z:actual)csv<<','<<z;csv<<','<<tail<<'\n';
 }
 double bfs=double(clock())/CLOCKS_PER_SEC-start-binding;
 cout<<"{\"status\":\"PASS\",\"n\":56943,\"m\":"<<edges<<",\"source_edges_retained_exact\":"<<oldindex<<",\"added_edges\":"<<added<<",\"new_vertices\":81,\"new_new_edges\":0,\"immutable_source_fullN_binding\":true,\"distinct_old_pins\":"<<used<<",\"max_old_pin_load\":"<<maxload<<",\"whole_pin_fibers\":"<<sixlayers<<",\"degree_histogram\":{\"54\":"<<dh[0]<<",\"55\":"<<dh[1]<<"},\"new_literal_BFS_roots\":81,\"old_literal_BFS_roots\":0,\"all_newroot_histograms\":[1,54,2477,54411],\"distance_predictions_match\":true,\"all_prefix_D3_immutable_source_proof\":true,\"exact_diameter\":3,\"binding_CPU_seconds\":"<<binding<<",\"new_BFS_CPU_seconds\":"<<bfs<<",\"validator_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
 return 0;
}catch(const exception&e){cerr<<"VALIDATION_FAIL: "<<e.what()<<'\n';return 2;}}

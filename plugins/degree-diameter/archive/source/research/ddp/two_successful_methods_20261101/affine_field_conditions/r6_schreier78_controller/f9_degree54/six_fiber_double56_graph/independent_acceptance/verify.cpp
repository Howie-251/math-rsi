#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int OLDN=56862,NEWN=57834,BASES=486,CLONES=972;
constexpr array<int,6> U={0,1,2,3,9,15};
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
int mul9(int a,int b){return (a%3*(b%3)+2*(a/3)*(b/3))%3+3*((a%3*(b/3)+a/3*(b%3))%3);}
int main(int argc,char**argv){try{
 need(argc==3,"source and new edge filenames required");double begin=double(clock())/CLOCKS_PER_SEC;
 vector<vector<int>>source(OLDN),adj(NEWN);for(auto&x:source)x.reserve(54);for(auto&x:adj)x.reserve(56);
 vector<pair<int,int>>oldedges;oldedges.reserve(1535274);ifstream oldin(argv[1]);need(bool(oldin),"accepted source readable");int a,b;
 while(oldin>>a>>b){need(0<=a&&a<b&&b<OLDN,"source label parse");source[a].push_back(b);source[b].push_back(a);oldedges.push_back({a,b});}
 need(oldin.eof()&&oldedges.size()==1535274,"complete accepted source read");
 array<int,BASES>centers{};vector<int>load(OLDN,0);ofstream recipe("CENTER_PIN_BINDING.tsv");recipe<<"j\tcopy\tbase\tuIndex\tu\ta\tb\tnewlabel\tcenter\tsource_degree\n";
 for(int ui=0;ui<6;ui++)for(int aa=0;aa<9;aa++)for(int bb=0;bb<9;bb++){
  int base=81*ui+9*aa+bb,c=729*U[ui]+aa+9*bb+81*mul9(4,aa);centers[base]=c;
  sort(source[c].begin(),source[c].end());need(source[c].size()==54,"base center immutableN54");for(int p:source[c])load[p]+=2;
  for(int copy=0;copy<2;copy++){int j=486*copy+base;recipe<<j<<'\t'<<copy<<'\t'<<base<<'\t'<<ui<<'\t'<<U[ui]<<'\t'<<aa<<'\t'<<bb<<'\t'<<OLDN+j<<'\t'<<c<<"\t54\n";}
 }
 int used=0,maxload=0;array<int,3>loadhist{};
 for(int v=0;v<OLDN;v++){need(load[v]==0||load[v]==2,"486base neighborhood packing disjoint");loadhist[load[v]]++;if(load[v])used++;maxload=max(maxload,load[v]);}
 need(used==26244&&maxload==2&&loadhist[0]==30618&&loadhist[2]==26244,"expected old load histogram");
 double source_read_and_recipe=double(clock())/CLOCKS_PER_SEC-begin;
 // Explicit old R2-only local enumeration for prediction, not an old R3 BFS.
 double predstart=double(clock())/CLOCKS_PER_SEC;vector<int>oldmark(OLDN,0);array<array<int,4>,BASES>pred{};
 ofstream prediction("BEFORE_NEW_GRAPH_SOURCE_R2_PREDICTIONS.csv");prediction<<"base,center,source_B2,source_R0,source_R1,source_R2,inherited_D3_source_R3,pred_new_R0,pred_new_R1,pred_new_R2,pred_new_R3\n";
 map<array<int,4>,int>predhist;
 for(int base=0;base<BASES;base++){
  int c=centers[base],stamp=base+1,count=1;oldmark[c]=stamp;
  for(int v:source[c])if(oldmark[v]!=stamp){oldmark[v]=stamp;count++;}
  for(int v:source[c])for(int w:source[v])if(oldmark[w]!=stamp){oldmark[w]=stamp;count++;}
  int K=count-55,R3=OLDN-count;pred[base]={1,54,K+2,R3+970};predhist[pred[base]]+=2;
  prediction<<base<<','<<c<<','<<count<<",1,54,"<<K<<','<<R3;for(int x:pred[base])prediction<<','<<x;prediction<<'\n';
 }
 prediction.close();double prediction_cpu=double(clock())/CLOCKS_PER_SEC-predstart;
 // No source field/controller/route/D3 premise check occurs here.
 double newstart=double(clock())/CLOCKS_PER_SEC;ifstream in(argv[2]);need(bool(in),"new complete literal graph readable");pair<int,int>prev={-1,-1};size_t oldindex=0;int added=0;long long edges=0;
 while(in>>a>>b){
  need(0<=a&&a<b&&b<NEWN,"new labels and no loops");need(prev<pair<int,int>{a,b},"strict global ordering/simple");prev={a,b};
  if(b<OLDN){need(oldindex<oldedges.size()&&oldedges[oldindex]==pair<int,int>{a,b},"complete old edge body exact");oldindex++;}
  else{need(a<OLDN,"no new-new edge");int j=b-OLDN,base=j%486;need(binary_search(source[centers[base]].begin(),source[centers[base]].end(),a),"new edge in immutable sourceN54");added++;}
  adj[a].push_back(b);adj[b].push_back(a);edges++;
 }
 need(in.eof()&&oldindex==oldedges.size(),"all old edges retained");need(edges==1587762&&added==52488,"exact total/new edges");array<int,3>degreehist{};
 for(int v=0;v<NEWN;v++){
  int expected=v<OLDN?54+load[v]:54;need(int(adj[v].size())==expected,"complete new literal degree formula");degreehist[expected-54]++;
 }
 need(degreehist[0]==31590&&degreehist[1]==0&&degreehist[2]==26244,"degree histogram");
 for(int j=0;j<CLONES;j++){sort(adj[OLDN+j].begin(),adj[OLDN+j].end());need(adj[OLDN+j]==source[centers[j%486]],"each of972fullN exact source binding");}
 double newbinding=double(clock())/CLOCKS_PER_SEC-newstart;
 double bfsstart=double(clock())/CLOCKS_PER_SEC;vector<int>mark(NEWN,0),dist(NEWN),queue(NEWN);map<array<int,4>,int>actualhist;
 ofstream csv("NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv");csv<<"j,copy,base,newroot,center,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable\n";
 for(int j=0;j<CLONES;j++){
  int root=OLDN+j,base=j%486,stamp=j+1,head=0,tail=1;queue[0]=root;dist[root]=0;mark[root]=stamp;array<int,4>actual={1,0,0,0};
  while(head<tail){int v=queue[head++];if(dist[v]==3)continue;for(int w:adj[v])if(mark[w]!=stamp){mark[w]=stamp;dist[w]=dist[v]+1;queue[tail++]=w;actual[dist[w]]++;}}
  need(tail==NEWN&&actual==pred[base],"new-root actual distance classes differ from prior prediction");actualhist[actual]++;
  csv<<j<<','<<j/486<<','<<base<<','<<root<<','<<centers[base];for(int z:pred[base])csv<<','<<z;for(int z:actual)csv<<','<<z;csv<<','<<tail<<'\n';
 }
 need(actualhist==predhist,"aggregate predicted and actual histograms");ofstream hist("NEW_ROOT_HISTOGRAMS.tsv");hist<<"R0\tR1\tR2\tR3\troots\n";for(auto[h,n]:actualhist){for(int z:h)hist<<z<<'\t';hist<<n<<'\n';}
 double bfs_cpu=double(clock())/CLOCKS_PER_SEC-bfsstart;
 cout<<"{\"status\":\"PASS\",\"n\":57834,\"m\":"<<edges<<",\"source_edges_retained_exact\":"<<oldindex<<",\"added_edges\":"<<added<<",\"base_centers\":486,\"copies_each\":2,\"new_vertices\":972,\"new_new_edges\":0,\"all_972_immutable_source_fullN54_bound\":true,\"distinct_old_pins\":"<<used<<",\"max_old_pin_load\":"<<maxload<<",\"old_load_histogram\":{\"0\":30618,\"2\":26244},\"degree_histogram\":{\"54\":31590,\"56\":26244},\"source_R2_only_prediction_centers\":486,\"source_R2_only_prediction_CPU_seconds\":"<<prediction_cpu<<",\"old_R3_BFS_roots\":0,\"new_literal_R3_BFS_roots\":972,\"every_distance_class_matches_prediction\":true,\"all_prefix_and_all_pairs_D3_proof\":true,\"exact_diameter\":3,\"source_read_recipe_CPU_seconds\":"<<source_read_and_recipe<<",\"new_literal_binding_CPU_seconds\":"<<newbinding<<",\"new_BFS_CPU_seconds\":"<<bfs_cpu<<",\"validator_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-begin<<"}\n";
 return 0;
}catch(const exception&e){cerr<<"VALIDATION_FAIL: "<<e.what()<<'\n';return 2;}}

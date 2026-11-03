#include <algorithm>
#include <array>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int SN=15552,SM=116316,N=16416,K=864,CN=192;
int M=0,sourceReadCount=0,candidateReadCount=0,finalRootCount=0;
double begun,budget;string phase="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-begun;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Reader{FILE*f;array<unsigned char,1<<18>buf;size_t p=0,n=0;
 Reader(const string&s):f(fopen(s.c_str(),"rb")){need(f,"readable candidate");}~Reader(){if(f)fclose(f);}
 int get(){if(p==n){n=fread(buf.data(),1,buf.size(),f);p=0;if(!n)return -1;}return buf[p++];}
 bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}
};
#include "I32_INPUT.hpp"
int main(int argc,char**argv){begun=double(clock())/CLOCKS_PER_SEC;try{
 need(argc==4,"author raw candidate budget");budget=stod(argv[3]);
 phase="one_original_author_adjlist_parse";double t0=cpu();
 vector<vector<int>>S(SN);vector<pair<int,int>>sourceEdges;sourceEdges.reserve(SM);
 ifstream raw(argv[1]);need(bool(raw),"original source readable");sourceReadCount++;string line;int row=0;
 while(getline(raw,line)){istringstream in(line);int u,v;need(bool(in>>u)&&u==row&&u<SN,"ordered headerless author rows");while(in>>v){need(0<=v&&v<SN&&v!=u,"actual simple source row");S[u].push_back(v);}sort(S[u].begin(),S[u].end());need(adjacent_find(S[u].begin(),S[u].end())==S[u].end(),"source duplicate neighbor");row++;}
 need(row==SN,"all original source rows");map<int,int>sourceHist;
 array<array<bool,CN>,CN>projected{};array<bool,CN>holding{};
 for(int u=0;u<SN;u++){sourceHist[S[u].size()]++;for(int v:S[u]){need(binary_search(S[v].begin(),S[v].end(),u),"source reverse literal adjacency");if(u<v){sourceEdges.emplace_back(u,v);int a=u/81,b=v/81;if(a==b)holding[a]=true;else projected[a][b]=projected[b][a]=true;}}}
 need(sourceEdges.size()==SM&&sourceHist==map<int,int>{{14,648},{15,14904}},"actual source edge and degree counts");
 ofstream proj("ACTUAL_SOURCE_CONTROLLER_PROJECTION.tsv");proj<<"controller\tloopless_degree\thas_actual_same_controller_edge\tactual_neighbor_controllers\n";
 int maxControllerDegree=0;map<int,int>controllerHist;
 for(int a=0;a<CN;a++){int d=0;for(int b=0;b<CN;b++)d+=projected[a][b];need(d<=5,"actual source loopless projection maximumdegree5");maxControllerDegree=max(maxControllerDegree,d);controllerHist[d]++;proj<<a<<'\t'<<d<<'\t'<<holding[a]<<'\t';bool first=true;for(int b=0;b<CN;b++)if(projected[a][b]){if(!first)proj<<' ';first=false;proj<<b;}proj<<'\n';}
 double sourceCPU=cpu()-t0;
 phase="independent_ordered864_actual_source_Ns";t0=cpu();
 vector<int>centers(K),load(SN,0),offset(N+1,0),actualNewDegree(K,0);map<int,int>centerHist;int expectedNewEdges=0;
 for(int j=0;j<K;j++){int k=j%27,off=k%3+9*((k/3)%3)+27*(k/9);centers[j]=81*I[j/27]+off;centerHist[S[centers[j]].size()]++;expectedNewEdges+=S[centers[j]].size();for(int v:S[centers[j]]){load[v]++;need(load[v]<=1,"all864 fullN literal pinload<=1");}}
 int pins=0;for(int x:load)pins+=x>0;
 need(pins==expectedNewEdges,"actual864 fullN disjoint pin count");M=SM+expectedNewEdges;
 for(int v=0;v<N;v++){int d=v<SN?int(S[v].size())+load[v]:int(S[centers[v-SN]].size());offset[v+1]=offset[v]+d;}
 need(offset[N]==2*M,"actual prescribed degree sum");vector<int>cursor=offset,CSR(2*M),degree(N,0);
 auto controller=[&](int v){return v<SN?v/81:centers[v-SN]/81;};
 phase="one_complete_candidate_stream";Reader in(argv[2]);candidateReadCount++;int a,b;need(in.integer(a)&&in.integer(b)&&a==N&&b==M,"candidate header");pair<int,int>prior={-1,-1};int oldidx=0,added=0,count=0,staying=0;
 while(in.integer(a)){need(in.integer(b),"complete edge pair");need(0<=a&&a<b&&b<N&&prior<pair<int,int>{a,b},"candidate strictlex/simple body");prior={a,b};
  if(b<SN){need(oldidx<SM&&sourceEdges[oldidx]==pair<int,int>{a,b},"every oldsource edge retained exact");oldidx++;}
  else{need(a<SN,"0newnew edges");int j=b-SN;need(binary_search(S[centers[j]].begin(),S[centers[j]].end(),a),"newedge belongs to actual oldsimpleN, no virtualself reinsertion");actualNewDegree[j]++;added++;}
  int ca=controller(a),cb=controller(b);if(ca==cb)staying++;else need(projected[ca][cb],"all candidate edges project to adjacentcontrollers orholding");
  need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"actual CSR degree capacity");CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;degree[a]++;degree[b]++;count++;
 }
 need(count==M&&oldidx==SM&&added==expectedNewEdges,"literal complete old/newedge counts");
 ofstream bind("ALL864_ACTUAL_ROLE_BINDINGS.tsv");bind<<"j\tcontroller\toffset\told_center_label\tnew_label\tactual_simple_N_size\tactual_edge_count\tfull_N_equal\told_center_excluded\tactual_old_simple_neighbors\n";
 for(int j=0;j<K;j++){int c=centers[j];need(actualNewDegree[j]==int(S[c].size()),"each864 fullN equality by membership/full degree/simple");bind<<j<<'\t'<<c/81<<'\t'<<c%81<<'\t'<<c<<'\t'<<SN+j<<'\t'<<S[c].size()<<'\t'<<actualNewDegree[j]<<"\ttrue\ttrue\t";for(size_t k=0;k<S[c].size();k++){if(k)bind<<' ';bind<<S[c][k];}bind<<'\n';}
 map<int,int>hist;for(int v=0;v<N;v++){need(cursor[v]==offset[v+1]&&degree[v]==offset[v+1]-offset[v],"all actual vertex degrees complete");hist[degree[v]]++;}
 need(hist.rbegin()->first<=16,"complete final maximumdegree<=16");double bindingCPU=cpu()-t0;
 phase="all_final16416_roots_ordinary_BFS_once";t0=cpu();
 vector<int>seen(N,0),dist(N),parent(N),queue(N);long long reachedPairs=0;int complete=0,minOld4=SN,maxOld4=0,minNew3=K,maxNew3=0,minNew4=K,maxNew4=0;bool witnessSaved=false;
 map<string,pair<int,int>>old4Ranges;map<array<int,5>,int>histogramProfiles;
 ofstream csv("ALL16416_FINAL_ROOT_BFS.csv");csv<<"root,kind,degree,pred_ecc,actual_ecc,pred_reached,actual_reached,pred_old_R4_min,actual_old_R4,R0,R1,R2,R3,R4,beyond4,pred_ownoldcenter_distance,actual_ownoldcenter_distance,othernew_le2,othernew_R3,othernew_R4,all_predictions_match\n";
 for(int root=0;root<N;root++){
  need(cpu()<budget,"single cumulative CPU budget");int stamp=root+1,head=0,tail=1,ecc=0,old4=0,beyond4=0;array<int,5>h={1,0,0,0,0};queue[0]=root;seen[root]=stamp;dist[root]=0;parent[root]=-1;
  while(head<tail){int v=queue[head++],dd=dist[v]+1;for(int p=offset[v];p<offset[v+1];p++){int w=CSR[p];if(seen[w]!=stamp){seen[w]=stamp;dist[w]=dd;parent[w]=v;queue[tail++]=w;ecc=max(ecc,dd);if(dd<=4)h[dd]++;else beyond4++;if(w<SN&&dd==4)old4++;}}}
  bool isnew=root>=SN;int own=isnew&&seen[centers[root-SN]]==stamp?dist[centers[root-SN]]:-1,n2=0,n3=0,n4=0;
  for(int z=SN;z<N;z++)if(z!=root&&seen[z]==stamp){n2+=dist[z]<=2;n3+=dist[z]==3;n4+=dist[z]==4;}
  bool match=tail==N&&ecc==4&&old4>=6966&&h[1]==degree[root]&&(!isnew||(own==2&&n2==0&&n3+n4==K-1));
  csv<<root<<','<<(isnew?"new":"old_labelled_in_final")<<','<<degree[root]<<",4,"<<ecc<<','<<N<<','<<tail<<",6966,"<<old4;for(int x:h)csv<<','<<x;csv<<','<<beyond4<<','<<(isnew?2:-1)<<','<<own<<','<<n2<<','<<n3<<','<<n4<<','<<match<<'\n';
  if(!match){csv.flush();ofstream f("PREDICTION_COUNTEREXAMPLE.json");f<<"{\"root\":"<<root<<",\"reached\":"<<tail<<",\"ecc\":"<<ecc<<",\"old_R4\":"<<old4<<",\"ownoldcenter_distance\":"<<own<<",\"othernew_le2\":"<<n2<<"}\n";need(false,"actual finalroot prediction failed; no retry");}
  if(!witnessSaved){int target=-1;for(int z=0;z<SN;z++)if(seen[z]==stamp&&dist[z]==4){target=z;break;}need(target>=0,"oldR4 actual witness");vector<int>walk;for(int z=target;z>=0;z=parent[z])walk.push_back(z);reverse(walk.begin(),walk.end());need(walk.size()==5,"actual genuine4walk length");ofstream f("GENUINE_FOUR_WALK.json");f<<"{\"root\":"<<root<<",\"target\":"<<target<<",\"actual_distance\":4,\"genuine_walk\":[";for(size_t k=0;k<walk.size();k++){if(k)f<<',';f<<walk[k];}f<<"],\"graph\":\"complete_final16416\",\"within_unique_all_final_roots_batch\":true,\"separate_source_BFS\":false}\n";witnessSaved=true;}
  reachedPairs+=tail;complete++;finalRootCount=complete;minOld4=min(minOld4,old4);maxOld4=max(maxOld4,old4);histogramProfiles[h]++;
  if(isnew){minNew3=min(minNew3,n3);maxNew3=max(maxNew3,n3);minNew4=min(minNew4,n4);maxNew4=max(maxNew4,n4);}
  if((root+1)%2048==0)cout<<"BFS_CHECKPOINT roots="<<root+1<<" CPU="<<cpu()<<'\n'<<flush;
 }
 csv.close();need(complete==N&&reachedPairs==1LL*N*N,"complete finalallroots/allorderedpairs");double bfsCPU=cpu()-t0;
 ofstream profiles("ACTUAL_HISTOGRAM_DISTRIBUTIONS.csv");profiles<<"R0,R1,R2,R3,R4,root_count\n";for(auto [h,c]:histogramProfiles){for(int x:h)profiles<<x<<',';profiles<<c<<'\n';}
 ofstream result("RESULT.json");result<<"{\"status\":\"PASS_COMPLETE_LITERAL_AND_ALL16416_FINAL_ROOTS_EXACT_D4\",\"Delta\":"<<hist.rbegin()->first<<",\"D\":4,\"n\":16416,\"m\":"<<M<<",\"source_n\":15552,\"source_m\":116316,\"source_raw_parses\":1,\"candidate_parses\":1,\"all_source_edges_retained_exact\":116316,\"new_edges\":"<<expectedNewEdges<<",\"new_new_edges\":0,\"simple\":true,\"header_body_match\":true,\"ordered_fullN_roles_bound\":864,\"center_degree_histogram\":{\"14\":"<<centerHist[14]<<",\"15\":"<<centerHist[15]<<"},\"distinct_actual_old_pins\":"<<pins<<",\"maximum_old_pin_load\":1,\"all_virtualself_entries_excluded_at_oldcenter\":true,\"degree_histogram\":{\"14\":"<<hist[14]<<",\"15\":"<<hist[15]<<",\"16\":"<<hist[16]<<"},\"actual_loopless_controller_maxdegree\":"<<maxControllerDegree<<",\"controller_projection_edges_all_bound\":"<<M<<",\"holding_projection_edges\":"<<staying<<",\"controller_B3_count_bound\":106,\"predicted_old_R4_lower_bound\":6966,\"actual_min_old_R4\":"<<minOld4<<",\"actual_max_old_R4\":"<<maxOld4<<",\"ordinary_final_graph_BFS_roots\":16416,\"final_old_labelled_roots\":15552,\"final_new_labelled_roots\":864,\"source_only_BFS_roots\":0,\"preliminary_or_duplicate_newroot_BFS\":0,\"actual_allordered_pairs_reached_within4\":"<<reachedPairs<<",\"every_finalroot_eccentricity\":4,\"all_newroot_ownoldcenter_distance\":2,\"all_newroot_other863new_distance3or4\":true,\"newroot_othernew_R3_range\":["<<minNew3<<','<<maxNew3<<"],\"newroot_othernew_R4_range\":["<<minNew4<<','<<maxNew4<<"],\"root_prediction_mismatches\":0,\"distance_histogram_profile_count\":"<<histogramProfiles.size()<<",\"allroot_CSV\":\"ALL16416_FINAL_ROOT_BFS.csv\",\"genuine4_witness\":\"GENUINE_FOUR_WALK.json\",\"fullN_bindings\":\"ALL864_ACTUAL_ROLE_BINDINGS.tsv\",\"source_projection_binding\":\"ACTUAL_SOURCE_CONTROLLER_PROJECTION.tsv\",\"source_D4_also_follows_by_retraction_from_actual_final_allroot_BFS\":true,\"source_parse_and_projection_CPU_seconds\":"<<sourceCPU<<",\"candidate_and_fullN_binding_CPU_seconds\":"<<bindingCPU<<",\"all_final16416_BFS_CPU_seconds\":"<<bfsCPU<<",\"validator_CPU_seconds\":"<<cpu()<<",\"field_rank_older_verifier_source_BFS_Lean_solver_queries_paidreview_runs\":0,\"producer_neighborhood_cache_used\":false,\"I32_input\":\"FROZEN_I32_INPUT.json\",\"global_priority\":\"UNKNOWN\",\"root_counts_modified\":false}\n";
 cout<<"ALL_FINAL_ROOTS_PASS roots="<<complete<<" oldR4="<<minOld4<<".."<<maxOld4<<" CPU="<<cpu()<<'\n'<<flush;return 0;
 }catch(const exception&e){ofstream("FAILURE.json")<<"{\"status\":\"FAIL_OR_BUDGET_UNKNOWN\",\"phase\":\""<<phase<<"\",\"message\":\""<<e.what()<<"\",\"validator_CPU_seconds\":"<<cpu()<<",\"source_raw_parses\":"<<sourceReadCount<<",\"candidate_parses\":"<<candidateReadCount<<",\"ordinary_final_graph_BFS_roots_completed\":"<<finalRootCount<<"}\n";cerr<<phase<<": "<<e.what()<<'\n';return 2;}
}

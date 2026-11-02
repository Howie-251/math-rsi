#include <algorithm>
#include <array>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int OLDN=56862,BASES=810;
constexpr array<int,10>U={31,32,44,45,59,60,61,72,73,74};
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
double now(){return double(clock())/CLOCKS_PER_SEC;}
int mul9(int a,int b){return (a%3*(b%3)+2*(a/3)*(b/3))%3+3*((a%3*(b/3)+a/3*(b%3))%3);}
string hist_json(const map<array<int,4>,int>&h){ostringstream s;s<<'[';bool comma=false;for(auto [x,n]:h){if(comma)s<<',';comma=true;s<<"{\"histogram\":["<<x[0]<<','<<x[1]<<','<<x[2]<<','<<x[3]<<"],\"roots\":"<<n<<'}';}s<<']';return s.str();}
int main(int argc,char**argv){try{
 need(argc==4,"source file, graph directory, CPU budget required");double begin=now(),budget=stod(argv[3]);
 vector<vector<int>>source(OLDN);for(auto&ns:source)ns.reserve(54);vector<pair<int,int>>oldedges;oldedges.reserve(1535274);ifstream oldin(argv[1]);need(bool(oldin),"accepted source readable");int a,b;
 while(oldin>>a>>b){need(0<=a&&a<b&&b<OLDN,"source parse labels");source[a].push_back(b);source[b].push_back(a);oldedges.push_back({a,b});}
 need(oldin.eof()&&oldedges.size()==1535274,"complete accepted source parsed once");oldin.close();
 array<int,BASES>centers{};vector<int>baseLoad(OLDN,0),centerSet(OLDN,0);ofstream basefile("CENTER_BASE_BINDING.tsv");basefile<<"base\tuIndex\tu\ta\tb\tcenter\tsource_degree\n";
 for(int ui=0;ui<10;ui++)for(int aa=0;aa<9;aa++)for(int bb=0;bb<9;bb++){
  int h=81*ui+9*aa+bb,c=729*U[ui]+aa+9*bb+81*mul9(4,aa);centers[h]=c;need(!centerSet[c],"810 distinct center labels");centerSet[c]=1;
  sort(source[c].begin(),source[c].end());need(source[c].size()==54,"810 center source N54");for(int p:source[c])baseLoad[p]++;
  basefile<<h<<'\t'<<ui<<'\t'<<U[ui]<<'\t'<<aa<<'\t'<<bb<<'\t'<<c<<"\t54\n";
 }
 int used=0,inducedIncidence=0;for(int v=0;v<OLDN;v++){need(baseLoad[v]<=1,"810 base neighborhoods pairwise disjoint");used+=baseLoad[v];}
 need(used==43740,"43740distinct base pins");
 for(int c:centers){int n=0;for(int v:source[c])n+=centerSet[v];need(n==1,"center induced matching one neighbor");inducedIncidence+=n;}
 need(inducedIncidence==810,"405 induced source-center edges");
 double source_read_recipe=now()-begin,predbegin=now();vector<int>oldmark(OLDN,0);array<int,BASES>oldR2{},oldR3{};map<int,int>sourceR2distribution;
 ofstream predictions("BEFORE_ANY_NEW_FILE_SOURCE_R2_PREDICTIONS.csv");predictions<<"base,center,source_B2,source_R2,inherited_D3_source_R3\n";
 for(int h=0;h<BASES;h++){
  int c=centers[h],stamp=h+1,B2=1;oldmark[c]=stamp;
  for(int v:source[c])if(oldmark[v]!=stamp){oldmark[v]=stamp;B2++;}
  for(int v:source[c])for(int w:source[v])if(oldmark[w]!=stamp){oldmark[w]=stamp;B2++;}
  oldR2[h]=B2-55;oldR3[h]=OLDN-B2;sourceR2distribution[oldR2[h]]++;
  predictions<<h<<','<<c<<','<<B2<<','<<oldR2[h]<<','<<oldR3[h]<<'\n';
 }
 predictions.close();double prediction_cpu=now()-predbegin;
 vector<string>caseResults;int totalBFS=0;bool pilot_continued=false;
 for(int k=1;k<=5;k++){
  double casebegin=now();int count=810*k,N=OLDN+count,degree=54+k;long long M=1535274+43740LL*k;string name="d"+to_string(degree)+"_n"+to_string(N),path="cases/"+name;filesystem::create_directories(path);
  string filename=string(argv[2])+"/d"+to_string(degree)+"_D3_n"+to_string(N)+".edges";
  vector<vector<int>>adj(N);for(auto&ns:adj)ns.reserve(degree);ifstream in(filename);need(bool(in),"new graph file readable: "+filename);pair<int,int>prev={-1,-1};size_t oldindex=0;long long edges=0;int added=0;
  while(in>>a>>b){
   need(0<=a&&a<b&&b<N,"new vertex labels/no loops");need(prev<pair<int,int>{a,b},"strict global ordering/simple");prev={a,b};
   if(b<OLDN){need(oldindex<oldedges.size()&&oldedges[oldindex]==pair<int,int>{a,b},"old body exact forcase "+name);oldindex++;}
   else{need(a<OLDN,"no new-new edge");int j=b-OLDN;need(binary_search(source[centers[j%810]].begin(),source[centers[j%810]].end(),a),"immutable sourceN54 membership");added++;}
   adj[a].push_back(b);adj[b].push_back(a);edges++;
  }
  need(in.eof()&&oldindex==oldedges.size()&&edges==M&&added==43740*k,"case complete exact edge totals");in.close();
  int high=0,low=0;for(int v=0;v<N;v++){
   int expected=v<OLDN?54+k*baseLoad[v]:54;need(int(adj[v].size())==expected,"case all literal degree formula");if(expected==54)low++;else if(expected==degree)high++;else need(false,"unexpected degree");
  }
  need(high==43740&&low==13122+count,"case degree histogram");ofstream recipe(path+"/ORDERED_CLONE_BINDING.tsv");recipe<<"j\tcopy\tbase\tcenter\tnewlabel\tsource_degree\n";
  for(int j=0;j<count;j++){sort(adj[OLDN+j].begin(),adj[OLDN+j].end());need(adj[OLDN+j]==source[centers[j%810]],"every new literalN54 exact");recipe<<j<<'\t'<<j/810<<'\t'<<j%810<<'\t'<<centers[j%810]<<'\t'<<OLDN+j<<"\t54\n";}
  double binding_cpu=now()-casebegin,bfsbegin=now();vector<int>mark(N,0),dist(N),queue(N);map<array<int,4>,int>hist;
  ofstream csv(path+"/NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv");csv<<"j,copy,base,newroot,center,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable\n";
  for(int j=0;j<count;j++){
   need((j%64)!=0||now()-begin<budget,"global CPU budget guard during new-root BFS");
   int root=OLDN+j,h=j%810,stamp=j+1,head=0,tail=1;queue[0]=root;dist[root]=0;mark[root]=stamp;array<int,4>actual={1,0,0,0},pred={1,54,oldR2[h]+k,oldR3[h]+809*k};
   while(head<tail){int v=queue[head++];if(dist[v]==3)continue;for(int w:adj[v])if(mark[w]!=stamp){mark[w]=stamp;dist[w]=dist[v]+1;queue[tail++]=w;actual[dist[w]]++;}}
   need(tail==N&&actual==pred,"case new-root distance prediction mismatch");hist[actual]++;
   csv<<j<<','<<j/810<<','<<h<<','<<root<<','<<centers[h];for(int z:pred)csv<<','<<z;for(int z:actual)csv<<','<<z;csv<<','<<tail<<'\n';
  }
  csv.close();totalBFS+=count;double bfs_cpu=now()-bfsbegin,case_cpu=now()-casebegin;
  ostringstream result;result<<"{\"status\":\"PASS\",\"case\":\""<<name<<"\",\"k\":"<<k<<",\"degree_cap\":"<<degree<<",\"n\":"<<N<<",\"m\":"<<M<<",\"old_edges_exact\":1535274,\"new_old_edges\":"<<added<<",\"new_new_edges\":0,\"new_vertices\":"<<count<<",\"every_new_N54_bound\":true,\"old_load_zero\":13122,\"old_load_k\":43740,\"degree54_count\":"<<low<<",\"high_degree_count\":"<<high<<",\"new_literal_R3_BFS_roots\":"<<count<<",\"old_R3_BFS_roots\":0,\"all_distance_classes_match\":true,\"actual_histogram_distribution\":"<<hist_json(hist)<<",\"binding_CPU_seconds\":"<<binding_cpu<<",\"new_BFS_CPU_seconds\":"<<bfs_cpu<<",\"case_CPU_seconds\":"<<case_cpu<<",\"all_pairs_and_prefix_proof\":true,\"exact_diameter\":3}";
  string r=result.str();caseResults.push_back(r);ofstream(path+"/RESULT.json")<<r<<'\n';ofstream(path+"/TERMINAL.json")<<"{\"status\":\"PASS\",\"k\":"<<k<<",\"all_case_work_terminal\":true,\"case_CPU_seconds\":"<<case_cpu<<",\"result\":"<<r<<"}\n";
  cout<<"CASE_PASS "<<name<<" newroots="<<count<<" CPU="<<case_cpu<<'\n'<<flush;
  if(k==1){
   double projected_remaining=1.5*(binding_cpu*4+bfs_cpu/810*11340)+1.0,remaining=budget-(now()-begin);pilot_continued=projected_remaining<remaining;
   ofstream pilot("PILOT_RESULT.json");pilot<<"{\"status\":\""<<(pilot_continued?"CONTINUE_WITHIN_BUDGET":"STOP_PROJECTED_BUDGET_EXCEEDS_CAP")<<"\",\"pilot_newroots\":810,\"binding_CPU_seconds\":"<<binding_cpu<<",\"BFS_CPU_seconds\":"<<bfs_cpu<<",\"projected_remaining_CPU_with_1_5_factor_and_1second_buffer\":"<<projected_remaining<<",\"remaining_validator_budget\":"<<remaining<<",\"remaining_newroots\":11340}\n";
   if(!pilot_continued)break;
  }
 }
 ofstream out("RESULT.json");out<<"{\"status\":\""<<(caseResults.size()==5?"PASS_ALL_FIVE_COMPLETE_GRAPHS":"PARTIAL_PILOT_BUDGET_STOP")<<"\",\"source_literal_parse_count\":1,\"source_R2_only_centers\":810,\"source_R2_prediction_runs\":1,\"source_R2_prediction_CPU_seconds\":"<<prediction_cpu<<",\"source_read_and_recipe_CPU_seconds\":"<<source_read_recipe<<",\"source_induced_center_matching_edges\":405,\"distinct_base_pins\":43740,\"old_R3_BFS_roots\":0,\"old_field_controller_checks\":0,\"total_new_R3_BFS_roots\":"<<totalBFS<<",\"pilot_continued_within_budget\":"<<(pilot_continued?"true":"false")<<",\"validator_CPU_seconds\":"<<now()-begin<<",\"cases\":[";for(size_t i=0;i<caseResults.size();i++){if(i)out<<',';out<<caseResults[i];}out<<"]}\n";
 return caseResults.size()==5?0:3;
}catch(const exception&e){cerr<<"VALIDATION_FAIL: "<<e.what()<<'\n';return 2;}}

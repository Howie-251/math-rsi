#include <algorithm>
#include <ctime>
#include <fstream>
#include <iostream>
#include <queue>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
const int N=360, NN=361, D=8;
clock_t started;
double cap;
double cpu(){return double(clock()-started)/CLOCKS_PER_SEC;}
struct Search{vector<int>d,p;int reached=0,ecc=0;};
Search bfs(const vector<vector<int>>&a,int root,int only=-1){
 Search b; b.d.assign(a.size(),-1);b.p.assign(a.size(),-1);
 queue<int>q;b.d[root]=0;q.push(root);
 while(!q.empty()){
  int u=q.front();q.pop();++b.reached;b.ecc=max(b.ecc,b.d[u]);
  if(u==only)break;
  for(int v:a[u])if(b.d[v]<0){b.d[v]=b.d[u]+1;b.p[v]=u;q.push(v);}
 }
 return b;
}
vector<int> path(const Search&b,int source,int target){
 vector<int>p;if(b.d[target]<0)return p;
 for(int v=target;v>=0;v=b.p[v]){p.push_back(v);if(v==source)break;}
 reverse(p.begin(),p.end());return p;
}
void arr(ostream&o,const vector<int>&v){o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';}
vector<int> rawpath(vector<int>p){for(int&v:p)++v;return p;}
void failure(const string&file,const string&stage,pair<int,int>e,int source,int target,
 const Search&b,const vector<vector<int>>&original,bool diagnostic){
 ofstream o(file);o<<"{\n\"stage\":\""<<stage<<"\",\n\"removed_edge_normalized\":["<<e.first<<','<<e.second<<"],\n\"removed_edge_raw\":["<<e.first+1<<','<<e.second+1<<"],\n\"inserted_normalized_newlabel\":360,\n\"added_edges\":[["<<e.first<<",360],["<<e.second<<",360]],\n\"failed_source\":"<<source<<",\n\"failed_target\":"<<target<<",\n\"distance\":"<<b.d[target]<<",\n\"actual_final_shortest_path_normalized\":";
 vector<int>p=path(b,source,target);arr(o,p);o<<",\n\"actual_final_shortest_path_raw_old1to360_new361\":";arr(o,rawpath(p));
 if(diagnostic){
  Search old=bfs(original,source,target);vector<int>oldp=path(old,source,target);bool uses=false;
  for(size_t i=1;i<oldp.size();++i)if(minmax(oldp[i-1],oldp[i])==minmax(e.first,e.second))uses=true;
  o<<",\n\"one_old_source_pair_diagnostic\":{\"source\":"<<source<<",\"target\":"<<target<<",\"distance\":"<<old.d[target]<<",\"shortest_path_normalized\":";arr(o,oldp);
  o<<",\"shortest_path_raw\":";arr(o,rawpath(oldp));o<<",\"uses_removed_edge\":"<<(uses?"true":"false")<<",\"scope\":\"one old pair diagnostic only,not sourceD8 verification\"}";
 }
 o<<"\n}\n";
}
int main(int argc,char**argv){
 started=clock();cap=stod(argv[2]);string out=argv[3];
 int parsed=0,m=0,startedCandidates=0,finished=0,newReject=0,oldReject=0,newPass=0;
 int newBFS=0,oldBFS=0,pairDiagnostic=0;bool full=false,hit=false,budget=false,upper=true;
 bool firstNew=false,firstOld=false,predTested=false,predSupported=false;
 string error,status;pair<int,int>hitEdge={-1,-1};vector<int>hitEcc;
 ofstream attempts(out+"/ATTEMPTS.csv");
 attempts<<"index,raw_u,raw_v,u,v,stage,failed_source,failed_target,distance,reached,newroot_eccentricity,old_label_BFS_completed\n";
 try{
  if(argc!=4)throw runtime_error("expected literal,CPUcap,outputdir");
  ifstream input(argv[1]);if(!input)throw runtime_error("source literal unavailable");++parsed;
  vector<vector<int>>original(N);vector<bool>seen(N,false);set<pair<int,int>>unique;string line;int rows=0;
  while(getline(input,line)){
   size_t first=line.find_first_not_of(" \t\r");if(first==string::npos||line[first]=='#')continue;
   istringstream s(line);int rawu;if(!(s>>rawu)||rawu<1||rawu>N)throw runtime_error("invalid source row label");
   int u=rawu-1;if(seen[u])throw runtime_error("duplicate source row");seen[u]=true;++rows;int rawv;
   while(s>>rawv){
    if(rawv<1||rawv>N||rawv==rawu)throw runtime_error("invalid source neighbor");
    int v=rawv-1;if(u>=v)upper=false;auto e=make_pair(min(u,v),max(u,v));
    if(!unique.insert(e).second)throw runtime_error("duplicate undirected source edge");
    original[u].push_back(v);original[v].push_back(u);
   }
   if(!s.eof())throw runtime_error("nonnumeric source adjacency field");
  }
  if(rows!=N||unique.size()!=540)throw runtime_error("source not expected360/540 single-occurrence undirected adjacency");
  for(auto&a:original){sort(a.begin(),a.end());if(a.size()!=3)throw runtime_error("source not3regular");}
  m=unique.size();
  ofstream parsedSource(out+"/NORMALIZED_SOURCE_INPUT.edges");
  for(auto e:unique)parsedSource<<e.first<<' '<<e.second<<'\n';
  parsedSource.close();
  vector<pair<int,int>>edges(unique.begin(),unique.end());pair<int,int>prediction={0,140};
  auto it=find(edges.begin(),edges.end(),prediction);if(it==edges.end())throw runtime_error("predicted literal edge missing");
  rotate(edges.begin(),it,it+1);
  for(auto e:edges){
   if(cpu()>=cap){budget=true;break;}++startedCandidates;
   auto a=original;a.resize(NN);
   for(auto uv:{make_pair(e.first,e.second),make_pair(e.second,e.first)}){
    auto&neigh=a[uv.first];neigh.erase(find(neigh.begin(),neigh.end(),uv.second));neigh.push_back(N);
   }
   a[N]={e.first,e.second};
   Search nr=bfs(a,N);++newBFS;int target=-1;
   for(int x=0;x<N;++x)if(nr.d[x]<0||nr.d[x]>D){target=x;break;}
   if(e==prediction){predTested=true;predSupported=target<0;}
   if(target>=0){
    ++newReject;++finished;
    attempts<<startedCandidates<<','<<e.first+1<<','<<e.second+1<<','<<e.first<<','<<e.second<<",FAIL_NEWROOT_R8,360,"<<target<<','<<nr.d[target]<<','<<nr.reached<<','<<nr.ecc<<",0\n";
    if(!firstNew){failure(out+"/FIRST_NEWROOT_FAILURE.json","FAIL_NEWROOT_R8",e,N,target,nr,original,false);firstNew=true;}
    continue;
   }
   ++newPass;bool failed=false,incomplete=false;int candidateOld=0;vector<int>ecc;
   for(int root=0;root<N;++root){
    if(cpu()>=cap){incomplete=true;budget=true;break;}
    Search b=bfs(a,root);++oldBFS;++candidateOld;ecc.push_back(b.ecc);target=-1;
    for(int x=0;x<N;++x)if(b.d[x]<0||b.d[x]>D){target=x;break;}
    if(target>=0){
     ++oldReject;++finished;failed=true;
     attempts<<startedCandidates<<','<<e.first+1<<','<<e.second+1<<','<<e.first<<','<<e.second<<",FAIL_OLDOLD_D8,"<<root<<','<<target<<','<<b.d[target]<<','<<b.reached<<','<<nr.ecc<<','<<candidateOld<<'\n';
     if(!firstOld){failure(out+"/FIRST_OLDOLD_FAILURE.json","FAIL_OLDOLD_D8",e,root,target,b,original,true);++pairDiagnostic;firstOld=true;}
     break;
    }
   }
   if(incomplete){attempts<<startedCandidates<<','<<e.first+1<<','<<e.second+1<<','<<e.first<<','<<e.second<<",INCOMPLETE_CPU,-1,-1,-1,-1,"<<nr.ecc<<','<<candidateOld<<'\n';break;}
   if(failed)continue;
   hit=true;++finished;hitEdge=e;hitEcc=ecc;hitEcc.push_back(nr.ecc);
   attempts<<startedCandidates<<','<<e.first+1<<','<<e.second+1<<','<<e.first<<','<<e.second<<",COMPLETE_HIT,-1,-1,-1,361,"<<nr.ecc<<','<<candidateOld<<'\n';
   ofstream graph(out+"/graph_d3_D8_n361.edges");
   for(int u=0;u<NN;++u)for(int v:a[u])if(u<v)graph<<u<<' '<<v<<'\n';
   ofstream params(out+"/PARAMETERS.json");params<<"{\"source_n\":360,\"source_m\":540,\"n\":361,\"m\":541,\"max_degree\":3,\"newroot_degree\":2,\"source_raw_to_normalized\":\"raw minus1\",\"newlabel\":360,\"removed_edge_normalized\":["<<e.first<<','<<e.second<<"],\"removed_edge_raw\":["<<e.first+1<<','<<e.second+1<<"],\"added_edges\":[["<<e.first<<",360],["<<e.second<<",360]],\"root_independent_acceptance\":\"PENDING\"}\n";
   ofstream stats(out+"/ALLROOT_STATS.json");stats<<"{\"root_count\":361,\"eccentricities_by_normalized_root\":";arr(stats,hitEcc);stats<<",\"actual_diameter\":"<<*max_element(hitEcc.begin(),hitEcc.end())<<"}\n";
   cout<<"COMPLETE361_HIT saved; root acceptance required\n";break;
  }
  full=!hit&&!budget&&finished==540;
  status=hit?"COMPLETE_CANDIDATE_361_PENDING_ROOT_ACCEPTANCE":full?"COMPLETE_NO_FIXED_CHEN360_ALL540_SINGLE_SUBDIVISIONS":"UNKNOWN_CPU_CAP_INCOMPLETE_FAMILY";
 }catch(const exception&e){error=e.what();status="STOP_SOURCE_INPUT_OR_RUNTIME_ERROR";}
 attempts.close();ofstream r(out+"/RAW_RESULT.json");
 r<<"{\n\"status\":\""<<status<<"\",\n\"error\":\""<<error<<"\",\n\"source_literal_parses\":"<<parsed<<",\n\"source_n\":360,\n\"source_m\":"<<m<<",\n\"necessary_source_format_simple_cubic_upperadj_pass\":"<<(m==540?"true":"false")<<",\n\"source_D8_validation_BFS\":0,\n\"source_raw_to_normalized\":\"raw1..360 minus1 gives0..359;newlabel360\",\n\"planned_oldedge_count\":540,\n\"candidates_started\":"<<startedCandidates<<",\n\"candidates_finished\":"<<finished<<",\n\"rejected_newroot_R8\":"<<newReject<<",\n\"newroot_R8_passed\":"<<newPass<<",\n\"rejected_old_old_D8\":"<<oldReject<<",\n\"candidate_newroot_BFS_count\":"<<newBFS<<",\n\"candidate_old_label_BFS_count\":"<<oldBFS<<",\n\"one_old_source_pair_diagnostic_BFS_count\":"<<pairDiagnostic<<",\n\"first_newroot_failure_saved\":"<<(firstNew?"true":"false")<<",\n\"first_oldold_failure_saved\":"<<(firstOld?"true":"false")<<",\n\"first_edge_raw\":[1,141],\n\"prediction_first_edge_newroot_tested\":"<<(predTested?"true":"false")<<",\n\"prediction_first_edge_newroot_supported\":"<<(predSupported?"true":"false")<<",\n\"hit\":"<<(hit?"true":"false")<<",\n\"whole_fixed_source_single_subdivision_family_excluded\":"<<(full?"true":"false")<<",\n\"all540_oldedges_explicit_no_symmetry_inference\":"<<(full?"true":"false")<<",\n\"time_cap_reached\":"<<(budget?"true":"false")<<",\n\"run_process_CPU_seconds\":"<<cpu()<<",\n\"scope\":\"Only this fixed primary Chen360 graph,one deleted oldedge replaced by a length2 path through one newvertex;not other edits/sources or general3D8\"\n}\n";
 return error.empty()?0:1;
}

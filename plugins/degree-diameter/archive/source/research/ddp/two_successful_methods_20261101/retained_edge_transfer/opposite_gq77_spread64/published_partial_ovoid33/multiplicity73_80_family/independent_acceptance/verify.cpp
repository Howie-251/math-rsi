// SUPERSEDED, UNEXECUTED DRAFT. Do not compile or run this k16 version.
// Actual accepted scope is multiplicity73_79_family/independent_acceptance/, k9..15.
#include <algorithm>
#include <array>
#include <cstdio>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include "center_input.h"
using namespace std;
constexpr int OLDN=160050,BASES=1650,OLDM=5121600;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
double now(){return double(clock())/CLOCKS_PER_SEC;}
struct Reader{
 FILE*f;array<unsigned char,1<<20>buf;size_t pos=0,len=0;
 explicit Reader(const string&p):f(fopen(p.c_str(),"rb")){need(f!=nullptr,"literal input readable: "+p);}
 ~Reader(){if(f)fclose(f);}
 int get(){if(pos==len){len=fread(buf.data(),1,buf.size(),f);pos=0;if(!len)return -1;}return buf[pos++];}
 bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer file syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}
};
string histjson(const map<array<int,4>,int>&h){ostringstream s;s<<'[';bool comma=false;for(auto[a,n]:h){if(comma)s<<',';comma=true;s<<"{\"histogram\":["<<a[0]<<','<<a[1]<<','<<a[2]<<','<<a[3]<<"],\"roots\":"<<n<<'}';}s<<']';return s.str();}
int main(int argc,char**argv){try{
 need(argc==4,"source file, graph directory, CPU budget arguments");double begin=now(),budget=stod(argv[3]);
 vector<vector<int>>source(OLDN);for(auto&ns:source)ns.reserve(64);vector<pair<int,int>>oldedges;oldedges.reserve(OLDM);int a,b;
 {Reader in(argv[1]);need(in.integer(a)&&in.integer(b)&&a==OLDN&&b==OLDM,"accepted filled-source n m header");
  while(in.integer(a)){need(in.integer(b),"source complete edge pair");need(0<=a&&a<b&&b<OLDN,"source parse labels");source[a].push_back(b);source[b].push_back(a);oldedges.push_back({a,b});}
 }
 need(oldedges.size()==OLDM,"entire accepted source parsed once");
 vector<int>baseOwner(OLDN,-1);array<array<int,64>,BASES>baseN{};
 ofstream centers("ORDERED_BASE_CENTERS.tsv");centers<<"base\tpoint_index\tspread_index\tsource_center_label\tsource_degree\n";
 for(int h=0;h<BASES;h++){
  int c=center_labels[h];need(0<=c&&c<160000,"original point-line center label");need(source[c].size()==64,"center literal fullN64");sort(source[c].begin(),source[c].end());
  for(int t=0;t<64;t++){int v=source[c][t];need(baseOwner[v]==-1,"1650 literal sourceN sets disjoint");baseOwner[v]=h;baseN[h][t]=v;}
  centers<<h<<'\t'<<h/50<<'\t'<<h%50<<'\t'<<c<<"\t64\n";
 }
 int used=0,oldpins=0,fillpins=0;for(int v=0;v<OLDN;v++)if(baseOwner[v]>=0){used++;oldpins+=v<160000;fillpins+=v>=160000;}
 need(used==105600&&oldpins==105567&&fillpins==33,"filled-source pin split exact");
 double source_cpu=now()-begin,predbegin=now();array<int,BASES>R{},sourceR3{};map<int,int>Rcounts;
 ofstream predfile("SOURCE_R2_PREDICTIONS_INHERITED.csv");predfile<<"base,center,source_B2,source_R2,inherited_D3_source_R3,provenance\n";
 for(int h=0;h<BASES;h++){
  R[h]=inherited_R2[h];sourceR3[h]=inherited_R3[h];
  need(R[h]>=0&&sourceR3[h]==OLDN-65-R[h],"inherited prediction per-center count identity");
  Rcounts[R[h]]++;predfile<<h<<','<<center_labels[h]<<','<<65+R[h]<<','<<R[h]<<','<<sourceR3[h]<<",accepted_lower_family_SOURCE_R2_ONLY_PREDICTIONS\n";
 }
 predfile.close();double pred_cpu=now()-predbegin;
 vector<string>results;int all_newN=0,max_BFS_roots=0;double max_BFS_cpu=0;
 for(int k=9;k<=16;k++){
  need(now()-begin<budget,"family CPU budget before binding");double casebegin=now();int clones=BASES*k,N=OLDN+clones,degree=64+k,M=OLDM+105600*k;
  string name="d"+to_string(degree)+"_n"+to_string(N),path="cases/"+name;filesystem::create_directories(path);
  vector<int>degrees(N,0),cloneCount(clones,0);vector<array<int,64>>cloneN(clones);
  vector<int>offset,cursor,CSR;
  if(k==16){offset.resize(N+1,0);for(int v=0;v<N;v++)offset[v+1]=offset[v]+(v<OLDN?64+k*int(baseOwner[v]>=0):64);need(offset[N]==2*M,"max CSR total predicted degree");cursor=offset;CSR.resize(2*M);}
  Reader in(string(argv[2])+"/d"+to_string(degree)+"_D3_n"+to_string(N)+".edges");need(in.integer(a)&&in.integer(b)&&a==N&&b==M,"case exact n m header");
  pair<int,int>prev={-1,-1};size_t oldindex=0;int edges=0,added=0;
  while(in.integer(a)){
   need(in.integer(b),"new complete edge pair");need(0<=a&&a<b&&b<N,"new valid labels/no loops");need(prev<pair<int,int>{a,b},"new strict global edge order/simple");prev={a,b};
   if(b<OLDN){need(oldindex<oldedges.size()&&oldedges[oldindex]==pair<int,int>{a,b},"complete old filled-source edge body exact");oldindex++;}
   else{need(a<OLDN,"no new-new edge");int j=b-OLDN;need(cloneCount[j]<64,"clone degree at most64");cloneN[j][cloneCount[j]++]=a;added++;}
   degrees[a]++;degrees[b]++;edges++;
   if(k==16){need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"max CSR degree slots");CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;}
  }
  need(oldindex==oldedges.size()&&edges==M&&added==105600*k,"case complete old/new edge counts");
  int low=0,high=0;for(int v=0;v<N;v++){int expected=v<OLDN?64+k*int(baseOwner[v]>=0):64;need(degrees[v]==expected,"case literal degree formula");low+=expected==64;high+=expected==degree;if(k==16)need(cursor[v]==offset[v+1],"max CSR exact slot fill");}
  need(low==54450+clones&&high==105600,"case degree histogram");ofstream binding(path+"/ORDERED_CLONE_BINDING.tsv");binding<<"j\tcopy\tbase\tsource_center_label\tnew_label\tliteral_N_size\n";
  for(int j=0;j<clones;j++){need(cloneCount[j]==64&&cloneN[j]==baseN[j%BASES],"all new immutable literal sourceN64 exact");binding<<j<<'\t'<<j/BASES<<'\t'<<j%BASES<<'\t'<<center_labels[j%BASES]<<'\t'<<OLDN+j<<"\t64\n";}
  all_newN+=clones;double binding_cpu=now()-casebegin;
  map<array<int,4>,int>predhist,actualhist;for(int h=0;h<BASES;h++)predhist[{1,64,R[h]+k,sourceR3[h]+1649*k}]+=k;
  int roots=0;double bfs_cpu=0;
  if(k==16){
   double bfsbegin=now();vector<int>seen(N,0),queue(N),dist(N);ofstream csv(path+"/NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv");csv<<"j,copy,base,newroot,center,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable\n";
   for(int j=0;j<clones;j++){
    if(j%256==0)need(now()-begin<budget,"family CPU budget during max new-root BFS");
    int h=j%BASES,root=OLDN+j,stamp=j+1,head=0,tail=1,reached=1;queue[0]=root;dist[root]=0;seen[root]=stamp;array<int,4>actual={1,0,0,0},prediction={1,64,R[h]+k,sourceR3[h]+1649*k};
    // Ordinary radius-three queue BFS: depth-three discoveries are marked/countable
    // but need no queue entry, since their adjacency is never expanded.
    while(head<tail){int v=queue[head++],next=dist[v]+1;for(int i=offset[v];i<offset[v+1];i++){int w=CSR[i];if(seen[w]!=stamp){seen[w]=stamp;dist[w]=next;actual[next]++;reached++;if(next<3)queue[tail++]=w;}}}
    need(reached==N&&actual==prediction,"max root all distance classes match source prediction");actualhist[actual]++;roots++;
    csv<<j<<','<<j/BASES<<','<<h<<','<<root<<','<<center_labels[h];for(int z:prediction)csv<<','<<z;for(int z:actual)csv<<','<<z;csv<<','<<reached<<'\n';
    if((j+1)%BASES==0){csv.flush();cout<<"MAX_NEW_BFS_PREFIX "<<j+1<<" CPU="<<now()-bfsbegin<<'\n'<<flush;}
   }
   need(actualhist==predhist,"max aggregate hist matches all roots");bfs_cpu=now()-bfsbegin;max_BFS_roots=roots;max_BFS_cpu=bfs_cpu;
  }
  ostringstream r;r<<"{\"status\":\"PASS_LITERAL_BINDING_AND_OLD_INTERIOR_ALL_PAIR_PREFIX_PROOF\",\"case\":\""<<name<<"\",\"k\":"<<k<<",\"n\":"<<N<<",\"m\":"<<M<<",\"degree_cap\":"<<degree<<",\"old_edges_retained_exact\":5121600,\"new_old_edges\":"<<added<<",\"new_new_edges\":0,\"new_vertices\":"<<clones<<",\"all_new_literal_fullN64_bound\":true,\"old_load_zero\":54450,\"old_load_k\":105600,\"degree64_count\":"<<low<<",\"high_degree_count\":"<<high<<",\"actual_new_literal_R3_BFS_roots\":"<<roots<<",\"old_literal_R3_BFS_roots\":0,\"all_pairs_prefix_proof_independent_of_max_BFS\":true,\"max_BFS_used_to_infer_smaller_prefix_diameter\":false,\"proof_derived_histogram_distribution\":"<<histjson(predhist)<<",\"actual_BFS_histogram_distribution\":"<<histjson(actualhist)<<",\"binding_CPU_seconds\":"<<binding_cpu<<",\"new_BFS_CPU_seconds\":"<<bfs_cpu<<",\"case_CPU_seconds\":"<<now()-casebegin<<",\"exact_diameter\":3}";
  results.push_back(r.str());ofstream(path+"/RESULT.json")<<r.str()<<'\n';ofstream(path+"/TERMINAL.json")<<"{\"status\":\"PASS\",\"case_work_terminal\":true,\"result\":"<<r.str()<<"}\n";
  cout<<"CASE_PASS "<<name<<" newN="<<clones<<" BFSroots="<<roots<<" CPU="<<now()-casebegin<<'\n'<<flush;
 }
 ofstream out("RESULT.json");out<<"{\"status\":\"PASS_ALL_EIGHT_P33_DEGREE73_80_ENDPOINT_GRAPHS\",\"source_literal_parses\":1,\"k_min\":9,\"k_max\":16,\"source_R2_only_centers\":0,\"source_R2_prediction_batches\":0,\"inherited_source_R2_prediction_centers\":1650,\"source_R2_inheritance_binding_CPU_seconds\":"<<pred_cpu<<",\"source_read_and_base_binding_CPU_seconds\":"<<source_cpu<<",\"source_R2_count_distribution\":[";bool comma=false;for(auto[R,n]:Rcounts){if(comma)out<<',';comma=true;out<<"{\"R2\":"<<R<<",\"centers\":"<<n<<'}';}out<<"],\"all_new_literal_N_bindings\":"<<all_newN<<",\"actual_new_literal_R3_BFS_roots\":"<<max_BFS_roots<<",\"BFS_graph_k\":16,\"max_new_BFS_CPU_seconds\":"<<max_BFS_cpu<<",\"old_R3_BFS_roots\":0,\"old_field_geometry_checks\":0,\"max_graph_CSR_separate_from_immutable_source\":true,\"validator_CPU_seconds\":"<<now()-begin<<",\"cases\":[";for(size_t i=0;i<results.size();i++){if(i)out<<',';out<<results[i];}out<<"]}\n";
 return 0;
}catch(const exception&e){cerr<<"VALIDATION_FAIL: "<<e.what()<<'\n';return 2;}}

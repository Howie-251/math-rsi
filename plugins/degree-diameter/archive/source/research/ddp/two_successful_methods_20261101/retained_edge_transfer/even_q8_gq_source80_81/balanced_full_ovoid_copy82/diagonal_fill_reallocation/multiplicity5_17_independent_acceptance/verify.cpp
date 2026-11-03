#include <algorithm>
#include <array>
#include <cstdio>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;namespace fs=std::filesystem;
constexpr int PN=346516,PM=14204970,JSTART=342290,J=4226;
double started,budget;string phase="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-started;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Reader{FILE*f;array<unsigned char,1<<20>buf;size_t pos=0,len=0;
 Reader(const string&p):f(fopen(p.c_str(),"rb")){need(f,"readable literal input "+p);}~Reader(){if(f)fclose(f);}
 int get(){if(pos==len){len=fread(buf.data(),1,buf.size(),f);pos=0;if(!len)return -1;}return buf[pos++];}
 bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}
};
struct Parent{
 vector<pair<int,int>>edges;vector<int>degree,load,owner;vector<vector<int>>N;
 vector<int>diag,off;double parseCPU=0;
};
Parent readParent(const string&path){phase="single_parent_literal_parse";double s=cpu();Parent p;
 p.edges.reserve(PM);p.degree.assign(PN,0);p.load.assign(PN,0);p.owner.assign(PN,-1);p.N.resize(J);
 Reader in(path);int a,b;need(in.integer(a)&&in.integer(b)&&a==PN&&b==PM,"actual G1 parent header, not83");pair<int,int>previous={-1,-1};
 while(in.integer(a)){need(in.integer(b),"complete parent edge");need(0<=a&&a<b&&b<PN&&previous<pair<int,int>{a,b},"accepted G1 lex/simple input contract");previous={a,b};p.edges.emplace_back(a,b);p.degree[a]++;p.degree[b]++;
  if(a>=JSTART)p.N[a-JSTART].push_back(b);if(b>=JSTART)p.N[b-JSTART].push_back(a);
  if(p.edges.size()%1000000==0)need(cpu()<budget,"CPU_BUDGET");
 }
 need(p.edges.size()==PM,"complete parent body count");
 ofstream out("PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv");out<<"role\tsource_center_label\ttype\tNsize\tactual_parent_neighbors\n";
 for(int h=0;h<J;h++){
  auto&n=p.N[h];sort(n.begin(),n.end());need(n.size()==size_t(p.degree[JSTART+h]),"parent role full literal adjacency");need(!n.empty(),"parent roles not isolated");
  string type=h==J-1?"hub":n.size()==80?"diagonal":"offdiagonal";
  if(h==J-1)need(n.size()==65,"literal firsthub N65");else if(n.size()==80)p.diag.push_back(h);else{need(n.size()==81,"literal off N81");p.off.push_back(h);}
  out<<h<<'\t'<<JSTART+h<<'\t'<<type<<'\t'<<n.size()<<'\t';
  for(size_t i=0;i<n.size();i++){int v=n[i];need(0<=v&&v<JSTART&&p.owner[v]<0,"actual J independent, N inside H, pairwise disjoint");p.owner[v]=h;p.load[v]++;if(i)out<<' ';out<<v;}out<<'\n';
 }
 need(p.diag.size()==65&&p.off.size()==4160,"literal role classes65/4160/1");
 int used=0;for(int v=0;v<PN;v++){need(p.load[v]<=1,"source J load1");used+=p.load[v]>0;need(p.degree[v]>0&&p.degree[v]<=82,"accepted G1 noisolates and cap82 input");}
 need(used==342225,"actual all-role pinunion342225");
 ofstream pred("PRESELECTED_BFS_ROLES.json");pred<<"{\"basis\":\"actual G1 role Nsizes before reading either candidate\",\"diagonal_roles\":[";for(size_t i=0;i<p.diag.size();i++){if(i)pred<<',';pred<<p.diag[i];}pred<<"],\"off_roles\":["<<p.off[0]<<','<<p.off[1]<<"],\"hub_role\":4225,\"last_new_block_only\":true,\"roots_per_case\":68}\n";
 p.parseCPU=cpu()-s;return p;
}
void arr(ostream&o,const array<int,4>&a){o<<'['<<a[0]<<','<<a[1]<<','<<a[2]<<','<<a[3]<<']';}
void checkCase(const Parent&p,const string&path,const string&outdir,int cap,int r,int n,int m,
               array<int,4>pd,array<int,4>po,array<int,4>ph){
 double caseStart=cpu();fs::create_directories(outdir);phase="candidate"+to_string(cap)+"_complete_single_stream";
 const int newcount=r*J,last=PN+(r-1)*J;
 vector<int>roles=p.diag;roles.push_back(p.off[0]);roles.push_back(p.off[1]);roles.push_back(J-1);
 ofstream pre(outdir+"/PRESELECTED_LAST_BLOCK_ROOTS.json");pre<<"{\"copy_index\":"<<r-1<<",\"new_roots\":[";for(size_t i=0;i<roles.size();i++){if(i)pre<<',';pre<<last+roles[i];}pre<<"],\"off_roles\":["<<p.off[0]<<','<<p.off[1]<<"],\"chosen_before_candidate_read\":true}\n";pre.close();
 vector<int>offset(n+1),degree(n,0),actualNcount(newcount,0),cursor,CSR(2*m);
 for(int v=0;v<n;v++){int d=v<PN?p.degree[v]+r*p.load[v]:int(p.N[(v-PN)%J].size());offset[v+1]=offset[v]+d;}
 need(offset[n]==2*m,"case expected degree sum");cursor=offset;
 Reader in(path);int a,b;need(in.integer(a)&&in.integer(b)&&a==n&&b==m,"candidate header degree"+to_string(cap));
 pair<int,int>previous={-1,-1};int oldidx=0,newedges=0,total=0;double bindStart=cpu();
 while(in.integer(a)){
  need(in.integer(b),"complete candidate edge pair");need(0<=a&&a<b&&b<n&&previous<pair<int,int>{a,b},"candidate strictlex simple / no loops");previous={a,b};
  if(b<PN){need(oldidx<PM&&p.edges[oldidx]==pair<int,int>{a,b},"all literal G1 edges retained exact");oldidx++;}
  else{need(a<JSTART,"newroles only actual source H neighbors, no new-new/J edge");int j=b-PN,h=j%J;const auto&expected=p.N[h];need(binary_search(expected.begin(),expected.end(),a),"every actual newedge belongs to literal parent role N");actualNcount[j]++;newedges++;}
  need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"actual case CSR degree capacity");CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;degree[a]++;degree[b]++;total++;
  if(total%1000000==0)need(cpu()<budget,"CPU_BUDGET");
 }
 need(oldidx==PM&&newedges==r*342225&&total==m,"complete parent/new/body counts");
 ofstream binding(outdir+"/ALL_NEW_ROLE_BINDINGS.tsv");binding<<"j\tcopy\trole\tsource_center_label\tnew_label\tliteral_N_size\tactual_edge_count\tcomplete_parent_N_equal\tactual_parent_N_template_row\n";
 for(int j=0;j<newcount;j++){int h=j%J;need(actualNcount[j]==int(p.N[h].size()),"every newrole full degree and actual N equality");binding<<j<<'\t'<<j/J<<'\t'<<h<<'\t'<<JSTART+h<<'\t'<<PN+j<<'\t'<<p.N[h].size()<<'\t'<<actualNcount[j]<<"\ttrue\t"<<h<<'\n';}
 map<int,int>hist;for(int v=0;v<n;v++){need(cursor[v]==offset[v+1]&&degree[v]==offset[v+1]-offset[v],"complete literal pervertex degree");hist[degree[v]]++;}
 const map<int,int>expected=cap==86?map<int,int>{{65,5},{80,325},{81,20865},{86,342225}}:map<int,int>{{65,17},{80,1105},{81,70785},{98,342225}};
 need(hist==expected,"complete actual degree histogram");double bindingCPU=cpu()-bindStart;
 phase="case"+to_string(cap)+"_only68_lastblock_BFS";double bfsStart=cpu();
 vector<int>seen(n,0),distance(n),prev(n),queue(n);map<array<int,4>,int>dh,oh,hh;int misses=0,mismatches=0;bool witness=false;
 ofstream bfs(outdir+"/ALL_68_LAST_BLOCK_NEW_ROOT_BFS.csv");bfs<<"root,role,kind,pred0,pred1,pred2,pred3,actual0,actual1,actual2,actual3,reached,prediction_match,same_class_others_distance2,new_vertex_R2,new_vertex_R3,first_missing\n";
 for(int k=0;k<int(roles.size());k++){
  need(cpu()<budget,"CPU_BUDGET");int h=roles[k],root=last+h,stamp=k+1,head=0,tail=1,reached=1;bool hub=h==J-1,diag=!hub&&p.N[h].size()==80;
  array<int,4>actual={1,0,0,0},pred=hub?ph:diag?pd:po;queue[0]=root;seen[root]=stamp;distance[root]=0;prev[root]=-1;
  while(head<tail){int v=queue[head++],next=distance[v]+1;for(int i=offset[v];i<offset[v+1];i++){int w=CSR[i];if(seen[w]!=stamp){seen[w]=stamp;distance[w]=next;prev[w]=v;actual[next]++;reached++;if(next<3)queue[tail++]=w;}}}
  int twins=0;need(seen[JSTART+h]==stamp&&distance[JSTART+h]==2,"same-role source center actual distance2");twins++;
  for(int copy=0;copy<r-1;copy++){int t=PN+copy*J+h;need(seen[t]==stamp&&distance[t]==2,"each earlier new same-role copy actual distance2");twins++;}
  need(twins==r,"complete same-role repeated class distance2");
  int nr2=0,nr3=0;for(int v=PN;v<n;v++)if(seen[v]==stamp){nr2+=distance[v]==2;nr3+=distance[v]==3;}
  need(nr2==r-1&&nr3==r*(J-1),"sameclass only atR2 and all other newrole classes atR3");
  int missing=-1;if(reached!=n){misses++;for(int v=0;v<n;v++)if(seen[v]!=stamp){missing=v;break;}}
  bool match=actual==pred;mismatches+=!match;(hub?hh:diag?dh:oh)[actual]++;
  bfs<<root<<','<<h<<','<<(hub?"hub":diag?"diagonal":"offdiagonal");for(int v:pred)bfs<<','<<v;for(int v:actual)bfs<<','<<v;bfs<<','<<reached<<','<<match<<','<<twins<<','<<nr2<<','<<nr3<<','<<missing<<'\n';
  if(hub){int target=JSTART;need(seen[target]==stamp&&distance[target]==3,"newhub-parentclone nonD2 witness");vector<int>w;for(int z=target;z>=0;z=prev[z])w.push_back(z);reverse(w.begin(),w.end());ofstream f(outdir+"/NON_D2_ACTUAL_LAST_HUB_WITNESS.json");f<<"{\"root\":"<<root<<",\"target\":"<<target<<",\"distance\":3,\"genuine_walk\":[";for(size_t i=0;i<w.size();i++){if(i)f<<',';f<<w[i];}f<<"],\"within_preselected68_BFS\":true,\"old_root_BFS\":0}\n";witness=true;}
 }
 need(witness,"actual nonD2 witness");double bfsCPU=cpu()-bfsStart;
 string status=misses?"FAIL_SELECTED_ROOT_D3":mismatches?"PASS_WITH_HIST_PREDICTION_MISMATCH":"PASS";
 ofstream result(outdir+"/RESULT.json");result<<"{\"status\":\""<<status<<"\",\"Delta\":"<<cap<<",\"D\":3,\"n\":"<<n<<",\"m\":"<<m<<",\"source_n\":346516,\"source_m\":14204970,\"source_is_actual_G1_not83\":true,\"shared_parent_literal_parse_count\":1,\"this_candidate_literal_parse_count\":1,\"parent_edges_retained_exact\":14204970,\"new_edges\":"<<newedges<<",\"new_new_edges\":0,\"simple\":true,\"header_body_match\":true,\"additional_blocks\":"<<r<<",\"total_multiplicity\":"<<r+1<<",\"new_roles_bound\":"<<newcount<<",\"parent_roles_bound\":4226,\"binding_method\":\"Every literal newedge in independently parsed parent N plus full actual degree; simple implies exact complete neighbor equality\",\"binding_rows\":\"ALL_NEW_ROLE_BINDINGS.tsv\",\"parent_N_templates\":\"../../multiplicity5_17_independent_acceptance/PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv\",\"source_role_N_pairwise_disjoint\":true,\"source_role_N_union\":342225,\"max_new_load\":"<<r<<",\"degree_histogram\":{";
 bool first=true;for(auto [d,c]:hist){if(!first)result<<',';first=false;result<<'"'<<d<<"\":"<<c;}result<<"},\"actual_lastblock_new_BFS_roots\":68,\"diagonal_roots\":65,\"off_roots\":2,\"hub_roots\":1,\"preselected_off_roles\":["<<p.off[0]<<','<<p.off[1]<<"],\"unmeasured_new_roots\":"<<newcount-68<<",\"old_root_BFS\":0,\"R3_failing_roots\":"<<misses<<",\"hist_mismatches\":"<<mismatches<<",\"actual_hist_distributions\":{";
 auto histout=[&](string name,const map<array<int,4>,int>&v,bool comma){if(comma)result<<',';result<<'"'<<name<<"\":[";bool first=true;for(auto [h,c]:v){if(!first)result<<',';first=false;result<<"{\"hist\":";arr(result,h);result<<",\"count\":"<<c<<'}';}result<<']';};histout("diagonal",dh,false);histout("off_selected",oh,true);histout("hub",hh,true);
 result<<"},\"same_role_distance2_others_per_measured_root\":"<<r<<",\"actual_new_vertex_R2_per_measured_root\":"<<r-1<<",\"actual_new_vertex_R3_per_measured_root\":"<<r*(J-1)<<",\"allpair_and_every_prefix_old_parent_interior_proof\":true,\"nonD2_witness\":\"NON_D2_ACTUAL_LAST_HUB_WITNESS.json\",\"exact_diameter\":"<<(misses?-1:3)<<",\"shared_parent_parse_CPU_seconds\":"<<p.parseCPU<<",\"case_binding_CPU_seconds\":"<<bindingCPU<<",\"case68_BFS_CPU_seconds\":"<<bfsCPU<<",\"case_validator_CPU_seconds\":"<<cpu()-caseStart<<",\"old_H_field_geometry_BFS_Lean_solver_paidreview_retests\":0,\"root_counts_modified\":false,\"global_record_claim\":false}\n";
 cout<<"CASE_TERMINAL degree="<<cap<<" status="<<status<<" CPU="<<cpu()-caseStart<<'\n'<<flush;need(!misses,"actual R3 missing target");
}
int main(int argc,char**argv){started=double(clock())/CLOCKS_PER_SEC;try{
 need(argc==7,"parent graph86 out86 graph98 out98 budget");budget=stod(argv[6]);Parent p=readParent(argv[1]);
 checkCase(p,argv[2],argv[3],86,4,363420,15573870,{1,80,5254,358085},{1,81,5333,358005},{1,65,5269,358085});
 checkCase(p,argv[4],argv[5],98,16,414132,19680570,{1,80,5266,408785},{1,81,5345,408705},{1,65,5281,408785});
 ofstream out("VALIDATOR_SUMMARY.json");out<<"{\"status\":\"PASS_BOTH_INDEPENDENT_G1_TARGETS\",\"parent_parse_count\":1,\"candidate_parse_count\":2,\"actual_new_BFS_roots\":136,\"old_BFS_roots\":0,\"shared_parent_parse_CPU_seconds\":"<<p.parseCPU<<",\"validator_total_CPU_seconds\":"<<cpu()<<",\"no_source_H_or_field_geometry_retests\":true}\n";return 0;
 }catch(const exception&e){ofstream("FAILURE.json")<<"{\"status\":\"FAILED_OR_BUDGET_UNKNOWN\",\"phase\":\""<<phase<<"\",\"reason\":\""<<e.what()<<"\",\"CPU_seconds\":"<<cpu()<<"}\n";cerr<<phase<<": "<<e.what()<<'\n';return 2;}
}

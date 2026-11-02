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
#include "center_input.h"
using namespace std;
constexpr int OLDN=342290,OLDM=13862745,K=4225,N=346515,M=14204970;
double startCPU,budget;string stage="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-startCPU;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Reader{FILE*f;array<unsigned char,1<<20>buf;size_t pos=0,len=0;Reader(const string&p):f(fopen(p.c_str(),"rb")){need(f!=nullptr,"literal input readable "+p);}~Reader(){if(f)fclose(f);}int get(){if(pos==len){len=fread(buf.data(),1,buf.size(),f);pos=0;if(!len)return -1;}return buf[pos++];}bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer file syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}};
int main(int argc,char**argv){startCPU=double(clock())/CLOCKS_PER_SEC;budget=argc>3?stod(argv[3]):110;try{
 need(argc==4,"source candidate CPUbudget");stage="ordered_center_binding";
 vector<int>center(K),which(OLDN,-1),diagonal(K,0),isD(OLDN,0);int diagcount=0;
 for(int i=0;i<65;i++)for(int j=0;j<65;j++){int h=65*i+j,c=ovoid[i]*585+spread[j];need(0<=c&&c<342225&&which[c]<0,"ordered center physical labels unique");center[h]=c;which[c]=h;diagonal[h]=j==ovoid_owner[i];if(diagonal[h]){isD[c]=1;diagcount++;}}
 need(diagcount==65,"65actual diagonal centers");
 vector<array<int,81>>sourceN(K),cloneN(K);vector<int>sourcecount(K,0),clonecount(K,0),degree(N,0),offset(N+1),cursor,CSR(2*M);
 for(int v=0;v<N;v++)offset[v+1]=offset[v]+81+int(v<OLDN&&!isD[v]);need(offset[N]==2*M,"expected CSR total degree");cursor=offset;
 stage="complete_literal_source_and_candidate_streams";double bindstart=cpu();
 Reader src(argv[1]),graph(argv[2]);int a,b,x,y;
 need(src.integer(x)&&src.integer(y)&&x==OLDN&&y==OLDM,"accepted source n m header");need(graph.integer(x)&&graph.integer(y)&&x==N&&y==M,"new candidate n m header");
 pair<int,int>previous={-1,-1};int oldedges=0,newedges=0,total=0;
 while(graph.integer(a)){
  need(graph.integer(b),"complete candidate edge pair");need(0<=a&&a<b&&b<N,"valid candidate endpoints / no loops");need(previous<pair<int,int>{a,b},"candidate strict global order / simple");previous={a,b};
  if(b<OLDN){need(src.integer(x)&&src.integer(y)&&x==a&&y==b,"complete oldsource body exact");oldedges++;
   int i=which[a],j=which[b];if(i>=0){need(sourcecount[i]<81,"sourcecenter neighbor count bound");sourceN[i][sourcecount[i]++]=b;}if(j>=0){need(sourcecount[j]<81,"sourcecenter neighbor count bound");sourceN[j][sourcecount[j]++]=a;}
  }else{need(a<OLDN,"no clone-clone edge");int h=b-OLDN;need(clonecount[h]<81,"newroot N size bound");cloneN[h][clonecount[h]++]=a;newedges++;}
  need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"actual CSR degree slots");CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;degree[a]++;degree[b]++;total++;
  if(total%1000000==0)need(cpu()<budget,"CPU_BUDGET");
 }
 need(!src.integer(x),"no omitted source suffix");need(oldedges==OLDM&&newedges==342225&&total==M,"exact old/new/total edge counts");
 vector<int>pinowner(OLDN,-1),priorpin(OLDN,0);ofstream ordered("ORDERED_SOURCE_N81_BINDING.tsv");ordered<<"h\tovoid_index\tspread_index\tcenter_oldlabel\tnewlabel\tdiagonal";for(int t=0;t<81;t++)ordered<<"\tpin"<<t;ordered<<'\n';
 ofstream prefix("INDEPENDENT_PREFIX_LOADS.csv");prefix<<"prefix_clones,new_label,Nsize,max_prior_pin_load,max_old_pin_load,degree81_count,degree82_count,degree_cap\n";prefix<<"0,-1,0,0,0,"<<OLDN<<",0,81\n";
 for(int h=0;h<K;h++){
  need(sourcecount[h]==81&&clonecount[h]==81,"complete source and clone N81");sort(sourceN[h].begin(),sourceN[h].end());need(cloneN[h]==sourceN[h],"newroot whole immutable source N81 binding");
  ordered<<h<<'\t'<<h/65<<'\t'<<h%65<<'\t'<<center[h]<<'\t'<<OLDN+h<<'\t'<<diagonal[h];
  for(int v:sourceN[h]){need(0<=v&&v<OLDN&&pinowner[v]<0&&!priorpin[v],"actual source Nsets disjoint");pinowner[v]=h;priorpin[v]=1;ordered<<'\t'<<v;}
  ordered<<'\n';int k=h+1;prefix<<k<<','<<OLDN+h<<",81,0,1,"<<OLDN-80*k<<','<<81*k<<",82\n";
 }
 int low=0,high=0,used=0,fillpins=0;
 for(int v=0;v<OLDN;v++){need((pinowner[v]<0)==bool(isD[v]),"pinunion exactly source minus65D");used+=pinowner[v]>=0;fillpins+=v>=342225&&pinowner[v]>=0;}
 need(used==342225&&fillpins==65,"source pin union and oldfill participation");
 for(int v=0;v<N;v++){int expect=81+int(v<OLDN&&pinowner[v]>=0);need(degree[v]==expect&&cursor[v]==offset[v+1],"every literal degree/load complete");low+=expect==81;high+=expect==82;}
 need(low==4290&&high==342225,"literal degree histogram");
 double bindingCPU=cpu()-bindstart;stage="all4225actual_newroot_ordinary_R3_BFS";double bfsstart=cpu();
 vector<int>seen(N,0),distance(N),queue(N);map<array<int,4>,int>hist;int actualdiag=0,actualoff=0;
 ofstream bfs("ALL_NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv");bfs<<"h,ovoid_index,spread_index,center,newroot,diagonal,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable\n";
 for(int h=0;h<K;h++){
  if(h%65==0)need(cpu()<budget,"CPU_BUDGET");
  int root=OLDN+h,stamp=h+1,head=0,tail=1,reached=1;queue[0]=root;seen[root]=stamp;distance[root]=0;
  array<int,4>actual={1,0,0,0},pred=diagonal[h]?array<int,4>{1,81,5249,341184}:array<int,4>{1,81,5329,341104};
  while(head<tail){int v=queue[head++],next=distance[v]+1;for(int p=offset[v];p<offset[v+1];p++){int w=CSR[p];if(seen[w]!=stamp){seen[w]=stamp;distance[w]=next;actual[next]++;reached++;if(next<3)queue[tail++]=w;}}}
  need(reached==N&&actual==pred,"newroot full distance classes match h="+to_string(h));hist[actual]++;actualdiag+=diagonal[h];actualoff+=!diagonal[h];
  bfs<<h<<','<<h/65<<','<<h%65<<','<<center[h]<<','<<root<<','<<diagonal[h];for(int n:pred)bfs<<','<<n;for(int n:actual)bfs<<','<<n;bfs<<','<<reached<<'\n';
  if((h+1)%650==0)cout<<"NEWROOT_PREFIX "<<h+1<<" CPU="<<cpu()-bfsstart<<'\n'<<flush;
 }
 need(actualdiag==65&&actualoff==4160&&hist.size()==2,"allroot class counts");
 double bfsCPU=cpu()-bfsstart;
 ofstream result("RESULT.json");result<<"{\"status\":\"PASS_COMPLETE_DEGREE82_GRAPH_BINDING_ALL4225_NEWROOT_BFS_ALLPAIR_PREFIX_PROOF\",\"n\":346515,\"m\":14204970,\"degree_cap\":82,\"source_n\":342290,\"source_m\":13862745,\"source_literal_parses\":1,\"candidate_literal_parses\":1,\"old_edge_body_retained_exact\":13862745,\"new_old_edges\":342225,\"new_new_edges\":0,\"all4225_source_N81_lists_bound\":true,\"source_pin_union\":342225,\"source_oldD_free\":65,\"source_original_fill_pins_used\":65,\"degree81_count\":4290,\"degree82_count\":342225,\"prefix_rows\":4226,\"actual_newroot_R3_BFS_roots\":4225,\"oldroot_BFS_or_sourceR2_enumerations\":0,\"actual_histogram_distribution\":[{\"roots\":65,\"histogram\":[1,81,5249,341184]},{\"roots\":4160,\"histogram\":[1,81,5329,341104]}],\"source_R2_values_are_prior_predictions_not_new_measurements\":true,\"allpair_old_interior_prefix_proof\":true,\"nonD2_method\":\"collapse everyclone to sourcecenter; inherited acceptedsource witness42705/43363\",\"extra_nonD2_BFS_or_CSR_witness_checks\":0,\"exact_diameter\":3,\"field_smallgeometry_projection_Lean_solver_reruns\":0,\"complete_binding_CPU_seconds\":"<<bindingCPU<<",\"all4225_newroot_BFS_CPU_seconds\":"<<bfsCPU<<",\"validator_CPU_seconds\":"<<cpu()<<",\"new_graphs_counted_by_agent\":0,\"global_record_or_priority_certified\":false}\n";return 0;
 }catch(const exception&e){ofstream("FAILURE.json")<<"{\"status\":\"FAIL_OR_BUDGET_UNKNOWN\",\"stage\":\""<<stage<<"\",\"reason\":\""<<e.what()<<"\",\"CPU_seconds\":"<<cpu()<<"}\n";cerr<<stage<<": "<<e.what()<<'\n';return 2;}}

#include <algorithm>
#include <array>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
#include "center_input.h"
using namespace std;
constexpr int UN=342225,HN=342290,HM=13862745,K=4225,OLDN=346515,N=346516,M=14204970;
double startCPU,budget;string phase="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-startCPU;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Reader{FILE*f;array<unsigned char,1<<20>buf;size_t pos=0,len=0;
 Reader(const string&p):f(fopen(p.c_str(),"rb")){need(f,"input readable "+p);}~Reader(){if(f)fclose(f);}
 int get(){if(pos==len){len=fread(buf.data(),1,buf.size(),f);pos=0;if(!len)return -1;}return buf[pos++];}
 bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}
};
void arr(ostream&o,const array<int,4>&a){o<<'['<<a[0]<<','<<a[1]<<','<<a[2]<<','<<a[3]<<']';}
int main(int argc,char**argv){startCPU=double(clock())/CLOCKS_PER_SEC;try{
 need(argc==5,"H old346515 new346516 CPUbudget");budget=stod(argv[4]);
 phase="actual_ordered_centers";
 vector<int>center(K),which(HN,-1),diag(K,0),isD(HN,0),diagroots;
 for(int i=0;i<65;i++)for(int j=0;j<65;j++){
  int h=65*i+j,c=585*ovoid[i]+spread[j];need(c>=0&&c<UN&&which[c]<0,"unique center label");
  center[h]=c;which[c]=h;diag[h]=j==ovoid_owner[i];
  if(diag[h]){isD[c]=1;diagroots.push_back(HN+h);}
 }
 need(diagroots.size()==65,"65 actual diagonal owners");
 vector<array<int,81>>sourceU(K),cloneU(K);vector<int>sourcecount(K,0),clonecount(K,0);
 vector<int>offset(N+1,0),degree(N,0),cursor,CSR(2*M);
 for(int v=0;v<N;v++){
  int d=v<HN?(82-isD[v]):(v==OLDN?65:81-diag[v-HN]);offset[v+1]=offset[v]+d;
 }
 need(offset[N]==2*M,"predicted total degree");cursor=offset;
 phase="three_single_literal_streams";double bindstart=cpu();
 Reader src(argv[1]),old(argv[2]),fresh(argv[3]);int x,y,a,b;
 need(src.integer(x)&&src.integer(y)&&x==HN&&y==HM,"source H header");
 need(old.integer(x)&&old.integer(y)&&x==OLDN&&y==M,"accepted old header");
 need(fresh.integer(x)&&fresh.integer(y)&&x==N&&y==M,"fresh header");
 pair<int,int>oldpair={-1,-1},prevold={-1,-1};bool haveold=false;int oldseen=0;
 auto nextOld=[&](){int a,b;if(!old.integer(a)){haveold=false;return;}
  need(old.integer(b),"complete accepted edge");oldpair={a,b};need(prevold<oldpair,"accepted lex input contract");prevold=oldpair;haveold=true;oldseen++;};
 nextOld();int removed=0,added=0,retained=0,total=0,hbody=0,clonedges=0,hubedges=0;
 ofstream delta("EXACT_65_REMOVED_65_ADDED.tsv");delta<<"operation\tu\tv\n";
 auto isRemoved=[&](pair<int,int>e){int h=e.second-HN;return 0<=h&&h<K&&diag[h]&&e.first==UN+ovoid_owner[h/65];};
 auto removeOld=[&](){need(isRemoved(oldpair),"unexpected deleted edge");delta<<"removed\t"<<oldpair.first<<'\t'<<oldpair.second<<'\n';removed++;nextOld();};
 pair<int,int>previous={-1,-1};
 while(fresh.integer(a)){
  need(fresh.integer(b),"complete fresh edge");pair<int,int>e={a,b};
  need(0<=a&&a<b&&b<N,"fresh simple endpoints");need(previous<e,"fresh strict lex / no duplicate");previous=e;
  while(haveold&&oldpair<e)removeOld();
  if(haveold&&oldpair==e){retained++;nextOld();}
  else{need(b==OLDN&&UN<=a&&a<HN,"unexpected added edge");delta<<"added\t"<<a<<'\t'<<b<<'\n';added++;}
  if(b<HN){need(src.integer(x)&&src.integer(y)&&x==a&&y==b,"source H complete body exact");hbody++;
   int h=which[a],k=which[b];
   if(h>=0&&b<UN){need(sourcecount[h]<81,"source U N cap");sourceU[h][sourcecount[h]++]=b;}
   if(k>=0&&a<UN){need(sourcecount[k]<81,"source U N cap");sourceU[k][sourcecount[k]++]=a;}
  }else if(b<OLDN){need(a<UN,"clone must only meet U");int h=b-HN;need(clonecount[h]<81,"clone U N cap");cloneU[h][clonecount[h]++]=a;clonedges++;}
  else{need(UN<=a&&a<HN,"hub pins exactly fillers");hubedges++;}
  need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"actual degree/CSR bound");
  CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;degree[a]++;degree[b]++;total++;
  if(total%1000000==0)need(cpu()<budget,"CPU_BUDGET");
 }
 while(haveold)removeOld();
 need(!src.integer(x),"no source H suffix omitted");
 need(total==M&&hbody==HM&&oldseen==M&&removed==65&&added==65&&retained==M-65,"actual complete counts/delta");
 need(clonedges==342160&&hubedges==65,"true modified clone and hub edge counts");
 phase="all4225_true_U_neighborhood_binding";
 vector<int>pinowner(UN,-1);ofstream pins("ALL_4225_TRUE_U_N_BINDINGS.tsv");
 pins<<"h\tovoid_index\tspread_index\tcenter\tnewlabel\tdiagonal\tpin_count\tactual_U_pins\n";
 int used=0;
 for(int h=0;h<K;h++){
  int n=81-diag[h];need(sourcecount[h]==n&&clonecount[h]==n,"complete actual U N sizes");
  sort(sourceU[h].begin(),sourceU[h].begin()+n);
  need(equal(sourceU[h].begin(),sourceU[h].begin()+n,cloneU[h].begin()),"whole true U N binding");
  pins<<h<<'\t'<<h/65<<'\t'<<h%65<<'\t'<<center[h]<<'\t'<<HN+h<<'\t'<<diag[h]<<'\t'<<n<<'\t';
  for(int k=0;k<n;k++){int v=sourceU[h][k];need(v>=0&&v<UN&&pinowner[v]<0,"all true U pins distinct");pinowner[v]=h;used++;if(k)pins<<' ';pins<<v;}pins<<'\n';
 }
 need(used==342160,"true U pin union size");
 for(int v=0;v<UN;v++)need((pinowner[v]<0)==bool(isD[v]),"true U pin union exactly U minus D65");
 map<int,int>degreehist;
 for(int v=0;v<N;v++){need(cursor[v]==offset[v+1]&&degree[v]==offset[v+1]-offset[v],"complete vertex degree");degreehist[degree[v]]++;}
 need(degreehist==map<int,int>{{65,1},{80,65},{81,4225},{82,342225}},"degree histogram");
 double bindingCPU=cpu()-bindstart;
 phase="only65_changed_diag_plus_hub_ordinary_BFS";double bfsstart=cpu();
 vector<int>roots=diagroots;roots.push_back(OLDN);vector<int>seen(N,0),distance(N),parent(N),queue(N);
 map<array<int,4>,int>diaghist,hubhist;int failures=0,mismatches=0;bool witness=false;
 ofstream bfs("ALL_66_CHANGED_ROOT_BFS.csv");bfs<<"root,kind,pred0,pred1,pred2,pred3,actual0,actual1,actual2,actual3,reached,prediction_match,first_missing\n";
 for(int k=0;k<int(roots.size());k++){
  need(cpu()<budget,"CPU_BUDGET");int root=roots[k],stamp=k+1,head=0,tail=1,reached=1;
  queue[0]=root;seen[root]=stamp;distance[root]=0;parent[root]=-1;
  array<int,4>actual={1,0,0,0},pred=root==OLDN?array<int,4>{1,65,5265,341185}:array<int,4>{1,80,5250,341185};
  while(head<tail){int v=queue[head++],next=distance[v]+1;
   for(int p=offset[v];p<offset[v+1];p++){int w=CSR[p];if(seen[w]!=stamp){seen[w]=stamp;distance[w]=next;parent[w]=v;actual[next]++;reached++;if(next<3)queue[tail++]=w;}}
  }
  int firstmissing=-1;if(reached!=N){failures++;for(int v=0;v<N;v++)if(seen[v]!=stamp){firstmissing=v;break;}}
  bool match=actual==pred;mismatches+=!match;(root==OLDN?hubhist:diaghist)[actual]++;
  bfs<<root<<','<<(root==OLDN?"hub":"diagonal");for(int n:pred)bfs<<','<<n;for(int n:actual)bfs<<','<<n;bfs<<','<<reached<<','<<match<<','<<firstmissing<<'\n';
  if(!witness){for(int v=0;v<UN;v++)if(seen[v]==stamp&&distance[v]==3){
    vector<int>w;for(int z=v;z>=0;z=parent[z])w.push_back(z);reverse(w.begin(),w.end());
    ofstream out("NON_D2_ACTUAL_CHANGED_ROOT_WITNESS.json");out<<"{\"root\":"<<root<<",\"target\":"<<v<<",\"actual_distance\":3,\"genuine_walk\":[";
    for(size_t i=0;i<w.size();i++){if(i)out<<',';out<<w[i];}out<<"],\"from_authorized_changed_root_BFS\":true,\"old_root_BFS\":0}\n";witness=true;break;
  }}
 }
 need(witness,"actual changed-root nonD2 witness");double bfsCPU=cpu()-bfsstart;
 string status=failures?"FAIL_CHANGED_ROOT_D3":(mismatches?"PASS_WITH_HIST_PREDICTION_MISMATCH":"PASS");
 ofstream result("RESULT.json");result<<"{\"status\":\""<<status<<"\",\"actual_n\":346516,\"actual_m\":14204970,\"max_degree\":82,\"simple\":true,\"header_matches_body\":true,\"source_H_edges_retained_exact\":13862745,\"source_H_parse\":1,\"old346515_delta_parse\":1,\"new346516_parse\":1,\"actual_removed_diagonal_F_edges\":65,\"actual_added_hub_F_edges\":65,\"all4225_true_U_clone_neighborhoods_bound\":true,\"clone_U_edges_and_disjoint_pins\":342160,\"hub_F_edges\":65,\"new_new_edges\":0,\"degree_histogram\":{\"65\":1,\"80\":65,\"81\":4225,\"82\":342225},\"changed_diag_roots_BFS\":65,\"hub_roots_BFS\":1,\"off4160_roots_BFS\":0,\"old_roots_BFS\":0,\"changed_roots_R3_failures\":"<<failures<<",\"hist_prediction_mismatches\":"<<mismatches<<",\"actual_diagonal_hist_distribution\":[";
 bool first=true;for(auto [h,n]:diaghist){if(!first)result<<',';first=false;result<<"{\"hist\":";arr(result,h);result<<",\"roots\":"<<n<<'}';}
 result<<"],\"actual_hub_hist_distribution\":[";first=true;for(auto [h,n]:hubhist){if(!first)result<<',';first=false;result<<"{\"hist\":";arr(result,h);result<<",\"roots\":"<<n<<'}';}
 result<<"],\"off4160_predicted_histogram_not_measured\":[1,81,5329,341105],\"unmeasured_off_pairs_proof\":\"U-only endpoint routes and retained H routes to fillers, not old maxgraph-BFS deletion\",\"prefix_proof\":\"Build true U-neighborhood clones directly from H, hub last; all interiors old U/H\",\"nonD2\":\"Actual distance3 witness from authorized changed-root BFS\",\"exact_diameter\":"<<(failures?-1:3)<<",\"field_geometry_oldBFS_Lean_solver_paidreview_reruns\":0,\"complete_binding_CPU_seconds\":"<<bindingCPU<<",\"only66_changed_root_BFS_CPU_seconds\":"<<bfsCPU<<",\"validator_CPU_seconds\":"<<cpu()<<",\"root_count_modified\":false,\"priority_or_global_record_claim\":false}\n";
 cout<<status<<" source/old/new each parse1; bindings4225; changedBFS66; offBFS0; CPU="<<cpu()<<'\n';return failures?2:0;
 }catch(const exception&e){ofstream("FAILURE.json")<<"{\"status\":\"FAILED_OR_BUDGET_UNKNOWN\",\"phase\":\""<<phase<<"\",\"reason\":\""<<e.what()<<"\",\"CPU_seconds\":"<<cpu()<<"}\n";cerr<<phase<<": "<<e.what()<<'\n';return 2;}
}

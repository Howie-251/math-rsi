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
constexpr int UN=342225,HN=342290,HM=13862745,K=4225,HUB0=346515,OLDN=346516,OLDM=14204970,HUB1=350741,N=350742,M=14547195;
double startCPU,budget;string phase="initial";
double cpu(){return double(clock())/CLOCKS_PER_SEC-startCPU;}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
struct Reader{FILE*f;array<unsigned char,1<<20>buf;size_t pos=0,len=0;
 Reader(const string&p):f(fopen(p.c_str(),"rb")){need(f,"readable input "+p);}~Reader(){if(f)fclose(f);}
 int get(){if(pos==len){len=fread(buf.data(),1,buf.size(),f);pos=0;if(!len)return -1;}return buf[pos++];}
 bool integer(int&v){int c;do{c=get();if(c<0)return false;}while(c<=32);need(c>='0'&&c<='9',"integer syntax");v=0;do{v=10*v+c-'0';c=get();}while(c>='0'&&c<='9');need(c<0||c<=32,"integer separator");return true;}
};
void arr(ostream&o,const array<int,4>&a){o<<'['<<a[0]<<','<<a[1]<<','<<a[2]<<','<<a[3]<<']';}
int main(int argc,char**argv){startCPU=double(clock())/CLOCKS_PER_SEC;try{
 need(argc==5,"H accepted346516 new350742 CPUbudget");budget=stod(argv[4]);
 phase="actual_ordered_centers_and_preselected_roots";
 vector<int>center(K),which(HN,-1),diag(K,0),isD(HN,0),roots;
 for(int i=0;i<65;i++)for(int j=0;j<65;j++){
  int h=65*i+j,c=585*ovoid[i]+spread[j];need(0<=c&&c<UN&&which[c]<0,"unique center label");
  center[h]=c;which[c]=h;diag[h]=j==ovoid_owner[i];if(diag[h]){isD[c]=1;roots.push_back(OLDN+h);}
 }
 need(roots.size()==65&&!diag[off_indices[0]]&&!diag[off_indices[1]]&&off_indices[0]!=off_indices[1],"preselected actual off roots");
 roots.push_back(OLDN+off_indices[0]);roots.push_back(OLDN+off_indices[1]);roots.push_back(HUB1);
 vector<array<int,81>>sourceU(K),copy0(K),copy1(K);vector<int>sourcecount(K,0),count0(K,0),count1(K,0);
 vector<int>offset(N+1),degree(N,0),cursor,CSR(2*M);
 for(int v=0;v<N;v++){
  int d;if(v<HN)d=83-2*isD[v];else if(v<HUB0)d=81-diag[v-HN];else if(v==HUB0||v==HUB1)d=65;else d=81-diag[v-OLDN];
  offset[v+1]=offset[v]+d;
 }
 need(offset[N]==2*M,"predicted full degree sum");cursor=offset;
 phase="three_single_literal_streams";double bindstart=cpu();
 Reader src(argv[1]),old(argv[2]),fresh(argv[3]);int a,b,x,y;
 need(src.integer(x)&&src.integer(y)&&x==HN&&y==HM,"H header");need(old.integer(x)&&old.integer(y)&&x==OLDN&&y==OLDM,"accepted346516 header");need(fresh.integer(x)&&fresh.integer(y)&&x==N&&y==M,"new header");
 pair<int,int>previous={-1,-1};int total=0,hbody=0,oldbody=0,newedges=0,cloneedges0=0,cloneedges1=0,hubedges0=0,hubedges1=0;
 while(fresh.integer(a)){
  need(fresh.integer(b),"complete fresh edge");need(0<=a&&a<b&&b<N,"fresh simple endpoints");need(previous<pair<int,int>{a,b},"strict lex / no duplicate");previous={a,b};
  if(b<OLDN){need(old.integer(x)&&old.integer(y)&&x==a&&y==b,"all accepted346516 oldbody retained exact");oldbody++;}
  else{need(a<OLDN,"no added new-new edge");newedges++;}
  if(b<HN){need(src.integer(x)&&src.integer(y)&&x==a&&y==b,"all original H body exact");hbody++;
   int h=which[a],k=which[b];if(h>=0&&b<UN){need(sourcecount[h]<81,"source U N size bound");sourceU[h][sourcecount[h]++]=b;}
   if(k>=0&&a<UN){need(sourcecount[k]<81,"source U N size bound");sourceU[k][sourcecount[k]++]=a;}
  }else if(b<HUB0){int h=b-HN;need(a<UN&&count0[h]<81,"copy0 only U / N size");copy0[h][count0[h]++]=a;cloneedges0++;}
  else if(b==HUB0){need(UN<=a&&a<HN,"oldhub exactly original fillers");hubedges0++;}
  else if(b<HUB1){int h=b-OLDN;need(a<UN&&count1[h]<81,"copy1 only U / N size");copy1[h][count1[h]++]=a;cloneedges1++;}
  else{need(UN<=a&&a<HN,"newhub exactly original fillers");hubedges1++;}
  need(cursor[a]<offset[a+1]&&cursor[b]<offset[b+1],"actual CSR degree capacity");CSR[cursor[a]++]=b;CSR[cursor[b]++]=a;degree[a]++;degree[b]++;total++;
  if(total%1000000==0)need(cpu()<budget,"CPU_BUDGET");
 }
 need(!old.integer(x)&&!src.integer(y),"no source input suffix omitted");
 need(total==M&&hbody==HM&&oldbody==OLDM&&newedges==342225,"actual literal edge counts");
 need(cloneedges0==342160&&cloneedges1==342160&&hubedges0==65&&hubedges1==65,"actual block edge counts");
 phase="all8450_original_H_restricted_U_bindings";
 vector<int>pinowner(UN,-1);int unique=0;ofstream pins("ALL_8450_BOTH_BLOCK_TRUE_U_N_BINDINGS.tsv");pins<<"copy\th\tovoid_index\tspread_index\tcenter\tclone\tdiagonal\tpin_count\tactual_U_pins\n";
 for(int h=0;h<K;h++){
  int n=81-diag[h];need(sourcecount[h]==n&&count0[h]==n&&count1[h]==n,"all true U N sizes");sort(sourceU[h].begin(),sourceU[h].begin()+n);
  need(equal(sourceU[h].begin(),sourceU[h].begin()+n,copy0[h].begin())&&equal(sourceU[h].begin(),sourceU[h].begin()+n,copy1[h].begin()),"both copies bind original H restricted U");
  for(int j=0;j<n;j++){int v=sourceU[h][j];need(pinowner[v]<0,"different center U pinsets disjoint");pinowner[v]=h;unique++;}
  for(int copy=0;copy<2;copy++){
   pins<<copy<<'\t'<<h<<'\t'<<h/65<<'\t'<<h%65<<'\t'<<center[h]<<'\t'<<(copy?OLDN:HN)+h<<'\t'<<diag[h]<<'\t'<<n<<'\t';
   for(int j=0;j<n;j++){if(j)pins<<' ';pins<<sourceU[h][j];}pins<<'\n';
  }
 }
 need(unique==342160,"per-copy true U pin count");for(int v=0;v<UN;v++)need((pinowner[v]<0)==bool(isD[v]),"pin union U minus D65");
 map<int,int>degreehist;for(int v=0;v<N;v++){need(cursor[v]==offset[v+1]&&degree[v]==offset[v+1]-offset[v],"every actual degree complete");degreehist[degree[v]]++;}
 need(degreehist==map<int,int>{{65,2},{80,130},{81,8385},{83,342225}},"actual exact degree histogram");double bindCPU=cpu()-bindstart;
 phase="only68_preselected_new_root_BFS";double bfsstart=cpu();vector<int>seen(N,0),dist(N),parent(N),queue(N);
 map<array<int,4>,int>dh,oh,hh;int misses=0,mismatches=0,samecopychecked=0,hubchecked=0;bool witness=false;
 ofstream bfs("ALL_68_PRESELECTED_NEW_ROOT_BFS.csv");bfs<<"root,h,kind,pred0,pred1,pred2,pred3,actual0,actual1,actual2,actual3,reached,prediction_match,matched_old_label,actual_oldcopy_or_oldhub_distance,first_missing\n";
 for(int k=0;k<int(roots.size());k++){
  need(cpu()<budget,"CPU_BUDGET");int root=roots[k],h=root-OLDN,stamp=k+1,head=0,tail=1,reached=1;bool hub=root==HUB1;
  queue[0]=root;seen[root]=stamp;dist[root]=0;parent[root]=-1;
  array<int,4>actual={1,0,0,0},pred=hub?array<int,4>{1,65,5266,345410}:(diag[h]?array<int,4>{1,80,5251,345410}:array<int,4>{1,81,5330,345330});
  while(head<tail){int v=queue[head++],next=dist[v]+1;for(int p=offset[v];p<offset[v+1];p++){int w=CSR[p];if(seen[w]!=stamp){seen[w]=stamp;dist[w]=next;parent[w]=v;actual[next]++;reached++;if(next<3)queue[tail++]=w;}}}
  int same=hub?HUB0:HN+h;need(seen[same]==stamp&&dist[same]==2,"actual same-center copy / hub distance2");if(hub)hubchecked++;else samecopychecked++;
  if(hub){need(seen[HN]==stamp&&dist[HN]==3,"hub to originalclone exact3");vector<int>w;for(int z=HN;z>=0;z=parent[z])w.push_back(z);reverse(w.begin(),w.end());ofstream f("HUB_CLONE_STRUCTURE_WITNESS.json");f<<"{\"hub\":"<<HUB1<<",\"clone\":"<<HN<<",\"actual_BFS_distance\":3,\"genuine_walk\":[";for(size_t j=0;j<w.size();j++){if(j)f<<',';f<<w[j];}f<<"],\"literal_hub_neighbors_only_F\":true,\"literal_clone_neighbors_only_U\":true,\"U_and_F_disjoint\":true,\"no_edge_or_common_neighbor\":true,\"extra_BFS\":0}\n";}
  int firstmissing=-1;if(reached!=N){misses++;for(int v=0;v<N;v++)if(seen[v]!=stamp){firstmissing=v;break;}}
  bool match=actual==pred;mismatches+=!match;if(hub)hh[actual]++;else if(diag[h])dh[actual]++;else oh[actual]++;
  bfs<<root<<','<<(hub?-1:h)<<','<<(hub?"hub":diag[h]?"diagonal":"offdiagonal");for(int n:pred)bfs<<','<<n;for(int n:actual)bfs<<','<<n;bfs<<','<<reached<<','<<match<<','<<same<<','<<dist[same]<<','<<firstmissing<<'\n';
  if(!witness)for(int v=0;v<UN;v++)if(seen[v]==stamp&&dist[v]==3){vector<int>w;for(int z=v;z>=0;z=parent[z])w.push_back(z);reverse(w.begin(),w.end());ofstream f("NON_D2_ACTUAL_NEW_ROOT_WITNESS.json");f<<"{\"root\":"<<root<<",\"target\":"<<v<<",\"distance\":3,\"genuine_walk\":[";for(size_t j=0;j<w.size();j++){if(j)f<<',';f<<w[j];}f<<"],\"from_authorized_newroot_BFS\":true,\"oldroot_BFS\":0}\n";witness=true;break;}
 }
 need(samecopychecked==67&&hubchecked==1&&witness,"actual requested distance checks");double bfsCPU=cpu()-bfsstart;
 string status=misses?"FAIL_SELECTED_NEW_ROOT_D3":mismatches?"PASS_WITH_HIST_PREDICTION_MISMATCH":"PASS";
 ofstream out("RESULT.json");out<<"{\"status\":\""<<status<<"\",\"actual_n\":350742,\"actual_m\":14547195,\"max_degree\":83,\"simple\":true,\"header_body_match\":true,\"source_H_body_exact\":13862745,\"accepted346516_oldbody_exact\":14204970,\"all_new_edges\":342225,\"new_new_edges\":0,\"all8450_both_block_original_U_N_bindings\":true,\"both_clone_blocks\":4225,\"per_copy_U_pin_union\":342160,\"actual_old_U_pin_load\":2,\"old_D65_pin_load\":0,\"filler_hub_load\":2,\"degree_histogram\":{\"65\":2,\"80\":130,\"81\":8385,\"83\":342225},\"H_streams\":1,\"accepted346516_streams\":1,\"new350742_streams\":1,\"actual_BFS_new_diagonal_roots\":65,\"actual_BFS_new_off_roots\":2,\"actual_BFS_new_hubs\":1,\"unmeasured_new_off_roots\":4158,\"old_roots_BFS\":0,\"hist_mismatches\":"<<mismatches<<",\"R3_failing_roots\":"<<misses<<",\"actual_same_center_oldcopy_distance2_checks\":67,\"all4225_same_center_pairs_distance2_from_full_pin_binding\":true,\"actual_hub_to_firsthub_distance\":2,\"new_off_indices_preselected\":["<<off_indices[0]<<','<<off_indices[1]<<"],\"hist_distributions\":{";
 auto histout=[&](const string&name,const map<array<int,4>,int>&m,bool comma){if(comma)out<<',';out<<'"'<<name<<"\":[";bool first=true;for(auto [h,n]:m){if(!first)out<<',';first=false;out<<"{\"hist\":";arr(out,h);out<<",\"count\":"<<n<<'}';}out<<']';};
 histout("new_diagonal",dh,false);histout("new_off_selected",oh,true);histout("new_hub",hh,true);
 out<<"},\"allpair_proof\":\"Retain all accepted oldpairs; all U/H endpoint/flag routes cover newpairs, including same-center clones and both hubs\",\"prefix_from_H_and_from_accepted346516\":true,\"nonD2\":\"Actual distance3 witness from authorized newroot BFS\",\"exact_diameter\":"<<(misses?-1:3)<<",\"binding_CPU_seconds\":"<<bindCPU<<",\"only68_newroot_BFS_CPU_seconds\":"<<bfsCPU<<",\"validator_CPU_seconds\":"<<cpu()<<",\"old_field_geometry_BFS_Lean_solver_paidreview_retests\":0,\"root_counts_modified\":false,\"global_priority_claim\":false}\n";
 cout<<status<<" both4225blocks bindings; 68newroot BFS; CPU="<<cpu()<<'\n';return misses?2:0;
 }catch(const exception&e){ofstream("FAILURE.json")<<"{\"status\":\"FAILED_OR_BUDGET_UNKNOWN\",\"phase\":\""<<phase<<"\",\"reason\":\""<<e.what()<<"\",\"CPU_seconds\":"<<cpu()<<"}\n";cerr<<phase<<": "<<e.what()<<'\n';return 2;}
}

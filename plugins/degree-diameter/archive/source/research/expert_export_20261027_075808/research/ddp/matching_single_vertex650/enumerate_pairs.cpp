// Complete finite two-edge / one-vertex augmentation. No regularity restriction on the new vertex.
#include <algorithm>
#include <array>
#include <chrono>
#include <climits>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t stop_requested=0;
void handle_stop(int){stop_requested=1;}
constexpr int N=650,M=1625,NN=651,W=11;
struct FullResult { long long bad=0,old_bad=0,new_bad=0;int diameter=0;array<long long,NN>hist{}; };
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage SOURCE CRITICAL_PAIRS CPU_SECONDS OUTPUT_PREFIX\n";return 2;}
 clock_t start_cpu=clock();auto start_wall=chrono::steady_clock::now();
 auto cpu=[&](){return double(clock()-start_cpu)/CLOCKS_PER_SEC;};double limit=stod(argv[3]);string prefix=argv[4];
 signal(SIGINT,handle_stop);signal(SIGTERM,handle_stop);
 ifstream source(argv[1]);int n,m;source>>n>>m;if(n!=N||m!=M)return 2;
 vector<pair<int,int>>edges(M);vector<vector<int>>source_adj(N);set<pair<int,int>>edge_set;
 for(auto&[u,v]:edges){if(!(source>>u>>v)||u<0||u>=v||v>=N||!edge_set.emplace(u,v).second)return 2;source_adj[u].push_back(v);source_adj[v].push_back(u);}
 for(auto&a:source_adj)if(a.size()!=5)return 2;string extra;if(source>>extra)return 2;
 ifstream pair_file(argv[2]);long long expected_incidence;pair_file>>n>>m>>expected_incidence;if(n!=N||m!=M)return 2;
 vector<vector<int>>critical(M);long long incidence=0;
 for(int e=0;e<M;e++){
  int eid,count;if(!(pair_file>>eid>>count)||eid!=e)return 2;critical[e].resize(count);incidence+=count;
  for(int j=0;j<count;j++){int&code=critical[e][j];if(!(pair_file>>code)||code/N>=code%N||code%N>=N||(j&&critical[e][j-1]>=code))return 2;}
 }if(incidence!=expected_incidence||pair_file>>extra)return 2;
 vector<unsigned char>distance(N*N),edge_distance(M*N);vector<array<unsigned long long,W>>balls(N),edge_balls(M);
 vector<int>queue(NN);
 for(int root=0;root<N;root++){
  auto*d=&distance[root*N];fill(d,d+N,255);int head=0,end=1;queue[0]=root;d[root]=0;
  while(head<end){int u=queue[head++];for(int v:source_adj[u])if(d[v]==255){d[v]=d[u]+1;queue[end++]=v;}}
  if(end!=N||*max_element(d,d+N)>5)return 2;
  for(int x=0;x<N;x++)if(d[x]<=4)balls[root][x/64]|=1ULL<<(x%64);
 }
 for(int e=0;e<M;e++){
  auto[u,v]=edges[e];for(int word=0;word<W;word++)edge_balls[e][word]=balls[u][word]|balls[v][word];
  for(int x=0;x<N;x++)edge_distance[e*N+x]=min(distance[u*N+x],distance[v*N+x]);
 }
 double preprocess_cpu=cpu();
 auto new_missing=[&](int i,int j){int count=0;for(int w=0;w<W;w++)count+=__builtin_popcountll(edge_balls[i][w]|edge_balls[j][w]);return N-count;};
 auto old_lower=[&](int i,int j,int&first_witness){
  int count=0;size_t a=0,b=0;auto&A=critical[i];auto&B=critical[j];
  while(a<A.size()||b<B.size()){
   int code;if(b==B.size()||(a<A.size()&&A[a]<B[b]))code=A[a++];
   else if(a==A.size()||B[b]<A[a])code=B[b++];else{code=A[a];a++;b++;}
   int x=code/N,y=code%N;
   int tx=min(edge_distance[i*N+x],edge_distance[j*N+x]);
   int ty=min(edge_distance[i*N+y],edge_distance[j*N+y]);
   if(tx+ty>3){if(!count)first_witness=code;count++;}
  }return count;
 };
 vector<vector<int>>candidate_adj(NN);
 auto build=[&](int i,int j){
  for(auto&a:candidate_adj)a.clear();
  for(int e=0;e<M;e++)if(e!=i&&e!=j){auto[u,v]=edges[e];candidate_adj[u].push_back(v);candidate_adj[v].push_back(u);}
  for(int e:{i,j})for(int x:{edges[e].first,edges[e].second}){candidate_adj[x].push_back(N);candidate_adj[N].push_back(x);}
  for(int x=0;x<N;x++)if(candidate_adj[x].size()!=5)throw runtime_error("old degree mismatch");
  if(candidate_adj[N].size()!=4)throw runtime_error("new degree mismatch");
 };
 auto full_bfs=[&](){
  FullResult result;vector<int>d(NN);
  for(int root=0;root<NN;root++){
   fill(d.begin(),d.end(),-1);int head=0,end=1;queue[0]=root;d[root]=0;
   while(head<end){int u=queue[head++];for(int v:candidate_adj[u])if(d[v]<0){d[v]=d[u]+1;queue[end++]=v;}}
   if(end!=NN)throw runtime_error("unexpected disconnected augmentation");
   for(int v=0;v<NN;v++){result.hist[d[v]]++;result.diameter=max(result.diameter,d[v]);if(v>root&&d[v]>5){result.bad++;if(v==N)result.new_bad++;else result.old_bad++;}}
  }return result;
 };
 auto write_graph=[&](const string&name){
  ofstream out(name);out<<NN<<" "<<M+2<<"\n";for(int u=0;u<NN;u++)for(int v:candidate_adj[u])if(u<v)out<<u<<" "<<v<<"\n";
 };
 auto save=[&](const string&name,int i,int j,int newmiss,int oldlb,int witness,const FullResult*full){
  build(i,j);write_graph(name+".edges");ofstream out(name+".json");
  out<<"{\"n\":651,\"edges\":1627,\"maximum_degree\":5,\"new_vertex_degree\":4,\"edge_ids\":["<<i<<","<<j<<"],\"removed_edges\":[["<<edges[i].first<<","<<edges[i].second<<"],["<<edges[j].first<<","<<edges[j].second<<"]],\"new_root_missing_exact\":"<<newmiss<<",\"old_old_lower_bound\":";
  if(oldlb<0)out<<"null";else out<<oldlb;out<<",\"old_old_witness\":";
  if(witness<0)out<<"null";else out<<"["<<witness/N<<","<<witness%N<<"]";
  out<<",\"all_roots_checked\":"<<(full?NN:0);
  if(full){out<<",\"diameter\":"<<full->diameter<<",\"actual_bad_unordered_pairs\":"<<full->bad<<",\"actual_old_old_bad\":"<<full->old_bad<<",\"actual_new_old_bad\":"<<full->new_bad<<",\"ordered_distance_histogram\":{";bool comma=false;for(int d=0;d<NN;d++)if(full->hist[d]){out<<(comma?",":"")<<"\""<<d<<"\":"<<full->hist[d];comma=true;}out<<"}";}
  out<<",\"seconds_at_save\":"<<cpu()<<"}\n";
 };
 long long considered=0,shared=0,disjoint=0,coverage_fail=0,coverage_pass=0,old_fail=0,necessary_pass=0,verified=0;
 int completed_rows=0,next_i=0,next_j=1,best_new=N+1,best_old=INT_MAX,best_i=-1,best_j=-1;
 long long best_actual=LLONG_MAX;bool found=false,budget=false;
 map<int,long long>new_missing_hist,old_lower_hist;
 ofstream progress(prefix+".progress.jsonl"),verified_records(prefix+".verified.jsonl");
 for(int i=0;i<M-1&&!found&&!budget&&!stop_requested;i++){
  bool row_complete=true;for(int j=i+1;j<M;j++){
   next_i=i;next_j=j;if(stop_requested||cpu()>=limit){budget=!stop_requested;row_complete=false;break;}
   considered++;auto[a,b]=edges[i];auto[c,d]=edges[j];
   if(a==c||a==d||b==c||b==d){shared++;continue;}
   disjoint++;int nm=new_missing(i,j);new_missing_hist[nm]++;
   if(nm){coverage_fail++;if(nm<best_new){best_new=nm;best_old=INT_MAX;best_i=i;best_j=j;save(prefix+".best_filtered",i,j,nm,-1,-1,nullptr);}continue;}
   coverage_pass++;int witness=-1,lb=old_lower(i,j,witness);old_lower_hist[lb]++;
   if(best_new>0||lb<best_old){best_new=0;best_old=lb;best_i=i;best_j=j;save(prefix+".best_filtered",i,j,0,lb,witness,nullptr);}
   if(lb){old_fail++;continue;}
   necessary_pass++;build(i,j);FullResult f=full_bfs();verified++;
   if(f.new_bad!=0)throw runtime_error("coverage filter/BFS mismatch");
   verified_records<<"{\"edge_ids\":["<<i<<","<<j<<"],\"bad_pairs\":"<<f.bad<<",\"diameter\":"<<f.diameter<<"}\n";verified_records.flush();
   if(f.bad<best_actual){best_actual=f.bad;save(prefix+".best_verified",i,j,0,0,-1,&f);cout<<"best verified "<<best_actual<<" edges "<<i<<" "<<j<<" cpu "<<cpu()<<endl;}
   if(f.bad==0){found=true;save(prefix+".success",i,j,0,0,-1,&f);row_complete=j==M-1;next_i=i;next_j=j+1;break;}
  }
  if(row_complete){completed_rows++;next_i=i+1;next_j=i+2;}
  progress<<"{\"outer_edge\":"<<i<<",\"row_complete\":"<<(row_complete?"true":"false")<<",\"pairs_considered\":"<<considered<<",\"next_i\":"<<next_i<<",\"next_j\":"<<next_j<<",\"coverage_pass\":"<<coverage_pass<<",\"necessary_pass\":"<<necessary_pass<<",\"cpu_seconds\":"<<cpu()<<"}\n";progress.flush();
 }
 bool complete=considered==1LL*M*(M-1)/2;
 string status=found?"SUCCESS_FULL_BFS":complete?"COMPLETE_NO_SOLUTION":stop_requested?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 if(complete&&(shared!=6500||disjoint!=1313000))return 2;
 ofstream out(prefix+".summary.json");out<<"{\"status\":\""<<status<<"\",\"source_vertices\":650,\"source_edges\":1625,\"candidate_vertices\":651,\"maximum_degree\":5,\"new_vertex_degree\":4,\"total_unordered_edge_pairs\":1319500,\"pairs_considered\":"<<considered<<",\"shared_endpoint_rejected\":"<<shared<<",\"disjoint_pairs\":"<<disjoint<<",\"new_root_coverage_rejected\":"<<coverage_fail<<",\"new_root_coverage_passed\":"<<coverage_pass<<",\"old_lower_bound_rejected\":"<<old_fail<<",\"necessary_conditions_passed\":"<<necessary_pass<<",\"full_graphs_checked\":"<<verified<<",\"completed_outer_rows\":"<<completed_rows<<",\"next_pair_indices\":["<<next_i<<","<<next_j<<"],\"best_filtered_edge_ids\":["<<best_i<<","<<best_j<<"],\"best_filtered_new_root_missing\":"<<best_new<<",\"best_filtered_old_lower_bound\":";
 if(best_old==INT_MAX)out<<"null";else out<<best_old;out<<",\"best_verified_bad_pairs\":";if(best_actual==LLONG_MAX)out<<"null";else out<<best_actual;
 out<<",\"new_root_missing_histogram\":{";bool comma=false;for(auto[x,c]:new_missing_hist){out<<(comma?",":"")<<"\""<<x<<"\":"<<c;comma=true;}
 out<<"},\"old_lower_bound_histogram_after_new_root_coverage\":{";comma=false;for(auto[x,c]:old_lower_hist){out<<(comma?",":"")<<"\""<<x<<"\":"<<c;comma=true;}
 out<<"},\"preprocess_cpu_seconds\":"<<preprocess_cpu<<",\"cpu_seconds\":"<<cpu()<<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start_wall).count()<<"}\n";
 cout<<"terminal "<<status<<" considered "<<considered<<" disjoint "<<disjoint<<" coverage_pass "<<coverage_pass<<" necessary_pass "<<necessary_pass<<" verified "<<verified<<" best_filter "<<best_new<<"/"<<best_old<<" cpu "<<cpu()<<endl;
}

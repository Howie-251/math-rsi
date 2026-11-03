#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;
constexpr int E=16,F=13,G=64,QP=32,N=256,Z=8192,SLOTS=512;
using State=array<int,E>;
array<int,E> eu,ev,edgebit;
array<int,3> tree;
array<int,F> free_edges;
int product[G][G],inv[G];
struct Walk {int parent,end,dart,mask,length;};
struct Form {int mask,b,length;};
array<vector<Walk>,4> walks;
array<vector<Form>,SLOTS> slots;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T>void list(ostream&o,const T&v){o<<'[';bool c=false;for(auto x:v){if(c)o<<',';c=true;o<<x;}o<<']';}
int quotient(int g){return g%16+16*(g/32);}
int section(int q){return q%16+32*(q/16);}
int parity(int x){return __builtin_parity((unsigned)x);}
struct LinearSystem {
 array<int,F> pivot{};bool consistent=true;int rank=0;
 void add(int row){
  if(!consistent)return;
  for(int k=F-1;k>=0;k--)if(row&(1<<k)){
   if(pivot[k])row^=pivot[k];else{pivot[k]=row;rank++;return;}
  }
  if(row&(1<<F))consistent=false;
 }
 int solve(int initial,bool homogeneous)const{
  int x=initial;
  for(int k=0;k<F;k++)if(pivot[k]){
   int value=parity((pivot[k]&(Z-1))&x)^(homogeneous?0:(pivot[k]>>F));
   if(value)x|=1<<k;
  }
  return x;
 }
 vector<int> basis()const{vector<int>b;for(int k=0;k<F;k++)if(!pivot[k])b.push_back(solve(1<<k,true));return b;}
};
template<class Function>void solutions(const LinearSystem&s,Function fn){
 if(!s.consistent)return;auto basis=s.basis();int x=s.solve(0,false),count=1<<basis.size();
 for(int k=0;k<count;k++){fn(x);if(k+1<count)x^=basis[__builtin_ctz((unsigned)(k+1))];}
}
void initialize(const string&base,State&source){
 ifstream input(base+"/input.txt");int edges;input>>edges;assert(edges==E);
 for(int e=0;e<E;e++)input>>eu[e]>>ev[e];
 for(int&t:tree)input>>t;
 edgebit.fill(0);int j=0;for(int e=0;e<E;e++)if(find(tree.begin(),tree.end(),e)==tree.end()){free_edges[j]=e;edgebit[e]=1<<j;j++;}assert(j==F);
 for(int&x:source)input>>x;assert(input);for(int e:tree)assert(source[e]==0);
 for(int g=0;g<G;g++)for(int h=0;h<G;h++)product[g][h]=((g%32+(g/32?-(h%32):h%32)+16*(g/32)*(h/32)+32)%32)+32*((g/32)^(h/32));
 for(int g=0;g<G;g++){inv[g]=g/32?((g%32+16)%32+32):(32-g)%32;assert(product[g][inv[g]]==0&&product[inv[g]][g]==0);}
 array<vector<int>,4>darts;for(int e=0;e<E;e++){assert(eu[e]<ev[e]);darts[eu[e]].push_back(2*e);darts[ev[e]].push_back(2*e+1);}for(auto&d:darts)assert(d.size()==8);
 for(int r=0;r<4;r++){
  walks[r].push_back({-1,r,-1,0,0});
  for(size_t i=0;i<walks[r].size();i++){
   Walk w=walks[r][i];if(w.length==3)continue;
   for(int d:darts[w.end])if(w.dart<0||d!=(w.dart^1))walks[r].push_back({int(i),(d&1)?eu[d/2]:ev[d/2],d,w.mask^edgebit[d/2],w.length+1});
  }
  assert(walks[r].size()==457);
 }
}
array<int,4> make_forms(const State&q){
 for(auto&v:slots)v.clear();array<int,32>dart;
 for(int e=0;e<E;e++){dart[2*e]=section(q[e]);dart[2*e+1]=inv[dart[2*e]];}
 array<int,4>empty{};
 for(int r=0;r<4;r++){
  vector<int>values(walks[r].size());
  for(size_t i=0;i<walks[r].size();i++){
   const Walk&w=walks[r][i];int value=i?product[values[w.parent]][dart[w.dart]]:0;values[i]=value;
   slots[r*128+w.end*32+quotient(value)].push_back({w.mask,(value%32)/16,w.length});
  }
  for(int j=0;j<128;j++)empty[r]+=slots[r*128+j].empty();
 }
 return empty;
}
LinearSystem legal_system(const State&q){
 LinearSystem s;
 for(int e=0;e<E;e++)for(int f=0;f<e;f++)if(eu[e]==eu[f]&&ev[e]==ev[f]&&q[e]==q[f])s.add((edgebit[e]^edgebit[f])|(1<<F));
 return s;
}
State lift(const State&q,int z){State h{};for(int e=0;e<E;e++)h[e]=section(q[e])+16*parity(z&edgebit[e]);return h;}
array<int,4> misses(int z){
 array<int,4>m{};
 for(int s=0;s<SLOTS;s++){
  int mask=0;for(auto f:slots[s])mask|=1<<(f.b^parity(f.mask&z));
  m[s/128]+=2-__builtin_popcount((unsigned)mask);
 }
 return m;
}
void scoreout(ostream&o,const array<int,4>&m,int score){o<<"{\"root_misses\":";list(o,m);o<<",\"score_sum\":"<<score<<",\"bad_unordered_pairs\":"<<32*score<<'}';}
void calibration(const string&base,int cursor,const State&q,int z,int expected_score){
 auto h=lift(q,z);auto m=misses(z);int sum=0;for(int x:m)sum+=x;assert(sum==expected_score);
 ofstream o(base+"/first.formal_center.json");o<<"{\"projection_cursor\":"<<cursor<<",\"center_mask\":"<<z<<",\"projection\":";list(o,q);o<<",\"voltages\":";list(o,h);o<<",\"score\":";scoreout(o,m,sum);o<<",\"score_reused_in_production\":true,\"slots\":[";
 for(int s=0;s<SLOTS;s++){
  if(s)o<<',';o<<'[';bool comma=false;for(auto f:slots[s]){if(comma)o<<',';comma=true;o<<'['<<f.mask<<','<<f.b<<','<<f.length<<']';}o<<']';
 }
 o<<"],\"radius3_distances\":[";
 for(int r=0;r<4;r++){
  if(r)o<<',';array<int,N>d;d.fill(-1);
  for(int j=0;j<128;j++)for(auto f:slots[r*128+j]){int orbit=j/32,qp=j%32,c=f.b^parity(f.mask&z);int v=64*orbit+section(qp)+16*c;int length=f.length;if(d[v]<0||length<d[v])d[v]=length;}
  list(o,d);
 }
 o<<"]}\n";
}
void save_best(const string&base,int cursor,const State&q,int z,int score){
 State h=lift(q,z);auto m=misses(z);int sum=0;for(int x:m)sum+=x;assert(sum==score);
 ofstream o(base+"/best.json");o<<"{\"selection\":\"minimum radius3 deficit among legal central lifts of quotient-complete projections actually scored\",\"not_global_minimum_over_quotient_rejected_projections\":true,\"n\":256,\"m\":1024,\"degree\":8,\"target_diameter\":3,\"group_name\":\"Q64\",\"group_twist\":16,\"projection_cursor\":"<<cursor<<",\"center_mask\":"<<z<<",\"projection\":";list(o,q);o<<",\"voltages\":";list(o,h);o<<",\"edge_u\":";list(o,eu);o<<",\"edge_v\":";list(o,ev);o<<",\"tree_edge_indices\":";list(o,tree);o<<",\"free_edge_indices\":";list(o,free_edges);o<<",\"score\":";scoreout(o,m,score);o<<"}\n";
 ofstream edges(base+"/best.edges");edges<<"256 1024\n";
 for(int e=0;e<E;e++)for(int g=0;g<G;g++)edges<<64*eu[e]+g<<' '<<64*ev[e]+product[g][h[e]]<<'\n';
}
int main(int argc,char**argv){
 assert(argc==3);string base=argv[1];double started=cpu(),limit=stod(argv[2]);State source;initialize(base,source);
 uint64_t quotient_rejected=0,no_legal=0,center_entered=0,raw_centers=0,legal_centers=0,illegal_centers=0,sparse_increments=0,slot_naive_visits=0;
 int completed=0,best=1025,best_cursor=-1;bool found=false,timeout=false,calibrated=false;
 ofstream results(base+"/projections.jsonl");array<int,Z>scores{};array<bool,Z>legal{};
 for(int k=0;k<F;k++)for(int value=0;value<QP;value++)if(value!=source[free_edges[k]]){
  int cursor=k*31+value-(value>source[free_edges[k]]);assert(cursor==completed);
  if(cpu()-started>=limit){timeout=true;goto done;}
  State q=source;q[free_edges[k]]=value;auto empty=make_forms(q);int total_empty=0;for(int x:empty)total_empty+=x;
  results<<"{\"cursor\":"<<cursor<<",\"changed_edge\":"<<free_edges[k]<<",\"new_quotient_value\":"<<value<<",\"empty_slots_by_root\":";list(results,empty);
  if(total_empty){quotient_rejected++;completed++;results<<",\"status\":\"QUOTIENT_MISSING\",\"central_assignments_scored\":0}\n";continue;}
  auto constraints=legal_system(q);
  if(!constraints.consistent){no_legal++;completed++;results<<",\"status\":\"NO_LEGAL_CENTRAL_ASSIGNMENT\",\"central_assignments_scored\":0}\n";continue;}
  center_entered++;scores.fill(0);legal.fill(false);solutions(constraints,[&](int z){legal[z]=true;});
  array<int,F+1>rank_counts{};int constant_penalty=0,inconsistent=0;uint64_t increments=0;
  for(int s=0;s<SLOTS;s++){
   assert(!slots[s].empty());auto first=slots[s][0];LinearSystem eq;
   for(auto f:slots[s])eq.add((f.mask^first.mask)|((f.b^first.b)<<F));
   if(!eq.consistent){inconsistent++;continue;}
   rank_counts[eq.rank]++;
   if(eq.rank==0){constant_penalty++;continue;}
   solutions(eq,[&](int z){scores[z]++;increments++;});
  }
  sparse_increments+=increments;slot_naive_visits+=uint64_t(SLOTS)*Z;
  int this_legal=0,this_illegal=0,min_score=1025,min_z=-1,first_legal=-1;
  for(int z=0;z<Z;z++){
   raw_centers++;
   if(!legal[z]){illegal_centers++;this_illegal++;continue;}
   legal_centers++;this_legal++;int score=scores[z]+constant_penalty;
   if(first_legal<0){first_legal=z;if(!calibrated){calibration(base,cursor,q,z,score);calibrated=true;}}
   if(score<min_score){min_score=score;min_z=z;}
   if(score<best){best=score;best_cursor=cursor;save_best(base,cursor,q,z,score);cout<<"BEST projection="<<cursor<<" z="<<z<<" score="<<score<<" bad="<<32*score<<" CPU="<<cpu()-started<<endl;}
   if(score==0){found=true;break;}
  }
  results<<",\"status\":\""<<(found?"FOUND_D3":"CENTRAL_COMPLETE_NO_D3")<<"\",\"legal_center_count_scored\":"<<this_legal<<",\"illegal_center_count\":"<<this_illegal<<",\"minimum_score\":"<<min_score<<",\"minimum_center_mask\":"<<min_z<<",\"first_legal_center_mask\":"<<first_legal<<",\"constant_bad_slots\":"<<constant_penalty<<",\"inconsistent_bad_system_slots\":"<<inconsistent<<",\"consistent_bad_system_rank_histogram\":";list(results,rank_counts);results<<",\"sparse_score_increments\":"<<increments<<",\"unfiltered_8192_by512_slot_visits\":"<<uint64_t(SLOTS)*Z<<"}\n";
  completed++;if(found)goto done;
 }
done:
 string status=found?"FOUND_D3":timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_403_NO_D3";
 ofstream out(base+"/search.terminal.json");out<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"planned_projections\":403,\"completed_projections\":"<<completed<<",\"quotient_missing_rejected\":"<<quotient_rejected<<",\"no_legal_center_rejected\":"<<no_legal<<",\"projections_entering_center_scoring\":"<<center_entered<<",\"raw_central_assignments_examined\":"<<raw_centers<<",\"legal_central_assignments_scored\":"<<legal_centers<<",\"illegal_central_assignments\":"<<illegal_centers<<",\"sparse_score_increments\":"<<sparse_increments<<",\"unfiltered_8192_by512_slot_visits\":"<<slot_naive_visits<<",\"minimum_score_in_scored_center_scope\":";
 if(best<=1024)out<<best;else out<<"null";
 out<<",\"best_projection_cursor\":";if(best_cursor>=0)out<<best_cursor;else out<<"null";
 out<<",\"next_projection_cursor\":";if(timeout)out<<completed;else out<<"null";
 out<<",\"first_formal_center_saved\":"<<(calibrated?"true":"false")<<",\"production_BFS_runs\":0,\"CPU_seconds\":"<<cpu()-started<<",\"running\":false,\"scope_exhausted\":"<<(!timeout&&!found?"true":"false")<<",\"entire_Q64_family_exhausted\":false}\n";
 cout<<status<<" projections="<<completed<<" center_entered="<<center_entered<<" legal_centers="<<legal_centers<<" CPU="<<cpu()-started<<endl;
}

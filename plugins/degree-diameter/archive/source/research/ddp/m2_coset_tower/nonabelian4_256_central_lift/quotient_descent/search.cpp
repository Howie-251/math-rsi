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
#include <map>
#include <random>
#include <tuple>
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
 ofstream o(base+"/best.json");o<<"{\"selection\":\"minimum radius3 deficit among legal central lifts of L0 projections actually scored\",\"not_global_minimum_over_quotient_rejected_projections\":true,\"n\":256,\"m\":1024,\"degree\":8,\"target_diameter\":3,\"group_name\":\"Q64\",\"group_twist\":16,\"projection_cursor\":"<<cursor<<",\"center_mask\":"<<z<<",\"projection\":";list(o,q);o<<",\"voltages\":";list(o,h);o<<",\"edge_u\":";list(o,eu);o<<",\"edge_v\":";list(o,ev);o<<",\"tree_edge_indices\":";list(o,tree);o<<",\"free_edge_indices\":";list(o,free_edges);o<<",\"score\":";scoreout(o,m,score);o<<"}\n";
 ofstream edges(base+"/best.edges");edges<<"256 1024\n";
 for(int e=0;e<E;e++)for(int g=0;g<G;g++)edges<<64*eu[e]+g<<' '<<64*ev[e]+product[g][h[e]]<<'\n';
}

struct Evaluation {int L=1025,empty=513,singleton=513,M=-1,z=-1;};
bool better(const Evaluation&a,const Evaluation&b){return make_tuple(a.L,a.empty,a.L==0?a.M:0)<make_tuple(b.L,b.empty,b.L==0?b.M:0);}
void eval_json(ostream&o,const Evaluation&a){o<<"{\"L\":"<<a.L<<",\"empty_slots\":"<<a.empty<<",\"singleton_distinct_form_slots\":"<<a.singleton<<",\"minimum_center_deficit\":";if(a.M<0)o<<"null";else o<<a.M;o<<",\"minimum_center_mask\":";if(a.z<0)o<<"null";else o<<a.z;o<<'}';}
string base;double started,limit;bool found=false,timedout=false;
uint64_t evaluated=0,illegal_neighbors=0,neighbor_trials=0,full_neighborhoods=0,strict_moves=0,kick_trials=0,kicks=0,center_projections=0,raw_centers=0,legal_centers=0,illegal_centers=0,center_cache_hits=0,sparse_increments=0;
map<State,Evaluation>center_cache;
Evaluation global_best;State global_q{};int starts_completed=0,segments_completed=0;
struct Cursor {int start=0,segment=0,step=0,neighbor=0;string phase="start";State current{},neighbor_best{};Evaluation current_score,neighbor_score;};
Cursor cursor;
void cursor_json(ostream&o){o<<"{\"start\":"<<cursor.start<<",\"segment\":"<<cursor.segment<<",\"step\":"<<cursor.step<<",\"neighbor_cursor\":"<<cursor.neighbor<<",\"phase\":\""<<cursor.phase<<"\",\"current_projection\":";list(o,cursor.current);o<<",\"current_score\":";eval_json(o,cursor.current_score);o<<",\"best_neighbor_so_far\":";list(o,cursor.neighbor_best);o<<",\"best_neighbor_score_so_far\":";eval_json(o,cursor.neighbor_score);o<<'}';}
bool budget(){if(cpu()-started>=limit){timedout=true;return false;}return true;}
void progress(const string&status){ofstream o(base+"/progress.json");o<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"evaluated_legal_projections\":"<<evaluated<<",\"raw_neighbor_trials\":"<<neighbor_trials<<",\"full_neighborhoods\":"<<full_neighborhoods<<",\"center_projections\":"<<center_projections<<",\"CPU_seconds\":"<<cpu()-started<<",\"best\":";eval_json(o,global_best);o<<",\"cursor\":";cursor_json(o);o<<"}\n";}
void deduplicate_forms(){for(auto&v:slots){sort(v.begin(),v.end(),[](const Form&a,const Form&b){return tie(a.mask,a.b,a.length)<tie(b.mask,b.b,b.length);});v.erase(unique(v.begin(),v.end(),[](const Form&a,const Form&b){return a.mask==b.mask&&a.b==b.b;}),v.end());}}
Evaluation evaluate(const State&q,const LinearSystem&constraints){
 assert(constraints.consistent);evaluated++;
 auto cache=center_cache.find(q);if(cache!=center_cache.end()){center_cache_hits++;return cache->second;}
 make_forms(q);deduplicate_forms();Evaluation result;result.empty=0;result.singleton=0;
 for(const auto&v:slots){result.empty+=v.empty();result.singleton+=v.size()==1;}result.L=2*result.empty+result.singleton;
 if(result.L==0){
  center_projections++;array<int,Z>scores{};array<bool,Z>legal{};solutions(constraints,[&](int z){legal[z]=true;});int constant_bad=0;
  for(const auto&v:slots){assert(v.size()>=2);auto first=v[0];LinearSystem bad;for(auto f:v)bad.add((f.mask^first.mask)|((f.b^first.b)<<F));if(!bad.consistent)continue;if(bad.rank==0){constant_bad++;continue;}solutions(bad,[&](int z){scores[z]++;sparse_increments++;});}
  result.M=1025;
  for(int z=0;z<Z;z++){raw_centers++;if(!legal[z]){illegal_centers++;continue;}legal_centers++;int score=scores[z]+constant_bad;if(score<result.M){result.M=score;result.z=z;}if(score==0){found=true;break;}}
  assert(result.z>=0);center_cache.emplace(q,result);
 }
 return result;
}
void record_best(const State&q,const Evaluation&score){
 if(!better(score,global_best))return;global_best=score;global_q=q;
 ofstream o(base+"/best_projection.json");o<<"{\"selection\":\"lexicographic minimum L,empty slots,and exact center minimum within L0 among evaluated legal projections\",\"is_full_graph\":false,\"projection\":";list(o,q);o<<",\"score\":";eval_json(o,score);o<<",\"evaluation_index\":"<<evaluated<<",\"position\":";cursor_json(o);o<<"}\n";
 if(score.L==0){make_forms(q);save_best(base,int(evaluated),q,score.z,score.M);}
 cout<<"BEST evaluated="<<evaluated<<" L="<<score.L<<" empty="<<score.empty<<" singleton="<<score.singleton<<" M="<<score.M<<" CPU="<<cpu()-started<<endl;
}
void source_check(const State&q,const Evaluation&score){
 ifstream input(base+"/source_reference.txt");int z,expected;input>>z>>expected;make_forms(q);deduplicate_forms();calibration(base,0,q,z,expected);
 int checked=0;
 for(int r=0;r<4;r++){array<int,N>d;d.fill(-1);for(int j=0;j<128;j++)for(auto f:slots[r*128+j]){int v=64*(j/32)+section(j%32)+16*(f.b^parity(f.mask&z));if(d[v]<0||f.length<d[v])d[v]=f.length;}for(int actual:d){int want;input>>want;assert(actual==want);checked++;}}
 assert(input&&checked==1024);ofstream o(base+"/source_calibration.json");o<<"{\"source\":\"old independently verified832-bad-pair graph\",\"radius3_entries_compared\":1024,\"all_equal\":true,\"new_BFS_runs\":0,\"source_center_enumerations\":0,\"source_projection_score\":";eval_json(o,score);o<<"}\n";
}
int main(int argc,char**argv){
 assert(argc==3);base=argv[1];limit=stod(argv[2]);started=cpu();State source;initialize(base,source);
 ifstream input(base+"/starts.txt");int count;input>>count;assert(count==16);vector<State>starts(count);for(auto&q:starts)for(int&x:q)input>>x;assert(input&&starts[0]==source);
 mt19937_64 rng(20261027080ULL);ofstream events(base+"/events.jsonl");
 for(int start=0;start<count&&!found&&!timedout;start++){
  State current=starts[start];cursor={};cursor.start=start;cursor.current=current;cursor.phase="start";if(!budget())break;auto legal=legal_system(current);assert(legal.consistent);
  Evaluation score=evaluate(current,legal);cursor.current_score=score;
  if(start==0){assert(score.L>0&&center_projections==0);source_check(current,score);}record_best(current,score);if(found)break;
  for(int segment=0;segment<9&&!found&&!timedout;segment++){
   cursor.segment=segment;bool completed_segment=false;
   for(int step=0;step<30&&!found&&!timedout;step++){
    cursor.step=step;cursor.phase="full_single_coordinate_neighborhood";cursor.current=current;cursor.current_score=score;cursor.neighbor_best=current;cursor.neighbor_score=score;cursor.neighbor=0;
    State winner=current;Evaluation winner_score=score;int trial=0;
    for(int k=0;k<F&&!found&&!timedout;k++)for(int value=0;value<QP&&!found&&!timedout;value++)if(value!=current[free_edges[k]]){
     cursor.neighbor=trial;if(!budget())break;State q=current;q[free_edges[k]]=value;trial++;neighbor_trials++;auto system=legal_system(q);
     if(!system.consistent){illegal_neighbors++;continue;}auto evaluated_score=evaluate(q,system);record_best(q,evaluated_score);if(better(evaluated_score,winner_score)){winner=q;winner_score=evaluated_score;cursor.neighbor_best=winner;cursor.neighbor_score=winner_score;}
     if(evaluated%10000==0)progress("RUNNING");
    }
    if(found||timedout)break;assert(trial==403);full_neighborhoods++;
    events<<"{\"start\":"<<start<<",\"segment\":"<<segment<<",\"step\":"<<step<<",\"full403_neighbors\":true,\"from\":";eval_json(events,score);events<<",\"selected\":";eval_json(events,winner_score);events<<",\"strict_improvement\":"<<(better(winner_score,score)?"true":"false")<<"}\n";
    if(!better(winner_score,score)){completed_segment=true;break;}current=winner;score=winner_score;strict_moves++;if(step==29)completed_segment=true;
   }
   if(found||timedout)break;assert(completed_segment);segments_completed++;cursor.current=current;cursor.current_score=score;
   if(segment<8){
    cursor.phase="two_coordinate_kick";if(!budget())break;State q;LinearSystem system;
    do{if(!budget())break;kick_trials++;q=current;int a=rng()%F,b=rng()%(F-1);if(b>=a)b++;for(int index:{a,b}){int e=free_edges[index],value=rng()%31;if(value>=q[e])value++;q[e]=value;}system=legal_system(q);}while(!system.consistent);
    if(timedout)break;kicks++;current=q;score=evaluate(current,system);cursor.current=current;cursor.current_score=score;record_best(current,score);
    events<<"{\"start\":"<<start<<",\"after_segment\":"<<segment<<",\"kind\":\"two_coordinate_legal_kick\",\"projection\":";list(events,current);events<<",\"score\":";eval_json(events,score);events<<"}\n";
   }
  }
  if(!found&&!timedout){starts_completed++;progress("RUNNING");cout<<"START_COMPLETE index="<<start<<" evaluated="<<evaluated<<" bestL="<<global_best.L<<" CPU="<<cpu()-started<<endl;}
 }
 string status=found?"FOUND_D3":timedout?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_16_START_PROFILE_NO_D3";
 ofstream out(base+"/search.terminal.json");out<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"running\":false,\"starts_scope\":16,\"starts_completed\":"<<starts_completed<<",\"segments_completed\":"<<segments_completed<<",\"full403_neighborhoods\":"<<full_neighborhoods<<",\"strict_moves\":"<<strict_moves<<",\"raw_neighbor_trials\":"<<neighbor_trials<<",\"illegal_neighbor_projections\":"<<illegal_neighbors<<",\"evaluated_legal_projections\":"<<evaluated<<",\"kick_proposals\":"<<kick_trials<<",\"accepted_kicks\":"<<kicks<<",\"L0_projections_exactly_optimized\":"<<center_projections<<",\"L0_cache_hits\":"<<center_cache_hits<<",\"raw_center_masks_examined\":"<<raw_centers<<",\"legal_center_masks_scored\":"<<legal_centers<<",\"illegal_center_masks\":"<<illegal_centers<<",\"sparse_score_increments\":"<<sparse_increments<<",\"best\":";eval_json(out,global_best);out<<",\"saved_graph\":"<<(global_best.L==0?"true":"false")<<",\"found_D3\":"<<(found?"true":"false")<<",\"production_BFS_runs\":0,\"source_radius3_entries_reused\":1024,\"CPU_seconds\":"<<cpu()-started<<",\"scope_exhausted\":"<<(!found&&!timedout?"true":"false")<<",\"entire_family_exhausted\":false,\"next_cursor\":";if(timedout)cursor_json(out);else out<<"null";out<<"}\n";out.close();progress(status);cout<<status<<" evaluated="<<evaluated<<" bestL="<<global_best.L<<" M="<<global_best.M<<" CPU="<<cpu()-started<<endl;
}

#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
constexpr int N=820,Q=41,K=20,D=12;
int pw[K],product[N][N],inverse_element[N],last_distance[N];
clock_t began;double limit_seconds;string directory;
int multiply(int a,int b){return (a%Q+pw[a/Q]*(b%Q))%Q+Q*((a/Q+b/Q)%K);}
int inverse(int a){int j=a/Q;return (Q-pw[(K-j)%K]*(a%Q)%Q)%Q+Q*((K-j)%K);}
double elapsed(){return double(clock()-began)/CLOCKS_PER_SEC;}
bool exhausted(){return elapsed()>=limit_seconds;}
struct Pattern{int id,pairs,involutions,anchor;vector<int>phase;};
struct Candidate{int pattern=-1,sample=-1,seed_rank=-1,round=-1;vector<int>field;array<int,D>S;int missing=N+1,diameter=-1;bool connected=false;string stage;};
vector<Pattern>patterns;
Candidate global_best;map<int,int>global_best_hist;
bool found=false,timed_out=false;
long long profile_evaluated=0,profile_draws=0,profile_illegal=0,profile_zero=0,profile_duplicates=0,descent_evaluated=0,descent_illegal=0,descent_zero=0;
int next_pattern=0,next_sample=0,active_seed=-1,active_round=0,active_coordinate=-1,active_value=-1;
vector<int>profile_completed,profile_best;
template<class T>void array_json(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
bool zero_field(const vector<int>&v){return all_of(v.begin(),v.end(),[](int x){return x==0;});}
bool generators(Candidate&c){const auto&p=patterns[c.pattern];int k=0;for(int j=0;j<p.pairs;++j){int s=c.field[j]+Q*p.phase[j];c.S[k++]=s;c.S[k++]=inverse_element[s];}for(int j=p.pairs;j<int(p.phase.size());++j)c.S[k++]=c.field[j]+10*Q;assert(k==D);auto sorted=c.S;sort(sorted.begin(),sorted.end());return sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end();}
void evaluate(Candidate&c){
 int queue[N],front=0,tail=1;fill(last_distance,last_distance+N,-1);last_distance[0]=0;queue[0]=0;
 while(front<tail){int u=queue[front++];for(int s:c.S){int v=product[u][s];if(last_distance[v]<0){last_distance[v]=last_distance[u]+1;queue[tail++]=v;}}}
 c.connected=tail==N;c.missing=0;c.diameter=0;
 for(int d:last_distance){if(d<0||d>3)c.missing++;c.diameter=max(c.diameter,d);}if(!c.connected)c.diameter=-1;
 if(c.missing<global_best.missing){global_best=c;global_best_hist.clear();for(int d:last_distance)global_best_hist[d]++;}
 if(c.missing==0)found=true;
}
void candidate_json(ostream&o,const Candidate&c){const auto&p=patterns[c.pattern];o<<"{\"pattern_index\":"<<c.pattern<<",\"source_pattern_id\":"<<p.id<<",\"pairs\":"<<p.pairs<<",\"involutions\":"<<p.involutions<<",\"anchor_slot\":"<<p.anchor<<",\"sample_index\":"<<c.sample<<",\"seed_rank\":"<<c.seed_rank<<",\"round\":"<<c.round<<",\"origin_stage\":\""<<c.stage<<"\",\"component_phases\":";array_json(o,p.phase);o<<",\"fields\":";array_json(o,c.field);o<<",\"S\":";array_json(o,c.S);o<<",\"root_deficit\":"<<c.missing<<",\"diameter\":"<<c.diameter<<",\"connected\":"<<(c.connected?"true":"false")<<'}';}
void save_best(){
 if(global_best.pattern<0)return;
 ofstream e(directory+"/profile.best.edges");e<<N<<" 4920\n";int edges=0;for(int u=0;u<N;++u)for(int s:global_best.S){int v=product[u][s];if(u<v){e<<u<<' '<<v<<'\n';edges++;}}assert(edges==4920);
 ofstream f(directory+"/profile.best.json");f<<"{\"n\":820,\"m\":4920,\"degree\":12,\"action_root\":36,\"encoding\":\"x+41*j\",\"selection\":\"best among the fixed profile and its 16 authorized descent trajectories\",\"candidate\":";candidate_json(f,global_best);f<<",\"bad_unordered_pairs\":"<<410LL*global_best.missing<<",\"root_distance_histogram\":{";bool first=true;for(auto [d,n]:global_best_hist){if(!first)f<<',';first=false;f<<'"'<<d<<"\":"<<n;}f<<"}}\n";
}
void progress(const string&stage){ofstream o(directory+"/profile.progress.json");o<<"{\"stage\":\""<<stage<<"\",\"profile_evaluated\":"<<profile_evaluated<<",\"descent_evaluated\":"<<descent_evaluated<<",\"best_missing\":"<<global_best.missing<<",\"CPU_seconds\":"<<elapsed()<<",\"next_pattern\":"<<next_pattern<<",\"next_sample\":"<<next_sample<<",\"seed_rank\":"<<active_seed<<",\"round\":"<<active_round<<",\"coordinate\":"<<active_coordinate<<",\"value\":"<<active_value<<"}\n";}
bool top_order(const Candidate&a,const Candidate&b){if(a.missing!=b.missing)return a.missing<b.missing;if(a.pattern!=b.pattern)return a.pattern<b.pattern;return a.sample<b.sample;}
struct SeedResult{int rank,initial_missing,final_missing,accepted_rounds;long long evaluated,illegal,zero;bool converged;Candidate current;};
int main(int argc,char**argv){
 assert(argc==3);directory=argv[1];limit_seconds=stod(argv[2]);began=clock();pw[0]=1;for(int j=1;j<K;++j)pw[j]=36*pw[j-1]%Q;assert(pw[10]==40);
 for(int a=0;a<N;++a){inverse_element[a]=inverse(a);assert(multiply(a,inverse_element[a])==0&&multiply(inverse_element[a],a)==0);for(int b=0;b<N;++b)product[a][b]=multiply(a,b);}
 ifstream in(directory+"/profile.patterns.txt");int count;in>>count;assert(count==2139);patterns.resize(count);profile_completed.assign(count,0);profile_best.assign(count,N+1);
 for(auto&p:patterns){in>>p.id>>p.pairs>>p.involutions>>p.anchor;p.phase.resize(p.pairs+p.involutions);for(int j=0;j<p.pairs;++j)in>>p.phase[j];for(int j=p.pairs;j<int(p.phase.size());++j)p.phase[j]=10;assert(p.phase[p.anchor]!=0);}
 mt19937_64 rng(2026102622ULL);vector<Candidate>top;
 ofstream samples(directory+"/profile.samples.jsonl");double stage1_start=elapsed();
 for(int k=0;k<count&&!found&&!timed_out;++k){set<vector<int>>seen;const auto&p=patterns[k];
  for(int sample=0;sample<16&&!found;++sample){
   next_pattern=k;next_sample=sample;
   Candidate c;c.pattern=k;c.sample=sample;c.stage="profile";c.field.resize(p.phase.size());
   while(true){
    if(exhausted()){timed_out=true;break;}
    for(int j=0;j<int(c.field.size());++j)c.field[j]=(j==p.anchor)?0:int(rng()%Q);
    profile_draws++;
    if(zero_field(c.field)){profile_zero++;continue;}
    if(!generators(c)){profile_illegal++;continue;}
    if(seen.count(c.field)){profile_duplicates++;continue;}
    seen.insert(c.field);break;
   }
   if(timed_out)break;
   evaluate(c);profile_evaluated++;profile_completed[k]++;profile_best[k]=min(profile_best[k],c.missing);candidate_json(samples,c);samples<<'\n';
   top.push_back(c);sort(top.begin(),top.end(),top_order);if(top.size()>16)top.pop_back();
   if(found){save_best();cout<<"FOUND_D3 stage=profile pattern="<<k<<" sample="<<sample<<endl;break;}
  }
  if(!timed_out&&!found){next_pattern=k+1;next_sample=0;}
  if(k%64==63){samples.flush();progress("profile");}
 }
 samples.close();double stage1_cpu=elapsed()-stage1_start;int stage1_best=global_best.missing;
 ofstream topfile(directory+"/profile.top16.json");topfile<<'[';for(size_t i=0;i<top.size();++i){if(i)topfile<<',';candidate_json(topfile,top[i]);}topfile<<"]\n";topfile.close();
 vector<SeedResult>seed_results;ofstream steps(directory+"/profile.descent_steps.jsonl");double stage2_start=elapsed();
 if(!found&&!timed_out){assert(profile_evaluated==34224&&top.size()==16);
  for(int rank=0;rank<16&&!found&&!timed_out;++rank){
   Candidate current=top[rank];current.seed_rank=rank;current.stage="descent";const auto&p=patterns[current.pattern];
   long long seed_before=descent_evaluated,illegal_before=descent_illegal,zero_before=descent_zero;int rounds=0;bool converged=false;active_seed=rank;
   while(!found&&!timed_out){
    Candidate neighbor_best=current;active_round=rounds;
    for(int coordinate=0;coordinate<int(current.field.size())&&!found&&!timed_out;++coordinate){
     if(coordinate==p.anchor)continue;
     for(int value=0;value<Q;++value){
      if(value==current.field[coordinate])continue;
      active_coordinate=coordinate;active_value=value;
      if(exhausted()){timed_out=true;break;}
      Candidate c=current;c.field[coordinate]=value;c.round=rounds;
      if(zero_field(c.field)){descent_zero++;continue;}
      if(!generators(c)){descent_illegal++;continue;}
      evaluate(c);descent_evaluated++;
      if(c.missing<neighbor_best.missing)neighbor_best=c;
      if(found){save_best();cout<<"FOUND_D3 stage=descent seed="<<rank<<" round="<<rounds<<endl;break;}
     }
    }
    if(found){current=global_best;break;}
    if(timed_out)break;
    if(neighbor_best.missing>=current.missing){converged=true;break;}
    current=neighbor_best;rounds++;candidate_json(steps,current);steps<<'\n';steps.flush();progress("descent");
   }
   seed_results.push_back({rank,top[rank].missing,current.missing,rounds,descent_evaluated-seed_before,descent_illegal-illegal_before,descent_zero-zero_before,converged,current});
   progress("descent");
  }
 }
 steps.close();double stage2_cpu=elapsed()-stage2_start;
 string status=found?"FOUND_D3":timed_out?"CPU_LIMIT_PROFILE_STOPPED":"COMPLETE_FIXED_PROFILE_NO_SOLUTION";
 if(!found)save_best();
 ofstream seeds(directory+"/profile.descent_seeds.json");seeds<<'[';for(size_t i=0;i<seed_results.size();++i){if(i)seeds<<',';auto&s=seed_results[i];seeds<<"{\"rank\":"<<s.rank<<",\"initial_missing\":"<<s.initial_missing<<",\"final_missing\":"<<s.final_missing<<",\"accepted_rounds\":"<<s.accepted_rounds<<",\"legal_neighbors_evaluated\":"<<s.evaluated<<",\"illegal_neighbors_skipped\":"<<s.illegal<<",\"zero_neighbors_skipped\":"<<s.zero<<",\"coordinate_minimum_reached\":"<<(s.converged?"true":"false")<<",\"current\":";candidate_json(seeds,s.current);seeds<<'}';}seeds<<"]\n";seeds.close();
 int converged=0;for(auto&s:seed_results)converged+=s.converged;
 ofstream out(directory+"/profile.terminal.json");out<<"{\n\"status\":\""<<status<<"\",\"running\":false,\"fixed_seed\":2026102622,\"phase_patterns_scope\":2139,\"samples_per_pattern\":16,\"profile_scope\":34224,\"profile_actual_graphs\":"<<profile_evaluated<<",\"profile_draws\":"<<profile_draws<<",\"profile_illegal_draws\":"<<profile_illegal<<",\"profile_zero_draws\":"<<profile_zero<<",\"profile_duplicate_draws\":"<<profile_duplicates<<",\"profile_best_missing\":"<<stage1_best<<",\"profile_CPU_seconds\":"<<stage1_cpu<<",\"descent_seed_scope\":16,\"descent_seeds_started\":"<<seed_results.size()<<",\"descent_seeds_at_coordinate_minimum\":"<<converged<<",\"descent_actual_neighbor_graphs\":"<<descent_evaluated<<",\"descent_illegal_neighbors_skipped\":"<<descent_illegal<<",\"descent_zero_neighbors_skipped\":"<<descent_zero<<",\"descent_CPU_seconds\":"<<stage2_cpu<<",\"final_best_missing\":"<<global_best.missing<<",\"total_BFS_runs\":"<<profile_evaluated+descent_evaluated<<",\"CPU_seconds\":"<<elapsed()<<",\"next_profile_pattern\":"<<next_pattern<<",\"next_profile_sample\":"<<next_sample<<",\"active_descent_seed\":"<<active_seed<<",\"active_descent_round\":"<<active_round<<",\"active_descent_coordinate\":"<<active_coordinate<<",\"active_descent_value\":"<<active_value<<",\n\"samples_completed_per_pattern\":";array_json(out,profile_completed);out<<",\n\"best_missing_per_pattern\":";array_json(out,profile_best);out<<",\n\"finite_profile_not_full_field_family\":true}\n";out.close();
 progress(status);cout<<status<<" profile="<<profile_evaluated<<" profilebest="<<stage1_best<<" descent="<<descent_evaluated<<" best="<<global_best.missing<<" CPU="<<elapsed()<<endl;
}

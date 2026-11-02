#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
constexpr int Q=41,K=10,H=410,N=820;
using Fields=array<int,14>;
int powers[K],product[H][H],inverses[H];
string directory; clock_t began; double cpu_limit;
bool found=false,timed_out=false;
long long evaluated=0,neighbor_evaluated=0,illegal_neighbors=0,random_draws=0,perturb_draws=0;
int active_seed=-1,active_segment=-1,active_round=-1,active_coordinate=-1,active_value=-1;
double elapsed(){return double(clock()-began)/CLOCKS_PER_SEC;}
bool exhausted(){return elapsed()>=cpu_limit;}
int multiply(int a,int b){return (a%Q+powers[a/Q]*(b%Q))%Q+Q*((a/Q+b/Q)%K);}
template<class C>void array_json(ostream&o,const C&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
struct Candidate{Fields fields{};array<array<int,6>,2> internal{},cross{};array<int,2>missing{};array<array<int,N+1>,2>hist{};int score=2*N+1,diameter=-1;bool connected=false;int seed=-1,segment=-1,round=-1;};
Candidate best,current_checkpoint,neighbor_checkpoint;
ofstream improvements;
bool generators(Candidate&c){
 for(int side=0;side<2;++side){int p=4*side;auto&a=c.internal[side];a={c.fields[p]+Q,inverses[c.fields[p]+Q],c.fields[p+1]+3*Q,inverses[c.fields[p+1]+3*Q],c.fields[p+2]+5*Q,c.fields[p+3]+5*Q};if(c.fields[p+2]==c.fields[p+3])return false;}
 for(int j=0;j<6;++j){c.cross[0][j]=c.fields[j+8]+Q*(j<3?1:8);c.cross[1][j]=inverses[c.cross[0][j]];}
 for(int j=0;j<6;++j)for(int k=j+1;k<6;++k)if(c.cross[0][j]==c.cross[0][k])return false;
 return true;
}
void candidate_json(ostream&o,const Candidate&c){o<<"{\"fields\":";array_json(o,c.fields);o<<",\"A\":";array_json(o,c.internal[0]);o<<",\"B\":";array_json(o,c.internal[1]);o<<",\"T\":";array_json(o,c.cross[0]);o<<",\"representative_missing\":";array_json(o,c.missing);o<<",\"score\":"<<c.score<<",\"diameter\":"<<c.diameter<<",\"connected\":"<<(c.connected?"true":"false")<<",\"seed_index\":"<<c.seed<<",\"segment\":"<<c.segment<<",\"round\":"<<c.round<<'}';}
void evaluate(Candidate&c){
 c.score=0;c.diameter=0;c.connected=true;
 for(int side=0;side<2;++side){int dist[N],queue[N],head=0,tail=1;fill(dist,dist+N,-1);dist[side*H]=0;queue[0]=side*H;c.hist[side].fill(0);c.missing[side]=0;
  while(head<tail){int u=queue[head++],s=u>=H,h=u-s*H,nd=dist[u]+1;const int*row=product[h];
   for(int g:c.internal[s]){int v=s*H+row[g];if(dist[v]<0){dist[v]=nd;queue[tail++]=v;}}
   for(int g:c.cross[s]){int v=(1-s)*H+row[g];if(dist[v]<0){dist[v]=nd;queue[tail++]=v;}}
  }
  if(tail!=N)c.connected=false;
  for(int d:dist){if(d<0||d>3)c.missing[side]++;c.hist[side][d<0?N:d]++;c.diameter=max(c.diameter,d);}
  c.score+=c.missing[side];
 }
 if(!c.connected)c.diameter=-1;evaluated++;
 if(c.score<best.score){best=c;improvements<<"{\"evaluation\":"<<evaluated<<",\"CPU_seconds\":"<<elapsed()<<",\"candidate\":";candidate_json(improvements,c);improvements<<"}\n";improvements.flush();cout<<"BEST score="<<c.score<<" misses="<<c.missing[0]<<','<<c.missing[1]<<" seed="<<c.seed<<" segment="<<c.segment<<" CPU="<<elapsed()<<endl;}
 if(c.score==0)found=true;
}
void histogram_json(ostream&o,const Candidate&c){o<<'[';for(int s=0;s<2;++s){if(s)o<<',';o<<'{';bool first=true;for(int d=0;d<=N;++d)if(c.hist[s][d]){if(!first)o<<',';first=false;o<<'"'<<(d==N?-1:d)<<"\":"<<c.hist[s][d];}o<<'}';}o<<']';}
void save_best(){ofstream e(directory+"/profile.best.edges");e<<N<<" 4920\n";int count=0;
 for(int u=0;u<N;++u){int side=u>=H,h=u-side*H;for(int g:best.internal[side]){int v=side*H+product[h][g];if(u<v){e<<u<<' '<<v<<'\n';count++;}}for(int g:best.cross[side]){int v=(1-side)*H+product[h][g];if(u<v){e<<u<<' '<<v<<'\n';count++;}}}assert(count==4920);
 ofstream o(directory+"/profile.best.json");o<<"{\"n\":820,\"m\":4920,\"degree\":12,\"group_order\":410,\"action_root\":25,\"encoding\":\"side*410+x+41*k\",\"candidate\":";candidate_json(o,best);o<<",\"bad_unordered_pairs\":"<<205LL*best.score<<",\"representative_distance_histograms\":";histogram_json(o,best);o<<",\"selection\":\"best evaluated candidate in the fixed seed and perturbation profile; not a full-family minimum\"}\n";
}
void progress(const string&stage){ofstream o(directory+"/profile.progress.json");o<<"{\"stage\":\""<<stage<<"\",\"evaluated_candidates\":"<<evaluated<<",\"full_root_BFS_runs\":"<<2*evaluated<<",\"best_score\":"<<best.score<<",\"CPU_seconds\":"<<elapsed()<<",\"seed\":"<<active_seed<<",\"segment\":"<<active_segment<<",\"round\":"<<active_round<<",\"coordinate\":"<<active_coordinate<<",\"value\":"<<active_value<<"}\n";}
struct DescentResult{Candidate result;int rounds=0;bool minimum=false,capped=false;long long tested=0,illegal=0;};
DescentResult descend(Candidate current){DescentResult out;long long before=neighbor_evaluated,ibefore=illegal_neighbors;
 for(int round=0;round<30&&!found&&!timed_out;++round){active_round=round;Candidate nb=current;current_checkpoint=current;
  for(int coordinate=0;coordinate<14&&!found&&!timed_out;++coordinate)for(int value=0;value<Q;++value){if(value==current.fields[coordinate])continue;active_coordinate=coordinate;active_value=value;neighbor_checkpoint=nb;
   if(exhausted()){timed_out=true;break;}Candidate c=current;c.fields[coordinate]=value;c.round=round;if(!generators(c)){illegal_neighbors++;continue;}evaluate(c);neighbor_evaluated++;if(c.score<nb.score)nb=c;if(found)break;
  }
  if(found){current=best;break;}if(timed_out)break;
  if(nb.score>=current.score){out.minimum=true;break;}current=nb;out.rounds++;if(out.rounds==30)out.capped=true;progress("descent");
 }
 out.result=current;out.tested=neighbor_evaluated-before;out.illegal=illegal_neighbors-ibefore;return out;
}
int main(int argc,char**argv){assert(argc==3);directory=argv[1];cpu_limit=stod(argv[2]);began=clock();powers[0]=1;for(int i=1;i<K;++i)powers[i]=25*powers[i-1]%Q;assert(powers[5]==40);
 for(int a=0;a<H;++a){int j=a/Q;inverses[a]=(Q-powers[(K-j)%K]*(a%Q)%Q)%Q+Q*((K-j)%K);assert(multiply(a,inverses[a])==0);for(int b=0;b<H;++b)product[a][b]=multiply(a,b);}
 improvements.open(directory+"/profile.improvements.jsonl");mt19937_64 rng(2026102624ULL);vector<Candidate>seeds(33);seeds[0].fields={0,36,28,22,0,25,24,13,34,6,16,17,3,8};seeds[0].seed=0;seeds[0].segment=0;assert(generators(seeds[0]));evaluate(seeds[0]);assert((seeds[0].missing==array<int,2>{34,34}));assert(seeds[0].diameter==4);for(int side=0;side<2;++side){assert(seeds[0].hist[side][0]==1&&seeds[0].hist[side][1]==12&&seeds[0].hist[side][2]==132&&seeds[0].hist[side][3]==641&&seeds[0].hist[side][4]==34);}
 {ofstream o(directory+"/calibration.roots.json");o<<"{\"exact_seed_two_root_BFS\":true,\"candidate\":";candidate_json(o,seeds[0]);o<<",\"histograms\":";histogram_json(o,seeds[0]);o<<",\"CPU_seconds\":"<<elapsed()<<"}\n";}
 for(int k=1;k<33;++k){seeds[k].seed=k;seeds[k].segment=0;do{for(int&x:seeds[k].fields)x=rng()%Q;random_draws++;}while(!generators(seeds[k]));}
 {ofstream o(directory+"/profile.seeds.json");o<<'[';for(int k=0;k<33;++k){if(k)o<<',';o<<"{\"seed_index\":"<<k<<",\"fields\":";array_json(o,seeds[k].fields);o<<'}';}o<<"]\n";}
 ofstream segments(directory+"/profile.segments.jsonl"),seed_results(directory+"/profile.seed_results.jsonl");int seeds_completed=0,segments_completed=0,minimum_segments=0,capped_segments=0,perturbations=0;long long accepted_moves=0;
 for(int k=0;k<33&&!found&&!timed_out;++k){active_seed=k;Candidate incumbent=seeds[k];active_segment=0;if(k){if(exhausted()){timed_out=true;break;}evaluate(incumbent);}int initial_score=incumbent.score;int completed_here=0;
  for(int segment=0;segment<=8&&!found&&!timed_out;++segment){active_segment=segment;active_round=-1;active_coordinate=-1;active_value=-1;Candidate start=incumbent;
   if(segment){do{if(exhausted()){timed_out=true;break;}start=incumbent;int a=rng()%14,b=rng()%13;if(b>=a)b++;start.fields[a]=(start.fields[a]+1+rng()%40)%Q;start.fields[b]=(start.fields[b]+1+rng()%40)%Q;perturb_draws++;}while(!generators(start));if(timed_out)break;start.seed=k;start.segment=segment;start.round=-1;evaluate(start);perturbations++;}
   start.seed=k;start.segment=segment;DescentResult d;if(found)d.result=start;else d=descend(start);if(d.result.score<incumbent.score)incumbent=d.result;accepted_moves+=d.rounds;
   string stop=found?"FOUND_D3":timed_out?"CPU_LIMIT":d.minimum?"COORDINATE_MINIMUM":"THIRTY_MOVE_CAP";
   segments<<"{\"seed_index\":"<<k<<",\"segment\":"<<segment<<",\"initial_score\":"<<start.score<<",\"end_score\":"<<d.result.score<<",\"incumbent_score\":"<<incumbent.score<<",\"accepted_strict_moves\":"<<d.rounds<<",\"legal_neighbor_candidates\":"<<d.tested<<",\"illegal_neighbors\":"<<d.illegal<<",\"stop\":\""<<stop<<"\",\"start_fields\":";array_json(segments,start.fields);segments<<",\"end_fields\":";array_json(segments,d.result.fields);segments<<"}\n";segments.flush();if(!timed_out&&!found){completed_here++;segments_completed++;minimum_segments+=d.minimum;capped_segments+=d.capped;}progress("segment_complete");
  }
  if(completed_here==9)seeds_completed++;seed_results<<"{\"seed_index\":"<<k<<",\"initial_score\":"<<initial_score<<",\"segments_completed\":"<<completed_here<<",\"best_candidate\":";candidate_json(seed_results,incumbent);seed_results<<"}\n";seed_results.flush();cout<<"SEED "<<k<<" initial="<<initial_score<<" incumbent="<<incumbent.score<<" global="<<best.score<<" segments="<<completed_here<<" CPU="<<elapsed()<<endl;
 }
 save_best();string status=found?"FOUND_D3":timed_out?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_FIXED_PROFILE_NO_SOLUTION";
 if(timed_out){ofstream o(directory+"/profile.checkpoint.json");o<<"{\"current\":";candidate_json(o,current_checkpoint);o<<",\"best_neighbor_seen\":";candidate_json(o,neighbor_checkpoint);o<<",\"rng_state\":\""<<rng<<"\"}\n";}
 ofstream o(directory+"/profile.terminal.json");o<<"{\"status\":\""<<status<<"\",\"running\":false,\"seed\":2026102624,\"seed_scope\":33,\"seeds_completed\":"<<seeds_completed<<",\"segment_scope\":297,\"segments_completed\":"<<segments_completed<<",\"coordinate_minimum_segments\":"<<minimum_segments<<",\"thirty_move_cap_segments\":"<<capped_segments<<",\"random_seed_draws\":"<<random_draws<<",\"perturbation_draws\":"<<perturb_draws<<",\"legal_double_coordinate_perturbations\":"<<perturbations<<",\"accepted_strict_moves\":"<<accepted_moves<<",\"evaluated_candidates\":"<<evaluated<<",\"full_root_BFS_runs\":"<<2*evaluated<<",\"legal_neighbors_evaluated\":"<<neighbor_evaluated<<",\"illegal_neighbors_skipped\":"<<illegal_neighbors<<",\"best_score\":"<<best.score<<",\"CPU_seconds\":"<<elapsed()<<",\"cursor\":{\"seed\":"<<active_seed<<",\"segment\":"<<active_segment<<",\"round\":"<<active_round<<",\"coordinate\":"<<active_coordinate<<",\"value\":"<<active_value<<"},\"finite_profile_not_full_family\":true,\"pending\":[\"unique independent final graph verification by parent\"]}\n";o.close();progress(status);cout<<status<<" evaluated="<<evaluated<<" best="<<best.score<<" CPU="<<elapsed()<<endl;
}

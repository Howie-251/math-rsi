#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=820,Q=41,K=20,D=12;
int powers[K],product[N][N],inverse_element[N],pair_index[N];
vector<array<int,2>>pair_pool;vector<int>pair_phase;
bool allowed[2000000]{};clock_t began;double cpu_limit;string directory;
bool found=false,timed_out=false;long long evaluations=0;int seed_cursor=-1,round_cursor=-1,type_cursor=-1,a_cursor=-1,b_cursor=-1,c_cursor=-1;
double elapsed(){return double(clock()-began)/CLOCKS_PER_SEC;}
int multiply(int a,int b){return (a%Q+powers[a/Q]*(b%Q))%Q+Q*((a/Q+b/Q)%K);}
template<class T>void array_json(ostream&o,const T&a){o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';}
struct Candidate{vector<int>pairs,refs;array<int,D>S{};int missing=N+1,diameter=-1;bool connected=false;int seed=-1,round=-1,move=-1;};
struct Stats{array<long long,4>legal{},pruned{},scored{};};
Candidate global_best,checkpoint_current,checkpoint_neighbor;array<int,N+1>best_hist{};Stats totals;
ofstream improvements;
int phase_key(const Candidate&c){array<int,6>p{};int size=c.pairs.size();for(int k=0;k<size;++k)p[k]=pair_phase[c.pairs[k]];sort(p.begin(),p.begin()+size);int key=1;for(int k=0;k<size;++k)key=10*key+p[k];return key;}
void make_S(Candidate&c){int k=0;for(int id:c.pairs){c.S[k++]=pair_pool[id][0];c.S[k++]=pair_pool[id][1];}for(int x:c.refs)c.S[k++]=410+x;assert(k==12);}
void candidate_json(ostream&o,const Candidate&c){o<<"{\"inverse_pair_pool_ids\":";array_json(o,c.pairs);o<<",\"reflection_fields\":";array_json(o,c.refs);o<<",\"S\":";array_json(o,c.S);o<<",\"pair_phases\":[";bool first=true;for(int id:c.pairs){if(!first)o<<',';first=false;o<<pair_phase[id];}o<<"],\"pairs\":"<<c.pairs.size()<<",\"involutions\":"<<c.refs.size()<<",\"root_missing\":"<<c.missing<<",\"diameter\":"<<c.diameter<<",\"connected\":"<<(c.connected?"true":"false")<<",\"seed_index\":"<<c.seed<<",\"accepted_at_round\":"<<c.round<<",\"move_type\":"<<c.move<<'}';}
void evaluate(Candidate&c){make_S(c);int dist[N],queue[N],head=0,tail=1;fill(dist,dist+N,-1);dist[0]=0;queue[0]=0;
 while(head<tail){int u=queue[head++],d=dist[u]+1;const int*row=product[u];for(int s:c.S){int v=row[s];if(dist[v]<0){dist[v]=d;queue[tail++]=v;}}}
 c.missing=0;c.diameter=0;c.connected=tail==N;for(int d:dist){c.missing+=(d<0||d>3);c.diameter=max(c.diameter,d);}if(!c.connected)c.diameter=-1;evaluations++;
 if(c.missing<global_best.missing){global_best=c;best_hist.fill(0);for(int d:dist)best_hist[d<0?N:d]++;improvements<<"{\"evaluation\":"<<evaluations<<",\"CPU_seconds\":"<<elapsed()<<",\"candidate\":";candidate_json(improvements,c);improvements<<"}\n";improvements.flush();cout<<"BEST missing="<<c.missing<<" seed="<<c.seed<<" round="<<c.round<<" type="<<c.move<<" CPU="<<elapsed()<<endl;}
 if(c.missing==0)found=true;
}
void stats_json(ostream&o,const Stats&s){o<<"{\"legal_neighbors\":";array_json(o,s.legal);o<<",\"capacity_pruned\":";array_json(o,s.pruned);o<<",\"actual_BFS_candidates\":";array_json(o,s.scored);o<<'}';}
bool offer(Candidate c,int type,Candidate&neighbor,Stats&round){
 if(elapsed()>=cpu_limit){timed_out=true;return false;}
 round.legal[type]++;totals.legal[type]++;
 if(!allowed[phase_key(c)]){round.pruned[type]++;totals.pruned[type]++;return true;}
 c.move=type;c.round=round_cursor;evaluate(c);round.scored[type]++;totals.scored[type]++;if(c.missing<neighbor.missing)neighbor=c;
 return !found;
}
bool scan(const Candidate&current,Candidate&neighbor,Stats&round){
 bool used_pair[389]{},used_ref[41]{};for(int id:current.pairs)used_pair[id]=true;for(int x:current.refs)used_ref[x]=true;
 int p=current.pairs.size(),i=current.refs.size();checkpoint_current=current;
 type_cursor=0;
 for(int a=0;a<p;++a)for(int id=0;id<389;++id)if(!used_pair[id]){a_cursor=a;b_cursor=id;c_cursor=-1;Candidate c=current;c.pairs[a]=id;sort(c.pairs.begin(),c.pairs.end());if(!offer(c,0,neighbor,round)){checkpoint_neighbor=neighbor;return false;}}
 type_cursor=1;
 for(int a=0;a<i;++a)for(int x=0;x<41;++x)if(!used_ref[x]){a_cursor=a;b_cursor=x;c_cursor=-1;Candidate c=current;c.refs[a]=x;sort(c.refs.begin(),c.refs.end());if(!offer(c,1,neighbor,round)){checkpoint_neighbor=neighbor;return false;}}
 type_cursor=2;
 for(int a=0;a<p;++a)for(int x=0;x<41;++x)if(!used_ref[x])for(int y=x+1;y<41;++y)if(!used_ref[y]){a_cursor=a;b_cursor=x;c_cursor=y;Candidate c=current;c.pairs.erase(c.pairs.begin()+a);c.refs.push_back(x);c.refs.push_back(y);sort(c.refs.begin(),c.refs.end());if(!offer(c,2,neighbor,round)){checkpoint_neighbor=neighbor;return false;}}
 type_cursor=3;
 for(int a=0;a<i;++a)for(int b=a+1;b<i;++b)for(int id=0;id<389;++id)if(!used_pair[id]){a_cursor=a;b_cursor=b;c_cursor=id;Candidate c=current;c.refs.erase(c.refs.begin()+b);c.refs.erase(c.refs.begin()+a);c.pairs.push_back(id);sort(c.pairs.begin(),c.pairs.end());if(!offer(c,3,neighbor,round)){checkpoint_neighbor=neighbor;return false;}}
 array<long long,4>expected={1LL*p*(389-p),1LL*i*(41-i),1LL*p*(41-i)*(40-i)/2,1LL*i*(i-1)/2*(389-p)};assert(round.legal==expected);return true;
}
void progress(const string&stage){ofstream o(directory+"/progress.json");o<<"{\"stage\":\""<<stage<<"\",\"CPU_seconds\":"<<elapsed()<<",\"evaluations\":"<<evaluations<<",\"best_root_missing\":"<<global_best.missing<<",\"cursor\":{\"seed\":"<<seed_cursor<<",\"round\":"<<round_cursor<<",\"type\":"<<type_cursor<<",\"a\":"<<a_cursor<<",\"b\":"<<b_cursor<<",\"c\":"<<c_cursor<<"}}\n";}
void save_best(){ofstream e(directory+"/production.best.edges");e<<N<<" 4920\n";int count=0;for(int u=0;u<N;++u)for(int s:global_best.S){int v=product[u][s];if(u<v){e<<u<<' '<<v<<'\n';count++;}}assert(count==4920);
 ofstream o(directory+"/production.best.json");o<<"{\"n\":820,\"m\":4920,\"degree\":12,\"action_root\":36,\"encoding\":\"x+41*j\",\"candidate\":";candidate_json(o,global_best);o<<",\"bad_unordered_pairs\":"<<410LL*global_best.missing<<",\"root_distance_histogram\":{";bool first=true;for(int d=0;d<=N;++d)if(best_hist[d]){if(!first)o<<',';first=false;o<<'"'<<(d==N?-1:d)<<"\":"<<best_hist[d];}o<<"},\"scope\":\"best actually scored candidate in 17 fixed trajectories with necessary phase pruning; not a full-family minimum\"}\n";
}
int main(int argc,char**argv){assert(argc==3);directory=argv[1];cpu_limit=stod(argv[2]);began=clock();powers[0]=1;for(int j=1;j<K;++j)powers[j]=36*powers[j-1]%Q;assert(powers[10]==40);fill(pair_index,pair_index+N,-1);
 for(int a=0;a<N;++a){int j=a/Q;inverse_element[a]=(Q-powers[(K-j)%K]*(a%Q)%Q)%Q+Q*((K-j)%K);assert(multiply(a,inverse_element[a])==0);for(int b=0;b<N;++b)product[a][b]=multiply(a,b);}
 int involutions=0;for(int a=1;a<N;++a){int b=inverse_element[a];if(a==b){assert(a/Q==10);involutions++;}if(a<b){pair_index[a]=pair_index[b]=pair_pool.size();pair_pool.push_back({a,b});pair_phase.push_back(min(a/Q,(K-a/Q)%K));}}assert(pair_pool.size()==389&&involutions==41);
 ifstream phases(directory+"/allowed_phases.txt");int phase_count;phases>>phase_count;assert(phase_count==2139);for(int row=0;row<phase_count;++row){int p,key=1;phases>>p;for(int j=0;j<p;++j){int a;phases>>a;key=10*key+a;}assert(!allowed[key]);allowed[key]=true;}
 ifstream input(directory+"/seeds.txt");int count;input>>count;assert(count==17);vector<Candidate>seeds(count);vector<int>expected(count);
 for(int k=0;k<count;++k){auto&c=seeds[k];c.seed=k;input>>expected[k];array<int,12>S;for(int&g:S)input>>g;auto sorted=S;sort(sorted.begin(),sorted.end());assert(sorted[0]>0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end());for(int g:S){int inv=inverse_element[g];assert(find(S.begin(),S.end(),inv)!=S.end());if(g==inv)c.refs.push_back(g%Q);else if(g<inv)c.pairs.push_back(pair_index[g]);}sort(c.pairs.begin(),c.pairs.end());sort(c.refs.begin(),c.refs.end());assert(allowed[phase_key(c)]);}
 improvements.open(directory+"/improvements.jsonl");ofstream rounds(directory+"/rounds.jsonl"),results(directory+"/seed_results.jsonl");int seeds_started=0,seeds_completed=0,minima=0,capped=0,accepted=0,complete_rounds=0;
 for(int k=0;k<count&&!found&&!timed_out;++k){seed_cursor=k;round_cursor=-1;type_cursor=-1;Candidate current=seeds[k];if(elapsed()>=cpu_limit){timed_out=true;break;}evaluate(current);seeds_started++;assert(current.missing==expected[k]);int moves=0;bool minimum=false,cap=false;
  for(int r=0;r<30&&!found&&!timed_out;++r){round_cursor=r;Candidate neighbor=current;Stats stats;double round_start=elapsed();bool complete=scan(current,neighbor,stats);
   rounds<<"{\"seed_index\":"<<k<<",\"round\":"<<r<<",\"initial_missing\":"<<current.missing<<",\"best_seen_missing\":"<<neighbor.missing<<",\"complete_neighborhood\":"<<(complete?"true":"false")<<",\"counts\":";stats_json(rounds,stats);rounds<<",\"CPU_seconds\":"<<elapsed()-round_start;
   if(found){current=global_best;rounds<<",\"stop\":\"FOUND_D3\"}\n";rounds.flush();break;}if(timed_out){rounds<<",\"stop\":\"CPU_LIMIT\"}\n";rounds.flush();break;}
   complete_rounds++;if(neighbor.missing>=current.missing){minimum=true;rounds<<",\"stop\":\"CAPACITY_SURVIVOR_NEIGHBORHOOD_MINIMUM\"}\n";rounds.flush();break;}
   current=neighbor;moves++;accepted++;rounds<<",\"stop\":\"STRICT_IMPROVEMENT\",\"accepted\":";candidate_json(rounds,current);rounds<<"}\n";rounds.flush();if(moves==30)cap=true;progress("descent");
  }
  if(!found&&!timed_out){seeds_completed++;minima+=minimum;capped+=cap;}
  results<<"{\"seed_index\":"<<k<<",\"initial_missing\":"<<expected[k]<<",\"accepted_moves\":"<<moves<<",\"capacity_survivor_neighborhood_minimum\":"<<(minimum?"true":"false")<<",\"thirty_move_cap\":"<<(cap?"true":"false")<<",\"current\":";candidate_json(results,current);results<<"}\n";results.flush();progress("seed_end");cout<<"SEED "<<k<<" initial="<<expected[k]<<" final="<<current.missing<<" accepted="<<moves<<" global="<<global_best.missing<<" CPU="<<elapsed()<<endl;
 }
 save_best();string status=found?"FOUND_D3":timed_out?"CPU_LIMIT_PREFIX_SAVED":"COMPLETE_FIXED_TRAJECTORIES_NO_SOLUTION";
 if(timed_out){ofstream cp(directory+"/checkpoint.json");cp<<"{\"current\":";candidate_json(cp,checkpoint_current);cp<<",\"best_neighbor_seen\":";candidate_json(cp,checkpoint_neighbor);cp<<"}\n";}
 ofstream o(directory+"/terminal.json");o<<"{\"status\":\""<<status<<"\",\"running\":false,\"seed_scope\":17,\"seeds_started\":"<<seeds_started<<",\"seeds_completed\":"<<seeds_completed<<",\"capacity_survivor_neighborhood_minima\":"<<minima<<",\"thirty_move_caps\":"<<capped<<",\"complete_neighborhood_scans\":"<<complete_rounds<<",\"accepted_strict_moves\":"<<accepted<<",\"actual_full_root_BFS\":"<<evaluations<<",\"move_type_order\":[\"replace_pair\",\"replace_reflection\",\"pair_to_two_reflections\",\"two_reflections_to_pair\"],\"neighbor_counts\":";stats_json(o,totals);o<<",\"best_root_missing\":"<<global_best.missing<<",\"CPU_seconds\":"<<elapsed()<<",\"cursor\":{\"seed\":"<<seed_cursor<<",\"round\":"<<round_cursor<<",\"type\":"<<type_cursor<<",\"a\":"<<a_cursor<<",\"b\":"<<b_cursor<<",\"c\":"<<c_cursor<<"},\"finite_trajectories_not_full_family\":true,\"pending\":[\"final saved graph verification decision by parent\"]}\n";o.close();progress(status);cout<<status<<" actual_BFS="<<evaluations<<" best="<<global_best.missing<<" CPU="<<elapsed()<<endl;
}

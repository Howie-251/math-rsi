#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
constexpr int N=122,D=6,M=N*D/2,STARTS=8,STEPS=250000;
using Bits=array<uint64_t,2>;using Edge=array<int,2>;
array<array<int,D>,N> adj;array<Bits,N> near1,near2;
vector<Edge> edges;string out;clock_t began;uint64_t proposals=0,legal=0,accepted=0,scores=0;
int best=1000000,beststart=-1,beststep=-1;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
bool linked(int a,int b){return (near1[a][b/64]>>(b%64))&1;}
void replace_neighbor(int a,int old,int now){auto it=find(adj[a].begin(),adj[a].end(),old);assert(it!=adj[a].end());*it=now;near1[a][old/64]&=~(1ULL<<(old%64));near1[a][now/64]|=1ULL<<(now%64);}
void change(const Edge&a,const Edge&b){replace_neighbor(a[0],a[1],b[0]);replace_neighbor(a[1],a[0],b[1]);replace_neighbor(b[0],b[1],a[0]);replace_neighbor(b[1],b[0],a[1]);}
int score(array<int,N>*misses=nullptr){
 for(int v=0;v<N;v++){near2[v]=near1[v];near2[v][v/64]|=1ULL<<(v%64);for(int u:adj[v])for(int k=0;k<2;k++)near2[v][k]|=near1[u][k];}
 int ordered=0;for(int v=0;v<N;v++){Bits ball=near2[v];for(int u:adj[v])for(int k=0;k<2;k++)ball[k]|=near2[u][k];int miss=N-__builtin_popcountll(ball[0])-__builtin_popcountll(ball[1]);if(misses)(*misses)[v]=miss;ordered+=miss;}assert(ordered%2==0);return ordered/2;
}
bool move(mt19937_64&rng,int &i,int &j,Edge&a,Edge&b){i=rng()%M;j=rng()%M;if(i==j)return false;a=edges[i];b=edges[j];if(rng()&1)swap(b[0],b[1]);return a[0]!=b[0]&&a[0]!=b[1]&&a[1]!=b[0]&&a[1]!=b[1]&&!linked(a[0],b[0])&&!linked(a[1],b[1]);}
void commit(int i,int j,const Edge&a,const Edge&b){edges[i]={a[0],b[0]};edges[j]={a[1],b[1]};for(int k:{i,j})if(edges[k][0]>edges[k][1])swap(edges[k][0],edges[k][1]);}
void save(int s,int start,int step){best=s;beststart=start;beststep=step;ofstream f(out+"/best.edges");f<<N<<' '<<M<<'\n';int count=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){f<<u<<' '<<v<<'\n';count++;}assert(count==M);ofstream j(out+"/best.json");j<<"{\"n\":122,\"m\":366,\"degree\":6,\"target_diameter\":3,\"bad_unordered_pairs_gt3_or_unreachable\":"<<s<<",\"start\":"<<start<<",\"step\":"<<step<<",\"scores_at_save\":"<<scores<<",\"symmetry_assumed\":false,\"all_roots_used\":122}\n";}
void fresh(mt19937_64&rng){
 edges.clear();for(auto &x:near1)x.fill(0);array<int,N>deg{};
 for(int u=0;u<N;u++)for(int k=1;k<=3;k++){int v=(u+k)%N;Edge e{min(u,v),max(u,v)};edges.push_back(e);adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;near1[u][v/64]|=1ULL<<(v%64);near1[v][u/64]|=1ULL<<(u%64);}
 assert(edges.size()==M);for(int d:deg)assert(d==D);
 int done=0;while(done<10000){int i,j;Edge a,b;if(!move(rng,i,j,a,b))continue;change(a,b);commit(i,j,a,b);done++;}
}
int main(int argc,char**argv){assert(argc==3);out=argv[1];double budget=stod(argv[2]);began=clock();ofstream rows(out+"/starts.jsonl");int completed=0;bool limited=false,hit=false;int cursorstart=0,cursorstep=0;
 for(int start=0;start<STARTS;start++){
  cursorstart=start;mt19937_64 rng(20261027180ULL+start);fresh(rng);array<int,N>initialmiss;int current=score(&initialmiss);scores++;
  if(start==0){ofstream f(out+"/first.edges");f<<N<<' '<<M<<'\n';for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)f<<u<<' '<<v<<'\n';ofstream j(out+"/first.expected.json");j<<"{\"bad_pairs\":"<<current<<",\"radius3_deficits\":[";for(int i=0;i<N;i++){if(i)j<<',';j<<initialmiss[i];}j<<"]}\n";f.close();j.close();
   // The parent driver performs the one independent ordinary-BFS calibration
   // of this first formal candidate before releasing the production run.
   cout<<"FIRST_READY score="<<current<<endl;
   ifstream ack;while(true){ack.open(out+"/first.calibrated");if(ack.good())break;ack.close();if(cpu()>budget){limited=true;goto finish;}}
  }
  if(current<best)save(current,start,-1);int startbest=current;uint64_t acceptedhere=0;int step;
  for(step=0;step<STEPS;step++){
   cursorstep=step;if((step&1023)==0&&cpu()>=budget){limited=true;goto finish;}
   proposals++;int i,j;Edge a,b;if(!move(rng,i,j,a,b))continue;legal++;change(a,b);int trial=score();scores++;
   if(trial<best){save(trial,start,step);if(trial==0){hit=true;goto finish;}}
   startbest=min(startbest,trial);double frac=double(step%50000)/49999.;double temperature=8.0*pow(0.0125,frac);
   bool take=trial<=current||generate_canonical<double,53>(rng)<exp(double(current-trial)/temperature);
   if(take){commit(i,j,a,b);current=trial;accepted++;acceptedhere++;}else {Edge c{a[0],b[0]},d{a[1],b[1]};change(c,d);}
  }
  completed++;rows<<"{\"start\":"<<start<<",\"seed\":"<<(20261027180ULL+start)<<",\"proposals\":"<<STEPS<<",\"best_bad_pairs\":"<<startbest<<",\"final_bad_pairs\":"<<current<<",\"accepted_moves\":"<<acceptedhere<<",\"CPU_seconds_cumulative\":"<<cpu()<<"}\n";rows.flush();cout<<"START_DONE "<<start<<" best="<<startbest<<" global="<<best<<" CPU="<<cpu()<<endl;
 }
 finish:
 string status=hit?"FOUND_D3":limited?"CPU_LIMIT_PREFIX_NO_D3":"COMPLETE_8_START_ANNEAL_PROFILE_NO_D3";
 ofstream t(out+"/terminal.json");t<<"{\"status\":\""<<status<<"\",\"running\":false,\"starts_completed\":"<<completed<<",\"starts_planned\":8,\"proposals\":"<<proposals<<",\"legal_switch_candidates\":"<<legal<<",\"exact_all_root_scores\":"<<scores<<",\"accepted_moves\":"<<accepted<<",\"best_bad_pairs\":"<<best<<",\"best_start\":"<<beststart<<",\"best_step\":"<<beststep<<",\"cursor\":{\"start\":"<<cursorstart<<",\"step\":"<<cursorstep<<"},\"production_CPU_seconds\":"<<cpu()<<",\"unrestricted_family_exhausted\":false,\"restarts\":0,\"pending\":[]}\n";
 cout<<status<<" best="<<best<<" CPU="<<cpu()<<endl;
}

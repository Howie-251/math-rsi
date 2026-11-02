#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <thread>
#include <vector>
using namespace std;
constexpr int P=107,N=108,SAMPLES=30000;
using Bits=array<uint64_t,2>;using Matrix=array<int,4>;
array<vector<int>,N>adj;array<Bits,N>near1,near2;array<int,P>inv;
string out;clock_t began;int best=N*N,bestindex=-1,improvements=0;uint64_t matrixdraws=0,singular=0;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
int mod(int x){x%=P;return x<0?x+P:x;}
Matrix random_matrix(mt19937_64&rng){while(true){matrixdraws++;Matrix m;for(int&i:m)i=rng()%P;if(mod(m[0]*m[3]-m[1]*m[2])){int first=0;while(m[first]==0)first++;int scale=inv[m[first]];for(int&i:m)i=i*scale%P;return m;}singular++;}}
int act(const Matrix&m,int x){if(x==P)return m[2]?m[0]*inv[m[2]]%P:P;int den=(m[2]*x+m[3])%P;return den?((m[0]*x+m[1])%P)*inv[den]%P:P;}
void build(const Matrix&a,const Matrix&b){for(auto&x:adj)x.clear();for(auto&x:near1)x.fill(0);for(const Matrix*m:{&a,&b})for(int x=0;x<N;x++){int y=act(*m,x);if(x==y||(near1[x][y/64]>>(y%64)&1))continue;near1[x][y/64]|=1ULL<<(y%64);near1[y][x/64]|=1ULL<<(x%64);adj[x].push_back(y);adj[y].push_back(x);}for(auto&v:adj)assert(v.size()<=4);}
int score(array<int,N>*deficits=nullptr){for(int v=0;v<N;v++){near2[v]=near1[v];near2[v][v/64]|=1ULL<<(v%64);for(int u:adj[v])for(int k=0;k<2;k++)near2[v][k]|=near1[u][k];}int ordered=0;for(int v=0;v<N;v++){Bits ball{};for(int k=0;k<2;k++){uint64_t bits=near2[v][k];while(bits){int u=64*k+__builtin_ctzll(bits);bits&=bits-1;ball[0]|=near2[u][0];ball[1]|=near2[u][1];}}int miss=N-__builtin_popcountll(ball[0])-__builtin_popcountll(ball[1]);ordered+=miss;if(deficits)(*deficits)[v]=miss;}assert(ordered%2==0);return ordered/2;}
int component0(){array<bool,N>seen{};array<int,N>q;int head=0,tail=1;seen[0]=true;q[0]=0;while(head<tail){int u=q[head++];for(int v:adj[u])if(!seen[v]){seen[v]=true;q[tail++]=v;}}return tail;}
void matrix_json(ostream&f,const Matrix&m){f<<'[';for(int i=0;i<4;i++){if(i)f<<',';f<<m[i];}f<<']';}
void edges_write(const string&file){int twice=0;for(auto&a:adj)twice+=a.size();assert(twice%2==0);ofstream f(file);f<<N<<' '<<twice/2<<'\n';for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)f<<u<<' '<<v<<'\n';}
void save(int s,int index,const Matrix&a,const Matrix&b,int comp){best=s;bestindex=index;array<int,5>hist{};for(auto&x:adj)hist[x.size()]++;int twice=0;for(auto&x:adj)twice+=x.size();edges_write(out+"/best.edges");string stem=out+"/improvements/"+to_string(index);edges_write(stem+".edges");
 auto emit=[&](const string&file){ofstream j(file);j<<"{\"n\":108,\"p\":107,\"infinity_label\":107,\"target_max_degree\":4,\"target_diameter\":4,\"matrix_A\":";matrix_json(j,a);j<<",\"matrix_B\":";matrix_json(j,b);j<<",\"degree_histogram_0_to4\":[";for(int i=0;i<5;i++){if(i)j<<',';j<<hist[i];}j<<"],\"m\":"<<twice/2<<",\"connected\":"<<(comp==N?"true":"false")<<",\"component0_size\":"<<comp<<",\"bad_unordered_pairs_gt4_or_unreachable\":"<<s<<",\"sample_index\":"<<index<<",\"symmetry_assumed\":false}\n";};emit(out+"/best.json");emit(stem+".json");improvements++;}
int main(int argc,char**argv){assert(argc==3);out=argv[1];double budget=stod(argv[2]);began=clock();for(int x=1;x<P;x++)for(int y=1;y<P;y++)if(x*y%P==1){inv[x]=y;break;}mt19937_64 rng(20261027190ULL);ofstream samples(out+"/samples.jsonl");int completed=0,connected=0,hit=0;bool limited=false;array<uint64_t,5>aggregate_degree{};
 for(int index=0;index<SAMPLES;index++){
  if((index&255)==0&&cpu()>=budget){limited=true;break;}Matrix a=random_matrix(rng),b=random_matrix(rng);build(a,b);array<int,N>deficits;int s=score(index==0?&deficits:nullptr);int comp=component0();connected+=comp==N;array<int,5>hist{};for(auto&x:adj)hist[x.size()]++;for(int k=0;k<5;k++)aggregate_degree[k]+=hist[k];
  if(index==0){edges_write(out+"/first.edges");ofstream j(out+"/first.expected.json");j<<"{\"matrix_A\":";matrix_json(j,a);j<<",\"matrix_B\":";matrix_json(j,b);j<<",\"bad_pairs\":"<<s<<",\"component0_size\":"<<comp<<",\"radius4_deficits\":[";for(int i=0;i<N;i++){if(i)j<<',';j<<deficits[i];}j<<"]}\n";j.close();cout<<"FIRST_READY bad="<<s<<endl;while(true){ifstream ack(out+"/first.calibrated");if(ack.good())break;this_thread::sleep_for(chrono::milliseconds(5));}}
  if(s<best){save(s,index,a,b,comp);cout<<"BEST sample="<<index<<" bad="<<s<<" CPU="<<cpu()<<endl;}
  samples<<"{\"sample_index\":"<<index<<",\"matrix_A\":";matrix_json(samples,a);samples<<",\"matrix_B\":";matrix_json(samples,b);samples<<",\"component0_size\":"<<comp<<",\"bad_pairs\":"<<s<<",\"degree_histogram_0_to4\":[";for(int i=0;i<5;i++){if(i)samples<<',';samples<<hist[i];}samples<<"]}\n";completed++;if(s==0){hit=1;break;}
 }
 string status=hit?"FOUND_D4":limited?"CPU_LIMIT_PREFIX_NO_D4":"COMPLETE_30000_MATRIX_PAIRS_NO_D4";ofstream t(out+"/terminal.json");t<<"{\"status\":\""<<status<<"\",\"running\":false,\"samples_planned\":30000,\"samples_scored\":"<<completed<<",\"connected_samples\":"<<connected<<",\"disconnected_samples\":"<<(completed-connected)<<",\"all_roots_per_score\":108,\"best_bad_pairs\":"<<best<<",\"best_sample_index\":"<<bestindex<<",\"strict_best_improvements\":"<<improvements<<",\"invertible_matrix_draws_used\":"<<2*completed<<",\"matrix_draws_including_singular\":"<<matrixdraws<<",\"singular_matrix_draws_rejected\":"<<singular<<",\"aggregate_degree_histogram_0_to4\":[";for(int i=0;i<5;i++){if(i)t<<',';t<<aggregate_degree[i];}t<<"],\"production_CPU_seconds\":"<<cpu()<<",\"family_exhausted\":false,\"restarts\":0,\"pending\":[]}\n";cout<<status<<" bad="<<best<<" CPU="<<cpu()<<endl;
}

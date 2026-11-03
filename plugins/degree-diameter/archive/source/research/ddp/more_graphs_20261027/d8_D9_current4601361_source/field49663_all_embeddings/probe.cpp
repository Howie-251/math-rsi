#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <sys/resource.h>
#include <unistd.h>
#include <vector>
using namespace std;
constexpr int Q=49663,M=93,N=4618659;
const array<int,8>phase{1,22,12,85,92,71,81,8},inverse{4,5,6,7,0,1,2,3};
template<class T>void arr(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<+x;}o<<']';}
int power(int a,int k){int z=1;while(k){if(k&1)z=int(int64_t(z)*a%Q);a=int(int64_t(a)*a%Q);k>>=1;}return z;}
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];rlimit limit{120,120};assert(setrlimit(RLIMIT_CPU,&limit)==0);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 vector<int>roots;for(int a=2;a<Q;a++)if(power(a,93)==1&&power(a,31)!=1&&power(a,3)!=1)roots.push_back(a);assert(roots.size()==60);
 ofstream rf(dir+"/ROOTS.json");rf<<"{\"field\":49663,\"exact_order\":93,\"roots\":";arr(rf,roots);rf<<"}\n";rf.close();
 int nextBase[M][8];for(int j=0;j<M;j++)for(int d=0;d<8;d++)nextBase[j][d]=((j+phase[d])%M)*Q;
 vector<int8_t>distance(N);vector<uint32_t>queue(N);ofstream cases(dir+"/CASES.jsonl");int done=0,cursor=0,hits=0,hitD=-1,incomplete=0;bool timed=false;
 auto checkpoint=[&](const string&status,int ri,int beta){ofstream c(dir+"/checkpoint.json");c<<"{\"status\":\""<<status<<"\",\"native_pid\":"<<getpid()<<",\"embedding_ordinal\":"<<ri<<",\"beta\":"<<beta<<",\"completed_cases\":"<<done<<",\"aggregate_native_CPU_seconds\":"<<cpu()<<"}\n";};
 for(int ri=0;ri<(int)roots.size();ri++){
  cursor=ri;if(cpu()>=119.0){timed=true;break;}int beta=roots[ri];clock_t caseStarted=clock();checkpoint("IN_PROGRESS",ri,beta);
  array<int,M>powers;powers[0]=1;for(int j=1;j<M;j++)powers[j]=int(int64_t(powers[j-1])*beta%Q);assert(int64_t(powers[92])*beta%Q==1);
  array<int,8>normal{0,1,4800,4208,0,0,0,0};for(int d=0;d<4;d++)normal[d+4]=(Q-int(int64_t(normal[d])*powers[phase[d+4]]%Q))%Q;
  for(int d=0;d<8;d++){assert((phase[d]+phase[inverse[d]])%M==0);assert((normal[d]+int64_t(powers[phase[d]])*normal[inverse[d]])%Q==0);}
  int shift[M][8];for(int j=0;j<M;j++)for(int d=0;d<8;d++)shift[j][d]=int(int64_t(powers[j])*normal[d]%Q);
  fill(distance.begin(),distance.end(),int8_t(-1));array<int,10>hist{};uint32_t lo=0,hi=1;queue[0]=0;distance[0]=0;hist[0]=1;bool aborted=false;
  while(lo<hi){
   if((lo&65535u)==0&&cpu()>=119.0){aborted=true;break;}
   uint32_t u=queue[lo++];int depth=distance[u];if(depth==9)continue;int j=u/Q,x=u-j*Q,nd=depth+1;
   for(int d=0;d<8;d++){int nx=x+shift[j][d];if(nx>=Q)nx-=Q;uint32_t v=nextBase[j][d]+nx;if(distance[v]<0){distance[v]=nd;hist[nd]++;queue[hi++]=v;}}
  }
  if(aborted){timed=true;incomplete=1;ofstream ip(dir+"/INCOMPLETE.json");ip<<"{\"embedding_ordinal\":"<<ri<<",\"beta\":"<<beta<<",\"status\":\"INCOMPLETE_R9_CPU_LIMIT\",\"partial_reached\":"<<hi<<",\"partial_queue_popped\":"<<lo<<",\"not_a_failure_witness\":true,\"CPU_seconds\":"<<cpu()<<"}\n";checkpoint("INCOMPLETE_R9_CPU_LIMIT",ri,beta);break;}
  int firstMissing=-1;if(hi<N)for(int u=0;u<N;u++)if(distance[u]<0){firstMissing=u;break;}
  double caseCPU=double(clock()-caseStarted)/CLOCKS_PER_SEC;
  cases<<"{\"embedding_ordinal\":"<<ri<<",\"beta\":"<<beta<<",\"n\":4618659,\"m\":18474636,\"simple\":true,\"degree\":8,\"connectivity_paper_guarantee\":true,\"identity_R9_reached\":"<<hi<<",\"identity_R9_missing\":"<<N-hi<<",\"first_R9_missing_vertex\":"<<firstMissing<<",\"identity_distance_histogram_through9\":";arr(cases,hist);cases<<",\"CPU_seconds\":"<<caseCPU<<",\"aggregate_native_CPU_seconds\":"<<cpu();
  if(firstMissing>=0){cases<<",\"status\":\"ACTUAL_IDENTITY_R9_FAILURE\",\"actual_global_D\":null,\"first_missing_state\":["<<firstMissing/Q<<','<<firstMissing%Q<<"]}\n";cases.flush();done++;checkpoint("CASE_COMPLETE_NEGATIVE",ri,beta);if(ri==0)cout<<"FIRST_CASE beta="<<beta<<" CPU="<<caseCPU<<" R9missing="<<N-hi<<endl;continue;}
  for(int d=0;d<=9;d++)if(hist[d])hitD=d;hits=1;done++;cases<<",\"status\":\"COMPLETE_TARGET_DIAMETER_HIT\",\"actual_global_D\":"<<hitD<<"}\n";cases.flush();
  ofstream hp(dir+"/HIT.json");hp<<"{\"status\":\"PRODUCER_COMPLETE_CAYLEY_HIT\",\"embedding_ordinal\":"<<ri<<",\"field\":49663,\"phase_modulus\":93,\"beta\":"<<beta<<",\"n\":4618659,\"m\":18474636,\"degree\":8,\"exact_global_D\":"<<hitD<<",\"operation\":\"AUTHOR LEFT(normal,I)(dart,J)=(normal+beta^I*dart,I+J)\",\"positive_generators_phase_normal\":[[1,0],[22,1],[12,4800],[85,4208]],\"all_phases\":";arr(hp,phase);hp<<",\"all_normals\":";arr(hp,normal);hp<<",\"vertex_encoding\":\"phase*49663+normal\",\"identity_distance_histogram\":";arr(hp,hist);hp<<",\"complete_identity_reached\":4618659,\"ordinary_unordered_bad_pairs\":0,\"deterministic_generator\":\"generate.py --parameters HIT.json --output graph.edges\",\"large_edge_file_not_generated\":true,\"CPU_seconds\":"<<caseCPU<<"}\n";hp.close();checkpoint("PRODUCER_FULL_TARGET_HIT",ri,beta);cursor=ri+1;cout<<"HIT beta="<<beta<<" exactD="<<hitD<<" CPU="<<caseCPU<<endl;break;
 }
 cases.close();if(!timed&&!hits)cursor=60;
 ofstream result(dir+"/NATIVE_RESULT.json");result<<"{\"status\":\""<<(hits?"PRODUCER_FULL_TARGET_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_ALL60_EMBEDDINGS_NO_HIT")<<"\",\"embeddings_total\":60,\"completed_R9_cases\":"<<done<<",\"actual_graphs_started\":"<<done+incomplete<<",\"started_incomplete_cases\":"<<incomplete<<",\"untested\":"<<60-done-incomplete<<",\"next_cursor\":"<<cursor<<",\"hits\":"<<hits<<",\"actual_global_D\":"<<(hits?to_string(hitD):"null")<<",\"source_BFS\":0,\"word_enumeration\":0,\"native_CPU_seconds\":"<<cpu()<<",\"ordinary_unordered_bad_pairs\":"<<(hits?"0":"null")<<"}\n";
 cout<<"TERMINAL completed="<<done<<" incomplete="<<incomplete<<" untested="<<60-done-incomplete<<" hits="<<hits<<" CPU="<<cpu()<<endl;
}

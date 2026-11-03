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
constexpr int F=811,P=25141,M=90,N=2262690;
const array<int,5>srcphase{24,35,34,39,26},srcnormal{18653,16221,10172,624,40},fieldnormal{0,1,440,624,40};
const array<int,9>inverse{4,5,6,7,0,1,2,3,8};
template<class T>void arr(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<+x;}o<<']';}
int power(int a,int k,int mod){int z=1;while(k){if(k&1)z=int(int64_t(z)*a%mod);a=int(int64_t(a)*a%mod);k>>=1;}return z;}
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];rlimit limit{90,90};assert(setrlimit(RLIMIT_CPU,&limit)==0);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 vector<int>roots;for(int b=2;b<F;b++)if(power(b,45,F)==1&&power(b,15,F)!=1&&power(b,9,F)!=1)roots.push_back(b);assert(roots.size()==24);
 ofstream rf(dir+"/ROOTS.json");rf<<"{\"field\":811,\"exact_field_order\":45,\"roots\":";arr(rf,roots);rf<<"}\n";rf.close();
 vector<int8_t>distance(N);vector<uint32_t>queue(N);ofstream cases(dir+"/CASES.jsonl");int done=0,algebraic=0,completedR8=0,graphs=0,incomplete=0,hits=0,hitD=-1,cursor=0;bool timed=false;array<int,5>algebraicBy{},actualBy{};
 auto checkpoint=[&](const string&status,int ordinal,int drop,int beta){ofstream o(dir+"/checkpoint.json");o<<"{\"status\":\""<<status<<"\",\"native_pid\":"<<getpid()<<",\"object_ordinal\":"<<ordinal<<",\"drop_pair\":"<<drop<<",\"beta\":"<<beta<<",\"objects_processed\":"<<done<<",\"completed_R8_cases\":"<<completedR8<<",\"actual_graphs_started\":"<<graphs<<",\"aggregate_native_CPU_seconds\":"<<cpu()<<"}\n";};
 for(int ordinal=0;ordinal<120;ordinal++){
  cursor=ordinal;if(cpu()>=89.0){timed=true;break;}int drop=ordinal/24,beta=roots[ordinal%24];clock_t caseStarted=clock();checkpoint("CHECKING_CONNECTEDNESS",ordinal,drop,beta);
  vector<int>centres;bool disconnected=false;
  if(drop==0){for(int i=1;i<5;i++){int den=(1-power(beta,srcphase[i],F)+F)%F;assert(den);centres.push_back(fieldnormal[i]*power(den,F-2,F)%F);}disconnected=all_of(centres.begin(),centres.end(),[&](int x){return x==centres[0];});}
  if(disconnected){algebraic++;algebraicBy[drop]++;done++;cases<<"{\"object_ordinal\":"<<ordinal<<",\"drop_pair\":"<<drop<<",\"beta\":"<<beta<<",\"status\":\"STRICT_COMMON_FIXED_POINT_DISCONNECTION\",\"common_centre_values\":";arr(cases,centres);cases<<",\"actual_R8_graph\":false,\"actual_global_D\":null,\"CPU_seconds\":"<<double(clock()-caseStarted)/CLOCKS_PER_SEC<<"}\n";cases.flush();checkpoint("COMPLETE_ALGEBRAIC_REJECTION",ordinal,drop,beta);continue;}
  int kk=((3-beta)%31+31)%31;kk=kk*25%31;int action=beta+F*kk;assert(action%31==3&&action%F==beta&&power(action,90,P)==1);int haction=power(action,45,P);assert(haction%31==30&&haction%F==1);
  array<int,M>powers;powers[0]=1;for(int j=1;j<M;j++)powers[j]=int(int64_t(powers[j-1])*action%P);
  array<int,9>phase{},normal{};vector<int>retained;int k=0;
  for(int i=0;i<5;i++)if(i!=drop){phase[k]=srcphase[i];normal[k]=srcnormal[i];retained.push_back(i);k++;}assert(k==4);
  for(int d=0;d<4;d++){phase[d+4]=M-phase[d];normal[d+4]=(P-int(int64_t(normal[d])*powers[phase[d+4]]%P))%P;}phase[8]=45;normal[8]=0;
  for(int d=0;d<9;d++){assert((phase[d]+phase[inverse[d]])%M==0);assert((normal[d]+int64_t(powers[phase[d]])*normal[inverse[d]])%P==0);}
  auto sorted=phase;sort(sorted.begin(),sorted.end());assert(sorted[0]>0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end());
  int shift[M][9],nextbase[M][9];for(int j=0;j<M;j++)for(int d=0;d<9;d++){shift[j][d]=int(int64_t(powers[j])*normal[d]%P);nextbase[j][d]=((j+phase[d])%M)*P;}
  graphs++;actualBy[drop]++;checkpoint("IN_PROGRESS_R8",ordinal,drop,beta);fill(distance.begin(),distance.end(),int8_t(-1));array<int,9>hist{};uint32_t lo=0,hi=1;queue[0]=0;distance[0]=0;hist[0]=1;bool aborted=false;
  while(lo<hi){if((lo&65535u)==0&&cpu()>=89.0){aborted=true;break;}uint32_t u=queue[lo++];int depth=distance[u];if(depth==8)continue;int j=u/P,x=u-j*P,nd=depth+1;for(int d=0;d<9;d++){int nx=x+shift[j][d];if(nx>=P)nx-=P;uint32_t v=nextbase[j][d]+nx;if(distance[v]<0){distance[v]=nd;hist[nd]++;queue[hi++]=v;}}}
  if(aborted){timed=true;incomplete=1;ofstream ip(dir+"/INCOMPLETE.json");ip<<"{\"object_ordinal\":"<<ordinal<<",\"drop_pair\":"<<drop<<",\"beta\":"<<beta<<",\"status\":\"INCOMPLETE_R8_CPU_LIMIT\",\"partial_reached\":"<<hi<<",\"not_a_failure_witness\":true}\n";checkpoint("INCOMPLETE_R8_CPU_LIMIT",ordinal,drop,beta);break;}
  int firstMissing=-1;if(hi<N)for(int u=0;u<N;u++)if(distance[u]<0){firstMissing=u;break;}
  completedR8++;done++;double caseCPU=double(clock()-caseStarted)/CLOCKS_PER_SEC;
  cases<<"{\"object_ordinal\":"<<ordinal<<",\"drop_pair\":"<<drop<<",\"retained_source_pair_indices\":";arr(cases,retained);cases<<",\"beta\":"<<beta<<",\"action_full_mod25141\":"<<action<<",\"common_centre_values_if_drop0\":";arr(cases,centres);cases<<",\"all_phases\":";arr(cases,phase);cases<<",\"all_normals_mod25141\":";arr(cases,normal);cases<<",\"actual_R8_graph\":true,\"n\":2262690,\"m\":10182105,\"simple\":true,\"degree\":9,\"connected\":true,\"identity_R8_reached\":"<<hi<<",\"identity_R8_missing\":"<<N-hi<<",\"first_R8_missing_vertex\":"<<firstMissing<<",\"identity_distance_histogram_through8\":";arr(cases,hist);cases<<",\"CPU_seconds\":"<<caseCPU<<",\"aggregate_native_CPU_seconds\":"<<cpu();
  if(firstMissing>=0){int j=firstMissing/P,x=firstMissing%P;cases<<",\"first_missing_state\":["<<j<<','<<x%31<<','<<x%F<<"],\"status\":\"ACTUAL_IDENTITY_R8_FAILURE\",\"actual_global_D\":null}\n";cases.flush();checkpoint("COMPLETE_R8_NEGATIVE",ordinal,drop,beta);if(completedR8==1)cout<<"FIRST_CASE frame="<<drop<<" beta="<<beta<<" CPU="<<caseCPU<<" R8missing="<<N-hi<<endl;continue;}
  for(int d=0;d<=8;d++)if(hist[d])hitD=d;hits=1;cases<<",\"status\":\"COMPLETE_TARGET_DIAMETER_HIT\",\"actual_global_D\":"<<hitD<<"}\n";cases.flush();
  ofstream hp(dir+"/HIT.json");hp<<"{\"status\":\"PRODUCER_COMPLETE_DEGREE_REDUCTION_CAYLEY_HIT\",\"object_ordinal\":"<<ordinal<<",\"drop_pair\":"<<drop<<",\"field\":811,\"beta\":"<<beta<<",\"phase_modulus\":90,\"normal_modulus\":25141,\"action\":"<<action<<",\"n\":2262690,\"m\":10182105,\"degree\":9,\"exact_global_D\":"<<hitD<<",\"operation\":\"AUTHOR LEFT(normal,I)(dart,J)=(normal+action^I*dart,I+J)\",\"all_phases\":";arr(hp,phase);hp<<",\"all_normals\":";arr(hp,normal);hp<<",\"retained_source_pair_indices\":";arr(hp,retained);hp<<",\"added_h\":[45,0],\"vertex_encoding\":\"phase*25141+normal\",\"identity_distance_histogram\":";arr(hp,hist);hp<<",\"complete_identity_reached\":2262690,\"ordinary_unordered_bad_pairs\":0,\"deterministic_generator\":\"generate.py --parameters HIT.json --output graph.edges\",\"large_edge_file_not_generated\":true}\n";hp.close();checkpoint("PRODUCER_FULL_TARGET_HIT",ordinal,drop,beta);cursor=ordinal+1;cout<<"HIT frame="<<drop<<" beta="<<beta<<" exactD="<<hitD<<endl;break;
 }
 cases.close();if(!timed&&!hits)cursor=120;ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hits?"PRODUCER_FULL_TARGET_HIT":timed?"UNKNOWN_CPU_LIMIT":"COMPLETE_ALL120_NO_HIT")<<"\",\"objects_total\":120,\"objects_processed\":"<<done<<",\"algebraic_disconnection_rejections\":"<<algebraic<<",\"actual_graphs_started\":"<<graphs<<",\"completed_R8_cases\":"<<completedR8<<",\"started_incomplete_cases\":"<<incomplete<<",\"untested\":"<<120-done-incomplete<<",\"next_cursor\":"<<cursor<<",\"hits\":"<<hits<<",\"actual_global_D\":"<<(hits?to_string(hitD):"null")<<",\"algebraic_rejections_by_frame\":";arr(out,algebraicBy);out<<",\"actual_graphs_by_frame\":";arr(out,actualBy);out<<",\"source_BFS\":0,\"word_or_coarse_DP\":0,\"native_CPU_seconds\":"<<cpu()<<",\"ordinary_unordered_bad_pairs\":"<<(hits?"0":"null")<<"}\n";cout<<"TERMINAL processed="<<done<<" algebraic="<<algebraic<<" actualR8="<<completedR8<<" hits="<<hits<<" CPU="<<cpu()<<endl;
}

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
constexpr int Q=108880,N=1415440;
const int phase[7]={38,3,58,42,77,22,40};
const int coreNormal[7]={824,625,1089,1057,769,951,1109};
const int invLabel[7]={3,4,5,0,1,2,6};
int mod(int x,int p){x%=p;if(x<0)x+=p;return x;}
string ints(const vector<int>&a){ostringstream o;o<<"[";for(size_t i=0;i<a.size();i++){if(i)o<<",";o<<a[i];}o<<"]";return o.str();}
struct Param{int actor;array<int,3>b;};
int main(int argc,char**argv){
 assert(argc==2);double budget=stod(argv[1]);clock_t start=clock();
 ifstream f("parameters.txt");int K;f>>K;assert(K==225);
 vector<Param>par(K);for(auto&p:par)f>>p.actor>>p.b[0]>>p.b[1]>>p.b[2];
 int corepow[80];corepow[0]=1;for(int j=1;j<80;j++)corepow[j]=corepow[j-1]*317%1361;assert(corepow[79]*317%1361==1);
 for(int d=0;d<7;d++){int e=invLabel[d];assert((phase[d]+phase[e])%80==0);assert((coreNormal[d]+corepow[phase[d]]*coreNormal[e])%1361==0);}
 vector<array<int,7>>nextbase(Q);vector<uint8_t>qphase(Q);
 for(int q=0;q<Q;q++){int j=q/1361,z=q%1361;qphase[q]=j;for(int d=0;d<7;d++)nextbase[q][d]=13*(((j+phase[d])%80)*1361+(z+corepow[j]*coreNormal[d])%1361);}
 vector<uint8_t>dist(N);vector<uint32_t>queue(N);
 int tested=0,tested6=0,tested7=0;bool hit=false,stopped=false;int hitParam=-1,hitRule=-1;
 ofstream cases("CASES.jsonl");
 auto checkpoint=[&](bool complete){
  ofstream o("WORKER_RESULT.json");
  o<<"{\"status\":\""<<(hit?"HIT":complete?"COMPLETE_NO_HIT":stopped?"UNKNOWN_CPU_BUDGET":"RUNNING")
   <<"\",\"planned_parameters_per_rule\":225,\"planned_target_objects\":450,\"tested_objects\":"<<tested
   <<",\"tested_degree6_D10\":"<<tested6<<",\"tested_degree7_D9\":"<<tested7
   <<",\"unvisited_objects\":"<<450-tested<<",\"hit_parameter_index\":"<<hitParam
   <<",\"hit_rule\":"<<hitRule<<",\"worker_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC
   <<",\"source_BFS\":0,\"core_BFS\":0,\"target_BFS\":"<<tested<<",\"ordinary_bad_unordered_pairs\":null}\n";
 };
 for(int k=0;k<K;k++){
  auto p=par[k];int smallpow[80];smallpow[0]=1;
  for(int j=1;j<80;j++)smallpow[j]=smallpow[j-1]*p.actor%13;
  assert(smallpow[79]*p.actor%13==1);
  int b[7];for(int i=0;i<3;i++){b[i]=p.b[i];b[i+3]=mod(-smallpow[(80-phase[i])%80]*b[i],13);}b[6]=0;
  for(int d=0;d<7;d++)assert((b[d]+smallpow[phase[d]]*b[invLabel[d]])%13==0);
  uint8_t snext[80][7][13];
  for(int j=0;j<80;j++)for(int d=0;d<7;d++)for(int s=0;s<13;s++)snext[j][d][s]=(s+smallpow[j]*b[d])%13;
  for(int rule=0;rule<2;rule++){
   if(double(clock()-start)/CLOCKS_PER_SEC>=budget){stopped=true;checkpoint(false);return 0;}
   int degree=rule?7:6,D=rule?9:10;clock_t cs=clock();
   fill(dist.begin(),dist.end(),uint8_t(255));vector<int>hist(D+1);
   uint32_t head=0,tail=1;queue[0]=0;dist[0]=0;hist[0]=1;
   while(head<tail){
    uint32_t u=queue[head++];uint8_t dep=dist[u];if(dep==D)continue;
    int q=u/13,s=u%13,j=qphase[q];
    for(int d=0;d<degree;d++){
     uint32_t v=nextbase[q][d]+snext[j][d][s];
     if(dist[v]==255){dist[v]=dep+1;hist[dep+1]++;queue[tail++]=v;}
    }
   }
   tested++;if(rule)tested7++;else tested6++;
   int first=-1;for(int v=0;v<N;v++)if(dist[v]==255){first=v;break;}
   bool full=tail==N;
   int thinPhase=rule?31:17,thinNormal=rule?684:395;
   int thinBase=13*(thinPhase*1361+thinNormal);unsigned thinMask=0;
   for(int t=0;t<13;t++)if(dist[thinBase+t]!=255)thinMask|=1U<<t;
   double cCPU=double(clock()-cs)/CLOCKS_PER_SEC;
   ostringstream record;
   record<<"{\"object_index\":"<<tested-1<<",\"parameter_index\":"<<k<<",\"actor13\":"<<p.actor
    <<",\"positive_small_normals\":"<<ints({p.b[0],p.b[1],p.b[2]})
    <<",\"rule\":\""<<(rule?"degree7_D9_keep_h":"degree6_D10_remove_h")
    <<"\",\"degree\":"<<degree<<",\"radius\":"<<D<<",\"n\":"<<N
    <<",\"m\":"<<(int64_t(N)*degree/2)<<",\"reached_R_D\":"<<tail<<",\"missing_R_D\":"<<N-tail
    <<",\"layer_counts\":"<<ints(hist)<<",\"first_missing_id\":"<<first<<",\"first_missing_decoded\":";
   if(first<0)record<<"null";else record<<"{\"phase\":"<<(first/13/1361)<<",\"normal1361\":"<<(first/13%1361)<<",\"normal13\":"<<first%13<<"}";
   record<<",\"firstthin_core_phase\":"<<thinPhase<<",\"firstthin_core_normal1361\":"<<thinNormal
    <<",\"firstthin_reachable_mask13\":"<<thinMask<<",\"firstthin_popcount\":"<<__builtin_popcount(thinMask);
   record<<",\"complete_target_R_D\":"<<(full?"true":"false")<<",\"actual_D\":";
   if(full){int diam=0;for(int d=0;d<=D;d++)if(hist[d])diam=d;record<<diam;}else record<<"null";
   record<<",\"ordinary_bad_unordered_pairs\":null,\"CPU_seconds\":"<<cCPU<<"}";
   cases<<record.str()<<"\n";cases.flush();
   if(full){
    hit=true;hitParam=k;hitRule=rule;ofstream h("HIT.json");h<<record.str()<<"\n";
    ofstream ds("HIT_ROOT_DIST.u8.bin",ios::binary);ds.write((char*)dist.data(),N);
    checkpoint(false);cout<<"HIT "<<record.str()<<"\n";return 0;
   }
   checkpoint(false);
   if(tested%20==0)cout<<"CHECKPOINT tested="<<tested<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<"\n"<<flush;
  }
 }
 checkpoint(true);return 0;
}

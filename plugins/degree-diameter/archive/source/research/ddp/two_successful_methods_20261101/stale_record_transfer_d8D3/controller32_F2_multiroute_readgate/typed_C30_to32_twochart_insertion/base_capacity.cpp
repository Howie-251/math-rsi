#include<fstream>
#include<iostream>
#include<sstream>
#include<array>
#include<vector>
#include<ctime>
#include<algorithm>
using namespace std;
int main(){
 double start=double(clock())/CLOCKS_PER_SEC;int old[30][4];ifstream in("INPUT_CONTROLLER.txt");for(auto&r:old)for(auto&p:r)in>>p;
 ifstream rows("ALL_INSERTION_RESULTS.tsv");string line;getline(rows,line);long raw=0,simple=0,survive=0;array<long,586> hist{};bool complete=true;
 ofstream out("BASE_CAPACITY_EACH_PARAMETER.tsv");out<<"i\tj\tk\tl\tminimumcapacity\tfirstminimumtarget\n";
 ofstream surv("BASE_CAPACITY_SURVIVORS.tsv");surv<<"i\tj\tk\tl\tminimumcapacity\n";
 while(getline(rows,line)){
  if((raw&255)==0&&double(clock())/CLOCKS_PER_SEC-start>3){complete=false;break;}
  int i,j,k,l,ok;istringstream s(line);s>>i>>j>>k>>l>>ok;++raw;if(!ok)continue;++simple;
  int A[32],B[32],Ai[32],Bi[32],C[32][4];for(int u=0;u<30;++u){A[u]=old[u][0];B[u]=old[u][2];}
  A[30]=A[i];A[i]=30;A[31]=A[j];A[j]=31;B[30]=B[k];B[k]=30;B[31]=B[l];B[l]=31;
  for(int u=0;u<32;++u){Ai[A[u]]=u;Bi[B[u]]=u;}
  for(int u=0;u<32;++u){C[u][0]=A[u];C[u][1]=Ai[u];C[u][2]=B[u];C[u][3]=Bi[u];}
  int cur[32]={},total[32]={};cur[30]=total[30]=1;
  for(int step=1;step<=3;++step){int next[32]={};for(int u=0;u<32;++u)if(cur[u])for(int p=0;p<4;++p)next[C[u][p]]+=2*cur[u];for(int u=0;u<32;++u){cur[u]=next[u];total[u]+=next[u];}}
  int best=*min_element(total,total+32),v=int(min_element(total,total+32)-total);++hist[best];
  out<<i<<'\t'<<j<<'\t'<<k<<'\t'<<l<<'\t'<<best<<'\t'<<v<<'\n';
  if(best>=8){++survive;surv<<i<<'\t'<<j<<'\t'<<k<<'\t'<<l<<'\t'<<best<<'\n';}
 }
 ofstream r("BASE_CAPACITY_RESULT.json");r<<"{\"status\":\""<<(!complete?"UNKNOWN_POSTPROCESS_CPU_CAP":survive?"COMPLETE_CAPACITY_GATE_WITH_SURVIVORS":"COMPLETE_NO_ALL_SIMPLE_INSERTION_CONTROLLERS_ANY_TWOCHOICE_FIBERRULE")<<"\",\"rows_read\":"<<raw<<",\"simple_checked\":"<<simple<<",\"survivors\":"<<survive<<",\"complete\":"<<(complete?"true":"false")<<",\"native_CPU\":"<<double(clock())/CLOCKS_PER_SEC-start<<",\"mincapacity_histogram\":[";bool first=true;for(int t=0;t<586;++t)if(hist[t]){if(!first)r<<',';first=false;r<<"{\"capacity\":"<<t<<",\"count\":"<<hist[t]<<'}';}r<<"]}\n";
 cout<<"savedrows="<<raw<<" simple="<<simple<<" survive="<<survive<<" CPU="<<double(clock())/CLOCKS_PER_SEC-start<<endl;
}

#include <algorithm>
#include <array>
#include <cassert>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sys/resource.h>
#include <unistd.h>
#include <vector>
using namespace std;
const int N=3750;
double cpu0;
double cpu(){return double(clock())/CLOCKS_PER_SEC-cpu0;}
int main(){
 cpu0=double(clock())/CLOCKS_PER_SEC;
 rlimit limit{45,46};setrlimit(RLIMIT_CPU,&limit);
 ofstream("HANDLE.json")<<"{\"status\":\"RUNNING\",\"pid\":"<<getpid()<<"}\n";
 ifstream in("INPUT.txt");int C[30][4],M[4][5][125];
 for(auto&row:C)for(int&v:row)in>>v;
 for(auto&port:M)for(auto&noise:port)for(int&v:noise)in>>v;
 int count;in>>count;ofstream log("CASES.jsonl");
 vector<array<int,5>> cases(count);for(auto&row:cases)for(int&v:row)in>>v;
 int complete=0,hit=-1,generated=0;bool budget=false;
 vector<vector<int>> G(N);vector<int> distance(N),queue(N);vector<long long> totals(5,0);
 for(int k=0;k<count;k++){
  if(cpu()>=44){budget=true;break;}
  auto c=cases[k];vector<int>A[4];A[0]={c[0],c[1]};A[2]={c[2],c[3],c[4]};
  for(int t:A[0])A[1].push_back((5-t)%5);
  for(int t:A[2])A[3].push_back((5-t)%5);
  for(int a=0;a<30;a++)for(int x=0;x<125;x++){
   int u=a*125+x;G[u].clear();
   for(int p=0;p<4;p++)for(int t:A[p])G[u].push_back(C[a][p]*125+M[p][t][x]);
   sort(G[u].begin(),G[u].end());assert(G[u].size()==10);
   assert(adjacent_find(G[u].begin(),G[u].end())==G[u].end());
   assert(!binary_search(G[u].begin(),G[u].end(),u));
  }
  for(int u=0;u<N;u++)for(int v:G[u])assert(binary_search(G[v].begin(),G[v].end(),u));
  generated++;int checked=0,badroot=-1,missing=-1,reached=0;vector<int> layers(5);
  fill(totals.begin(),totals.end(),0);
  for(int s=0;s<N;s++){
   if(cpu()>=44){budget=true;break;}
   fill(distance.begin(),distance.end(),-1);distance[s]=0;queue[0]=s;int tail=1;
   fill(layers.begin(),layers.end(),0);layers[0]=1;
   for(int head=0;head<tail;head++){
    int u=queue[head];if(distance[u]==4)continue;
    for(int v:G[u])if(distance[v]<0){distance[v]=distance[u]+1;queue[tail++]=v;layers[distance[v]]++;}
   }
   checked++;reached=tail;
   if(tail<N){badroot=s;missing=find(distance.begin(),distance.end(),-1)-distance.begin();break;}
   for(int r=0;r<5;r++)totals[r]+=layers[r];
  }
  bool pass=!budget&&badroot<0&&checked==N;
  log<<"{\"case\":"<<k<<",\"A0\":["<<c[0]<<","<<c[1]<<"],\"A2\":["<<c[2]<<","<<c[3]<<","<<c[4]<<"],\"n\":3750,\"m\":18750,\"degree\":10,\"roots_checked\":"<<checked<<",\"R4_pass\":"<<(pass?"true":"false")<<",\"bad_root\":"<<badroot<<",\"first_missing\":"<<missing<<",\"reached_at_last_root\":"<<reached<<",\"last_root_layers\":[";
  for(int r=0;r<5;r++)log<<(r?",":"")<<layers[r];
  log<<"],\"budget_exhausted\":"<<(budget?"true":"false")<<",\"cumulative_cpu\":"<<cpu()<<"}\n";log.flush();
  if(budget)break;complete++;
  if(pass){
   hit=k;ofstream edges("graph_d10_D4_n3750.edges");edges<<N<<" "<<18750<<"\n";
   for(int u=0;u<N;u++)for(int v:G[u])if(u<v)edges<<u<<" "<<v<<"\n";
   ofstream params("HIT.json");params<<"{\"case\":"<<k<<",\"A0\":["<<c[0]<<","<<c[1]<<"],\"A2\":["<<c[2]<<","<<c[3]<<","<<c[4]<<"],\"n\":3750,\"m\":18750,\"maxdegree\":10,\"all3750roots_R4_pass\":true,\"source_old_edges_retained_claimed\":false,\"ordered_distance_counts\":[";
   for(int r=0;r<5;r++)params<<(r?",":"")<<totals[r];params<<"]}\n";break;
  }
 }
 ofstream result("RESULT.json");result<<"{\"status\":\""<<(hit>=0?"NEW_GRAPH_HIT_NEEDS_INDEPENDENT_CHECK":budget?"CPU_BUDGET_PARTIAL":"COMPLETE_100_NO_HIT")<<"\",\"complete_cases\":"<<complete<<",\"generated_graphs\":"<<generated<<",\"hit_case\":"<<hit<<",\"untested_or_incomplete\":"<<count-complete<<",\"CPU_seconds\":"<<cpu()<<",\"pid\":"<<getpid()<<"}\n";
 ofstream("HANDLE.json")<<"{\"status\":\"TERMINAL\",\"pid\":"<<getpid()<<"}\n";
 cout<<"Generated "<<generated<<" complete "<<complete<<" hit "<<hit<<" CPU "<<cpu()<<"\n";
}

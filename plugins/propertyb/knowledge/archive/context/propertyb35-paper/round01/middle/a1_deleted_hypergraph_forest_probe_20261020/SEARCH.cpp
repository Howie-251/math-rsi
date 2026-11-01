#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
using H=array<unsigned,29>;
constexpr int N=29;
const int W[5]={506,22,132,572,2002};
mt19937_64 rng;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int ri(int n){return int(rng()%n);}
int pop(unsigned a){return __builtin_popcount(a);}
struct State {H e; int w[N][N]{}; long sum=0; int F=0;};
int prim(const State &s){
 int key[N];bool vis[N]{};fill(key,key+N,-1);key[0]=0;int total=0;
 for(int k=0;k<N;k++){int v=-1;for(int i=0;i<N;i++)if(!vis[i]&&(v<0||key[i]>key[v]))v=i;
  assert(v>=0);vis[v]=true;total+=key[v];for(int j=0;j<N;j++)if(!vis[j])key[j]=max(key[j],s.w[v][j]);}
 return total;
}
void rebuild(State &s){s.sum=0;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){int w=W[pop(s.e[i]&s.e[j])];s.w[i][j]=s.w[j][i]=w;s.sum+=w;}s.F=prim(s);}
State initial(){
 State s;for(int i=0;i<20;i++){s.e[i]=0;for(int j=0;j<5;j++)s.e[i]|=1u<<((i+j)%20);}
 vector<int> stubs;for(int i=0;i<20;i++)for(int j=0;j<(i<5?1:i<10?2:3);j++)stubs.push_back(i);
 for(;;){shuffle(stubs.begin(),stubs.end(),rng);bool okay=true;for(int k=0;k<9;k++){unsigned m=0;for(int t=0;t<5;t++)m|=1u<<stubs[5*k+t];s.e[20+k]=m;if(pop(m)!=5)okay=false;}
  for(int i=0;i<N;i++)for(int j=0;j<i;j++)if(s.e[i]==s.e[j])okay=false;if(okay)break;}
 rebuild(s);return s;
}
void validate(const H &e){array<int,20>d{};for(int i=0;i<N;i++){assert(pop(e[i])==5&&e[i]<(1u<<20));for(int j=0;j<i;j++)assert(e[i]!=e[j]);for(int v=0;v<20;v++)if(e[i]>>v&1)d[v]++;}
 for(int v=0;v<20;v++)assert(d[v]==(v<5?6:v<10?7:8));}
int kruskal(const State &s){vector<array<int,3>>a;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)a.push_back({s.w[i][j],i,j});sort(a.rbegin(),a.rend());int pa[N];iota(pa,pa+N,0);auto root=[&](int x){while(pa[x]!=x)x=pa[x];return x;};int total=0,c=0;for(auto z:a){int x=root(z[1]),y=root(z[2]);if(x==y)continue;pa[x]=y;total+=z[0];c++;}assert(c==28);return total;}
void save(const State &s,const string &file,long steps,long accepted,int restart,double secs,unsigned long long seed){
 validate(s.e);assert(prim(s)==s.F&&kruskal(s)==s.F);
 int hist[5]{};for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)hist[pop(s.e[i]&s.e[j])]++;
 ofstream f(file);f<<"{\n\"scope\":\"Original20-point29-edge hypergraph only; no paircover or A1-extension claim\",\n\"seed\":"<<seed<<",\n\"F\":"<<s.F<<",\n\"threshold\":9278,\n\"hit\":"<<(s.F<=9278?"true":"false")<<",\n\"objective\":\"16*maximum_spanning_tree_weight + sum_all_pair_weights\",\n\"cpu_seconds\":"<<secs<<",\n\"steps\":"<<steps<<",\n\"accepted\":"<<accepted<<",\n\"restart\":"<<restart<<",\n\"pair_weight_sum\":"<<s.sum<<",\n\"intersection_histogram\":[";
 for(int i=0;i<5;i++){if(i)f<<",";f<<hist[i];}f<<"],\n\"degrees\":[";for(int i=0;i<20;i++){if(i)f<<",";f<<(i<5?6:i<10?7:8);}f<<"],\n\"edges\":[";
 for(int i=0;i<N;i++){if(i)f<<",";f<<"[";bool first=true;for(int v=0;v<20;v++)if(s.e[i]>>v&1){if(!first)f<<",";first=false;f<<v;}f<<"]";}f<<"]\n}\n";
}
int main(int argc,char **argv){
 double budget=argc>1?stod(argv[1]):52.0;assert(budget>0&&budget<=55);unsigned long long seed=argc>2?stoull(argv[2]):20261020;string base=argc>3?argv[3]:".";rng.seed(seed);double started=cpu();
 State best=initial();long steps=0,accepted=0;int restarts=0;save(best,base+"/BEST.json",steps,accepted,restarts,cpu()-started,seed);
 cout<<"initial F="<<best.F<<" cpu="<<cpu()-started<<endl;
 while(cpu()-started<budget&&best.F>9278){
  State s=(restarts%4==0?initial():best);restarts++;int cyc=0;double temp0=1500;long curr=16L*s.F+s.sum;
  while(cyc<250000&&cpu()-started<budget&&best.F>9278){
   cyc++;steps++;int i=ri(N),j=ri(N-1);if(j>=i)j++;
   unsigned onlyi=s.e[i]&~s.e[j],onlyj=s.e[j]&~s.e[i];if(!onlyi||!onlyj)continue;
   int ai=ri(pop(onlyi)),aj=ri(pop(onlyj));int u=-1,v=-1;for(int b=0;b<20;b++){if(onlyi>>b&1&&ai--==0)u=b;if(onlyj>>b&1&&aj--==0)v=b;}
   assert(u>=0&&v>=0);unsigned oldi=s.e[i],oldj=s.e[j],ni=oldi^(1u<<u)^(1u<<v),nj=oldj^(1u<<u)^(1u<<v);
   if(ni==oldj&&nj==oldi)continue;bool duplicate=false;for(int k=0;k<N;k++)if(k!=i&&k!=j&&(s.e[k]==ni||s.e[k]==nj))duplicate=true;if(duplicate)continue;
   int oldrowi[N],oldrowj[N];copy(s.w[i],s.w[i]+N,oldrowi);copy(s.w[j],s.w[j]+N,oldrowj);long oldsum=s.sum;int oldF=s.F;s.e[i]=ni;s.e[j]=nj;
   for(int k=0;k<N;k++)if(k!=i&&k!=j){int wi=W[pop(ni&s.e[k])],wj=W[pop(nj&s.e[k])];s.sum+=wi+wj-s.w[i][k]-s.w[j][k];s.w[i][k]=s.w[k][i]=wi;s.w[j][k]=s.w[k][j]=wj;}
   s.F=prim(s);long obj=16L*s.F+s.sum;double temp=temp0*pow(0.001,double(cyc)/250000.0);double z=generate_canonical<double,53>(rng);
   if(obj<=curr||z<exp(double(curr-obj)/temp)){curr=obj;accepted++;if(s.F<best.F||(s.F==best.F&&s.sum<best.sum)){bool improve=s.F<best.F;best=s;save(best,base+"/BEST.json",steps,accepted,restarts,cpu()-started,seed);if(improve)cout<<"best F="<<best.F<<" sum="<<best.sum<<" steps="<<steps<<" cpu="<<cpu()-started<<endl;}}
   else{s.e[i]=oldi;s.e[j]=oldj;s.sum=oldsum;s.F=oldF;for(int k=0;k<N;k++){s.w[i][k]=s.w[k][i]=oldrowi[k];s.w[j][k]=s.w[k][j]=oldrowj[k];}}
  }
 }
 save(best,base+"/BEST.json",steps,accepted,restarts,cpu()-started,seed);cout<<"FINAL F="<<best.F<<" steps="<<steps<<" accepted="<<accepted<<" restarts="<<restarts<<" cpu="<<cpu()-started<<" status="<<(best.F<=9278?"THRESHOLD_HIT":"CPU_BUDGET_NO_HIT")<<endl;
}

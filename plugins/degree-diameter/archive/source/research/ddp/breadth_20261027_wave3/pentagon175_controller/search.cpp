#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <random>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cstdint>
using namespace std;
constexpr int N=175,K=700,W=3;
struct Bits{uint64_t x[W]={0,0,0};void put(int p){x[p/64]|=1ULL<<(p%64);}};
using Ext=array<pair<int,int>,N>;
bool fixedEdge[N][N],externalEdge[N][N];
array<array<uint64_t,W>,N> expected;
int score(const Ext& E,bool calibrate=false){
 array<array<int,4>,N> a;array<int,N> fill;
 for(int v=0;v<N;v++){int b=v-v%5,k=v%5;a[v][0]=b+(k+1)%5;a[v][1]=b+(k+4)%5;fill[v]=2;}
 for(auto [u,v]:E){assert(fill[u]<4&&fill[v]<4);a[u][fill[u]++]=v;a[v][fill[v]++]=u;}
 array<int,K> rev;
 for(int v=0;v<N;v++){assert(fill[v]==4);for(int j=0;j<4;j++){int u=a[v][j],found=-1;for(int k=0;k<4;k++)if(a[u][k]==v)found=4*u+k;assert(found>=0);rev[4*v+j]=found;}}
 array<Bits,K> p{},q{};
 for(int v=0;v<N;v++)for(int j=0;j<4;j++)p[4*v+j].put(v);
 for(int length=2;length<=5;length++){
  for(int v=0;v<N;v++)for(int w=0;w<W;w++){
   uint64_t z0=p[rev[4*v]].x[w],z1=p[rev[4*v+1]].x[w],z2=p[rev[4*v+2]].x[w],z3=p[rev[4*v+3]].x[w];
   q[4*v].x[w]=z1|z2|z3;q[4*v+1].x[w]=z0|z2|z3;q[4*v+2].x[w]=z0|z1|z3;q[4*v+3].x[w]=z0|z1|z2;
  }p.swap(q);
 }
 int missing=0;
 for(int v=0;v<N;v++){
  int reached=0;
  for(int w=0;w<W;w++){
   uint64_t z=p[rev[4*v]].x[w]|p[rev[4*v+1]].x[w]|p[rev[4*v+2]].x[w]|p[rev[4*v+3]].x[w];
   if(calibrate)assert(z==expected[v][w]);reached+=__builtin_popcountll(z);
  }
  missing+=N-reached;
 }
 assert(missing%2==0);return missing;
}
void save(const Ext& E,int best,int start,int step,long long scores){
 array<array<bool,N>,N> a{};
 for(int v=0;v<N;v++){int u=v-v%5+(v%5+1)%5;a[v][u]=a[u][v]=true;}
 for(auto [u,v]:E)a[u][v]=a[v][u]=true;
 ofstream out("best.edges");out<<N<<" "<<350<<"\n";
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(a[u][v])out<<u<<" "<<v<<"\n";
 ofstream ext("best.external_edges");for(auto [u,v]:E)ext<<u<<" "<<v<<"\n";
 ofstream meta("best.json");meta<<"{\"n\":175,\"m\":350,\"degree\":4,\"exact_NB5_missing_ordered_pairs\":"<<best<<",\"start\":"<<start<<",\"step\":"<<step<<",\"scores_at_save\":"<<scores<<",\"partial_controller_only\":true,\"ordinary_diameter\":\"pending independent final check\"}\n";
}
int main(int argc,char**argv){
 double t0=double(clock())/CLOCKS_PER_SEC;double budget=argc>1?stod(argv[1]):85;
 array<Ext,4> starts;ifstream in("starts.txt");for(auto &E:starts)for(auto &e:E)in>>e.first>>e.second;assert(in.good());
 ifstream calib("first_expected.txt");for(auto &row:expected)for(auto &x:row)calib>>x;
 for(int v=0;v<N;v++){int b=v-v%5;fixedEdge[v][b+(v%5+1)%5]=true;fixedEdge[v][b+(v%5+4)%5]=true;}
 mt19937_64 rng(202610271751ULL);long long proposals=0,illegal=0,scored=0,accepted=0;int best=100000,completed=0,curStart=-1,curStep=-1;bool hit=false,limit=false;
 for(int s=0;s<4&&!hit&&!limit;s++){
  Ext E=starts[s];for(auto &row:externalEdge)for(bool &x:row)x=false;
  for(auto [u,v]:E){assert(u!=v&&!fixedEdge[u][v]&&!externalEdge[u][v]);externalEdge[u][v]=externalEdge[v][u]=true;}
  int current=score(E,s==0);scored++;if(current<best){best=current;save(E,best,s,-1,scored);}if(best==0){hit=true;break;}
  for(int step=0;step<10000;step++){
   curStart=s;curStep=step;if(double(clock())/CLOCKS_PER_SEC-t0>=budget){limit=true;break;}proposals++;
   int i=rng()%N,j=rng()%N;if(i==j){illegal++;continue;}auto [u,v]=E[i];auto [w,z]=E[j];
   if(u==w||u==z||v==w||v==z){illegal++;continue;}
   int a=u,b=(rng()&1)?w:z,c=v,d=(b==w)?z:w;
   if(fixedEdge[a][b]||fixedEdge[c][d]||externalEdge[a][b]||externalEdge[c][d]){illegal++;continue;}
   externalEdge[u][v]=externalEdge[v][u]=externalEdge[w][z]=externalEdge[z][w]=false;
   externalEdge[a][b]=externalEdge[b][a]=externalEdge[c][d]=externalEdge[d][c]=true;E[i]={a,b};E[j]={c,d};
   int next=score(E);scored++;
   double temp=30.0*pow(0.02,double(step)/9999.0),coin=double(rng())/double(UINT64_MAX);
   if(next<=current||coin<exp(double(current-next)/temp)){current=next;accepted++;}
   else{externalEdge[a][b]=externalEdge[b][a]=externalEdge[c][d]=externalEdge[d][c]=false;externalEdge[u][v]=externalEdge[v][u]=externalEdge[w][z]=externalEdge[z][w]=true;E[i]={u,v};E[j]={w,z};}
   if(next<best){best=next;save(E,best,s,step,scored);}if(best==0){hit=true;break;}
  }
  if(!limit)completed++;
 }
 ofstream out("production_terminal.json");out<<"{\"status\":\""<<(hit?"FOUND_EXACT_NB5_CONTROLLER":limit?"CPU_STOP_WITH_CURSOR":"COMPLETE_4_START_PROFILE_NO_EXACT_NB5")<<"\",\"running\":false,\"found_exact_NB5\":"<<(hit?"true":"false")<<",\"starts_scope\":4,\"starts_completed\":"<<completed<<",\"proposals\":"<<proposals<<",\"illegal_proposals\":"<<illegal<<",\"exact_NB5_scores\":"<<scored<<",\"accepted_moves\":"<<accepted<<",\"best_missing_ordered_pairs\":"<<best<<",\"cursor\":{\"start\":"<<curStart<<",\"step\":"<<curStep<<"},\"production_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-t0<<",\"restarts\":0,\"entire_controller_family_exhausted\":false}\n";
 cout<<"best="<<best<<" hit="<<hit<<" completed="<<completed<<" scores="<<scored<<"\n";
}

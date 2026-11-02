#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int Q=53,L=Q*Q,N=816*L;
using Mat=array<int,4>;
Mat mm(Mat a,Mat b){return {(a[0]*b[0]+a[1]*b[2])%Q,(a[0]*b[1]+a[1]*b[3])%Q,(a[2]*b[0]+a[3]*b[2])%Q,(a[2]*b[1]+a[3]*b[3])%Q};}
int act(Mat a,int x){int u=x%Q,v=x/Q;return (a[0]*u+a[1]*v)%Q+Q*((a[2]*u+a[3]*v)%Q);}
int neg(int x){return (Q-x%Q)%Q+Q*((Q-x/Q)%Q);}
int main(int argc,char**argv){
 const clock_t started=clock();const string dir=argv[1];const double limit=stod(argv[2]);
 auto elapsed=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"cases\":[";bool hit=false,unknown=false;int evaluated=0;
 array<Mat,2> matrices={Mat{49,10,6,4},Mat{3,38,41,50}};
 for(int which=0;which<2;which++){
  if(elapsed()>=limit){unknown=true;break;}
  clock_t begin=clock();Mat I={1,0,0,1},A=matrices[which],B={0,52,1,52};array<Mat,16>ap;array<Mat,3>bp;ap[0]=bp[0]=I;
  for(int i=1;i<16;i++)ap[i]=mm(ap[i-1],A);for(int i=1;i<3;i++)bp[i]=mm(bp[i-1],B);
  array<Mat,48>rho;for(int v=0;v<16;v++)for(int u=0;u<3;u++)rho[u+3*v]=mm(bp[u],ap[v]);
  int chi[16];chi[0]=1;for(int i=1;i<16;i++)chi[i]=chi[i-1]*5%17;
  auto qm=[&](int q,int s){int c=q%17,h=q/17,u=h%3,v=h/3,d=s%17,k=s/17,us=k%3,vs=k/3;return (c+chi[v]*d)%17+17*((u+(v%2?-us:us)+3)%3+3*((v+vs)%16));};
  array<int,3>cp={0,1,5},up={0,1,2},vp={1,12,11},normal={0,Q,2*Q};array<int,6>gq,gv,ids;
  for(int j=0;j<3;j++){int uv=(-((vp[j]%2)?-1:1)*up[j]+3)%3,vv=(16-vp[j])%16,ci=(17-chi[vv]*cp[j]%17)%17,hinv=uv+3*vv;
   gq[2*j]=cp[j]+17*(up[j]+3*vp[j]);gv[2*j]=normal[j];gq[2*j+1]=ci+17*hinv;gv[2*j+1]=neg(act(rho[hinv],normal[j]));}
  for(int k=0;k<6;k++)ids[k]=L*gq[k]+gv[k];auto sorted=ids;sort(sorted.begin(),sorted.end());assert(sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end());
  for(int k=0;k<6;k++){assert(qm(gq[k],gq[k^1])==0);int a=gv[k],b=act(rho[gq[k]/17],gv[k^1]);assert((a%Q+b%Q)%Q==0&&(a/Q+b/Q)%Q==0);}
  array<array<int,6>,816>qnext;array<array<int,6>,48>sx,sy;
  for(int q=0;q<816;q++)for(int k=0;k<6;k++)qnext[q][k]=L*qm(q,gq[k]);
  for(int h=0;h<48;h++)for(int k=0;k<6;k++){int z=act(rho[h],gv[k]);sx[h][k]=z%Q;sy[h][k]=z/Q;}
  auto neighbors=[&](int u,array<int,6>& ns){int q=u/L,z=u-q*L,h=q/17,x=z%Q,y=z/Q;for(int k=0;k<6;k++){int xx=x+sx[h][k],yy=y+sy[h][k];if(xx>=Q)xx-=Q;if(yy>=Q)yy-=Q;ns[k]=qnext[q][k]+xx+Q*yy;}};
  vector<int>dist(N,-1),queue(N);int lo=0,hi=1;queue[0]=0;dist[0]=0;bool timeout=false;
  while(lo<hi){int u=queue[lo++];array<int,6>ns;neighbors(u,ns);for(int v:ns)if(dist[v]<0){dist[v]=dist[u]+1;queue[hi++]=v;}if((lo&16383)==0&&elapsed()>=limit){timeout=true;unknown=true;break;}}
  int ecc=0,missing=0,first=-1;for(int u=0;u<N;u++){ecc=max(ecc,dist[u]);if(dist[u]<0||dist[u]>10){missing++;if(first<0)first=u;}}
  const bool complete=!timeout,connected=complete&&hi==N;hit=connected&&ecc<=10;vector<int>hist(ecc+1);for(int d:dist)if(d>=0)hist[d]++;
  if(evaluated)out<<',';evaluated++;
  out<<"{\"control_index\":"<<which+1<<",\"status\":\""<<(timeout?"UNKNOWN_CPU_LIMIT":hit?"COMPLETE_D10_HIT":"COMPLETE_FIXED_CONTROL_FAILED")<<"\",\"alpha_matrix\":[";
  for(int i=0;i<4;i++){if(i)out<<',';out<<A[i];}out<<"],\"n\":"<<N<<",\"m\":"<<3LL*N<<",\"degree\":6,\"simple\":true,\"undirected\":true,\"complete_identity_BFS\":"<<(complete?"true":"false")<<",\"visited\":"<<hi<<",\"connected\":"<<(connected?"true":"false")<<",\"global_exact_D\":";if(connected)out<<ecc;else out<<"null";
  out<<",\"root_R10_missing\":"<<(complete?missing:-1)<<",\"first_target_outside_R10\":";if(complete&&first>=0)out<<first;else out<<"null";out<<",\"distance_histogram\":[";
  for(size_t j=0;j<hist.size();j++){if(j)out<<',';out<<hist[j];}out<<"],\"generators_and_true_inverses\":[";
  for(int k=0;k<6;k++){if(k)out<<',';out<<"{\"vertex\":"<<ids[k]<<",\"normal\":["<<gv[k]%Q<<','<<gv[k]/Q<<"],\"c17\":"<<gq[k]%17<<",\"u\":"<<(gq[k]/17)%3<<",\"v\":"<<(gq[k]/17)/3<<'}';}
  out<<"],\"BFS_and_model_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC;
  if(hit){
   ofstream edges(dir+"/graph_d6_D10_n2292144.edges");edges<<N<<' '<<3LL*N<<'\n';long long count=0;
   for(int u=0;u<N;u++){array<int,6>ns;neighbors(u,ns);for(int v:ns)if(u<v){edges<<u<<' '<<v<<'\n';count++;}}
   assert(count==3LL*N);edges.close();ofstream db(dir+"/identity_distances.i32le.bin",ios::binary);db.write(reinterpret_cast<const char*>(dist.data()),N*sizeof(int));
   out<<",\"exported_edges\":"<<count;
  }
  out<<'}';out.flush();cout<<"control "<<which+1<<" "<<(timeout?"UNKNOWN":hit?"HIT":"FAILED")<<" visited "<<hi<<" D "<<(connected?ecc:-1)<<" missingR10 "<<(complete?missing:-1)<<" CPU "<<elapsed()<<endl;
  if(hit||timeout)break;
 }
 out<<"],\"status\":\""<<(hit?"FIRST_D10_HIT_STOP":unknown?"UNKNOWN_CPU_LIMIT":"TWO_FIXED_CONTROLS_COMPLETE_NO_HIT")<<"\",\"controls_evaluated\":"<<evaluated<<",\"controls_unattempted\":"<<2-evaluated<<",\"native_CPU_seconds\":"<<elapsed()<<",\"source_D7_BFS_repeated\":0}\n";
}

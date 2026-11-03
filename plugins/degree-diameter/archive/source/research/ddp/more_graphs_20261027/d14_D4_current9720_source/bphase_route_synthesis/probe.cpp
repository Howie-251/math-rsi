#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
using M2=array<int,4>; using M4=array<int,16>; using V4=array<int,4>;
constexpr int C=216,L=81,N=C*L;
int mod(int x,int m){x%=m;return x<0?x+m:x;}
M2 mul(M2 a,M2 b){return{(a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,(a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3};}
int affine(const M4&a,const V4&c,int x){V4 v;for(int j=0;j<4;j++){v[j]=x%3;x/=3;}int out=0,p=1;for(int i=0;i<4;i++){int z=c[i];for(int j=0;j<4;j++)z+=a[4*i+j]*v[j];out+=mod(z,3)*p;p*=3;}return out;}
struct Frame{int B,k,l,reached,first;array<int,5>layers;};
struct Actual{int B,k,l,p,q,checked,failed,missing,first;array<int,5>layers;array<int,C>missing_cells;bool hit;};
int main(int argc,char**argv){
 assert(argc==2);string dir=argv[1];clock_t begin=clock();rlimit lim{5,5};setrlimit(RLIMIT_CPU,&lim);
 auto expired=[&](){return double(clock()-begin)/CLOCKS_PER_SEC>=4.90;};
 ifstream input(dir+"/../m9_degree16_transfer/input.txt");assert(input);array<M2,4>sl;array<M4,4>chart;array<V4,4>direction;int ignoredphase;
 for(int k=0;k<4;k++){for(int&x:sl[k])input>>x;input>>ignoredphase;for(int&x:chart[k])input>>x;for(int&x:direction[k])input>>x;}
 M4 plain;V4 c;for(int&x:plain)input>>x;for(int&x:c)input>>x;assert(input);
 vector<M2>group;M2 I={1,0,0,1};group.push_back(I);
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int cc=0;cc<3;cc++)for(int d=0;d<3;d++){M2 x={a,b,cc,d};if(mod(a*d-b*cc,3)==1&&x!=I)group.push_back(x);}assert(group.size()==24);
 array<array<int,4>,24>gstep;
 for(int g=0;g<24;g++)for(int k=0;k<4;k++){auto t=mul(group[g],sl[k]);auto it=find(group.begin(),group.end(),t);assert(it!=group.end());gstep[g][k]=it-group.begin();}
 array<array<array<int,3>,L>,4>line;
 for(int k=0;k<4;k++)for(int x=0;x<L;x++){
  for(int lambda=0;lambda<3;lambda++){V4 add;for(int j=0;j<4;j++)add[j]=lambda*direction[k][j]%3;line[k][x][lambda]=affine(chart[k],add,x);}
  auto t=line[k][x];sort(t.begin(),t.end());assert(adjacent_find(t.begin(),t.end())==t.end());
 }
 for(int k=0;k<4;k++)for(int x=0;x<L;x++)for(int y:line[k][x])assert(find(line[k^1][y].begin(),line[k^1][y].end(),x)!=line[k^1][y].end());
 array<int,L>gamma;for(int x=0;x<L;x++)gamma[x]=affine(plain,c,x);for(int x=0;x<L;x++)assert(gamma[gamma[x]]==x);
 vector<Frame>frames;vector<Actual>actuals;bool timeout=false,hit=false;int cursorB=0,cursork=1,cursorl=2,cursorparity=0;
 vector<int>dist(N),queue(N);array<array<int,8>,C>next;
 auto graph_neighbors=[&](int u,array<int,16>&out,const array<int,4>&powers){int cell=u/L,x=u%L,pos=0;for(int k=0;k<4;k++)for(int y:line[k][x])out[pos++]=L*next[cell][k]+y;for(int k=0;k<4;k++)out[pos++]=L*next[cell][k+4]+((abs(powers[k])%2)?gamma[x]:x);};
 for(int B=0;B<9&&!timeout&&!hit;B++)for(int k=1;k<=4&&!timeout&&!hit;k++)for(int l=k+1;l<=4&&!timeout&&!hit;l++){
  cursorB=B;cursork=k;cursorl=l;cursorparity=0;if(expired()){timeout=true;break;}
  array<int,4>phase={1,-1,B,-B};array<int,4>projected={k,-k,l,-l};
  for(int cell=0;cell<C;cell++){int g=cell/9,z=cell%9;for(int t=0;t<4;t++)next[cell][t]=9*gstep[g][t]+mod(z+phase[t],9);for(int t=0;t<4;t++)next[cell][t+4]=9*g+mod(z+projected[t],9);}
  array<int,C>d;d.fill(-1);array<int,C>q;int lo=0,hi=1;q[0]=0;d[0]=0;Frame frame{B,k,l,0,-1,{1,0,0,0,0}};
  for(int depth=0;depth<4;depth++){int end=hi;while(lo<end){int u=q[lo++];for(int v:next[u])if(d[v]<0){d[v]=depth+1;q[hi++]=v;}}frame.layers[depth+1]=hi-end;}
  frame.reached=hi;for(int v=0;v<C;v++)if(d[v]<0){frame.first=v;break;}frames.push_back(frame);
  if(hi<C)continue;
  for(int parity=0;parity<4&&!timeout&&!hit;parity++){
   cursorparity=parity;if(expired()){timeout=true;break;}
   int p=(parity&1)?9-k:k,r=(parity&2)?9-l:l;array<int,4>powers={p,-p,r,-r};
   for(int cell=0;cell<C;cell++){int g=cell/9,z=cell%9;for(int t=0;t<4;t++)next[cell][t+4]=9*g+mod(z+powers[t],9);auto row=next[cell];sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());assert(!binary_search(row.begin(),row.end(),cell));}
   for(int cell=0;cell<C;cell++)for(int t=0;t<8;t++)assert(next[next[cell][t]][t^1]==cell);
   Actual a{B,k,l,p,r,0,-1,0,-1,{0,0,0,0,0},{},false};
   for(int root=0;root<L;root++){
    if(expired()){timeout=true;break;}fill(dist.begin(),dist.end(),-1);lo=0;hi=1;queue[0]=root;dist[root]=0;array<int,5>layers{1,0,0,0,0};
    for(int depth=0;depth<4&&!timeout;depth++){int end=hi;while(lo<end){int u=queue[lo++];array<int,16>out;graph_neighbors(u,out,powers);for(int v:out)if(dist[v]<0){dist[v]=depth+1;queue[hi++]=v;}if((lo&1023)==0&&expired()){timeout=true;break;}}layers[depth+1]=hi-end;}
    if(timeout)break;a.checked++;if(hi<N){a.failed=root;a.missing=N-hi;a.layers=layers;for(int v=0;v<N;v++)if(dist[v]<0){if(a.first<0)a.first=v;a.missing_cells[v/L]++;}break;}
   }
   a.hit=!timeout&&a.checked==L&&a.failed<0;actuals.push_back(a);hit=a.hit;
   if(hit){ofstream edges(dir+"/graph_d16_D4_n17496.edges");edges<<N<<' '<<8LL*N<<'\n';long long m=0;for(int u=0;u<N;u++){array<int,16>out;graph_neighbors(u,out,powers);for(int v:out)if(u<v){edges<<u<<' '<<v<<'\n';m++;}}assert(m==8LL*N);}
  }
 }
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_D4_HIT_REQUIRES_PARENT_CHECK":timeout?"UNKNOWN_NATIVE_CPU_LIMIT":"COMPLETE_FINITE_FAMILY_NO_D4")<<"\",\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<",\"coarse_frames_checked\":"<<frames.size()<<",\"coarse_frames_total\":54,\"actual_models_checked\":"<<actuals.size()<<",\"full_hits\":"<<int(hit)<<",\"cursor\":{\"b_phase\":"<<cursorB<<",\"class_k\":"<<cursork<<",\"class_l\":"<<cursorl<<",\"parity_index\":"<<cursorparity<<"},\"frames\":[";
 for(int j=0;j<(int)frames.size();j++){auto&f=frames[j];if(j)out<<',';out<<"{\"b_phase\":"<<f.B<<",\"projected_classes\":["<<f.k<<','<<f.l<<"],\"controller_R4_reached\":"<<f.reached<<",\"controller_R4_missing\":"<<C-f.reached<<",\"first_missing_controller\":";if(f.first<0)out<<"null";else out<<f.first;out<<",\"layers\":[";for(int t=0;t<5;t++){if(t)out<<',';out<<f.layers[t];}out<<"]}";}
 out<<"],\"actual_models\":[";
 for(int j=0;j<(int)actuals.size();j++){auto&a=actuals[j];if(j)out<<',';out<<"{\"b_phase\":"<<a.B<<",\"projected_classes\":["<<a.k<<','<<a.l<<"],\"positive_plain_powers\":["<<a.p<<','<<a.q<<"],\"n\":"<<N<<",\"m\":"<<8LL*N<<",\"max_min_degree\":16,\"simple_undirected\":true,\"actual_implicit_adjacency\":true,\"fiber_representatives_checked\":"<<a.checked<<",\"failed_source_fiber\":";if(a.failed<0)out<<"null";else out<<a.failed;out<<",\"root_R4_missing\":"<<a.missing<<",\"first_missing_target\":";if(a.first<0)out<<"null";else out<<a.first;out<<",\"full_D4\":"<<(a.hit?"true":"false")<<",\"global_D\":"<<(a.hit?"4":"null")<<",\"missing_by_controller\":[";for(int t=0;t<C;t++){if(t)out<<',';out<<a.missing_cells[t];}out<<"]}";}
 out<<"]}\n";cout<<"frames="<<frames.size()<<" actual="<<actuals.size()<<" hit="<<hit<<" timeout="<<timeout<<" nativeCPU="<<double(clock()-begin)/CLOCKS_PER_SEC<<endl;
}

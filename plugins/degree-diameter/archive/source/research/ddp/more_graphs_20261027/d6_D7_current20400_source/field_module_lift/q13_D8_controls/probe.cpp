#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using Mat=array<int,4>;
Mat mm(Mat a,Mat b){return{(a[0]*b[0]+a[1]*b[2])%13,(a[0]*b[1]+a[1]*b[3])%13,(a[2]*b[0]+a[3]*b[2])%13,(a[2]*b[1]+a[3]*b[3])%13};}
int act(Mat a,int x){int u=x%13,v=x/13;return(a[0]*u+a[1]*v)%13+13*((a[2]*u+a[3]*v)%13);}
int neg(int x){return(13-x%13)%13+13*((13-x/13)%13);}
int main(int argc,char**argv){
 clock_t start=clock();string dir=argv[1];const int L=169,N=816*L;
 Mat I={1,0,0,1},A=(stoi(argv[2])==5?Mat{8,6,1,5}:Mat{9,5,1,4}),B={0,12,1,12};array<Mat,16>ap;array<Mat,3>bp;ap[0]=bp[0]=I;
 for(int i=1;i<16;i++)ap[i]=mm(ap[i-1],A);for(int i=1;i<3;i++)bp[i]=mm(bp[i-1],B);
 assert(mm(ap[15],A)==I);assert(mm(bp[2],B)==I);assert(mm(A,B)==mm(mm(B,B),A));assert(mm(A,A)==Mat({stoi(argv[2]),0,0,stoi(argv[2])}));array<Mat,48>rho;for(int v=0;v<16;v++)for(int u=0;u<3;u++)rho[u+3*v]=mm(bp[u],ap[v]);
 int chi[16];chi[0]=1;for(int i=1;i<16;i++)chi[i]=chi[i-1]*5%17;
 auto qm=[&](int q,int s){int c=q%17,h=q/17,u=h%3,v=h/3,d=s%17,k=s/17,us=k%3,vs=k/3;return(c+chi[v]*d)%17+17*((u+(v%2?-us:us)+3)%3+3*((v+vs)%16));};
 array<int,3>cp={0,1,5},up={0,1,2},vp={1,12,11},normal={0,13,26};array<int,6>gq,gv,ids;
 for(int j=0;j<3;j++){int uv=(-((vp[j]%2)?-1:1)*up[j]+3)%3,vv=(16-vp[j])%16,ci=(17-chi[vv]*cp[j]%17)%17,hinv=uv+3*vv;
  gq[2*j]=cp[j]+17*(up[j]+3*vp[j]);gv[2*j]=normal[j];gq[2*j+1]=ci+17*hinv;gv[2*j+1]=neg(act(rho[hinv],normal[j]));}
 for(int k=0;k<6;k++)ids[k]=L*gq[k]+gv[k];auto s=ids;sort(s.begin(),s.end());assert(s[0]!=0&&adjacent_find(s.begin(),s.end())==s.end());
 array<array<int,6>,816>qnext;array<array<int,6>,48>shift;
 for(int q=0;q<816;q++)for(int k=0;k<6;k++)qnext[q][k]=qm(q,gq[k]);
 for(int h=0;h<48;h++)for(int k=0;k<6;k++)shift[h][k]=act(rho[h],gv[k]);
 array<array<int,L>,L>add;for(int x=0;x<L;x++)for(int y=0;y<L;y++)add[x][y]=(x%13+y%13)%13+13*((x/13+y/13)%13);
 vector<array<int,6>>adj(N);for(int u=0;u<N;u++){int q=u/L,z=u%L,h=q/17;for(int k=0;k<6;k++)adj[u][k]=L*qnext[q][k]+add[z][shift[h][k]];
  auto a=adj[u];sort(a.begin(),a.end());assert(adjacent_find(a.begin(),a.end())==a.end()&&find(a.begin(),a.end(),u)==a.end());}
 for(int u=0;u<N;u++)for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());
 vector<int>d(N,-1),q(N);int lo=0,hi=0;d[0]=0;q[hi++]=0;while(lo<hi){int u=q[lo++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q[hi++]=v;}}
 bool connected=hi==N;int ecc=*max_element(d.begin(),d.end()),miss=count_if(d.begin(),d.end(),[](int z){return z<0||z>8;});bool hit=connected&&ecc<=8;
 vector<int>hist(ecc+1);for(int x:d)if(x>=0)hist[x]++;
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"COMPLETE_CAYLEY_D8_HIT":"SINGLE_CONTROL_FAILED_STOP")<<"\",\"n\":"<<N<<",\"m\":"<<3*N<<",\"degree\":6,\"simple\":true,\"undirected\":true,\"connected\":"<<(connected?"true":"false")<<",\"root\":0,\"roots_BFS\":1,\"visited\":"<<hi<<",\"actual_global_D\":";
 if(connected)out<<ecc;else out<<"null";out<<",\"root_R8_missing\":"<<miss<<",\"accepted_D8\":"<<(hit?"true":"false")<<",\"distance_histogram\":[";
 for(size_t i=0;i<hist.size();i++){if(i)out<<',';out<<hist[i];}out<<"],\"positive_and_true_inverse_generator_ids\":[";
 for(int i=0;i<6;i++){if(i)out<<',';out<<ids[i];}out<<"],\"source_BFS_repeated\":0,\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
 if(hit){ofstream edges(dir+"/graph_d6_D8_n137904.edges");edges<<N<<' '<<3*N<<'\n';long long count=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){edges<<u<<' '<<v<<'\n';count++;}assert(count==3LL*N);}
 cout<<(hit?"HIT":"FAILED")<<" connected "<<connected<<" D "<<ecc<<" missingR8 "<<miss<<endl;
}

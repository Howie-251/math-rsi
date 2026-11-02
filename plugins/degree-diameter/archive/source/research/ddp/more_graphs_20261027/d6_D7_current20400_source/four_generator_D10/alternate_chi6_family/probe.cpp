#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;using Mat=array<int,4>;
Mat mm(Mat a,Mat b){return{(a[0]*b[0]+a[1]*b[2])%5,(a[0]*b[1]+a[1]*b[3])%5,(a[2]*b[0]+a[3]*b[2])%5,(a[2]*b[1]+a[3]*b[3])%5};}
int apply(Mat a,int z){return(a[0]*(z%5)+a[1]*(z/5))%5+5*((a[2]*(z%5)+a[3]*(z/5))%5);}
int neg(int z){return(5-z%5)%5+5*((5-z/5)%5);}
int main(int argc,char**argv){
 const clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};string dir=argv[1];double budget=stod(argv[2]);const int N=20400,L=25;
 Mat I={1,0,0,1},A={4,2,1,1},B={0,4,1,4};array<Mat,16>ap;array<Mat,3>bp;ap[0]=bp[0]=I;
 for(int v=1;v<16;v++)ap[v]=mm(ap[v-1],A);for(int u=1;u<3;u++)bp[u]=mm(bp[u-1],B);
 array<array<int,L>,48>action;for(int v=0;v<16;v++)for(int u=0;u<3;u++){auto m=mm(bp[u],ap[v]);for(int z=0;z<L;z++)action[u+3*v][z]=apply(m,z);}
 int chi[16];chi[0]=1;for(int v=1;v<16;v++)chi[v]=chi[v-1]*6%17;assert(chi[8]==16);
 auto qm=[&](int q,int s){int c=q%17,h=q/17,u=h%3,v=h/3,d=s%17,k=s/17,us=k%3,vs=k/3;return(c+chi[v]*d)%17+17*((u+(v%2?-us:us)+3)%3+3*((v+vs)%16));};
 auto invq=[&](int c,int u,int v){int vv=(16-v)%16,uu=(-(v%2?-1:1)*u+3)%3;return(17-chi[vv]*c%17)%17+17*(uu+3*vv);};
 array<array<int,L>,L>add;for(int x=0;x<L;x++)for(int y=0;y<L;y++)add[x][y]=(x%5+y%5)%5+5*((x/5+y/5)%5);
 vector<pair<int,int>>lines={{1,0},{1,1},{1,2},{1,3},{1,4},{0,1}};vector<int>d(N),queue(N);
 int done=0,legal=0,connected=0,bfs=0,lastA=-1,lastB=-1,lastLine=-1;bool hit=false,limited=false;
 ofstream rows(dir+"/cases.tsv");rows<<"ordinal\ta\tb\tvx\tvy\tlegal\tvisited\texact_D_if_connected\taccepted\n";
 for(int a:{1,3,5,7})for(int b=0;b<=8;b++)for(int li=0;li<6;li++){
  lastA=a;lastB=b;lastLine=li;auto[x,y]=lines[li];int vec=x+5*y;
  array<int,4>gq={17*(3*a),invq(0,0,a),1+17*(1+3*b),invq(1,1,b)};
  array<int,4>gv={0,0,vec,neg(action[gq[3]/17][vec])},ids;
  for(int k=0;k<4;k++)ids[k]=L*gq[k]+gv[k];auto sorted=ids;sort(sorted.begin(),sorted.end());bool valid=sorted[0]!=0&&adjacent_find(sorted.begin(),sorted.end())==sorted.end();
  ++done;if(!valid){rows<<done-1<<'\t'<<a<<'\t'<<b<<'\t'<<x<<'\t'<<y<<"\t0\t0\t-1\t0\n";continue;}++legal;
  assert(qm(gq[0],gq[1])==0&&qm(gq[2],gq[3])==0);assert(add[vec][action[gq[2]/17][gv[3]]]==0);
  array<array<int,4>,816>qnext;array<array<int,4>,48>shift;
  for(int q=0;q<816;q++)for(int k=0;k<4;k++)qnext[q][k]=qm(q,gq[k]);
  for(int h=0;h<48;h++)for(int k=0;k<4;k++)shift[h][k]=action[h][gv[k]];
  fill(d.begin(),d.end(),-1);int lo=0,hi=0,ecc=0;d[0]=0;queue[hi++]=0;
  while(lo<hi){int u=queue[lo++],q=u/L,z=u%L,h=q/17;for(int k=0;k<4;k++){int v=L*qnext[q][k]+add[z][shift[h][k]];if(d[v]<0){d[v]=d[u]+1;ecc=max(ecc,d[v]);queue[hi++]=v;}}}
  ++bfs;connected+=hi==N;bool accepted=hi==N&&ecc<=10;
  rows<<done-1<<'\t'<<a<<'\t'<<b<<'\t'<<x<<'\t'<<y<<"\t1\t"<<hi<<'\t'<<(hi==N?ecc:-1)<<'\t'<<accepted<<'\n';
  if(accepted){
   hit=true;ofstream out(dir+"/FIRST_HIT.json");out<<"{\"chi17_alpha\":6,\"a\":"<<a<<",\"b\":"<<b<<",\"normal_vector\":["<<x<<','<<y<<"],\"case_ordinal\":"<<done-1<<",\"n\":20400,\"m\":40800,\"degree\":4,\"connected\":true,\"simple\":true,\"actual_global_D\":"<<ecc<<",\"ordinary_bad_unordered_pairs_targetD10\":0,\"root_BFS\":1,\"distance_histogram\":[";
   vector<int>hist(ecc+1);for(int z:d)hist[z]++;for(size_t j=0;j<hist.size();j++){if(j)out<<',';out<<hist[j];}out<<"],\"positive_and_true_inverse_generator_ids\":[";
   for(int k=0;k<4;k++){if(k)out<<',';out<<ids[k];}out<<"],\"independent_acceptance_pending\":true}\n";
   ofstream edges(dir+"/graph_d4_D10_n20400.edges");edges<<"20400 40800\n";long long count=0;
   for(int u=0;u<N;u++){int q=u/L,z=u%L,h=q/17;for(int k=0;k<4;k++){int v=L*qnext[q][k]+add[z][shift[h][k]];if(u<v){edges<<u<<' '<<v<<'\n';++count;}}}assert(count==40800);goto terminal;
  }
  if(cpu()>budget){limited=true;goto terminal;}
 }
terminal:
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_D10_HIT":limited?"UNKNOWN_CPU_LIMIT":"ALL_CHI6_216_COMPLETE_NO_HIT")<<"\",\"chi17_alpha\":6,\"settings_scope\":216,\"settings_processed\":"<<done<<",\"legal_inverseclosed4_cases\":"<<legal<<",\"connected_cases\":"<<connected<<",\"actual_new_Cayley_root_BFS\":"<<bfs<<",\"hit\":"<<(hit?"true":"false")<<",\"CPU_limited\":"<<(limited?"true":"false")<<",\"cursor\":{\"a\":"<<lastA<<",\"b\":"<<lastB<<",\"line_index\":"<<lastLine<<"},\"native_CPU_seconds\":"<<cpu()<<",\"chi5_controls_inherited\":0,\"source_BFS_repeated\":0,\"complete_edgefiles_exported\":"<<(hit?1:0)<<"}\n";
 cout<<(hit?"HIT":limited?"UNKNOWN":"COMPLETE_NO_HIT")<<" chi6 settings "<<done<<" CPU "<<cpu()<<endl;
}

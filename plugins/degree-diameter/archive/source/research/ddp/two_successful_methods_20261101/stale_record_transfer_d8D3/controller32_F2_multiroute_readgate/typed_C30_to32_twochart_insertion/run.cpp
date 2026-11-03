#include <array>
#include <vector>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <ctime>
#include <algorithm>
#include <string>
using namespace std;
using U=uint64_t;
const U FULL=~U(0);
const int BAR[4]={1,0,3,2};
struct Word{int n;array<int,3> w;U packet;};
int baseC[30][4], C[32][4];
int maps[2][4][3]={{{2,1,4},{2,1,4},{1,2,7},{1,2,7}},{{2,1,4},{2,1,4},{2,1,7},{2,1,7}}};
int V[4]={1,2,4,7};
vector<Word> words[2];
int apply(int z,int p,int x){return ((x&1)?maps[z][p][0]:0)^((x&2)?maps[z][p][1]:0)^((x&4)?maps[z][p][2]:0);}
U packet(int z,const Word&w){
 U ans=0;
 for(int x=0;x<8;++x){int out=1<<x;
  for(int k=0;k<w.n;++k){int next=0,p=w.w[k];for(int y=0;y<8;++y)if(out>>y&1){int a=apply(z,p,y);next|=(1<<a)|(1<<(a^V[p]));}out=next;}
  ans|=U(out)<<(8*x);
 }return ans;
}
int endpoint(int u,const Word&w){for(int k=0;k<w.n;++k)u=C[u][w.w[k]];return u;}
struct Bad{int root=-1,target=-1,x=-1,y=-1;};
bool test(int z,Bad&bad){
 for(int rr=0;rr<32;++rr){int u=rr<2?30+rr:rr-2;
  U cover[32]={};uint32_t fullmask=0;
  for(int p=0;p<4;++p)fullmask|=uint32_t(1)<<C[u][p];
  for(auto&w:words[z]){int v=endpoint(u,w);if(w.packet==FULL)fullmask|=uint32_t(1)<<v;else cover[v]|=w.packet;}
  for(int v=0;v<32;++v)if(!(fullmask>>v&1)&&cover[v]!=FULL){bad.root=u;bad.target=v;
   for(int x=0;x<8;++x){int byte=int((cover[v]>>(8*x))&255);if(byte!=255){bad.x=x;for(int y=0;y<8;++y)if(!(byte>>y&1)){bad.y=y;break;}break;}}return false;}
 }return true;
}
int main(){
 double start=double(clock())/CLOCKS_PER_SEC;
 ifstream in("INPUT_CONTROLLER.txt");for(auto&r:baseC)for(int&p:r)in>>p;if(!in){cerr<<"input error\n";return 2;}
 for(int u=0;u<30;++u)for(int p=0;p<4;++p)if(baseC[baseC[u][p]][BAR[p]]!=u)return 3;
 for(int z=0;z<2;++z){
  for(int p=0;p<4;++p)for(int x=0;x<8;++x)if(apply(z,BAR[p],apply(z,p,x))!=x||apply(z,BAR[p],V[p])!=V[BAR[p]])return 4;
  for(int n=0;n<=3;++n){int count=1;for(int k=0;k<n;++k)count*=4;
   for(int code=0;code<count;++code){Word w{};w.n=n;int a=code;for(int k=n-1;k>=0;--k){w.w[k]=a%4;a/=4;}
    if(n==3&&(w.w[1]==BAR[w.w[0]]||w.w[2]==BAR[w.w[1]]))continue;
    w.packet=packet(z,w);words[z].push_back(w);
   }
  }
  if(words[z].size()!=57)return 5;
 }
 long raw=0,simple=0,repeated=0,checked[2]={},rootsfail[2][32]={};bool timed=false,hit=false;int hz=-1,hi=-1,hj=-1,hk=-1,hl=-1;
 ofstream rows("ALL_INSERTION_RESULTS.tsv");rows<<"i\tj\tk\tl\tsimple\tARC_badroot\tARC_badtarget\tR_badroot\tR_badtarget\n";
 for(int i=0;i<30&&!timed&&!hit;++i)for(int j=i+1;j<30&&!timed&&!hit;++j)for(int k=0;k<30&&!timed&&!hit;++k)for(int l=0;l<30;++l){
  if(k==l)continue;
  if((raw&255)==0&&double(clock())/CLOCKS_PER_SEC-start>20){timed=true;break;}
  ++raw;int A[32],B[32],Ai[32],Bi[32];for(int u=0;u<30;++u){A[u]=baseC[u][0];B[u]=baseC[u][2];}
  A[30]=A[i];A[i]=30;A[31]=A[j];A[j]=31;
  B[30]=B[k];B[k]=30;B[31]=B[l];B[l]=31;
  for(int u=0;u<32;++u){Ai[A[u]]=u;Bi[B[u]]=u;}
  bool ok=true;for(int u=0;u<32;++u){C[u][0]=A[u];C[u][1]=Ai[u];C[u][2]=B[u];C[u][3]=Bi[u];
   for(int p=0;p<4;++p){if(C[u][p]==u)ok=false;for(int q=0;q<p;++q)if(C[u][p]==C[u][q])ok=false;}}
  if(!ok){++repeated;rows<<i<<'\t'<<j<<'\t'<<k<<'\t'<<l<<"\t0\t-1\t-1\t-1\t-1\n";continue;}
  ++simple;Bad bad[2];bool passes[2]={};
  for(int z=0;z<2;++z){++checked[z];passes[z]=test(z,bad[z]);if(!passes[z])++rootsfail[z][bad[z].root];
   if(passes[z]){hit=true;hz=z;hi=i;hj=j;hk=k;hl=l;break;}}
  rows<<i<<'\t'<<j<<'\t'<<k<<'\t'<<l<<"\t1\t"<<bad[0].root<<'\t'<<bad[0].target<<'\t'<<bad[1].root<<'\t'<<bad[1].target<<'\n';
  if(hit){ofstream c("HIT_CONTROLLER.txt");for(auto&r:C){for(int p=0;p<4;++p)c<<r[p]<<(p==3?'\n':' ');}break;}
 }
 ofstream r("NATIVE_RESULT.json");
 r<<"{\"status\":\""<<(hit?"FULL256_POINT_COVER_HIT":timed?"UNKNOWN_NATIVE_CPU_CAP":"COMPLETE_NO_TWO_FIXED_CHARTS_INSERTION_FAMILY")<<"\",\"raw_controllers_checked\":"<<raw<<",\"expected_raw\":378450,\"simple_controllers\":"<<simple<<",\"nonsimple_rejected\":"<<repeated<<",\"chart_checked\":["<<checked[0]<<','<<checked[1]<<"],\"hit\":"<<(hit?"true":"false")<<",\"hit_chart\":"<<hz<<",\"hit_tails\":["<<hi<<','<<hj<<','<<hk<<','<<hl<<"],\"complete\":"<<(!timed&&!hit?"true":"false")<<",\"CPU\":"<<double(clock())/CLOCKS_PER_SEC-start<<",\"first_badroot_counts\":[[";
 for(int z=0;z<2;++z){if(z)r<<"],[";for(int u=0;u<32;++u){if(u)r<<',';r<<rootsfail[z][u];}}r<<"]]}\n";
 cout<<(hit?"HIT":timed?"UNKNOWN":"COMPLETE_NO")<<" raw="<<raw<<" simple="<<simple<<" CPU="<<double(clock())/CLOCKS_PER_SEC-start<<endl;
 return 0;
}

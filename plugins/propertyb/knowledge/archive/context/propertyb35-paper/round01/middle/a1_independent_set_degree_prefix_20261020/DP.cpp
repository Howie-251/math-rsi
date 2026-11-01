#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <iostream>
#include <vector>
using namespace std;
static constexpr int NEG=-1000000000;
int f(int s){int a=s/5,r=s%5;return (s*s-(5-r)*a*a-r*(a+1)*(a+1))/2;}
int main(int argc,char**argv){
 int e=argc>1?atoi(argv[1]):76;int all=argc>2?atoi(argv[2]):0; int strong=argc>3?atoi(argv[3]):0;int n4cap=argc>4?atoi(argv[4]):8;
 auto low=[&](int N){int x=max(0,N-21);if(strong&&N>21){int v=8*N*(N-21)-105*n4cap;if(v>0)x=max(x,(v+83)/84);x=max(x,(8*N*(N-21)+188)/189);}if(strong>=2){int a=152*N*(N-21)-2037*n4cap;if(a>0)x=max(x,(a+1427)/1428);}return max(0,x);};
 int maxsum=2*e,S=maxsum+1;
 auto at=[&](int l,int s){return l*S+s;};
 vector<int>old(35*S,NEG),now(35*S,NEG);
 vector<vector<short>>parent(36,vector<short>(35*S,-1));
 old[at(34,0)]=0; long long reachable=1,transitions=0;
 for(int i=1;i<=35;i++){
  fill(now.begin(),now.end(),NEG);
  int cap=e+i*(i-1)/2-low(35-i);
  int minq=i<=32?1:0;
  for(int last=0;last<=34;last++)for(int sum=0;sum<=maxsum;sum++){
   int value=old[at(last,sum)];if(value==NEG)continue;
   int upper=min(last,(all||i>=2)?29:34);
   if(strong>=3)upper=min(upper,e-60+2*n4cap-(i>=13));
   for(int q=minq;q<=upper;q++){
    int newsum=sum+q;if(newsum>maxsum||newsum>cap)continue;
    int rem=35-i;
    if(newsum+q*rem<maxsum)continue;
    if(newsum+max(0,32-i)>maxsum)continue;
    ++transitions;int nv=value+f(34-q),id=at(q,newsum);
    if(nv>now[id]){now[id]=nv;parent[i][id]=last;}
   }
  }
  for(int v:now)reachable+=(v!=NEG);
  old.swap(now);
 }
 int best=NEG,lastbest=-1;
 for(int q=0;q<=34;q++)if(old[at(q,maxsum)]>best){best=old[at(q,maxsum)];lastbest=q;}
 cout<<"{\"e\":"<<e<<",\"allcritical\":"<<all<<",\"strong_prefix\":"<<strong<<",\"n4_cap\":"<<n4cap<<",\"bound\":"<<best<<",\"states\":"<<reachable<<",\"transitions\":"<<transitions<<",\"q\":[";
 if(best!=NEG){
  vector<int>seq(35);int s=maxsum,l=lastbest;
  for(int i=35;i>=1;i--){seq[i-1]=l;int prev=parent[i][at(l,s)];assert(prev>=0);s-=l;l=prev;}
  assert(s==0);int sum=0,obj=0,zeros=0;
  for(int i=0;i<35;i++){int q=seq[i];sum+=q;obj+=f(34-q);zeros+=q==0;assert(i==0||seq[i-1]>=q);assert(sum<=e+(i+1)*i/2-low(34-i));assert(q>=0&&q<=34);if(i>=1||all)assert(q<=29);if(i)cout<<",";cout<<q;}
  assert(sum==2*e&&obj==best&&zeros<=3);
 }
 cout<<"]}\n";
}

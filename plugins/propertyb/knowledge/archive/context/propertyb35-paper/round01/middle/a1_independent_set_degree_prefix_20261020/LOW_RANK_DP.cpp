#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std; const int NEG=-1000000000;
int f(int s){int a=s/5,r=s%5;return (s*s-(5-r)*a*a-r*(a+1)*(a+1))/2;}
int main(int argc,char**argv){
 int E=atoi(argv[1]),t=atoi(argv[2]),target=2*E,S=target+1,R=min(34,E-60+2*t);long long states=0,trans=0;
 auto lower=[&](int N){return max({0,N-21,(8*N*(N-21)-105*t+83)/84,(8*N*(N-21)+188)/189,(152*N*(N-21)-2037*t+1427)/1428});};
 // All numerator divisions with negative numerators are dominated by max(0,...).
 auto cap=[&](int i){int c=E+i*(i-1)/2-lower(35-i);if(i==2)c=min(c,E-49+2*t);return c;};
 auto at=[&](int q,int sum){return q*S+sum;};
 int totalbest=NEG;vector<int>bestseq;
 for(int M=(target+34)/35;M<=R;M++){
  if(M>cap(1))continue;
  vector<int>old(35*S,NEG),now(35*S,NEG);vector<vector<short>>par(36,vector<short>(35*S,-1));old[at(M,M)]=f(34-M);
  for(int i=2;i<=35;i++){
   fill(now.begin(),now.end(),NEG);
   int minq=i<=max(15,M-15)?2:(i<=32?1:0);
   for(int last=0;last<=M;last++)for(int sum=0;sum<=target;sum++)if(old[at(last,sum)]!=NEG){
    states++;int upper=min({last,29,R-(i>=13)});
    for(int q=minq;q<=upper;q++){
     int ns=sum+q;if(ns>target||ns>cap(i))continue;
     if(ns+q*(35-i)<target||ns+max(0,32-i)>target)continue;
     trans++;int v=old[at(last,sum)]+f(34-q),id=at(q,ns);
     if(v>now[id]){now[id]=v;par[i][id]=last;}
    }
   }
   old.swap(now);
  }
  int best=NEG,last=-1;for(int q=0;q<=34;q++)if(old[at(q,target)]>best){best=old[at(q,target)];last=q;}
  if(best>totalbest){
   vector<int>seq(35);int sum=target,l=last;
   for(int i=35;i>=2;i--){seq[i-1]=l;int prev=par[i][at(l,sum)];assert(prev>=0);sum-=l;l=prev;}
   assert(sum==M&&l==M);seq[0]=M;bestseq=seq;totalbest=best;
  }
 }
 assert(totalbest>NEG);int sum=0,obj=0,l=0,z=0;
 for(int i=0;i<35;i++){int q=bestseq[i];sum+=q;obj+=f(34-q);l+=q==1;z+=q==0;assert(sum<=cap(i+1));if(i)assert(q<=bestseq[i-1]&&q<=29);}
 assert(sum==target&&obj==totalbest&&z<=3&&l+z<=20&&bestseq[0]+l+z<=50&&bestseq[12]<=R-1);
 cout<<"{\"e\":"<<E<<",\"n4_cap\":"<<t<<",\"allcritical\":0,\"bound\":"<<totalbest<<",\"states\":"<<states<<",\"transitions\":"<<trans<<",\"q\":[";
 for(int i=0;i<35;i++){if(i)cout<<",";cout<<bestseq[i];}cout<<"]}\n";
}

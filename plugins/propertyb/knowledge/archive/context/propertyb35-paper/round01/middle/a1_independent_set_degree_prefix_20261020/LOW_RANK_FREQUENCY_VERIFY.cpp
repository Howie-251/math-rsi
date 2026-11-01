#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <unordered_map>
using namespace std; const int BAD=-1000000000;
int f(int s){int v=0;for(int j=0;j<5;j++){int a=s/5+(j<s%5);v+=a*a;}return (s*s-v)/2;}
int main(int argc,char**argv){
 int E=atoi(argv[1]),t=atoi(argv[2]),target=2*E,R=E-60+2*t;
 auto lower=[&](int N){return max({0,N-21,(8*N*(N-21)-105*t+83)/84,(8*N*(N-21)+188)/189,(152*N*(N-21)-2037*t+1427)/1428});};
 auto cap=[&](int i){int b=E+i*(i-1)/2-lower(35-i);return i==2?min(b,E-49+2*t):b;};
 unordered_map<int,int>memo;
 function<int(int,int,int,int)>solve=[&](int q,int n,int s,int M)->int{
  if(s>target||s+q*(35-n)<target)return BAD;
  if(n==35)return s==target?0:BAD;
  if(q==1){
   if(n<15)return BAD;
   int c=target-s,z=35-n-c;if(c<0||z<0||z>3||M+c+z>50)return BAD;
   for(int a=1;a<=c;a++)if(s+a>cap(n+a))return BAD;
   for(int a=1;a<=z;a++)if(target>cap(n+c+a))return BAD;
   return c*f(33)+z*f(34);
  }
  int key=((q*36+n)*(target+1)+s)*35+M;auto hit=memo.find(key);if(hit!=memo.end())return hit->second;
  int maxc=min(35-n,(target-s)/q);if(q>R)maxc=0;if(q==R)maxc=min(maxc,12);if(q>29)maxc=min(maxc,max(0,1-n));
  int best=BAD;
  for(int c=0;c<=maxc;c++){
   bool ok=true;for(int a=1;a<=c;a++)if(s+a*q>cap(n+a)){ok=false;break;}if(!ok)continue;
   int newM=M?M:(c?q:0);int v=solve(q-1,n+c,s+c*q,newM);if(v==BAD)continue;
   best=max(best,c*f(34-q)+v);
  }
  memo[key]=best;return best;
 };
 int best=solve(34,0,0,0);cout<<"{\"e\":"<<E<<",\"n4_cap\":"<<t<<",\"bound\":"<<best<<",\"states\":"<<memo.size()<<"}\n";
}

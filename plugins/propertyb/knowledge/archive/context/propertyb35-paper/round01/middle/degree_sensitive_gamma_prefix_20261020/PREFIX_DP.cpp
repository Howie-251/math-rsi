#include <algorithm>
#include <cassert>
#include <ctime>
#include <functional>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
int f(int s){int a=s/5,b=s%5;return (s*s-(5-b)*a*a-b*(a+1)*(a+1))/2;}
int ceildiv(int a,int b){return a>=0?(a+b-1)/b:a/b;}
int main(int argc,char**argv){
 int W=atoi(argv[1]),S5=atoi(argv[2]),E=atoi(argv[3]),t=atoi(argv[4]),target=2*E,sz=target+1;
 vector<int> cap(36,target);for(int k=1;k<=13;k++){int N=35-k,Wp=min(W,W-k*(S5-5)+4*k*(k-1)/2),T=Wp-N*(N-1)/2;int R=ceildiv(152*N*(N-21)-273*T,882);int B=max({0,R-2*t,ceildiv(152*N*(N-21)-2037*t,1428)});cap[k]=E+k*(k-1)/2-B;}
 const int BAD=-1000000000;auto ix=[&](int q,int s){return q*sz+s;};long long transitions=0;
 vector<int> old(30*sz,BAD),now(30*sz,BAD);vector<vector<short>> par(36,vector<short>(30*sz,-1));old[ix(29,0)]=0;
 clock_t c0=clock();
 for(int n=1;n<=35;n++){
  fill(now.begin(),now.end(),BAD);
  for(int last=3;last<=29;last++)for(int s=0;s<=target;s++)if(old[ix(last,s)]!=BAD)
   for(int q=3;q<=last;q++){
    int ns=s+q,r=35-n;if(ns>target||ns>cap[n]||ns+3*r>target||ns+q*r<target)continue;transitions++;
    int v=old[ix(last,s)]+f(34-q),id=ix(q,ns);if(v>now[id]){now[id]=v;par[n][id]=last;}
   }
  old.swap(now);
 }
 int best=BAD,last=-1;for(int q=3;q<=29;q++)if(old[ix(q,target)]>best){best=old[ix(q,target)];last=q;}
 vector<int> seq(35);if(best!=BAD){int s=target;for(int n=35;n>=1;n--){seq[n-1]=last;int prev=par[n][ix(last,s)];assert(prev>=0);s-=last;last=prev;}assert(s==0);}
 double cpu1=double(clock()-c0)/CLOCKS_PER_SEC;
 // Independent frequency recurrence: assign multiplicity of q from 29 down to 3.
 unordered_map<int,int>memo;long long ftrans=0;clock_t c1=clock();
 function<int(int,int,int)> rec=[&](int q,int n,int sum)->int{
  if(n==35)return sum==target?0:BAD;
  if(q<3||sum+3*(35-n)>target||sum+q*(35-n)<target)return BAD;
  int key=(q*36+n)*sz+sum;auto it=memo.find(key);if(it!=memo.end())return it->second;
  int ans=BAD,maxc=min(35-n,(target-sum)/q);
  for(int count=0;count<=maxc;count++){
   bool ok=true;for(int j=1;j<=count;j++)if(sum+j*q>cap[n+j]){ok=false;break;}if(!ok)continue;
   ftrans++;int tail=rec(q-1,n+count,sum+count*q);if(tail!=BAD)ans=max(ans,count*f(34-q)+tail);
  }
  return memo[key]=ans;
 };
 int check=rec(29,0,0);assert(check==best);
 if(best!=BAD){int sum=0,v=0;for(int i=0;i<35;i++){assert(seq[i]>=3&&seq[i]<=29);if(i)assert(seq[i]<=seq[i-1]);sum+=seq[i];v+=f(34-seq[i]);assert(sum<=cap[i+1]);}assert(sum==target&&v==best);}
 cout<<"{\"W\":"<<W<<",\"S5\":"<<S5<<",\"E\":"<<E<<",\"t\":"<<t<<",\"maxP\":"<<best<<",\"frequency_maxP\":"<<check<<",\"position_transitions\":"<<transitions<<",\"frequency_states\":"<<memo.size()<<",\"frequency_transitions\":"<<ftrans<<",\"position_cpu_seconds\":"<<cpu1<<",\"frequency_cpu_seconds\":"<<double(clock()-c1)/CLOCKS_PER_SEC<<",\"caps\":[";
 for(int k=1;k<=13;k++){if(k>1)cout<<",";cout<<cap[k];}cout<<"],\"maximizer_q\":[";for(int i=0;i<35;i++){if(i)cout<<",";cout<<seq[i];}cout<<"]}\n";
}

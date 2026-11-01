#include <algorithm>
#include <cassert>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
const int NEG=-100000000, E=76,R=21,N=35;
int f(int s){int a=s/5,b=s%5;return (s*s-((5-b)*a*a+b*(a+1)*(a+1)))/2;}
int g(int q){assert(q>=0&&q<=34);return f(34-q);}
int rho(int s){int p=1,l=0;while(p<s){p*=2;l++;}return 1+l;}
int memo[36][77][36];
int U(int s,int m,int r){if(m<0||m>s*(s-1)/2)return NEG;if(!s)return m==0?0:NEG;int &v=memo[s][m][r];if(v!=-1)return v;v=max(g(r)+U(s-1,m,r),g(s-1+r)+U(s-1,m-s+1,r+1));return v;}
int dp[36][22][77],ps[36][22][77],pm[36][22][77];
int main(int argc,char**argv){clock_t st=clock();fill(&memo[0][0][0],&memo[0][0][0]+36*77*36,-1);fill(&dp[0][0][0],&dp[0][0][0]+36*22*77,NEG);dp[0][0][0]=0;
for(int n=2;n<=35;n++)for(int r=2;r<=21;r++)for(int e=1;e<=76;e++)for(int s=2;s<=n;s++){int c=rho(s);if(c>r)continue;for(int m=s-1;m<=min(e,s*(s-1)/2);m++){int old=dp[n-s][r-c][e-m];if(old<0)continue;int v=old+U(s,m,0);if(v>dp[n][r][e]){dp[n][r][e]=v;ps[n][r][e]=s;pm[n][r][e]=m;}}}
int best=NEG,bi=-1,br=-1;for(int i=0;i<=3;i++)for(int r=0;r<=21-i;r++){int v=i*g(0)+dp[35-i][r][76];if(v>best){best=v;bi=i;br=r;}}
cout<<"{\n\"n1\":519,\"e_nonunit\":76,\"P_component_majorant\":"<<best<<",\"isolates\":"<<bi<<",\"rho_nontrivial\":"<<br<<",\"components\":[";
int n=35-bi,r=br,e=76;bool first=true;while(n){int s=ps[n][r][e],m=pm[n][r][e];assert(s>=2);if(!first)cout<<",";first=false;cout<<"{\"s\":"<<s<<",\"m\":"<<m<<",\"rho\":"<<rho(s)<<",\"U\":"<<U(s,m,0)<<"}";n-=s;r-=rho(s);e-=m;}assert(!r&&!e);cout<<"],\"cpu_seconds\":"<<double(clock()-st)/CLOCKS_PER_SEC<<"}\n";
}

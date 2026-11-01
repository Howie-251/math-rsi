#include <array>
#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 // order u1..u5,p,B1..B4,v1..v10.
 vector<vector<int>> L={{0,1,2,6},{3,4,7,10},{5,8,11,12},{6,7,13,14},{8,9,15,16},{9,17,18,19}};
 vector<int> lm;for(auto q:L){int m=0;for(int v:q)m|=1<<v;lm.push_back(m);}
 vector<int> masks,idx(1<<20,-1),w;for(int a=0;a<16;a++)for(int b=a+1;b<17;b++)for(int c=b+1;c<18;c++)for(int d=c+1;d<19;d++)for(int e=d+1;e<20;e++){int m=(1<<a)|(1<<b)|(1<<c)|(1<<d)|(1<<e);idx[m]=masks.size();masks.push_back(m);}
 w.resize(masks.size());int nc=0,n11=0,minsafe=100,maxpred=0;vector<int>pred(1<<20);
 const int full=(1<<20)-1;
 for(int red=0;red<=full;red++)if(popcount((unsigned)red)==10){int A=0,B=0,ri=-1,bi=-1;for(int i=0;i<6;i++){int z=red&lm[i];if(z==lm[i])A++,ri=i;if(!z)B++,bi=i;}
 if(A==1&&B==1){n11++;int sr=0,sb=0;for(int a:L[ri]){bool safe=true;for(int l:lm)if((l&(1<<a))&&popcount((unsigned)(l&red))==1)safe=false;if(safe)sr|=1<<a;}
 for(int b:L[bi]){bool safe=true;for(int l:lm)if((l&(1<<b))&&popcount((unsigned)(l&~red))==1)safe=false;if(safe)sb|=1<<b;}
 assert(popcount((unsigned)sr)>=2&&popcount((unsigned)sb)>=2);minsafe=min(minsafe,popcount((unsigned)sr)*popcount((unsigned)sb));
 for(int a=0;a<20;a++)if(sr>>a&1)for(int b=0;b<20;b++)if(sb>>b&1){int t=red^(1<<a)^(1<<b);for(int l:lm)assert((t&l)!=0&&(t&l)!=l);maxpred=max(maxpred,++pred[t]);}}
 if(A&&B)continue;nc++;array<int,10>r,b;int nr=0,nb=0;for(int i=0;i<20;i++)if(red>>i&1)r[nr++]=i;else b[nb++]=i;
 for(auto q:{r,b})for(int a=0;a<6;a++)for(int bb=a+1;bb<7;bb++)for(int c=bb+1;c<8;c++)for(int d=c+1;d<9;d++)for(int e=d+1;e<10;e++)w[idx[(1<<q[a])|(1<<q[bb])|(1<<q[c])|(1<<q[d])|(1<<q[e])]]++;
 }
 assert(nc==167174&&n11==15366&&maxpred<=9);ofstream out("WEIGHTS.tsv");for(int i=0;i<(int)masks.size();i++)out<<masks[i]<<'\t'<<w[i]<<'\n';
 cout<<"{\"C_count\":"<<nc<<",\"star_AB11_count\":"<<n11<<",\"min_safe_swaps\":"<<minsafe<<",\"max_star_clearing_target_predecessors\":"<<maxpred<<",\"five_sets\":"<<masks.size()<<",\"min_weight\":"<<*min_element(w.begin(),w.end())<<",\"max_weight\":"<<*max_element(w.begin(),w.end())<<"}\n";
}

#include <bits/stdc++.h>
using namespace std;
int main(){
  clock_t start=clock();
  auto color=[](int a,int b){int dx=(b%5-a%5+5)%5,dy=(b/5-a/5+5)%5;
    if(!dx)return 0;if(!dy)return 1;if(dx==dy)return 2;return -1;};
  vector<array<int,3>> tri;
  vector<vector<uint32_t>> pairs(25);
  for(int a=0;a<25;a++)for(int b=a+1;b<25;b++)for(int c=b+1;c<25;c++){
    int x=color(a,b),y=color(a,c),z=color(b,c);
    if(x>=0&&y>=0&&z>=0&&x!=y&&x!=z&&y!=z){tri.push_back({a,b,c});pairs[a].push_back((1u<<b)|(1u<<c));}
  }
  vector<uint8_t> ok(1u<<25);ok[0]=1;
  array<unsigned long long,26> hist{};hist[0]=1;
  int best=0;uint32_t witness=0;
  for(uint32_t s=1;s<(1u<<25);s++){
    int v=__builtin_ctz(s);uint32_t rest=s&(s-1);if(!ok[rest])continue;
    bool good=true;for(uint32_t p:pairs[v])if((rest&p)==p){good=false;break;}
    if(good){ok[s]=1;int k=__builtin_popcount(s);hist[k]++;if(k>best){best=k;witness=s;}}
  }
  vector<uint32_t> non(25);for(int a=0;a<25;a++)for(int b=0;b<25;b++)if(a!=b&&color(a,b)<0)non[a]|=1u<<b;
  int singlemax=0,pairmax=0;for(int a=0;a<25;a++){singlemax=max(singlemax,__builtin_popcount(non[a]));for(int b=a+1;b<25;b++)pairmax=max(pairmax,__builtin_popcount(non[a]&non[b]));}
  cout<<"{\"complete\":true,\"subsets_checked\":33554432,\"noncollinear_triangles\":"<<tri.size()<<",\"largest_triangle_free_subset\":"<<best<<",\"witness\":[";
  bool first=true;for(int i=0;i<25;i++)if(witness>>i&1){if(!first)cout<<",";cout<<i;first=false;}
  cout<<"],\"triangle_free_histogram\":[";for(int i=0;i<=25;i++){if(i)cout<<",";cout<<hist[i];}
  cout<<"],\"nonneighbor_single_max\":"<<singlemax<<",\"common_nonneighbor_pair_max\":"<<pairmax<<",\"CPU_seconds\":"<<setprecision(12)<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}

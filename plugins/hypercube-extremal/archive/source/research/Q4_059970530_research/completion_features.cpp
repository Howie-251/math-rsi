#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int pc(unsigned x){return __builtin_popcount(x);}
template<class T> vector<T> read(const char* p){ifstream f(p,ios::binary|ios::ate);size_t n=f.tellg();f.seekg(0);vector<T> a(n/sizeof(T));f.read((char*)a.data(),n);return a;}
template<class T> void write(const char*p,const vector<T>&a){ofstream f(p,ios::binary);f.write((char*)a.data(),a.size()*sizeof(T));}
int main(){
 auto keys=read<int32_t>("keys.bin"), ed=read<int32_t>("edges.bin"), sq=read<int32_t>("squares.bin");
 int fstat[4096][3]={};
 for(int m=0;m<4096;m++)for(int q:sq){
  int z=m&q,n=pc(z);
  if(!n)fstat[m][0]++;
  if(n==1)fstat[m][2]++;
  if(n==2){int vertices=0;for(int e=0;e<12;e++)if((z>>e)&1)vertices|=(1<<ed[2*e])|(1<<ed[2*e+1]);if(pc(vertices)==4)fstat[m][1]++;}
 }
 int inside[256]={};int pattern[256][12];
 for(int s=0;s<256;s++)for(int e=0;e<12;e++){
  int x=ed[2*e],y=ed[2*e+1];int a=(s>>x)&1,b=(s>>y)&1;
  pattern[s][e]=a+b;if(a&&b)inside[s]|=1<<e;
 }
 vector<int64_t> ptr{0}; vector<int16_t> counts;vector<array<int8_t,4>> all;
 for(int key:keys){int a=key/4096,b=key%4096,inter=a&b,nb=0;vector<array<int8_t,4>> v;
  int vis[3];for(int j=0;j<3;j++)vis[j]=fstat[a][j]+fstat[b][j];
  for(int s=0;s<256;s++)if(!(inside[s]&inter)){
   nb++;int mixed[3]={};
   for(int e=0;e<12;e++){
    int aa=(a>>e)&1,bb=(b>>e)&1,c=pattern[s][e],n=aa+bb+c;
    if(!n)mixed[0]++;
    if(n==1)mixed[2]++;
    if(n==2&&((aa&&bb)||c==2))mixed[1]++;
   }
   v.push_back({int8_t(3*pc(s)-pc(a)-pc(b)),int8_t(mixed[0]-vis[0]),int8_t(mixed[1]-vis[1]),int8_t(mixed[2]-vis[2])});
  }
  sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());all.insert(all.end(),v.begin(),v.end());ptr.push_back(all.size());counts.push_back(nb);
 }
 write("feature_ptr.bin",ptr);write("features.bin",all);write("completion_counts.bin",counts);
 cerr<<"partial types "<<keys.size()<<" unique feature pairs "<<all.size()<<"\n";
}

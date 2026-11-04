#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
template<class T> vector<T> read(const char* p){ifstream f(p,ios::binary|ios::ate);size_t n=f.tellg();f.seekg(0);vector<T> a(n/sizeof(T));f.read((char*)a.data(),n);return a;}
template<class T> void write(const char*p,const vector<T>&a){ofstream f(p,ios::binary);f.write((char*)a.data(),a.size()*sizeof(T));}
int main(){auto keys=read<int32_t>("keys.bin"),edges=read<int32_t>("edges.bin"),idx=read<int32_t>("pair_index.bin");int ei[8][8];fill(&ei[0][0],&ei[0][0]+64,-1);for(int e=0;e<12;e++)ei[edges[2*e]][edges[2*e+1]]=ei[edges[2*e+1]][edges[2*e]]=e;
 static int ma[3][2][4096]={},mb[3][2][4096]={},ms[3][2][256]={};int inside[256]={};
 for(int s=0;s<256;s++)for(int e=0;e<12;e++)if((s>>edges[2*e]&1)&&(s>>edges[2*e+1]&1))inside[s]|=1<<e;
 for(int i=0;i<3;i++){vector<int> rem;for(int j=0;j<3;j++)if(j!=i)rem.push_back(j);rem.push_back(3);
  for(int h=0;h<2;h++){int vm[8];for(int x=0;x<8;x++){vm[x]=h<<i;for(int j=0;j<3;j++)if(x>>j&1)vm[x]|=1<<rem[j];}
   for(int e=0;e<12;e++){int x=vm[edges[2*e]],y=vm[edges[2*e+1]];
    if((x^y)==8){for(int s=0;s<256;s++)if(s>>(x&7)&1)ms[i][h][s]|=1<<e;}
    else {int q=ei[x&7][y&7];for(int m=0;m<4096;m++)if(m>>q&1){if(x&8)mb[i][h][m]|=1<<e;else ma[i][h][m]|=1<<e;}}
   }
  }
 }
 vector<array<int32_t,4>> rows;rows.reserve(5000000);long long count=0;
 for(int h=0;h<(int)keys.size();h++){int a=keys[h]/4096,b=keys[h]%4096;
  for(int s=0;s<256;s++)if(!(inside[s]&(a&b))){count++;array<int32_t,4> r={h,0,0,0};bool minimal=true;
   for(int i=0;i<3;i++){int q0=ma[i][0][a]|mb[i][0][b]|ms[i][0][s],q1=ma[i][1][a]|mb[i][1][b]|ms[i][1][s];int id=idx[4096*q0+q1];if(id<0){cerr<<"invalid";return 2;}r[i+1]=id;if(id<h){minimal=false;break;}}
   if(minimal){sort(r.begin(),r.end());rows.push_back(r);}
  }
 }
 cerr<<"all valid marked completions "<<count<<" min-shadow rows "<<rows.size()<<"\n";
 sort(rows.begin(),rows.end());rows.erase(unique(rows.begin(),rows.end()),rows.end());
 write("joint_shadows.bin",rows);cerr<<"unique joint shadow types "<<rows.size()<<"\n";
}

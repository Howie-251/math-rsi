#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
template<class T> vector<T> read(const char* p){ifstream f(p,ios::binary|ios::ate);size_t n=f.tellg();f.seekg(0);vector<T> a(n/sizeof(T));f.read((char*)a.data(),n);return a;}
template<class T> void write(const char*p,const vector<T>&a){ofstream f(p,ios::binary);f.write((char*)a.data(),a.size()*sizeof(T));}
int tri(int i,int j,int n){if(i>j)swap(i,j);return i*n-i*(i-1)/2+j-i;}
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
 
 auto pairlookup=read<int32_t>("face_pair_lookup.bin"),vc=read<int32_t>("vertex_flag_codes.bin");
 int e4[16][16];fill(&e4[0][0],&e4[0][0]+256,-1);
 for(int e=0;e<12;e++){int x=edges[2*e],y=edges[2*e+1];e4[x][y]=e4[y][x]=e;e4[x+8][y+8]=e4[y+8][x+8]=e+12;}
 for(int x=0;x<8;x++)e4[x][x+8]=e4[x+8][x]=24+x;
 struct Face{uint32_t mask;int root[4];int path[2][8];};vector<Face> fs;
 int qe[4][2]={{0,1},{0,2},{1,3},{2,3}};
 for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)for(int x=0;x<16;x++)if(!(x&((1<<i)|(1<<j)))){
  Face f;f.mask=0;int vm[4]={x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)};
  for(int a=0;a<4;a++){f.root[a]=e4[vm[qe[a][0]]][vm[qe[a][1]]];f.mask|=1u<<f.root[a];}
  int l=0;for(int k=0;k<4;k++)if(k!=i&&k!=j){
   for(int a=0;a<4;a++)f.path[l][a]=e4[vm[a]][vm[a]^(1<<k)];
   for(int a=0;a<4;a++)f.path[l][a+4]=e4[vm[qe[a][0]]^(1<<k)][vm[qe[a][1]]^(1<<k)];l++;
  }fs.push_back(f);
 }
 int vp[16][6][4];int dp[6][2];int l=0;
 for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){dp[l][0]=i;dp[l][1]=j;
  for(int x=0;x<16;x++){int vm[4]={x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)};
   for(int a=0;a<4;a++)vp[x][l][a]=e4[vm[qe[a][0]]][vm[qe[a][1]]];}l++;
 }
 vector<array<int32_t,4>> rows;rows.reserve(3400000);vector<uint32_t> graphs;vector<uint16_t> face_indices;vector<uint8_t> vertex_indices;long long count=0;

 for(int h=0;h<(int)keys.size();h++){int a=keys[h]/4096,b=keys[h]%4096;
  for(int s=0;s<256;s++)if(!(inside[s]&(a&b))){count++;array<int32_t,4> r={h,0,0,0};bool minimal=true;
   for(int i=0;i<3;i++){int q0=ma[i][0][a]|mb[i][0][b]|ms[i][0][s],q1=ma[i][1][a]|mb[i][1][b]|ms[i][1][s];int id=idx[4096*q0+q1];if(id<0){cerr<<"invalid";return 2;}r[i+1]=id;if(id<h){minimal=false;break;}}
   
   if(minimal){
    sort(r.begin(),r.end());rows.push_back(r);uint32_t g=(uint32_t)a|((uint32_t)b<<12)|((uint32_t)s<<24);graphs.push_back(g);
    for(const Face&f:fs){
     int root=0;for(int j=0;j<4;j++)root|=((g>>f.root[j])&1)<<j;
     int code[2]={};for(int z=0;z<2;z++)for(int j=0;j<8;j++)code[z]|=((g>>f.path[z][j])&1)<<j;
     int ix=pairlookup[(root*256+code[0])*256+code[1]];
     if(ix<0||ix>=65536){cerr<<"bad face pair";return 2;}
     face_indices.push_back(ix);
    }
    for(int x=0;x<16;x++)for(int p=0;p<6;p++)for(int q=p+1;q<6;q++){
     if(dp[p][0]==dp[q][0]||dp[p][0]==dp[q][1]||dp[p][1]==dp[q][0]||dp[p][1]==dp[q][1])continue;
     int c0=0,c1=0;for(int j=0;j<4;j++){c0|=((g>>vp[x][p][j])&1)<<j;c1|=((g>>vp[x][q][j])&1)<<j;}
     int u=vc[c0],v=vc[c1];if(u<0||v<0){cerr<<"bad vertexflag";return 2;}
     vertex_indices.push_back(tri(u,v,9));
    }

   }

  }
 }
 cerr<<"all valid marked completions "<<count<<" min-shadow rows "<<rows.size()<<"\n";
 
 write("shadows.bin",rows);write("graphs.bin",graphs);write("face_indices.bin",face_indices);write("vertex_indices.bin",vertex_indices);
 cerr<<"face columns "<<face_indices.size()<<" vertex columns "<<vertex_indices.size()<<"\n";
}

#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <ctime>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "engine_tables.hpp"
using namespace std;
constexpr int L=6174,B=882,N=7203,D=8;
using Generators=array<int,7>;
static array<array<int,D>,N> adj;
static array<int,N> deg,dist,que;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int gp(int g,int h){return AADD[g%147][KACTION[g/147][h%147]]+147*KPROD[g/147][h/147];}
void edge(int u,int v){assert(u!=v&&deg[u]<D&&deg[v]<D);adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
void build(const Generators&S){
    deg.fill(0);
    for(int g=0;g<L;g++){
        for(int s:S){int h=gp(g,s);if(g<h)edge(g,h);}
        edge(g,L+g%147+147*KCOORD[g/147][1]);
    }
    for(int z=0;z<B;z++)edge(L+z,L+B+z%147);
    for(int uv=0;uv<49;uv++)for(int w=0;w<3;w++)edge(L+B+uv+49*w,L+B+uv+49*((w+1)%3));
    for(int g=0;g<N;g++){assert(deg[g]==D);auto row=adj[g];sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());}
}
struct Score{array<int,3> miss{};array<array<int,3>,3> layer{};array<int,3> ecc{};long long bad=0;};
static bool CHECK_BB=false;
static array<array<uint64_t,3>,6> CHECK_MASKS{};
Score score(bool full){
    Score z;array<int,3> roots{0,L,L+B};
    for(int t=0;t<3;t++){
        dist.fill(-1);int front=0,end=1;que[0]=roots[t];dist[roots[t]]=0;
        while(front<end){int v=que[front++];if(!full&&dist[v]==5)continue;for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;que[end++]=w;}}
        for(int v=0;v<N;v++){
            if(dist[v]<0||dist[v]>5){z.miss[t]++;z.layer[t][v<L?0:v<L+B?1:2]++;}
            if(dist[v]>=0)z.ecc[t]=max(z.ecc[t],dist[v]);
        }
        if(full&&end!=N)z.ecc[t]=-1;
        if(CHECK_BB&&t==1)for(int j=0;j<6;j++)for(int x=0;x<147;x++){
            bool want=(CHECK_MASKS[j][x/64]>>(x%64))&1;
            assert(want==(dist[L+x+147*j]>=0&&dist[L+x+147*j]<=5));
        }
    }
    assert(z.layer[2][2]==0);
    z.bad=(6174LL*z.miss[0]+882LL*z.miss[1]+147LL*z.miss[2])/2;return z;
}
template<class T>void list(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
int branch_at(int cursor){return cursor<600?cursor/300:2+(cursor-600)/200;}
void output(ostream&o,const Generators&S,const Score&z,int cursor){
    o<<"{\"cursor\":"<<cursor<<",\"branch\":"<<branch_at(cursor)<<",\"S\":";list(o,S);o<<",\"root_missing\":";list(o,z.miss);
    o<<",\"root_missing_by_target_layer\":[";for(int t=0;t<3;t++){if(t)o<<',';list(o,z.layer[t]);}
    o<<"],\"bad_unordered_pairs\":"<<z.bad<<'}';
}
void save(const string&prefix,const Generators&S,const Score&z,int cursor){
    ofstream p(prefix+".json");output(p,S,z,cursor);p<<'\n';
    ofstream f(prefix+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int h:adj[g])if(g<h)f<<g<<' '<<h<<'\n';
}
void cache(const string&path,Score&z,bool write){
    if(write){ofstream f(path);for(int x:z.miss)f<<x<<' ';for(auto row:z.layer)for(int x:row)f<<x<<' ';for(int x:z.ecc)f<<x<<' ';f<<z.bad<<'\n';}
    else{ifstream f(path);for(int&x:z.miss)f>>x;for(auto&row:z.layer)for(int&x:row)f>>x;for(int&x:z.ecc)f>>x;f>>z.bad;assert(f);}
}

#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <ctime>
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
int main(int argc,char**argv){
    assert(argc==4);string mode=argv[1],base=argv[3];double limit=stod(argv[2]),start=cpu();
    ifstream in(base+"/profile.inputs.txt");int count;in>>count;assert(count==1200);vector<Generators> inputs(count);for(auto&S:inputs)for(int&x:S)in>>x;assert(in);
    if(mode=="preflight"){
        build(inputs[0]);Score z=score(true);save(base+"/preflight",inputs[0],z,0);cache(base+"/preflight.cache.txt",z,true);
        ofstream t(base+"/preflight.terminal.json");t<<"{\"status\":\""<<(z.bad==0?"D5_CANDIDATE":"SAMPLE_COMPLETE")<<"\",\"cpu_seconds\":"<<cpu()-start<<",\"root_eccentricity\":";list(t,z.ecc);t<<",\"sample\":";output(t,inputs[0],z,0);t<<"}\n";output(cout,inputs[0],z,0);cout<<'\n';return 0;
    }
    assert(mode=="profile");int cursor=0,newBFS=0;long long best=LLONG_MAX;array<int,3> mins{N,N,N},zeros{};int joint=0;
    ofstream rows(base+"/profile.results.jsonl");string status="PROFILE_COMPLETE";double build_seconds=0,bfs_seconds=0;
    for(;cursor<count;cursor++){
        if(cpu()-start>limit){status="CPU_LIMIT";break;}
        const auto&S=inputs[cursor];Score z;
        if(cursor==0)cache(base+"/preflight.cache.txt",z,false);
        else{double t=cpu();build(S);build_seconds+=cpu()-t;t=cpu();z=score(false);bfs_seconds+=cpu()-t;newBFS++;}
        output(rows,S,z,cursor);rows<<'\n';for(int i=0;i<3;i++){mins[i]=min(mins[i],z.miss[i]);if(!z.miss[i])zeros[i]++;}if(!z.miss[1]&&!z.miss[2])joint++;
        if(z.bad<best){best=z.bad;if(cursor==0){filesystem::copy_file(base+"/preflight.edges",base+"/profile.best.edges",filesystem::copy_options::overwrite_existing);ofstream p(base+"/profile.best.json");output(p,S,z,cursor);p<<'\n';}else save(base+"/profile.best",S,z,cursor);}
        if(!z.bad){status="D5_CANDIDATE";cursor++;break;}
    }
    ofstream t(base+"/profile.terminal.json");t<<"{\"status\":\""<<status<<"\",\"next_cursor\":"<<cursor<<",\"raw\":"<<cursor<<",\"legal\":"<<cursor<<",\"HH_pass\":"<<cursor<<",\"three_root_BFS_scored\":"<<cursor<<",\"new_three_root_BFS_this_process\":"<<newBFS<<",\"cached_preflight_used\":true,\"root_minimum_missing\":";list(t,mins);
    t<<",\"root_zero_counts\":";list(t,zeros);t<<",\"head_and_block_zero\":"<<joint<<",\"best_bad_pairs\":"<<best<<",\"cpu_seconds\":"<<cpu()-start<<",\"build_cpu_seconds\":"<<build_seconds<<",\"BFS_cpu_seconds\":"<<bfs_seconds<<",\"full_production_started\":false}\n";
    cout<<status<<" cursor="<<cursor<<" best="<<best<<" CPU="<<cpu()-start<<'\n';
}

#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <cstdint>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "profile_tables.hpp"
using namespace std;
constexpr int L=2688,B=448,N=3200,D=7;
using Generators=array<int,6>;
static array<array<int,D>,N> adj;
static array<int,N> deg,dist,que;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int gp(int g,int h){return ((g%64)^KACTION[g/64][h%64])+64*KPROD[g/64][h/64];}
void edge(int u,int v){assert(u!=v&&deg[u]<D&&deg[v]<D);adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
void build(const Generators&S){
    deg.fill(0);
    for(int g=0;g<L;g++){
        for(int s:S){int h=gp(g,s);if(g<h)edge(g,h);}
        edge(g,L+g%64+64*KCOORD[g/64][0]);
    }
    for(int z=0;z<B;z++)edge(L+z,L+B+z%64);
    for(int g=0;g<N;g++){assert(deg[g]==D);auto row=adj[g];sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());}
}
uint64_t transform(uint64_t mask,int k){uint64_t ans=0;while(mask){int x=__builtin_ctzll(mask);mask&=mask-1;ans|=1ULL<<KACTION[k][x];}return ans;}
array<uint64_t,2> bb_masks(const Generators&S){
    array<uint64_t,64> hm{};
    for(int x=0;x<64;x++)for(int h:HCODE)hm[x]|=1ULL<<KACTION[h][x];
    uint64_t r0=0,r1=0,p=1,q=1;
    auto insert=[&](int g){int x=g%64,t=KCOORD[g/64][0];if(!t)r0|=hm[x];else{int ti=1;while(t*ti%7!=1)ti++;r1|=1ULL<<KACTION[LCODE[ti]][x];}};
    vector<int> frontier{0};insert(0);
    for(int depth=1;depth<=3;depth++){
        vector<int> next;next.reserve(frontier.size()*6);
        for(int w:frontier)for(int s:S){int g=gp(w,s);insert(g);next.push_back(g);}frontier.swap(next);
    }
    for(int s:S){int x=s%64,t=KCOORD[s/64][0];p|=hm[x];q|=hm[KACTION[(7-t)%7][x]];}
    return {r0|p|q,r1|p|transform(q,1)};
}
struct Score{array<int,3> miss{};array<array<int,3>,3> layer{};array<int,3> ecc{};array<uint64_t,2> bb{};long long bad=0;};
Score score(const Generators&S,bool full){
    Score z;z.bb=bb_masks(S);array<int,3> roots{0,L,L+B};
    array<uint64_t,7> bm{};bm[0]=z.bb[0];for(int t=1;t<7;t++)bm[t]=transform(z.bb[1],LCODE[t]);
    for(int t=0;t<3;t++){
        dist.fill(-1);int front=0,end=1;que[0]=roots[t];dist[roots[t]]=0;
        while(front<end){int v=que[front++];if(!full&&dist[v]==5)continue;for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;que[end++]=w;}}
        for(int v=0;v<N;v++){
            if(dist[v]<0||dist[v]>5){z.miss[t]++;z.layer[t][v<L?0:v<L+B?1:2]++;}
            if(dist[v]>=0)z.ecc[t]=max(z.ecc[t],dist[v]);
        }
        if(full&&end!=N)z.ecc[t]=-1;
        if(t==1)for(int b=0;b<B;b++){bool actual=dist[L+b]>=0&&dist[L+b]<=5;bool algebra=bm[b/64]>>(b%64)&1;assert(actual==algebra);}
    }
    z.bad=(2688LL*z.miss[0]+448LL*z.miss[1]+64LL*z.miss[2])/2;return z;
}
template<class T>void list(ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
void output(ostream&o,const Generators&S,const Score&z,int cursor){
    o<<"{\"cursor\":"<<cursor<<",\"branch\":"<<cursor/200<<",\"S\":";list(o,S);o<<",\"root_missing\":";list(o,z.miss);
    o<<",\"root_missing_by_target_layer\":[";for(int t=0;t<3;t++){if(t)o<<',';list(o,z.layer[t]);}
    o<<"],\"BB_masks_M0_M1\":";list(o,z.bb);o<<",\"bad_unordered_pairs\":"<<z.bad<<'}';
}
void save(const string&prefix,const Generators&S,const Score&z,int cursor){
    ofstream p(prefix+".json");output(p,S,z,cursor);p<<'\n';
    ofstream f(prefix+".edges");f<<N<<' '<<N*D/2<<'\n';for(int g=0;g<N;g++)for(int h:adj[g])if(g<h)f<<g<<' '<<h<<'\n';
}
void cache(const string&path,Score&z,bool write){
    if(write){ofstream f(path);for(int x:z.miss)f<<x<<' ';for(auto row:z.layer)for(int x:row)f<<x<<' ';for(int x:z.ecc)f<<x<<' ';for(auto x:z.bb)f<<x<<' ';f<<z.bad<<'\n';}
    else {ifstream f(path);for(int&x:z.miss)f>>x;for(auto&row:z.layer)for(int&x:row)f>>x;for(int&x:z.ecc)f>>x;for(auto&x:z.bb)f>>x;f>>z.bad;assert(f);}
}
int main(int argc,char**argv){
    assert(argc==4);string mode=argv[1],base=argv[3];double limit=stod(argv[2]),start=cpu();
    ifstream in(base+"/profile.inputs.txt");int count;in>>count;assert(count==1200);vector<Generators> inputs(count);for(auto&S:inputs)for(int&x:S)in>>x;assert(in);
    if(mode=="preflight"){
        build(inputs[0]);Score z=score(inputs[0],true);save(base+"/preflight",inputs[0],z,0);cache(base+"/preflight.cache.txt",z,true);
        ofstream t(base+"/preflight.terminal.json");t<<"{\"status\":\""<<(z.bad==0?"D5_CANDIDATE":"SAMPLE_COMPLETE")<<"\",\"cpu_seconds\":"<<cpu()-start<<",\"root_eccentricity\":";list(t,z.ecc);
        t<<",\"all_448_BB_targets_match_two_mask_formula\":true,\"sample\":";output(t,inputs[0],z,0);t<<"}\n";output(cout,inputs[0],z,0);cout<<'\n';return 0;
    }
    assert(mode=="profile");int cursor=0,newBFS=0;long long best=LLONG_MAX;array<int,3> mins{N,N,N},zeros{};int joint=0;
    ofstream rows(base+"/profile.results.jsonl");string status="PROFILE_COMPLETE";double build_seconds=0,bfs_seconds=0;
    for(;cursor<count;cursor++){
        if(cpu()-start>limit){status="CPU_LIMIT";break;}
        const auto&S=inputs[cursor];Score z;
        if(cursor==0)cache(base+"/preflight.cache.txt",z,false);
        else{double t=cpu();build(S);build_seconds+=cpu()-t;t=cpu();z=score(S,false);bfs_seconds+=cpu()-t;newBFS++;}
        output(rows,S,z,cursor);rows<<'\n';for(int i=0;i<3;i++){mins[i]=min(mins[i],z.miss[i]);if(!z.miss[i])zeros[i]++;}if(!z.miss[1]&&!z.miss[2])joint++;
        if(z.bad<best){best=z.bad;if(cursor==0){filesystem::copy_file(base+"/preflight.edges",base+"/profile.best.edges",filesystem::copy_options::overwrite_existing);ofstream p(base+"/profile.best.json");output(p,S,z,cursor);p<<'\n';}else save(base+"/profile.best",S,z,cursor);}
        if(!z.bad){status="D5_CANDIDATE";cursor++;break;}
    }
    ofstream t(base+"/profile.terminal.json");t<<"{\"status\":\""<<status<<"\",\"next_cursor\":"<<cursor<<",\"raw\":"<<cursor<<",\"legal\":"<<cursor<<",\"HH_pass\":"<<cursor<<",\"three_root_BFS_scored\":"<<cursor<<",\"new_three_root_BFS_this_process\":"<<newBFS<<",\"cached_preflight_used\":true,\"root_minimum_missing\":";list(t,mins);
    t<<",\"root_zero_counts\":";list(t,zeros);t<<",\"head_and_block_zero\":"<<joint<<",\"best_bad_pairs\":"<<best<<",\"cpu_seconds\":"<<cpu()-start<<",\"build_cpu_seconds\":"<<build_seconds<<",\"BFS_and_BB_calibration_cpu_seconds\":"<<bfs_seconds<<",\"all_448_BB_targets_match_each_time\":true,\"full_production_started\":false}\n";
    cout<<status<<" cursor="<<cursor<<" best="<<best<<" CPU="<<cpu()-start<<'\n';
}

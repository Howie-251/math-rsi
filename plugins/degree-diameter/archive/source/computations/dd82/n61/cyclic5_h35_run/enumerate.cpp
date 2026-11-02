#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using Perm=std::array<int,7>;
using Graph=std::array<uint64_t,35>;
static const std::array<Perm,2> ds={Perm{0,0,0,1,2,3,4},Perm{0,0,1,1,2,3,4}};
int mod5(int x){return (x%5+5)%5;}
uint32_t signature(const Perm& p,const Perm& d,int step){
    Perm inv{}; for(int r=0;r<7;++r)inv[p[r]]=r;
    uint32_t key=0;
    for(int r=0;r<7;++r){
        int a=mod5(step+d[p[r]]-d[r]),b=mod5(-step+d[inv[r]]-d[r]);
        if(!a||!b||a==b)return UINT32_MAX;
        key|=((1u<<(a-1))|(1u<<(b-1)))<<(4*r);
    }
    return key;
}
Graph graph(const Perm&p,const Perm&q){
    Graph a{};
    auto edge=[&](int x,int y){a[x]|=1ull<<y;a[y]|=1ull<<x;};
    for(int r=0;r<7;++r)for(int i=0;i<5;++i){
        edge(5*r+i,5*p[r]+(i+1)%5);
        edge(5*r+i,5*q[r]+(i+2)%5);
    }
    return a;
}
struct Score{Perm rho{};int mx=0,total=0;};
Score score(const Graph&a,const Perm&d){
    Score s;
    for(int r=0;r<7;++r){
        int z=5*r;uint64_t reach=a[z],bits=a[z];
        while(bits){int v=__builtin_ctzll(bits);bits&=bits-1;reach|=a[v];}
        reach&=~(1ull<<z);
        int m=std::count(d.begin(),d.end(),d[r]);
        s.rho[r]=16-__builtin_popcountll(reach)+m-1;
        s.mx=std::max(s.mx,s.rho[r]);s.total+=5*s.rho[r];
    }return s;
}
template<class T>void array_json(std::ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<x;}o<<']';}
void candidate_json(std::ostream&o,int type,const Perm&p,const Perm&q,const Score&s){
    o<<"{\"type\":"<<type<<",\"d\":";array_json(o,ds[type]);
    o<<",\"p\":";array_json(o,p);o<<",\"q\":";array_json(o,q);
    o<<",\"rho_orbit\":";array_json(o,s.rho);
    o<<",\"max_rho\":"<<s.mx<<",\"sum_rho\":"<<s.total<<'}';
}
int main(int argc,char**argv){
    const auto start=std::chrono::steady_clock::now(); const auto cpu=std::clock();
    if(argc==2 && std::string(argv[1])=="--sanity"){
        const Perm id={0,1,2,3,4,5,6},shift={1,2,3,4,5,6,0},triple={1,2,0,3,4,5,6};
        std::cout<<"{\"cases\":[";
        for(int c=0;c<3;++c){if(c)std::cout<<',';int t=c==2?1:0;
            auto p=c==1?triple:id,q=c==2?shift:id;auto s=score(graph(p,q),ds[t]);
            std::cout<<"{\"candidate\":";candidate_json(std::cout,t,p,q,s);
            std::cout<<",\"signature_accept\":"<<((signature(p,ds[t],1)!=UINT32_MAX && signature(q,ds[t],2)==(0x0fffffffu^signature(p,ds[t],1)))?"true":"false")<<'}';}
        std::cout<<"]}\n";return 0;
    }
    if(argc!=2){std::cerr<<"usage: enumerate OUTPUT_DIR or --sanity\n";return 2;}
    std::vector<Perm> permutations;Perm id={0,1,2,3,4,5,6};
    do{permutations.push_back(id);}while(std::next_permutation(id.begin(),id.end()));
    struct Stats{uint64_t valid_p=0,valid_q=0,joined=0,row_pass=0;bool complete=false;};
    std::array<Stats,2> stats{};
    bool found=false,limited=false,have_best=false; int bt=0;
    Perm bp{},bq{};Score bs;
    for(int t=0;t<2 && !found && !limited;++t){
        std::map<uint32_t,std::vector<Perm>> qs;
        for(const auto&q:permutations){auto k=signature(q,ds[t],2);if(k!=UINT32_MAX){qs[k].push_back(q);++stats[t].valid_q;}}
        for(const auto&p:permutations){
            auto key=signature(p,ds[t],1);if(key==UINT32_MAX)continue;++stats[t].valid_p;
            auto it=qs.find(0x0fffffffu^key);if(it==qs.end())continue;
            for(const auto&q:it->second){
                auto s=score(graph(p,q),ds[t]);++stats[t].joined;
                if(s.mx<=4)++stats[t].row_pass;
                if(!have_best || std::pair{s.mx,s.total}<std::pair{bs.mx,bs.total}){
                    have_best=true;bt=t;bp=p;bq=q;bs=s;
                }
                if(s.mx<=4 && s.total<=130){found=true;bt=t;bp=p;bq=q;bs=s;break;}
                if((stats[t].joined&1023)==0 &&
                    (double(std::clock()-cpu)/CLOCKS_PER_SEC>=27 ||
                     std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=40)){
                    limited=true;break;
                }
            }if(found||limited)break;
        }
        if(!found&&!limited)stats[t].complete=true;
    }
    std::string dir=argv[1];std::ofstream out(dir+"/result.json");
    out<<"{\"status\":\""<<(found?"FRONTEND_FOUND":limited?"INCOMPLETE_RESOURCE_LIMIT":"EXHAUSTED_NO_FRONTEND")<<"\",\"types\":[";
    for(int t=0;t<2;++t){if(t)out<<',';auto s=stats[t];out<<"{\"type\":"<<t<<",\"valid_p_processed\":"<<s.valid_p<<",\"valid_q\":"<<s.valid_q<<",\"compatible_pairs_checked\":"<<s.joined<<",\"pointwise_pass\":"<<s.row_pass<<",\"complete\":"<<(s.complete?"true":"false")<<'}';}
    out<<"],\"candidate\":";if(have_best)candidate_json(out,bt,bp,bq,bs);else out<<"null";
    out<<",\"cpu_seconds\":"<<double(std::clock()-cpu)/CLOCKS_PER_SEC<<",\"wall_seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"}\n";
    if(have_best){std::ofstream edges(dir+"/candidate.edges");auto a=graph(bp,bq);for(int x=0;x<35;++x)for(int y=x+1;y<35;++y)if(a[x]&(1ull<<y))edges<<x<<' '<<y<<'\n';}
    std::cout<<(found?"FRONTEND_FOUND":limited?"INCOMPLETE_RESOURCE_LIMIT":"EXHAUSTED_NO_FRONTEND")<<'\n';
    return 0;
}

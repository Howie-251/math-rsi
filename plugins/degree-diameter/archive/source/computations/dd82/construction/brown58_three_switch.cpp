// Exhaust or time-limit one six-cycle / three-disjoint-edge switch neighborhood.
// This is a local diagnostic, not nonexistence of arbitrary order-58 graphs.
// Standalone C++17, one thread. All scores count unordered pairs at distance >2.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

using Bits = uint64_t;
using Graph = std::array<Bits,58>;
using Edge = std::pair<int,int>;
using Matching = std::array<Edge,3>;
constexpr Bits ALL = (Bits(1)<<58)-1;
int pc(Bits x) { return __builtin_popcountll(x); }
void toggle(Graph& g,int a,int b) {g[a]^=Bits(1)<<b;g[b]^=Bits(1)<<a;}
Bits missing(const Graph& g,int u) {
    Bits cover=g[u]|(Bits(1)<<u), neighbors=g[u];
    while(neighbors) {int v=__builtin_ctzll(neighbors);neighbors&=neighbors-1;cover|=g[v];}
    return ALL&~cover;
}
int full_score(const Graph& g) {int s=0;for(int u=0;u<58;++u)s+=pc(missing(g,u));return s/2;}
void write_graph(const Graph& g,const std::string& path) {
    std::ofstream f(path);f<<"58 232\n";
    for(int u=0;u<58;++u)for(int v=u+1;v<58;++v)if((g[u]>>v)&1)f<<u<<' '<<v<<'\n';
}
void write_matching(std::ostream& f,const Matching& m) {
    f<<'[';for(int i=0;i<3;++i){if(i)f<<',';f<<'['<<m[i].first<<','<<m[i].second<<']';}f<<']';
}
void write_hist(std::ostream& f,const std::map<int,uint64_t>& h) {
    f<<'{';bool first=true;for(auto [k,v]:h){if(!first)f<<',';first=false;f<<'"'<<k<<"\":"<<v;}f<<'}';
}
int main(int argc,char** argv) {
    if(argc!=4){std::cerr<<"usage: brown58_three_switch brown57.edges seconds output_prefix\n";return 2;}
    std::ifstream input(argv[1]);int n,m;if(!(input>>n>>m)||n!=57||m!=224)return 3;
    Graph g{};std::vector<Edge> edges;
    for(int i=0,u,v;i<m;++i){if(!(input>>u>>v)||u<0||u>=57||v<0||v>=57||u==v||((g[u]>>v)&1))return 4;toggle(g,u,v);}
    for(int u=0;u<57;++u)if(pc(g[u])==7)toggle(g,u,57);
    for(int u=0;u<58;++u){if(pc(g[u])!=8)return 5;for(int v=u+1;v<58;++v)if((g[u]>>v)&1)edges.emplace_back(u,v);}
    assert(edges.size()==232);const Graph original=g;
    const double limit=std::stod(argv[2]);const std::string prefix=argv[3];
    write_graph(original,prefix+".seed.edges");
    Graph old_missing{};int initial=full_score(g);for(int u=0;u<58;++u)old_missing[u]=missing(g,u);
    std::vector<Matching> patterns;Matching work{};
    std::function<void(unsigned,int)> rec=[&](unsigned used,int depth){
        if(depth==3){patterns.push_back(work);return;}
        int a=0;while((used>>a)&1)++a;
        for(int b=a+1;b<6;++b)if(!((used>>b)&1)&&(a/2!=b/2)){
            work[depth]={a,b};rec(used|(1u<<a)|(1u<<b),depth+1);
        }
    };rec(0,0);assert(patterns.size()==8);
    const auto wall_start=std::chrono::steady_clock::now();const auto cpu_start=std::clock();
    uint64_t triples=0,disjoint_triples=0,legal=0,checked=0;bool complete=true;
    int best=10000;Graph best_graph{};Matching best_remove{},best_add{};
    std::map<int,uint64_t> hist,hub_hist,fixed_hub_hist;
    for(int i=0;i<230&&complete;++i)for(int j=i+1;j<231&&complete;++j)for(int k=j+1;k<232;++k){
        ++triples;
        if((triples&4095)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-wall_start).count()>=limit){complete=false;break;}
        const std::array<int,6> v={edges[i].first,edges[i].second,edges[j].first,edges[j].second,edges[k].first,edges[k].second};
        Bits U=0;for(int x:v)U|=Bits(1)<<x;if(pc(U)!=6)continue;
        ++disjoint_triples;
        int old_count=0,old_inside_twice=0;
        for(int u:v){old_count+=pc(old_missing[u]);old_inside_twice+=pc(old_missing[u]&U);}
        old_count-=old_inside_twice/2;
        for(int p=0;p<3;++p)toggle(g,v[2*p],v[2*p+1]);
        for(const auto& pattern:patterns){
            bool valid=true;Matching added;
            for(int p=0;p<3;++p){auto [a,b]=pattern[p];added[p]={v[a],v[b]};if((g[v[a]]>>v[b])&1){valid=false;break;}}
            if(!valid)continue;
            for(auto [a,b]:added)toggle(g,a,b);
            int new_count=0,new_inside_twice=0;
            for(int u:v){Bits miss=missing(g,u);new_count+=pc(miss);new_inside_twice+=pc(miss&U);}
            const int score=initial-old_count+new_count-new_inside_twice/2;
            if((legal&65535)==0){assert(score==full_score(g));++checked;}
            ++legal;++hist[score];if((U>>57)&1)++hub_hist[score];else ++fixed_hub_hist[score];
            if(score<best){best=score;best_graph=g;best_remove={edges[i],edges[j],edges[k]};best_add=added;}
            for(auto [a,b]:added)toggle(g,a,b);
        }
        for(int p=0;p<3;++p)toggle(g,v[2*p],v[2*p+1]);
        assert(g==original);
    }
    const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-wall_start).count();
    const double cpu=double(std::clock()-cpu_start)/CLOCKS_PER_SEC;
    write_graph(best_graph,prefix+".best_neighbor.edges");
    int repaired=0,new_bad=0;
    for(int u=0;u<58;++u){Bits after=missing(best_graph,u);repaired+=pc(old_missing[u]&~after);new_bad+=pc(after&~old_missing[u]);}
    std::ofstream out(prefix+".json");
    out<<"{\n\"scope\":\"One three-disjoint-edge rewiring from the fixed Brown57 plus absolute-point hub seed; removed and added matchings form one six-cycle\",\n"
       <<"\"complete\":"<<(complete?"true":"false")<<",\n\"wall_limit_seconds\":"<<limit
       <<",\n\"elapsed_seconds\":"<<elapsed<<",\n\"cpu_seconds\":"<<cpu
       <<",\n\"threads\":1,\n\"initial_uncovered_pairs\":"<<initial
       <<",\n\"edge_triples_visited\":"<<triples<<",\n\"disjoint_edge_triples\":"<<disjoint_triples
       <<",\n\"matching_patterns_per_disjoint_triple\":8,\n\"legal_moves\":"<<legal
       <<",\n\"incremental_scores_checked_against_full_score\":"<<checked
       <<",\n\"minimum_neighbor_uncovered_pairs\":"<<best<<",\n\"score_histogram\":";write_hist(out,hist);
    out<<",\n\"hub_edge_changed_histogram\":";write_hist(out,hub_hist);
    out<<",\n\"hub_neighbors_fixed_histogram\":";write_hist(out,fixed_hub_hist);
    out<<",\n\"minimum_move_removed\":";write_matching(out,best_remove);
    out<<",\n\"minimum_move_added\":";write_matching(out,best_add);
    out<<",\n\"minimum_move_repairs_old_missing_pairs\":"<<repaired/2
       <<",\n\"minimum_move_creates_missing_pairs\":"<<new_bad/2
       <<",\n\"status\":\"local_neighborhood_diagnostic_not_a_target_graph_or_global_bound\"\n}\n";
    std::cout<<"complete="<<complete<<" legal="<<legal<<" min_neighbor="<<best<<" elapsed="<<elapsed<<" cpu="<<cpu<<'\n';
}

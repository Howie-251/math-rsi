// Full false-twin58 matching cover: one continuous, bounded annealing chain.
// Reuses the graph-bitset/switch pattern of petersen_all_matchings.cpp.
// The root's seven identity blocks are a coordinate gauge, not symmetry.
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <algorithm>

using Graph=std::array<uint64_t,58>;
constexpr uint64_t ALL=(1ULL<<58)-1;
constexpr uint64_t COORDS=63;
constexpr long long PERIOD=250000;
constexpr uint64_t RANDOM_SEED=2026101301ULL;
std::array<std::array<int,2>,21> interfaces;
double cpu_start;
double elapsed(){return double(std::clock())/CLOCKS_PER_SEC-cpu_start;}
uint64_t fibre(int i){return COORDS<<(10+6*i);}
int vertex(int i,int a){return 10+6*i+a;}

Graph read_graph(const std::string& path){
    std::ifstream in(path);int n,m;in>>n>>m;assert(n==58&&m==232);
    Graph g{};
    for(int k=0,u,v;k<m;++k){in>>u>>v;assert(in&&0<=u&&u<v&&v<58);
        assert(!(g[u]>>v&1));g[u]|=1ULL<<v;g[v]|=1ULL<<u;}
    return g;
}
void validate(const Graph& g){
    for(int u=0;u<58;++u){assert(__builtin_popcountll(g[u])==8);assert(!(g[u]>>u&1));
        for(int v=0;v<58;++v)assert((g[u]>>v&1)==(g[v]>>u&1));}
    for(int p=2;p<10;++p){assert(g[p]==((1ULL<<0)|(1ULL<<1)|fibre(p-2)));}
    assert(g[0]==(255ULL<<2)&&g[1]==g[0]);
    for(int i=0;i<8;++i)for(int a=0;a<6;++a){int u=vertex(i,a);
        assert(g[u]>> (2+i)&1);
        for(int j=0;j<8;++j)assert(__builtin_popcountll(g[u]&fibre(j))==(i!=j));
        if(i)assert(g[u]>>vertex(0,a)&1);
    }
}
uint64_t reached(const Graph& g,int u){
    uint64_t result=g[u]|(1ULL<<u),todo=g[u];
    while(todo){int w=__builtin_ctzll(todo);todo&=todo-1;result|=g[w];}
    return result;
}
// Only cross-fibre pairs can fail; counting ordered missing pairs and /2
// is precisely the objective on 28*36=1008 unordered cross-fibre pairs.
int score(const Graph& g){
    int missing=0;
    for(int u=10;u<58;++u)missing+=__builtin_popcountll(ALL&~reached(g,u));
    assert(!(missing%2));return missing/2;
}
int route_score(const Graph& g){
    int q[8][8][6];
    for(int i=0;i<8;++i)for(int j=0;j<8;++j)if(i!=j)
        for(int a=0;a<6;++a)q[i][j][a]=__builtin_ctzll(g[vertex(i,a)]&fibre(j))-(10+6*j);
    int missing=0;
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)for(int a=0;a<6;++a){
        unsigned mask=1u<<q[i][j][a];
        for(int k=0;k<8;++k)if(k!=i&&k!=j)mask|=1u<<q[k][j][q[i][k][a]];
        missing+=6-__builtin_popcount(mask);
    }
    return missing;
}
void change(Graph& g,int e,int a,int b){
    int i=interfaces[e][0],j=interfaces[e][1],u=vertex(i,a),v=vertex(i,b);
    assert(i>=1&&i<j&&a!=b);
    int x=__builtin_ctzll(g[u]&fibre(j)),y=__builtin_ctzll(g[v]&fibre(j));
    assert(x!=y&&!(g[u]>>y&1)&&!(g[v]>>x&1));
    g[u]^=(1ULL<<x)|(1ULL<<y);g[v]^=(1ULL<<x)|(1ULL<<y);
    g[x]^=(1ULL<<u)|(1ULL<<v);g[y]^=(1ULL<<u)|(1ULL<<v);
}
void save(const std::string& prefix,const Graph& g,int bad,long long iteration,
          long long accepted,long long uphill,double temperature){
    validate(g);assert(score(g)==bad&&route_score(g)==bad);
    std::ofstream out(prefix+".json"),edges(prefix+".edges");
    out<<std::setprecision(12)<<"{\"n\":58,\"bad_pairs\":"<<bad
       <<",\"iteration\":"<<iteration<<",\"accepted\":"<<accepted
       <<",\"accepted_uphill\":"<<uphill<<",\"random_seed\":"<<RANDOM_SEED
       <<",\"cpu_seconds_at_save\":"<<elapsed()<<",\"temperature\":"<<temperature
       <<",\"edges\":[";edges<<"58 232\n";
    bool first=true;int count=0;
    for(int u=0;u<58;++u)for(int v=u+1;v<58;++v)if(g[u]>>v&1){
        if(!first)out<<',';first=false;out<<'['<<u<<','<<v<<']';edges<<u<<' '<<v<<'\n';++count;}
    assert(count==232);out<<"],\"interfaces\":[";first=true;
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j){
        if(!first)out<<',';first=false;out<<"{\"i\":"<<i<<",\"j\":"<<j<<",\"permutation\":[";
        for(int a=0;a<6;++a){if(a)out<<',';out<<__builtin_ctzll(g[vertex(i,a)]&fibre(j))-(10+6*j);}
        out<<"]}";}
    out<<"]}\n";
}
int main(int argc,char**argv){
    assert(argc==4||argc==5);cpu_start=double(std::clock())/CLOCKS_PER_SEC;
    int e=0;for(int i=1;i<8;++i)for(int j=i+1;j<8;++j)interfaces[e++]={i,j};assert(e==21);
    std::string action=argv[1];Graph initial=read_graph(argv[2]);validate(initial);
    int initial_score=score(initial);assert(initial_score==105&&route_score(initial)==105);
    if(action=="selfcheck"){
        assert(argc==4);int checked=0;
        for(int block=0;block<21;++block)for(int a=0;a<6;++a)for(int b=a+1;b<6;++b){
            Graph next=initial;change(next,block,a,b);validate(next);
            assert(score(next)==route_score(next));change(next,block,a,b);assert(next==initial);++checked;
        }
        std::ofstream out(argv[3]);out<<std::setprecision(12)
          <<"{\"status\":\"SELF_CHECK_ONLY\",\"initial_bad_pairs\":105,\"switches_checked\":"<<checked
          <<",\"all_reversible\":true,\"all_degree_and_gauge_preserving\":true,\"graph_and_route_scores_agree\":true,"
          <<"\"optimization_runs\":0,\"cpu_seconds\":"<<elapsed()<<"}\n";
        std::cout<<"selfcheck "<<checked<<" score-equivalent reversible switches\n";return 0;
    }
    assert(action=="search"&&argc==5);double budget=std::stod(argv[3]);assert(budget>0&&budget<=120);
    std::string dir=argv[4];std::mt19937_64 rng(RANDOM_SEED);
    Graph current=initial,best_graph=initial;int energy=initial_score,best=energy;
    long long iteration=0,accepted=0,uphill=0;double temperature=2.5;
    save(dir+"/candidate.initial",initial,energy,0,0,0,temperature);
    save(dir+"/candidate.best",best_graph,best,0,0,0,temperature);
    std::ofstream trace(dir+"/improvements.jsonl");
    std::cout<<"initial "<<initial_score<<std::endl;
    while(best>0&&elapsed()<budget){
        int block=rng()%21,a=rng()%6,b=rng()%5;if(b>=a)++b;
        Graph proposal=current;change(proposal,block,a,b);int next=score(proposal);
        temperature=2.5*std::pow(0.15/2.5,double(iteration%PERIOD)/PERIOD);
        // One continuous chain. Reheating changes only temperature; neither
        // graph nor RNG is reset at period boundaries.
        double uniform=double(rng()>>11)*0x1.0p-53;
        if(next<=energy||uniform<std::exp(double(energy-next)/temperature)){
            if(next>energy)++uphill;current=proposal;energy=next;++accepted;
        }
        ++iteration;
        if(energy<best){
            best=energy;best_graph=current;
            save(dir+"/candidate.best",best_graph,best,iteration,accepted,uphill,temperature);
            save(dir+"/best_"+std::to_string(best),best_graph,best,iteration,accepted,uphill,temperature);
            trace<<std::setprecision(12)<<"{\"iteration\":"<<iteration<<",\"bad_pairs\":"<<best
                 <<",\"cpu_seconds\":"<<elapsed()<<",\"changed_interface\":["<<interfaces[block][0]<<','<<interfaces[block][1]
                 <<"],\"swapped_source_coordinates\":["<<a<<','<<b<<"],\"temperature\":"<<temperature<<"}\n";trace.flush();
            std::cout<<"best "<<best<<" iteration "<<iteration<<" cpu "<<elapsed()<<std::endl;
        }
    }
    save(dir+"/candidate.current",current,energy,iteration,accepted,uphill,temperature);
    std::ofstream state(dir+"/rng.final.txt");state<<rng<<'\n';
    std::ofstream out(dir+"/search.json");out<<std::setprecision(12)
      <<"{\"status\":\""<<(best==0?"TARGET_CANDIDATE_PENDING_BFS":"BOUNDED_HEURISTIC_COMPLETED")
      <<"\",\"stop_reason\":\""<<(best==0?"score_zero":"cpu_budget")
      <<"\",\"initial_bad_pairs\":"<<initial_score<<",\"best_bad_pairs\":"<<best<<",\"current_bad_pairs\":"<<energy
      <<",\"proposals\":"<<iteration<<",\"accepted\":"<<accepted<<",\"accepted_uphill\":"<<uphill
      <<",\"random_seed\":"<<RANDOM_SEED<<",\"temperature_period_proposals\":"<<PERIOD
      <<",\"temperature_high\":2.5,\"temperature_low\":0.15,\"cpu_seconds\":"<<elapsed()
      <<",\"cpu_budget_seconds\":"<<budget<<",\"threads\":1,\"chain_restarts\":0,\"complete_enumeration\":false}\n";
    std::cout<<"finished best "<<best<<" cpu "<<elapsed()<<" proposals "<<iteration<<std::endl;
}

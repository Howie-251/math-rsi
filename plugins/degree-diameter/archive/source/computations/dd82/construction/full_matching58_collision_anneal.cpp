// One continuous collision-energy search on all 21 free S6 interfaces.
// No HS-core edges are frozen. Root identities are only the existing gauge.
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
#include <algorithm>
using Graph=std::array<uint64_t,58>;
constexpr uint64_t ALL=(1ULL<<58)-1;
constexpr long long PERIOD=250000;
constexpr uint64_t RANDOM_SEED=2026101302ULL;
std::array<std::array<int,2>,21> interfaces;
double cpu_start;
double elapsed(){return double(std::clock())/CLOCKS_PER_SEC-cpu_start;}
uint64_t fibre(int i){return 63ULL<<(10+6*i);}
int vertex(int i,int a){return 10+6*i+a;}
Graph read_graph(const std::string& path){
    std::ifstream in(path);int n,m;in>>n>>m;assert(n==58&&m==232);Graph g{};
    for(int z=0,u,v;z<m;++z){in>>u>>v;assert(in&&0<=u&&u<v&&v<58);
        assert(!(g[u]>>v&1));g[u]|=1ULL<<v;g[v]|=1ULL<<u;}
    return g;
}
void validate(const Graph& g){
    for(int u=0;u<58;++u){assert(__builtin_popcountll(g[u])==8);assert(!(g[u]>>u&1));
        for(int v=0;v<58;++v)assert((g[u]>>v&1)==(g[v]>>u&1));}
    for(int p=2;p<10;++p)assert(g[p]==((1ULL<<0)|(1ULL<<1)|fibre(p-2)));
    assert(g[0]==(255ULL<<2)&&g[1]==g[0]);
    for(int i=0;i<8;++i)for(int a=0;a<6;++a){int u=vertex(i,a);assert(g[u]>>(2+i)&1);
        for(int j=0;j<8;++j)assert(__builtin_popcountll(g[u]&fibre(j))==(i!=j));
        if(i)assert(g[u]>>vertex(0,a)&1);}
}
uint64_t reached(const Graph& g,int u){
    uint64_t r=g[u]|(1ULL<<u),todo=g[u];
    while(todo){int w=__builtin_ctzll(todo);todo&=todo-1;r|=g[w];}return r;
}
int bad_count(const Graph& g){
    int n=0;for(int u=10;u<58;++u)n+=__builtin_popcountll(ALL&~reached(g,u));
    assert(!(n%2));return n/2;
}
int energy(const Graph& g){
    // K(u,v)=direct edge + actual number of common neighbours for cross pairs.
    int F=-168;
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)
        for(int u=vertex(i,0);u<vertex(i,6);++u)for(int v=vertex(j,0);v<vertex(j,6);++v){
            int K=__builtin_popcountll(g[u]&g[v])+int(g[u]>>v&1);
            F+=K*(K-1)/2;
        }
    assert(F>=0);return F;
}
struct RouteStats{int F=0,alternative_F=0,bad=0;std::array<int,21> row_F{};std::array<int,8> max_K{};};
RouteStats route_stats(const Graph& g){
    int q[8][8][6];
    for(int i=0;i<8;++i)for(int j=0;j<8;++j)if(i!=j)
        for(int a=0;a<6;++a)q[i][j][a]=__builtin_ctzll(g[vertex(i,a)]&fibre(j))-(10+6*j);
    RouteStats result;
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)for(int a=0;a<6;++a){
        std::array<int,6> row{};row[q[i][j][a]]++;
        for(int k=0;k<8;++k)if(k!=i&&k!=j)row[q[k][j][q[i][k][a]]]++;
        int f=-1,alt=0,total=0,mx=0;
        for(int K:row){f+=K*(K-1)/2;alt+=(K-1)*(K-2)/2;total+=K;mx=std::max(mx,K);result.bad+=K==0;}
        assert(total==7&&f>=0&&f==alt);result.F+=f;result.alternative_F+=alt;
        result.row_F[f]++;result.max_K[mx]++;
    }
    return result;
}
void change(Graph& g,int e,int a,int b){
    int i=interfaces[e][0],j=interfaces[e][1],u=vertex(i,a),v=vertex(i,b);assert(i>=1&&i<j&&a!=b);
    int x=__builtin_ctzll(g[u]&fibre(j)),y=__builtin_ctzll(g[v]&fibre(j));
    assert(x!=y&&!(g[u]>>y&1)&&!(g[v]>>x&1));
    g[u]^=(1ULL<<x)|(1ULL<<y);g[v]^=(1ULL<<x)|(1ULL<<y);
    g[x]^=(1ULL<<u)|(1ULL<<v);g[y]^=(1ULL<<u)|(1ULL<<v);
}
void save(const std::string& prefix,const Graph& g,int F,int bad,long long iteration,
          long long accepted,long long uphill,double temperature){
    validate(g);auto rs=route_stats(g);
    assert(energy(g)==F&&rs.F==F&&rs.alternative_F==F&&bad_count(g)==bad&&rs.bad==bad);
    std::ofstream out(prefix+".json"),edges(prefix+".edges");out<<std::setprecision(12);
    out<<"{\"n\":58,\"F\":"<<F<<",\"bad_pairs\":"<<bad<<",\"iteration\":"<<iteration
       <<",\"accepted\":"<<accepted<<",\"accepted_uphill_F\":"<<uphill<<",\"random_seed\":"<<RANDOM_SEED
       <<",\"cpu_seconds_at_save\":"<<elapsed()<<",\"temperature\":"<<temperature<<",\"row_F_histogram\":[";
    for(int k=0;k<21;++k){if(k)out<<',';out<<rs.row_F[k];}out<<"],\"row_max_K_histogram\":[";
    for(int k=0;k<8;++k){if(k)out<<',';out<<rs.max_K[k];}out<<"],\"edges\":[";edges<<"58 232\n";
    bool first=true;int count=0;
    for(int u=0;u<58;++u)for(int v=u+1;v<58;++v)if(g[u]>>v&1){
        if(!first)out<<',';first=false;out<<'['<<u<<','<<v<<']';edges<<u<<' '<<v<<'\n';++count;}
    assert(count==232);out<<"],\"interfaces\":[";first=true;
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j){
        if(!first)out<<',';first=false;out<<"{\"i\":"<<i<<",\"j\":"<<j<<",\"permutation\":[";
        for(int a=0;a<6;++a){if(a)out<<',';out<<__builtin_ctzll(g[vertex(i,a)]&fibre(j))-(10+6*j);}out<<"]}";
    }out<<"]}\n";
}
int main(int argc,char**argv){
    assert(argc==4||argc==5);cpu_start=double(std::clock())/CLOCKS_PER_SEC;
    int e=0;for(int i=1;i<8;++i)for(int j=i+1;j<8;++j)interfaces[e++]={i,j};assert(e==21);
    std::string action=argv[1];Graph initial=read_graph(argv[2]);validate(initial);
    auto initial_routes=route_stats(initial);assert(bad_count(initial)==24&&energy(initial)==84);
    assert(initial_routes.F==84&&initial_routes.alternative_F==84&&initial_routes.bad==24);
    assert(initial_routes.row_F[0]==162&&initial_routes.row_F[14]==6);
    if(action=="selfcheck"){
        assert(argc==4);int checked=0;
        for(int block=0;block<21;++block)for(int a=0;a<6;++a)for(int b=a+1;b<6;++b){
            Graph next=initial;change(next,block,a,b);validate(next);auto r=route_stats(next);
            assert(energy(next)==r.F&&r.F==r.alternative_F&&bad_count(next)==r.bad);
            assert((r.F==0)==(r.bad==0));change(next,block,a,b);assert(next==initial);++checked;
        }
        std::ofstream out(argv[3]);out<<std::setprecision(12)
          <<"{\"status\":\"SELF_CHECK_ONLY\",\"initial_F\":84,\"initial_bad_pairs\":24,"
          <<"\"initial_zero_F_rows\":162,\"initial_F14_rows\":6,\"switches_checked\":"<<checked
          <<",\"graph_and_both_route_energy_formulas_agree\":true,\"bad_counts_agree\":true,"
          <<"\"all_reversible_degree_and_gauge_preserving\":true,\"optimization_runs\":0,\"cpu_seconds\":"<<elapsed()<<"}\n";
        std::cout<<"selfcheck "<<checked<<" switches, seed F84/bad24\n";return 0;
    }
    assert(action=="search"&&argc==5);double budget=std::stod(argv[3]);assert(budget>0&&budget<=60);
    std::string dir=argv[4];std::mt19937_64 rng(RANDOM_SEED);
    Graph current=initial;int current_F=84,current_bad=24,best_F=84,bad_at_best_F=24,best_bad=24,F_at_best_bad=84;
    long long iteration=0,accepted=0,uphill=0;double temperature=2.5;
    save(dir+"/candidate.initial",initial,84,24,0,0,0,temperature);
    save(dir+"/candidate.best_energy",initial,84,24,0,0,0,temperature);
    save(dir+"/candidate.best_bad",initial,84,24,0,0,0,temperature);
    std::ofstream trace(dir+"/improvements.jsonl");std::cout<<"initial F 84 bad 24"<<std::endl;
    while(best_F>0&&elapsed()<budget){
        int block=rng()%21,a=rng()%6,b=rng()%5;if(b>=a)++b;
        Graph proposal=current;change(proposal,block,a,b);int next_F=energy(proposal),next_bad=bad_count(proposal);
        temperature=2.5*std::pow(0.15/2.5,double(iteration%PERIOD)/PERIOD);
        double uniform=double(rng()>>11)*0x1.0p-53;
        bool accept=next_F<=current_F||uniform<std::exp(double(current_F-next_F)/temperature);
        if(accept){if(next_F>current_F)++uphill;current=proposal;current_F=next_F;current_bad=next_bad;++accepted;}
        ++iteration;
        auto record=[&](const std::string& kind){
            trace<<std::setprecision(12)<<"{\"kind\":\""<<kind<<"\",\"iteration\":"<<iteration
                 <<",\"F\":"<<next_F<<",\"bad_pairs\":"<<next_bad<<",\"accepted\":"<<(accept?"true":"false")
                 <<",\"cpu_seconds\":"<<elapsed()<<",\"changed_interface\":["<<interfaces[block][0]<<','<<interfaces[block][1]
                 <<"],\"swapped_coordinates\":["<<a<<','<<b<<"],\"temperature\":"<<temperature<<"}\n";trace.flush();
        };
        if(next_F<best_F){
            best_F=next_F;bad_at_best_F=next_bad;
            save(dir+"/candidate.best_energy",proposal,next_F,next_bad,iteration,accepted,uphill,temperature);
            save(dir+"/best_F_"+std::to_string(best_F),proposal,next_F,next_bad,iteration,accepted,uphill,temperature);
            record("strict_best_F");std::cout<<"best F "<<best_F<<" bad "<<next_bad<<" iteration "<<iteration<<" cpu "<<elapsed()<<std::endl;
        }
        // Every evaluated full proposal may improve the independently tracked
        // bad count, even if the energy acceptance rejected it. Ties prefer F.
        if(next_bad<best_bad||(next_bad==best_bad&&next_F<F_at_best_bad)){
            best_bad=next_bad;F_at_best_bad=next_F;
            save(dir+"/candidate.best_bad",proposal,next_F,next_bad,iteration,accepted,uphill,temperature);
            save(dir+"/best_bad_"+std::to_string(best_bad),proposal,next_F,next_bad,iteration,accepted,uphill,temperature);
            record("best_bad_lexicographic_tie_F");
        }
    }
    save(dir+"/candidate.current",current,current_F,current_bad,iteration,accepted,uphill,temperature);
    std::ofstream state(dir+"/rng.final.txt");state<<rng<<'\n';
    std::ofstream out(dir+"/search.json");out<<std::setprecision(12)
      <<"{\"status\":\""<<(best_F==0?"TARGET_CANDIDATE_PENDING_BFS":"BOUNDED_HEURISTIC_COMPLETED")
      <<"\",\"stop_reason\":\""<<(best_F==0?"energy_zero":"cpu_budget")
      <<"\",\"initial_F\":84,\"initial_bad_pairs\":24,\"best_F\":"<<best_F<<",\"bad_at_best_F\":"<<bad_at_best_F
      <<",\"best_bad_pairs\":"<<best_bad<<",\"F_at_best_bad\":"<<F_at_best_bad
      <<",\"current_F\":"<<current_F<<",\"current_bad_pairs\":"<<current_bad<<",\"proposals\":"<<iteration
      <<",\"accepted\":"<<accepted<<",\"accepted_uphill_F\":"<<uphill<<",\"random_seed\":"<<RANDOM_SEED
      <<",\"temperature_period_proposals\":"<<PERIOD<<",\"temperature_high\":2.5,\"temperature_low\":0.15"
      <<",\"cpu_seconds\":"<<elapsed()<<",\"cpu_budget_seconds\":"<<budget
      <<",\"threads\":1,\"chain_restarts\":0,\"complete_enumeration\":false}\n";
    std::cout<<"finished best F "<<best_F<<" best bad "<<best_bad<<" cpu "<<elapsed()<<std::endl;
}

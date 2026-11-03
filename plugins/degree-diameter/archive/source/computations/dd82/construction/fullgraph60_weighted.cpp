// Full 60-vertex simple 8-regular domain. Weighted strict descent with
// persistent positive pair penalties; no partition, group action or frozen edge.
#include <array>
#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>
using Graph=std::array<uint64_t,60>;
using Weights=std::array<std::array<int64_t,60>,60>;
using Edge=std::pair<int,int>;
struct Value {int64_t weighted=0;int bad=0;};
struct Move {std::array<Edge,2> removed{},added{};};
struct Scan {bool complete=true;uint64_t evaluated=0,banned=0;Value minimum{INT64_MAX,0};Move move;int64_t jump=INT64_MAX;};
double cpu_start;
auto wall_start=std::chrono::steady_clock::now();
double cpu(){return double(std::clock())/CLOCKS_PER_SEC-cpu_start;}
double wall(){return std::chrono::duration<double>(std::chrono::steady_clock::now()-wall_start).count();}
Edge edge(int a,int b){return std::minmax(a,b);}
void toggle(Graph& g,Edge e){auto[a,b]=e;g[a]^=1ULL<<b;g[b]^=1ULL<<a;}
void apply_switch(Graph& g,const Move& m){for(auto e:m.removed)toggle(g,e);for(auto e:m.added)toggle(g,e);}
bool bad(const Graph& g,int a,int b){return !(g[a]>>b&1) && !(g[a]&g[b]);}
void validate(const Graph& g){
    for(int a=0;a<60;++a){assert(__builtin_popcountll(g[a])==8 && !(g[a]>>a&1));
        for(int b=0;b<60;++b)assert((g[a]>>b&1)==(g[b]>>a&1));}
}
Graph load(const std::string& path){
    std::ifstream in(path);int n,m;in>>n>>m;assert(n==60&&m==240);Graph g{};
    for(int i=0,a,b;i<m;++i){in>>a>>b;assert(in&&0<=a&&a<b&&b<60&&!(g[a]>>b&1));toggle(g,{a,b});}
    int extra;assert(!(in>>extra));validate(g);return g;
}
Value full(const Graph& g,const Weights& w){
    Value v;for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(g,a,b)){v.bad++;v.weighted+=w[a][b];}return v;
}
// Independent sanity evaluator: explicit adjacency matrix and all actual
// intermediate vertices, not the bitset-intersection or delta implementation.
Value slow(const Graph& g,const Weights& w){
    bool a[60][60];for(int u=0;u<60;++u)for(int v=0;v<60;++v)a[u][v]=g[u]>>v&1;
    Value ans;for(int u=0;u<60;++u)for(int v=u+1;v<60;++v){
        bool covered=a[u][v];for(int x=0;x<60&&!covered;++x)covered=a[u][x]&&a[x][v];
        if(!covered){ans.bad++;ans.weighted+=w[u][v];}}
    return ans;
}
Value incident(const Graph& g,const Weights& w,const std::array<int,4>& changed){
    uint64_t mask=0;for(int u:changed)mask|=1ULL<<u;Value v;
    for(int u:changed)for(int x=0;x<60;++x){
        if(x==u || ((mask>>x&1)&&x<u))continue;
        if(bad(g,u,x)){++v.bad;v.weighted+=w[u][x];}}
    return v;
}
bool inverse_of(const Move& m,const Move& last){
    auto r=m.removed,a=m.added,lr=last.removed,la=last.added;
    std::sort(r.begin(),r.end());std::sort(a.begin(),a.end());
    std::sort(lr.begin(),lr.end());std::sort(la.begin(),la.end());
    return r==la&&a==lr;
}
Value trial(Graph& g,const Weights& w,Value now,const Move& m,int* repaired=nullptr){
    std::array<int,4> changed={m.removed[0].first,m.removed[0].second,m.removed[1].first,m.removed[1].second};
    std::array<uint64_t,4> old_bad{};
    if(repaired)for(int i=0;i<4;++i)for(int x=0;x<60;++x)
        if(x!=changed[i]&&bad(g,changed[i],x))old_bad[i]|=1ULL<<x;
    Value before=incident(g,w,changed);apply_switch(g,m);Value after=incident(g,w,changed);
    if(repaired){
        *repaired=0;uint64_t mask=0;for(int u:changed)mask|=1ULL<<u;
        for(int i=0;i<4;++i){int u=changed[i];for(int x=0;x<60;++x)
            if(x!=u&&!((mask>>x&1)&&x<u)&&(old_bad[i]>>x&1)&&!bad(g,u,x))++*repaired;}
    }
    apply_switch(g,m);
    return {now.weighted+after.weighted-before.weighted,now.bad+after.bad-before.bad};
}
std::vector<Edge> edges(const Graph& g){
    std::vector<Edge> result;for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(g[a]>>b&1)result.emplace_back(a,b);return result;
}
template<class Visit> bool enumerate(Graph& g,Visit visit){
    const auto es=edges(g);
    for(unsigned i=0;i<es.size();++i)for(unsigned j=i+1;j<es.size();++j){
        auto[a,b]=es[i];auto[c,d]=es[j];if(a==c||a==d||b==c||b==d)continue;
        for(int mode=0;mode<2;++mode){
            Move m{{es[i],es[j]},mode==0?std::array<Edge,2>{edge(a,c),edge(b,d)}:
                std::array<Edge,2>{edge(a,d),edge(b,c)}};
            if((g[m.added[0].first]>>m.added[0].second&1)||(g[m.added[1].first]>>m.added[1].second&1))continue;
            if(!visit(m))return false;
        }}
    return true;
}
Scan scan(Graph& g,const Weights& w,Value now,const Move* last,double cpu_limit,double wall_limit){
    Scan s;s.complete=enumerate(g,[&](const Move& m){
        if(last&&inverse_of(m,*last)){++s.banned;return true;}
        int repaired=0;Value v=trial(g,w,now,m,&repaired);++s.evaluated;
        // Lexicographic enumeration supplies deterministic ties; no RNG.
        if(v.weighted<s.minimum.weighted){s.minimum=v;s.move=m;}
        const int64_t delta=v.weighted-now.weighted;
        if(repaired>0&&delta>=0)s.jump=std::min(s.jump,delta/repaired+1);
        return s.evaluated%512 || (cpu()<cpu_limit&&wall()<wall_limit);
    });return s;
}
void move_json(std::ostream& o,const Move& m){
    o<<"{\"removed\":[";for(int i=0;i<2;++i){if(i)o<<',';o<<'['<<m.removed[i].first<<','<<m.removed[i].second<<']';}
    o<<"],\"added\":[";for(int i=0;i<2;++i){if(i)o<<',';o<<'['<<m.added[i].first<<','<<m.added[i].second<<']';}o<<"]}";
}
void save_graph(const std::string& prefix,const Graph& g,Value v,uint64_t step){
    validate(g);std::ofstream e(prefix+".edges"),j(prefix+".json");e<<"60 240\n";
    j<<"{\"n\":60,\"bad_pairs\":"<<v.bad<<",\"weighted_score_at_save\":"<<v.weighted<<",\"accepted_step\":"<<step<<",\"edges\":[";
    bool first=true;for(auto[a,b]:edges(g)){e<<a<<' '<<b<<'\n';if(!first)j<<',';first=false;j<<'['<<a<<','<<b<<']';}j<<"]}\n";
}
void save_weights(const std::string& path,const Weights& w){
    std::ofstream o(path);o<<"[";for(int a=0;a<60;++a){if(a)o<<',';o<<'[';for(int b=0;b<60;++b){if(b)o<<',';o<<w[a][b];}o<<']';}o<<"]\n";
}
void save_bad_overlap(const std::string& path,const Graph& g,const Graph& initial){
    std::ofstream o(path);int count=0,common=0;
    for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(g,a,b)){++count;common+=bad(initial,a,b);}
    o<<"{\"bad_pair_count\":"<<count<<",\"intersection_with_initial_bad_pairs\":"<<common<<",\"bad_pairs\":[";
    bool first=true;for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(g,a,b)){
        if(!first)o<<',';first=false;o<<'['<<a<<','<<b<<']';}o<<"]}\n";
}
int main(int argc,char**argv){
    assert(argc==6);cpu_start=double(std::clock())/CLOCKS_PER_SEC;wall_start=std::chrono::steady_clock::now();
    std::string action=argv[1],out=argv[3];Graph initial=load(argv[2]),current=initial;
    Weights w{};for(int a=0;a<60;++a)for(int b=0;b<60;++b)w[a][b]=(a!=b);
    Value now=full(current,w);assert(now.bad==20&&now.weighted==20);
    if(action=="sanity"){
        // Exactly 1000 legal proposals; independently check unit and nonuniform weights.
        int checked=0;enumerate(current,[&](const Move& m){
            if(checked==500){for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)w[a][b]=w[b][a]=1+(a*61+b*17)%7;now=full(current,w);}
            Value predicted=trial(current,w,now,m);apply_switch(current,m);validate(current);Value actual=slow(current,w);
            assert(predicted.bad==actual.bad&&predicted.weighted==actual.weighted);apply_switch(current,m);assert(current==initial);
            return ++checked<1000;
        });assert(checked==1000);
        Value before=slow(current,w);for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(current,a,b)){++w[a][b];++w[b][a];}
        Value after=slow(current,w);assert(after.weighted==before.weighted+before.bad&&after.bad==before.bad);
        std::ofstream s(out+"/sanity.json");s<<std::setprecision(12)<<"{\"passed\":true,\"initial_bad_pairs\":20,\"legal_proposals_checked\":1000,\"unit_weight_checks\":500,\"nonuniform_weight_checks\":500,\"weight_increment_check\":true,\"cpu_seconds\":"<<cpu()<<",\"wall_seconds\":"<<wall()<<"}\n";
        return 0;
    }
    if(action=="change_sanity"){
        Move first_move;bool got=false;enumerate(current,[&](const Move& m){first_move=m;got=true;return false;});assert(got);
        apply_switch(current,first_move);int inverses=0;Move next_move;bool got_next=false;
        enumerate(current,[&](const Move& m){
            if(inverse_of(m,first_move))++inverses;
            else if(!got_next){next_move=m;got_next=true;}
            return true;
        });assert(inverses==1&&got_next);
        Move exact_inverse{first_move.added,first_move.removed};assert(inverse_of(exact_inverse,first_move));
        for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(current,a,b)){++w[a][b];++w[b][a];}
        assert(inverse_of(exact_inverse,first_move)); // A weight-only update retains last move.
        Move next_inverse{next_move.added,next_move.removed};assert(inverse_of(next_inverse,next_move));
        assert(!inverse_of(exact_inverse,next_move));
        current=initial;for(int a=0;a<60;++a)for(int b=0;b<60;++b)w[a][b]=(a!=b);now=full(current,w);
        struct Check {Move m;int k;int64_t delta;};std::vector<Check> checks;int64_t jump=INT64_MAX;
        enumerate(current,[&](const Move& m){
            int k;Value v=trial(current,w,now,m,&k);Graph next=current;apply_switch(next,m);
            int expected=0;for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)expected+=bad(current,a,b)&&!bad(next,a,b);
            assert(k==expected);assert(v.weighted-now.weighted>=0);
            if(k>0)jump=std::min(jump,(v.weighted-now.weighted)/k+1);
            checks.push_back({m,k,v.weighted-now.weighted});return checks.size()<64;
        });assert(checks.size()==64&&jump!=INT64_MAX);
        bool at_jump_improvement=false;
        for(int64_t t:{jump-1,jump}){
            Weights incremented=w;for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(current,a,b))incremented[a][b]=incremented[b][a]=1+t;
            Value base=slow(current,incremented);
            for(const auto& c:checks){Graph next=current;apply_switch(next,c.m);int64_t delta=slow(next,incremented).weighted-base.weighted;
                assert(delta==c.delta-t*c.k);if(t==jump-1)assert(delta>=0);else at_jump_improvement|=delta<0;}
        }assert(at_jump_improvement);
        std::ofstream s(out+"/change_sanity.json");s<<std::setprecision(12)<<"{\"passed\":true,\"inverse_candidates_for_one_real_move\":1,\"inverse_ban_persists_across_weight_updates\":true,\"last_move_changes_after_next_move\":true,\"jump_formula_moves_checked\":64,\"jump_checked_at_t_minus_one_and_t\":true,\"subset_jump\":"<<jump<<",\"cpu_seconds\":"<<cpu()<<",\"wall_seconds\":"<<wall()<<"}\n";
        return 0;
    }
    assert(action=="search");const double cpu_limit=std::stod(argv[4]),wall_limit=std::stod(argv[5]);
    Graph best=current;Value best_value=now;
    uint64_t scans=0,complete_scans=0,evaluated=0,banned=0,steps=0,updates=0,raw_uphill=0,raw_equal=0,total_increment=0,unit_rounds_skipped=0;
    std::array<uint64_t,4> equal_recent{};std::vector<Graph> recent{initial};Move last_move;bool have_last=false;
    std::string stop="cpu_budget";bool first_departure=false;
    save_graph(out+"/candidate.best",best,best_value,0);
    std::ofstream events(out+"/events.jsonl");
    while(now.bad){
        if(cpu()>=cpu_limit){stop="cpu_budget";break;}if(wall()>=wall_limit){stop="wall_budget";break;}
        Scan s=scan(current,w,now,have_last?&last_move:nullptr,cpu_limit,wall_limit);++scans;evaluated+=s.evaluated;banned+=s.banned;
        if(!s.complete){stop="budget_during_neighborhood";break;}++complete_scans;
        if(s.minimum.weighted<now.weighted){
            Value before=now;apply_switch(current,s.move);now=full(current,w);
            assert(now.weighted==s.minimum.weighted&&now.bad==s.minimum.bad);++steps;
            last_move=s.move;have_last=true;
            for(unsigned lag=1;lag<=recent.size();++lag)equal_recent[lag-1]+=current==recent[recent.size()-lag];
            recent.push_back(current);if(recent.size()>4)recent.erase(recent.begin());
            raw_uphill+=now.bad>before.bad;raw_equal+=now.bad==before.bad;
            events<<"{\"event\":\"weighted_descent\",\"step\":"<<steps<<",\"scan\":"<<scans<<",\"bad_before\":"<<before.bad<<",\"bad_after\":"<<now.bad<<",\"weighted_before\":"<<before.weighted<<",\"weighted_after\":"<<now.weighted<<",\"move\":";move_json(events,s.move);events<<"}\n";
            if(!first_departure){save_graph(out+"/candidate.first_departure",current,now,steps);save_bad_overlap(out+"/first.bad_pairs.json",current,initial);first_departure=true;}
            if(now.bad<best_value.bad){best=current;best_value=now;save_graph(out+"/candidate.best",best,best_value,steps);
                save_graph(out+"/best_"+std::to_string(now.bad),best,best_value,steps);
                std::cout<<"best "<<now.bad<<" step "<<steps<<" cpu "<<cpu()<<std::endl;}
        }else{
            assert(s.jump!=INT64_MAX&&s.jump>0);++updates;total_increment+=uint64_t(now.bad)*s.jump;unit_rounds_skipped+=s.jump-1;
            events<<"{\"event\":\"increment_current_bad_pair_weights\",\"update\":"<<updates<<",\"scan\":"<<scans<<",\"bad_pairs\":"<<now.bad<<",\"increment\":"<<s.jump<<",\"weighted_before\":"<<now.weighted;
            for(int a=0;a<60;++a)for(int b=a+1;b<60;++b)if(bad(current,a,b)){w[a][b]+=s.jump;w[b][a]+=s.jump;}
            now.weighted+=int64_t(now.bad)*s.jump;assert(full(current,w).weighted==now.weighted);
            events<<",\"weighted_after\":"<<now.weighted<<"}\n";
        }
    }
    if(!now.bad)stop="target_candidate_found";
    save_graph(out+"/candidate.current",current,now,steps);save_weights(out+"/weights.final.json",w);
    save_bad_overlap(out+"/best.bad_pairs.json",best,initial);save_bad_overlap(out+"/final.bad_pairs.json",current,initial);
    int64_t max_weight=1;int increased_pairs=0;
    for(int a=0;a<60;++a)for(int b=a+1;b<60;++b){max_weight=std::max(max_weight,w[a][b]);increased_pairs+=w[a][b]>1;}
    std::ofstream checkpoint(out+"/checkpoint.json");checkpoint<<"{\"has_last_move\":"<<(have_last?"true":"false")<<",\"last_move\":";
    if(have_last)move_json(checkpoint,last_move);else checkpoint<<"null";
    checkpoint<<",\"accepted_steps\":"<<steps<<",\"rng_used\":false,\"graph\":\"candidate.current.edges\",\"weights\":\"weights.final.json\",\"incomplete_scan_retained\":false}\n";
    std::ofstream result(out+"/search.json");result<<std::setprecision(15)
       <<"{\"status\":\""<<(now.bad?"BOUNDED_HEURISTIC_COMPLETED":"TARGET_REQUIRES_INDEPENDENT_BFS")<<"\",\"stop_reason\":\""<<stop
       <<"\",\"initial_bad_pairs\":20,\"best_bad_pairs\":"<<best_value.bad<<",\"current_bad_pairs\":"<<now.bad<<",\"current_weighted_score\":"<<now.weighted
       <<",\"neighborhood_scans\":"<<scans<<",\"complete_neighborhood_scans\":"<<complete_scans<<",\"evaluated_switches\":"<<evaluated
       <<",\"accepted_weighted_descent_steps\":"<<steps<<",\"raw_bad_pair_increasing_steps\":"<<raw_uphill<<",\"raw_bad_pair_equal_steps\":"<<raw_equal
       <<",\"weight_update_events\":"<<updates<<",\"total_pair_weight_increments\":"<<total_increment<<",\"unit_increment_rounds_skipped\":"<<unit_rounds_skipped<<",\"inverse_moves_banned\":"<<banned<<",\"distinct_pairs_with_increased_weight\":"<<increased_pairs<<",\"maximum_pair_weight\":"<<max_weight<<",\"equal_to_previous_accepted_states_by_lag\":["<<equal_recent[0]<<','<<equal_recent[1]<<','<<equal_recent[2]<<','<<equal_recent[3]<<"],\"departed_initial\":"<<(first_departure?"true":"false")
       <<",\"rng_used\":false,\"tie_break\":\"lexicographically_first_minimum_weighted_score\",\"chain_restarts\":0,\"complete_enumeration\":false"
       <<",\"checkpoint_scope\":\"current graph and all pair weights; incomplete neighborhood is not retained\",\"cpu_seconds\":"<<cpu()<<",\"wall_seconds\":"<<wall()<<"}\n";
    std::cout<<"stopped "<<stop<<" best "<<best_value.bad<<" current "<<now.bad<<" scans "<<complete_scans<<std::endl;
}

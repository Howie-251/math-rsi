#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using Perm = std::array<int, 7>;
using Graph = std::array<uint64_t, 35>;
constexpr uint64_t FULL = (1ull << 35) - 1;
constexpr uint32_t ALL_COLORS = 0x0fffffffu;
const std::array<Perm, 2> ds = {Perm{0,0,0,1,2,3,4}, Perm{0,0,1,1,2,3,4}};
const Perm OLD_P = {0,2,3,4,5,6,1}, OLD_Q = {2,0,6,1,3,4,5};
int pop(uint64_t x) { return __builtin_popcountll(x); }
int first(uint64_t x) { return __builtin_ctzll(x); }
int mod5(int x) { return (x % 5 + 5) % 5; }

// Identical permutation order, signatures, and q-bucket insertion order to
// cyclic5_h35_run/enumerate.cpp. This is essential to the inherited prefix.
uint32_t signature(const Perm& p, const Perm& d, int step) {
    Perm inv{};
    for (int r=0; r<7; ++r) inv[p[r]]=r;
    uint32_t key=0;
    for (int r=0; r<7; ++r) {
        int a=mod5(step+d[p[r]]-d[r]);
        int b=mod5(-step+d[inv[r]]-d[r]);
        if (!a || !b || a==b) return UINT32_MAX;
        key |= ((1u << (a-1)) | (1u << (b-1))) << (4*r);
    }
    return key;
}
Graph graph(const Perm& p, const Perm& q) {
    Graph a{};
    auto edge=[&](int x, int y) { a[x]|=1ull<<y; a[y]|=1ull<<x; };
    for (int r=0; r<7; ++r) for (int i=0; i<5; ++i) {
        edge(5*r+i, 5*p[r]+(i+1)%5);
        edge(5*r+i, 5*q[r]+(i+2)%5);
    }
    return a;
}
struct Score { Perm rho{}; int mx=0, total=0; };
Score score(const Graph& a, const Perm& d) {
    Score s;
    for (int r=0; r<7; ++r) {
        int z=5*r;
        uint64_t reach=a[z], bits=a[z];
        while (bits) { int v=first(bits); bits&=bits-1; reach|=a[v]; }
        reach &= ~(1ull<<z);
        int m=std::count(d.begin(),d.end(),d[r]);
        s.rho[r]=16-pop(reach)+m-1;
        s.mx=std::max(s.mx,s.rho[r]); s.total+=5*s.rho[r];
    }
    return s;
}
struct Budget {
    std::chrono::steady_clock::time_point wall=std::chrono::steady_clock::now();
    std::clock_t cpu=std::clock();
    uint64_t polls=0, nodes=0;
    int64_t sanity_node_limit=-1; // Used only by --sanity, never production.
    bool limited=false;
    double cpu_seconds() const { return double(std::clock()-cpu)/CLOCKS_PER_SEC; }
    double wall_seconds() const {
        return std::chrono::duration<double>(std::chrono::steady_clock::now()-wall).count();
    }
    bool check(bool force=false) {
        if (limited) return true;
        if (force || (++polls % 256 == 0))
            limited=cpu_seconds()>=27 || wall_seconds()>=40;
        return limited;
    }
    bool node() {
        ++nodes;
        if (sanity_node_limit>=0 && nodes>=uint64_t(sanity_node_limit)) limited=true;
        return check();
    }
};
struct HData {
    Graph adj, closed{}, allowed{}, covered{}, holes{};
    std::array<int,35> f{}, g{}, rho{};
    HData(const Graph& a, const Perm& d): adj(a) {
        for (int z=0; z<35; ++z) { f[z]=z%5; g[z]=(z%5+d[z/5])%5; }
        for (int z=0; z<35; ++z) {
            closed[z]=adj[z]|(1ull<<z);
            uint64_t reach=closed[z], bits=adj[z];
            while (bits) { int v=first(bits); bits&=bits-1; reach|=adj[v]; }
            allowed[z]=FULL^reach;
            for (int v=0; v<35; ++v)
                if (f[v]==f[z] || g[v]==g[z]) reach|=1ull<<v;
            covered[z]=reach & ~(1ull<<z);
            holes[z]=FULL & ~reach;
            rho[z]=28-pop(covered[z]);
        }
    }
    bool independent(uint64_t set) const {
        for (uint64_t bits=set; bits; bits&=bits-1)
            if (adj[first(bits)] & set) return false;
        return true;
    }
    bool colors21111(uint64_t set) const {
        std::array<int,5> cf{},cg{};
        for (uint64_t bits=set; bits; bits&=bits-1) {
            int v=first(bits); ++cf[f[v]]; ++cg[g[v]];
        }
        std::sort(cf.begin(),cf.end()); std::sort(cg.begin(),cg.end());
        const std::array<int,5> target={1,1,1,1,2};
        return cf==target && cg==target;
    }
    bool ap_covered(uint64_t A, uint64_t P) const {
        for (uint64_t bits=A; bits; bits&=bits-1)
            if (holes[first(bits)] & P) return false;
        return true;
    }
    bool root_parent(int z, uint64_t parent) const {
        uint64_t outside=holes[z] & ~parent;
        return pop(outside)<=5 && independent(outside);
    }
};
struct Evaluation {
    uint64_t P=0;
    bool packing=false, color=false, p_independent=false, p_rho=false;
    bool ap=false, a_out=false, p_out=false;
    bool pass() const {
        return packing && color && p_independent && p_rho && ap && a_out && p_out;
    }
};
Evaluation evaluate(const HData& h, uint64_t A) {
    Evaluation e;
    uint64_t occupied=0;
    for (uint64_t bits=A; bits; bits&=bits-1) occupied|=h.closed[first(bits)];
    e.P=FULL^occupied;
    e.packing=pop(A)==6 && pop(occupied)==30;
    e.color=h.colors21111(A);
    e.p_independent=pop(e.P)==5 && h.independent(e.P);
    e.p_rho=pop(e.P)==5;
    for (uint64_t bits=e.P; bits; bits&=bits-1)
        if (h.rho[first(bits)]>3) e.p_rho=false;
    e.ap=h.ap_covered(A,e.P);
    e.a_out=true; e.p_out=true;
    for (uint64_t bits=A; bits; bits&=bits-1)
        if (!h.root_parent(first(bits),A)) e.a_out=false;
    for (uint64_t bits=e.P; bits; bits&=bits-1)
        if (!h.root_parent(first(bits),e.P)) e.p_out=false;
    return e;
}
struct PackingStats {
    uint64_t nodes=0, six=0, color=0, independent=0, p_rho=0, ap=0, a_out=0, all=0;
    void add(const PackingStats& b) {
        nodes+=b.nodes; six+=b.six; color+=b.color; independent+=b.independent;
        p_rho+=b.p_rho; ap+=b.ap; a_out+=b.a_out; all+=b.all;
    }
};
struct PackingSearch {
    const HData& h;
    Budget& budget;
    PackingStats stats;
    bool found=false, complete=false;
    uint64_t witness=0;
    std::vector<uint64_t>* leaves=nullptr;
    PackingSearch(const HData& data, Budget& limit): h(data), budget(limit) {}
    void dfs(uint64_t A, uint64_t choices, int depth) {
        ++stats.nodes;
        if (budget.node()) return;
        if (depth==6) {
            ++stats.six;
            if (leaves) leaves->push_back(A);
            auto e=evaluate(h,A);
            if (!e.color) return;
            ++stats.color;
            if (!e.p_independent) return;
            ++stats.independent;
            if (!e.p_rho) return;
            ++stats.p_rho;
            if (!e.ap) return;
            ++stats.ap;
            if (!e.a_out) return;
            ++stats.a_out;
            if (!e.p_out) return;
            ++stats.all;
            found=true; witness=A;
            return;
        }
        while (choices && pop(choices)>=6-depth) {
            int v=first(choices); choices&=choices-1;
            dfs(A|(1ull<<v), choices & h.allowed[v], depth+1);
            if (found || budget.limited) return;
        }
    }
    void run() { dfs(0,FULL,0); complete=!found && !budget.limited; }
};
template<class T> void array_json(std::ostream& o, const T& v) {
    o<<'['; bool first_item=true;
    for (auto x:v) { if (!first_item) o<<','; first_item=false; o<<x; } o<<']';
}
void set_json(std::ostream& o, uint64_t set) {
    std::vector<int> v;
    while (set) { v.push_back(first(set)); set&=set-1; } array_json(o,v);
}
void evaluation_json(std::ostream& o, const Evaluation& e) {
    o<<std::boolalpha<<"{\"packing\":"<<e.packing<<",\"colors_21111\":"<<e.color
     <<",\"P_independent\":"<<e.p_independent<<",\"P_rho_at_most3\":"<<e.p_rho
     <<",\"AP_covered\":"<<e.ap<<",\"A_Rout\":"<<e.a_out
     <<",\"P_Rout\":"<<e.p_out<<",\"pass\":"<<e.pass()<<'}';
}
void packing_stats_json(std::ostream& o, const PackingStats& s) {
    o<<"{\"nodes\":"<<s.nodes<<",\"six_packings\":"<<s.six
     <<",\"color_pass\":"<<s.color<<",\"P_independent_pass\":"<<s.independent
     <<",\"P_rho_pass\":"<<s.p_rho<<",\"AP_pass\":"<<s.ap
     <<",\"A_Rout_pass\":"<<s.a_out<<",\"all_pass\":"<<s.all<<'}';
}
void candidate_json(std::ostream& o, int type, const Perm& p, const Perm& q, const Score& s) {
    o<<"{\"type\":"<<type<<",\"d\":"; array_json(o,ds[type]);
    o<<",\"p\":"; array_json(o,p); o<<",\"q\":"; array_json(o,q);
    o<<",\"rho_orbit\":"; array_json(o,s.rho);
    o<<",\"max_rho\":"<<s.mx<<",\"sum_rho\":"<<s.total<<'}';
}
uint64_t mask(std::initializer_list<int> v) {
    uint64_t x=0; for (int z:v) x|=1ull<<z; return x;
}
void sanity() {
    const Perm id={0,1,2,3,4,5,6}, shift={1,2,3,4,5,6,0};
    struct Case { int type; Perm p,q; };
    const std::array<Case,4> cases={Case{0,id,id},Case{1,id,id},Case{1,id,shift},Case{0,OLD_P,OLD_Q}};
    std::cout<<std::boolalpha<<"{\"graph_cases\":[";
    for (size_t k=0; k<cases.size(); ++k) {
        if (k) std::cout<<',';
        auto c=cases[k]; auto a=graph(c.p,c.q); auto s=score(a,ds[c.type]);
        uint32_t sig=signature(c.p,ds[c.type],1);
        std::cout<<"{\"candidate\":"; candidate_json(std::cout,c.type,c.p,c.q,s);
        std::cout<<",\"signature_accept\":"<<(sig!=UINT32_MAX && signature(c.q,ds[c.type],2)==(ALL_COLORS^sig));
        std::cout<<",\"edges\":["; bool one=true;
        for (int x=0; x<35; ++x) for (int y=x+1; y<35; ++y) if (a[x]&(1ull<<y)) {
            if (!one) std::cout<<',';
            one=false; std::cout<<'['<<x<<','<<y<<']';
        }
        std::cout<<"]}";
    }
    HData old(graph(OLD_P,OLD_Q),ds[0]);
    Budget b; std::vector<uint64_t> leaves;
    PackingSearch search{old,b}; search.leaves=&leaves; search.run();
    std::cout<<"],\"old_packing\":{\"complete\":"<<search.complete<<",\"stats\":";
    packing_stats_json(std::cout,search.stats); std::cout<<",\"leaves\":[";
    for (size_t k=0; k<leaves.size(); ++k) {
        if (k) std::cout<<',';
        auto e=evaluate(old,leaves[k]); std::cout<<"{\"A\":"; set_json(std::cout,leaves[k]);
        std::cout<<",\"P\":"; set_json(std::cout,e.P);
        std::cout<<",\"checks\":"; evaluation_json(std::cout,e); std::cout<<'}';
    }
    std::cout<<"]},\"AP_probes\":[";
    const std::array<uint64_t,2> targets={mask({1,2,5}),mask({17})};
    for (int k=0; k<2; ++k) {
        if (k) std::cout<<',';
        std::cout<<"{\"A\":[0],\"P\":"; set_json(std::cout,targets[k]);
        std::cout<<",\"pass\":"<<old.ap_covered(1,targets[k])<<'}';
    }
    std::cout<<"],\"Rout_probes\":[";
    const std::array<uint64_t,3> parents={mask({0,24,26,28,29,33}),mask({0,17,24,26,28,33}),mask({0,1,2,3,4,5})};
    for (int k=0; k<3; ++k) {
        if (k) std::cout<<',';
        std::cout<<"{\"root\":0,\"parent\":"; set_json(std::cout,parents[k]);
        std::cout<<",\"outside\":"; set_json(std::cout,old.holes[0]&~parents[k]);
        std::cout<<",\"pass\":"<<old.root_parent(0,parents[k])<<'}';
    }
    Budget stopped; stopped.sanity_node_limit=2;
    PackingSearch partial{old,stopped}; partial.run();
    std::cout<<"],\"interrupted_packing\":{\"limited\":"<<stopped.limited
             <<",\"complete\":"<<partial.complete<<",\"found\":"<<partial.found
             <<",\"stats\":"; packing_stats_json(std::cout,partial.stats);
    std::cout<<"}}\n";
}
struct TypeStats {
    uint64_t valid_q=0, valid_p_processed=0, seen=0, skipped=0, checked=0;
    uint64_t row_pass=0, rho_pass=0, packing_started=0, packing_exhausted=0;
    bool started=false, complete=false;
    PackingStats packing;
};
int main(int argc, char** argv) {
    if (argc==2 && std::string(argv[1])=="--sanity") { sanity(); return 0; }
    if (argc!=2) { std::cerr<<"usage: enumerate OUTPUT_DIR or --sanity\n"; return 2; }
    Budget budget;
    std::vector<Perm> permutations; Perm id={0,1,2,3,4,5,6};
    do { permutations.push_back(id); } while (std::next_permutation(id.begin(),id.end()));
    std::array<TypeStats,2> stats{};
    bool found=false; int found_type=-1, active_type=-1;
    Perm found_p{}, found_q{}; Score found_score;
    uint64_t found_A=0, found_P=0;
    for (int t: {1,0}) {
        if (found || budget.check(true)) break;
        auto& st=stats[t]; st.started=true; active_type=t;
        std::map<uint32_t,std::vector<Perm>> qs;
        for (const auto& q:permutations) {
            if (budget.check()) break;
            auto key=signature(q,ds[t],2);
            if (key!=UINT32_MAX) { qs[key].push_back(q); ++st.valid_q; }
        }
        if (budget.limited) break;
        for (const auto& p:permutations) {
            if (budget.check()) break;
            auto key=signature(p,ds[t],1);
            if (key==UINT32_MAX) continue;
            ++st.valid_p_processed;
            auto it=qs.find(ALL_COLORS^key); if (it==qs.end()) continue;
            for (const auto& q:it->second) {
                if (budget.check()) break;
                ++st.seen;
                if (t==0 && st.seen<=116) {
                    if (st.seen==116 && (p!=OLD_P || q!=OLD_Q)) {
                        std::cerr<<"Inherited type0 prefix endpoint disagrees with source order\n"; return 3;
                    }
                    ++st.skipped; continue;
                }
                ++st.checked;
                auto a=graph(p,q); auto s=score(a,ds[t]);
                if (s.mx<=4) ++st.row_pass;
                if (s.mx>4 || s.total>130) continue;
                ++st.rho_pass;
                if (budget.check(true)) break;
                HData h(a,ds[t]); PackingSearch packing{h,budget};
                ++st.packing_started; packing.run(); st.packing.add(packing.stats);
                if (packing.complete) ++st.packing_exhausted;
                if (packing.found) {
                    found=true; found_type=t; found_p=p; found_q=q; found_score=s;
                    found_A=packing.witness; found_P=evaluate(h,found_A).P;
                    break;
                }
                if (budget.limited) break;
            }
            if (found || budget.limited) break;
        }
        if (!found && !budget.limited) st.complete=true;
    }
    bool complete=stats[0].complete && stats[1].complete;
    std::string status=found?"JOINT_PARENT_FRONTEND_FOUND":complete?"EXHAUSTED_NO_JOINT_PARENT_FRONTEND":"INCOMPLETE_RESOURCE_LIMIT";
    std::string dir=argv[1]; std::ofstream out(dir+"/result.json");
    out<<std::boolalpha<<"{\"status\":\""<<status<<"\",\"complete\":"<<complete
       <<",\"type_order\":[1,0],\"active_type\":"<<active_type
       <<",\"inherited_type0_prefix\":{\"count\":116,\"source\":\"../cyclic5_h35_run/result.json\",\"packing_source\":\"../cyclic5_h35_run/packing_result.json\"},\"types\":[";
    for (int t=0; t<2; ++t) {
        if (t) out<<',';
        const auto& s=stats[t];
        out<<"{\"type\":"<<t<<",\"started\":"<<s.started<<",\"complete\":"<<s.complete
           <<",\"valid_q\":"<<s.valid_q<<",\"valid_p_processed\":"<<s.valid_p_processed
           <<",\"compatible_pairs_seen\":"<<s.seen<<",\"skipped_inherited\":"<<s.skipped
           <<",\"checked_this_run\":"<<s.checked<<",\"pointwise_pass_this_run\":"<<s.row_pass
           <<",\"rho_pass_this_run\":"<<s.rho_pass<<",\"packing_started\":"<<s.packing_started
           <<",\"packing_exhausted\":"<<s.packing_exhausted<<",\"packing\":";
        packing_stats_json(out,s.packing); out<<'}';
    }
    out<<"],\"candidate\":";
    if (found) candidate_json(out,found_type,found_p,found_q,found_score); else out<<"null";
    out<<",\"A\":"; set_json(out,found_A); out<<",\"P\":"; set_json(out,found_P);
    out<<",\"cpu_seconds\":"<<budget.cpu_seconds()<<",\"wall_seconds\":"<<budget.wall_seconds()<<"}\n";
    if (found) {
        auto a=graph(found_p,found_q); HData h(a,ds[found_type]);
        std::ofstream edges(dir+"/candidate.edges");
        for (int x=0; x<35; ++x) for (int y=x+1; y<35; ++y)
            if (a[x]&(1ull<<y)) edges<<x<<' '<<y<<'\n';
        std::ofstream parent(dir+"/candidate_parent.json");
        parent<<"{\"A\":"; set_json(parent,found_A); parent<<",\"P\":"; set_json(parent,found_P);
        parent<<",\"checks\":"; evaluation_json(parent,evaluate(h,found_A)); parent<<"}\n";
    }
    std::cout<<status<<'\n';
    return 0;
}

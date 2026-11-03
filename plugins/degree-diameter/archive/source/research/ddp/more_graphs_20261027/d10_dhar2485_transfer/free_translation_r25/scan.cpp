#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using Vec = std::array<int,4>;
constexpr int M=25, P=101, R=25, TOTAL=1040604;
const std::array<int,5> PHASES={1,3,6,7,9};
std::array<int,M> rp;
struct Arc { int phase; Vec coeff; };
std::array<Arc,10> arcs;
std::array<std::set<Vec>,M> formal_sets;
std::array<std::vector<Vec>,M> forms;
std::array<int,5> words_by_length{};
std::array<int,M> raw_by_phase{};
std::filesystem::path out;
double began;
double elapsed() { return double(std::clock())/CLOCKS_PER_SEC-began; }
void require(bool yes, const std::string &message) { if(!yes) throw std::runtime_error(message); }
int mod(int x) { x%=P; return x<0?x+P:x; }
template<class C> void json_ints(std::ostream &f,const C &values) {
    f<<'['; bool first=true; for(auto v:values) {if(!first)f<<','; first=false; f<<v;} f<<']';
}
void words(int depth,int phase,const Vec &coeff,int last) {
    ++words_by_length[depth]; ++raw_by_phase[phase]; formal_sets[phase].insert(coeff);
    if(depth==4) return;
    for(int k=0;k<10;++k) {
        if(last>=0 && k==(last^1)) continue;
        Vec next{}; for(int j=0;j<4;++j) next[j]=(coeff[j]*rp[arcs[k].phase]+arcs[k].coeff[j])%P;
        words(depth+1,(phase+arcs[k].phase)%M,next,k);
    }
}
struct Mask {
    uint64_t lo=0,hi=0;
    void add(int x) {if(x<64)lo|=uint64_t(1)<<x;else hi|=uint64_t(1)<<(x-64);}
    bool full()const {return lo==UINT64_MAX && hi==((uint64_t(1)<<37)-1);}
    int count()const {return __builtin_popcountll(lo)+__builtin_popcountll(hi);}
    bool has(int x)const {return x<64?((lo>>x)&1):((hi>>(x-64))&1);}
};
Mask evaluate(int phase,const Vec &v) {
    Mask mask;
    for(const Vec &f:forms[phase]) {
        const int x=(f[0]*v[0]+f[1]*v[1]+f[2]*v[2]+f[3]*v[3])%P;
        mask.add(x);
        if(mask.full()) break;
    }
    return mask;
}
void witness_json(std::ostream &f,const Vec &v,int phase,const Mask &mask,
                  uint64_t ordinal,const std::string &chart) {
    f<<"{\"ordinal\":"<<ordinal<<",\"chart\":\""<<chart<<"\",\"coefficients_BCDE\":";
    json_ints(f,v); f<<",\"phase\":"<<phase<<",\"endpoint_count\":"<<mask.count()<<",\"missing\":[";
    bool first=true;for(int x=0;x<P;++x)if(!mask.has(x)){if(!first)f<<',';first=false;f<<x;}f<<"]}";
}
std::string make_witness(const Vec &v,int phase,const Mask &mask,uint64_t ordinal,const std::string &chart) {
    std::ostringstream s; witness_json(s,v,phase,mask,ordinal,chart);return s.str();
}
void save_forms() {
    std::ofstream f(out/"forms.json");
    f<<"{\"m\":25,\"p\":101,\"r\":25,\"coefficient_order\":[\"B\",\"C\",\"D\",\"E\"],\"raw_words_by_length\":";
    json_ints(f,words_by_length);f<<",\"raw_words_by_phase\":";json_ints(f,raw_by_phase);
    f<<",\"formal_capacity_by_phase\":[";
    for(int q=0;q<M;++q){if(q)f<<',';f<<forms[q].size();}f<<"],\"forms_by_phase\":[";
    for(int q=0;q<M;++q){if(q)f<<',';f<<'[';bool first=true;for(const auto &v:forms[q]){if(!first)f<<',';first=false;json_ints(f,v);}f<<']';}f<<"]}\n";
}
void prepare() {
    rp[0]=1;for(int j=1;j<M;++j)rp[j]=rp[j-1]*R%P;
    require(rp[M-1]*R%P==1 && rp[5]!=1,"action does not have order25");
    for(int a=0;a<5;++a) {
        Vec v{};if(a)v[a-1]=1;
        arcs[2*a]={PHASES[a],v};
        int invphase=(M-PHASES[a])%M;Vec iv{};
        for(int j=0;j<4;++j)iv[j]=mod(-v[j]*rp[invphase]);
        arcs[2*a+1]={invphase,iv};
    }
    words(0,0,Vec{},-1);
    require(words_by_length==std::array<int,5>{1,10,90,810,7290},"reduced word count mismatch");
    for(int q=0;q<M;++q)forms[q].assign(formal_sets[q].begin(),formal_sets[q].end());
    require(forms[10].size()==308,"phase10 formal capacity differs from frozen308");
    save_forms();
}
std::array<int,M> coverage(const Vec &v) {
    std::array<int,M> c{};for(int q=0;q<M;++q)c[q]=evaluate(q,v).count();return c;
}
void export_hit(const Vec &v,uint64_t ordinal,const std::string &chart) {
    std::set<std::pair<int,int>> edges;
    for(int i=0;i<M;++i)for(int x=0;x<P;++x) {
        const int u=i*P+x;
        for(const Arc &a:arcs) {
            int b=0;for(int j=0;j<4;++j)b+=a.coeff[j]*v[j];b%=P;
            int w=((i+a.phase)%M)*P+(x*rp[a.phase]+b)%P;
            require(u!=w,"unexpected loop");edges.insert(std::minmax(u,w));
        }
    }
    require(edges.size()==12625,"unexpected edge count");
    std::ofstream g(out/"first_hit.edges");g<<2525<<' '<<edges.size()<<'\n';for(auto [u,w]:edges)g<<u<<' '<<w<<'\n';
    std::ofstream f(out/"first_hit.json");
    f<<"{\"status\":\"PRODUCER_EXACT_ENDPOINT_HIT_ROOT_CHECK_PENDING\",\"n\":2525,\"m_edges\":12625,\"degree\":10,\"target_diameter\":4,\"actual_diameter\":null,\"saved_lower_bound\":2485,\"group_m\":25,\"p\":101,\"r\":25,\"right_law\":\"(i,x)(j,y)=(i+j mod25,x*25^j+y mod101)\",\"vertex_encoding\":\"phase*101+x\",\"ordinal\":"<<ordinal<<",\"chart\":\""<<chart<<"\",\"coefficients_BCDE\":";
    json_ints(f,v);f<<",\"positive_generators\":[";
    for(int j=0;j<5;++j){if(j)f<<',';f<<'['<<PHASES[j]<<','<<(j?v[j-1]:0)<<']';}
    f<<"],\"endpoint_counts_by_phase\":";json_ints(f,coverage(v));f<<",\"edge_file\":\"first_hit.edges\"}\n";
}
int main(int argc,char **argv) {
    began=double(std::clock())/CLOCKS_PER_SEC;
    double budget=58;bool diagnostic=false;Vec one{};out=".";
    for(int j=1;j<argc;++j) {
        std::string s=argv[j];
        if(s=="--out" && j+1<argc)out=argv[++j];
        else if(s=="--budget" && j+1<argc)budget=std::stod(argv[++j]);
        else if(s=="--onecoeff" && j+4<argc){diagnostic=true;for(int k=0;k<4;++k)one[k]=std::stoi(argv[++j]);}
        else throw std::runtime_error("unknown/incomplete argument: "+s);
    }
    std::filesystem::create_directories(out);
    try {
        prepare();
        Vec control={18,81,76,1};auto control_counts=coverage(control);
        int control_missing=0;for(int c:control_counts)control_missing+=P-c;
        require(control_missing==66,"quadratic r25 control expected66 missing");
        {std::ofstream f(out/"control.json");f<<"{\"coefficients_BCDE\":";json_ints(f,control);f<<",\"endpoint_counts_by_phase\":";json_ints(f,control_counts);f<<",\"identity_root_missing\":"<<control_missing<<"}\n";}
        if(diagnostic) {
            for(int x:one)require(0<=x && x<P,"coefficient outside0..100");
            auto c=coverage(one);int miss=0;for(int z:c)miss+=P-z;
            std::ofstream f(out/"onecoeff.json");f<<"{\"coefficients_BCDE\":";json_ints(f,one);f<<",\"endpoint_counts_by_phase\":";json_ints(f,c);f<<",\"identity_root_missing\":"<<miss<<",\"CPU_seconds\":"<<elapsed()<<"}\n";
            std::cout<<"onecoeff root_missing="<<miss<<" CPU="<<elapsed()<<'\n';return 0;
        }
        std::array<uint64_t,M> firstfailed{};std::array<std::string,M> witnesses;
        uint64_t checked=0,thinfull=0,hits=0;std::string firstthin="null",status="RUNNING";
        double prep_cpu=elapsed(),scan_start=prep_cpu,profile_cpu=0,forecast=0;
        bool stop=false;
        auto candidate=[&](const Vec &v,const std::string &chart) {
            if(stop)return;
            if(elapsed()>=budget){status="BUDGET_UNKNOWN";stop=true;return;}
            ++checked;Mask thin=evaluate(10,v);int failed=-1;Mask bad=thin;
            if(!thin.full())failed=10;
            else {
                ++thinfull;if(firstthin=="null")firstthin=make_witness(v,10,thin,checked,chart);
                for(int q=0;q<M;++q)if(q!=10){Mask m=evaluate(q,v);if(!m.full()){failed=q;bad=m;break;}}
            }
            if(failed>=0){++firstfailed[failed];if(witnesses[failed].empty())witnesses[failed]=make_witness(v,failed,bad,checked,chart);}
            else {++hits;export_hit(v,checked,chart);status="FIRST_HIT_STOP";stop=true;}
            if(checked==1000 && !stop) {
                profile_cpu=elapsed()-scan_start;forecast=prep_cpu+profile_cpu*double(TOTAL)/1000.0;
                std::ofstream f(out/"profile1000.json");f<<"{\"evaluated_candidates\":1000,\"scan_CPU_seconds\":"<<profile_cpu<<",\"preparation_CPU_seconds\":"<<prep_cpu<<",\"projected_complete_native_CPU_seconds\":"<<forecast<<",\"native_budget_CPU_seconds\":"<<budget<<",\"thin_phase_full\":"<<thinfull<<"}\n";
                std::cout<<"profile1000 CPU="<<profile_cpu<<" forecast="<<forecast<<" thinfull="<<thinfull<<std::endl;
                if(forecast>budget-0.25){status="PROFILE_UNKNOWN";stop=true;}
            }
        };
        for(int b=0;b<P && !stop;++b)for(int c=0;c<P && !stop;++c)for(int d=0;d<P && !stop;++d)candidate({b,c,d,1},"E1");
        for(int b=0;b<P && !stop;++b)for(int c=0;c<P && !stop;++c)candidate({b,c,1,0},"E0_D1");
        for(int b=0;b<P && !stop;++b)candidate({b,1,0,0},"E0_D0_C1");
        if(!stop)candidate({1,0,0,0},"E0_D0_C0_B1");
        if(checked==TOTAL && !hits)status="COMPLETE_NO_HIT";
        bool complete=(checked==TOTAL);
        std::ofstream f(out/"terminal.json");f<<std::setprecision(12);
        f<<"{\"status\":\""<<status<<"\",\"complete_space\":"<<(complete?"true":"false")<<",\"total_projective_charts\":"<<TOTAL<<",\"evaluated_candidates\":"<<checked<<",\"untested_candidates\":"<<TOTAL-checked<<",\"cursor_next_ordinal\":"<<checked+1<<",\"thin_phase\":10,\"thin_phase_full\":"<<thinfull<<",\"full_hits\":"<<hits<<",\"first_failed_phase_counts\":";
        json_ints(f,firstfailed);f<<",\"first_failure_witness_by_phase\":[";for(int q=0;q<M;++q){if(q)f<<',';f<<(witnesses[q].empty()?"null":witnesses[q]);}
        f<<"],\"first_thin_phase_passer\":"<<firstthin<<",\"CPU_seconds\":"<<elapsed()<<",\"preparation_CPU_seconds\":"<<prep_cpu<<",\"profile1000_scan_CPU_seconds\":"<<profile_cpu<<",\"profile_projected_native_CPU_seconds\":"<<forecast<<",\"native_budget_CPU_seconds\":"<<budget<<",\"actual_graph_order\":"<<(hits?"2525":"null")<<",\"actual_diameter\":null,\"old_source_BFS\":0}\n";
        std::cout<<status<<" evaluated="<<checked<<" thinfull="<<thinfull<<" hits="<<hits<<" CPU="<<elapsed()<<std::endl;
    } catch(const std::exception &e) {
        std::ofstream f(out/"error.txt");f<<e.what()<<'\n';std::cerr<<e.what()<<'\n';return 1;
    }
}

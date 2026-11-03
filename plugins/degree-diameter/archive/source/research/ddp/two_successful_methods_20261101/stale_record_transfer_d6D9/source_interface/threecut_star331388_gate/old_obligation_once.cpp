#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

constexpr int P=6763,H=49,N=P*H;
const int phase[6]={25,24,18,31,47,2},normal[6]={1254,2125,541,3289,4642,1300};
int power49[49];double budget;std::string stage="cachedinput";
double cpu(){return double(std::clock())/CLOCKS_PER_SEC;}
void check(){if(cpu()>budget)throw std::runtime_error("CPU_BUDGET_STOP_"+stage);}
int mul(int a,int b){return ((a/P+b/P)%49)*P+int((1LL*(a%P)*power49[b/P]+b%P)%P);}
int inv(int a){int j=(49-a/P)%49;return j*P+int((P-1LL*(a%P)*power49[j]%P)%P);}
int gen(int t){return phase[2*t]*P+normal[2*t];}
int neighbor(int a,int k){return ((a/P+phase[k])%49)*P+int((1LL*(a%P)*power49[phase[k]]+normal[k])%P);}
template<class T>std::vector<T>read(const std::string&path){std::ifstream f(path,std::ios::binary|std::ios::ate);if(!f)throw std::runtime_error("cachedfile_missing");auto n=f.tellg();if(n%sizeof(T))throw std::runtime_error("cachedfile_shape");std::vector<T>v(std::size_t(n)/sizeof(T));f.seekg(0);f.read(reinterpret_cast<char*>(v.data()),n);return v;}
template<class V>void arr(std::ostream&o,const V&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<static_cast<unsigned long long>(x);}o<<']';}
struct Edge{int h=0,type=0,v=0;};
bool disjoint(const Edge&a,const Edge&b){return a.h!=b.h&&a.h!=b.v&&a.v!=b.h&&a.v!=b.v;}
bool same(const Edge&a,const Edge&b){return (a.h==b.h&&a.v==b.v)||(a.h==b.v&&a.v==b.h);}
void edgejson(std::ostream&o,const Edge&e){o<<"{\"h\":"<<e.h<<",\"type\":"<<e.type<<",\"endpoints\":["<<e.h<<','<<e.v<<"]}";}
struct Pair{int u=0,w=0,v=0,a=0,b=0;};
struct Class{std::uint64_t mask=0,count=0;int pop=0;std::vector<Edge>reps;};
struct Post{
    bool present=false;std::array<Edge,3>cuts;std::vector<int>pins;
    std::uint64_t newroot_misses=0;int first_newroot_miss=-1;std::vector<int>newroot_path;
    std::array<std::uint64_t,3>critical_examined{},critical_failed{};
    bool oldfail=false;int failed_cut=-1,u=0,v=0,du=0,dv=0;std::uint32_t total=0,left=0,right=0;std::vector<int>old9,new10;
};
struct Result{
    int type=0,critical=0;std::uint64_t scanned=0,excluded=0,admissible=0,classes=0,zero_count=0;
    int maxpop=0;std::uint64_t possible_maskpairs=0,bound_skipped=0,OR_checks=0,OR_full=0,rep_checks=0;
    bool strictmax=false,found=false,complete=false;Edge e1,e2;Post post;
};
std::vector<int>cached4(int index,const std::vector<std::uint32_t>&paths){std::vector<int>r;for(int j=0;j<5;++j)r.push_back(paths[5*index+j]);return r;}
std::vector<int>rootpath(int v,const std::vector<std::uint8_t>&d){std::vector<int>r{v};while(v){int next=-1;for(int k=0;k<6;++k){int q=neighbor(v,k);if(d[q]+1==d[v]&&(next<0||q<next))next=q;}if(next<0)throw std::runtime_error("cacheddistance_predecessor_missing");v=next;r.push_back(v);}std::reverse(r.begin(),r.end());return r;}
int nearest(int x,const std::vector<int>&inversepins,const std::vector<std::uint8_t>&d){int best=9;for(int p:inversepins)best=std::min(best,int(d[mul(p,x)]));return best;}

Post postcheck(int firsttype,const Edge&a,const Edge&b,const std::array<std::vector<Pair>,3>&relations,
               const std::array<std::vector<std::uint8_t>,3>&miss,const std::vector<std::uint8_t>&d,
               const std::vector<std::uint32_t>&counts,const std::vector<std::uint32_t>&paths){
    Post r;r.present=true;r.cuts={Edge{0,firsttype,gen(firsttype)},a,b};std::set<int>pinset;
    for(auto e:r.cuts){pinset.insert(e.h);pinset.insert(e.v);}if(pinset.size()!=6)throw std::runtime_error("triple_not_sixdistinct");r.pins.assign(pinset.begin(),pinset.end());
    std::array<int,3>hi{};for(int i=0;i<3;++i)hi[i]=inv(r.cuts[i].h);
    stage="firsttriple_exact_missing_intersection_no_BFS";
    for(int v=0;v<N;++v){if((v&32767)==0)check();bool hit=true;for(int i=0;i<3;++i)hit=hit&&miss[r.cuts[i].type][mul(hi[i],v)];if(hit){++r.newroot_misses;if(r.first_newroot_miss<0)r.first_newroot_miss=v;}}
    std::vector<int>inversepins;for(int p:r.pins)inversepins.push_back(inv(p));
    if(r.first_newroot_miss>=0){int p=r.pins[0],relative=mul(inv(p),r.first_newroot_miss);auto rp=rootpath(relative,d);r.newroot_path.push_back(N);for(int x:rp)r.newroot_path.push_back(mul(p,x));if(r.newroot_path.size()!=11)throw std::runtime_error("newroot10_length");}
    stage="firsttriple_othercuts_critical_obligations";
    for(int i=0;i<3;++i)for(auto pair:relations[r.cuts[i].type]){
        int u=mul(r.cuts[i].h,pair.u),v=mul(r.cuts[i].h,pair.v);
        int du=nearest(u,inversepins,d),dv=nearest(v,inversepins,d);++r.critical_examined[i];
        if(du+dv>7){++r.critical_failed[i];if(!r.oldfail){
            r.oldfail=true;r.failed_cut=i;r.u=u;r.v=v;r.du=du;r.dv=dv;
            r.total=counts[mul(inv(pair.u),pair.v)];r.left=counts[inv(pair.u)];r.right=counts[pair.w];
            auto pu=cached4(pair.a,paths);std::reverse(pu.begin(),pu.end());pu.push_back(gen(r.cuts[i].type));
            auto pw=cached4(pair.b,paths);for(int j=1;j<5;++j)pu.push_back(mul(gen(r.cuts[i].type),pw[j]));
            for(int x:pu)r.old9.push_back(mul(r.cuts[i].h,x));
            for(std::size_t j=0;j<r.old9.size();++j){r.new10.push_back(r.old9[j]);if(j==4)r.new10.push_back(N);}
            if(du!=4||dv!=4||r.old9.size()!=10||r.new10.size()!=11)throw std::runtime_error("criticalcounter_shape");
        }}
    }
    auto validstarpath=[&](const std::vector<int>&path){for(std::size_t j=1;j<path.size();++j){int x=path[j-1],y=path[j];if(x==N||y==N){if(!pinset.count(x==N?y:x))return false;}else{bool edge=false;for(int k=0;k<6;++k)edge|=neighbor(x,k)==y;if(!edge)return false;for(auto e:r.cuts)if((x==e.h&&y==e.v)||(x==e.v&&y==e.h))return false;}}return true;};
    if(!r.newroot_path.empty()&&!validstarpath(r.newroot_path))throw std::runtime_error("actual_newroot10_path_binding");
    if(r.oldfail&&!validstarpath(r.new10))throw std::runtime_error("actual_oldpair10_path_binding");
    return r;
}

int main(int argc,char**argv){std::string folder=argv[1];budget=std::stod(argv[2]);try{
    power49[0]=1;for(int j=1;j<49;++j)power49[j]=int(41LL*power49[j-1]%P);
    auto d=read<std::uint8_t>(folder+"/PROFILE_IDENTITY_DISTANCE.u8");auto counts=read<std::uint32_t>(folder+"/PROFILE_IDENTITY_SHORTEST_COUNTS.u32");
    auto sphere=read<std::uint32_t>(folder+"/PROFILE_SPHERE4_LABELS.u32");auto paths=read<std::uint32_t>(folder+"/OLD_CACHED_SPHERE4_PATHS.u32");
    if(d.size()!=N||counts.size()!=N||sphere.size()!=750||paths.size()!=5*sphere.size())throw std::runtime_error("cachedsupport_shape");
    std::vector<int>B3;for(int x=0;x<N;++x)if(d[x]<=3)B3.push_back(x);
    std::array<std::vector<Pair>,3>relations;std::array<std::vector<std::uint8_t>,3>miss;
    int stride=(sphere.size()+63)/64;
    for(int t=0;t<3;++t){auto matrix=read<std::uint64_t>(folder+"/PROFILE_CRITICAL_TYPE"+std::to_string(t)+".u64");if(matrix.size()!=sphere.size()*stride)throw std::runtime_error("criticalmatrix_shape");for(int a=0;a<int(sphere.size());++a)for(int k=0;k<stride;++k){auto bits=matrix[std::size_t(a)*stride+k];while(bits){int b=k*64+__builtin_ctzll(bits);bits&=bits-1;if(b>=int(sphere.size()))throw std::runtime_error("criticalpadding_bit");relations[t].push_back(Pair{int(sphere[a]),int(sphere[b]),mul(gen(t),sphere[b]),a,b});}}
        auto labels=read<std::uint32_t>(folder+"/PROFILE_M_TYPE"+std::to_string(t)+"_LABELS.u32");miss[t].assign(N,0);for(int v:labels)miss[t][v]=1;
    }
    std::array<Result,3>results;
    for(int firsttype=0;firsttype<3;++firsttype){
        Result&r=results[firsttype];r.type=firsttype;r.critical=relations[firsttype].size();if(r.critical<1||r.critical>63)throw std::runtime_error("actualcritical_mask_width");
        const std::uint64_t ALL=(1ULL<<r.critical)-1;std::vector<std::uint64_t>vertexmask(N,0);
        stage="critical_vertex_hitmasks_type"+std::to_string(firsttype);
        for(int i=0;i<r.critical;++i)for(int w:B3){vertexmask[mul(relations[firsttype][i].u,w)]|=1ULL<<i;vertexmask[mul(relations[firsttype][i].v,w)]|=1ULL<<i;}
        std::unordered_map<std::uint64_t,Class>grouped;int s=gen(firsttype);
        stage="full_admissible_edge_maskclasses_type"+std::to_string(firsttype);
        for(int h=0;h<N;++h){if((h&16383)==0)check();for(int t=0;t<3;++t){int v=neighbor(h,2*t);++r.scanned;if(h==0||h==s||v==0||v==s){++r.excluded;continue;}++r.admissible;auto mask=vertexmask[h]|vertexmask[v];auto&c=grouped[mask];c.mask=mask;++c.count;if(c.reps.size()<12){Edge e{h,t,v};bool duplicate=false;for(auto old:c.reps)duplicate|=same(e,old);if(duplicate)throw std::runtime_error("duplicate_positive_edge_parameter");c.reps.push_back(e);}}}
        if(r.scanned!=994161||r.excluded!=11||r.admissible!=994150)throw std::runtime_error("admissible_edgepool_binding");
        std::vector<Class>classes;for(auto&entry:grouped){auto c=entry.second;c.pop=__builtin_popcountll(c.mask);r.maxpop=std::max(r.maxpop,c.pop);if(!c.mask)r.zero_count=c.count;classes.push_back(std::move(c));}
        std::sort(classes.begin(),classes.end(),[](const Class&a,const Class&b){return a.pop!=b.pop?a.pop>b.pop:a.mask<b.mask;});r.classes=classes.size();r.possible_maskpairs=r.classes*(r.classes+1)/2;
        {std::ofstream f(folder+"/OLD_TYPE"+std::to_string(firsttype)+"_MASK_CLASSES.tsv");f<<"mask_decimal\tpopcount\tfull_admissible_edge_count\trepresentatives_h_type_endpoint\n";for(auto&c:classes){f<<c.mask<<'\t'<<c.pop<<'\t'<<c.count<<'\t';for(std::size_t j=0;j<c.reps.size();++j){if(j)f<<';';f<<c.reps[j].h<<','<<c.reps[j].type<<','<<c.reps[j].v;}f<<'\n';}}
        r.strictmax=2*r.maxpop<r.critical;
        stage="complete_maskpair_OR_and_real_disjointness_type"+std::to_string(firsttype);
        if(r.strictmax){r.bound_skipped=r.possible_maskpairs;r.complete=true;}
        else for(std::size_t i=0;i<classes.size()&&!r.found;++i){check();for(std::size_t j=i;j<classes.size();++j){if(classes[i].pop+classes[j].pop<r.critical){r.bound_skipped+=classes.size()-j;break;}++r.OR_checks;if((classes[i].mask|classes[j].mask)!=ALL)continue;++r.OR_full;for(auto a:classes[i].reps){for(auto b:classes[j].reps){++r.rep_checks;if(disjoint(a,b)){r.found=true;r.e1=a;r.e2=b;break;}}if(r.found)break;}if(r.found)break;}}
        if(!r.found)r.complete=true;
        if(r.found)r.post=postcheck(firsttype,r.e1,r.e2,relations,miss,d,counts,paths);
    }
    bool allNo=true,anyPass=false;for(auto&r:results){allNo&=!r.found&&r.complete;anyPass|=r.found;}
    std::ofstream f(folder+"/OLD_RAW_RESULT.json");f<<"{\"status\":\""<<(allNo?"COMPLETE_NO_FIXED_SOURCE_MINIMAL_THREECUT_SIXSTAR_BY_OLD_OBLIGATIONS":"OLD_OBLIGATION_BARRIER_PREDICTION_REFUTED_REAL_TRIPLE_FOUND")<<"\",\"B3_cached_label_count\":"<<B3.size()<<",\"source_edge_parameters_each_type\":994161,\"firsttypes\":[";
    for(int i=0;i<3;++i){auto&r=results[i];if(i)f<<',';f<<"{\"first_type\":"<<i<<",\"critical_pair_count\":"<<r.critical<<",\"all_source_positive_edges_scanned\":"<<r.scanned<<",\"base_incident_edges_excluded_before_grouping\":"<<r.excluded<<",\"admissible_edges\":"<<r.admissible<<",\"mask_classes\":"<<r.classes<<",\"zero_mask_edges\":"<<r.zero_count<<",\"maximum_single_edge_obligations_hit\":"<<r.maxpop<<",\"strict_two_edge_cardinality_bound_excludes\":"<<(r.strictmax?"true":"false")<<",\"unordered_maskpair_domain\":"<<r.possible_maskpairs<<",\"maskpairs_skipped_by_strict_bound\":"<<r.bound_skipped<<",\"maskpair_OR_checks\":"<<r.OR_checks<<",\"full_OR_maskpairs\":"<<r.OR_full<<",\"actual_representative_edgepair_checks\":"<<r.rep_checks<<",\"found_real_disjoint_pair\":"<<(r.found?"true":"false")<<",\"complete_necessary_gate_NO\":"<<((!r.found&&r.complete)?"true":"false")<<",\"first_triple\":";
        if(!r.found)f<<"null";else{auto&p=r.post;f<<"{\"cuts\":[";for(int j=0;j<3;++j){if(j)f<<',';edgejson(f,p.cuts[j]);}f<<"],\"sixpins\":";arr(f,p.pins);f<<",\"exact_newroot_R9_missing_count\":"<<p.newroot_misses<<",\"first_newroot_badlabel\":"<<p.first_newroot_miss<<",\"actual_newroot10_path\":";arr(f,p.newroot_path);f<<",\"critical_examined_by_cut\":";arr(f,p.critical_examined);f<<",\"critical_failed_by_cut\":";arr(f,p.critical_failed);f<<",\"first_othercut_counterexample\":";if(!p.oldfail)f<<"null";else{f<<"{\"cut_index\":"<<p.failed_cut<<",\"u\":"<<p.u<<",\"v\":"<<p.v<<",\"duP\":"<<p.du<<",\"dvP\":"<<p.dv<<",\"source9_geodesics_total\":"<<p.total<<",\"left4_count\":"<<p.left<<",\"right4_count\":"<<p.right<<",\"actual_old9_path\":";arr(f,p.old9);f<<",\"actual_star10_path\":";arr(f,p.new10);f<<",\"implicit_newdistance\":10}";}f<<",\"postfilter_failure_not_a_class_NO\":true}";}
        f<<'}';
    }
    f<<"],\"all_three_firsttypes_NO\":"<<(allNo?"true":"false")<<",\"barrier_prediction_supported\":"<<(allNo?"true":"false")<<",\"any_real_triple_meets_firstcut_obligations\":"<<(anyPass?"true":"false")<<",\"new_BFS_DP_or_source_validity_checks\":0,\"candidate_graphs_generated\":0,\"native_CPU_seconds\":"<<cpu()<<"}\n";
    std::cout<<"OLD_GATE_COMPLETE all3NO="<<allNo<<" anyPASS="<<anyPass<<" CPU="<<cpu()<<'\n';return 0;
}catch(const std::exception&e){std::ofstream f(folder+"/OLD_RAW_RESULT.json");f<<"{\"status\":\"UNKNOWN_OLD_OBLIGATION_GATE_STOP\",\"stage\":\""<<stage<<"\",\"error\":\""<<e.what()<<"\",\"native_CPU_seconds\":"<<cpu()<<"}\n";std::cerr<<e.what()<<'\n';return 2;}}

#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

constexpr int MOD=6763, PH=49, N=MOD*PH;
const int phases[6]={25,24,18,31,47,2};
const int normals[6]={1254,2125,541,3289,4642,1300};
int powers[PH];
double budget;
std::string stage="input";
double cpu(){return double(std::clock())/CLOCKS_PER_SEC;}
void check(){if(cpu()>budget)throw std::runtime_error("CPU_BUDGET_STOP_"+stage);}
int mul(int u,int v){return ((u/MOD+v/MOD)%PH)*MOD+int((1LL*(u%MOD)*powers[v/MOD]+v%MOD)%MOD);}
int inv(int u){int j=(PH-u/MOD)%PH;return j*MOD+int((MOD-1LL*(u%MOD)*powers[j]%MOD)%MOD);}
int gen(int k){return phases[k]*MOD+normals[k];}
int neighbor(int u,int k){int j=u/MOD+phases[k];if(j>=PH)j-=PH;return j*MOD+int((1LL*(u%MOD)*powers[phases[k]]+normals[k])%MOD);}
template<class T>void binary(const std::string&name,const std::vector<T>&v){std::ofstream f(name,std::ios::binary);f.write(reinterpret_cast<const char*>(v.data()),std::streamsize(v.size()*sizeof(T)));}
template<class T>void arr(std::ostream&o,const T&v){o<<'[';bool first=true;for(auto x:v){if(!first)o<<',';first=false;o<<static_cast<unsigned long long>(x);}o<<']';}
std::vector<int> rootpath(int u,const std::vector<int>&parent){std::vector<int>p;while(u){p.push_back(u);u=parent[u];}p.push_back(0);std::reverse(p.begin(),p.end());return p;}
struct W{bool exists=false;int u=0,w=0,v=0,relative=0;std::uint32_t total=0,left=0,right=0;std::vector<int>path;};
void witness(std::ostream&o,const W&w){if(!w.exists){o<<"null";return;}o<<"{\"u\":"<<w.u<<",\"w\":"<<w.w<<",\"v_s_times_w\":"<<w.v<<",\"u_inverse_v\":"<<w.relative<<",\"distance\":9,\"total_shortest_count\":"<<w.total<<",\"left4_count\":"<<w.left<<",\"right4_count\":"<<w.right<<",\"actual_old9_path\":";arr(o,w.path);o<<'}';}
std::uint64_t rotate49(std::uint64_t x,int shift){constexpr std::uint64_t full=(1ULL<<49)-1;if(!shift)return x;return ((x<<shift)|(x>>(49-shift)))&full;}

int main(int argc,char**argv){
    const std::string out=argv[1];budget=std::stod(argv[2]);
    try{
        powers[0]=1;for(int j=1;j<PH;++j)powers[j]=int(41LL*powers[j-1]%MOD);
        for(int k=0;k<6;++k)if(mul(gen(k),gen(k^1))||mul(gen(k^1),gen(k)))throw std::runtime_error("literal_inverse_binding_failed");
        stage="one_identity_R8_support";
        std::vector<std::uint8_t>d(N,9);std::vector<int>parent(N,-1),queue;queue.reserve(N);
        d[0]=0;parent[0]=0;queue.push_back(0);
        for(std::size_t head=0;head<queue.size();++head){
            if((head&16383)==0)check();int u=queue[head];if(d[u]==8)continue;
            for(int k=0;k<6;++k){int v=neighbor(u,k);if(d[v]==9){d[v]=d[u]+1;parent[v]=u;queue.push_back(v);}}
        }
        stage="shortest_count_DP_using_measured_distances_and_inherited9";
        std::vector<std::uint32_t>count(N,0);count[0]=1;
        for(std::size_t index=0;index<queue.size();++index){
            if((index&16383)==0)check();int u=queue[index];
            for(int k=0;k<6;++k){int v=neighbor(u,k);if(d[v]==d[u]+1)count[v]+=count[u];}
        }
        std::array<std::uint32_t,10>hist{};std::uint32_t max_count=0,zero_count=0;
        std::vector<std::uint32_t>sphere;
        for(int v=0;v<N;++v){++hist[d[v]];max_count=std::max(max_count,count[v]);zero_count+=count[v]==0;if(d[v]==4)sphere.push_back(v);}
        binary(out+"/PROFILE_IDENTITY_DISTANCE.u8",d);binary(out+"/PROFILE_IDENTITY_SHORTEST_COUNTS.u32",count);
        binary(out+"/PROFILE_SPHERE4_LABELS.u32",sphere);
        {std::ofstream f(out+"/PROFILE_SPHERE4_PATHS.json");f<<"{\"paths_from_identity\":[";for(std::size_t i=0;i<sphere.size();++i){if(i)f<<',';f<<"{\"target\":"<<sphere[i]<<",\"path\":";arr(f,rootpath(sphere[i],parent));f<<'}';}f<<"]}\n";}
        std::array<std::vector<std::uint8_t>,3>miss;
        std::array<std::vector<std::uint32_t>,3>missing_labels;
        std::array<std::array<std::uint32_t,49>,3>phase_count{};
        std::array<std::uint64_t,3>phase_support{};
        stage="three_M_sets_from_shared_identity_support_no_BFS";
        for(int type=0;type<3;++type){
            miss[type].assign(N,0);int si=gen(2*type+1);
            for(int v=0;v<N;++v){if((v&16383)==0)check();if(d[v]==9&&d[mul(si,v)]==9){miss[type][v]=1;missing_labels[type].push_back(v);++phase_count[type][v/MOD];phase_support[type]|=1ULL<<(v/MOD);}}
            binary(out+"/PROFILE_M_TYPE"+std::to_string(type)+"_LABELS.u32",missing_labels[type]);
        }
        const int sphere_n=int(sphere.size()),stride=(sphere_n+63)/64;
        std::array<std::vector<std::uint64_t>,3>critical;
        std::array<std::uint64_t,3>critical_count{};std::array<W,3>first{};
        stage="complete_4plus1plus4_critical_relation";
        for(int type=0;type<3;++type){
            critical[type].assign(std::size_t(sphere_n)*stride,0);int s=gen(2*type);
            for(int a=0;a<sphere_n;++a){
                if((a&31)==0)check();int u=sphere[a],ui=inv(u);
                for(int b=0;b<sphere_n;++b){
                    int w=sphere[b],v=mul(s,w),relative=mul(ui,v);
                    std::uint64_t factor=std::uint64_t(count[ui])*count[w];
                    if(d[relative]==9&&factor>0&&count[relative]==factor){
                        critical[type][std::size_t(a)*stride+b/64]|=1ULL<<(b%64);++critical_count[type];
                        if(!first[type].exists){
                            W&z=first[type];z.exists=true;z.u=u;z.w=w;z.v=v;z.relative=relative;
                            z.total=count[relative];z.left=count[ui];z.right=count[w];
                            z.path=rootpath(u,parent);std::reverse(z.path.begin(),z.path.end());z.path.push_back(s);
                            auto pw=rootpath(w,parent);for(std::size_t j=1;j<pw.size();++j)z.path.push_back(mul(s,pw[j]));
                            if(z.path.size()!=10)throw std::runtime_error("old9_witness_length_mismatch");
                            for(std::size_t j=1;j<z.path.size();++j){bool edge=false;for(int k=0;k<6;++k)edge|=neighbor(z.path[j-1],k)==z.path[j];if(!edge)throw std::runtime_error("old9_witness_edge_mismatch");}
                        }
                    }
                }
            }
            binary(out+"/PROFILE_CRITICAL_TYPE"+std::to_string(type)+".u64",critical[type]);
        }
        stage="all64827_phase_support_tuples";
        std::uint64_t phase_domain=0,phase_hits=0;std::array<std::uint64_t,50>common_hist{};
        std::array<int,3>selected_types{};std::array<int,3>selected_phases{};
        {std::ofstream f(out+"/PROFILE_ALL_PHASE_TUPLES.tsv");f<<"type0\ttype1\ttype2\tphase1\tphase2\tcommon_phase_count\tfirst_common_phase\n";
            for(int a=0;a<3;++a)for(int b=0;b<3;++b)for(int c=0;c<3;++c)for(int j=0;j<49;++j)for(int k=0;k<49;++k){
                std::uint64_t common=phase_support[a]&rotate49(phase_support[b],j)&rotate49(phase_support[c],k);
                int n=__builtin_popcountll(common);++phase_domain;++common_hist[n];
                f<<a<<'\t'<<b<<'\t'<<c<<'\t'<<j<<'\t'<<k<<'\t'<<n<<'\t'<<(common?__builtin_ctzll(common):-1)<<'\n';
                if(!common){if(!phase_hits){selected_types={a,b,c};selected_phases={0,j,k};}++phase_hits;}
            }
        }
        check();
        bool selected=false;std::array<int,3>bases{};std::vector<int>pins;std::array<std::array<int,2>,3>cuts{};
        std::array<std::uint64_t,3>filter_examined{},filter_failed{};bool fail_witness=false;
        int fail_cut=-1,fail_u=0,fail_v=0,fail_du=0,fail_dv=0;std::vector<int>fail_oldpath,fail_newpath;
        std::uint64_t actual_missing_intersection=0;
        if(phase_hits){
            selected=true;std::set<int>used;
            for(int i=0;i<3;++i){bool found=false;for(int n=0;n<9;++n){int h=selected_phases[i]*MOD+n,hs=mul(h,gen(2*selected_types[i]));if(!used.count(h)&&!used.count(hs)){bases[i]=h;cuts[i]={h,hs};used.insert(h);used.insert(hs);found=true;break;}}if(!found)throw std::runtime_error("smallnormal_disjointness_choice_failed");}
            pins.assign(used.begin(),used.end());if(pins.size()!=6)throw std::runtime_error("sixdistinct_pins_failed");
            std::array<int,3>base_inv{};for(int i=0;i<3;++i)base_inv[i]=inv(bases[i]);
            for(int v=0;v<N;++v){if((v&16383)==0)check();bool all=true;for(int i=0;i<3;++i)all=all&&miss[selected_types[i]][mul(base_inv[i],v)];actual_missing_intersection+=all;}
            if(actual_missing_intersection)throw std::runtime_error("phase_certificate_disagrees_with_fullmissing_intersection");
            stage="selected_sixpin_translated_critical_filter_no_BFS";
            std::vector<std::uint8_t>nearest(N,9);for(int v=0;v<N;++v){if((v&16383)==0)check();for(int p:pins)nearest[v]=std::min(nearest[v],d[mul(inv(p),v)]);}
            for(int i=0;i<3;++i){int type=selected_types[i],h=bases[i],s=gen(2*type);
                for(int a=0;a<sphere_n;++a){if((a&31)==0)check();for(int word=0;word<stride;++word){auto bits=critical[type][std::size_t(a)*stride+word];while(bits){int bit=__builtin_ctzll(bits),b=word*64+bit;bits&=bits-1;int u=mul(h,sphere[a]),v=mul(h,mul(s,sphere[b]));++filter_examined[i];if(nearest[u]+nearest[v]>7){++filter_failed[i];if(!fail_witness){fail_witness=true;fail_cut=i;fail_u=u;fail_v=v;fail_du=nearest[u];fail_dv=nearest[v];auto pu=rootpath(sphere[a],parent);std::reverse(pu.begin(),pu.end());pu.push_back(s);auto pw=rootpath(sphere[b],parent);for(std::size_t j=1;j<pw.size();++j)pu.push_back(mul(s,pw[j]));for(int x:pu)fail_oldpath.push_back(mul(h,x));for(std::size_t j=0;j<fail_oldpath.size();++j){fail_newpath.push_back(fail_oldpath[j]);if(j+1<fail_oldpath.size()&&j==4)fail_newpath.push_back(N);}for(std::size_t j=1;j<fail_newpath.size();++j){int x=fail_newpath[j-1],y=fail_newpath[j];if(x==N||y==N){if(!used.count(x==N?y:x))throw std::runtime_error("star10_witness_pin_mismatch");}else{for(auto e:cuts)if((x==e[0]&&y==e[1])||(x==e[1]&&y==e[0]))throw std::runtime_error("star10_witness_uses_deletededge");}}}}}}}
            }
        }
        std::ofstream f(out+"/PROFILE_RAW_RESULT.json");
        f<<"{\"status\":\"COMPLETE_NEW_SUPPORT_AND_PHASE_CRITICAL_PROFILE\",\"new_question_support_BFS_roots\":1,\"support_depth\":8,\"source_D9_validity_BFS_roots\":0,\"measured_identity_B8_size\":"<<queue.size()<<",\"distance_histogram_with_inherited9\":";arr(f,hist);
        f<<",\"sphere4_size\":"<<sphere_n<<",\"maximum_shortest_word_count\":"<<max_count<<",\"zero_shortest_count_entries\":"<<zero_count<<",\"critical_u64_stride\":"<<stride<<",\"types\":[";
        for(int i=0;i<3;++i){if(i)f<<',';f<<"{\"type\":"<<i<<",\"positive_generator\":["<<phases[2*i]<<','<<normals[2*i]<<"],\"M_count\":"<<missing_labels[i].size()<<",\"M_phase_counts\":";arr(f,phase_count[i]);f<<",\"M_phase_support_size\":"<<__builtin_popcountll(phase_support[i])<<",\"M_phase_support_u64\":"<<phase_support[i]<<",\"critical_pair_count\":"<<critical_count[i]<<",\"first_critical\":";witness(f,first[i]);f<<'}';}
        f<<"],\"phase_domain_count\":"<<phase_domain<<",\"phase_empty_intersections\":"<<phase_hits<<",\"phase_common_size_histogram\":";arr(f,common_hist);
        f<<",\"phase_prediction_supported\":"<<(phase_hits?"true":"false")<<",\"critical_each_type_prediction_supported\":"<<((first[0].exists&&first[1].exists&&first[2].exists)?"true":"false")<<",\"selected_sixpin_certificate\":";
        if(!selected)f<<"null";else{f<<"{\"types\":";arr(f,selected_types);f<<",\"base_phases\":";arr(f,selected_phases);f<<",\"base_labels\":";arr(f,bases);f<<",\"sixpins\":";arr(f,pins);f<<",\"full_translated_missing_intersection_size\":"<<actual_missing_intersection<<",\"newroot_R9_exact_gate_pass\":true,\"translated_critical_examined_by_cut\":";arr(f,filter_examined);f<<",\"translated_critical_failed_by_cut\":";arr(f,filter_failed);f<<",\"first_old_bottleneck\":";if(!fail_witness)f<<"null";else{f<<"{\"cut_index\":"<<fail_cut<<",\"u\":"<<fail_u<<",\"v\":"<<fail_v<<",\"dist_u_P\":"<<fail_du<<",\"dist_v_P\":"<<fail_dv<<",\"actual_old9_path\":";arr(f,fail_oldpath);f<<",\"actual_implicit_star10_path\":";arr(f,fail_newpath);f<<",\"new_pair_distance\":10,\"lower_basis\":\"all_source9geodesics_use_cut_and_pin_distance_sum8\"}";}f<<'}';}
        f<<",\"candidate_graphs_generated\":0,\"u_v_BFS_queries\":0,\"native_CPU_seconds\":"<<cpu()<<"}\n";
        std::cout<<"PROFILE_COMPLETE sphere4="<<sphere_n<<" critical="<<critical_count[0]<<','<<critical_count[1]<<','<<critical_count[2]<<" phaseempty="<<phase_hits<<" CPU="<<cpu()<<'\n';
        return 0;
    }catch(const std::exception&e){std::ofstream f(out+"/PROFILE_RAW_RESULT.json");f<<"{\"status\":\"UNKNOWN_NATIVE_PROFILE_STOP\",\"stage\":\""<<stage<<"\",\"error\":\""<<e.what()<<"\",\"native_CPU_seconds\":"<<cpu()<<"}\n";std::cerr<<e.what()<<'\n';return 2;}
}

#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using Edge=std::array<int,2>;
using Adj=std::array<std::array<int,4>,365>;
struct Config{std::array<int,2>cuts;std::array<Edge,14>matching;};
struct BFS{int root,target,distance,reached,ecc;std::array<int,365>d;std::vector<int>path;};
static double cpu(){return double(std::clock())/CLOCKS_PER_SEC;}
template<size_t N> static std::string arr(const std::array<int,N>&a){std::ostringstream o;o<<'[';for(size_t i=0;i<N;++i){if(i)o<<',';o<<a[i];}return o.str()+']';}
static std::string pathjson(const std::vector<int>&a){std::ostringstream o;o<<'[';for(size_t i=0;i<a.size();++i){if(i)o<<',';o<<a[i];}return o.str()+']';}
static std::string cfgjson(const Config&c,const std::vector<Edge>&core){std::ostringstream o;o<<"{\"core_cut_pool_indices\":"<<arr(c.cuts)<<",\"core_cut_edges\":["<<arr(core[c.cuts[0]])<<','<<arr(core[c.cuts[1]])<<"],\"port_matching\":[";for(int i=0;i<14;++i){if(i)o<<',';o<<arr(c.matching[i]);}return o.str()+"]}";}
static BFS bfs(const Adj&a,int root){
    std::array<int,365>d,par,q;d.fill(-1);par.fill(-1);d[root]=0;q[0]=root;int head=0,tail=1;
    while(head<tail){int u=q[head++];for(int v:a[u])if(d[v]<0){d[v]=d[u]+1;par[v]=u;q[tail++]=v;}}
    int target=-1,ecc=0;for(int v=0;v<365;++v){ecc=std::max(ecc,d[v]);if(target<0&&(d[v]<0||d[v]>5))target=v;}
    if(target<0)for(int v=0;v<365;++v)if(d[v]==ecc){target=v;break;}
    std::vector<int>path;if(d[target]>=0){for(int v=target;v>=0;v=par[v])path.push_back(v);std::reverse(path.begin(),path.end());}
    return{root,target,d[target],tail,ecc,d,path};
}
static bool pass(const BFS&b){return b.reached==365&&b.ecc<=5;}
static std::string bfsjson(const BFS&b){std::ostringstream o;o<<"{\"root\":"<<b.root<<",\"target\":"<<b.target<<",\"distance\":"<<b.distance<<",\"reached\":"<<b.reached<<",\"eccentricity\":"<<b.ecc<<",\"actual_path\":"<<pathjson(b.path)<<'}';return o.str();}
static void replace(Adj&a,int u,int v,int w){for(int&x:a[u])if(x==v){x=w;return;}throw std::runtime_error("missing cut edge");}
int main(int argc,char**argv){
    const std::string source=argv[1],portsfile=argv[2],out=argv[3];const double limit=std::stod(argv[4]);
    const unsigned long long seed=202611010405ULL;std::mt19937_64 rng(seed);
    std::ifstream pin(portsfile);std::array<int,28>ports;std::array<bool,364>isport{};for(int&i:ports){pin>>i;isport[i]=true;}
    Adj original;for(auto&r:original)r.fill(-1);std::array<int,365>deg{};
    std::ifstream in(source);int n,m,u,v;in>>n>>m;assert(n==364&&m==714);std::vector<Edge>old,core;
    while(in>>u>>v){old.push_back({u,v});original[u][deg[u]++]=v;original[v][deg[v]++]=u;if(!isport[u]&&!isport[v])core.push_back({u,v});}
    assert(old.size()==714&&core.size()==630);
    std::set<std::array<int,30>>seen;int draws=0,duplicates=0,started=0,finished=0,failnew=0,failold=0,newpass=0;long long oldroots=0;
    bool hit=false,timed=false;std::string firstnew="null",firstold="null",winning="null",witness="null";
    std::ofstream ledger(out+"/ATTEMPTS.csv");ledger<<"index,core_cut0,core_cut1,matching_index,stage,failed_root,failed_target,distance,newroot_reached,newroot_ecc\n";
    std::ofstream matchinglog(out+"/MATCHING_AND_CUTS.csv");matchinglog<<"configuration,cut0u,cut0v,cut1u,cut1v";for(int i=0;i<14;++i)matchinglog<<",port"<<i<<"a,port"<<i<<'b';matchinglog<<'\n';
    while(started<10000){
        if(cpu()>=limit){timed=true;break;}
        ++draws;Config c;c.cuts={int(rng()%core.size()),int(rng()%core.size())};std::sort(c.cuts.begin(),c.cuts.end());
        const Edge e=core[c.cuts[0]],f=core[c.cuts[1]];if(e[0]==f[0]||e[0]==f[1]||e[1]==f[0]||e[1]==f[1])continue;
        auto shuffled=ports;std::shuffle(shuffled.begin(),shuffled.end(),rng);
        for(int i=0;i<14;++i){c.matching[i]={shuffled[2*i],shuffled[2*i+1]};std::sort(c.matching[i].begin(),c.matching[i].end());}std::sort(c.matching.begin(),c.matching.end());
        std::array<int,30>key;key[0]=c.cuts[0];key[1]=c.cuts[1];for(int i=0;i<14;++i){key[2+2*i]=c.matching[i][0];key[3+2*i]=c.matching[i][1];}if(!seen.insert(key).second){++duplicates;continue;}
        Adj a=original;for(Edge p:c.matching){for(int i=0;i<2;++i){bool added=false;for(int&x:a[p[i]])if(x==-1){x=p[1-i];added=true;break;}assert(added);}}
        replace(a,e[0],e[1],364);replace(a,e[1],e[0],364);replace(a,f[0],f[1],364);replace(a,f[1],f[0],364);a[364]={e[0],e[1],f[0],f[1]};
        const int index=started++;matchinglog<<index<<','<<e[0]<<','<<e[1]<<','<<f[0]<<','<<f[1];for(Edge p:c.matching)matchinglog<<','<<p[0]<<','<<p[1];matchinglog<<'\n';
        BFS b=bfs(a,364),newb=b;int stage=0;bool failed=false;
        if(!pass(b)){++failnew;failed=true;stage=1;if(firstnew=="null")firstnew="{\"configuration\":"+cfgjson(c,core)+",\"BFS\":"+bfsjson(b)+'}';}
        int maxecc=newb.ecc;std::vector<BFS>all;
        if(!failed){++newpass;all.push_back(newb);for(int root=0;root<364;++root){if(cpu()>=limit){timed=true;stage=3;break;}b=bfs(a,root);++oldroots;maxecc=std::max(maxecc,b.ecc);if(!pass(b)){++failold;failed=true;stage=2;if(firstold=="null")firstold="{\"configuration\":"+cfgjson(c,core)+",\"BFS\":"+bfsjson(b)+'}';break;}all.push_back(b);}}
        if(!failed&&!timed){hit=true;winning=cfgjson(c,core);witness=bfsjson(newb);std::ofstream graph(out+"/graph_d4_D5_n365.edges");graph<<"365 730\n";int count=0;for(int x=0;x<365;++x){auto row=a[x];std::sort(row.begin(),row.end());assert(std::adjacent_find(row.begin(),row.end())==row.end());for(int y:row){assert(x!=y&&y>=0);if(x<y){graph<<x<<' '<<y<<'\n';++count;}}}assert(count==730);
            std::ofstream h(out+"/ALL_ROOT_HISTOGRAMS.csv");h<<"root,N0,N1,N2,N3,N4,N5,eccentricity\n";for(const auto&r:all){std::array<int,6>hist{};for(int d:r.d)++hist[d];h<<r.root;for(int x:hist)h<<','<<x;h<<','<<r.ecc<<'\n';}
            std::ofstream hitfile(out+"/HIT.json");hitfile<<"{\"n\":365,\"m\":730,\"degree\":4,\"actual_diameter\":"<<maxecc<<",\"final_graph_BFS_roots\":365,\"configuration\":"<<winning<<",\"actual_distance_witness\":"<<witness<<"}\n";
        }
        ledger<<index<<','<<c.cuts[0]<<','<<c.cuts[1]<<','<<index<<','<<stage<<','<<(failed?b.root:-1)<<','<<(failed?b.target:-1)<<','<<(failed?b.distance:-1)<<','<<newb.reached<<','<<newb.ecc<<'\n';
        if(!timed)++finished;if(hit||timed)break;
    }
    std::ofstream raw(out+"/RAW_RESULT.json");raw<<"{\"status\":\""<<(hit?"FOUND365_PENDING_ROOT_ACCEPTANCE":timed?"UNKNOWN_CPU_CAP_NO_HIT":"UNKNOWN_10000_SAMPLE_NO_HIT")<<"\",\"seed\":"<<seed<<",\"sample_cap\":10000,\"distinct_configurations_started\":"<<started<<",\"distinct_configurations_finished\":"<<finished<<",\"draws\":"<<draws<<",\"duplicate_configurations\":"<<duplicates<<",\"rejected_newroot_R5\":"<<failnew<<",\"newroot_R5_passed\":"<<newpass<<",\"rejected_old_old\":"<<failold<<",\"final_candidate_old_label_BFS_roots\":"<<oldroots<<",\"first_newroot_failure\":"<<firstnew<<",\"first_old_old_failure\":"<<firstold<<",\"hit\":"<<(hit?"true":"false")<<",\"winning_configuration\":"<<winning<<",\"winning_distance_witness\":"<<witness<<",\"source_BFS\":0,\"run_process_CPU_seconds\":"<<cpu()<<",\"time_cap_reached\":"<<(timed?"true":"false")<<"}\n";
    std::cout<<(hit?"FOUND365":timed?"CPU_CAP":"SAMPLE_CAP")<<" distinct="<<started<<" newpass="<<newpass<<" oldfail="<<failold<<" CPU="<<cpu()<<std::endl;
}

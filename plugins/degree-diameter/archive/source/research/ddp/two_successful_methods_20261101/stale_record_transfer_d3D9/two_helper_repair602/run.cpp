#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using Adj = std::array<std::array<int, 3>, 602>;
using Edge = std::array<int, 2>;
struct Config { std::array<int,3> cuts; Edge repair; std::array<int,2> A,B; };
struct SearchBFS { int root, target, distance, reached, eccentricity; std::vector<int> path; };

static double cpu() { return double(std::clock()) / CLOCKS_PER_SEC; }
static std::string vec(const std::vector<int>& a) {
    std::ostringstream o; o << '[';
    for (size_t i=0;i<a.size();++i) {if(i)o<<',';o<<a[i];} return o.str()+']';
}
template<size_t N> static std::string arr(const std::array<int,N>& a) {return vec(std::vector<int>(a.begin(),a.end()));}
static std::string config_json(const Config& c, const std::vector<Edge>& edges) {
    std::ostringstream o; o << "{\"cut_edge_indices\":"<<arr(c.cuts)<<",\"cut_edges\":[";
    for(int i=0;i<3;++i){if(i)o<<',';o<<arr(edges[c.cuts[i]]);}o<<"],\"repair\":"<<arr(c.repair)
    <<",\"pins600\":"<<arr(c.A)<<",\"pins601\":"<<arr(c.B)<<'}';return o.str();
}
static SearchBFS bfs(const Adj& adj,int root) {
    std::array<int,602> d,par,q; d.fill(-1);par.fill(-1);d[root]=0;q[0]=root;int head=0,tail=1;
    while(head<tail){int v=q[head++];for(int w:adj[v])if(d[w]<0){d[w]=d[v]+1;par[w]=v;q[tail++]=w;}}
    int target=-1,ecc=0;for(int v=0;v<602;++v){if(d[v]>ecc)ecc=d[v];if(target<0&&(d[v]<0||d[v]>9))target=v;}
    if(target<0){for(int v=0;v<602;++v)if(d[v]==ecc){target=v;break;}}
    std::vector<int> path;if(d[target]>=0){for(int v=target;v>=0;v=par[v])path.push_back(v);std::reverse(path.begin(),path.end());}
    return {root,target,d[target],tail,ecc,path};
}
static bool pass(const SearchBFS& b) {return b.reached==602&&b.eccentricity<=9;}
static std::string bfs_json(const SearchBFS& b){std::ostringstream o;o<<"{\"root\":"<<b.root<<",\"target\":"<<b.target<<",\"distance\":"<<b.distance<<",\"reached\":"<<b.reached<<",\"eccentricity\":"<<b.eccentricity<<",\"actual_path\":"<<vec(b.path)<<'}';return o.str();}
static void replace(Adj& a,int u,int v,int w){for(int& x:a[u])if(x==v){x=w;return;}throw std::runtime_error("missing cut endpoint");}
int main(int argc,char** argv){
    const double start=cpu();const std::string source=argv[1],out=argv[2];const double limit=std::stod(argv[3]);
    const unsigned long long seed=202611010309ULL;std::mt19937_64 rng(seed);
    std::ifstream in(source);int n,m;in>>n>>m;if(n!=600||m!=900)return 2;
    Adj original{};std::array<int,602> size{};std::vector<Edge> edges;int u,v;
    while(in>>u>>v){edges.push_back({u,v});original[u][size[u]++]=v;original[v][size[v]++]=u;}
    if(edges.size()!=900)return 3;
    std::ofstream ledger(out+"/ATTEMPTS.csv");ledger<<"index,cut0,cut1,cut2,repair0,repair1,pin600a,pin600b,pin601a,pin601b,stage,failroot,failtarget,distance\n";
    std::unordered_set<unsigned long long> seen;seen.reserve(11000);
    int generated=0,finished=0,matching_draws=0,duplicate_draws=0,fail600=0,fail601=0,failold=0;
    long long helper_roots=0,old_roots=0;int bothpass=0;bool hit=false,timed=false;
    Config winning{};SearchBFS winning_witness{};int winning_diameter=0;
    std::string first600="null",first601="null",firstold="null",firstboth="null";
    while(generated<10000){
        if(cpu()-start>=limit){timed=true;break;}
        Config c;for(int i=0;i<3;++i)c.cuts[i]=int(rng()%900);std::sort(c.cuts.begin(),c.cuts.end());++matching_draws;
        std::array<int,6> endpoints;for(int i=0;i<3;++i){endpoints[2*i]=edges[c.cuts[i]][0];endpoints[2*i+1]=edges[c.cuts[i]][1];}
        std::sort(endpoints.begin(),endpoints.end());if(std::adjacent_find(endpoints.begin(),endpoints.end())!=endpoints.end())continue;
        std::vector<Edge> repairs;
        for(int i=0;i<6;++i)for(int j=i+1;j<6;++j){int a=endpoints[i],b=endpoints[j];if(std::find(original[a].begin(),original[a].end(),b)==original[a].end())repairs.push_back({i,j});}
        if(repairs.empty())continue;
        Edge rp=repairs[rng()%repairs.size()];int partition=int(rng()%3);
        unsigned long long key=static_cast<unsigned long long>(c.cuts[0])|(static_cast<unsigned long long>(c.cuts[1])<<10)|(static_cast<unsigned long long>(c.cuts[2])<<20)|(static_cast<unsigned long long>(rp[0]*6+rp[1])<<30)|(static_cast<unsigned long long>(partition)<<36);
        if(!seen.insert(key).second){++duplicate_draws;continue;}
        c.repair={endpoints[rp[0]],endpoints[rp[1]]};std::vector<int> remain;
        for(int i=0;i<6;++i)if(i!=rp[0]&&i!=rp[1])remain.push_back(endpoints[i]);
        c.A={remain[0],remain[partition+1]};std::vector<int> last;
        for(int x:remain)if(x!=c.A[0]&&x!=c.A[1])last.push_back(x);c.B={last[0],last[1]};
        Adj a=original;
        for(int i=0;i<3;++i){Edge e=edges[c.cuts[i]];replace(a,e[0],e[1],-1);replace(a,e[1],e[0],-1);}
        for(int i=0;i<2;++i)for(int& x:a[c.repair[i]])if(x==-1)x=c.repair[1-i];
        for(int x:c.A)for(int& w:a[x])if(w==-1)w=600;
        for(int x:c.B)for(int& w:a[x])if(w==-1)w=601;
        a[600]={c.A[0],c.A[1],601};a[601]={c.B[0],c.B[1],600};
        const int index=generated++;int stage=0;SearchBFS failure{};bool failed=false;
        auto b=bfs(a,600);++helper_roots;
        if(!pass(b)){++fail600;stage=1;failure=b;failed=true;if(first600=="null")first600="{\"configuration\":"+config_json(c,edges)+",\"BFS\":"+bfs_json(b)+'}';}
        if(!failed){b=bfs(a,601);++helper_roots;if(!pass(b)){++fail601;stage=2;failure=b;failed=true;if(first601=="null")first601="{\"configuration\":"+config_json(c,edges)+",\"BFS\":"+bfs_json(b)+'}';}}
        int candidate_diameter=0;SearchBFS exact_witness=b;
        if(!failed){
            ++bothpass;if(firstboth=="null")firstboth=config_json(c,edges);
            for(int root=0;root<600;++root){
                if(cpu()-start>=limit){timed=true;stage=4;break;}
                b=bfs(a,root);++old_roots;
                if(b.eccentricity>=candidate_diameter){candidate_diameter=b.eccentricity;exact_witness=b;}
                if(!pass(b)){++failold;stage=3;failure=b;failed=true;if(firstold=="null")firstold="{\"configuration\":"+config_json(c,edges)+",\"BFS\":"+bfs_json(b)+'}';break;}
            }
            if(!failed&&!timed){hit=true;winning=c;winning_diameter=candidate_diameter;winning_witness=exact_witness;
                std::ofstream graph(out+"/candidate_d3_D9_n602.edges");graph<<"602 903\n";for(int x=0;x<602;++x){auto row=a[x];std::sort(row.begin(),row.end());for(int y:row)if(x<y)graph<<x<<' '<<y<<'\n';}}
        }
        ledger<<index<<','<<c.cuts[0]<<','<<c.cuts[1]<<','<<c.cuts[2]<<','<<c.repair[0]<<','<<c.repair[1]<<','<<c.A[0]<<','<<c.A[1]<<','<<c.B[0]<<','<<c.B[1]<<','<<stage<<','<<(failed?failure.root:-1)<<','<<(failed?failure.target:-1)<<','<<(failed?failure.distance:-1)<<'\n';
        if(!timed)++finished;if(hit||timed)break;
    }
    std::ofstream raw(out+"/RAW_RESULT.json");raw<<"{\n\"status\":\""<<(hit?"FOUND602_PENDING_ROOT_ACCEPTANCE":(timed?"UNKNOWN_CPU_CAP_NO_HIT":"UNKNOWN_10000_SAMPLE_NO_HIT"))<<"\",\n"
    <<"\"seed\":"<<seed<<",\"sample_cap\":10000,\"distinct_configurations_started\":"<<generated<<",\"distinct_configurations_finished\":"<<finished<<",\"matching_draws\":"<<matching_draws<<",\"duplicate_draws\":"<<duplicate_draws<<",\n"
    <<"\"rejected_helper600\":"<<fail600<<",\"rejected_helper601\":"<<fail601<<",\"both_helpers_passed\":"<<bothpass<<",\"rejected_old_old\":"<<failold<<",\"helper_root_BFS_count\":"<<helper_roots<<",\"modified_graph_old_label_BFS_count\":"<<old_roots<<",\n"
    <<"\"all_source600_validity_BFS_count\":0,\"first_helper600_failure\":"<<first600<<",\"first_helper601_failure\":"<<first601<<",\"first_old_old_failure\":"<<firstold<<",\"first_both_helper_pass_configuration\":"<<firstboth<<",\n"
    <<"\"hit\":"<<(hit?"true":"false")<<",\"winning_configuration\":"<<(hit?config_json(winning,edges):"null")<<",\"winning_diameter\":"<<winning_diameter<<",\"winning_distance_witness\":"<<(hit?bfs_json(winning_witness):"null")<<",\"run_process_CPU_seconds\":"<<cpu()<<",\"run_CPU_limit_seconds\":"<<limit<<",\"time_cap_reached\":"<<(timed?"true":"false")<<"\n}\n";
    std::cout<<(hit?"FOUND602":(timed?"CPU_CAP":"SAMPLE_CAP"))<<" distinct="<<generated<<" bothhelpers="<<bothpass<<" oldfail="<<failold<<" CPU="<<cpu()<<'\n';
}

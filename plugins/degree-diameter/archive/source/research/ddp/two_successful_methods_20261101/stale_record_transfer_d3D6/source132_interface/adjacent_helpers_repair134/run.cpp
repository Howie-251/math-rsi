#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using Adj = std::array<std::array<int, 3>, 134>;
using Edge = std::array<int, 2>;
struct Config { std::array<int,3> cuts; Edge repair; std::array<int,2> A,B; };
struct SearchBFS { int root, target, distance, reached, eccentricity; std::vector<int> path; std::array<int,7> hist; };

static double cpu() { return double(std::clock()) / CLOCKS_PER_SEC; }
static std::string vec(const std::vector<int>& a) {
    std::ostringstream o; o << '[';
    for (size_t i=0;i<a.size();++i) {if(i)o<<',';o<<a[i];} return o.str()+']';
}
template<size_t N> static std::string arr(const std::array<int,N>& a) {return vec(std::vector<int>(a.begin(),a.end()));}
static std::string config_json(const Config& c, const std::vector<Edge>& edges) {
    std::ostringstream o; o << "{\"cut_edge_indices\":"<<arr(c.cuts)<<",\"cut_edges\":[";
    for(int i=0;i<3;++i){if(i)o<<',';o<<arr(edges[c.cuts[i]]);}o<<"],\"repair\":"<<arr(c.repair)
    <<",\"pins132\":"<<arr(c.A)<<",\"pins133\":"<<arr(c.B)<<'}';return o.str();
}
static SearchBFS bfs(const Adj& adj,int root) {
    std::array<int,134> d,par,q; d.fill(-1);par.fill(-1);d[root]=0;q[0]=root;int head=0,tail=1;
    while(head<tail){int v=q[head++];for(int w:adj[v])if(d[w]<0){d[w]=d[v]+1;par[w]=v;q[tail++]=w;}}
    int target=-1,ecc=0;for(int v=0;v<134;++v){if(d[v]>ecc)ecc=d[v];if(target<0&&(d[v]<0||d[v]>6))target=v;}
    if(target<0){for(int v=0;v<134;++v)if(d[v]==ecc){target=v;break;}}
    std::vector<int> path;if(d[target]>=0){for(int v=target;v>=0;v=par[v])path.push_back(v);std::reverse(path.begin(),path.end());}
    std::array<int,7>hist{};for(int v=0;v<134;++v)if(d[v]>=0&&d[v]<=6)++hist[d[v]];return {root,target,d[target],tail,ecc,path,hist};
}
static bool pass(const SearchBFS& b) {return b.reached==134&&b.eccentricity<=6;}
static std::string bfs_json(const SearchBFS& b){std::ostringstream o;o<<"{\"root\":"<<b.root<<",\"target\":"<<b.target<<",\"distance\":"<<b.distance<<",\"reached\":"<<b.reached<<",\"eccentricity\":"<<b.eccentricity<<",\"actual_path\":"<<vec(b.path)<<'}';return o.str();}
static void replace(Adj& a,int u,int v,int w){for(int& x:a[u])if(x==v){x=w;return;}throw std::runtime_error("missing cut endpoint");}
static std::string original_pair_diagnostic(const Adj& a,int source,int target,const Config& c,const std::vector<Edge>& edges){
    std::array<int,132>d,par,q;d.fill(-1);par.fill(-1);d[source]=0;q[0]=source;int head=0,tail=1;
    while(head<tail&&d[target]<0){int u=q[head++];for(int v:a[u])if(d[v]<0){d[v]=d[u]+1;par[v]=u;q[tail++]=v;}}
    std::vector<int>path;for(int v=target;v>=0;v=par[v])path.push_back(v);std::reverse(path.begin(),path.end());
    std::ostringstream o;o<<"{\"source\":"<<source<<",\"target\":"<<target<<",\"original_distance\":"<<d[target]<<",\"original_shortest_path\":"<<vec(path)<<",\"cut_edges_on_this_path\":[";bool comma=false;
    for(int id:c.cuts){Edge cut=edges[id];for(size_t i=1;i<path.size();++i)if((path[i-1]==cut[0]&&path[i]==cut[1])||(path[i-1]==cut[1]&&path[i]==cut[0])){if(comma)o<<',';o<<arr(cut);comma=true;break;}}
    o<<"],\"single_pair_only\":true,\"all_source_geodesics_enumerated\":false}";return o.str();
}
int main(int argc,char** argv){
    const double start=cpu();const std::string source=argv[1],out=argv[2];const double limit=std::stod(argv[3]);
    const unsigned long long seed=202611010306ULL;std::mt19937_64 rng(seed);
    std::ifstream in(source);std::string line;std::set<Edge> edge_set;std::array<bool,132>labels{};int rawedges=0,rows=0,loops=0,duprows=0;
    while(std::getline(in,line)){
        auto pos=line.find_first_not_of(" \t\r");if(pos==std::string::npos||line[pos]=='#')continue;
        std::istringstream row(line);int u,v;if(!(row>>u)||u<0||u>=132)throw std::runtime_error("input node label outside0..131");
        if(labels[u])++duprows;labels[u]=true;++rows;
        while(row>>v){if(v<0||v>=132)throw std::runtime_error("input neighbor outside0..131");++rawedges;if(u==v){++loops;continue;}edge_set.insert({std::min(u,v),std::max(u,v)});}
        if(!row.eof())throw std::runtime_error("noninteger input neighbor");
    }
    Adj original{};std::array<int,134>size{};std::vector<Edge>edges(edge_set.begin(),edge_set.end());
    for(Edge e:edges){if(size[e[0]]>=3||size[e[1]]>=3)throw std::runtime_error("source input degree greater3");original[e[0]][size[e[0]]++]=e[1];original[e[1]][size[e[1]]++]=e[0];}
    bool inputok=rows==132&&duprows==0&&loops==0&&edges.size()==198;
    for(int u=0;u<132;++u)inputok=inputok&&labels[u]&&size[u]==3;
    std::ofstream binding(out+"/SOURCE_INPUT_BINDING.json");binding<<"{\"status\":\""<<(inputok?"PASS_LITERAL_SIMPLE_CUBIC_INPUT":"INPUT_FAILURE_NO_SAMPLE")<<"\",\"n\":132,\"m\":"<<edges.size()<<",\"raw_edge_occurrences\":"<<rawedges<<",\"row_count\":"<<rows<<",\"duplicate_row_labels\":"<<duprows<<",\"selfloops\":"<<loops<<",\"all132_labels_present_and_degree3\":"<<(inputok?"true":"false")<<",\"source_D6_BFS\":0,\"raw_parse_count\":1}\n";binding.close();if(!inputok)return 4;
    std::ofstream ledger(out+"/ATTEMPTS.csv");ledger<<"index,cut0,cut1,cut2,repair0,repair1,pin132a,pin132b,pin133a,pin133b,stage,failroot,failtarget,distance\n";
    std::unordered_set<unsigned long long> seen;seen.reserve(11000);
    int generated=0,finished=0,matching_draws=0,duplicate_draws=0,fail132=0,fail133=0,failold=0;
    long long helper_roots=0,old_roots=0;int bothpass=0;bool hit=false,timed=false;
    Config winning{};SearchBFS winning_witness{};int winning_diameter=0;
    std::vector<SearchBFS> winning_roots;
    std::string first132="null",first133="null",firstold="null",firstboth="null",old_pair_diagnostic="null";
    int source_pair_diagnostic_count=0;
    while(generated<10000){
        if(cpu()-start>=limit){timed=true;break;}
        Config c;for(int i=0;i<3;++i)c.cuts[i]=int(rng()%198);std::sort(c.cuts.begin(),c.cuts.end());++matching_draws;
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
        for(int x:c.A)for(int& w:a[x])if(w==-1)w=132;
        for(int x:c.B)for(int& w:a[x])if(w==-1)w=133;
        a[132]={c.A[0],c.A[1],133};a[133]={c.B[0],c.B[1],132};
        const int index=generated++;int stage=0;SearchBFS failure{};bool failed=false;
        auto b=bfs(a,132);++helper_roots;SearchBFS first_helper_result=b;
        if(!pass(b)){++fail132;stage=1;failure=b;failed=true;if(first132=="null")first132="{\"configuration\":"+config_json(c,edges)+",\"BFS\":"+bfs_json(b)+'}';}
        if(!failed){b=bfs(a,133);++helper_roots;if(!pass(b)){++fail133;stage=2;failure=b;failed=true;if(first133=="null")first133="{\"configuration\":"+config_json(c,edges)+",\"BFS\":"+bfs_json(b)+'}';}}
        int candidate_diameter=0;SearchBFS exact_witness=b;std::vector<SearchBFS> candidate_roots;
        if(!failed){
            ++bothpass;candidate_roots.push_back(first_helper_result);candidate_roots.push_back(b);if(firstboth=="null")firstboth=config_json(c,edges);
            for(int root=0;root<132;++root){
                if(cpu()-start>=limit){timed=true;stage=4;break;}
                b=bfs(a,root);++old_roots;candidate_roots.push_back(b);
                if(b.eccentricity>=candidate_diameter){candidate_diameter=b.eccentricity;exact_witness=b;}
                if(!pass(b)){++failold;stage=3;failure=b;failed=true;if(firstold=="null"){
                    firstold="{\"configuration\":"+config_json(c,edges)+",\"BFS\":"+bfs_json(b)+'}';
                    if(b.root<132&&b.target<132){old_pair_diagnostic=original_pair_diagnostic(original,b.root,b.target,c,edges);++source_pair_diagnostic_count;}
                }break;}
            }
            if(!failed&&!timed){hit=true;winning=c;winning_diameter=candidate_diameter;winning_witness=exact_witness;winning_roots=candidate_roots;
                std::ofstream graph(out+"/graph_d3_D6_n134.edges");graph<<"134 201\n";for(int x=0;x<134;++x){auto row=a[x];std::sort(row.begin(),row.end());for(int y:row)if(x<y)graph<<x<<' '<<y<<'\n';}}
        }
        ledger<<index<<','<<c.cuts[0]<<','<<c.cuts[1]<<','<<c.cuts[2]<<','<<c.repair[0]<<','<<c.repair[1]<<','<<c.A[0]<<','<<c.A[1]<<','<<c.B[0]<<','<<c.B[1]<<','<<stage<<','<<(failed?failure.root:-1)<<','<<(failed?failure.target:-1)<<','<<(failed?failure.distance:-1)<<'\n';
        if(!timed)++finished;if(hit||timed)break;
    }
    if(hit){std::ofstream hist(out+"/ALL_ROOT_HISTOGRAMS.csv");hist<<"root,N0,N1,N2,N3,N4,N5,N6,eccentricity\n";for(const auto&r:winning_roots){hist<<r.root;for(int n:r.hist)hist<<','<<n;hist<<','<<r.eccentricity<<'\n';}}
    std::ofstream raw(out+"/RAW_RESULT.json");raw<<"{\n\"status\":\""<<(hit?"FOUND134_PENDING_ROOT_ACCEPTANCE":(timed?"UNKNOWN_CPU_CAP_NO_HIT":"UNKNOWN_10000_SAMPLE_NO_HIT"))<<"\",\n"
    <<"\"seed\":"<<seed<<",\"sample_cap\":10000,\"distinct_configurations_started\":"<<generated<<",\"distinct_configurations_finished\":"<<finished<<",\"matching_draws\":"<<matching_draws<<",\"duplicate_draws\":"<<duplicate_draws<<",\n"
    <<"\"rejected_helper132\":"<<fail132<<",\"rejected_helper133\":"<<fail133<<",\"both_helpers_passed\":"<<bothpass<<",\"rejected_old_old\":"<<failold<<",\"helper_root_BFS_count\":"<<helper_roots<<",\"modified_graph_old_label_BFS_count\":"<<old_roots<<",\n"
    <<"\"all_source132_validity_BFS_count\":0,\"original_source_pair_diagnostic_BFS_count\":"<<source_pair_diagnostic_count<<",\"single_old_pair_diagnostic\":"<<old_pair_diagnostic<<",\"first_helper132_failure\":"<<first132<<",\"first_helper133_failure\":"<<first133<<",\"first_old_old_failure\":"<<firstold<<",\"first_both_helper_pass_configuration\":"<<firstboth<<",\n"
    <<"\"hit\":"<<(hit?"true":"false")<<",\"winning_configuration\":"<<(hit?config_json(winning,edges):"null")<<",\"winning_diameter\":"<<winning_diameter<<",\"winning_distance_witness\":"<<(hit?bfs_json(winning_witness):"null")<<",\"run_process_CPU_seconds\":"<<cpu()<<",\"run_CPU_limit_seconds\":"<<limit<<",\"time_cap_reached\":"<<(timed?"true":"false")<<"\n}\n";
    std::cout<<(hit?"FOUND134":(timed?"CPU_CAP":"SAMPLE_CAP"))<<" distinct="<<generated<<" bothhelpers="<<bothpass<<" oldfail="<<failold<<" CPU="<<cpu()<<'\n';
}

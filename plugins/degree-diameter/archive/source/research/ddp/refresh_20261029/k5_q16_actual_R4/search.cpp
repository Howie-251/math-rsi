// Prepared only. Input is converted from root's actual-provider cache;
// this executable contains no old full-NB4 filter and no provider enumeration.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=6480, ALL=4096;
constexpr uint64_t LOW=~uint64_t(0), HIGH=(uint64_t(1)<<17)-1;
struct Mask { uint64_t lo=0,hi=0; bool full()const{return lo==LOW&&hi==HIGH;} };
struct Group {int node; Mask mask;};
struct Node {int parent, letter;};
static int mul(int a,int b){
    int i=a&7,j=a>>3,k=b&7,l=b>>3;
    return ((i+(j?-k:k)+4*j*l+16)&7)+8*(j^l);
}
static int inv(int a){return a<8?((-a)&7):(((a&7)+4)&7)+8;}
static double cpu(){return double(clock())/CLOCKS_PER_SEC;}
static int idx(int b,int g,int x){return (16*b+g)*81+x;}
static const int chord[6][2]={{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}};
struct Engine {
    vector<Node> nodes;
    array<vector<Group>,5> groups;
    int port[5][4]{}, field[4][81][3]{};
    vector<array<int,6>> phases;
    int prod[16][16]{}, values[12]{}, edge[5][5]{};
    vector<int> memo;
    vector<uint32_t> seen;
    uint32_t generation=0;
    array<array<int,12>,N> adj;
    array<int,N> queue{}, visited{};
    int bfs_generation=0;
    uint64_t checked=0, root0_pass=0, failed_full=0, bfs_roots=0;
    uint64_t root0_failed_base[5]{};
    double limit,start;
    ofstream failures;
    bool expired()const{return cpu()-start>=limit;}
    explicit Engine(const string& path,double seconds):limit(seconds),start(cpu()),failures("candidate_failures.jsonl"){
        ifstream f(path); int version, nn,ng,np;
        f>>version; assert(version==1);
        f>>nn; nodes.resize(nn); memo.resize(nn); seen.resize(nn);
        for(auto &n:nodes) f>>n.parent>>n.letter;
        assert(nodes[0].parent==-1);
        f>>ng;
        for(int i=0;i<ng;i++) {int b;Group g;f>>b>>g.node>>g.mask.lo>>g.mask.hi;groups[b].push_back(g);}
        for(auto& gg:groups) stable_sort(gg.begin(),gg.end(),[](const Group&a,const Group&b){return a.mask.full()>b.mask.full();});
        for(auto &row:port)for(int &x:row)f>>x;
        for(auto &p:field)for(auto &x:p)for(int &y:x)f>>y;
        f>>np; phases.resize(np);for(auto &p:phases)for(int &x:p)f>>x;
        assert(f.good());
        for(int a=0;a<16;a++)for(int b=0;b<16;b++)prod[a][b]=mul(a,b);
        for(int a=0;a<16;a++)assert(prod[a][inv(a)]==0);
    }
    int word(int n){
        if(seen[n]==generation)return memo[n];
        const auto q=nodes[n];
        int v=prod[word(q.parent)][values[q.letter]];
        seen[n]=generation;return memo[n]=v;
    }
    void assign(const array<int,6>& q){
        generation++;memo[0]=0;seen[0]=generation;
        for(int u=0;u<5;u++)for(int v=0;v<5;v++)edge[u][v]=0;
        for(int i=0;i<6;i++){
            values[2*i]=q[i];values[2*i+1]=inv(q[i]);
            edge[chord[i][0]][chord[i][1]]=q[i];
            edge[chord[i][1]][chord[i][0]]=inv(q[i]);
        }
    }
    bool zero_root(){
        for(int b=0;b<5;b++){
            Mask cover[16];
            for(const auto &g:groups[b]){
                int d=word(g.node);
                cover[d].lo|=g.mask.lo;cover[d].hi|=g.mask.hi;
            }
            for(int d=0;d<16;d++)if(!cover[d].full()){root0_failed_base[b]++;return false;}
        }
        return true;
    }
    void build(){
        for(int b=0;b<5;b++)for(int g=0;g<16;g++)for(int x=0;x<81;x++){
            auto &out=adj[idx(b,g,x)];int k=0;
            for(int p=0;p<4;p++){
                int v=port[b][p],h=prod[g][edge[b][v]];
                for(int t=0;t<3;t++)out[k++]=idx(v,h,field[p][x][t]);
            }
        }
        // Literal local checks, not a second diameter check.
        for(int u=0;u<N;u++){
            auto a=adj[u];sort(a.begin(),a.end());
            assert(adjacent_find(a.begin(),a.end())==a.end());
            for(int p=0;p<4;p++)for(int t=0;t<3;t++){
                int v=adj[u][3*p+t];assert(v!=u);
                auto first=adj[v].begin()+3*(p^1);
                assert(find(first,first+3,u)!=first+3);
            }
        }
    }
    // Returns number reached within four, and a literal missing vertex.
    pair<int,int> bfs(int root){
        bfs_generation++;int head=0,tail=1;queue[0]=root;visited[root]=bfs_generation;
        for(int depth=0;depth<4 && tail<N;depth++){
            int end=tail;
            while(head<end){int u=queue[head++];for(int v:adj[u])if(visited[v]!=bfs_generation){visited[v]=bfs_generation;queue[tail++]=v;}}
        }
        bfs_roots++;
        if(tail==N)return {tail,-1};
        for(int v=0;v<N;v++)if(visited[v]!=bfs_generation)return {tail,v};
        assert(false);return {0,0};
    }
    // 1=complete PASS, 0=real failed root, -1=budget with this candidate pending.
    int validate(size_t pi,int li,const array<int,6>& q,int& next_root){
        build();
        vector<int> roots;
        for(int b=1;b<5;b++)roots.push_back(idx(b,0,0));
        roots.push_back(0);
        for(int b=0;b<5;b++)for(int x=1;x<81;x++)roots.push_back(idx(b,0,x));
        assert(roots.size()==405);
        for(int k=0;k<405;k++){
            next_root=k;if(expired())return -1;
            auto [reached,bad]=bfs(roots[k]);
            if(bad>=0){
                failures<<"{\"phase_index\":"<<pi<<",\"lift_index\":"<<li<<",\"voltages\":[";
                for(int j=0;j<6;j++)failures<<(j?",":"")<<q[j];
                failures<<"],\"root\":"<<roots[k]<<",\"unreached_target\":"<<bad<<",\"closed_R4_size\":"<<reached<<",\"roots_checked_this_candidate\":"<<k+1<<"}\n";
                failed_full++;return 0;
            }
        }
        next_root=405;return 1;
    }
    void save_hit(const array<int,6>& q){
        ofstream g("hit.edges");g<<N<<' '<<N*6<<'\n';
        for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)g<<u<<' '<<v<<'\n';
        ofstream c("hit.controller.edges");c<<80<<' '<<160<<'\n';
        for(int b=0;b<5;b++)for(int d=0;d<16;d++)for(int p=0;p<4;p++){
            int u=16*b+d,v=16*port[b][p]+prod[d][edge[b][port[b][p]]];if(u<v)c<<u<<' '<<v<<'\n';
        }
        ofstream f("HIT.json");f<<"{\"voltages\":[";for(int i=0;i<6;i++)f<<(i?",":"")<<q[i];
        f<<"],\"n\":6480,\"m\":38880,\"regular_degree\":12,\"verified_representative_roots\":405,\"diameter_at_most\":4,\"independent_verification\":\"pending_root\"}\n";
    }
    void calibrate(){
        assert(!phases.empty());array<int,6> q;
        for(int i=0;i<6;i++){int c=phases[0][i];q[i]=(c&1)+8*(c>>1);}
        assign(q);Mask cover[5][16];
        for(int b=0;b<5;b++)for(const auto &g:groups[b]){
            int d=word(g.node);cover[b][d].lo|=g.mask.lo;cover[b][d].hi|=g.mask.hi;
        }
        build();auto [reached,bad]=bfs(0);int image_size=0,matches=0;
        ofstream a("CALIBRATION.cache_R4.u8.bin",ios::binary),b("CALIBRATION.literal_R4.u8.bin",ios::binary);
        for(int u=0;u<N;u++){
            int x=u%81,d=(u/81)%16,v=u/(81*16);
            unsigned char by_cache=x<64?((cover[v][d].lo>>x)&1):((cover[v][d].hi>>(x-64))&1);
            unsigned char by_bfs=visited[u]==bfs_generation;
            a.put(by_cache);b.put(by_bfs);image_size+=by_cache;matches+=by_cache==by_bfs;
        }
        ofstream f("CALIBRATION.json");f<<"{\"status\":\""<<(matches==N?"PASS":"FAIL")<<"\",\"voltages\":[";
        for(int i=0;i<6;i++)f<<(i?",":"")<<q[i];
        f<<"],\"n\":6480,\"m\":38880,\"simple\":true,\"degree\":12,\"inverse_ports_literal_checked\":true,\"root\":0,\"cache_R4_size\":"<<image_size
         <<",\"literal_R4_size\":"<<reached<<",\"pointwise_matches\":"<<matches<<",\"first_unreached_target\":"<<bad<<",\"native_CPU_seconds\":"<<cpu()-start<<"}\n";
        assert(matches==N);cout<<"CALIBRATION_PASS reached="<<reached<<"\n";
    }
    void terminal(const string& status,size_t pi,int li,int next_root){
        failures.flush();ofstream f("NATIVE_TERMINAL.json");
        f<<"{\"status\":\""<<status<<"\",\"phase_index\":"<<pi<<",\"lift_index\":"<<li<<",\"pending_candidate_next_root\":"<<next_root
         <<",\"passing_projection_count\":"<<phases.size()<<",\"actual_lift_scope\":"<<uint64_t(phases.size())*ALL
         <<",\"fully_decided_lifts\":"<<checked<<",\"root0_pass_candidates\":"<<root0_pass<<",\"literal_candidate_failures\":"<<failed_full
         <<",\"literal_BFS_roots\":"<<bfs_roots<<",\"native_CPU_seconds\":"<<cpu()-start<<",\"root0_failed_base_counts\":[";
        for(int b=0;b<5;b++)f<<(b?",":"")<<root0_failed_base[b];f<<"]}\n";
        cout<<status<<" checked="<<checked<<" candidates="<<root0_pass<<" cpu="<<cpu()-start<<endl;
    }
    void run(){
        for(size_t pi=0;pi<phases.size();pi++)for(int li=0;li<ALL;li++){
            if(expired()){terminal("BUDGET_UNKNOWN",pi,li,0);return;}
            int k=li;array<int,6>q;
            for(int i=5;i>=0;i--){int c=phases[pi][i];q[i]=(c&1)+2*(k&3)+8*(c>>1);k>>=2;}
            assign(q);
            if(!zero_root()){checked++;continue;}
            root0_pass++;int next_root=0;
            int result=validate(pi,li,q,next_root);
            if(result<0){terminal("BUDGET_UNKNOWN",pi,li,next_root);return;}
            checked++;
            if(result==1){save_hit(q);terminal("COMPLETE_GRAPH_PASS",pi,li,405);return;}
        }
        terminal("COMPLETE_NO_FULL_GRAPH",phases.size(),0,0);
    }
};
int main(int argc,char**argv){
    if(argc==4 && string(argv[1])=="--calibrate"){
        Engine e(argv[2],stod(argv[3]));e.calibrate();return 0;
    }
    if(argc!=3){cerr<<"usage: search search_input.txt cpu_seconds\n";return 2;}
    Engine e(argv[1],stod(argv[2]));e.run();return 0;
}

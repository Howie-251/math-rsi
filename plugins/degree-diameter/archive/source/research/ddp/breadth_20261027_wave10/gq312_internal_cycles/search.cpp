#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
constexpr int N=312,H=156,W=5;
using Bits=array<uint64_t,W>;
using Rows=array<Bits,N>;
using Edge=pair<int,int>;
array<array<int,8>,N> adj;
array<array<bool,H>,H> inside[2];
array<vector<Edge>,2> factors;
vector<Edge> incidence;
string directory;
clock_t began;
double budget=17;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}
Edge canonical(int u,int v){if(u>v)swap(u,v);return {u,v};}
void put(Bits&x,int v){x[v>>6]|=1ULL<<(v&63);}
int score(Rows* saved=nullptr){
    Rows one{},two{},three{};
    for(int u=0;u<N;u++){put(one[u],u);for(int v:adj[u])put(one[u],v);}
    for(int u=0;u<N;u++){
        two[u]=one[u];
        for(int v:adj[u])for(int w=0;w<W;w++)two[u][w]|=one[v][w];
    }
    long long covered=0;
    for(int u=0;u<N;u++){
        three[u]=two[u];
        for(int v:adj[u])for(int w=0;w<W;w++)three[u][w]|=two[v][w];
        for(auto w:three[u])covered+=__builtin_popcountll(w);
    }
    if(saved)*saved=three;
    assert((N*N-covered)%2==0);
    return (N*N-covered)/2;
}
void walk(int u,int remaining,Bits&out,long long&visits){
    put(out,u);visits++;
    if(!remaining)return;
    for(int v:adj[u])walk(v,remaining-1,out,visits);
}
void initialize(uint64_t seed){
    memset(inside,0,sizeof(inside));
    array<int,N> deg{};
    for(auto [u,v]:incidence){adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
    mt19937_64 rng(seed);
    for(int part=0;part<2;part++){
        vector<int> cycle(H);iota(cycle.begin(),cycle.end(),0);shuffle(cycle.begin(),cycle.end(),rng);
        factors[part].clear();
        for(int i=0;i<H;i++){
            int a=cycle[i],b=cycle[(i+1)%H],u=part*H+a,v=part*H+b;
            factors[part].push_back(canonical(a,b));inside[part][a][b]=inside[part][b][a]=true;
            adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;
        }
    }
    for(int x:deg)assert(x==8);
}
void change(int part,Edge old0,Edge old1,Edge new0,Edge new1){
    array<Edge,2> old={old0,old1},neu={new0,new1};
    for(auto [a,b]:old)inside[part][a][b]=inside[part][b][a]=false;
    for(auto [a,b]:neu)inside[part][a][b]=inside[part][b][a]=true;
    for(auto [a,b]:old){
        for(auto [u,was]:{Edge{a,b},Edge{b,a}}){
            int to=-1;
            for(auto [x,y]:neu){if(x==u)to=y;if(y==u)to=x;}
            assert(to>=0);
            int g=part*H+u;
            int slot=adj[g][6]==part*H+was?6:7;
            assert(adj[g][slot]==part*H+was);adj[g][slot]=part*H+to;
        }
    }
}
void save_graph(int best,int start,int proposal,uint64_t seed){
    set<Edge> all;
    for(int u=0;u<N;u++){
        set<int> unique(adj[u].begin(),adj[u].end());assert(unique.size()==8&&!unique.count(u));
        for(int v:unique)all.insert(canonical(u,v));
    }
    assert(all.size()==1248);
    for(auto e:incidence)assert(all.count(e));
    ofstream f(directory+"/best.edges");f<<N<<' '<<all.size()<<'\n';
    for(auto [u,v]:all)f<<u<<' '<<v<<'\n';
    ofstream h(directory+"/best.factors.json");h<<"{\"point_factor\":[";
    for(int part=0;part<2;part++){
        for(int i=0;i<H;i++){if(i)h<<',';auto [a,b]=factors[part][i];h<<'['<<a+part*H<<','<<b+part*H<<']';}
        if(part==0)h<<"],\"line_factor\":[";
    }
    h<<"],\"n\":312,\"incidence_edges\":936,\"factor_edges_each\":156,\"total_edges\":1248,\"degree\":8}\n";
    ofstream p(directory+"/best_parameters.json");
    p<<"{\"start\":"<<start<<",\"legal_proposal\":"<<proposal<<",\"seed\":"<<seed
     <<",\"n\":312,\"edges\":1248,\"degree\":8,\"target_D\":3,\"savedL\":253,\"bad_unordered_pairs_predicted\":"<<best
     <<",\"producer_BFS_performed\":false,\"all_incidence_edges_retained\":true}\n";
}
int main(int argc,char**argv){
    assert(argc==3);directory=argv[1];budget=stod(argv[2]);began=clock();
    rlimit hard{18,20};assert(setrlimit(RLIMIT_CPU,&hard)==0);
    ifstream f(directory+"/incidence.edges");int nn,mm;f>>nn>>mm;assert(nn==N&&mm==936);
    for(int k=0,u,v;k<mm;k++){f>>u>>v;incidence.push_back({u,v});}
    constexpr uint64_t seeds[2]={20261027103121ULL,20261027103122ULL};
    struct Stat{int start,initial=0,final=0,raw=0,legal=0,rejected=0,accepted=0,improvements=0;};
    vector<Stat> stats;bool calibrated=false,hit=false,limit=false;int best=INT_MAX;
    ofstream progress(directory+"/progress.jsonl");
    for(int start=0;start<2&&!hit&&!limit;start++){
        initialize(seeds[start]);mt19937_64 rng(seeds[start]^0x5a17d4ULL);Stat s;s.start=start;
        int current=score();s.initial=current;
        if(current<best){best=current;save_graph(best,start,0,seeds[start]);}
        cout<<"START "<<start<<" initial="<<current<<endl;
        while(s.legal<1000&&!hit){
            if(cpu()>budget){limit=true;break;}
            s.raw++;int part=rng()%2,i=rng()%H,j=rng()%H;
            if(i==j){s.rejected++;continue;}
            Edge old0=factors[part][i],old1=factors[part][j];auto [a,b]=old0;auto [c,d]=old1;
            if(a==c||a==d||b==c||b==d){s.rejected++;continue;}
            if(rng()&1)swap(c,d);
            Edge new0=canonical(a,c),new1=canonical(b,d);
            if(inside[part][new0.first][new0.second]||inside[part][new1.first][new1.second]){s.rejected++;continue;}
            change(part,old0,old1,new0,new1);factors[part][i]=new0;factors[part][j]=new1;
            Rows bits;int candidate=score(calibrated?nullptr:&bits);s.legal++;
            if(!calibrated){
                long long visits=0;for(int root=0;root<N;root++){Bits direct{};walk(root,3,direct,visits);assert(direct==bits[root]);}
                assert(visits==1LL*N*585);
                ofstream cal(directory+"/first_proposal_calibration.json");
                cal<<"{\"status\":\"MATCH\",\"start\":0,\"legal_proposal\":1,\"candidate_bad_unordered_pairs\":"<<candidate
                   <<",\"roots\":312,\"direct_walks_len0_to3_per_root\":585,\"direct_walk_visits_total\":"<<visits
                   <<",\"all312x312_reachability_bits_match\":true,\"formal_proposal_reused\":true,\"graph_BFS_performed\":false}\n";
                calibrated=true;
            }
            double temperature=30.0*pow(1.0/30.0,double(s.legal-1)/999.0);
            bool accept=candidate<=current||generate_canonical<double,53>(rng)<exp(double(current-candidate)/temperature);
            if(accept){if(candidate<current)s.improvements++;current=candidate;s.accepted++;}
            else{change(part,new0,new1,old0,old1);factors[part][i]=old0;factors[part][j]=old1;}
            if(current<best){best=current;save_graph(best,start,s.legal,seeds[start]);}
            if(current==0){hit=true;cout<<"HIT start="<<start<<" proposal="<<s.legal<<endl;}
            if(s.legal%100==0)progress<<"{\"start\":"<<start<<",\"legal\":"<<s.legal<<",\"current\":"<<current<<",\"best\":"<<best<<"}\n";
        }
        s.final=current;stats.push_back(s);cout<<"END "<<start<<" legal="<<s.legal<<" final="<<current<<" best="<<best<<" CPU="<<cpu()<<endl;
    }
    ofstream r(directory+"/search_result.json");
    r<<"{\"status\":\""<<(hit?"HIT_CANDIDATE_PENDING_ROOT_BFS":limit?"CPU_LIMIT_INCOMPLETE_PROFILE":"TWO_FIXED_2FACTOR_PROFILES_COMPLETE_NO_HIT")
     <<"\",\"n\":312,\"edges\":1248,\"max_degree\":8,\"target_D\":3,\"savedL\":253,\"best_bad_unordered_pairs_predicted\":"<<best
     <<",\"first_formal_proposal_calibrated\":"<<(calibrated?"true":"false")<<",\"producer_graph_BFS_performed\":false,\"CPU_seconds\":"<<cpu()
     <<",\"native_internal_CPU_limit\":"<<budget<<",\"native_soft_CPU_limit\":18,\"native_hard_CPU_limit\":20,\"workers\":1,\"starts_planned\":2,\"starts_actual\":"<<stats.size()<<",\"profiles\":[";
    for(size_t i=0;i<stats.size();i++){if(i)r<<',';auto s=stats[i];r<<"{\"start\":"<<s.start<<",\"seed\":"<<seeds[s.start]<<",\"initial_bad\":"<<s.initial<<",\"final_bad\":"<<s.final<<",\"raw\":"<<s.raw<<",\"legal\":"<<s.legal<<",\"illegal_rejects\":"<<s.rejected<<",\"accepted\":"<<s.accepted<<",\"strict_improvements\":"<<s.improvements<<'}';}
    r<<"]}\n";
}

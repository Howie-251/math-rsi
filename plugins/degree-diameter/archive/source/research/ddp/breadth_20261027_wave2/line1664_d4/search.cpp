#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
constexpr int BASE=104, M=208, FIBER=16, N=1664;
struct Edge{int u,v;};
struct State{array<int,M>b,v;};
vector<Edge>E;
vector<pair<int,int>>ADJ[BASE];
uint16_t PERM[FIBER][65536];
uint8_t PC[65536];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void init(){
    for(int m=0;m<65536;m++){
        PC[m]=__builtin_popcount((unsigned)m);
        for(int a=0;a<FIBER;a++){
            unsigned z=0;
            for(int x=0;x<FIBER;x++)if((m>>x)&1)z|=1U<<(x^a);
            PERM[a][m]=z;
        }
    }
}
long score(const State&s,ostream*out=nullptr){
    long deficits=0;
    for(int root=0;root<BASE;root++){
        uint16_t seen[BASE]={},front[BASE]={},next[BASE]={};
        seen[root]=front[root]=1;
        for(int depth=0;depth<4;depth++){
            fill(next,next+BASE,0);
            for(int u=0;u<BASE;u++)if(front[u]){
                auto mask=front[u];
                for(auto [v,e]:ADJ[u])next[v]|=PERM[s.b[e]][mask]|PERM[s.b[e]^s.v[e]][mask];
            }
            for(int u=0;u<BASE;u++){
                front[u]=next[u]&uint16_t(~seen[u]);
                seen[u]|=front[u];
            }
        }
        int reached=0;
        for(auto mask:seen)reached+=PC[mask];
        deficits+=N-reached;
        if(out){for(auto mask:seen)*out<<mask<<' ';*out<<'\n';}
    }
    return 8*deficits;
}
void savebest(const State&s,long val,int start,int step,long evals){
    ofstream f("best_parameters.json");
    f<<"{\"bad_unordered_pairs\":"<<val<<",\"start\":"<<start<<",\"step\":"<<step<<",\"evaluation\":"<<evals<<",\"offsets\":[";
    for(int i=0;i<M;i++){if(i)f<<',';f<<s.b[i];}
    f<<"],\"directions\":[";
    for(int i=0;i<M;i++){if(i)f<<',';f<<s.v[i];}
    f<<"]}\n";
}
int main(int argc,char**argv){
    init();ifstream in("inputs.txt");int base,m;in>>base>>m;
    if(base!=BASE||m!=M)return 3;
    for(int e=0;e<M;e++){
        Edge x;in>>x.u>>x.v;E.push_back(x);
        ADJ[x.u].push_back({x.v,e});ADJ[x.v].push_back({x.u,e});
    }
    vector<State>starts(4);
    for(auto&s:starts){for(auto&x:s.b)in>>x;for(auto&x:s.v)in>>x;}
    if(argc>1&&string(argv[1])=="calibrate"){
        ofstream f("first_reachable.txt");long val=score(starts[0],&f);
        ofstream q("first_score.txt");q<<val<<'\n';return 0;
    }
    const double budget=stod(argv[2]),began=cpu();
    long best=1000000000,evals=0,accepted=0,done=0;
    int completed=0,cursor_start=0,cursor_step=-1;
    bool timeout=false,hit=false;
    ifstream cachedfile("first_score.txt");long cached;cachedfile>>cached;
    mt19937_64 rng(20261027402ULL);uniform_real_distribution<double>U(0.,1.);
    for(int k=0;k<4&&!timeout&&!hit;k++){
        cursor_start=k;cursor_step=-1;State s=starts[k];
        long val=k==0?cached:score(s);evals++;
        if(val<best){best=val;savebest(s,val,k,-1,evals);}
        if(!val){hit=true;break;}
        for(int step=0;step<2000;step++){
            cursor_step=step;
            if((step&15)==0&&cpu()-began>budget){timeout=true;break;}
            int e=rng()%M,type=rng()%2;
            int*ptr=type?&s.v[e]:&s.b[e];int old=*ptr,next;
            do{next=type?1+rng()%15:rng()%16;}while(next==old);
            *ptr=next;long trial=score(s);evals++;done++;
            if(trial<best){best=trial;savebest(s,trial,k,step,evals);}
            if(!trial){hit=true;val=0;break;}
            double phase=double(step%500)/499.,temperature=1000.*pow(.002,phase);
            if(trial<=val||U(rng)<exp(double(val-trial)/temperature)){val=trial;accepted++;}
            else *ptr=old;
        }
        if(!timeout&&!hit)completed++;
    }
    ofstream f("production_terminal.json");
    f<<"{\"status\":\""<<(hit?"FOUND_D4":timeout?"CPU_BUDGET_NO_D4":"COMPLETE_4_START_PROFILE_NO_D4")
     <<"\",\"running\":false,\"starts_completed\":"<<completed<<",\"coordinate_updates\":"<<done
     <<",\"score_evaluations_including_cached_first\":"<<evals<<",\"first_score_reused\":true,\"accepted\":"<<accepted
     <<",\"best_bad_unordered_pairs\":"<<best<<",\"production_CPU_seconds\":"<<cpu()-began
     <<",\"production_budget_seconds\":"<<budget<<",\"found_D4\":"<<(hit?"true":"false")
     <<",\"scope_exhausted\":"<<(!timeout&&!hit?"true":"false")<<",\"entire_family_exhausted\":false"
     <<",\"cursor\":{\"start\":"<<cursor_start<<",\"step\":"<<cursor_step<<"}}\n";
    cout<<"best="<<best<<" updates="<<done<<" cpu="<<cpu()-began<<'\n';
}

#include <algorithm>
#include <array>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
struct Edge {int u,v,single;};
struct State {array<int,360>b,v;array<int,120>s;};
vector<Edge>E;
vector<pair<int,int>>ADJ[120];
unsigned char XOR[8][256];
int PC[256];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void init(){
    for(int m=0;m<256;m++){
        PC[m]=__builtin_popcount((unsigned)m);
        for(int a=0;a<8;a++){
            int z=0;for(int x=0;x<8;x++)if(m>>x&1)z|=1<<(x^a);
            XOR[a][m]=z;
        }
    }
}
long score(const State&st,vector<int>*def=nullptr){
    long sum=0;
    for(int root=0;root<120;root++){
        unsigned char seen[120]={},front[120]={},nxt[120]={};
        seen[root]=front[root]=1;
        for(int depth=0;depth<3;depth++){
            fill(nxt,nxt+120,0);
            for(int u=0;u<120;u++)if(front[u]){
                unsigned char x=front[u];
                nxt[u]|=XOR[st.s[u]][x];
                for(auto [v,e]:ADJ[u]){
                    nxt[v]|=XOR[st.b[e]][x];
                    if(!E[e].single)nxt[v]|=XOR[st.b[e]^st.v[e]][x];
                }
            }
            for(int u=0;u<120;u++){front[u]=nxt[u]&~seen[u];seen[u]|=front[u];}
        }
        int reached=0;for(int u=0;u<120;u++)reached+=PC[seen[u]];
        int miss=960-reached;sum+=miss;if(def)def->push_back(miss);
    }
    return 4*sum;
}
void savebest(const State&s,long val,int start,int step,long evals){
    ofstream f("best_parameters.json");
    f<<"{\"bad_unordered_pairs\":"<<val<<",\"start\":"<<start<<",\"step\":"<<step<<",\"evaluation\":"<<evals<<",\"offsets\":[";
    for(int i=0;i<360;i++){if(i)f<<",";f<<s.b[i];}f<<"],\"directions\":[";
    for(int i=0;i<360;i++){if(i)f<<",";f<<s.v[i];}f<<"],\"internal_shifts\":[";
    for(int i=0;i<120;i++){if(i)f<<",";f<<s.s[i];}f<<"]}\n";
}
int main(int argc,char**argv){
    init();ifstream in("inputs.txt");int n,m;in>>n>>m;if(n!=120||m!=360)return 3;
    for(int e=0;e<m;e++){Edge x;in>>x.u>>x.v>>x.single;E.push_back(x);ADJ[x.u].push_back({x.v,e});ADJ[x.v].push_back({x.u,e});}
    vector<State>starts(4);
    for(auto &s:starts){for(int &x:s.b)in>>x;for(int &x:s.v)in>>x;for(int &x:s.s)in>>x;}
    if(string(argv[1])=="calibrate"){
        vector<int>d;long val=score(starts[0],&d);ofstream f("first_score.txt");f<<val<<"\n";for(int x:d)f<<x<<" ";f<<"\n";
        return 0;
    }
    double budget=stod(argv[2]);double began=cpu();long best=1000000000,evals=0,accepted=0;int completed=0,done=0;bool timeout=false,hit=false;
    ifstream first("first_score.txt");long cached;first>>cached;
    mt19937_64 rng(20261027305ULL);uniform_real_distribution<double>U(0.0,1.0);
    vector<pair<int,int>>vars;for(int e=0;e<360;e++)vars.push_back({0,e});for(int e=0;e<360;e++)if(!E[e].single)vars.push_back({1,e});for(int u=0;u<120;u++)vars.push_back({2,u});
    for(int k=0;k<4 && !timeout && !hit;k++){
        State st=starts[k];long val=(k==0?cached:score(st));evals++;
        if(val<best){best=val;savebest(st,val,k,-1,evals);}
        if(!val){hit=true;break;}
        for(int step=0;step<5000;step++){
            if((step&15)==0 && cpu()-began>budget){timeout=true;break;}
            auto [type,index]=vars[rng()%vars.size()];int *p=type==0?&st.b[index]:type==1?&st.v[index]:&st.s[index];int old=*p,lo=(type==0?0:1),range=(type==0?8:7),next;
            do{next=lo+rng()%range;}while(next==old);*p=next;
            long trial=score(st);evals++;done++;
            if(trial<best){best=trial;savebest(st,trial,k,step,evals);}
            if(!trial){hit=true;val=0;break;}
            double phase=double(step%1250)/1249.;double temp=150.*pow(0.004,phase);
            if(trial<=val || U(rng)<exp(double(val-trial)/temp)){val=trial;accepted++;}else *p=old;
        }
        if(!timeout&&!hit)completed++;
    }
    ofstream f("production_terminal.json");f<<"{\"status\":\""<<(hit?"FOUND_D3":timeout?"CPU_BUDGET_NO_D3":"COMPLETE_4_START_PROFILE_NO_D3")<<"\",\"starts_completed\":"<<completed<<",\"coordinate_updates\":"<<done<<",\"score_evaluations_including_cached_first\":"<<evals<<",\"cached_first_reused\":true,\"accepted\":"<<accepted<<",\"best_bad_unordered_pairs\":"<<best<<",\"production_CPU_seconds\":"<<cpu()-began<<",\"production_budget_seconds\":"<<budget<<",\"found_D3\":"<<(hit?"true":"false")<<",\"scope_exhausted\":"<<(!timeout&&!hit?"true":"false")<<",\"entire_family_exhausted\":false,\"running\":false}\n";
    cout<<"best="<<best<<" updates="<<done<<" cpu="<<cpu()-began<<"\n";
}

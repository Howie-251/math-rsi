#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

// One worker; fixed three starts, 50 CPU seconds each. No graph expansion.
struct RNG {
    uint64_t x;
    uint64_t next() { x ^= x << 13; x ^= x >> 7; x ^= x << 17; return x; }
    int pick(int n) { return int(next() % n); }
    double unit() { return (next() >> 11) * 0x1.0p-53; }
};
struct Run {
    int n;
    const vector<vector<int>>& adj;
    vector<int> st, c1, c2, cost, bad, pos, bestlegal, bestnear;
    int S = 0, V = 0, bestS = 0, nearS = 0, nearV = 0;
    uint64_t proposals = 0, accepted = 0;
    explicit Run(const vector<vector<int>>& a, vector<int> s): n(a.size()), adj(a), st(move(s)),
        c1(n), c2(n), cost(n), pos(n, -1), bestlegal(n, 0) {
        for(int u=0;u<n;u++) { S += st[u]!=0; for(int v:adj[u]) {c1[u]+=st[v]==1;c2[u]+=st[v]==2;} }
        for(int u=0;u<n;u++) refresh(u);
        nearS=S; nearV=V; bestnear=st;
        if(V==0) {bestS=S;bestlegal=st;}
    }
    static int val(int s,int a,int b) {
        int load = s==0 ? a+b : s==1 ? a : b;
        int e=max(0,load-2);
        return (s==0?1:2)*e*e;
    }
    void refresh(int u) {
        int z=val(st[u],c1[u],c2[u]);V += z-cost[u];cost[u]=z;
        if(z && pos[u]<0) {pos[u]=bad.size();bad.push_back(u);}
        if(!z && pos[u]>=0) {int j=pos[u],v=bad.back();bad[j]=v;pos[v]=j;bad.pop_back();pos[u]=-1;}
    }
    int delta(int u,int s) const {
        int old=st[u], d=val(s,c1[u],c2[u])-cost[u];
        for(int v:adj[u]) d+=val(st[v],c1[v]+(s==1)-(old==1),c2[v]+(s==2)-(old==2))-cost[v];
        return d;
    }
    void apply(int u,int s) {
        int old=st[u];S+=(s!=0)-(old!=0);
        for(int v:adj[u]) {c1[v]+=(s==1)-(old==1);c2[v]+=(s==2)-(old==2);}
        st[u]=s;refresh(u);for(int v:adj[u])refresh(v);
        if(V==0 && S>bestS) {bestS=S;bestlegal=st;}
    }
    bool exact() const {
        int ss=0,vv=0;
        for(int u=0;u<n;u++) {int a=0,b=0;ss+=st[u]!=0;for(int v:adj[u]){a+=st[v]==1;b+=st[v]==2;}
            if(a!=c1[u]||b!=c2[u])return false;vv+=val(st[u],a,b);}
        return ss==S && vv==V;
    }
};
void save(const string& path,const vector<int>& st) {
    ofstream o(path);for(size_t i=0;i<st.size();i++)o<<st[i]<<(i+1==st.size()?'\n':' ');
}
int main(int argc,char**argv) {
    string dir=argc>1?argv[1]:".";ifstream in(dir+"/input.txt");int n;in>>n;
    vector<vector<int>> adj(n);for(auto& row:adj){int d;in>>d;row.resize(d);for(int&v:row)in>>v;}
    vector<vector<int>> starts(3,vector<int>(n));for(auto&s:starts)for(int&x:s)in>>x;
    if(!in || n!=33033)return 2;
    ofstream log(dir+"/search_log.jsonl");
    const uint64_t seeds[]={202610270401ULL,202610270402ULL,202610270403ULL};
    int globalbest=0;bool target=false;clock_t batch=clock();
    for(int k=0;k<3 && !target;k++) {
        Run r(adj,starts[k]);RNG rng{seeds[k]};int initialS=r.S,initialV=r.V;
        clock_t start=clock();double elapsed=0,nextlog=10;int phase=-1;
        // Phases: 0..33 anneal; 33..40 increasing penalty repair;
        // 40..50 feasible-only exchange if legal; otherwise continue exact repair.
        while(elapsed<50) {
            if((r.proposals&2047)==0) {
                elapsed=double(clock()-start)/CLOCKS_PER_SEC;
                if(elapsed>=50)break;
                if(elapsed>=nextlog) {
                    cout<<"start "<<k<<" cpu "<<elapsed<<" S "<<r.S<<" V "<<r.V<<" bestlegal "<<r.bestS<<endl;
                    nextlog+=10;
                }
            }
            int ph=elapsed<33?0:elapsed<40?1:2;
            if(ph!=phase) {
                if(ph==1) {r.nearS=r.S;r.nearV=r.V;r.bestnear=r.st;}
                if(ph==2 && r.bestS>0) {
                    // Prefer a certified feasible basin for final legal exchanges.
                    r.st=r.bestlegal;fill(r.c1.begin(),r.c1.end(),0);fill(r.c2.begin(),r.c2.end(),0);
                    fill(r.cost.begin(),r.cost.end(),0);fill(r.pos.begin(),r.pos.end(),-1);r.bad.clear();r.V=0;r.S=r.bestS;
                    for(int u=0;u<n;u++)for(int v:adj[u]){r.c1[u]+=r.st[v]==1;r.c2[u]+=r.st[v]==2;}
                    for(int u=0;u<n;u++)r.refresh(u);
                }
                phase=ph;
            }
            int u;
            if(!r.bad.empty() && rng.unit()<.75) {
                int b=r.bad[rng.pick(r.bad.size())];
                u=rng.unit()<.35?b:adj[b][rng.pick(adj[b].size())];
            } else u=rng.pick(n);
            int ns=rng.pick(2);if(ns>=r.st[u])ns++;
            int dv=r.delta(u,ns),ds=(ns!=0)-(r.st[u]!=0);
            double penalty,temp;
            bool legalphase=ph==2 && r.V==0;
            if(ph==0) {double f=elapsed/33;penalty=.75+5.25*f*f;temp=1.25*pow(.08/1.25,f);}
            else if(ph==1) {double f=(elapsed-33)/7;penalty=8+92*f;temp=.5*(1-f)+.025;}
            else {penalty=100;temp=.30*pow(.025/.30,(elapsed-40)/10);}
            double de=penalty*dv-ds;
            bool ok=legalphase ? (dv==0 && (ds>=0 || rng.unit()<exp(double(ds)/temp))) : (de<=0 || rng.unit()<exp(-de/temp));
            r.proposals++;
            if(ok){r.apply(u,ns);r.accepted++;}
            if(r.V==0 && r.S>=8946) {target=true;break;}
        }
        elapsed=double(clock()-start)/CLOCKS_PER_SEC;
        if(!r.exact())return 3;
        save(dir+"/start"+to_string(k)+"_best_legal.states",r.bestlegal);
        save(dir+"/start"+to_string(k)+"_anneal_end.states",r.bestnear);
        save(dir+"/start"+to_string(k)+"_final.states",r.st);
        if(r.bestS>globalbest){globalbest=r.bestS;save(dir+"/best_legal.states",r.bestlegal);}
        log<<"{\"start\":"<<k<<",\"seed\":"<<seeds[k]<<",\"initial_S\":"<<initialS<<",\"initial_weighted_squared_excess\":"<<initialV
           <<",\"best_legal_S\":"<<r.bestS<<",\"anneal_end_S\":"<<r.nearS<<",\"anneal_end_weighted_squared_excess\":"<<r.nearV
           <<",\"final_S\":"<<r.S<<",\"final_weighted_squared_excess\":"<<r.V<<",\"proposals\":"<<r.proposals<<",\"accepted\":"<<r.accepted
           <<",\"CPU_seconds\":"<<setprecision(9)<<elapsed<<",\"incremental_state_exact_recheck\":true}"<<endl;
        cout<<"DONE "<<k<<" bestlegal "<<r.bestS<<" final "<<r.S<<" V "<<r.V<<" cpu "<<elapsed<<endl;
    }
    ofstream out(dir+"/batch_result.json");
    out<<"{\"status\":\""<<(target?"LEGAL_TARGET_REACHED":"BOUNDED_BATCH_COMPLETE_NO_TARGET")<<"\",\"best_legal_S\":"<<globalbest
       <<",\"best_legal_core_order\":"<<33397+globalbest<<",\"search_CPU_seconds\":"<<setprecision(9)<<double(clock()-batch)/CLOCKS_PER_SEC
       <<",\"target_S\":8946,\"worker_count\":1,\"additional_batches\":0,\"full_graph_generated\":false}"<<endl;
    return 0;
}

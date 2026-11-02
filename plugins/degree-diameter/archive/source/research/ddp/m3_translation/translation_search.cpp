#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

struct Arc {int v,e;};
struct Route {int source,target,a,b,c,length;};
static int plus3(int x,int y) {
    int z=0,p=1;
    for(int i=0;i<3;i++){z+=((x%3+y%3)%3)*p;x/=3;y/=3;p*=3;}
    return z;
}
static int twice3(int x){return plus3(x,x);}

int main(int argc,char**argv){
    if(argc!=5){cerr<<"usage: translation_search CONTROL.edges OUTPUT.json SECONDS SEED\n";return 1;}
    double budget=stod(argv[3]);uint64_t seed=stoull(argv[4]);
    ifstream input(argv[1]);if(!input){cerr<<"cannot read control edges\n";return 1;}
    vector<pair<int,int>>edges;string line;int n=0;
    while(getline(input,line)){
        if(line.empty()||line[0]=='#')continue;
        istringstream in(line);int u,v;if(!(in>>u>>v))return 1;
        if(u<0||v<0||u==v){cerr<<"invalid edge\n";return 1;}
        if(u>v)swap(u,v);edges.push_back({u,v});n=max(n,v+1);
    }
    sort(edges.begin(),edges.end());
    if(adjacent_find(edges.begin(),edges.end())!=edges.end()){cerr<<"duplicate edge\n";return 1;}
    vector<vector<Arc>>adj(n);
    for(int e=0;e<(int)edges.size();e++){
        auto[u,v]=edges[e];adj[u].push_back({v,e});adj[v].push_back({u,e});
    }
    for(auto&ns:adj)if(ns.size()!=4){cerr<<"control not 4-regular\n";return 1;}
    vector<Route>routes;vector<int>A3(n*n,0);
    for(int s=0;s<n;s++)for(auto a:adj[s]){
        routes.push_back({s,a.v,a.e,0,0,1});
        for(auto b:adj[a.v]){
            routes.push_back({s,b.v,a.e,b.e,0,2});
            for(auto c:adj[b.v]){
                routes.push_back({s,c.v,a.e,b.e,c.e,3});A3[s*n+c.v]++;
            }
        }
    }
    int control_zeros=count(A3.begin(),A3.end(),0);
    if(control_zeros){cerr<<"REJECT: "<<control_zeros<<" zero entries of A^3; no fiber search\n";return 2;}

    // Normalize projective directions by first nonzero little-endian coordinate.
    vector<int>directions;
    for(int x=1;x<27;x++){
        int a=x;while(a%3==0)a/=3;if(a%3==1)directions.push_back(x);
    }
    if(directions.size()!=13)return 1;
    array<uint32_t,13>single{};array<array<uint32_t,13>,13>pairmask{};
    array<array<array<uint32_t,13>,13>,13>triple{};
    for(int a=0;a<13;a++){
        int va[3]={0,directions[a],twice3(directions[a])};
        for(int x:va)single[a]|=1u<<x;
        for(int b=0;b<13;b++){
            int vb[3]={0,directions[b],twice3(directions[b])};
            for(int x:va)for(int y:vb)pairmask[a][b]|=1u<<plus3(x,y);
            for(int c=0;c<13;c++){
                int vc[3]={0,directions[c],twice3(directions[c])};
                for(int x:va)for(int y:vb)for(int z:vc)triple[a][b][c]|=1u<<plus3(plus3(x,y),z);
            }
        }
    }
    vector<uint32_t>reached(n*n);
    auto evaluate=[&](const vector<int>&labels){
        fill(reached.begin(),reached.end(),0);
        for(int s=0;s<n;s++)reached[s*n+s]=1;
        for(auto&r:routes){
            uint32_t mask;
            if(r.length==1)mask=single[labels[r.a]];
            else if(r.length==2)mask=pairmask[labels[r.a]][labels[r.b]];
            else mask=triple[labels[r.a]][labels[r.b]][labels[r.c]];
            reached[r.source*n+r.target]|=mask;
        }
        int missing=0;for(uint32_t mask:reached)missing+=27-__builtin_popcount(mask);
        return missing;
    };
    mt19937_64 rng(seed);vector<int>labels(edges.size()),best_labels;
    int best=27*n*n;uint64_t iterations=0,restarts=0;
    auto begin=chrono::steady_clock::now();
    auto elapsed=[&](){return chrono::duration<double>(chrono::steady_clock::now()-begin).count();};
    auto save=[&](const string&status){
        int verified_score=evaluate(best_labels);
        if(verified_score!=best){cerr<<"score recomputation mismatch\n";exit(3);}
        ofstream out(argv[2]);
        out<<"{\n  \"status\": \""<<status<<"\",\n  \"family\": \"translation_only_F3_cubed_lines\",\n"
           <<"  \"source_control\": \""<<argv[1]<<"\",\n  \"control_order\": "<<n<<",\n"
           <<"  \"lift_order\": "<<27*n<<",\n  \"degree\": 12,\n  \"diameter_target\": 3,\n"
           <<"  \"missing_from_control_roots_fiber_zero\": "<<best<<",\n  \"seed\": "<<seed<<",\n"
           <<"  \"iterations\": "<<iterations<<",\n  \"restarts\": "<<restarts<<",\n"
           <<"  \"budget_seconds\": "<<budget<<",\n  \"elapsed_seconds\": "<<elapsed()<<",\n"
           <<"  \"vector_encoding\": \"x0+3*x1+9*x2\",\n  \"edge_directions\": [\n";
        for(int e=0;e<(int)edges.size();e++){
            auto[u,v]=edges[e];out<<"    ["<<u<<","<<v<<","<<directions[best_labels[e]]<<"]";
            out<<(e+1==(int)edges.size()?"\n":",\n");
        }
        out<<"  ],\n  \"missing_by_control_pair\": [\n";
        bool first=true;
        for(int s=0;s<n;s++)for(int t=0;t<n;t++){
            int missing=27-__builtin_popcount(reached[s*n+t]);
            if(missing){if(!first)out<<",\n";first=false;out<<"    ["<<s<<","<<t<<","<<missing<<"]";}
        }
        out<<"\n  ]\n}\n";
    };
    do{
        for(int&e:labels)e=rng()%13;
        int current=evaluate(labels);restarts++;double restart_time=elapsed();
        if(current<best){best=current;best_labels=labels;save("in_progress");}
        while(elapsed()<budget&&elapsed()-restart_time<12&&best){
            int edge=rng()%labels.size(),old=labels[edge];
            labels[edge]=(old+1+rng()%12)%13;
            int next=evaluate(labels);iterations++;
            double age=(elapsed()-restart_time)/12;
            double temperature=40*pow(.05,age);
            if(next<=current||generate_canonical<double,53>(rng)<exp((current-next)/temperature))current=next;
            else labels[edge]=old;
            if(current<best){
                best=current;best_labels=labels;
                cout<<"best_missing="<<best<<" iterations="<<iterations<<" seconds="<<elapsed()<<"\n"<<flush;
                save(best?"in_progress":"candidate_zero_missing");
            }
        }
    }while(elapsed()<budget&&best);
    save(best?"budget_complete_not_valid":"candidate_zero_missing");
    cout<<"FINAL order="<<27*n<<" best_missing="<<best<<" iterations="<<iterations<<" seconds="<<elapsed()<<"\n";
}

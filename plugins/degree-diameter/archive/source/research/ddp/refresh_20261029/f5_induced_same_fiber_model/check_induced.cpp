#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

// Candidate checking only; no generation, source-distance check, or optimization.
int main(int argc,char**argv) {
    if(argc!=4) return 2;
    const double started=double(clock())/CLOCKS_PER_SEC;
    const double allowance=stod(argv[3]);
    auto elapsed=[&](){return double(clock())/CLOCKS_PER_SEC-started;};
    array<array<uint16_t,20>,3750> adj;
    ifstream source(argv[1],ios::binary);
    source.read(reinterpret_cast<char*>(adj.data()),sizeof(adj));
    if(source.gcount()!=sizeof(adj)) return 2;
    ifstream input(argv[2]);
    int n;input>>n;
    vector<int> kept(n);
    array<bool,3750> selected{};
    for(int &v:kept) {
        input>>v;
        if(!input || v<0 || v>=3750 || selected[v]) return 2;
        selected[v]=true;
    }
    sort(kept.begin(),kept.end());
    int maxdegree=0,mindegree=20,twice_edges=0;
    for(int v:kept) {
        int d=0;for(int w:adj[v])d+=selected[w];
        maxdegree=max(maxdegree,d);mindegree=min(mindegree,d);twice_edges+=d;
    }
    if(n<1921 || maxdegree>16) {
        cout<<"{\"status\":\"ENCODING_OR_MODEL_ERROR\",\"n\":"<<n
            <<",\"max_degree\":"<<maxdegree<<"}\n";
        return 2;
    }
    array<int,3750> component;component.fill(-1);
    vector<vector<int>> components;
    array<int,3750> queue;
    for(int root:kept)if(component[root]<0) {
        int id=components.size(),head=0,tail=0;
        components.push_back({});component[root]=id;queue[tail++]=root;
        while(head<tail) {
            int v=queue[head++];components.back().push_back(v);
            for(int w:adj[v])if(selected[w] && component[w]<0) {
                component[w]=id;queue[tail++]=w;
            }
        }
        sort(components.back().begin(),components.back().end());
    }
    int large=-1;
    for(int i=0;i<int(components.size());++i)if(components[i].size()>1920) {
        if(large>=0)return 2; // Impossible for at most 3750 selected vertices.
        large=i;
    }
    // A unique large component may itself be a valid target. If it fails,
    // its internal missing pairs are still missing in the whole candidate.
    const vector<int>& targets=large>=0?components[large]:kept;
    array<int,3750> stamp{},depth{};
    int token=0,roots=0;
    bool timed_out=false;
    vector<pair<int,int>> bad;
    set<pair<int,int>> bad_set;
    for(int root:targets) {
        if(elapsed()>=allowance) {timed_out=true;break;}
        ++token;stamp[root]=token;depth[root]=0;
        int head=0,tail=0;queue[tail++]=root;
        while(head<tail) {
            int v=queue[head++];if(depth[v]==3)continue;
            for(int w:adj[v])if(selected[w] && stamp[w]!=token) {
                stamp[w]=token;depth[w]=depth[v]+1;queue[tail++]=w;
            }
        }
        ++roots;
        // At most one new unordered counterexample per checked root.
        for(int v:targets)if(stamp[v]!=token) {
            auto p=minmax(root,v);
            if(bad_set.insert(p).second) {bad.push_back(p);break;}
        }
        if(bad.size()==128)break;
    }
    bool all_roots=roots==int(targets.size());
    bool hit=!timed_out && all_roots && bad.empty();
    string status=timed_out?"CHECK_BUDGET_STOP":hit?"D3_HIT":"R3_COUNTEREXAMPLES";
    cout<<"{\"status\":\""<<status<<"\",\"candidate_n\":"<<n
        <<",\"candidate_m\":"<<twice_edges/2
        <<",\"candidate_min_degree\":"<<mindegree
        <<",\"candidate_max_degree\":"<<maxdegree
        <<",\"component_sizes\":[";
    for(int i=0;i<int(components.size());++i) {if(i)cout<<',';cout<<components[i].size();}
    cout<<"],\"checked_target_n\":"<<targets.size()
        <<",\"checked_scope\":\""<<(large>=0?"unique_component_above1920":"whole_candidate")
        <<"\",\"R3_roots_checked\":"<<roots
        <<",\"all_scope_roots_checked\":"<<(all_roots?"true":"false")
        <<",\"witness_pairs_are_not_global_bad_pair_count\":true,\"bad_pairs_old_ids\":[";
    for(int i=0;i<int(bad.size());++i) {if(i)cout<<',';cout<<'['<<bad[i].first<<','<<bad[i].second<<']';}
    cout<<"],\"CPU_seconds\":"<<elapsed();
    if(hit) {
        cout<<",\"accepted_old_ids\":[";
        for(int i=0;i<int(targets.size());++i) {if(i)cout<<',';cout<<targets[i];}
        cout<<"],\"component_extraction\":"<<(targets.size()!=kept.size()?"true":"false");
    }
    cout<<"}\n";
    return timed_out?3:hit?0:1;
}

// Independent finite verification of exactly ten saved matching augmentations.
// This program never chooses or changes an edge and performs no search.
#include <algorithm>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

using Edge = pair<int,int>;
struct Graph {
    int n;
    set<Edge> edges;
    vector<vector<int>> adj;
};

Graph read_graph(const string& path) {
    ifstream in(path);
    int n; long long m;
    if (!(in >> n >> m) || n < 1 || m < 0) throw runtime_error("invalid graph header: " + path);
    Graph g{n, {}, vector<vector<int>>(n)};
    for (long long i=0; i<m; ++i) {
        int u,v;
        if (!(in >> u >> v) || u<0 || v<0 || u>=n || v>=n || u==v)
            throw runtime_error("invalid/missing edge or loop: " + path);
        if (u>v) swap(u,v);
        if (!g.edges.emplace(u,v).second) throw runtime_error("duplicate edge: " + path);
        g.adj[u].push_back(v); g.adj[v].push_back(u);
    }
    string extra;
    if (in >> extra) throw runtime_error("extra input after declared edges: " + path);
    return g;
}

template<class T> void map_json(ostream& out, const map<int,T>& values) {
    out << "{"; bool comma=false;
    for (auto [k,v]:values) {if(comma)out<<",";comma=true;out<<"\""<<k<<"\":"<<v;}
    out << "}";
}
void edges_json(ostream& out, const vector<Edge>& edges) {
    out << "[";
    for(size_t i=0;i<edges.size();++i){if(i)out<<",";out<<"["<<edges[i].first<<","<<edges[i].second<<"]";}
    out << "]";
}

struct RootCheck {
    int root=0, max_finite_distance=0, missing=0, unreachable=0;
    map<int,long long> histogram;
};

vector<int> multi_source_distances(const vector<vector<int>>& adj, const vector<int>& sources) {
    constexpr int INF=1000000000;
    vector<int> distances(adj.size(),INF),queue(adj.size());int head=0,end=0;
    for(int s:sources)if(s<(int)adj.size() && distances[s]==INF){distances[s]=0;queue[end++]=s;}
    while(head<end){int u=queue[head++];for(int v:adj[u])if(distances[v]==INF){distances[v]=distances[u]+1;queue[end++]=v;}}
    return distances;
}

string check_one(const Graph& source, const string& path, int id) {
    auto start=chrono::steady_clock::now(); clock_t cpu_start=clock();
    Graph g=read_graph(path);
    if(g.n!=2812)throw runtime_error("candidate order is not 2812: "+path);
    constexpr int OLD=2810,U=2810,V=2811,D=5;
    vector<Edge> removed,added;
    set_difference(source.edges.begin(),source.edges.end(),g.edges.begin(),g.edges.end(),back_inserter(removed));
    set_difference(g.edges.begin(),g.edges.end(),source.edges.begin(),source.edges.end(),back_inserter(added));
    set<int> endpoints;
    bool matching=removed.size()==6;
    for(auto [a,b]:removed){matching &= a<OLD && b<OLD; endpoints.insert(a);endpoints.insert(b);}
    matching &= endpoints.size()==12;
    bool additions=added.size()==13 && g.edges.count({U,V})==1;
    int ua=0,va=0;
    for(auto [a,b]:added){
        if(a==U && b==V)continue;
        if(a<OLD && b==U)++ua;
        else if(a<OLD && b==V)++va;
        else additions=false;
    }
    additions &= ua==6 && va==6;
    bool orientations=matching;
    for(auto [a,b]:removed){
        bool au=g.edges.count({a,U}),av=g.edges.count({a,V});
        bool bu=g.edges.count({b,U}),bv=g.edges.count({b,V});
        orientations &= (au && bv && !av && !bu) || (av && bu && !au && !bv);
    }
    bool exact_augmentation=matching && additions && orientations;
    constexpr int INF=1000000000;
    vector<vector<int>> h_adj(OLD);
    for(auto [a,b]:source.edges)if(g.edges.count({a,b})){h_adj[a].push_back(b);h_adj[b].push_back(a);}
    vector<int> a_distance=multi_source_distances(h_adj,g.adj[U]);
    vector<int> b_distance=multi_source_distances(h_adj,g.adj[V]);
    vector<int> h_dist(OLD),h_queue(OLD);
    long long h_bad=0,h_repaired=0,h_residual=0,h_unreachable=0;
    long long old_formula_mismatches=0,new_formula_mismatches=0;
    int h_diameter=0;
    map<int,long long> degree_histogram;
    for(auto& row:g.adj)degree_histogram[row.size()]++;
    bool regular=degree_histogram.size()==1 && degree_histogram.begin()->first==7;
    long long bad_oo=0,bad_no=0,bad_uv=0,unreachable=0;
    map<int,long long> full_histogram;
    vector<Edge> witnesses_oo,witnesses_no,witnesses_uv;
    vector<RootCheck> new_roots;
    vector<int> dist(g.n),queue(g.n);
    int diameter=0;
    for(int root=0;root<g.n;++root){
        fill(dist.begin(),dist.end(),-1); int head=0,end=1;queue[0]=root;dist[root]=0;
        while(head<end){int u=queue[head++];for(int v:g.adj[u])if(dist[v]<0){dist[v]=dist[u]+1;queue[end++]=v;}}
        if(root<OLD){
            fill(h_dist.begin(),h_dist.end(),INF);int h_head=0,h_end=1;h_queue[0]=root;h_dist[root]=0;
            while(h_head<h_end){int u=h_queue[h_head++];for(int v:h_adj[u])if(h_dist[v]==INF){h_dist[v]=h_dist[u]+1;h_queue[h_end++]=v;}}
            for(int target=root+1;target<OLD;++target){
                int hd=h_dist[target];
                if(hd==INF)++h_unreachable;else h_diameter=max(h_diameter,hd);
                if(hd>D){
                    ++h_bad;
                    if(dist[target]>=0 && dist[target]<=D)++h_repaired;else ++h_residual;
                }
                int predicted=min({hd,
                    a_distance[root]+a_distance[target]+2,
                    b_distance[root]+b_distance[target]+2,
                    a_distance[root]+b_distance[target]+3,
                    b_distance[root]+a_distance[target]+3});
                if(predicted>=INF)predicted=-1;
                if(predicted!=dist[target])++old_formula_mismatches;
            }
        }else{
            for(int target=0;target<OLD;++target){
                int predicted=root==U ? min(a_distance[target]+1,b_distance[target]+2)
                                      : min(b_distance[target]+1,a_distance[target]+2);
                if(predicted>=INF)predicted=-1;
                if(predicted!=dist[target])++new_formula_mismatches;
            }
        }
        RootCheck record;record.root=root;
        for(int target=0;target<g.n;++target){
            int d=dist[target]; full_histogram[d]++;
            if(d>=0)diameter=max(diameter,d);
            if(root>=OLD){
                record.histogram[d]++;
                if(d<0)++record.unreachable;else record.max_finite_distance=max(record.max_finite_distance,d);
                if(d<0 || d>D)++record.missing;
            }
            if(target<=root)continue;
            if(d<0)++unreachable;
            if(d>=0 && d<=D)continue;
            long long* count;vector<Edge>* examples;
            if(target<OLD){count=&bad_oo;examples=&witnesses_oo;}
            else if(root<OLD){count=&bad_no;examples=&witnesses_no;}
            else{count=&bad_uv;examples=&witnesses_uv;}
            ++*count;if(examples->size()<16)examples->emplace_back(root,target);
        }
        if(root>=OLD)new_roots.push_back(record);
    }
    bool connected=unreachable==0;
    bool valid=regular && connected && bad_oo+bad_no+bad_uv==0;
    double wall=chrono::duration<double>(chrono::steady_clock::now()-start).count();
    double cpu=double(clock()-cpu_start)/CLOCKS_PER_SEC;
    ostringstream out;out<<setprecision(9);
    out<<"{\"candidate_id\":"<<id<<",\"n\":"<<g.n<<",\"m\":"<<g.edges.size()
       <<",\"simple\":true,\"degree_histogram\":";map_json(out,degree_histogram);
    out<<",\"regular7\":"<<(regular?"true":"false")<<",\"connected\":"<<(connected?"true":"false")
       <<",\"diameter\":"<<(connected?diameter:-1)<<",\"roots_checked\":"<<g.n
       <<",\"bad_unordered_pairs\":{\"old_old\":"<<bad_oo<<",\"new_old\":"<<bad_no<<",\"new_u_v\":"<<bad_uv
       <<",\"total\":"<<bad_oo+bad_no+bad_uv<<"},\"unreachable_unordered_pairs\":"<<unreachable
       <<",\"removed_edge_count\":"<<removed.size()<<",\"added_edge_count\":"<<added.size()
       <<",\"removed_six_matching\":"<<(matching?"true":"false")
       <<",\"added_uv_and_six_attachments_each\":"<<(additions?"true":"false")
       <<",\"each_removed_edge_split_between_new_vertices\":"<<(orientations?"true":"false")
       <<",\"exact_requested_augmentation\":"<<(exact_augmentation?"true":"false")
       <<",\"removed_edges\":";edges_json(out,removed);out<<",\"added_edges\":";edges_json(out,added);
    out<<",\"deleted_graph_H\":{\"diameter\":"<<(h_unreachable?-1:h_diameter)
       <<",\"unreachable_unordered_pairs\":"<<h_unreachable
       <<",\"old_old_pairs_over5_or_unreachable\":"<<h_bad
       <<",\"repaired_by_augmentation\":"<<h_repaired
       <<",\"remaining_bad_pairs\":"<<h_residual<<"}"
       <<",\"exact_distance_formula_check\":{\"old_old_pairs_checked\":"<<1LL*OLD*(OLD-1)/2
       <<",\"old_old_mismatches\":"<<old_formula_mismatches
       <<",\"new_old_pairs_checked\":"<<2*OLD<<",\"new_old_mismatches\":"<<new_formula_mismatches
       <<",\"H_residual_equals_candidate_old_old_bad\":"<<(h_residual==bad_oo?"true":"false")<<"}";
    out<<",\"ordered_distance_histogram\":";map_json(out,full_histogram);
    out<<",\"new_roots\":[";
    for(size_t i=0;i<new_roots.size();++i){
        auto& r=new_roots[i];if(i)out<<",";
        out<<"{\"root\":"<<r.root<<",\"distance_histogram\":";map_json(out,r.histogram);
        out<<",\"maximum_distance\":"<<(r.unreachable?-1:r.max_finite_distance)
           <<",\"missing_within_5\":"<<r.missing<<",\"unreachable\":"<<r.unreachable<<"}";
    }
    out<<"],\"bad_pair_examples\":{\"old_old\":";edges_json(out,witnesses_oo);
    out<<",\"new_old\":";edges_json(out,witnesses_no);out<<",\"new_u_v\":";edges_json(out,witnesses_uv);
    out<<"},\"valid_degree7_diameter5\":"<<(valid?"true":"false")
       <<",\"wall_seconds\":"<<wall<<",\"cpu_seconds\":"<<cpu<<"}";
    cout<<"candidate_"<<setw(2)<<setfill('0')<<id<<" D="<<(connected?diameter:-1)
        <<" bad="<<bad_oo<<"/"<<bad_no<<"/"<<bad_uv<<" valid="<<valid
        <<" construction="<<exact_augmentation<<" cpu="<<cpu<<" wall="<<wall<<endl;
    return out.str();
}

int main(int argc,char**argv){
    if(argc!=4){cerr<<"usage: SOURCE_EDGES CANDIDATE_DIRECTORY OUTPUT_JSON\n";return 2;}
    try{
        Graph source=read_graph(argv[1]);
        if(source.n!=2810 || source.edges.size()!=9835)throw runtime_error("unexpected baseline size");
        for(auto& row:source.adj)if(row.size()!=7)throw runtime_error("baseline is not 7-regular");
        auto start=chrono::steady_clock::now();clock_t cpu_start=clock();
        ofstream out(argv[3]);if(!out)throw runtime_error("cannot write output");
        out<<"{\"scope\":\"exactly candidate_00.edges through candidate_09.edges\",\"candidates\":[";
        for(int id=0;id<10;++id){
            ostringstream name;name<<argv[2]<<"/candidate_"<<setw(2)<<setfill('0')<<id<<".edges";
            string result=check_one(source,name.str(),id);
            if(id)out<<",";out<<result;out.flush();
        }
        out<<"],\"total_wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()
           <<",\"total_cpu_seconds\":"<<double(clock()-cpu_start)/CLOCKS_PER_SEC<<"}\n";
    }catch(const exception& e){cerr<<e.what()<<"\n";return 2;}
    return 0;
}

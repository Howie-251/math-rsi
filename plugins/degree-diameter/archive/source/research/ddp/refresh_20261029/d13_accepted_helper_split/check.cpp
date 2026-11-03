#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <vector>
using namespace std;

static double cpu() { return double(clock()) / CLOCKS_PER_SEC; }
static void ints(ostream& out, const vector<int>& v) {
    out << '[';
    for (size_t i=0;i<v.size();++i) { if(i)out<<',';out<<v[i]; }
    out << ']';
}
struct Case {
    int h, degree, ecc, far_count, singleton_target=-1, singleton_mask=0;
    vector<int> neighbors;
    map<int,pair<int,int>> supports; // mask -> first target,count
    vector<pair<int,int>> partition_rejections; // normalized A mask, rejected support
    int passing_A=-1;
};
int main(int argc,char**argv) {
    assert(argc==4);
    const string source=argv[1], outdir=argv[2];
    const double budget=stod(argv[3]);
    int n,m;ifstream in(source);in>>n>>m;
    assert(n==51457&&m==324863);
    vector<vector<int>> adj(n);vector<pair<int,int>> edges;edges.reserve(m);
    int u,v;while(in>>u>>v){assert(u>=0&&u<n&&v>=0&&v<n&&u!=v);adj[u].push_back(v);adj[v].push_back(u);edges.push_back({u,v});}
    assert(int(edges.size())==m);
    for(auto& a:adj)sort(a.begin(),a.end());
    vector<Case> cases;
    int bfs_runs=0, graph_exports=0, pass_h=-1, pass_A=-1;
    string status="COMPLETE_ALL40_ADJACENT_HELPER_SPLITS_EXCLUDED";
    for(int h=51417;h<51457;++h){
        if(cpu()>budget){status="BUDGET_STOP_INCOMPLETE";break;}
        Case c;c.h=h;c.neighbors=adj[h];c.degree=adj[h].size();c.ecc=0;c.far_count=0;
        assert(c.degree>=10&&c.degree<=12);
        for(int x:c.neighbors)assert(x<51417);
        vector<int8_t> dist(n,-1);vector<uint16_t> masks(n,0);vector<int> q(n);int head=0,tail=0;
        dist[h]=0;q[tail++]=h;
        for(int i=0;i<c.degree;++i){int x=c.neighbors[i];dist[x]=1;masks[x]=uint16_t(1u<<i);q[tail++]=x;}
        while(head<tail){int x=q[head++];if(x==h||dist[x]>=5)continue;
            for(int y:adj[x]){
                if(dist[y]<0){dist[y]=dist[x]+1;masks[y]=masks[x];q[tail++]=y;}
                else if(dist[y]==dist[x]+1)masks[y]|=masks[x];
            }
        }
        ++bfs_runs;
        assert(tail==n);
        for(int t=0;t<n;++t){
            c.ecc=max(c.ecc,int(dist[t]));
            if(dist[t]!=5)continue;
            ++c.far_count;int mask=masks[t];assert(mask>0);
            auto it=c.supports.find(mask);
            if(it==c.supports.end())c.supports[mask]={t,1};else ++it->second.second;
            if((mask&(mask-1))==0&&c.singleton_target<0){c.singleton_target=t;c.singleton_mask=mask;}
        }
        if(c.singleton_target<0){
            const int full=(1<<c.degree)-1;
            for(int assignment=0;assignment<(1<<(c.degree-1));++assignment){
                const int A=assignment<<1,B=full^A;int rejected=0;
                for(const auto& kv:c.supports){int s=kv.first;if((s&A)==0||(s&B)==0){rejected=s;break;}}
                if(rejected==0){c.passing_A=A;pass_h=h;pass_A=A;break;}
                c.partition_rejections.push_back({A,rejected});
            }
        }
        cases.push_back(c);
        if(pass_h>=0){
            status="PASS_SPLIT_GRAPH_EXPORTED_PENDING_INDEPENDENT_ACCEPTANCE";
            const int b=n;
            ofstream graph(outdir+"/candidate_n51458.edges");graph<<n+1<<' '<<m+1<<'\n';
            for(auto e:edges){int x=e.first,y=e.second;
                if(x==h){int i=lower_bound(c.neighbors.begin(),c.neighbors.end(),y)-c.neighbors.begin();if(!(pass_A&(1<<i)))x=b;}
                if(y==h){int i=lower_bound(c.neighbors.begin(),c.neighbors.end(),x)-c.neighbors.begin();if(!(pass_A&(1<<i)))y=b;}
                if(x>y)swap(x,y);graph<<x<<' '<<y<<'\n';
            }
            graph<<h<<' '<<b<<'\n';++graph_exports;
            break;
        }
        cout<<"h="<<h<<" far="<<c.far_count<<" supports="<<c.supports.size()<<" singleton_target="<<c.singleton_target<<" checked_partitions="<<c.partition_rejections.size()<<'\n';
    }
    ofstream detail(outdir+"/CASES.json");detail<<"[\n";
    for(size_t k=0;k<cases.size();++k){const auto& c=cases[k];if(k)detail<<",\n";
        detail<<"{\"h\":"<<c.h<<",\"degree\":"<<c.degree<<",\"neighbors\":";ints(detail,c.neighbors);
        detail<<",\"eccentricity\":"<<c.ecc<<",\"distance5_targets\":"<<c.far_count<<",\"unique_support_count\":"<<c.supports.size();
        detail<<",\"singleton_target\":"<<c.singleton_target<<",\"singleton_mask\":"<<c.singleton_mask;
        detail<<",\"normalized_partitions_total\":"<<(1<<(c.degree-1))<<",\"passing_A_mask\":"<<c.passing_A;
        detail<<",\"support_witnesses\":[";bool first=true;
        for(const auto&kv:c.supports){if(!first)detail<<',';first=false;detail<<"{\"mask\":"<<kv.first<<",\"target\":"<<kv.second.first<<",\"target_count\":"<<kv.second.second<<'}';}
        detail<<"],\"complete_partition_rejections\":[";first=true;
        for(auto x:c.partition_rejections){if(!first)detail<<',';first=false;detail<<"{\"A_mask\":"<<x.first<<",\"monochromatic_support\":"<<x.second<<",\"witness_target\":"<<c.supports.at(x.second).first<<'}';}
        detail<<"]}";
    }
    detail<<"\n]\n";
    ofstream out(outdir+"/NATIVE_RESULT.json");
    out<<"{\"status\":\""<<status<<"\",\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"source_reads\":1,\"objects_tested\":"<<cases.size()<<",\"BFS_roots\":"<<bfs_runs<<",\"source_all_roots_rechecked\":false,\"graph_exports\":"<<graph_exports<<",\"passing_h\":"<<pass_h<<",\"passing_A_mask\":"<<pass_A<<",\"native_CPU_seconds\":"<<cpu()<<",\"running\":false}\n";
}

#include <algorithm>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int main(int argc,char**argv){
    if(argc!=4)return 2;
    const double start=double(clock())/CLOCKS_PER_SEC;
    ifstream core(argv[1]),queries(argv[2]);
    int n,m;core>>n>>m;
    vector<vector<int>>adj(n);
    for(int k=0,u,v;k<m;k++){core>>u>>v;adj[u].push_back(v);adj[v].push_back(u);}
    int count;queries>>count;
    vector<int>ids(count);
    vector<vector<int>> mandatory(count),anchors(count);
    for(int i=0;i<count;i++){
        int a,b;queries>>ids[i]>>a>>b;
        mandatory[i].resize(a);anchors[i].resize(b);
        for(int&v:mandatory[i])queries>>v;
        for(int&v:anchors[i])queries>>v;
    }
    ofstream failures(argv[3]);
    failures<<"condition\tleft_extra\tright_extra\n";
    long long failed[2]={0,0};
    vector<int>seen(n,0),dist(n),queue(n);
    int stamp=0;
    for(int kind=0;kind<2;kind++){
        const auto&sets=kind?anchors:mandatory;
        for(int i=0;i<count;i++){
            stamp++;int head=0,tail=0;
            for(int v:sets[i]){seen[v]=stamp;dist[v]=0;queue[tail++]=v;}
            while(head<tail){
                int u=queue[head++];if(dist[u]==3)continue;
                for(int v:adj[u])if(seen[v]!=stamp){
                    seen[v]=stamp;dist[v]=dist[u]+1;queue[tail++]=v;
                }
            }
            for(int j=i+1;j<count;j++){
                bool hit=false;
                for(int v:sets[j])if(seen[v]==stamp){hit=true;break;}
                if(!hit){failed[kind]++;failures<<(kind?"actual_core_attachments":"mandatory_Q_line_images")<<'\t'<<ids[i]<<'\t'<<ids[j]<<'\n';}
            }
        }
    }
    cout<<"{\"source_core_order\":"<<n<<",\"subjects\":"<<count
        <<",\"set_pairs_per_condition\":"<<1LL*count*(count-1)/2
        <<",\"mandatory_failed_set_pairs\":"<<failed[0]
        <<",\"actual_attachment_failed_set_pairs\":"<<failed[1]
        <<",\"new_multisource_R3_tests\":"<<2*count
        <<",\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
}

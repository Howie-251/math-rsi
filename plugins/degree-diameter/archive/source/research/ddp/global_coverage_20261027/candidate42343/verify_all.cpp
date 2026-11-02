// Independent all-source BFS from the expanded edge list, no search caches.
#include <algorithm>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <omp.h>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;
int main(int argc,char**argv){try{
    if(argc!=5)throw runtime_error("usage: verify_all EDGES DEGREE DIAMETER THREADS");
    int cap=stoi(argv[2]),target=stoi(argv[3]),workers=stoi(argv[4]);
    ifstream f(argv[1]);int n;long long m;
    if(!(f>>n>>m)||n<1||m<0)throw runtime_error("invalid header");
    auto start=chrono::steady_clock::now();double cpu=double(clock())/CLOCKS_PER_SEC;
    vector<pair<int,int>> edges;edges.reserve(m);vector<int>degree(n);
    for(long long k=0;k<m;k++){
        int u,v;if(!(f>>u>>v)||u<0||v<0||u>=n||v>=n||u==v)throw runtime_error("invalid edge");
        if(u>v)swap(u,v);edges.emplace_back(u,v);degree[u]++;degree[v]++;
    }
    string tail;if(f>>tail)throw runtime_error("unexpected trailing input");
    sort(edges.begin(),edges.end());
    if(adjacent_find(edges.begin(),edges.end())!=edges.end())throw runtime_error("duplicate edge");
    vector<int>offset(n+1);for(int v=0;v<n;v++)offset[v+1]=offset[v]+degree[v];
    vector<int>neighbor(2*m),next=offset;
    for(auto[u,v]:edges){neighbor[next[u]++]=v;neighbor[next[v]++]=u;}
    int diameter=0,checked=0;long long bad=0,unreachable=0;
    vector<long long>hist(n),ecc_hist(n);
    omp_set_num_threads(workers);
    #pragma omp parallel
    {
        vector<int>distance(n),queue(n);vector<long long>local_hist(n),local_ecc(n);
        int local_diameter=0,local_checked=0;long long local_bad=0,local_unreachable=0;
        #pragma omp for schedule(dynamic,16)
        for(int source=0;source<n;source++){
            fill(distance.begin(),distance.end(),-1);
            int head=0,end=0;queue[end++]=source;distance[source]=0;
            while(head<end){
                int u=queue[head++];
                for(int k=offset[u];k<offset[u+1];k++){
                    int v=neighbor[k];if(distance[v]<0){distance[v]=distance[u]+1;queue[end++]=v;}
                }
            }
            int ecc=0;
            for(int v=0;v<n;v++){
                int d=distance[v];
                if(d<0){if(v>source)local_unreachable++;}
                else{local_hist[d]++;ecc=max(ecc,d);}
                if(v>source&&(d<0||d>target))local_bad++;
            }
            local_ecc[ecc]++;local_diameter=max(local_diameter,ecc);local_checked++;
        }
        #pragma omp critical
        {
            diameter=max(diameter,local_diameter);checked+=local_checked;
            bad+=local_bad;unreachable+=local_unreachable;
            for(int d=0;d<n;d++){hist[d]+=local_hist[d];ecc_hist[d]+=local_ecc[d];}
        }
    }
    int low=*min_element(degree.begin(),degree.end()),high=*max_element(degree.begin(),degree.end());
    bool valid=checked==n&&bad==0&&unreachable==0&&high<=cap;
    double seconds=chrono::duration<double>(chrono::steady_clock::now()-start).count();
    cout<<"{\"n\":"<<n<<",\"m\":"<<m<<",\"min_degree\":"<<low<<",\"max_degree\":"<<high
        <<",\"diameter\":"<<(unreachable?-1:diameter)<<",\"roots_checked\":"<<checked
        <<",\"bad_unordered_pairs\":"<<bad<<",\"unreachable_unordered_pairs\":"<<unreachable
        <<",\"simple\":true,\"valid\":"<<(valid?"true":"false")<<",\"workers\":"<<workers
        <<",\"wall_seconds\":"<<seconds<<",\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-cpu
        <<",\"ordered_distance_histogram\":{";
    bool first=true;for(int d=0;d<n;d++)if(hist[d]){if(!first)cout<<',';first=false;cout<<'"'<<d<<"\":"<<hist[d];}
    cout<<"},\"eccentricity_histogram\":{";
    first=true;for(int d=0;d<n;d++)if(ecc_hist[d]){if(!first)cout<<',';first=false;cout<<'"'<<d<<"\":"<<ecc_hist[d];}
    cout<<"}}\n";
    return valid?0:1;
}catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}

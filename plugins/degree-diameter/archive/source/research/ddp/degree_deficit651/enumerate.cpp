#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>

constexpr int N=651, W=650;
using Adj=std::array<std::array<int,5>,N>;
static int marks[N]={}, stamp=0, queue_nodes[N];
long long bad_pairs(const Adj& adj,const std::array<int,N>& degree){
    long long ordered=0;
    for(int root=0;root<N;root++){
        ++stamp; marks[root]=stamp; queue_nodes[0]=root;
        int start=0,end=1;
        for(int depth=0;depth<5 && end<N;depth++){
            int next=end;
            for(int q=start;q<end;q++){
                int u=queue_nodes[q];
                for(int j=0;j<degree[u];j++){
                    int v=adj[u][j];
                    if(marks[v]!=stamp){marks[v]=stamp;queue_nodes[next++]=v;}
                }
            }
            start=end;end=next;
        }
        ordered+=N-end;
    }
    assert(ordered%2==0);
    return ordered/2;
}
void save_edges(const std::string& path,const Adj& adj,const std::array<int,N>& degree){
    std::vector<std::pair<int,int>> edges;
    for(int u=0;u<N;u++)for(int j=0;j<degree[u];j++)if(u<adj[u][j])edges.emplace_back(u,adj[u][j]);
    std::sort(edges.begin(),edges.end());
    assert(edges.size()==1627);
    std::ofstream out(path);out<<N<<" "<<edges.size()<<"\n";
    for(auto [u,v]:edges)out<<u<<" "<<v<<"\n";
}
int main(int argc,char**argv){
    assert(argc==4);
    const std::string source=argv[1],prefix=argv[2];
    const double budget=std::stod(argv[3]);
    auto wall_start=std::chrono::steady_clock::now();
    auto cpu_start=std::clock();
    auto cpu=[&](){return double(std::clock()-cpu_start)/CLOCKS_PER_SEC;};
    std::ifstream in(source);int n,m;in>>n>>m;assert(n==N&&m==1627);
    Adj adj{};std::array<int,N> degree{};
    for(int i=0,u,v;i<m;i++){
        in>>u>>v;assert(0<=u&&u<v&&v<N);
        assert(degree[u]<5&&degree[v]<5);
        adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;
    }
    for(int u=0;u<N;u++){
        assert(degree[u]==(u==W?4:5));
        std::sort(adj[u].begin(),adj[u].begin()+degree[u]);
        for(int j=1;j<degree[u];j++)assert(adj[u][j-1]!=adj[u][j]);
    }
    std::vector<std::pair<int,int>> moves;
    for(int x=0;x<W;x++){
        bool neighbor=false;
        for(int i=0;i<degree[W];i++)neighbor|=adj[W][i]==x;
        if(!neighbor)for(int i=0;i<degree[x];i++)moves.emplace_back(x,adj[x][i]);
    }
    assert(moves.size()==3230);
    std::ofstream rows(prefix+".moves.tsv");rows<<"index\tx\ty\tbad_pairs\n";
    std::vector<long long> scores;
    std::map<long long,int> histogram;
    long long best=1LL<<60;int best_index=-1,best_x=-1,best_y=-1,improved=0,equal=0,worse=0;
    for(int k=0;k<int(moves.size());k++){
        if(cpu()>budget-0.15)break;
        auto [x,y]=moves[k];
        int ix=0,iy=0;
        while(adj[x][ix]!=y)ix++;
        while(adj[y][iy]!=x)iy++;
        adj[x][ix]=W;
        adj[y][iy]=adj[y][4];degree[y]=4;
        adj[W][4]=x;degree[W]=5;
        long long bad=bad_pairs(adj,degree);
        rows<<k<<"\t"<<x<<"\t"<<y<<"\t"<<bad<<"\n";
        scores.push_back(bad);histogram[bad]++;
        if(bad<59)improved++;else if(bad==59)equal++;else worse++;
        if(bad<best){
            best=bad;best_index=k;best_x=x;best_y=y;
            save_edges(prefix+".best.edges",adj,degree);
            std::cout<<"BEST index="<<k<<" add="<<W<<","<<x<<" remove="<<x<<","<<y<<" bad_pairs="<<bad<<" cpu="<<cpu()<<std::endl;
        }
        adj[x][ix]=y;
        adj[y][4]=adj[y][iy];adj[y][iy]=x;degree[y]=5;
        degree[W]=4;
        if(k==15){
            double elapsed=cpu();
            std::cout<<"PILOT completed=16 cpu="<<elapsed<<" projected_total_cpu="<<elapsed*moves.size()/16<<std::endl;
        }
    }
    rows.close();
    auto sorted=scores;std::sort(sorted.begin(),sorted.end());
    double median=sorted.empty()?-1:(sorted[(sorted.size()-1)/2]+sorted[sorted.size()/2])/2.0;
    const bool complete=scores.size()==moves.size();
    std::ofstream out(prefix+".summary.json");
    out<<"{\n  \"status\": \""<<(complete?"COMPLETE":"CPU_BUDGET_EXHAUSTED_PARTIAL")<<"\",\n"
       <<"  \"source\": \""<<source<<"\",\n  \"vertices\": 651,\n  \"edges\": 1627,\n"
       <<"  \"source_bad_pairs\": 59,\n  \"initial_deficit_vertex\": 650,\n"
       <<"  \"legal_neighbor_count\": "<<moves.size()<<",\n  \"evaluated\": "<<scores.size()<<",\n"
       <<"  \"next_index\": "<<scores.size()<<",\n  \"minimum\": "<<sorted.front()<<",\n"
       <<"  \"median\": "<<median<<",\n  \"maximum\": "<<sorted.back()<<",\n"
       <<"  \"improving\": "<<improved<<",\n  \"equal\": "<<equal<<",\n  \"worsening\": "<<worse<<",\n"
       <<"  \"best_move_index\": "<<best_index<<",\n  \"best_added_edge\": [650,"<<best_x<<"],\n"
       <<"  \"best_deleted_edge\": ["<<best_x<<","<<best_y<<"],\n  \"best_new_deficit_vertex\": "<<best_y<<",\n"
       <<"  \"cpu_budget_seconds\": "<<budget<<",\n  \"cpu_seconds\": "<<cpu()<<",\n"
       <<"  \"wall_seconds\": "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-wall_start).count()<<",\n"
       <<"  \"score_histogram\": {";
    bool first=true;for(auto [score,count]:histogram){if(!first)out<<",";first=false;out<<"\""<<score<<"\":"<<count;}out<<"}\n}\n";
    std::cout<<"TERMINAL "<<(complete?"COMPLETE":"CPU_BUDGET_EXHAUSTED_PARTIAL")<<" evaluated="<<scores.size()<<" best="<<best<<" median="<<median<<" max="<<sorted.back()<<" improving="<<improved<<" equal="<<equal<<" worsening="<<worse<<" cpu="<<cpu()<<std::endl;
}

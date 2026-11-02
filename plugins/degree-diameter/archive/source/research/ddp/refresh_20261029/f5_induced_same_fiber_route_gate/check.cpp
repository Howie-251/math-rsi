#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include "literal_parameters.h"
using namespace std;
constexpr int N=3750,D=20;

template<class T> void array_json(ostream& o,const vector<T>& xs){
    o<<"[";for(size_t i=0;i<xs.size();i++){if(i)o<<",";o<<xs[i];}o<<"]";
}
void hist_json(ostream& o,const map<int,int>& h){
    o<<"{";bool first=true;for(auto [key,value]:h){if(!first)o<<",";first=false;o<<"\""<<key<<"\":"<<value;}o<<"}";
}
array<int,3> coord(int v){return {v%5,(v/5)%5,(v/25)%5};}
int direction(int x,int y){
    auto a=coord(x),b=coord(y);
    for(int p=0;p<4;p++)for(int t=1;t<5;t++){
        bool yes=true;
        for(int k=0;k<3;k++)if((b[k]-a[k]+5)%5!=(t*DIRECTIONS[p][k])%5)yes=false;
        if(yes)return p;
    }
    return -1;
}

int main(int argc,char**argv){
    assert(argc==3);
    double start=double(clock())/CLOCKS_PER_SEC;
    vector<array<uint16_t,D>> adj(N);
    ifstream input(argv[1],ios::binary);
    input.read(reinterpret_cast<char*>(adj.data()),N*D*sizeof(uint16_t));
    assert(input.gcount()==N*D*sizeof(uint16_t));
    vector<bitset<N>> membership(N);
    for(int v=0;v<N;v++)for(int u:adj[v])membership[v].set(u);
    map<int,int> two_hist,three_hist,and_hist,nonline_and_hist,overlap_hist,line_direction_hist;
    int pairs=0,line_pairs=0,nonline_pairs=0,prediction_failures=0,nontriangle_routes=0;
    long long total_two=0,total_three=0;
    string out=argv[2];
    ofstream examples(out+"/EXAMPLES.json");
    examples<<"[";int examples_written=0;
    ofstream first_failure(out+"/FIRST_FAILURE.json");
    bool failure_written=false;
    for(int x=0;x<125;x++)for(int y=x+1;y<125;y++){
        vector<int> mids;
        vector<array<int,2>> routes;
        set<array<int,2>> ands;
        for(int a:adj[x]){
            if(membership[a][y])mids.push_back(a);
            for(int b:adj[y])if(membership[a][b]){
                routes.push_back({a,b});
                ands.insert({min(a,b),max(a,b)});
                int ca=a/125,cb=b/125;
                bool triangle=ca!=0 && cb!=0 && ca!=cb;
                bool ca0=false,cb0=false,cacb=false;
                for(int u:CONTROLLER[0]){ca0|=u==ca;cb0|=u==cb;}
                for(int u:CONTROLLER[ca])cacb|=u==cb;
                if(!(triangle&&ca0&&cb0&&cacb))nontriangle_routes++;
            }
        }
        int p=direction(x,y),overlap=-1;
        if(routes.size()==2){
            set<int> left{routes[0][0],routes[0][1]};
            overlap=int(left.count(routes[1][0])+left.count(routes[1][1]));
            overlap_hist[overlap]++;
        }
        pairs++;two_hist[mids.size()]++;three_hist[routes.size()]++;and_hist[ands.size()]++;
        total_two+=mids.size();total_three+=routes.size();
        if(p>=0){line_pairs++;line_direction_hist[p]++;}
        else {nonline_pairs++;nonline_and_hist[ands.size()]++;}
        bool pass=routes.size()==2 && mids.size()==size_t(p>=0?5:0);
        if(p<0)pass=pass&&ands.size()==2&&overlap==0;
        if(!pass){
            prediction_failures++;
            if(!failure_written){
                first_failure<<"{\"endpoints\":["<<x<<","<<y<<"],\"direction\":"<<p
                    <<",\"two_midpoints\":"<<mids.size()<<",\"three_walks\":"<<routes.size()
                    <<",\"distinct_internal_AND_terms\":"<<ands.size()<<",\"overlap\":"<<overlap<<"}\n";
                failure_written=true;
            }
        }
        if(x==0&&(y==1||y==6||y==31)){
            if(examples_written++)examples<<",";
            examples<<"{\"endpoints_old_ids\":["<<x<<","<<y<<"],\"direction_index\":"<<p<<",\"two_step_midpoints\":";
            array_json(examples,mids);
            examples<<",\"directed_three_step_walks\":[";
            for(size_t j=0;j<routes.size();j++){if(j)examples<<",";examples<<"["<<x<<","<<routes[j][0]<<","<<routes[j][1]<<","<<y<<"]";}
            examples<<"],\"distinct_unordered_internal_AND_terms\":[";
            bool first=true;for(auto t:ands){if(!first)examples<<",";first=false;examples<<"["<<t[0]<<","<<t[1]<<"]";}
            examples<<"],\"internal_route_overlap\":"<<overlap<<"}";
        }
    }
    if(!failure_written)first_failure<<"null\n";
    examples<<"]\n";
    ofstream result(out+"/NATIVE_RESULT.json");
    result<<"{\"pairs_checked\":"<<pairs<<",\"line_difference_pairs\":"<<line_pairs
        <<",\"other_difference_pairs\":"<<nonline_pairs<<",\"two_step_midpoint_count_histogram\":";
    hist_json(result,two_hist);
    result<<",\"directed_three_step_walk_count_histogram_fixed_x_less_y\":";
    hist_json(result,three_hist);
    result<<",\"distinct_unordered_internal_AND_terms_histogram\":";
    hist_json(result,and_hist);
    result<<",\"no_two_step_pairs_AND_term_count_histogram\":";
    hist_json(result,nonline_and_hist);
    result<<",\"two_three_walks_internal_vertex_overlap_histogram\":";
    hist_json(result,overlap_hist);
    result<<",\"line_pairs_by_direction\":";hist_json(result,line_direction_hist);
    result<<",\"total_two_step_paths\":"<<total_two<<",\"total_directed_three_step_walks_fixed_x_less_y\":"<<total_three
        <<",\"nontriangle_three_step_walks\":"<<nontriangle_routes
        <<",\"prediction_failures\":"<<prediction_failures
        <<",\"source_cache_reads\":1,\"BFS_runs\":0,\"solver_calls\":0,\"graphs_generated\":0"
        <<",\"CPU_seconds\":"<<(double(clock())/CLOCKS_PER_SEC-start)<<"}\n";
}

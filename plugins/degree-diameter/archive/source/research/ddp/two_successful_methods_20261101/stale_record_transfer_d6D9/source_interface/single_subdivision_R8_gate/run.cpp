#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(int argc,char**argv){
    constexpr int M=49,P=6763,N=M*P;
    const int phase[6]={25,24,18,31,47,2};
    const int normal[6]={1254,2125,541,3289,4642,1300};
    int power[M];power[0]=1;for(int i=1;i<M;++i)power[i]=int(41LL*power[i-1]%P);
    const double limit=std::stod(argv[2]);
    std::ofstream out(std::string(argv[1])+"/RAW_RESULT.json");
    out<<"{\"source_order\":"<<N<<",\"queries\":[";
    bool allfail=true;int done=0;
    for(int k=0;k<3;++k){
        if(double(std::clock())/CLOCKS_PER_SEC>=limit){allfail=false;break;}
        const double started=double(std::clock())/CLOCKS_PER_SEC;
        const int gen=2*k,target=phase[gen]*P+normal[gen];
        std::vector<signed char>d(N,-1);std::vector<int>q(N);int head=0,tail=2;
        q[0]=0;q[1]=target;d[0]=d[target]=0;
        std::array<int,9>hist{};hist[0]=2;long long examined=0;int expanded=0;
        while(head<tail){
            int u=q[head++],depth=d[u];if(depth==8)continue;++expanded;
            int j=u/P,n=u%P;
            for(int g=0;g<6;++g){
                int jj=j+phase[g];if(jj>=M)jj-=M;
                int nn=int((1LL*n*power[phase[g]]+normal[g])%P),v=jj*P+nn;++examined;
                if((u==0&&v==target)||(u==target&&v==0))continue;
                if(d[v]>=0)continue;d[v]=depth+1;q[tail++]=v;++hist[depth+1];
            }
        }
        int missing=N-tail,first=-1;for(int v=0;v<N;++v)if(d[v]<0){first=v;break;}
        if(!missing)allfail=false;
        if(done)out<<',';
        out<<"{\"type\":"<<k<<",\"positive_generator\":["<<phase[gen]<<','<<normal[gen]<<"],\"inverse_generator\":["<<phase[gen+1]<<','<<normal[gen+1]<<"],\"deleted_edge\":[0,"<<target<<"],\"covered_old_count\":"<<tail<<",\"missing_old_count\":"<<missing<<",\"first_missing_label\":"<<first<<",\"first_missing_coordinates\":";
        if(first>=0)out<<'['<<first/P<<','<<first%P<<']';else out<<"null";
        out<<",\"minimum_new_point_distance_to_missing\":"<<(missing?10:0)<<",\"multi_source_depth8_histogram\":[";
        for(int i=0;i<9;++i){if(i)out<<',';out<<hist[i];}
        out<<"],\"expanded_vertices\":"<<expanded<<",\"neighbor_darts_examined\":"<<examined<<",\"query_CPU_seconds\":"<<double(std::clock())/CLOCKS_PER_SEC-started<<'}';
        ++done;
    }
    out<<"],\"query_count\":"<<done<<",\"all_three_types_fail\":"<<(allfail&&done==3?"true":"false")<<",\"run_process_CPU_seconds\":"<<double(std::clock())/CLOCKS_PER_SEC<<"}\n";
    std::cout<<"queries="<<done<<" allfail="<<(allfail&&done==3)<<" CPU="<<double(std::clock())/CLOCKS_PER_SEC<<'\n';
}

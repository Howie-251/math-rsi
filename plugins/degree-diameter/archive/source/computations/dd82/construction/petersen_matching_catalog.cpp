// Exact S10 catalog for the necessary Petersen pair-matching condition.
// Standalone; does not read or modify the six-fiber search state.
#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sched.h>
#include <sys/resource.h>
using Perm=std::array<int,10>;
void perm_json(std::ostream& o,const Perm& p){o<<'[';for(int i=0;i<10;i++){if(i)o<<',';o<<p[i];}o<<']';}
int main(int argc,char**argv){
    if(argc!=2){std::cerr<<"usage: catalog output.json\n";return 2;}
    cpu_set_t cpus;CPU_ZERO(&cpus);sched_getaffinity(0,sizeof(cpus),&cpus);
    int pinned=-1;for(int i=0;i<CPU_SETSIZE;i++)if(CPU_ISSET(i,&cpus)){pinned=i;break;}
    if(pinned>=0){CPU_ZERO(&cpus);CPU_SET(pinned,&cpus);sched_setaffinity(0,sizeof(cpus),&cpus);}
    rlimit cpu_limit{3,3};setrlimit(RLIMIT_CPU,&cpu_limit);
    rlimit mem_limit{1024ULL*1024*1024,1024ULL*1024*1024};setrlimit(RLIMIT_AS,&mem_limit);
    std::array<unsigned,10> neighbors{};
    auto add=[&](int a,int b){neighbors[a]|=1U<<b;neighbors[b]|=1U<<a;};
    for(int i=0;i<5;i++){add(i,(i+1)%5);add(5+i,5+(i+2)%5);add(i,i+5);}
    std::array<std::array<int,2>,15> edges;int edge_count=0;
    for(int u=0;u<10;u++)for(int v=u+1;v<10;v++)if(neighbors[u]&(1U<<v))edges[edge_count++]={u,v};
    if(edge_count!=15)return 3;
    std::array<uint64_t,6> counts{};std::array<Perm,6> examples{};
    Perm p;std::iota(p.begin(),p.end(),0);
    uint64_t processed=0,accepted=0;bool complete=false;
    const clock_t start=clock();
    do{
        unsigned used=0;int q=0;bool valid=true;
        for(const auto&e:edges){
            const int u=p[e[0]],v=p[e[1]];
            if(neighbors[u]&(1U<<v)){
                const unsigned endpoints=(1U<<u)|(1U<<v);
                if(used&endpoints){valid=false;break;}
                used|=endpoints;q++;
            }
        }
        processed++;
        if(valid){if(counts[q]==0)examples[q]=p;counts[q]++;accepted++;}
        if((processed&16383)==0 && double(clock()-start)/CLOCKS_PER_SEC>=2.90)break;
        if(!std::next_permutation(p.begin(),p.end())){complete=true;break;}
    }while(true);
    const double seconds=double(clock()-start)/CLOCKS_PER_SEC;
    std::ofstream out(argv[1]);
    out<<"{\n  \"petersen_labeling\": \"outer cycle 0..4, inner star 5..9, spokes i--(i+5)\",\n  \"condition\": \"maximum degree of P intersect M(P) is at most one\",\n  \"permutation_convention\": \"M[u] is the target label of source u\",\n  \"complete_enumeration\": "<<(complete?"true":"false")<<",\n  \"permutations_processed\": "<<processed<<",\n  \"total_S10\": 3628800,\n  \"admissible_permutations\": "<<accepted<<",\n  \"rejected_permutations\": "<<processed-accepted<<",\n  \"cpu_seconds\": "<<seconds<<",\n  \"cpu_limit_seconds\": 3,\n  \"threads\": 1,\n  \"pinned_cpu\": "<<pinned<<",\n  \"counts_by_intersection_edge_number\": {";
    for(int q=0;q<=5;q++){if(q)out<<',';out<<'\"'<<q<<"\":"<<counts[q];}
    out<<"},\n  \"first_permutation_by_intersection_edge_number\": {";
    bool first=true;for(int q=0;q<=5;q++)if(counts[q]){if(!first)out<<',';first=false;out<<'\"'<<q<<"\":";perm_json(out,examples[q]);}
    out<<"},\n  \"edge_disjoint_exists\": "<<(counts[0]?"true":"false")<<",\n  \"scope\": \"Necessary condition on one matching only; no claim of a complete degree-8 diameter-2 graph\"\n}\n";
    std::cout<<"processed "<<processed<<" admissible "<<accepted<<" complete "<<complete<<" CPU "<<seconds<<'\n';
}

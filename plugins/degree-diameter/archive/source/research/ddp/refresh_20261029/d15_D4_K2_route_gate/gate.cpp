#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <unistd.h>
constexpr int N=15552,M=116316,K=648,W=243,TW=11;

template<class T>void write_vector(const std::string&p,const std::vector<T>&a){
    std::ofstream f(p,std::ios::binary);f.write(reinterpret_cast<const char*>(a.data()),a.size()*sizeof(T));assert(f.good());
}
void json_hist(std::ostream&f,const std::map<int,int>&h){bool first=true;f<<'{';for(auto [v,n]:h){if(!first)f<<',';first=false;f<<'"'<<v<<"\":"<<n;}f<<'}';}

int main(int argc,char**argv){
    assert(argc==4);double start=double(clock())/CLOCKS_PER_SEC;
    const uint16_t endian=1;assert(*reinterpret_cast<const uint8_t*>(&endian)==1);
    std::string source=argv[1],cache=argv[2],out=argv[3];
    // Exactly one opening/reading of the literal old source; no diameter check.
    std::ifstream graph(source);int n,m;graph>>n>>m;assert(n==N&&m==M);
    std::vector<std::vector<int>> adj(N);
    for(int i=0;i<M;++i){int u,v;graph>>u>>v;assert(graph&&0<=u&&u<N&&0<=v&&v<N&&u!=v);adj[u].push_back(v);adj[v].push_back(u);}
    int extra;assert(!(graph>>extra));graph.close();
    std::vector<uint32_t> free;
    for(int v=0;v<N;++v){std::sort(adj[v].begin(),adj[v].end());assert(std::adjacent_find(adj[v].begin(),adj[v].end())==adj[v].end());assert(adj[v].size()==14||adj[v].size()==15);if(adj[v].size()==14)free.push_back(v);}
    assert(free.size()==K);

    std::ifstream old(cache,std::ios::binary|std::ios::ate);
    assert(old&&uint64_t(old.tellg())==12+uint64_t(K)*(4+8*W));old.seekg(0);
    uint32_t header[3];old.read(reinterpret_cast<char*>(header),12);assert(header[0]==K&&header[1]==N&&header[2]==W);
    std::vector<uint64_t> rows3(size_t(K)*W),rows2(size_t(K)*W,0);
    std::vector<uint32_t> labels(K);
    std::vector<bool> used(N,false);
    for(int j=0;j<K;++j){
        old.read(reinterpret_cast<char*>(&labels[j]),4);old.read(reinterpret_cast<char*>(&rows3[size_t(j)*W]),8*W);
        assert(old.good()&&labels[j]<N&&!used[labels[j]]&&adj[labels[j]].size()==14);used[labels[j]]=true;
        assert((rows3[size_t(j)*W+labels[j]/64]>>(labels[j]%64))&1);
    }
    auto sorted_labels=labels;std::sort(sorted_labels.begin(),sorted_labels.end());assert(sorted_labels==free);
    old.close();

    std::vector<uint64_t> trans2(size_t(N)*TW,0),trans3(size_t(N)*TW,0);
    std::vector<uint16_t> counts2(N,0),counts3(N,0);
    std::map<int,int> balls2,balls3;
    for(int j=0;j<K;++j){
        uint64_t* r2=&rows2[size_t(j)*W];const uint64_t* r3=&rows3[size_t(j)*W];int v=labels[j];
        auto mark=[&](int t){r2[t/64]|=uint64_t(1)<<(t%64);};
        mark(v);for(int u:adj[v]){mark(u);for(int t:adj[u])mark(t);}
        int size2=0,size3=0;
        for(int w=0;w<W;++w){
            assert((r2[w]&~r3[w])==0);size2+=__builtin_popcountll(r2[w]);size3+=__builtin_popcountll(r3[w]);
            for(int radius=2;radius<=3;++radius){
                uint64_t bits=(radius==2?r2[w]:r3[w]);
                while(bits){int b=__builtin_ctzll(bits),t=64*w+b;assert(t<N);
                    auto&tr=(radius==2?trans2:trans3);auto&counts=(radius==2?counts2:counts3);
                    tr[size_t(t)*TW+j/64]|=uint64_t(1)<<(j%64);++counts[t];bits&=bits-1;
                }
            }
        }
        ++balls2[size2];++balls3[size3];
    }
    {
        std::ofstream f(out+"/R2_MASKS.bin",std::ios::binary);f.write(reinterpret_cast<char*>(header),12);
        for(int j=0;j<K;++j){f.write(reinterpret_cast<const char*>(&labels[j]),4);f.write(reinterpret_cast<const char*>(&rows2[size_t(j)*W]),8*W);}assert(f.good());
    }
    write_vector(out+"/target_R2_support.u64le.bin",trans2);write_vector(out+"/target_R3_support.u64le.bin",trans3);
    write_vector(out+"/target_R2_provider_counts.u16le.bin",counts2);write_vector(out+"/target_R3_provider_counts.u16le.bin",counts3);
    write_vector(out+"/FREE_ORDER.u32le.bin",labels);
    {std::ofstream f(out+"/FREE_ORDER.txt");for(auto v:labels)f<<v<<'\n';}

    std::vector<uint32_t> t0,zeros,singletons;
    std::map<int,int> hist2,hist3t0;
    int min3=K+1,max3=-1,min3target=-1,pairs=0;
    std::ofstream pairfile(out+"/T0_SUPPORT2_OPPOSITION.tsv");pairfile<<"target\tcolumn0\tcolumn1\told_label0\told_label1\n";
    for(int t=0;t<N;++t){
        ++hist2[counts2[t]];
        if(counts2[t])continue;
        t0.push_back(t);++hist3t0[counts3[t]];
        if(counts3[t]<min3){min3=counts3[t];min3target=t;}max3=std::max(max3,int(counts3[t]));
        if(counts3[t]==0)zeros.push_back(t);
        if(counts3[t]==1)singletons.push_back(t);
        if(counts3[t]==2){
            std::vector<int> c;for(int w=0;w<TW;++w){uint64_t bits=trans3[size_t(t)*TW+w];while(bits){c.push_back(64*w+__builtin_ctzll(bits));bits&=bits-1;}}
            assert(c.size()==2);pairfile<<t<<'\t'<<c[0]<<'\t'<<c[1]<<'\t'<<labels[c[0]]<<'\t'<<labels[c[1]]<<'\n';++pairs;
        }
    }
    write_vector(out+"/T0_TARGETS.u32le.bin",t0);
    std::ofstream detail(out+"/T0_SUPPORTS.json");
    detail<<"{\"targets\":[";
    for(size_t i=0;i<t0.size();++i){int t=t0[i];if(i)detail<<',';detail<<"{\"target\":"<<t<<",\"R3_count\":"<<counts3[t]<<",\"provider_columns\":[";bool first=true;for(int w=0;w<TW;++w){uint64_t bits=trans3[size_t(t)*TW+w];while(bits){int j=64*w+__builtin_ctzll(bits);if(!first)detail<<',';first=false;detail<<j;bits&=bits-1;}}detail<<"]}";}
    detail<<"]}\n";
    const std::string status=(!zeros.empty()||!singletons.empty())?"STRICT_K2_OBSTRUCTION_AT_T0":"T0_NECESSARY_GATE_PASSES_NO_INTEGER_EXISTENCE_CONCLUSION";
    int witness=!zeros.empty()?zeros[0]:(!singletons.empty()?singletons[0]:-1);
    std::ofstream result(out+"/NATIVE_RESULT.json");
    result<<"{\"status\":\""<<status<<"\",\"pid\":"<<getpid()<<",\"source_n\":"<<N<<",\"source_m\":"<<M
      <<",\"ports\":"<<K<<",\"all_port_spares\":1,\"R3_header_KNW\":[648,15552,243],\"literal_source_reads\":1,\"computed_R2_balls\":648,\"R3_balls_recomputed\":0,\"source_D4_BFS_runs\":0,\"T0_size\":"<<t0.size()
      <<",\"T0_min_R3_support\":"<<(t0.empty()?-1:min3)<<",\"T0_max_R3_support\":"<<max3<<",\"T0_min_support_target\":"<<min3target
      <<",\"T0_zero_R3_support_targets\":"<<zeros.size()<<",\"T0_singleton_R3_support_targets\":"<<singletons.size()<<",\"T0_pair_R3_support_targets\":"<<pairs
      <<",\"first_strict_obstruction_target\":"<<witness<<",\"all_target_R2_provider_min\":"<<*std::min_element(counts2.begin(),counts2.end())
      <<",\"all_target_R2_provider_max\":"<<*std::max_element(counts2.begin(),counts2.end())
      <<",\"all_target_R3_provider_min\":"<<*std::min_element(counts3.begin(),counts3.end())<<",\"all_target_R3_provider_max\":"<<*std::max_element(counts3.begin(),counts3.end())
      <<",\"R2_ball_size_histogram\":";json_hist(result,balls2);result<<",\"inherited_R3_ball_size_histogram\":";json_hist(result,balls3);
    result<<",\"R2_provider_count_histogram\":";json_hist(result,hist2);result<<",\"T0_R3_provider_count_histogram\":";json_hist(result,hist3t0);
    result<<",\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<",\"solver_calls\":0,\"new_graphs\":0}\n";assert(result.good());
    std::cout<<status<<" T0="<<t0.size()<<" min3="<<(t0.empty()?-1:min3)<<" zeros="<<zeros.size()<<" singletons="<<singletons.size()<<std::endl;
}

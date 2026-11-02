#include <algorithm>
#include <cstdint>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int N=94186,K=3685,W=1472;
struct BudgetStop{};
double started,allowance;
string stage="start";
double cpu(){return double(clock())/CLOCKS_PER_SEC-started;}
void check(){if(cpu()>=allowance)throw BudgetStop{};}
vector<uint64_t> read_bits(const string& path){
    vector<uint64_t> v(size_t(K)*W);
    ifstream f(path,ios::binary);f.read(reinterpret_cast<char*>(v.data()),v.size()*8);
    if(size_t(f.gcount())!=v.size()*8)throw runtime_error("Input cache size mismatch");
    for(int j=0;j<K;++j)if(v[size_t(j)*W+W-1]>>(N%64))throw runtime_error("Nonzero padding");
    return v;
}
template<class T>void binary(const string& path,const vector<T>& data){
    ofstream f(path,ios::binary);f.write(reinterpret_cast<const char*>(data.data()),data.size()*sizeof(T));
    if(!f)throw runtime_error("Output write failed");
}
template<class T>void json_array(ostream& out,const vector<T>& data){
    out<<'[';for(size_t i=0;i<data.size();++i){if(i)out<<',';out<<data[i];}out<<']';
}
int main(int argc,char**argv){
    if(argc!=6)return 2;
    started=double(clock())/CLOCKS_PER_SEC;allowance=stod(argv[5]);
    string outdir=argv[4];
    try{
        stage="read_complete_caches";
        auto r3=read_bits(argv[1]),r4=read_bits(argv[2]);
        vector<int> labels,spares;int label,spare;
        ifstream info(argv[3]);while(info>>label>>spare){labels.push_back(label);spares.push_back(spare);}
        if(labels.size()!=K)throw runtime_error("Port order size mismatch");
        for(int x:spares)if(x<1 || x>2)throw runtime_error("Unexpected current capacity");
        double after_read=cpu();check();
        stage="exact_port_pair_groups";
        vector<int> order(K);iota(order.begin(),order.end(),0);
        auto compare_port=[&](int a,int b){
            int c=memcmp(r3.data()+size_t(a)*W,r3.data()+size_t(b)*W,W*8);
            if(c)return c;
            return memcmp(r4.data()+size_t(a)*W,r4.data()+size_t(b)*W,W*8);
        };
        sort(order.begin(),order.end(),[&](int a,int b){int c=compare_port(a,b);return c?c<0:a<b;});
        vector<vector<int>> groups;
        for(int j:order){
            if(groups.empty() || compare_port(groups.back()[0],j)!=0)groups.push_back({});
            groups.back().push_back(j);
        }
        sort(groups.begin(),groups.end(),[](const auto&a,const auto&b){return a[0]<b[0];});
        const int G=groups.size(),GW=(G+63)/64;
        vector<uint32_t> port_map(K);
        int cap1=0,cap2=0,max_group=0;
        ofstream ports(outdir+"/PORT_GROUPS.json");
        ports<<"{\"signature\":\"ordered pair of full R3 and R4 target bitsets\",\"groups\":[";
        for(int g=0;g<G;++g){
            if(g)ports<<',';
            int sum=0,twice=-1;
            vector<int> old,ss;
            for(int j:groups[g]){port_map[j]=g;sum+=spares[j];old.push_back(labels[j]);ss.push_back(spares[j]);if(spares[j]>=2)twice=labels[j];}
            int cap=min(2,sum);cap1+=cap==1;cap2+=cap==2;max_group=max(max_group,int(groups[g].size()));
            ports<<"{\"group\":"<<g<<",\"representative_column\":"<<groups[g][0]
                <<",\"representative_old_label\":"<<old[0]<<",\"member_columns\":";
            json_array(ports,groups[g]);ports<<",\"member_old_labels\":";json_array(ports,old);
            ports<<",\"member_spares\":";json_array(ports,ss);
            ports<<",\"sum_spare\":"<<sum<<",\"two_helper_capacity\":"<<cap;
            if(cap==2){
                vector<int> choice=twice>=0?vector<int>{twice,twice}:vector<int>{old[0],old[1]};
                ports<<",\"literal_ports_for_two_uses\":";json_array(ports,choice);
            }
            ports<<'}';
        }
        ports<<"]}\n";ports.close();
        binary(outdir+"/port_to_group.u32le.bin",port_map);
        double after_ports=cpu();check();
        stage="complete_group_support_transpose";
        vector<uint64_t> support3(size_t(N)*GW),support4(size_t(N)*GW);
        uint64_t ones3=0,ones4=0;
        for(int g=0;g<G;++g){
            if(g%16==0)check();
            int j=groups[g][0],gw=g/64;uint64_t bit=uint64_t(1)<<(g%64);
            for(int w=0;w<W;++w){
                uint64_t x=r3[size_t(j)*W+w];
                while(x){int t=64*w+__builtin_ctzll(x);support3[size_t(t)*GW+gw]|=bit;x&=x-1;++ones3;}
                x=r4[size_t(j)*W+w];
                while(x){int t=64*w+__builtin_ctzll(x);support4[size_t(t)*GW+gw]|=bit;x&=x-1;++ones4;}
            }
        }
        double after_transpose=cpu();check();
        stage="exact_target_row_pair_groups";
        vector<int> targets(N);iota(targets.begin(),targets.end(),0);
        auto compare_target=[&](int a,int b){
            int c=memcmp(support4.data()+size_t(a)*GW,support4.data()+size_t(b)*GW,GW*8);
            if(c)return c;
            return memcmp(support3.data()+size_t(a)*GW,support3.data()+size_t(b)*GW,GW*8);
        };
        uint64_t comparisons=0;
        sort(targets.begin(),targets.end(),[&](int a,int b){
            if(++comparisons%100000==0)check();
            int c=compare_target(a,b);return c?c<0:a<b;
        });
        vector<int> representatives,counts;
        vector<uint32_t> target_map(N);
        for(int t:targets){
            if(representatives.empty() || compare_target(representatives.back(),t)!=0){representatives.push_back(t);counts.push_back(0);}
            target_map[t]=representatives.size()-1;++counts.back();
        }
        const int C=representatives.size();
        vector<int> class_order(C);iota(class_order.begin(),class_order.end(),0);
        sort(class_order.begin(),class_order.end(),[&](int a,int b){return representatives[a]<representatives[b];});
        vector<int> sorted_reps(C),sorted_counts(C);
        vector<uint32_t> remap(C);
        for(int c=0;c<C;++c){int old=class_order[c];remap[old]=c;sorted_reps[c]=representatives[old];sorted_counts[c]=counts[old];}
        for(auto& c:target_map)c=remap[c];
        int max_class=*max_element(sorted_counts.begin(),sorted_counts.end());
        double after_targets=cpu();check();
        stage="save_complete_equivalence_data";
        ofstream classes(outdir+"/TARGET_CLASSES.json");
        classes<<"{\"signature\":\"ordered (R4 group support,R3 group support)\",\"class_representatives\":";
        json_array(classes,sorted_reps);classes<<",\"class_counts\":";json_array(classes,sorted_counts);
        classes<<",\"membership_file\":\"target_to_class.u32le.bin\"}\n";classes.close();
        binary(outdir+"/target_to_class.u32le.bin",target_map);
        binary(outdir+"/target_R3_group_support.u64le.bin",support3);
        check();
        binary(outdir+"/target_R4_group_support.u64le.bin",support4);
        ofstream result(outdir+"/NATIVE_RESULT.json");
        result<<"{\"status\":\"COMPLETE_EXACT_EQUALITY_COMPRESSION\",\"source_targets\":"<<N
            <<",\"original_ports\":"<<K<<",\"port_groups\":"<<G<<",\"removed_duplicate_ports\":"<<K-G
            <<",\"maximum_port_group_size\":"<<max_group<<",\"group_capacity1_count\":"<<cap1
            <<",\"group_capacity2_count\":"<<cap2<<",\"target_row_classes\":"<<C
            <<",\"removed_duplicate_target_rows\":"<<N-C<<",\"maximum_target_class_size\":"<<max_class
            <<",\"original_coverage_clauses_for_both_helpers\":"<<2*N
            <<",\"equivalent_complete_coverage_clauses\":"<<2*C
            <<",\"selector_variables_after_grouping\":"<<2*G
            <<",\"support_words_per_target\":"<<GW<<",\"support_rows\":"<<N
            <<",\"group_R3_support_ones\":"<<ones3<<",\"group_R4_support_ones\":"<<ones4
            <<",\"group_equality\":\"complete exact byte comparison, no containment\""
            <<",\"CPU_read\":"<<after_read<<",\"CPU_port_groups\":"<<after_ports-after_read
            <<",\"CPU_transpose\":"<<after_transpose-after_ports<<",\"CPU_target_groups\":"<<after_targets-after_transpose
            <<",\"CPU_save\":"<<cpu()-after_targets<<",\"CPU_seconds\":"<<cpu()
            <<",\"source_graph_reads\":0,\"BFS_runs\":0,\"solver_calls\":0}\n";
        cout<<"COMPLETE ports "<<G<<"/"<<K<<" targets "<<C<<"/"<<N<<" CPU "<<cpu()<<'\n';
        return 0;
    }catch(const BudgetStop&){
        ofstream out(outdir+"/NATIVE_RESULT.json");
        out<<"{\"status\":\"CPU_BUDGET_STOP\",\"stage\":\""<<stage<<"\",\"CPU_seconds\":"<<cpu()<<"}\n";
        return 3;
    }catch(const exception&e){cerr<<stage<<": "<<e.what()<<'\n';return 2;}
}

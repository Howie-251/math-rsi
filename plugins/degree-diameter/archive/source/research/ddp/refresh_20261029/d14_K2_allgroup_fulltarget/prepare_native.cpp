#include <array>
#include <cassert>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <ctime>
#include <sys/resource.h>
#include <unistd.h>

constexpr int N=94186,K=3589,W=57;
using Row=std::array<uint64_t,2*W>;

template<class T> std::vector<T> read_exact(const std::string &p,size_t n) {
    std::ifstream f(p,std::ios::binary|std::ios::ate);
    assert(f && size_t(f.tellg())==n*sizeof(T));
    f.seekg(0);
    std::vector<T> v(n);
    f.read(reinterpret_cast<char*>(v.data()),n*sizeof(T));
    assert(f.good());
    return v;
}
template<class T> void write_binary(const std::string &p,const std::vector<T> &v) {
    std::ofstream f(p,std::ios::binary);
    f.write(reinterpret_cast<const char*>(v.data()),v.size()*sizeof(T));
    assert(f.good());
}

int main(int argc,char **argv) {
    assert(argc==5);
    const double start=double(clock())/CLOCKS_PER_SEC;
    const uint16_t endian=1;
    assert(*reinterpret_cast<const uint8_t*>(&endian)==1);
    const std::string outdir=argv[4];
    const auto r3=read_exact<uint64_t>(argv[1],size_t(N)*W);
    const auto r4=read_exact<uint64_t>(argv[2],size_t(N)*W);
    const auto caps=read_exact<uint8_t>(argv[3],K);
    int cap1=0,cap2=0;
    for(auto c:caps) { assert(c==1 || c==2);cap1+=(c==1);cap2+=(c==2); }
    assert(cap1==3480 && cap2==109);

    // Key is the complete A-selector support followed by complete B support.
    // Padding bits must be zero. Ordered-map key comparison is exact equality;
    // no support containment, row implication or symmetry filtering is applied.
    std::map<Row,uint32_t> seen;
    std::vector<uint32_t> rowmap(2*size_t(N)),multiplicity;
    std::vector<std::array<uint32_t,2>> representatives;
    for(int t=0;t<N;++t) {
        const uint64_t *p3=&r3[size_t(t)*W],*p4=&r4[size_t(t)*W];
        assert((p3[W-1]>>(K%64))==0 && (p4[W-1]>>(K%64))==0);
        for(int w=0;w<W;++w) assert((p3[w]&~p4[w])==0);
        for(int side=0;side<2;++side) {
            Row key;
            const uint64_t *a=(side==0 ? p4 : p3),*b=(side==0 ? p3 : p4);
            std::memcpy(key.data(),a,W*sizeof(uint64_t));
            std::memcpy(key.data()+W,b,W*sizeof(uint64_t));
            const uint32_t next=uint32_t(representatives.size());
            auto [it,added]=seen.emplace(key,next);
            if(added) {
                representatives.push_back({uint32_t(side),uint32_t(t)});
                multiplicity.push_back(0);
            }
            rowmap[size_t(side)*N+t]=it->second;
            ++multiplicity[it->second];
        }
    }
    uint64_t original_rows=0;
    for(uint32_t c:multiplicity) original_rows+=c;
    assert(original_rows==2*uint64_t(N));
    write_binary(outdir+"/target_side_to_coverage_row.u32le.bin",rowmap);
    write_binary(outdir+"/coverage_row_multiplicities.u32le.bin",multiplicity);
    {
        std::ofstream f(outdir+"/coverage_row_representatives.tsv");
        f<<"coverage_row\tside\ttarget\tmultiplicity\n";
        for(size_t i=0;i<representatives.size();++i)
            f<<i<<'\t'<<representatives[i][0]<<'\t'<<representatives[i][1]<<'\t'<<multiplicity[i]<<'\n';
        assert(f.good());
    }
    // All exact keys have now been used; the output needs only representatives.
    seen.clear();
    std::cout<<"{\"stage\":\"ALL_TARGET_ROWS_GROUPED\",\"pid\":"<<getpid()
             <<",\"unique_rows\":"<<representatives.size()<<",\"CPU_seconds\":"
             <<double(clock())/CLOCKS_PER_SEC-start<<"}"<<std::endl;

    constexpr int VARIABLES=2*K+2*K*13;
    constexpr uint64_t CARDINALITY_CLAUSES=2*(13+uint64_t(K-1)*27);
    const uint64_t expected_clauses=CARDINALITY_CLAUSES+cap1+representatives.size();
    std::ofstream cnf(outdir+"/model.cnf",std::ios::binary);
    cnf<<"p cnf "<<VARIABLES<<' '<<expected_clauses<<'\n';
    uint64_t clauses=0,literals=0;
    std::string buf;
    buf.reserve(2*1024*1024);
    auto flush=[&](){ cnf.write(buf.data(),buf.size());buf.clear();assert(cnf.good()); };
    auto append=[&](const std::vector<int>& row){
        for(int x:row) { buf+=std::to_string(x);buf+=' '; }
        buf+="0\n";++clauses;literals+=row.size();
        if(buf.size()>=1024*1024)flush();
    };
    int variables=2*K;
    for(int side=0;side<2;++side) {
        std::array<int,13> previous{};
        for(int j=0;j<K;++j) {
            const int x=1+side*K+j;
            std::array<int,13> cur;
            for(int k=0;k<13;++k)cur[k]=++variables;
            append({-x,cur[0]});
            if(j==0) {
                for(int k=1;k<13;++k)append({-cur[k]});
            } else {
                for(int k=0;k<13;++k)append({-previous[k],cur[k]});
                for(int k=1;k<13;++k)append({-x,-previous[k-1],cur[k]});
                append({-x,-previous[12]});
            }
            previous=cur;
        }
    }
    assert(variables==VARIABLES && clauses==CARDINALITY_CLAUSES);
    for(int j=0;j<K;++j)if(caps[j]==1)append({-(j+1),-(K+j+1)});
    const uint64_t base_clauses=clauses;
    std::array<std::string,2*K> literal_text;
    for(int i=0;i<2*K;++i)literal_text[i]=std::to_string(i+1)+" ";
    int min_width=2*K,max_width=0;
    for(const auto &rep:representatives) {
        const int side=rep[0],t=rep[1];
        const uint64_t *p3=&r3[size_t(t)*W],*p4=&r4[size_t(t)*W];
        int width=0;
        for(int selected_side=0;selected_side<2;++selected_side) {
            const uint64_t *p=(selected_side==side ? p4 : p3);
            for(int w=0;w<W;++w) {
                uint64_t bits=p[w];
                while(bits) {
                    const int bit=__builtin_ctzll(bits);
                    const int g=64*w+bit;
                    assert(g<K);
                    buf+=literal_text[selected_side*K+g];
                    ++width;bits&=bits-1;
                }
            }
        }
        assert(width>0);
        min_width=std::min(min_width,width);max_width=std::max(max_width,width);
        buf+="0\n";++clauses;literals+=width;
        if(buf.size()>=1024*1024)flush();
    }
    flush();cnf.flush();assert(cnf.good());
    const uint64_t bytes=uint64_t(cnf.tellp());
    cnf.close();assert(clauses==expected_clauses);
    struct rusage ru{};getrusage(RUSAGE_SELF,&ru);
    std::ofstream result(outdir+"/CNF_BUILD_RESULT.json");
    result<<"{\n"
      <<"  \"status\": \"FULL_ALLGROUP_CNF_PREPARED_NOT_SOLVED\",\n"
      <<"  \"pid\": "<<getpid()<<",\n"
      <<"  \"variables\": "<<variables<<",\n"
      <<"  \"selector_variables\": "<<2*K<<",\n"
      <<"  \"cardinality_clauses\": "<<CARDINALITY_CLAUSES<<",\n"
      <<"  \"capacity_mutex_clauses\": "<<cap1<<",\n"
      <<"  \"base_clauses\": "<<base_clauses<<",\n"
      <<"  \"original_sided_rows\": "<<2*N<<",\n"
      <<"  \"unique_coverage_rows\": "<<representatives.size()<<",\n"
      <<"  \"duplicate_coverage_rows\": "<<2*N-representatives.size()<<",\n"
      <<"  \"clauses\": "<<clauses<<",\n"
      <<"  \"literal_occurrences\": "<<literals<<",\n"
      <<"  \"min_coverage_clause_literals\": "<<min_width<<",\n"
      <<"  \"max_coverage_clause_literals\": "<<max_width<<",\n"
      <<"  \"cnf_bytes\": "<<bytes<<",\n"
      <<"  \"native_CPU_seconds\": "<<double(clock())/CLOCKS_PER_SEC-start<<",\n"
      <<"  \"native_peak_RSS_KiB\": "<<ru.ru_maxrss<<"\n}\n";
    assert(result.good());
    std::cout<<"{\"stage\":\"COMPLETE\",\"pid\":"<<getpid()
      <<",\"variables\":"<<variables<<",\"clauses\":"<<clauses
      <<",\"cnf_bytes\":"<<bytes<<"}"<<std::endl;
}

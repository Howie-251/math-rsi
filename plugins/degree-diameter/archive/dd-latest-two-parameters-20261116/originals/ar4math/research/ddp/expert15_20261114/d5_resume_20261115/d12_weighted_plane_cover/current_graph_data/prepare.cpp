#include <algorithm>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <sys/resource.h>

double cpu(){return double(std::clock())/CLOCKS_PER_SEC;}
void u32(std::ostream&out,uint32_t x){for(int i=0;i<4;++i)out.put(char((x>>(8*i))&255));}
void u64(std::ostream&out,uint64_t x){for(int i=0;i<8;++i)out.put(char((x>>(8*i))&255));}
int main(int argc,char**argv){
    try{
        if(argc!=3)throw std::runtime_error("usage: prepare SOURCE.edges OUTDIR");
        rlimit limit{15,15},mem{2ULL*1024*1024*1024,2ULL*1024*1024*1024};setrlimit(RLIMIT_CPU,&limit);setrlimit(RLIMIT_AS,&mem);
        double start=cpu();std::string dir=argv[2];std::ifstream in(argv[1]);int n,m,a,b;
        if(!(in>>n>>m)||n!=42402||m!=245937)throw std::runtime_error("not the bound current42402 source");
        std::vector<std::vector<int>>rows(n);int edgecount=0;
        while(in>>a>>b){if(a<0||a>=n||b<0||b>=n||a==b)throw std::runtime_error("invalid source edge");rows[a].push_back(b);rows[b].push_back(a);++edgecount;}
        if(!in.eof()||edgecount!=m)throw std::runtime_error("source edge count mismatch");
        std::vector<uint32_t>ptr(n+1),adj;adj.reserve(2*m);
        std::vector<int>free,freeindex(n,-1);std::vector<uint8_t>degree(n),capacity(n);
        for(int v=0;v<n;++v){auto&row=rows[v];std::sort(row.begin(),row.end());
            if(row.size()>12||std::adjacent_find(row.begin(),row.end())!=row.end())throw std::runtime_error("source not simple/max12");
            degree[v]=row.size();capacity[v]=12-row.size();
            if(row.size()<12){freeindex[v]=free.size();free.push_back(v);}
            ptr[v]=adj.size();for(int w:row)adj.push_back(w);}
        ptr[n]=adj.size();if(free.size()!=13857)throw std::runtime_error("current free count mismatch");
        {std::ofstream out(dir+"/SOURCE_CSR.u32le.bin",std::ios::binary);u32(out,n);u32(out,m);for(auto x:ptr)u32(out,x);for(auto x:adj)u32(out,x);}
        {std::ofstream out(dir+"/FREE_IDS.u32le.bin",std::ios::binary);for(int x:free)u32(out,x);}
        {std::ofstream out(dir+"/DEGREES.u8.bin",std::ios::binary);out.write(reinterpret_cast<char*>(degree.data()),degree.size());}
        {std::ofstream out(dir+"/CAPACITY.u8.bin",std::ios::binary);out.write(reinterpret_cast<char*>(capacity.data()),capacity.size());}
        constexpr int begin=41356,end=42402,roots=end-begin;
        int words=(free.size()+63)/64;std::vector<uint64_t>bits(words);
        std::vector<int>stamp(n),queue(n);std::vector<uint8_t>d(n);long providerbits=0;
        int mincovered=n,maxcovered=0;double bfsstart=cpu();
        std::ofstream providers(dir+"/PERIPHERY_R4_FREE.u64le.bin",std::ios::binary);
        std::ofstream stats(dir+"/PROVIDER_STATS.csv");stats<<"provider_id,ball4_size,sphere0,sphere1,sphere2,sphere3,sphere4,covered_free\n";
        for(int root=begin;root<end;++root){int tag=root-begin+1,head=0,tail=0;queue[tail++]=root;stamp[root]=tag;d[root]=0;
            int spheres[5]={1,0,0,0,0};
            while(head!=tail){int v=queue[head++];if(d[v]==4)continue;
                for(uint32_t j=ptr[v];j<ptr[v+1];++j){int w=adj[j];if(stamp[w]!=tag){stamp[w]=tag;d[w]=d[v]+1;++spheres[d[w]];queue[tail++]=w;}}}
            std::fill(bits.begin(),bits.end(),0);int count=0;
            for(int j=0;j<tail;++j){int index=freeindex[queue[j]];if(index>=0){bits[index/64]|=uint64_t(1)<<(index%64);++count;}}
            for(uint64_t x:bits)u64(providers,x);
            providerbits+=count;mincovered=std::min(mincovered,count);maxcovered=std::max(maxcovered,count);
            stats<<root<<','<<tail;for(int x:spheres)stats<<','<<x;stats<<','<<count<<'\n';
        }
        providers.close();stats.close();if(!providers||!stats)throw std::runtime_error("provider output failed");
        std::ofstream meta(dir+"/PROVIDERS_META.json");
        meta<<"{\n\"status\":\"COMPLETE_CURRENT42402_ALL_PERIPHERY_R4\",\n\"source_n\":"<<n<<",\"source_m\":"<<m
            <<",\n\"free_count\":"<<free.size()<<",\"free_rule\":\"actual current degree<12\",\"provider_first_id\":41356,\"provider_end_exclusive\":42402,\"provider_rows\":"<<roots
            <<",\n\"BFS_roots_completed\":"<<roots<<",\"BFS_depth\":4,\"provider_words_per_row\":"<<words<<",\"provider_row_bytes\":"<<8*words
            <<",\n\"provider_total_bytes\":"<<long(roots)*words*8<<",\"provider_bit_order\":\"bit k is FREE_IDS[k], LSB-first uint64 little endian; row i is vertex41356+i\",\"padding_bits_zero\":true"
            <<",\n\"CSR_layout\":\"u32le n,m then n+1 offsets then 2m sorted adjacent IDs\",\"covered_free_min_max\":["<<mincovered<<','<<maxcovered<<"],\"covered_free_sum\":"<<providerbits
            <<",\n\"BFS_CPU\":"<<cpu()-bfsstart<<",\"native_CPU\":"<<cpu()-start<<",\"single_thread\":true,\"source_D5_revalidated\":false,\"solver_calls\":0}\n";
        std::cout<<"COMPLETE n="<<n<<" m="<<m<<" free="<<free.size()<<" roots="<<roots<<" native_CPU="<<cpu()-start<<'\n';
    }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}
}

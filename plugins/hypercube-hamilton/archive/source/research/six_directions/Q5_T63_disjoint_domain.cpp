#include <array>
#include <vector>
#include <string>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std;
int main(int argc,char**argv){
 if(argc!=6)return 2;
 ifstream ni(argv[1],ios::binary),nu(argv[2],ios::binary),tl(argv[3],ios::binary);
 ofstream output(argv[4],ios::binary),report(argv[5]);
 vector<array<unsigned char,18>> N;array<unsigned char,18> r;
 while(ni.read((char*)r.data(),18))N.push_back(r);
 vector<uint32_t> masks(N.size());nu.read((char*)masks.data(),4*masks.size());
 if(nu.gcount()!=4*(long long)masks.size()||N.size()!=270270)return 3;
 array<vector<int>,33> bywidth;
 for(int i=0;i<(int)N.size();++i)bywidth[__builtin_popcount(masks[i])].push_back(i);
 vector<pair<int,int>> edges;array<array<int,16>,16> ix;
 for(auto& a:ix)a.fill(-1);
 for(int a=0;a<16;++a)for(int b=a+1;b<16;++b)if(__builtin_popcount(unsigned(a^b))==1){ix[a][b]=ix[b][a]=edges.size();edges.push_back({a,b});}
 unordered_map<string,uint32_t> seen;long long comparisons=0,pairs=0,lowrecords=0;
 array<long long,33> counts{};array<unsigned char,22> low;
 while(tl.read((char*)low.data(),22)){
  ++lowrecords;uint32_t baseMask=0;for(int i=0;i<4;++i)baseMask|=uint32_t(low[18+i])<<(8*i);
  array<int,4> perm{0,1,2,3};
  do{
   array<int,16> mapping{};
   for(int shift=0;shift<16;++shift)if(__builtin_popcount(unsigned(shift))%2){
    for(int x=0;x<16;++x){int y=0;for(int j=0;j<4;++j)y|=((x>>perm[j])&1)<<j;mapping[x]=y^shift;}
    string key(18,char(255));
    for(int x=0;x<16;++x)if(low[x]!=255)key[mapping[x]]=char(mapping[low[x]]);
    key[16]=char(min(mapping[low[16]],mapping[low[17]]));key[17]=char(max(mapping[low[16]],mapping[low[17]]));
    uint32_t bm=0;
    for(int i=0;i<32;++i)if(baseMask>>i&1){auto[a,b]=edges[i];bm|=uint32_t(1)<<ix[mapping[a]][mapping[b]];}
    auto[it,fresh]=seen.emplace(key,bm);if(!fresh){if(it->second!=bm)return 4;continue;}
    int width=__builtin_popcount(bm);
    for(int w=0;w<=32-width;++w)for(int index:bywidth[w]){
     ++comparisons;if(masks[index]&bm)continue;
     output.write((char*)N[index].data(),16);output.write(key.data(),18);
     ++pairs;++counts[width];
    }
   }
  }while(next_permutation(perm.begin(),perm.end()));
 }
 if(lowrecords!=6978)return 5;
 report<<"{\"canonical_N14_inputs\":"<<N.size()<<",\"canonical_T44_low_inputs\":"<<lowrecords
 <<",\"distinct_transformed_T44_low_states\":"<<seen.size()<<",\"width_filtered_scalar_comparisons\":"<<comparisons
 <<",\"disjoint_pairs\":"<<pairs<<",\"bytes_per_pair\":34,\"pairs_by_T44_union_size\":{";
 bool comma=false;for(int w=0;w<=32;++w)if(counts[w]){if(comma)report<<",";comma=true;report<<"\""<<w<<"\":"<<counts[w];}
 report<<"}}\n";
 cout<<seen.size()<<" distinct T44 states; "<<comparisons<<" comparisons; "<<pairs<<" disjoint pairs\n";
}

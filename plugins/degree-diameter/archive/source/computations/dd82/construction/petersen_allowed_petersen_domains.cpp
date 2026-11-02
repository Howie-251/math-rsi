// Complete labeled-Petersen containment domains for twelve given graphs.
// Uses the same 30240-copy generator as petersen_internal_reassembly.cpp.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
int main(int argc,char**argv) {
  assert(argc==3);clock_t start=clock();
  int index[10][10];std::vector<std::pair<int,int>> edges;
  for(int u=0;u<10;++u)for(int v=u+1;v<10;++v) {
    index[u][v]=index[v][u]=edges.size();edges.emplace_back(u,v);
  }
  const std::vector<std::pair<int,int>> standard={{0,1},{0,4},{0,5},{1,2},{1,6},
    {2,3},{2,7},{3,4},{3,8},{4,9},{5,7},{5,8},{6,8},{6,9},{7,9}};
  std::array<int,10> p{};for(int u=0;u<10;++u)p[u]=u;
  std::set<uint64_t> catalog;
  do {
    if(!(p[1]<p[4]&&p[4]<p[5]&&p[2]<p[6]))continue;
    uint64_t mask=0;for(auto [u,v]:standard)mask|=1ULL<<index[p[u]][p[v]];
    assert(catalog.insert(mask).second);
  }while(std::next_permutation(p.begin()+1,p.end()));
  assert(catalog.size()==30240);
  std::ifstream input(argv[1]);int cases;input>>cases;assert(cases==12);
  std::ofstream output(argv[2]);output.precision(12);
  output<<"{\"catalog_size\":30240,\"domains\":[";
  for(int c=0;c<cases;++c) {
    uint64_t allowed,seed;input>>allowed>>seed;assert(catalog.count(seed));
    std::vector<uint64_t> domain;int minimum=100,min_count=0;uint64_t witness=0;
    for(auto mask:catalog) {
      int missing=__builtin_popcountll(mask&~allowed);
      if(!missing)domain.push_back(mask);
      if(missing<minimum){minimum=missing;min_count=1;witness=mask;}
      else if(missing==minimum)++min_count;
    }
    if(c)output<<",";
    output<<"{\"input_index\":"<<c<<",\"source_index\":"<<c/6
          <<",\"fiber\":"<<c%6<<",\"allowed_mask\":"<<allowed
          <<",\"allowed_edge_count\":"<<__builtin_popcountll(allowed)
          <<",\"domain_size\":"<<domain.size()
          <<",\"seed_internal_in_domain\":"<<((seed&~allowed)?"false":"true")
          <<",\"minimum_forbidden_edges\":"<<minimum
          <<",\"minimum_attaining_copies\":"<<min_count
          <<",\"one_closest_copy_mask\":"<<witness<<",\"all_domain_masks\":[";
    for(size_t i=0;i<domain.size();++i){if(i)output<<",";output<<domain[i];}
    output<<"]}";
  }
  output<<"],\"complete\":true,\"internal_cpu_seconds\":"
        <<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
  std::cout<<"complete 12 domains over "<<catalog.size()<<" labeled copies, cpu "
           <<double(clock()-start)/CLOCKS_PER_SEC<<"\n";
}

#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

using Row=std::array<int,5>;
using Matrix=std::array<Row,5>;
struct Input { int id, expected; uint64_t key; Matrix matrix; };
double cpu(){return double(std::clock())/CLOCKS_PER_SEC;}
void require(bool b,const std::string&s){if(!b)throw std::runtime_error(s);}
std::vector<Row> rows, permutations;
std::vector<uint32_t> colors;
std::map<uint64_t,uint64_t> orbit_sizes;
Matrix current{};
Row sums{};
uint64_t terminals=0, visited_nodes=0;

uint64_t encode(const Matrix&m){
 uint64_t ans=0;
 for(const auto&r:m)for(int x:r)ans=5*ans+x;
 return ans;
}
// Every column permutation, followed by lexicographic row sorting, is considered.
// Canonicalization is performed for EVERY complete matrix: no doublelex filter.
uint64_t canonical(const Matrix&m){
 uint64_t ans=UINT64_MAX;
 for(const auto&p:permutations){
  std::array<unsigned,5> words{};
  for(int i=0;i<5;++i)for(int j=0;j<5;++j)words[i]=5*words[i]+m[i][p[j]];
  std::sort(words.begin(),words.end());
  uint64_t value=0;
  for(unsigned w:words)value=3125*value+w;
  ans=std::min(ans,value);
 }
 return ans;
}
void generate(int depth,int lower){
 ++visited_nodes;
 if(depth==5){
  require(sums==Row{4,4,4,4,4},"terminal column sums");
  ++terminals; ++orbit_sizes[canonical(current)]; return;
 }
 // In contrast to the producer, the fifth row is also freely selected from all
 // 70 rows. Only nondecreasing rows and column capacities prune this recursion.
 for(int k=lower;k<int(rows.size());++k){
  bool possible=true;
  for(int j=0;j<5;++j)if(sums[j]+rows[k][j]>4)possible=false;
  if(!possible)continue;
  current[depth]=rows[k];
  for(int j=0;j<5;++j)sums[j]+=rows[k][j];
  generate(depth+1,k);
  for(int j=0;j<5;++j)sums[j]-=rows[k][j];
 }
}
std::array<uint32_t,5> fixed_rows(){
 std::array<uint32_t,5>a{};
 for(int i=0;i<5;++i)a[i]=uint32_t(15)<<(4*i);
 return a;
}
bool conflict(uint32_t red,const std::array<uint32_t,5>&blocks){
 bool all_red=false,all_blue=false;
 for(uint32_t b:blocks){
  uint32_t x=red&b;
  if(x==b)all_red=true;
  if(x==0)all_blue=true;
 }
 return all_red&&all_blue;
}
int literal(const Matrix&m){
 std::array<uint32_t,5> rb{},cb{};
 int label=0;
 for(int i=0;i<5;++i)for(int j=0;j<5;++j)for(int k=0;k<m[i][j];++k){
  require(label<20,"too many labels");
  rb[i]|=uint32_t(1)<<label; cb[j]|=uint32_t(1)<<label; ++label;
 }
 require(label==20&&rb==fixed_rows(),"twenty labels and fixed four-point rows");
 uint32_t used=0;
 for(uint32_t b:cb){require(__builtin_popcount(b)==4&&!(used&b),"column partition");used|=b;}
 int answer=0;
 for(uint32_t red:colors){
  if(conflict(red,rb)&&conflict(red,cb))++answer;
 }
 return answer;
}
int main(int argc,char**argv){
 try{
  const double start=cpu();
  const bool profile=argc>1&&std::string(argv[1])=="profile";
  std::ifstream in("INPUT.txt"); int n=0; in>>n;
  require(n==264,"264 input representatives");
  std::vector<Input> input(n); std::set<uint64_t> expected_keys;
  for(auto&x:input){
   in>>x.id>>x.key>>x.expected;
   for(auto&r:x.matrix)for(int&v:r)in>>v;
   require(bool(in),"complete input");
   for(const auto&r:x.matrix)require(std::accumulate(r.begin(),r.end(),0)==4,"input row sum");
   for(int j=0;j<5;++j){int s=0;for(int i=0;i<5;++i)s+=x.matrix[i][j];require(s==4,"input column sum");}
   require(encode(x.matrix)==x.key,"input encoded key");
   require(expected_keys.insert(x.key).second,"distinct keys");
  }
  // Independent row domain generation: enumerate all 5^5 digit vectors.
  for(int word=0;word<3125;++word){
   int a=word;Row r{};
   for(int j=4;j>=0;--j){r[j]=a%5;a/=5;}
   if(std::accumulate(r.begin(),r.end(),0)==4)rows.push_back(r);
  }
  require(rows.size()==70,"all 70 row compositions");
  Row permutation{0,1,2,3,4};
  do{permutations.push_back(permutation);}while(std::next_permutation(permutation.begin(),permutation.end()));
  require(permutations.size()==120,"120 column permutations");
  // Gosper's algorithm visits every 20-bit integer of Hamming weight ten once.
  uint32_t mask=(1u<<10)-1;
  while(mask<(1u<<20)){
   colors.push_back(mask);
   uint32_t bit=mask&-mask, rise=mask+bit;
   mask=rise+(((rise^mask)/bit)>>2);
  }
  require(colors.size()==184756,"C(20,10) colors");
  const double domain_start=cpu();
  if(!profile){
   generate(0,0);
   require(terminals==19834,"19834 unscreened terminals");
   std::set<uint64_t> generated;
   for(auto [key,multiplicity]:orbit_sizes){
    generated.insert(key); require(expected_keys.count(key)==1,"every generated terminal maps to a producer representative");
   }
   require(generated==expected_keys,"canonical sets equal");
   require(orbit_sizes.size()==264,"264 canonical orbits");
   for(const auto&x:input)require(canonical(x.matrix)==x.key,"each producer matrix is canonical");
  }
  const double domain_cpu=cpu()-domain_start;
  Matrix diag{},offdiag{};
  for(int i=0;i<5;++i)for(int j=0;j<5;++j){diag[i][j]=i==j?4:0;offdiag[i][j]=i==j?0:1;}
  const double count_start=cpu();
  int diagonal=literal(diag),complement=literal(offdiag);
  require(diagonal==16980&&complement==400,"literal controls");
  const int limit=profile?5:n;
  std::vector<int> values;int minimum=184757,maximum=-1,minimizers=0;
  std::map<int,int> histogram;
  for(int i=0;i<limit;++i){
   int value=literal(input[i].matrix);
   require(value==input[i].expected,"literal joint mismatch at id "+std::to_string(input[i].id));
   values.push_back(value);++histogram[value];
   if(value<minimum){minimum=value;minimizers=1;}else if(value==minimum)++minimizers;
   maximum=std::max(maximum,value);
  }
  const double count_cpu=cpu()-count_start;
  if(!profile){require(minimum==400&&maximum==16980&&minimizers==1,"complete extrema");}
  std::ofstream out(profile?"PROFILE.json":"RESULT.json");
  out<<"{\n\"status\":\"PASS\",\"mode\":\""<<(profile?"profile":"full")<<"\",\n"
     <<"\"row_domain\":"<<rows.size()<<",\"column_permutations\":"<<permutations.size()<<",\n"
     <<"\"terminal_matrices\":"<<terminals<<",\"visited_nodes\":"<<visited_nodes<<",\"canonical_domain\":"<<orbit_sizes.size()<<",\n"
     <<"\"doublelex_filter_used\":false,\"complete_domain_checked\":"<<(!profile?"true":"false")<<",\n"
     <<"\"colorings_per_matrix\":"<<colors.size()<<",\"representatives_checked\":"<<limit<<",\n"
     <<"\"representative_coloring_pairs\":"<<uint64_t(limit)*colors.size()<<",\"additional_control_colorings\":"<<2*colors.size()<<",\n"
     <<"\"literal_counts_match_producer\":true,\"baseline_4I\":"<<diagonal<<",\"baseline_J_minus_I\":"<<complement<<",\n"
     <<"\"minimum\":"<<minimum<<",\"maximum\":"<<maximum<<",\"minimizer_count\":"<<minimizers<<",\n"
     <<"\"domain_cpu_seconds\":"<<domain_cpu<<",\"literal_count_cpu_seconds\":"<<count_cpu<<",\"total_cpu_seconds\":"<<cpu()-start<<",\n"
     <<"\"histogram\":{";
  bool first=true;for(auto [value,number]:histogram){if(!first)out<<',';first=false;out<<'\"'<<value<<"\":"<<number;}
  out<<"},\n\"representatives\":[\n";
  for(int i=0;i<limit;++i){
   if(i)out<<",\n";
   out<<"{\"id\":"<<input[i].id<<",\"key\":"<<input[i].key<<",\"jointcount\":"<<values[i]<<",\"producer_jointcount\":"<<input[i].expected;
   if(!profile)out<<",\"row_sorted_terminals_in_orbit\":"<<orbit_sizes.at(input[i].key);
   out<<'}';
  }
  out<<"\n]}\n";
  std::cout<<"PASS mode="<<(profile?"profile":"full")<<" checked="<<limit<<" terminals="<<terminals<<" min="<<minimum<<" domain_cpu="<<domain_cpu<<" literal_cpu="<<count_cpu<<" total_cpu="<<cpu()-start<<'\n';
 }catch(const std::exception&e){std::cerr<<"FAIL "<<e.what()<<'\n';return 1;}
}

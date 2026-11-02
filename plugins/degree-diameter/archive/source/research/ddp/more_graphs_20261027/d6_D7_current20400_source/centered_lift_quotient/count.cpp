#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
struct Port{int to,a,b,c,rev;};
Port port[48][6];
uint32_t countq[1200];
__uint128_t sums[1200];
long long words;
void visit(int v,int a,int b,int c,int forbidden,int depth){
 int q=25*v+a+5*b;countq[q]++;sums[q]|=(__uint128_t(1)<<(c+56));words++;
 if(depth==7)return;
 for(int k=0;k<6;k++)if(k!=forbidden){auto&p=port[v][k];visit(p.to,(a+p.a)%5,(b+p.b)%5,c+p.c,p.rev,depth+1);}
}
struct Witness{int root=-1,q=-1,c=-1;vector<int>integer_sums;};
int main(int argc,char**argv){
 assert(argc==3);clock_t start=clock();rlimit lim{3,3};setrlimit(RLIMIT_CPU,&lim);ifstream in(argv[1]);string out=argv[2];int n,k;in>>n>>k;assert(n==48&&k==6);
 for(auto&row:port)for(auto&p:row)in>>p.to>>p.a>>p.b>>p.c>>p.rev;
 for(int v=0;v<48;v++)for(int s=0;s<6;s++){auto&p=port[v][s];auto&r=port[p.to][p.rev];assert(r.to==v&&r.rev==s&&(p.a+r.a)%5==0&&(p.b+r.b)%5==0&&p.c+r.c==0);}
 uint32_t minimum=UINT_MAX;int minroot=-1,minq=-1,mindistinct=999;Witness witness[2];int moduli[2]={18,19};long long missing_total[2]={0,0};vector<array<long long,2>>root_missing;vector<int>root_minima;vector<int>root_min_distinct;
 ofstream counts(out+"/projected_word_counts.u32le.bin",ios::binary);
 long long totalwords=0;
 for(int root=0;root<48;root++){
  fill(begin(countq),end(countq),0);fill(begin(sums),end(sums),0);words=0;visit(root,0,0,0,-1,0);assert(words==117187);totalwords+=words;
  uint32_t localmin=*min_element(begin(countq),end(countq));root_minima.push_back(localmin);counts.write(reinterpret_cast<char*>(countq),sizeof(countq));
  array<long long,2>rm{};int localdistinct=999;
  for(int q=0;q<1200;q++){
   if(countq[q]<minimum){minimum=countq[q];minroot=root;minq=q;}
   vector<int>integers;for(int s=-56;s<=56;s++)if((sums[q]>>(s+56))&1)integers.push_back(s);
   localdistinct=min(localdistinct,(int)integers.size());mindistinct=min(mindistinct,(int)integers.size());
   for(int j=0;j<2;j++){
    int m=moduli[j];uint32_t residues=0;for(int s:integers)residues|=1U<<((s%m+m)%m);int miss=m-__builtin_popcount(residues);rm[j]+=miss;
    if(miss&&witness[j].root<0){int c=0;while((residues>>c)&1)c++;witness[j]={root,q,c,integers};}
   }
  }
  root_min_distinct.push_back(localdistinct);root_missing.push_back(rm);for(int j=0;j<2;j++)missing_total[j]+=rm[j];
 }
 ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\"COMPLETE_48_ROOT_PROJECTED_WORD_AND_SCALAR_IMAGES\",\"roots\":48,\"projected_states\":1200,\"words_per_root\":117187,\"total_words\":"<<totalwords<<",\"minimum_projected_word_count\":"<<minimum<<",\"minimum_root\":"<<minroot<<",\"minimum_q\":"<<minq<<",\"minimum_distinct_integer_scalar_sums\":"<<mindistinct<<",\"root_minimum_word_counts\":[";
 for(int r=0;r<48;r++){if(r)f<<',';f<<root_minima[r];}f<<"],\"root_minimum_distinct_integer_sums\":[";for(int r=0;r<48;r++){if(r)f<<',';f<<root_min_distinct[r];}f<<"],\"moduli\":[";
 for(int j=0;j<2;j++){
  if(j)f<<',';auto&w=witness[j];f<<"{\"m\":"<<moduli[j]<<",\"n\":"<<1200*moduli[j]<<",\"raw_capacity_allows\":"<<(minimum>=moduli[j]?"true":"false")<<",\"complete_R7_endpoint_certificate\":"<<(missing_total[j]==0?"true":"false")<<",\"sum_missing_targets_over_48_representatives\":"<<missing_total[j]<<",\"missing_targets_per_root\":[";
  for(int r=0;r<48;r++){if(r)f<<',';f<<root_missing[r][j];}f<<"],\"first_hole\":";
  if(w.root<0)f<<"null";else{f<<"{\"root_base\":"<<w.root<<",\"source_deck\":[0,0,0],\"target_base\":"<<w.q/25<<",\"a\":"<<w.q%5<<",\"b\":"<<w.q%25/5<<",\"missing_c\":"<<w.c<<",\"integer_scalar_endpoint_sums\":[";for(size_t i=0;i<w.integer_sums.size();i++){if(i)f<<',';f<<w.integer_sums[i];}f<<"]}";}f<<'}';
 }
 f<<"],\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"graph_generation\":false,\"BFS\":0,\"old_source_D7_rechecked\":false,\"ordinary_bad_unordered_pairs\":null,\"actual_global_D\":null}\n";
 cout<<"minraw="<<minimum<<" mininteger="<<mindistinct<<" m18miss="<<missing_total[0]<<" m19miss="<<missing_total[1]<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}

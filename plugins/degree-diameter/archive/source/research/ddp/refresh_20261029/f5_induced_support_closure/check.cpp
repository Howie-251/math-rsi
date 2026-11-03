#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;using U=uint32_t;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int main(int argc,char**argv){
 assert(argc==4);double start=cpu(),budget=stod(argv[3]);string input=argv[1],out=argv[2];
 rlimit lim{(rlim_t)ceil(budget),(rlim_t)ceil(budget+1)};setrlimit(RLIMIT_CPU,&lim);
 vector<pair<U,U>>rules;int u,a,b,v,count=0;ifstream f(input);
 while(f>>u>>a>>b>>v){rules.push_back({(1u<<u)|(1u<<v),(1u<<a)|(1u<<b)});count++;}
 assert(count==258);sort(rules.begin(),rules.end());rules.erase(unique(rules.begin(),rules.end()),rules.end());
 uint64_t closurecalls=0;auto close=[&](U q){closurecalls++;while(true){U old=q;for(auto[p,c]:rules)if((q&p)==p)q|=c;if(q==old)return q;}};
 const U ALL=(1u<<30)-1;U current=close(0),best=0,witness=0;int largest=0;uint64_t sets=0;array<uint64_t,31>hist{};bool complete=false;
 ofstream masks(out+"/CLOSED_SUPPORTS.u32le.bin",ios::binary);
 while(true){
  sets++;hist[__builtin_popcount(current)]++;masks.write((char*)&current,4);
  int size=__builtin_popcount(current);
  if(current!=ALL&&size>largest){largest=size;best=current;}
  if(current!=ALL&&size>=16&&!witness)witness=current;
  if(current==ALL){complete=true;break;}
  if(cpu()-start>budget-.05)break;
  bool found=false;
  for(int i=29;i>=0;i--)if(!(current>>i&1)){
   U prefix=(1u<<i)-1;U next=close((current&prefix)|(1u<<i));
   if((next&prefix)==(current&prefix)){current=next;found=true;break;}
  }
  assert(found);
 }
 ofstream r(out+"/NATIVE_RESULT.json");
 r<<setprecision(12)<<"{\"complete\":"<<(complete?"true":"false")<<",\"original_rules\":258,\"distinct_Horn_rules\":"<<rules.size()<<",\"closed_supports_visited\":"<<sets<<",\"closure_calls\":"<<closurecalls<<",\"largest_proper_size\":"<<largest<<",\"largest_proper_mask\":"<<best<<",\"counterexample_mask\":"<<witness<<",\"CPU_seconds\":"<<cpu()-start<<",\"cardinality_histogram\":[";
 for(int i=0;i<=30;i++){if(i)r<<',';r<<hist[i];}r<<"]}\n";
 cout<<"complete="<<complete<<" closed="<<sets<<" maxproper="<<largest<<" CPU="<<cpu()-start<<'\n';
}

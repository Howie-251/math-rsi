#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
int main(int argc,char**argv){
 const clock_t begin=clock();const double budget=stod(argv[4]);
 auto cpu=[&](){return double(clock()-begin)/CLOCKS_PER_SEC;};
 string prefix=argv[3];ifstream f(argv[1],ios::binary);uint32_t n,m2;
 f.read((char*)&n,4);f.read((char*)&m2,4);assert(n==186033&&m2==2021634);
 vector<uint32_t>off(n+1),adj(m2);f.read((char*)off.data(),4*(n+1));f.read((char*)adj.data(),4*m2);
 vector<int>missing;ifstream mf(argv[2]);for(int x;mf>>x;)missing.push_back(x);
 const int T=missing.size(),W=(T+63)/64;assert(T==4201);
 vector<int>mandatory={72425,85923,89934,95946,103392,107088,113094,120546,127006};
 vector<bool>isPin(n);for(int x:mandatory)isPin[x]=true;
 int steps=0,K=0,eligible=0,zero=0,pairtested=0;bool complete=false;vector<int>anchors;
 auto finish=[&](string status){
  ofstream o(prefix+"/EXACT_RESULT.json");
  o<<"{\"status\":\""<<status<<"\",\"source_n\":"<<n<<",\"source_m\":"<<m2/2
   <<",\"missing_targets\":"<<T<<",\"mask_words\":"<<W
   <<",\"completed_radius_steps\":"<<steps<<",\"eligible_guards\":"<<eligible
   <<",\"distinct_nonzero_masks\":"<<K<<",\"zero_cover_guards\":"<<zero
   <<",\"pair_first_masks_tested\":"<<pairtested
   <<",\"exact_complete\":"<<(complete?"true":"false")<<",\"guards\":[";
  for(size_t i=0;i<anchors.size();i++){if(i)o<<',';o<<anchors[i];}
  o<<"],\"native_CPU_seconds\":"<<cpu()<<"}\n";
  cout<<status<<" CPU "<<cpu()<<endl;
 };
 vector<U>cur(size_t(n)*W),next;
 for(int j=0;j<T;j++)cur[size_t(missing[j])*W+j/64]|=U(1)<<(j%64);
 for(int step=0;step<5;step++){
  next=cur;
  for(uint32_t u=0;u<n;u++){
   U*du=next.data()+size_t(u)*W;const U*su=cur.data()+size_t(u)*W;
   for(uint32_t k=off[u];k<off[u+1];k++){uint32_t v=adj[k];if(v<=u)continue;
    U*dv=next.data()+size_t(v)*W;const U*sv=cur.data()+size_t(v)*W;
    for(int w=0;w<W;w++){du[w]|=sv[w];dv[w]|=su[w];}
   }
   if((u&2047)==0&&cpu()>budget){finish("UNKNOWN_RADIUS_PROPAGATION_CPU_LIMIT");return 0;}
  }
  cur.swap(next);++steps;
  cout<<"radius_step "<<steps<<" CPU "<<cpu()<<endl;
 }
 vector<U>().swap(next);
 map<vector<U>,int>distinct;
 for(uint32_t u=0;u<n;u++)if(off[u+1]-off[u]<11&&!isPin[u]){
  ++eligible;vector<U>mask(cur.begin()+size_t(u)*W,cur.begin()+size_t(u+1)*W);
  if(all_of(mask.begin(),mask.end(),[](U x){return x==0;})){++zero;continue;}
  distinct.emplace(move(mask),u);
 }
 vector<U>().swap(cur);
 vector<pair<int,vector<U>>>rows;
 for(auto&kv:distinct)rows.emplace_back(kv.second,kv.first);
 distinct.clear();sort(rows.begin(),rows.end());K=rows.size();
 vector<U>full(W,~U(0));if(T%64)full.back()=(U(1)<<(T%64))-1;
 ofstream binary(prefix+"/guard_masks.u64le.bin",ios::binary),labels(prefix+"/guard_labels.txt");
 for(auto&r:rows){labels<<r.first<<'\n';binary.write((char*)r.second.data(),W*sizeof(U));}
 binary.close();labels.close();
 for(auto&r:rows)if(r.second==full){anchors={r.first};complete=true;finish("EXACT_ONE_GUARD_HIT");return 0;}
 if(cpu()>budget){finish("UNKNOWN_BEFORE_PAIR_DECISION_CPU_LIMIT");return 0;}
 const int KW=(K+63)/64;
 vector<U>coverers(size_t(T)*KW);
 vector<int>counts(T),order(T);iota(order.begin(),order.end(),0);
 for(int i=0;i<K;i++)for(int w=0;w<W;w++){
  U bits=rows[i].second[w];while(bits){
   int bit=__builtin_ctzll(bits),j=64*w+bit;
   coverers[size_t(j)*KW+i/64]|=U(1)<<(i%64);counts[j]++;bits&=bits-1;
  }
 }
 ofstream supports(prefix+"/TARGET_SUPPORTS.json");supports<<"{\"missing_targets\":[";
 for(int j=0;j<T;j++){if(j)supports<<',';supports<<missing[j];}
 supports<<"],\"distinct_mask_support_counts\":[";
 for(int j=0;j<T;j++){if(j)supports<<',';supports<<counts[j];}
 supports<<"]}\n";supports.close();
 if(find(counts.begin(),counts.end(),0)!=counts.end()){
  complete=true;finish("EXACT_NO_AT_MOST_TWO_GUARDS_ZERO_SUPPORT_TARGET");return 0;
 }
 sort(order.begin(),order.end(),[&](int a,int b){return counts[a]!=counts[b]?counts[a]<counts[b]:a<b;});
 vector<U>candidate(KW);
 for(int i=0;i<K;i++){
  ++pairtested;
  fill(candidate.begin(),candidate.end(),~U(0));
  if(K%64)candidate.back()=(U(1)<<(K%64))-1;
  for(int w=0;w<i/64;w++)candidate[w]=0;
  candidate[i/64]&=~((U(1)<<(i%64))-1);
  candidate[i/64]&=~(U(1)<<(i%64));
  bool any=false;
  for(int j:order)if(!(rows[i].second[j/64]>>(j%64)&1)){
   any=false;const U*c=coverers.data()+size_t(j)*KW;
   for(int w=0;w<KW;w++){candidate[w]&=c[w];any|=candidate[w]!=0;}
   if(!any)break;
  }
  if(any){
   int other=-1;for(int w=0;w<KW;w++)if(candidate[w]){other=64*w+__builtin_ctzll(candidate[w]);break;}
   assert(other>i&&other<K);anchors={rows[i].first,rows[other].first};
   complete=true;finish("EXACT_TWO_GUARD_HIT");return 0;
  }
  if((i&31)==0&&cpu()>budget){finish("UNKNOWN_PAIR_DECISION_CPU_LIMIT");return 0;}
 }
 complete=true;finish("EXACT_NO_AT_MOST_TWO_GUARDS");return 0;
}

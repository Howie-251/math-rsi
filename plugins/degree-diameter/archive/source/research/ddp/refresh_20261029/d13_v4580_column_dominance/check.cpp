#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using U=uint64_t;
int main(int argc,char**argv){
 assert(argc==5);const clock_t start=clock();int K=stoi(argv[2]),W=stoi(argv[3]),N=stoi(argv[4]);
 vector<U> rows(size_t(K)*W);ifstream in(argv[1],ios::binary);in.read(reinterpret_cast<char*>(rows.data()),rows.size()*sizeof(U));assert(size_t(in.gcount())==rows.size()*sizeof(U));
 vector<int> pop(K),order(K),retained,removed,witness(K,-1);iota(order.begin(),order.end(),0);
 for(int i=0;i<K;i++){for(int w=0;w<W;w++)pop[i]+=__builtin_popcountll(rows[size_t(i)*W+w]);assert(pop[i]>0);if(N%64)assert((rows[size_t(i)*W+W-1]>>(N%64))==0);}
 sort(order.begin(),order.end(),[&](int a,int b){return pop[a]!=pop[b]?pop[a]>pop[b]:a<b;});
 U comparisons=0,word_checks=0;size_t cursor=0;
 for(;cursor<order.size();cursor++){
  if(double(clock()-start)/CLOCKS_PER_SEC>3.6)break;
  const int c=order[cursor];int sup=-1;
  for(int r:retained){
   if(pop[r]<=pop[c])break;
   comparisons++;bool subset=true;
   for(int w=0;w<W;w++){word_checks++;if(rows[size_t(c)*W+w]&~rows[size_t(r)*W+w]){subset=false;break;}}
   if(subset){sup=r;break;}
  }
  if(sup<0)retained.push_back(c);else{removed.push_back(c);witness[c]=sup;}
 }
 vector<bool> still_retained(K);for(int r:retained)still_retained[r]=true;
 int checked=0;
 for(int c:removed){const int r=witness[c];assert(still_retained[r]&&pop[r]>pop[c]);for(int w=0;w<W;w++)assert((rows[size_t(c)*W+w]&~rows[size_t(r)*W+w])==0);checked++;}
 auto ids=[&](const char*key,const vector<int>&v){cout<<"\""<<key<<"\":[";for(size_t i=0;i<v.size();i++){if(i)cout<<",";cout<<v[i];}cout<<"]";};
 cout<<"{\"complete\":"<<(cursor==order.size()?"true":"false")<<",\"input_columns\":"<<K<<",\"target_count\":"<<N<<",\"processed_columns\":"<<cursor<<",\"retained_count\":"<<retained.size()<<",\"removed_count\":"<<removed.size()<<",";
 ids("retained_column_ids",retained);cout<<",";ids("removed_column_ids",removed);
 cout<<",\"drop_witnesses\":[";
 for(size_t i=0;i<removed.size();i++){if(i)cout<<",";int c=removed[i],r=witness[c];cout<<"{\"removed_column_id\":"<<c<<",\"retained_superset_column_id\":"<<r<<",\"removed_popcount\":"<<pop[c]<<",\"superset_popcount\":"<<pop[r]<<"}";}
 cout<<"],\"exact_witness_checks\":"<<checked<<",\"candidate_subset_comparisons\":"<<comparisons<<",\"word_subset_checks\":"<<word_checks<<",\"worker_cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
}

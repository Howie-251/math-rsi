#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
struct Arc{int v,code,voltage;};
using Flow=array<int16_t,5>;
int mod(int x){x%=23;return x<0?x+23:x;}
Flow canonical(const vector<int>& path){
 vector<int> s=path;sort(s.begin(),s.end(),[](int a,int b){return abs(a)<abs(b);});Flow out{};int k=0;
 for(int i=0;i<(int)s.size();){int id=abs(s[i]),c=0;while(i<(int)s.size()&&abs(s[i])==id){c+=(s[i]>0?1:-1);i++;}for(int j=0;j<abs(c);j++)out[k++]=c>0?id:-id;}return out;
}
int main(){
 auto start=chrono::steady_clock::now();int n,m;ifstream in("INPUT.txt");in>>n>>m;assert(n==240&&m==960);vector<vector<Arc>> g(n);vector<int> voltage(m);
 for(int e=0;e<m;e++){int u,v,t;in>>u>>v>>t;voltage[e]=t;g[u].push_back({v,e+1,t});g[v].push_back({u,-e-1,mod(-t)});}
 ofstream stats("PACKETS.tsv"),cache("ALL_PACKET_FLOWS.bin",ios::binary),offset("PACKET_CACHE_OFFSETS.tsv");stats<<"u\tv\tNB_paths\tdistinct_signed_flows\twitness_phases\tphase_mask\n";offset<<"packet\tu\tv\tbyte_offset\tdistinct_flows\n";
 int minimum=100000,mu=-1,mv=-1,nbmin=100000,below=0,fail=0,pass=0,pkt=0,diagmin=100000,diagmax=0,diagzero=0,diagpmfail=0;uint64_t totalflow=0,totalNB=0;map<int,int> phasedist;vector<int> path;bool first=false;int fu=-1,fv=-1,missing=-1,fphases=-1;uint32_t firstmask=0;vector<Flow> minpacket;
 for(int root=0;root<n;root++){
  vector<set<Flow>> fs(n);vector<int> nb(n);vector<uint32_t> phases(n);
  auto dfs=[&](auto&& self,int u,int prev,int depth,int phase)->void{
   if(u>=root){fs[u].insert(canonical(path));nb[u]++;phases[u]|=1u<<phase;}
   if(depth==5)return;
   for(const auto& a:g[u])if(a.v!=prev){path.push_back(a.code);self(self,a.v,u,depth+1,mod(phase+a.voltage));path.pop_back();}
  };dfs(dfs,root,-1,0,0);
  for(int v=root;v<n;v++){
   int sz=fs[v].size(),pc=__builtin_popcount(phases[v]);totalflow+=sz;totalNB+=nb[v];nbmin=min(nbmin,nb[v]);phasedist[pc]++;
   if(sz<minimum){minimum=sz;mu=root;mv=v;minpacket.assign(fs[v].begin(),fs[v].end());}
   if(sz<23)below++;
   if(pc==23)pass++;else{fail++;if(!first){first=true;fu=root;fv=v;fphases=pc;firstmask=phases[v];missing=0;while((phases[v]>>missing)&1u)missing++;}}
   if(v==root){diagmin=min(diagmin,sz);diagmax=max(diagmax,sz);Flow z{};diagzero+=fs[v].count(z);for(auto f:fs[v]){for(auto& x:f)x=-x;if(!fs[v].count(f))diagpmfail++;}}
   stats<<root<<'\t'<<v<<'\t'<<nb[v]<<'\t'<<sz<<'\t'<<pc<<'\t'<<phases[v]<<'\n';offset<<pkt<<'\t'<<root<<'\t'<<v<<'\t'<<cache.tellp()<<'\t'<<sz<<'\n';
   uint32_t count=sz;cache.write((char*)&count,sizeof count);for(const auto& f:fs[v])cache.write((char*)f.data(),sizeof(int16_t)*5);pkt++;
  }
 }
 ofstream minout("MINIMUM_PACKET_FLOWS.tsv");for(auto f:minpacket){for(int i=0;i<5;i++)minout<<f[i]<<(i==4?'\n':'\t');}
 ofstream out("NATIVE_RESULT.json");out<<"{\"unordered_packets\":"<<pkt<<",\"total_NB_paths_saved_direction\":"<<totalNB<<",\"total_distinct_signed_flows\":"<<totalflow<<",\"minimum_NB_paths\":"<<nbmin<<",\"minimum_distinct_signed_flows\":"<<minimum<<",\"minimum_pair\":["<<mu<<","<<mv<<"],\"packets_below23_distinctflows\":"<<below<<",\"allpair_flow_capacity_pass\":"<<(below==0?"true":"false")<<",\"witness_full23_packets\":"<<pass<<",\"witness_failing_packets\":"<<fail<<",\"first_witness_bad_pair\":["<<fu<<","<<fv<<"],\"first_witness_bad_phase\":"<<missing<<",\"first_witness_covered_phases\":"<<fphases<<",\"first_witness_phase_mask\":"<<firstmask<<",\"diagonal_min_distinct_flows\":"<<diagmin<<",\"diagonal_max_distinct_flows\":"<<diagmax<<",\"diagonal_zero_flow_packets\":"<<diagzero<<",\"diagonal_sign_pair_failures\":"<<diagpmfail<<",\"witness_phase_coverage_histogram\":{";
 bool sep=false;for(auto [p,c]:phasedist){if(sep)out<<',';sep=true;out<<'\"'<<p<<"\":"<<c;}out<<"},\"native_wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"}\n";
}

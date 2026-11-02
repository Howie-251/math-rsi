#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <random>
#include <vector>
using namespace std;using Flow=array<int16_t,5>;
struct Packet{int u,v,start,n;};
int mod(int x){x%=23;return x<0?x+23:x;}
int main(){
 auto t0=chrono::steady_clock::now();ifstream ci("CONSTRAINTS.txt");int n,r;ci>>n>>r;assert(n==960&&r==22);vector<int> piv(r);vector<bool> isp(n,false);for(auto& p:piv){ci>>p;isp[p]=true;}vector<int> rhs(r);vector<vector<int>> a(r,vector<int>(n));for(int i=0;i<r;i++){ci>>rhs[i];for(auto& x:a[i])ci>>x;}
 ifstream cache("../allpair_edgeflow_gate/ALL_PACKET_FLOWS.bin",ios::binary);vector<Packet> packets;vector<Flow> flows;flows.reserve(2699760);for(int u=0;u<240;u++)for(int v=u;v<240;v++){uint32_t count;cache.read((char*)&count,4);assert(cache&&count>=23);packets.push_back({u,v,(int)flows.size(),(int)count});size_t old=flows.size();flows.resize(old+count);cache.read((char*)(flows.data()+old),10*count);assert(cache);}
 assert(flows.size()==2699760);int critical=-1;for(int p=0;p<(int)packets.size();p++)if(packets[p].u==8&&packets[p].v==70)critical=p;assert(critical>=0);
 ofstream stats("SAMPLES.tsv"),allvol("ALL_VOLTAGES.tsv");stats<<"sample\tfull_packets\tmissing_phase_obligations\tdiagonal_full\tcross_full\tcritical_full\tfirst_bad_u\tfirst_bad_v\tfirst_missing_phase\tnonzero_edges\n";
 mt19937 rng(20261102);uniform_int_distribution<int> val(0,22);vector<int> best,hitvol;vector<uint32_t> bm;int bestmiss=10000000,besti=-1,bestfull=-1,bestdiag=-1,joint=0,actual=0;bool hit=false;
 for(int sample=0;sample<32;sample++){
  vector<int> theta(n);for(int e=0;e<n;e++)if(!isp[e])theta[e]=val(rng);
  for(int i=0;i<r;i++){int z=rhs[i];for(int e=0;e<n;e++)if(!isp[e])z-=a[i][e]*theta[e];theta[piv[i]]=mod(z);}
  for(int i=0;i<r;i++){int z=0;for(int e=0;e<n;e++)z+=a[i][e]*theta[e];assert(mod(z)==rhs[i]);}
  vector<uint32_t> masks(packets.size());int full=0,missing=0,diagfull=0,crossfull=0,fu=-1,fv=-1,fp=-1;
  for(int p=0;p<(int)packets.size();p++){
   const auto& x=packets[p];uint32_t mask=0;for(int j=x.start;j<x.start+x.n;j++){int phase=0;for(auto code:flows[j])if(code)phase+=(code>0?theta[code-1]:-theta[-code-1]);mask|=1u<<mod(phase);if(mask==((1u<<23)-1))break;}
   masks[p]=mask;int covered=__builtin_popcount(mask);missing+=23-covered;
   if(covered==23){full++;if(x.u==x.v)diagfull++;else crossfull++;}else if(fu<0){fu=x.u;fv=x.v;fp=0;while((mask>>fp)&1u)fp++;}
  }
  assert(masks[critical]==((1u<<23)-1));if(masks[0]==((1u<<23)-1))joint++;actual++;
  int nonzero=count_if(theta.begin(),theta.end(),[](int x){return x!=0;});stats<<sample<<'\t'<<full<<'\t'<<missing<<'\t'<<diagfull<<'\t'<<crossfull<<"\t1\t"<<fu<<'\t'<<fv<<'\t'<<fp<<'\t'<<nonzero<<'\n';allvol<<sample;for(int t:theta)allvol<<'\t'<<t;allvol<<'\n';
  if(missing<bestmiss){bestmiss=missing;besti=sample;best=theta;bm=masks;bestfull=full;bestdiag=diagfull;}
  if(!missing){hit=true;hitvol=theta;break;}
 }
 ofstream bv("BEST_VOLTAGE_VALUES.txt");for(int t:best)bv<<t<<'\n';ofstream bstats("BEST_PACKET_PHASES.tsv");bstats<<"u\tv\tdistinct_flow_and_NB_count\tcovered_phases\tphase_mask\n";map<int,array<int,4>> bynb;int bestmin=23;array<int,24> hist{};
 for(int p=0;p<(int)packets.size();p++){const auto& x=packets[p];int k=__builtin_popcount(bm[p]);bestmin=min(bestmin,k);hist[k]++;bstats<<x.u<<'\t'<<x.v<<'\t'<<x.n<<'\t'<<k<<'\t'<<bm[p]<<'\n';auto& z=bynb[x.n];z[0]++;z[1]+=(k==23);z[2]+=23-k;z[3]+=(x.u==x.v);}
 ofstream cls("BEST_BY_NB_COUNT.tsv");cls<<"NB_count\tpackets\tfull23\tmissing_phase_obligations\tdiagonal_packets\n";for(auto [nb,z]:bynb)cls<<nb<<'\t'<<z[0]<<'\t'<<z[1]<<'\t'<<z[2]<<'\t'<<z[3]<<'\n';
 ofstream result("NATIVE_RESULT.json");result<<"{\"samples\":"<<actual<<",\"critical_packet_preserved_all\":true,\"joint_critical_and_first_diagonal_full_samples\":"<<joint<<",\"full_D5_hit\":"<<(hit?"true":"false")<<",\"best_sample\":"<<besti<<",\"best_full_packets\":"<<bestfull<<",\"best_missing_phase_obligations\":"<<bestmiss<<",\"best_diagonal_full\":"<<bestdiag<<",\"best_minimum_phase_coverage\":"<<bestmin<<",\"unordered_packets\":"<<packets.size()<<",\"best_phase_coverage_histogram\":{";bool sep=false;for(int i=0;i<24;i++)if(hist[i]){if(sep)result<<',';sep=true;result<<'\"'<<i<<"\":"<<hist[i];}result<<"},\"native_wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"}\n";
}

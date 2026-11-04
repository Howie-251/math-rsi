// Independent subset-DP domain counts and direct32-vertex positive certificate audit.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;using U=uint64_t;
void req(bool b,string why){if(!b)throw runtime_error(why);}int pc(U x){return __builtin_popcountll(x);}U bit(int x){return U(1)<<x;}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int a){while(p[a]!=a){p[a]=p[p[a]];a=p[a];}return a;}bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}};
vector<unsigned char> read(string file){ifstream f(file,ios::binary|ios::ate);req(bool(f),"open "+file);size_t n=f.tellg();vector<unsigned char>b(n);f.seekg(0);if(n)f.read((char*)b.data(),n);req(bool(f),"read "+file);return b;}
int main(int argc,char**argv){try{req(argc==2,"args");string dir=argv[1];vector<int>E,O;int ei[32],oi[32];fill(ei,ei+32,-1);fill(oi,oi+32,-1);U G=0,even=0,units=0;for(int x=0;x<32;x++){if(pc(x)%2==0)even|=bit(x);if(pc(x)==1)units|=bit(x);if(x&&pc(x)%2==0){ei[x]=E.size();E.push_back(x);G|=bit(x);}else if(pc(x)>=3&&pc(x)%2){oi[x]=O.size();O.push_back(x);G|=bit(x);}}
 req(E.size()==15&&O.size()==11,"G populations");array<array<int,5>,6> Ts{{{7,11,13,19,21},{7,11,13,19,31},{7,11,13,22,31},{7,11,19,28,31},{7,11,21,25,31},{7,11,21,26,31}}};
 array<U,6>Tvertices{},Tbits{};for(int k=0;k<6;k++)for(int x:Ts[k]){Tvertices[k]|=bit(x);Tbits[k]|=bit(oi[x]);}
 int neighbors[11]={};U actualN[32]={};for(int j=0;j<11;j++)for(int i=0;i<15;i++)if(pc(O[j]^E[i])==1){neighbors[j]|=1<<i;actualN[O[j]]|=bit(E[i]);}
 // Independently partition by the exact unmatched-odd subset, then count all
 // short injective partners using the used-even mask as the only DP state.
 array<array<U,12>,6> dpcounts{};int evaluatedU=0,prunedU=0;vector<U>dp(1<<15),next(1<<15);
 for(int unmatched=0;unmatched<(1<<11);unmatched++){
  bool relevant=false;for(int k=0;k<6;k++)if(!(U(unmatched)&Tbits[k]))relevant=true;if(!relevant)continue;
  int required=0;for(int j=0;j<11;j++)if(unmatched>>j&1)required|=neighbors[j];int m=11-__builtin_popcount(unsigned(unmatched));if(__builtin_popcount(unsigned(required))>m){prunedU++;continue;}
  fill(dp.begin(),dp.end(),0);dp[0]=1;
  for(int j=0;j<11;j++)if(!(unmatched>>j&1)){
   fill(next.begin(),next.end(),0);for(int mask=0;mask<(1<<15);mask++)if(dp[mask]){int available=neighbors[j]&~mask;while(available){int b=available&-available;available-=b;next[mask|b]+=dp[mask];}}dp.swap(next);
  }
  U count=0;for(int mask=0;mask<(1<<15);mask++)if((mask&required)==required)count+=dp[mask];
  for(int k=0;k<6;k++)if(!(U(unmatched)&Tbits[k]))dpcounts[k][m]+=count;evaluatedU++;
 }
 array<array<int,32>,120>maps;array<int,5>perm{0,1,2,3,4};int pn=0;do{for(int x=0;x<32;x++){maps[pn][x]=0;for(int d=0;d<5;d++)maps[pn][x]|=((x>>perm[d])&1)<<d;}pn++;}while(next_permutation(perm.begin(),perm.end()));req(pn==120,"maps");
 array<vector<unsigned char>,2>forests;int seeds[2][3]={{3,4,7},{15,1,7}};U sourceForests=0;
 for(int c=0;c<2;c++){string nn=dir+"/TWELVE_ROOT_STAR_OPENING_case_"+(c==0?string("00"):string("03"))+"_forests.bin";forests[c]=read(nn);req(forests[c].size()==8031*32,"source forest length");for(int i=0;i<8031;i++){DS ds;int deg[32]={};bool open=false;for(int j=0;j<32;j+=2){int a=forests[c][i*32+j],b=forests[c][i*32+j+1];req(a<32&&b<32&&a!=b&&pc(a^b)==1,"source forest edge");deg[a]++;deg[b]++;req(ds.join(a,b),"source forest labelcycle");if((a==seeds[c][0]&&b==7)||(b==seeds[c][0]&&a==7))open=true;}
   for(int x=0;x<32;x++)req(deg[x]==((x==0||x==31)?0:(x==seeds[c][0]||x==seeds[c][1])?2:1),"source forest degree");req(open,"source opening edge");sourceForests++;}}
 cout<<"{\"status\":\"PASS\",\"independent_domain_method\":\"unmatched_odd_subset_and_used_even_injection_DP\",\"DP_unmatched_subsets_evaluated\":"<<evaluatedU<<",\"DP_subsets_pruned_by_necessary_neighborhood_size\":"<<prunedU<<",\"source_forests_verified\":"<<sourceForests<<",\"reports\":[";
 U total=0,totalInternal=0,totalCross=0;bool comma=false;
 for(int k=0;k<6;k++){
  auto opbytes=read(dir+"/TWELVE_STAR_MAXIMAL_A_options_"+to_string(k)+".bin");req(opbytes.size()%6==0,"options align");unordered_set<U>options;for(size_t j=0;j<opbytes.size();j+=6){U key=0;for(int t=0;t<6;t++)key|=U(opbytes[j+t])<<(8*t);req(options.insert(key).second,"duplicate options");}
  auto cert=read(dir+"/TWELVE_STAR_MAXIMAL_A_full_"+to_string(k)+"_certificates.bin");req(cert.size()%32==0,"certificate alignment");vector<U>codes;codes.reserve(cert.size()/32);array<U,12>counts{};U internal=0,cross=0;
  for(size_t at=0;at<cert.size();at+=32){const auto*r=cert.data()+at;int m=r[22],q=r[23],t=r[24],w=r[25],b=r[26],cas=r[27],row=int(r[28])+(int(r[29])<<8),pi=r[30];req(m>=9&&m<=11&&q<32&&t<32&&w<32&&b<32&&(cas==0||cas==3)&&row<8031&&pi<120,"certificate header");
   U optionKey=U(q)|(U(t)<<8)|(U(w)<<16)|(U(b)<<24)|(U(cas)<<32)|(U(pi)<<40);req(options.count(optionKey),"selected option not independently bound to accepted B");
   U used=0,code=0;int hv=-1,last=-1;vector<pair<int,int>>original;for(int j=0;j<2*m;j+=2){int a=r[j],z=r[j+1];req(a<z&&z<32&&pc(a^z)==1&&int(a*32+z)>last,"sorted original short edges");last=a*32+z;req((G&bit(a))&&(G&bit(z))&&!(used&bit(a))&&!(used&bit(z)),"legal original matching");used|=bit(a)|bit(z);int odd=(pc(a)%2)?a:z,ev=(odd==a)?z:a;req(oi[odd]>=0&&ei[ev]>=0,"original parity");code|=U(ei[ev]+1)<<(4*oi[odd]);original.push_back({a,z});if(a==31)hv=z;if(z==31)hv=a;}
   for(int j=2*m;j<22;j++)req(r[j]==255,"original padding");req((used&Tvertices[k])==Tvertices[k],"mandatory T not covered");for(int x:O)if(!(used&bit(x)))req(!(actualN[x]&~used),"matching not inclusion maximal");req(!(used&bit(q))&&ei[q]>=0,"q not unmatched even G vertex");req((Tvertices[k]&bit(t))&&t!=31&&pc(q^t)==1&&(used&bit(t)),"t not covered mandatory opening source");req(w!=b&&(units&bit(w))&&(units&bit(b)),"unit roles");req(r[31]==int(hv>=0),"target internal flag");
   int fc=cas==0?0:1;req(maps[pi][seeds[fc][0]]==q&&maps[pi][seeds[fc][1]]==b&&maps[pi][7]==t,"actual forest role map");
   DS ds;for(int j=0;j<32;j+=2){int a=maps[pi][forests[fc][row*32+j]],z=maps[pi][forests[fc][row*32+j+1]];req(ds.join(a,z),"mapped source cycle");}
   U LAused=0;for(auto[a,z]:original){if(a==31)a=w;else if(z==31)z=w;req(a!=0&&a!=31&&z!=0&&z!=31&&pc(a)%2!=pc(z)%2&&!(LAused&bit(a))&&!(LAused&bit(z)),"modified LA matching");LAused|=bit(a)|bit(z);req(ds.join(a,z),"S plus LA labelled cycle");}
   U retained=((bit(32)-1)&~bit(0)&~bit(31));U Kopen=retained&~bit(q)&~bit(b);req(!(LAused&~Kopen)&&pc(LAused)==2*m,"modified support");U Q=Kopen&~LAused;req(pc(Q&even)==14-m&&pc(Q&~even)==14-m&&14-m>=3,"balanced completion endpoint populations");U X=G&~used;U Xprime=hv>=0?X:((X&~bit(31))|bit(w));U expected=(Xprime&~bit(q))|(units&~bit(w)&~bit(b));req(Q==expected&&!(Q&bit(t)),"exact actual completion domain");req(ds.root(q)==ds.root(t),"opening edge component");
   codes.push_back(code);counts[m]++;if(hv>=0)internal++;else cross++;
  }
  sort(codes.begin(),codes.end());req(adjacent_find(codes.begin(),codes.end())==codes.end(),"duplicate original matching certificate");for(int m=0;m<=11;m++)req(counts[m]==dpcounts[k][m],"independent full-domain cardinality mismatch");
  if(comma)cout<<',';comma=true;cout<<"{\"index\":"<<k<<",\"unique_legal_maximal_T_covered_matchings\":"<<codes.size()<<",\"independent_DP_count\":"<<codes.size()<<",\"edge_count_histogram\":{\"9\":"<<counts[9]<<",\"10\":"<<counts[10]<<",\"11\":"<<counts[11]<<"},\"positive_witnesses_verified\":"<<codes.size()<<",\"target_internal\":"<<internal<<",\"target_crossing\":"<<cross<<",\"all_direct32_vertex_labelled_DSU_checks_pass\":true,\"exact_endpoint_domains_and_B_options_verified\":true}";
  total+=codes.size();totalInternal+=internal;totalCross+=cross;
 }
 req(total==3620052,"total domain");cout<<"],\"all_certificates_verified\":"<<total<<",\"target_internal_certificates\":"<<totalInternal<<",\"target_crossing_certificates\":"<<totalCross<<",\"coverage_complete_by_independent_DP_plus_legal_unique_equal_cardinality\":true,\"finite_A_premise_proved\":true,\"full_twelve_hole_proved\":false,\"full_P6_proved\":false}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}

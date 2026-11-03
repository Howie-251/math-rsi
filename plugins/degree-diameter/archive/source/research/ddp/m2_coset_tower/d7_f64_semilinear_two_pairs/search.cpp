#include "engine.hpp"
constexpr long long PAIR_CHOICES=1300LL*1299/2,TYPE_I_TOTAL=40*PAIR_CHOICES;
constexpr long long INV_CHOICES=45LL*44/2,TYPE_II_PER=INV_CHOICES*1299;
constexpr long long TOTAL=TYPE_I_TOTAL+6*TYPE_II_PER,HH_TOTAL=38982510;
const array<array<int,2>,6>FIRST_PAIR={{{1,0},{1,1},{3,0},{3,1},{7,0},{7,1}}};
volatile sig_atomic_t stopped=0;void stop_signal(int){stopped=1;}
struct Scope{
 vector<int>involutions,otherInv;array<int,2>firstInv={1,1345};array<vector<vector<int>>,2>orbits;
 Scope(Engine&e){
  for(int g=1;g<Engine::L;g++)if(e.inverse[g]==g){involutions.push_back(g);if(__builtin_popcountll(e.km[g%64])!=21)otherInv.push_back(g);}
  if(involutions.size()!=87||otherInv.size()!=45)throw runtime_error("wrong involution scope");
  auto frob2=[&](int g){return int(e.mul[g%64][g%64])+64*((2*((g/64)%21))%21+21*(g/1344));};
  for(int z=0;z<2;z++){
   set<int>todo(involutions.begin(),involutions.end());if(frob2(firstInv[z])!=firstInv[z])throw runtime_error("first invol not Frobenius fixed");todo.erase(firstInv[z]);
   while(!todo.empty()){int g=*todo.begin(),u=g;vector<int>orbit;do{if(!todo.erase(u))throw runtime_error("broken involution orbit");orbit.push_back(u);u=frob2(u);}while(u!=g);sort(orbit.begin(),orbit.end());orbits[z].push_back(orbit);}
   int bc=0;for(auto&orb:orbits[z])bc+=(__builtin_popcountll(e.km[orb[0]%64])==42);
   if(orbits[z].size()!=20||bc!=7)throw runtime_error("wrong second-involution orbit count");
  }
 }
 void dump(string file,Engine&e){ofstream f(file);f<<"{\"encoding\":\"x+64*(a+21e)\",\"involution_codes\":[";
  for(size_t j=0;j<involutions.size();j++)f<<(j?",":"")<<involutions[j];f<<"],\"inverse_pair_representative_codes\":[";
  for(size_t j=0;j<e.pairs.size();j++)f<<(j?",":"")<<e.pairs[j];f<<"],\"type_i\":[";
  for(int z=0;z<2;z++){f<<(z?",":"")<<"{\"first_code\":"<<firstInv[z]<<",\"orbits\":[";for(int j=0;j<20;j++){auto&orb=orbits[z][j];f<<(j?",":"")<<"{\"representative_code\":"<<orb[0]<<",\"member_codes\":[";for(size_t k=0;k<orb.size();k++)f<<(k?",":"")<<orb[k];f<<"]}";}f<<"]}";}
  f<<"],\"type_ii_involution_codes\":[";for(size_t j=0;j<otherInv.size();j++)f<<(j?",":"")<<otherInv[j];f<<"],\"type_i_total\":"<<TYPE_I_TOTAL<<",\"type_ii_total\":"<<6*TYPE_II_PER<<",\"raw_total\":"<<TOTAL<<",\"HH_total\":"<<HH_TOTAL<<"}\n";
 }
};
void cursor_parameters(ostream&f,long long cursor){
 if(cursor>=TOTAL){f<<"null";return;}
 if(cursor<TYPE_I_TOTAL){long long branch=cursor/PAIR_CHOICES,rem=cursor%PAIR_CHOICES;int j=0;while(rem>=1299-j){rem-=1299-j;j++;}
  f<<"{\"type\":\"I\",\"first_involution_index\":"<<branch/20<<",\"second_involution_orbit_index\":"<<branch%20<<",\"pair_j\":"<<j<<",\"pair_k\":"<<j+1+rem<<"}";
 }else{long long off=cursor-TYPE_I_TOTAL,branch=off/TYPE_II_PER,rem=off%TYPE_II_PER,invpair=rem/1299;int j=0;while(invpair>=44-j){invpair-=44-j;j++;}
  f<<"{\"type\":\"II\",\"first_pair_branch\":"<<branch<<",\"involution_j\":"<<j<<",\"involution_k\":"<<j+1+invpair<<",\"other_pair_index_in_1299_list\":"<<rem%1299<<"}";
 }
}
struct Counts{long long raw=0,invalid=0,hh=0,bb=0,scored=0,hbzero=0;int minBB=449;long long best=numeric_limits<long long>::max();array<int,3>minRoot={3201,3201,3201};array<long long,3>zeroRoot{};};
int main(int argc,char**argv){try{
 clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};Engine e;Scope scope(e);
 auto make=[&](int i,int j,int a,int b)->Labels{return {i,j,a,e.inverse[a],b,e.inverse[b]};};
 if(argc==3&&string(argv[1])=="prepare"){
  string directory=argv[2];scope.dump(directory+"/generated_scope.json",e);auto S=make(1345,2,1539,64);
  if(!e.legal(S))throw runtime_error("illegal involution preflight");e.save(directory+"/preflight",S,-1,-1,{-1,-1},true);cout<<"prepared scope and one graph cpu "<<cpu()<<endl;return 0;
 }
 if(argc==9&&string(argv[1])=="check"){
  Labels S;for(int j=0;j<6;j++)S[j]=stoi(argv[j+2]);if(!e.legal(S))throw runtime_error("illegal saved generators");e.save(argv[8],S,-1,-1,{-1,-1},true);cout<<"saved graph scored cpu "<<cpu()<<endl;return 0;
 }
 if(argc!=5)throw runtime_error("CPU_LIMIT HH_PROFILE_TARGET START_CURSOR PREFIX");double limit=stod(argv[1]);long long target=stoll(argv[2]),first=stoll(argv[3]);string prefix=argv[4];
 signal(SIGINT,stop_signal);signal(SIGTERM,stop_signal);scope.dump(prefix+".scope.json",e);
 array<Counts,46>counts;map<int,long long>bbhist;map<long long,long long>scorehist;
 long long cursor=0,next=first,raw=0,invalid=0,hh=0,bb=0,minCursor=-1,bestCursor=-1;int minBB=449,minBranch=-1,bestBranch=-1;long long best=numeric_limits<long long>::max();
 Labels minS{},bestS{};array<int,2>minPairs{},bestPairs{};double hhCPU=0,bbCPU=0,bfsCPU=0;bool done=false,found=false;double setup=cpu();
 long long nextMilestone=first<1000000?1000000:(first/5000000+1)*5000000;
 auto process=[&](const Labels&S,int branch,array<int,2>pair_indices){
  if(cursor<first){cursor++;return;}
  if(next>=nextMilestone){
   double used=cpu(),loop=used-setup,overhead=max(0.0,loop-hhCPU-bbCPU-bfsCPU);
   string report=prefix+(nextMilestone==1000000?".first_million.json":".progress.json");ofstream progress(report);
   progress<<"{\"global_next_cursor\":"<<next<<",\"start_cursor\":"<<first<<",\"raw_visited_this_process\":"<<raw<<",\"HH_pass_this_process\":"<<hh<<",\"BB_pass_this_process\":"<<bb<<",\"cpu_seconds\":"<<used<<",\"HH_filter_cpu_seconds\":"<<hhCPU<<",\"BB_formula_cpu_seconds\":"<<bbCPU<<",\"three_root_BFS_cpu_seconds\":"<<bfsCPU<<",\"raw_and_timing_overhead_cpu_seconds\":"<<overhead<<",\"minimum_BB_missing\":"<<minBB<<",\"best_scored_bad_pairs\":"<<(bestCursor>=0?to_string(best):"null")<<"}\n";
   cout<<"progress cursor "<<next<<" raw_this_process "<<raw<<" HH "<<hh<<" BB "<<bb<<" cpu "<<used<<" stages_HH_BB_BFS_overhead "<<hhCPU<<" "<<bbCPU<<" "<<bfsCPU<<" "<<overhead<<endl;
   nextMilestone=nextMilestone==1000000?5000000:nextMilestone+5000000;
  }
  if(stopped||cpu()>=limit){done=true;return;}
  long long current=cursor++;next=cursor;auto&ct=counts[branch];ct.raw++;raw++;
  if(!e.legal(S)){ct.invalid++;invalid++;return;}
  clock_t t=clock();bool hp=e.hh(S);hhCPU+=double(clock()-t)/CLOCKS_PER_SEC;if(!hp)return;hh++;ct.hh++;
  t=clock();auto masks=e.bb(S);int miss=e.missing(masks);bbCPU+=double(clock()-t)/CLOCKS_PER_SEC;bbhist[miss]++;ct.minBB=min(ct.minBB,miss);
  if(miss<minBB){minBB=miss;minS=S;minBranch=branch;minPairs=pair_indices;minCursor=current;}
  if(miss==0){bb++;ct.bb++;t=clock();e.build(S);auto m=e.roots();long long bad=e.bad(m);ct.scored++;ct.best=min(ct.best,bad);scorehist[bad]++;
   for(int z=0;z<3;z++){ct.minRoot[z]=min(ct.minRoot[z],m[z]);ct.zeroRoot[z]+=(m[z]==0);}ct.hbzero+=(m[1]==0&&m[2]==0);
   if(bad<best){best=bad;bestS=S;bestBranch=branch;bestPairs=pair_indices;bestCursor=current;}
   bfsCPU+=double(clock()-t)/CLOCKS_PER_SEC;
   if(!bad){found=true;done=true;return;}
  }
  if(hh==target)done=true;
 };
 for(int firstIndex=0;firstIndex<2&&!done;firstIndex++)for(int orbit=0;orbit<20&&!done;orbit++){
  int i=scope.firstInv[firstIndex],j=scope.orbits[firstIndex][orbit][0],branch=20*firstIndex+orbit;
  for(int a=0;a<1300&&!done;a++)for(int b=a+1;b<1300&&!done;b++)process(make(i,j,e.pairs[a],e.pairs[b]),branch,{a,b});
 }
 for(int branch=0;branch<6&&!done;branch++){
  int a=1+64*(FIRST_PAIR[branch][0]+21*FIRST_PAIR[branch][1]),canonical=min(a,e.inverse[a]),fixedIndex=-1;vector<int>remaining;
  for(int k=0;k<1300;k++)if(e.pairs[k]==canonical)fixedIndex=k;else remaining.push_back(k);
  if(fixedIndex<0||remaining.size()!=1299)throw runtime_error("missing fixed A pair");
  for(int i=0;i<45&&!done;i++)for(int j=i+1;j<45&&!done;j++)for(int b=0;b<1299&&!done;b++)
   process(make(scope.otherInv[i],scope.otherInv[j],a,e.pairs[remaining[b]]),40+branch,{fixedIndex,remaining[b]});
 }
 double loop=cpu()-setup,rawOverhead=max(0.0,loop-hhCPU-bbCPU-bfsCPU),estimate=setup+TOTAL*(hhCPU+rawOverhead)/max(1LL,raw)+HH_TOTAL*bbCPU/max(1LL,hh);
 if(minCursor>=0)e.save(prefix+".best_BB",minS,minCursor,minBranch,minPairs,false);
 if(bestCursor>=0)e.save(prefix+".best",bestS,bestCursor,bestBranch,bestPairs,true);
 string status=found?"CANDIDATE_D5":hh==target?"PROFILE_COMPLETE_STOPPED":next==TOTAL?"COMPLETE_NO_SOLUTION":stopped?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 ofstream f(prefix+".terminal.json");f<<"{\"status\":\""<<status<<"\",\"raw_total\":"<<TOTAL<<",\"HH_total_from_scope\":"<<HH_TOTAL<<",\"start_cursor\":"<<first<<",\"next_candidate_cursor\":"<<next<<",\"raw_visited\":"<<raw<<",\"invalid\":"<<invalid<<",\"HH_pass\":"<<hh<<",\"HH_skipped\":"<<raw-invalid-hh<<",\"BB_pass\":"<<bb<<",\"three_root_BFS_scored\":"<<bb<<",\"minimum_BB_missing\":"<<minBB<<",\"best_bad_pairs\":"<<(bestCursor>=0?to_string(best):"null")<<",\"setup_cpu_seconds\":"<<setup<<",\"loop_cpu_seconds\":"<<loop<<",\"HH_filter_cpu_seconds\":"<<hhCPU<<",\"BB_formula_cpu_seconds\":"<<bbCPU<<",\"conditional_three_root_BFS_cpu_seconds\":"<<bfsCPU<<",\"raw_timing_and_loop_overhead_cpu_seconds\":"<<rawOverhead<<",\"estimated_full_HH_BB_cpu_seconds\":"<<estimate<<",\"estimated_full_BFS_cpu_using_prefix_rate\":"<<HH_TOTAL*bfsCPU/max(1LL,hh)<<",\"cpu_seconds\":"<<cpu()<<",\"per_branch\":[";
 for(int b=0;b<46;b++){auto&ct=counts[b];f<<(b?",":"")<<"{\"branch\":"<<b<<",\"type\":\""<<(b<40?"I":"II")<<"\",\"raw_total\":"<<(b<40?PAIR_CHOICES:TYPE_II_PER)<<",\"raw_visited\":"<<ct.raw<<",\"invalid\":"<<ct.invalid<<",\"HH_pass\":"<<ct.hh<<",\"HH_skipped\":"<<ct.raw-ct.invalid-ct.hh<<",\"BB_pass\":"<<ct.bb<<",\"three_root_BFS_scored\":"<<ct.scored<<",\"minimum_BB_missing\":"<<(ct.hh?to_string(ct.minBB):"null")<<",\"best_bad_pairs\":"<<(ct.scored?to_string(ct.best):"null")<<",\"minimum_root_missing\":[";
  for(int z=0;z<3;z++)f<<(z?",":"")<<(ct.scored?to_string(ct.minRoot[z]):"null");f<<"],\"root_zero_counts\":[";for(int z=0;z<3;z++)f<<(z?",":"")<<ct.zeroRoot[z];f<<"],\"head_block_zero\":"<<ct.hbzero<<"}";
 }f<<"],\"BB_missing_histogram\":{";bool comma=false;for(auto[k,v]:bbhist){f<<(comma?",":"")<<"\""<<k<<"\":"<<v;comma=true;}f<<"},\"score_histogram\":{";comma=false;for(auto[k,v]:scorehist){f<<(comma?",":"")<<"\""<<k<<"\":"<<v;comma=true;}f<<"},\"next_parameters\":";cursor_parameters(f,next);f<<"}\n";
 cout<<"terminal "<<status<<" raw "<<raw<<" HH "<<hh<<" BB "<<bb<<" minBB "<<minBB<<" next "<<next<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<endl;return 2;}}

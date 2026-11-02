#include <algorithm>
#include <array>
#include <chrono>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using U=unsigned short;
volatile sig_atomic_t stopped=0;
void stop_signal(int){stopped=1;}

struct Engine{
 int q,r,L,n;vector<int>power,inv;vector<U>right,queue;vector<array<U,5>>adj;
 vector<unsigned>seen;unsigned stamp=0;
 Engine(int Q,int R):q(Q),r(R),L(20*q),n(26*q),power(20),inv(L),right(L*L),queue(n),adj(n),seen(n){
  power[0]=1;for(int i=1;i<20;i++)power[i]=power[i-1]*r%q;
  if(power[19]*r%q!=1||power[10]!=q-1||n>65535)throw runtime_error("unsupported group");
  for(int s=0;s<L;s++)for(int g=0;g<L;g++)right[s*L+g]=(g%q+power[g/q]*(s%q))%q+q*((g/q+s/q)%20);
  for(int g=0;g<L;g++){int j=(20-g/q)%20;inv[g]=((q-power[j]*(g%q)%q)%q)+q*j;}
  for(int i=0;i<20;i++)for(int x=0;x<q;x++)adj[x+q*i][0]=20*q+x+q*(i%5);
  for(int j=0;j<5;j++)for(int x=0;x<q;x++)adj[20*q+x+q*j]={(U)(x+q*j),(U)(x+q*(j+5)),(U)(x+q*(j+10)),(U)(x+q*(j+15)),(U)(25*q+x)};
  for(int x=0;x<q;x++)for(int j=0;j<5;j++)adj[25*q+x][j]=20*q+x+q*j;
 }
 bool legal(const array<int,4>&S){set<int>s;for(int g:S){if(g<=0||g>=L)return false;s.insert(g);}if(s.size()!=4)return false;for(int g:S)if(!s.count(inv[g]))return false;return true;}
 void build(const array<int,4>&S){for(int j=0;j<4;j++){const U*t=&right[S[j]*L];for(int g=0;g<L;g++)adj[g][j+1]=t[g];}}
 array<int,3>missing(){array<int,3>answer{};array<int,3>roots={0,20*q,25*q};
  for(int side=0;side<3;side++){++stamp;int head=0,end=1;queue[0]=roots[side];seen[roots[side]]=stamp;
   for(int depth=0;depth<5&&head<end&&end<n;depth++){int boundary=end;while(head<boundary){int u=queue[head++];for(U v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}}}
   answer[side]=n-end;
  }return answer;
 }
 long long bad(const array<int,3>&a){long long twice=1LL*20*q*a[0]+1LL*5*q*a[1]+1LL*q*a[2];if(twice%2)throw runtime_error("odd weighted ordered pair count");return twice/2;}
 void save(string prefix,const array<int,4>&S,const array<int,3>&miss,string type,int first,int second,long long cursor,double cpu){
  vector<pair<int,int>>edges;for(int u=0;u<n;u++)for(int v:adj[u])if(u<v)edges.emplace_back(u,v);sort(edges.begin(),edges.end());
  if((int)edges.size()!=5*n/2||adjacent_find(edges.begin(),edges.end())!=edges.end())throw runtime_error("invalid complete edge list");
  ofstream e(prefix+".edges");e<<n<<" "<<edges.size()<<"\n";for(auto[u,v]:edges)e<<u<<" "<<v<<"\n";
  ofstream f(prefix+".json");f<<"{\"q\":"<<q<<",\"r\":"<<r<<",\"n\":"<<n<<",\"type\":\""<<type<<"\",\"first_parameter\":"<<first<<",\"second_pair_index\":"<<second<<",\"candidate_cursor\":"<<cursor<<",\"S_ids\":[";
  for(int j=0;j<4;j++)f<<(j?",":"")<<S[j];f<<"],\"S_coordinates\":[";
  for(int j=0;j<4;j++)f<<(j?",":"")<<"["<<S[j]%q<<","<<S[j]/q<<"]";
  f<<"],\"root_missing_leaf_block_head\":["<<miss[0]<<","<<miss[1]<<","<<miss[2]<<"],\"bad_unordered_pairs\":"<<bad(miss)<<",\"cpu_seconds\":"<<cpu<<"}\n";
 }
};
struct Candidate{int type,first,second;array<int,4>S;};
struct Counts{long long raw=0,invalid=0,valid=0,skippedHH=0,scored=0,best=numeric_limits<long long>::max();map<long long,long long>hist;};
void write_counts(ostream&o,const Counts&c){o<<"{\"raw_slots_visited\":"<<c.raw<<",\"invalid_duplicate_pairs\":"<<c.invalid<<",\"valid_candidates\":"<<c.valid<<",\"skipped_HH\":"<<c.skippedHH<<",\"fully_scored\":"<<c.scored<<",\"best_bad_pairs_after_HH_filter\":"<<(c.scored?to_string(c.best):"null")<<",\"score_histogram\":{";bool comma=false;for(auto[s,n]:c.hist){o<<(comma?",":"")<<"\""<<s<<"\":"<<n;comma=true;}o<<"}}";}
int main(int argc,char**argv){try{
 if(argc>=2&&string(argv[1])=="check"){
  if(argc!=9)throw runtime_error("check q r S0 S1 S2 S3 prefix");Engine e(stoi(argv[2]),stoi(argv[3]));array<int,4>S;for(int j=0;j<4;j++)S[j]=stoi(argv[4+j]);if(!e.legal(S))throw runtime_error("invalid S");e.build(S);auto miss=e.missing();e.save(argv[8],S,miss,"source_check",-1,-1,-1,0);cout<<"bad "<<e.bad(miss)<<" roots "<<miss[0]<<" "<<miss[1]<<" "<<miss[2]<<"\n";return 0;
 }
 if(argc!=4)throw runtime_error("CPU_LIMIT PROFILE_COUNT PREFIX");double limit=stod(argv[1]);long long profile_count=stoll(argv[2]);string prefix=argv[3];clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 signal(SIGINT,stop_signal);signal(SIGTERM,stop_signal);Engine e(41,2);vector<int>pairs;
 for(int g=1;g<e.L;g++)if(g<e.inv[g])pairs.push_back(g);if(pairs.size()!=389)throw runtime_error("expected 389 inverse pairs");
 ofstream pf(prefix+".inverse_pairs.json");pf<<"[";for(int j=0;j<(int)pairs.size();j++)pf<<(j?",":"")<<"["<<pairs[j]%41<<","<<pairs[j]/41<<"]";pf<<"]\n";pf.close();
 vector<Candidate>candidates;
 for(int v=0;v<41;v++)if(v!=1)for(int j=0;j<389;j++)candidates.push_back({0,v,j,{411,410+v,pairs[j],e.inv[pairs[j]]}});
 for(int i=0;i<20;i++)if(i!=10)for(int j=0;j<389;j++){int g=1+41*i;candidates.push_back({1,i,j,{g,e.inv[g],pairs[j],e.inv[pairs[j]]}});}
 if(candidates.size()!=22951)throw runtime_error("wrong candidate slot count");
 vector<int>orbit(41,2);orbit[0]=0;for(int p:e.power)orbit[p]=1;
 array<Counts,2>counts;long long best=numeric_limits<long long>::max(),scored_total=0,next=0;bool profile_done=false,found=false,budget=false,projected_over=false;
 for(long long cursor=0;cursor<(long long)candidates.size();cursor++){
  if(stopped||((cursor&255)==0&&cpu()>=limit)){budget=!stopped;break;}
  auto c=candidates[cursor];auto&ct=counts[c.type];ct.raw++;next=cursor+1;
  if(!e.legal(c.S)){ct.invalid++;}
  else{ct.valid++;int mask=0;for(int g:c.S)mask|=orbit[g%41];if(mask!=3)ct.skippedHH++;
   else{e.build(c.S);auto miss=e.missing();auto bad=e.bad(miss);ct.scored++;scored_total++;ct.hist[bad]++;
    if(bad<ct.best){ct.best=bad;e.save(prefix+(c.type?".B.best":".A.best"),c.S,miss,c.type?"B":"A",c.first,c.second,cursor,cpu());}
    if(bad<best){best=bad;e.save(prefix+".best",c.S,miss,c.type?"B":"A",c.first,c.second,cursor,cpu());cout<<"best "<<bad<<" type "<<(c.type?"B":"A")<<" cursor "<<cursor<<" cpu "<<cpu()<<endl;}
    if(bad==0){found=true;break;}
   }
  }
  if(!profile_done&&next>=profile_count){
   double used=cpu(),cost_per_scored=used/max(1LL,scored_total),estimate=used+(candidates.size()-next)*cost_per_scored;
   ofstream p(prefix+".profile.json");p<<"{\"raw_slots\":"<<next<<",\"fully_scored\":"<<scored_total<<",\"cpu_seconds\":"<<used<<",\"conservative_estimated_total_cpu_seconds\":"<<estimate<<",\"cpu_limit\":"<<limit<<",\"continue_with_same_process\":"<<(estimate<limit?"true":"false")<<"}\n";
   cout<<"profile slots "<<next<<" scored "<<scored_total<<" cpu "<<used<<" estimated_total "<<estimate<<" limit "<<limit<<endl;profile_done=true;
   if(estimate>=limit){projected_over=true;break;}
  }
 }
 string status=found?"CANDIDATE_D5":next==(long long)candidates.size()?"COMPLETE_NO_SOLUTION":projected_over?"PROFILE_ESTIMATE_EXCEEDS_BUDGET":stopped?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 ofstream out(prefix+".terminal.json");out<<"{\"status\":\""<<status<<"\",\"raw_slots_total\":22951,\"valid_candidates_expected\":22932,\"next_candidate_cursor\":"<<next<<",\"cpu_seconds\":"<<cpu()<<",\"best_bad_pairs_after_HH_filter\":"<<(scored_total?to_string(best):"null")<<",\"counts\":{\"A\":";write_counts(out,counts[0]);out<<",\"B\":";write_counts(out,counts[1]);out<<"},\"next_parameters\":";
 if(next<(long long)candidates.size()){auto c=candidates[next];out<<"{\"type\":\""<<(c.type?"B":"A")<<"\",\"first\":"<<c.first<<",\"pair_index\":"<<c.second<<"}";}else out<<"null";
 out<<"}\n";cout<<"terminal "<<status<<" next "<<next<<" best "<<best<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<"\n";return 2;}}

#include <algorithm>
#include <array>
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
using Labels=array<int,5>;
const array<string,3>names={"A1","A0","B"};

struct Engine{
 int q,r,d,m,L,n;vector<int>power,inv;vector<U>right,queue;vector<array<U,6>>adj;
 vector<unsigned>seen;unsigned stamp=0;
 Engine(int Q,int R,int D):q(Q),r(R),d(D),m(d*(d-1)),L(m*q),n((m+d+1)*q),power(m),inv(L),right(L*L),queue(n),adj(n),seen(n){
  if(d<5||d>6||n>65535)throw runtime_error("unsupported size");
  power[0]=1;for(int i=1;i<m;i++)power[i]=power[i-1]*r%q;
  if(power[m-1]*r%q!=1||power[m/2]!=q-1)throw runtime_error("unsupported action");
  for(int s=0;s<L;s++)for(int g=0;g<L;g++)right[s*L+g]=(g%q+power[g/q]*(s%q))%q+q*((g/q+s/q)%m);
  for(int g=0;g<L;g++){int j=(m-g/q)%m;inv[g]=((q-power[j]*(g%q)%q)%q)+q*j;}
  for(int i=0;i<m;i++)for(int x=0;x<q;x++)adj[x+q*i][0]=L+x+q*(i%d);
  for(int j=0;j<d;j++)for(int x=0;x<q;x++){
   int b=L+x+q*j;for(int k=0;k<d-1;k++)adj[b][k]=x+q*(j+d*k);
   adj[b][d-1]=(m+d)*q+x;
  }
  for(int x=0;x<q;x++)for(int j=0;j<d;j++)adj[(m+d)*q+x][j]=L+x+q*j;
 }
 bool legal(const Labels&S){for(int j=0;j<d-1;j++){
  if(S[j]<=0||S[j]>=L)return false;
  bool has_inverse=false;for(int k=0;k<d-1;k++){if(j!=k&&S[j]==S[k])return false;if(S[k]==inv[S[j]])has_inverse=true;}
  if(!has_inverse)return false;
 }return true;}
 void build(const Labels&S){for(int j=0;j<d-1;j++){const U*t=&right[S[j]*L];for(int g=0;g<L;g++)adj[g][j+1]=t[g];}}
 array<int,3>missing(){array<int,3>a{};array<int,3>roots={0,L,(m+d)*q};
  for(int side=0;side<3;side++){++stamp;int head=0,end=1;queue[0]=roots[side];seen[roots[side]]=stamp;
   for(int depth=0;depth<5&&head<end&&end<n;depth++){int boundary=end;while(head<boundary){int u=queue[head++];for(int j=0;j<d;j++){int v=adj[u][j];if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}}}}
   a[side]=n-end;
  }return a;
 }
 long long bad(const array<int,3>&a){long long twice=1LL*m*q*a[0]+1LL*d*q*a[1]+1LL*q*a[2];if(twice%2)throw runtime_error("odd weighted count");return twice/2;}
 void save_json(string path,const Labels&S,const array<int,3>&miss,string type,array<int,3>parameters,long long cursor,double cpu){
  ofstream f(path);f<<"{\"degree\":"<<d<<",\"q\":"<<q<<",\"r\":"<<r<<",\"m\":"<<m<<",\"n\":"<<n<<",\"type\":\""<<type<<"\",\"parameters\":["<<parameters[0]<<","<<parameters[1]<<","<<parameters[2]<<"],\"candidate_cursor\":"<<cursor<<",\"S_ids\":[";
  for(int j=0;j<d-1;j++)f<<(j?",":"")<<S[j];f<<"],\"S_coordinates\":[";
  for(int j=0;j<d-1;j++)f<<(j?",":"")<<"["<<S[j]%q<<","<<S[j]/q<<"]";
  f<<"],\"root_orbit_sizes\":["<<m*q<<","<<d*q<<","<<q<<"],\"root_missing_leaf_block_head\":["<<miss[0]<<","<<miss[1]<<","<<miss[2]<<"],\"bad_unordered_pairs\":"<<bad(miss)<<",\"cpu_seconds\":"<<cpu<<"}\n";
 }
 void save(string prefix,const Labels&S,const array<int,3>&miss,string type,array<int,3>parameters,long long cursor,double cpu){
  vector<pair<int,int>>edges;for(int u=0;u<n;u++)for(int j=0;j<d;j++){int v=adj[u][j];if(u<v)edges.emplace_back(u,v);}sort(edges.begin(),edges.end());
  if((int)edges.size()!=d*n/2||adjacent_find(edges.begin(),edges.end())!=edges.end())throw runtime_error("invalid complete edge list");
  ofstream e(prefix+".edges");e<<n<<" "<<edges.size()<<"\n";for(auto[u,v]:edges)e<<u<<" "<<v<<"\n";
  save_json(prefix+".json",S,miss,type,parameters,cursor,cpu);
 }
};
struct Candidate{int type;array<int,3>parameters;Labels S;};
struct Counts{
 long long raw=0,invalid=0,valid=0,skippedHH=0,scored=0,best=numeric_limits<long long>::max(),headBlockZero=0,firstHeadCursor=-1;
 array<int,3>rootMin={2258,2258,2258};array<long long,3>rootZero{};map<long long,long long>hist;
};
void write_counts(ostream&o,const Counts&c){
 o<<"{\"raw_slots_visited\":"<<c.raw<<",\"invalid_duplicate_pairs\":"<<c.invalid<<",\"valid_candidates\":"<<c.valid<<",\"skipped_HH\":"<<c.skippedHH<<",\"fully_scored\":"<<c.scored<<",\"best_bad_pairs_after_HH_filter\":"<<(c.scored?to_string(c.best):"null")<<",\"root_minimum_missing\":[";
 for(int j=0;j<3;j++)o<<(j?",":"")<<(c.scored?to_string(c.rootMin[j]):"null");o<<"],\"root_zero_counts\":[";
 for(int j=0;j<3;j++)o<<(j?",":"")<<c.rootZero[j];o<<"],\"head_and_block_zero_count\":"<<c.headBlockZero<<",\"first_head_zero_cursor\":"<<(c.firstHeadCursor<0?"null":to_string(c.firstHeadCursor))<<",\"score_histogram\":{";
 bool comma=false;for(auto[s,n]:c.hist){o<<(comma?",":"")<<"\""<<s<<"\":"<<n;comma=true;}o<<"}}";
}
int main(int argc,char**argv){try{
 if(argc>=2&&string(argv[1])=="check"){
  int d=stoi(argv[2]);if(argc!=d+5)throw runtime_error("check d q r S0 ... S[d-2] PREFIX");
  Engine e(stoi(argv[3]),stoi(argv[4]),d);Labels S{};for(int j=0;j<d-1;j++)S[j]=stoi(argv[5+j]);if(!e.legal(S))throw runtime_error("invalid S");
  e.build(S);auto miss=e.missing();e.save(argv[d+4],S,miss,"regression",{-1,-1,-1},-1,0);cout<<"bad "<<e.bad(miss)<<" roots "<<miss[0]<<" "<<miss[1]<<" "<<miss[2]<<"\n";return 0;
 }
 if(argc!=4)throw runtime_error("CPU_LIMIT PROFILE_COUNT PREFIX");double limit=stod(argv[1]);long long profile_count=stoll(argv[2]);string prefix=argv[3];clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 signal(SIGINT,stop_signal);signal(SIGTERM,stop_signal);Engine e(61,4,6);vector<int>pairs;
 for(int g=1;g<e.L;g++)if(g<e.inv[g])pairs.push_back(g);if(pairs.size()!=884)throw runtime_error("expected 884 inverse pairs");
 ofstream pf(prefix+".inverse_pairs.json");pf<<"[";for(int j=0;j<(int)pairs.size();j++)pf<<(j?",":"")<<"["<<pairs[j]%61<<","<<pairs[j]/61<<"]";pf<<"]\n";pf.close();
 vector<Candidate>candidates;candidates.reserve(1980602);
 for(int i=0;i<884;i++)for(int j=i+1;j<884;j++)candidates.push_back({0,{i,j,-1},{916,pairs[i],e.inv[pairs[i]],pairs[j],e.inv[pairs[j]]}});
 for(int i=0;i<30;i++)if(i!=15)for(int j=0;j<884;j++){int g=1+61*i;candidates.push_back({1,{i,j,-1},{915,g,e.inv[g],pairs[j],e.inv[pairs[j]]}});}
 for(int v=0;v<61;v++)if(v!=1)for(int w=v+1;w<61;w++)if(w!=1)for(int j=0;j<884;j++)candidates.push_back({2,{v,w,j},{916,915+v,915+w,pairs[j],e.inv[pairs[j]]}});
 if(candidates.size()!=1980602)throw runtime_error("wrong raw slot count");
 vector<int>orbit(61,2);orbit[0]=0;for(int p:e.power)orbit[p]=1;
 if(set<int>(e.power.begin(),e.power.end()).size()!=30)throw runtime_error("action order not 30");
 array<Counts,3>counts;long long best=numeric_limits<long long>::max(),scored_total=0,next=0;bool profile_done=false,found=false,projected_over=false,first_head_saved=false;
 double setup_cpu=cpu();cout<<"setup cpu "<<setup_cpu<<" total_slots "<<candidates.size()<<endl;
 for(long long cursor=0;cursor<(long long)candidates.size();cursor++){
  if(stopped||((cursor&255)==0&&cpu()>=limit))break;
  const auto&c=candidates[cursor];auto&ct=counts[c.type];ct.raw++;next=cursor+1;
  if(!e.legal(c.S))ct.invalid++;
  else{ct.valid++;int mask=0;for(int g:c.S)mask|=orbit[g%61];if(mask!=3)ct.skippedHH++;
   else{e.build(c.S);auto miss=e.missing();auto bad=e.bad(miss);ct.scored++;scored_total++;ct.hist[bad]++;
    for(int k=0;k<3;k++){ct.rootMin[k]=min(ct.rootMin[k],miss[k]);if(miss[k]==0)ct.rootZero[k]++;}
    if(miss[2]==0&&miss[1]==0)ct.headBlockZero++;
    if(miss[2]==0&&ct.firstHeadCursor<0){ct.firstHeadCursor=cursor;e.save_json(prefix+"."+names[c.type]+".first_head_zero.json",c.S,miss,names[c.type],c.parameters,cursor,cpu());}
    if(miss[2]==0&&!first_head_saved){first_head_saved=true;e.save_json(prefix+".first_head_zero.json",c.S,miss,names[c.type],c.parameters,cursor,cpu());}
    if(bad<ct.best){ct.best=bad;e.save(prefix+"."+names[c.type]+".best",c.S,miss,names[c.type],c.parameters,cursor,cpu());}
    if(bad<best){best=bad;e.save(prefix+".best",c.S,miss,names[c.type],c.parameters,cursor,cpu());cout<<"best "<<bad<<" type "<<names[c.type]<<" cursor "<<cursor<<" roots "<<miss[0]<<" "<<miss[1]<<" "<<miss[2]<<" cpu "<<cpu()<<endl;}
    if(bad==0){found=true;break;}
   }
  }
  if(!profile_done&&next>=profile_count){
   double used=cpu(),loop_cpu=used-setup_cpu,cost_per_scored=loop_cpu/max(1LL,scored_total),estimate=used+(candidates.size()-next)*cost_per_scored;
   ofstream p(prefix+".profile.json");p<<"{\"raw_slots\":"<<next<<",\"fully_scored\":"<<scored_total<<",\"setup_cpu_seconds\":"<<setup_cpu<<",\"loop_cpu_seconds\":"<<loop_cpu<<",\"cpu_seconds\":"<<used<<",\"conservative_estimated_total_cpu_seconds\":"<<estimate<<",\"cpu_limit\":"<<limit<<",\"continue_with_same_process\":"<<(estimate<limit?"true":"false")<<"}\n";
   cout<<"profile slots "<<next<<" scored "<<scored_total<<" cpu "<<used<<" estimated_total "<<estimate<<" limit "<<limit<<endl;profile_done=true;
   if(estimate>=limit){projected_over=true;break;}
  }
  if(next==390286||next==415922)cout<<"branch_complete "<<names[c.type]<<" cursor "<<next<<" cpu "<<cpu()<<endl;
 }
 string status=found?"CANDIDATE_D5":next==(long long)candidates.size()?"COMPLETE_NO_SOLUTION":projected_over?"PROFILE_ESTIMATE_EXCEEDS_BUDGET":stopped?"STOPPED":"CPU_BUDGET_EXHAUSTED";
 ofstream out(prefix+".terminal.json");out<<"{\"status\":\""<<status<<"\",\"raw_slots_total\":1980602,\"valid_candidates_expected\":1980573,\"next_candidate_cursor\":"<<next<<",\"cpu_seconds\":"<<cpu()<<",\"best_bad_pairs_after_HH_filter\":"<<(scored_total?to_string(best):"null")<<",\"metrics_scope\":\"HH-passing fully scored candidates only\",\"counts\":{";
 for(int k=0;k<3;k++){out<<(k?",":"")<<"\""<<names[k]<<"\":";write_counts(out,counts[k]);}out<<"},\"next_parameters\":";
 if(next<(long long)candidates.size()){auto c=candidates[next];out<<"{\"type\":\""<<names[c.type]<<"\",\"parameters\":["<<c.parameters[0]<<","<<c.parameters[1]<<","<<c.parameters[2]<<"]}";}else out<<"null";
 out<<"}\n";cout<<"terminal "<<status<<" next "<<next<<" best "<<best<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<"\n";return 2;}}

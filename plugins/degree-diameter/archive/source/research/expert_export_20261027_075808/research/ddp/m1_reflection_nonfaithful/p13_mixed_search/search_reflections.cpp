#include <algorithm>
#include <array>
#include <chrono>
#include <csignal>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t stopped=0;
void stop_signal(int){stopped=1;}
using U=unsigned short;
struct Engine {
 int p,m,r,q,n; vector<int>power,inverse; vector<U>right,queue;
 vector<array<U,5>>adj; vector<unsigned>seen; unsigned stamp=0;
 Engine(int P,int M,int R):p(P),m(M),r(R),q(P*M),n(2*q),power(m),inverse(q),right(q*q),queue(n),adj(n),seen(n){
  power[0]=1;for(int i=1;i<m;i++)power[i]=power[i-1]*r%p;
  if(m%2||power.back()*r%p!=1||power[m/2]!=p-1||n>65535)throw runtime_error("unsupported group");
  for(int h=0;h<q;h++)for(int g=0;g<q;g++)right[h*q+g]=((g/m+power[g%m]*(h/m))%p)*m+(g%m+h%m)%m;
  for(int g=0;g<q;g++){int j=(m-g%m)%m;inverse[g]=((p-power[j]*(g/m)%p)%p)*m+j;}
 }
 array<int,6>generators(const string&kind,const array<int,3>&sk,const vector<int>&v){
  int b=v[0]*m+sk[0],d=kind=="mixed"?inverse[b]:v[1]*m+m/2;
  int offset=kind=="mixed"?1:2;
  return {m/2,m+m/2,b,d,v[offset]*m+sk[1],v[offset+1]*m+sk[2]};
 }
 int illegal(const string&kind,const array<int,6>&g){
  if(!g[2]||!g[3])return 1;
  if(kind=="mixed"&&g[2]==g[3])return 2;
  if(kind=="both"&&g[2]==g[3])return 3;
  if(!g[4]||!g[5]||g[4]==g[5])return 4;
  return 0;
 }
 void build(const array<int,6>&g){
  const U *a=&right[g[0]*q],*c=&right[g[1]*q],*b=&right[g[2]*q],*d=&right[g[3]*q];
  const U *s=&right[g[4]*q],*t=&right[g[5]*q],*si=&right[inverse[g[4]]*q],*ti=&right[inverse[g[5]]*q];
  for(int x=0;x<q;x++){
   adj[x]={(U)a[x],(U)c[x],(U)(q+x),(U)(q+s[x]),(U)(q+t[x])};
   adj[q+x]={(U)(q+b[x]),(U)(q+d[x]),(U)x,si[x],ti[x]};
  }
 }
 array<int,2>score(int*diameter=nullptr){
  array<int,2>miss{};if(diameter)*diameter=0;
  for(int side=0;side<2;side++){
   ++stamp;int end=1,head=0,depth=0;queue[0]=side*q;seen[queue[0]]=stamp;
   while(end<n&&head<end&&(diameter||depth<5)){
    int boundary=end;while(head<boundary){int u=queue[head++];for(U v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}}
    depth++;if(depth==5)miss[side]=n-end;
   }
   if(depth<5)miss[side]=n-end;
   if(diameter)*diameter=max(*diameter,end==n?depth:n);
  }return miss;
 }
 void save(const string&prefix,const array<int,6>&g,const array<int,2>&miss,const string&kind,const array<int,3>&sk,const vector<int>&v,int sid,long long code,double cpu){
  vector<pair<int,int>>edges;for(int u=0;u<n;u++)for(int w:adj[u])if(u<w)edges.emplace_back(u,w);sort(edges.begin(),edges.end());
  if((int)edges.size()!=5*n/2||adjacent_find(edges.begin(),edges.end())!=edges.end())throw runtime_error("saved graph violates degree/simple contract");
  ofstream e(prefix+".edges");e<<n<<" "<<edges.size()<<"\n";for(auto[u,w]:edges)e<<u<<" "<<w<<"\n";
  ofstream j(prefix+".json");j<<"{\"p\":"<<p<<",\"m\":"<<m<<",\"r\":"<<r<<",\"n\":"<<n<<",\"branch\":\""<<kind<<"\",\"skeleton_id\":"<<sid<<",\"assignment_index\":"<<code<<",\"quotient\":["<<sk[0]<<","<<sk[1]<<","<<sk[2]<<"],\"variables\":[";
  for(int i=0;i<(int)v.size();i++)j<<(i?",":"")<<v[i];
  j<<"],\"generators_A0_A1_B0_B1_s_t\":[";for(int i=0;i<6;i++)j<<(i?",":"")<<g[i];
  j<<"],\"root_missing\":["<<miss[0]<<","<<miss[1]<<"],\"missing_sum\":"<<miss[0]+miss[1]<<",\"bad_unordered_pairs\":"<<q*(miss[0]+miss[1])/2<<",\"cpu_seconds_at_best\":"<<cpu<<"}\n";
 }
};
int main(int argc,char**argv){
 try{
  if(argc>=2&&string(argv[1])=="check"){
   if(argc!=12)throw runtime_error("check P M R A0 A1 B0 B1 s t PREFIX");
   Engine e(stoi(argv[2]),stoi(argv[3]),stoi(argv[4]));array<int,6>g;for(int i=0;i<6;i++)g[i]=stoi(argv[5+i]);
   e.build(g);int diameter;auto miss=e.score(&diameter);e.save(argv[11],g,miss,"explicit",{-1,-1,-1},{},-1,-1,0);
   cout<<"root_missing "<<miss[0]<<" "<<miss[1]<<" diameter "<<diameter<<"\n";return 0;
  }
  if(argc!=11)throw runtime_error("BRANCH P M R SKELETONS CPU_LIMIT PREFIX MAX_RAW STOP_ZERO DETAILED_SMALL");
  string kind=argv[1];if(kind!="mixed"&&kind!="both")throw runtime_error("invalid branch");
  clock_t start=clock();auto wall_start=chrono::steady_clock::now();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
  Engine e(stoi(argv[2]),stoi(argv[3]),stoi(argv[4]));double limit=stod(argv[6]);string prefix=argv[7];long long maxraw=stoll(argv[8]);bool stopzero=stoi(argv[9]),detail=stoi(argv[10]);
  if(detail&&e.n>100)throw runtime_error("detailed scoring restricted to tiny regression");
  ifstream in(argv[5]);int count;in>>count;vector<array<int,3>>skels(count);for(auto&sk:skels){for(int&i:sk)in>>i;int d=gcd(e.m,e.m/2);for(int i:sk){if(i<0||i>=e.m)throw runtime_error("bad residue");d=gcd(d,i);}if(d!=1)throw runtime_error("disconnected quotient");if(kind=="both"&&sk[0]!=e.m/2)throw runtime_error("bad reflection residue");}
  if(!in)throw runtime_error("invalid skeleton input");
  signal(SIGINT,stop_signal);signal(SIGTERM,stop_signal);
  int dim=kind=="mixed"?3:4;long long per=1;for(int i=0;i<dim;i++)per*=e.p;
  long long raw=0,legal=0,rejected=0;array<long long,5>reasons{};vector<long long>hist(2*e.n+1),dhist(e.n+1);
  int complete=0,best=2*e.n+1,nextsid=0;long long nextcode=0;bool found=false,budget=false,capped=false;ofstream records(prefix+".skeleton_results.jsonl");
  for(int sid=0;sid<count;sid++){
   long long done=0,scored=0;int localbest=2*e.n+1;vector<long long>lhist(2*e.n+1),ldhist(e.n+1);
   for(long long code=0;code<per;code++){
    if(stopped||(maxraw&&raw>=maxraw)||((raw&1023)==0&&cpu()>=limit)){budget=!stopped&&!(maxraw&&raw>=maxraw);capped=maxraw&&raw>=maxraw;break;}
    vector<int>v(dim);long long z=code;for(int&i:v){i=z%e.p;z/=e.p;}auto g=e.generators(kind,skels[sid],v);raw++;done++;
    int reason=e.illegal(kind,g);if(reason){rejected++;reasons[reason]++;continue;}
    e.build(g);int diameter=0;auto miss=e.score(detail?&diameter:nullptr);int score=miss[0]+miss[1];legal++;scored++;hist[score]++;lhist[score]++;localbest=min(localbest,score);if(detail){dhist[diameter]++;ldhist[diameter]++;}
    if(score<best){best=score;e.save(prefix+".best",g,miss,kind,skels[sid],v,sid,code,cpu());cout<<"best "<<best<<" badpairs "<<e.q*best/2<<" skeleton "<<sid<<" assignment "<<code<<" cpu "<<cpu()<<endl;}
    if(score==0&&stopzero){found=true;break;}
   }
   bool finished=done==per;if(finished)complete++;
   nextsid=finished?sid+1:sid;nextcode=finished?0:done;
   records<<"{\"skeleton_id\":"<<sid<<",\"quotient\":["<<skels[sid][0]<<","<<skels[sid][1]<<","<<skels[sid][2]<<"],\"status\":\""<<(finished?"COMPLETE":found?"FOUND":"PARTIAL")<<"\",\"raw_visited\":"<<done<<",\"legal_fully_scored\":"<<scored<<",\"illegal\":"<<done-scored<<",\"next_assignment_index\":"<<done<<",\"minimum_missing\":"<<(scored?to_string(localbest):"null")<<",\"cpu_seconds\":"<<cpu()<<",\"score_histogram\":{";
   bool comma=false;for(int s=0;s<(int)lhist.size();s++)if(lhist[s]){records<<(comma?",":"")<<"\""<<s<<"\":"<<lhist[s];comma=true;}records<<"},\"diameter_histogram\":{";comma=false;for(int d=0;d<(int)ldhist.size();d++)if(ldhist[d]){records<<(comma?",":"")<<"\""<<d<<"\":"<<ldhist[d];comma=true;}records<<"}}\n";records.flush();
   if(found||stopped||budget||capped)break;
  }
  string status=found?"CANDIDATE_COVERED":complete==count?(best==0?"COMPLETE_WITH_SOLUTIONS":"COMPLETE_NO_SOLUTION"):stopped?"STOPPED":capped?"CALIBRATION_LIMIT":"CPU_BUDGET_EXHAUSTED";
  ofstream out(prefix+".summary.json");out<<"{\"branch\":\""<<kind<<"\",\"p\":"<<e.p<<",\"m\":"<<e.m<<",\"r\":"<<e.r<<",\"status\":\""<<status<<"\",\"skeletons_total\":"<<count<<",\"skeletons_completed\":"<<complete<<",\"raw_per_skeleton\":"<<per<<",\"raw_visited\":"<<raw<<",\"legal_fully_scored\":"<<legal<<",\"illegal_rejected\":"<<rejected<<",\"illegal_identity\":"<<reasons[1]<<",\"illegal_mixed_involution\":"<<reasons[2]<<",\"illegal_both_duplicate\":"<<reasons[3]<<",\"illegal_cross_collision\":"<<reasons[4]<<",\"next_skeleton_id\":"<<nextsid<<",\"next_assignment_index\":"<<nextcode<<",\"minimum_missing_seen\":"<<best<<",\"minimum_global_for_input\":"<<(complete==count?"true":"false")<<",\"cpu_seconds\":"<<cpu()<<",\"wall_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-wall_start).count()<<",\"score_histogram\":{";
  bool comma=false;for(int s=0;s<(int)hist.size();s++)if(hist[s]){out<<(comma?",":"")<<"\""<<s<<"\":"<<hist[s];comma=true;}out<<"},\"diameter_histogram\":{";comma=false;for(int d=0;d<(int)dhist.size();d++)if(dhist[d]){out<<(comma?",":"")<<"\""<<d<<"\":"<<dhist[d];comma=true;}out<<"}}\n";
  cout<<"terminal "<<status<<" raw "<<raw<<" legal "<<legal<<" best "<<best<<" cpu "<<cpu()<<endl;
 }catch(const exception&e){cerr<<e.what()<<"\n";return 2;}
}

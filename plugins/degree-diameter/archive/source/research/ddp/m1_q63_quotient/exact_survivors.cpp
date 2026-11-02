#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <csignal>
#include <fstream>
#include <iostream>
#include <mutex>
#include <set>
#include <string>
#include <thread>
#include <vector>
using namespace std;
volatile sig_atomic_t interrupted=0;
void handle_stop(int){interrupted=1;}
struct Form { array<int,5> c; };
struct Bucket { int root,side,residue; vector<Form> forms; };
struct Skeleton { int id,a,b;array<int,3>s;vector<Bucket>buckets; };
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage FORMS SECONDS THREADS OUTPUT_PREFIX\n";return 2;}
 ifstream input(argv[1]);int n;input>>n;vector<Skeleton>rows(n);
 for(auto&r:rows){int k;input>>r.id>>r.a>>r.b>>r.s[0]>>r.s[1]>>r.s[2]>>k;r.buckets.resize(k);
  for(auto&bucket:r.buckets){int len;input>>bucket.root>>bucket.side>>bucket.residue>>len;bucket.forms.resize(len);
   for(auto&f:bucket.forms){int code;input>>code;for(int&c:f.c){c=code%7;code/=7;}}
  }
 }
 if(!input)return 2;
 double limit=stod(argv[2]);int workers=stoi(argv[3]);if(workers<1||workers>3)return 2;
 string prefix=argv[4];auto start=chrono::steady_clock::now();
 auto elapsed=[&](){return chrono::duration<double>(chrono::steady_clock::now()-start).count();};
 atomic<int>cursor(0),complete(0),partial(0);atomic<long long>raw_total(0),legal_total(0);
 atomic<bool>found(false);mutex found_mutex;
 signal(SIGTERM,handle_stop);signal(SIGINT,handle_stop);
 auto candidate=[&](const Skeleton&r,const array<int,5>&v){
  lock_guard<mutex>lock(found_mutex);if(found.exchange(true))return;
  ofstream o(prefix+".candidate.json");o<<"{\"skeleton_id\":"<<r.id<<",\"a\":["<<v[0]<<","<<r.a<<"],\"b\":["<<v[1]<<","<<r.b<<"],\"S\":[[0,0]";
  for(int j=0;j<3;j++)o<<",["<<v[j+2]<<","<<r.s[j]<<"]";o<<"],\"elapsed_seconds\":"<<elapsed()<<"}\n";
  array<int,9>pow2{1,2,4,1,2,4,1,2,4};
  auto mul=[&](int g,int h){return ((g/9+pow2[g%9]*(h/9))%7)*9+(g%9+h%9)%9;};
  auto inv=[&](int g){int ri=(9-g%9)%9;return ((7-pow2[ri]*(g/9)%7)%7)*9+ri;};
  int a=v[0]*9+r.a,b=v[1]*9+r.b;array<int,4>S{0,v[2]*9+r.s[0],v[3]*9+r.s[1],v[4]*9+r.s[2]};
  set<pair<int,int>>edges;auto edge=[&](int u,int w){if(u>w)swap(u,w);edges.emplace(u,w);};
  for(int g=0;g<63;g++){edge(g,mul(g,a));edge(g,mul(g,inv(a)));edge(63+g,63+mul(g,b));edge(63+g,63+mul(g,inv(b)));for(int s:S)edge(g,63+mul(g,s));}
  ofstream e(prefix+".candidate.edges");e<<126<<" "<<edges.size()<<"\n";for(auto[u,w]:edges)e<<u<<" "<<w<<"\n";
 };
 auto worker=[&](int worker_id){
  ofstream log(prefix+".worker"+to_string(worker_id)+".jsonl");
  while(!interrupted&&!found&&elapsed()<limit){
   int index=cursor.fetch_add(1);if(index>=n)break;const auto&r=rows[index];
   int checked=0,legal=0,next_assignment=0;bool done=true,hit=false;
   for(int assignment=0;assignment<16807;assignment++){
    if((assignment&255)==0&&(interrupted||found||elapsed()>=limit)){done=false;next_assignment=assignment;break;}
    checked++;array<int,5>v;int code=assignment;for(int&x:v){x=code%7;code/=7;}
    if((r.a==0&&v[0]==0)||(r.b==0&&v[1]==0))continue;
    bool distinct=true;for(int j=0;j<3;j++){
     if(r.s[j]==0&&v[j+2]==0)distinct=false;
     for(int k=0;k<j;k++)if(r.s[j]==r.s[k]&&v[j+2]==v[k+2])distinct=false;
    }
    if(!distinct)continue;legal++;
    bool cover=true;
    for(const auto&bucket:r.buckets){
     unsigned mask=0;
     for(const auto&f:bucket.forms){const auto&c=f.c;int x=(c[0]*v[0]+c[1]*v[1]+c[2]*v[2]+c[3]*v[3]+c[4]*v[4])%7;mask|=1u<<x;if(mask==127)break;}
     if(mask!=127){cover=false;break;}
    }
    if(cover){candidate(r,v);hit=true;done=false;next_assignment=assignment+1;break;}
   }
   raw_total+=checked;legal_total+=legal;if(done)complete++;else partial++;
   log<<"{\"skeleton_id\":"<<r.id<<",\"alpha\":"<<r.a<<",\"beta\":"<<r.b<<",\"sigmas\":["<<r.s[0]<<","<<r.s[1]<<","<<r.s[2]<<"],\"status\":\""<<(done?"EXHAUSTED_NO_SOLUTION":hit?"CANDIDATE_FOUND":"PARTIAL")<<"\",\"raw_assignments_checked\":"<<checked<<",\"legal_assignments_checked\":"<<legal<<",\"next_assignment\":"<<(done?16807:next_assignment)<<",\"elapsed_seconds\":"<<elapsed()<<"}\n";log.flush();
  }
 };
 vector<thread>threads;for(int j=0;j<workers;j++)threads.emplace_back(worker,j);for(auto&t:threads)t.join();
 ofstream summary(prefix+".summary.json");
 string status=found?"CANDIDATE_FOUND":complete==n?"ALL_SURVIVING_SKELETONS_EXHAUSTED_NO_SOLUTION":interrupted?"STOPPED":"BUDGET_EXHAUSTED";
 summary<<"{\"status\":\""<<status<<"\",\"skeletons_total\":"<<n<<",\"skeletons_completed\":"<<complete<<",\"skeletons_partial\":"<<partial<<",\"raw_assignments_checked\":"<<raw_total<<",\"legal_assignments_checked\":"<<legal_total<<",\"workers\":"<<workers<<",\"elapsed_seconds\":"<<elapsed()<<"}\n";
 cout<<status<<" completed="<<complete<<" raw="<<raw_total<<" legal="<<legal_total<<" seconds="<<elapsed()<<endl;
}

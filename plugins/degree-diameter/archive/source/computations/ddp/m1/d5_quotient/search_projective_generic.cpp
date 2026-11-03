#include <algorithm>
#include <array>
#include <chrono>
#include <csignal>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t interrupted=0;
void handle_stop(int){interrupted=1;}
struct Search{
 int p,m,action,q,n;
 vector<vector<int>>mul;
 vector<int>inverse,power,queue;
 vector<array<int,5>>adj;
 vector<unsigned>seen;unsigned stamp=0;
 Search(int field,int quotient,int automorphism):p(field),m(quotient),action(automorphism),q(p*m),n(2*q),mul(q,vector<int>(q)),inverse(q),power(m),queue(n),adj(n),seen(n){
  power[0]=1;for(int i=1;i<m;i++)power[i]=power[i-1]*action%p;
  if(action<=1||action>=p||power.back()*action%p!=1)throw runtime_error("invalid specified action");
  for(int g=0;g<q;g++)for(int h=0;h<q;h++)mul[g][h]=((g/m+power[g%m]*(h/m))%p)*m+(g%m+h%m)%m;
  for(int g=0;g<q;g++){int residue=(m-g%m)%m;inverse[g]=((p-power[residue]*(g/m)%p)%p)*m+residue;if(mul[g][inverse[g]]!=0)throw runtime_error("inverse mismatch");}
 }
 vector<array<int,4>>representatives(const array<int,4>&r){
  int pivot=-1;for(int i=0;i<4;i++)if(power[r[i]]!=1){pivot=i;break;}
  if(pivot<0)throw runtime_error("zero conjugation vector outside supported scope");
  vector<int>free;for(int i=0;i<4;i++)if(i!=pivot)free.push_back(i);
  vector<array<int,4>>out;
  for(int first=0;first<3;first++){
   int count=1;for(int j=first+1;j<3;j++)count*=p;
   for(int code=0;code<count;code++){array<int,4>v{};v[free[first]]=1;int x=code;for(int j=first+1;j<3;j++){v[free[j]]=x%p;x/=p;}out.push_back(v);}
  }return out;
 }
 int illegal_reason(const array<int,4>&r,const array<int,4>&v){
  int a=v[0]*m+r[0],b=v[1]*m+r[1];
  if(a==0||b==0)return 1;
  if(a==inverse[a]||b==inverse[b])return 2;
  if((r[2]==0&&v[2]==0)||(r[3]==0&&v[3]==0)||(r[2]==r[3]&&v[2]==v[3]))return 3;
  return 0;
 }
 void build(const array<int,4>&r,const array<int,4>&v){
  int a=v[0]*m+r[0],b=v[1]*m+r[1],s=v[2]*m+r[2],t=v[3]*m+r[3];
  int ai=inverse[a],bi=inverse[b],si=inverse[s],ti=inverse[t];
  for(int g=0;g<q;g++){adj[g]={mul[g][a],mul[g][ai],q+g,q+mul[g][s],q+mul[g][t]};adj[q+g]={q+mul[g][b],q+mul[g][bi],g,mul[g][si],mul[g][ti]};}
 }
 array<int,2>score(){
  array<int,2>miss;
  for(int side=0;side<2;side++){
   ++stamp;int end=1,head=0;queue[0]=side*q;seen[queue[0]]=stamp;
   for(int depth=0;depth<5&&end<n;depth++){int boundary=end;while(head<boundary){int u=queue[head++];for(int v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}}}
   miss[side]=n-end;
  }return miss;
 }
 void save(const string&prefix,const array<int,4>&r,const array<int,4>&v,const array<int,2>&miss,int skeleton_id,int projective_index,double seconds){
  set<pair<int,int>>edges;for(int u=0;u<n;u++)for(int w:adj[u])if(u<w)edges.emplace(u,w);
  ofstream e(prefix+".edges");e<<n<<" "<<edges.size()<<"\n";for(auto[u,w]:edges)e<<u<<" "<<w<<"\n";
  ofstream j(prefix+".json");j<<"{\"p\":"<<p<<",\"m\":"<<m<<",\"action\":"<<action<<",\"n\":"<<n<<",\"degree\":5,\"target_diameter\":5,\"skeleton_id\":"<<skeleton_id<<",\"projective_index\":"<<projective_index<<",\"quotient_residues\":[";
  for(int i=0;i<4;i++)j<<(i?",":"")<<r[i];j<<"],\"translation_values\":[";for(int i=0;i<4;i++)j<<(i?",":"")<<v[i];
  j<<"],\"root_missing\":["<<miss[0]<<","<<miss[1]<<"],\"representative_missing_sum\":"<<miss[0]+miss[1]<<",\"bad_unordered_pairs\":"<<q*(miss[0]+miss[1])/2<<",\"seconds_at_best\":"<<seconds<<"}\n";
 }
};
int main(int argc,char**argv){
 if(argc!=7){cerr<<"usage P M ACTION SKELETONS SECONDS OUTPUT_PREFIX\n";return 2;}
 int p=stoi(argv[1]),m=stoi(argv[2]),action=stoi(argv[3]);
 vector<array<int,4>>skeletons;ifstream input(argv[4]);array<int,4>r;
 while(input>>r[0]>>r[1]>>r[2]>>r[3]){int divisor=m;for(int x:r){if(x<0||x>=m)return 2;divisor=gcd(divisor,x);}if(divisor!=1)return 2;skeletons.push_back(r);}
 if(!input.eof()||skeletons.empty())return 2;
 double limit=stod(argv[5]);string prefix=argv[6];Search search(p,m,action);
 signal(SIGINT,handle_stop);signal(SIGTERM,handle_stop);
 auto start=chrono::steady_clock::now();auto seconds=[&](){return chrono::duration<double>(chrono::steady_clock::now()-start).count();};
 unsigned long long visited=0,legal=0,illegal=0;array<unsigned long long,4>illegal_types{};int complete=0,best=2*search.n+1;bool found=false;map<int,int>score_hist;
 int count_per_skeleton=p*p+p+1;
 ofstream records(prefix+".skeleton_results.jsonl");
 for(int id=0;id<(int)skeletons.size()&&!found&&!interrupted&&seconds()<limit;id++){
  r=skeletons[id];auto values=search.representatives(r);if((int)values.size()!=count_per_skeleton)return 2;
  int done=0,scored=0,rejected=0,local_best=2*search.n+1;bool partial=false;
  for(int i=0;i<count_per_skeleton;i++){
   if(interrupted||seconds()>=limit){partial=true;break;}done++;visited++;
   auto v=values[i];int reason=search.illegal_reason(r,v);if(reason){illegal++;rejected++;illegal_types[reason]++;continue;}
   legal++;scored++;search.build(r,v);auto miss=search.score();int score=miss[0]+miss[1];local_best=min(local_best,score);score_hist[score]++;
   if(score<best){best=score;search.save(prefix+".best",r,v,miss,id,i,seconds());cout<<"best "<<best<<" badpairs "<<search.q*best/2<<" skeleton "<<id<<" projective "<<i<<" seconds "<<seconds()<<endl;}
   if(score==0){found=true;partial=(done<count_per_skeleton);break;}
  }
  bool finished=done==count_per_skeleton;if(finished)complete++;
  records<<"{\"skeleton_id\":"<<id<<",\"residues\":["<<r[0]<<","<<r[1]<<","<<r[2]<<","<<r[3]<<"],\"status\":\""<<(finished?"COMPLETE":found?"CANDIDATE_FOUND":"PARTIAL")<<"\",\"projective_visited\":"<<done<<",\"legal_fully_scored\":"<<scored<<",\"illegal_rejected\":"<<rejected<<",\"zero_class_excluded\":1,\"next_projective_index\":"<<done<<",\"minimum_missing\":"<<(scored?to_string(local_best):"null")<<",\"elapsed_seconds\":"<<seconds()<<"}\n";records.flush();
  if(partial)break;
 }
 string status=found?"CANDIDATE_COVERED":complete==(int)skeletons.size()?"COMPLETE_NO_SOLUTION":interrupted?"STOPPED":"BUDGET_EXHAUSTED";
 ofstream summary(prefix+".summary.json");summary<<"{\"p\":"<<p<<",\"m\":"<<m<<",\"action\":"<<action<<",\"n\":"<<search.n<<",\"status\":\""<<status<<"\",\"skeletons_total\":"<<skeletons.size()<<",\"skeletons_completed\":"<<complete<<",\"projective_per_skeleton\":"<<count_per_skeleton<<",\"projective_visited\":"<<visited<<",\"legal_fully_scored\":"<<legal<<",\"illegal_rejected\":"<<illegal<<",\"illegal_internal_identity\":"<<illegal_types[1]<<",\"illegal_internal_involution\":"<<illegal_types[2]<<",\"illegal_cross_collision\":"<<illegal_types[3]<<",\"zero_classes_excluded_in_complete_skeletons\":"<<complete<<",\"minimum_missing_seen\":"<<best<<",\"minimum_is_global_for_input\":"<<(complete==(int)skeletons.size()?"true":"false")<<",\"elapsed_seconds\":"<<seconds()<<",\"score_histogram\":{";
 bool comma=false;for(auto[s,count]:score_hist){summary<<(comma?",":"")<<"\""<<s<<"\":"<<count;comma=true;}summary<<"}}\n";
 cout<<"terminal "<<status<<" completed "<<complete<<" visited "<<visited<<" legal "<<legal<<" illegal "<<illegal<<" best "<<best<<" seconds "<<seconds()<<endl;
}

#include <algorithm>
#include <array>
#include <chrono>
#include <csignal>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
volatile sig_atomic_t interrupted=0;
void handle_stop(int){interrupted=1;}
struct Search{
 array<array<int,351>,351>mul;
 array<int,351>inverse;
 array<array<int,5>,702>adj;
 array<unsigned,702>seen{};unsigned stamp=0;
 array<int,27>power;
 Search(){
  power[0]=1;for(int i=1;i<27;i++)power[i]=power[i-1]*3%13;
  for(int g=0;g<351;g++)for(int h=0;h<351;h++)mul[g][h]=((g/27+power[g%27]*(h/27))%13)*27+(g%27+h%27)%27;
  for(int g=0;g<351;g++)inverse[g]=find(mul[g].begin(),mul[g].end(),0)-mul[g].begin();
 }
 vector<array<int,4>>representatives(const array<int,4>&r){
  int pivot=-1;for(int i=0;i<4;i++)if(power[r[i]]!=1){pivot=i;break;}
  if(pivot<0)throw runtime_error("quotient skeleton does not generateC27");
  vector<int>free;for(int i=0;i<4;i++)if(i!=pivot)free.push_back(i);
  vector<array<int,4>>out;
  for(int first=0;first<3;first++){
   int count=1;for(int j=first+1;j<3;j++)count*=13;
   for(int code=0;code<count;code++){
    array<int,4>v{};v[free[first]]=1;int x=code;
    for(int j=first+1;j<3;j++){v[free[j]]=x%13;x/=13;}out.push_back(v);
   }
  }return out;
 }
 bool legal(const array<int,4>&r,const array<int,4>&v){
  if((r[0]==0&&v[0]==0)||(r[1]==0&&v[1]==0))return false;
  if((r[2]==0&&v[2]==0)||(r[3]==0&&v[3]==0))return false;
  return r[2]!=r[3]||v[2]!=v[3];
 }
 void build(const array<int,4>&r,const array<int,4>&v){
  int a=v[0]*27+r[0],b=v[1]*27+r[1],s=v[2]*27+r[2],t=v[3]*27+r[3];
  int ai=inverse[a],bi=inverse[b],si=inverse[s],ti=inverse[t];
  for(int g=0;g<351;g++){
   adj[g]={mul[g][a],mul[g][ai],351+g,351+mul[g][s],351+mul[g][t]};
   adj[351+g]={351+mul[g][b],351+mul[g][bi],g,mul[g][si],mul[g][ti]};
  }
 }
 array<int,2>score(){
  array<int,2>miss;array<int,702>queue;
  for(int side=0;side<2;side++){
   ++stamp;int end=1,head=0;queue[0]=side*351;seen[queue[0]]=stamp;
   for(int depth=0;depth<5&&end<702;depth++){
    int boundary=end;while(head<boundary){int u=queue[head++];for(int v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;queue[end++]=v;}}
   }miss[side]=702-end;
  }return miss;
 }
 void save(const string&prefix,const array<int,4>&r,const array<int,4>&v,const array<int,2>&miss,int skeleton_id,int projective_index,double seconds){
  set<pair<int,int>>edges;for(int u=0;u<702;u++)for(int w:adj[u])if(u<w)edges.emplace(u,w);
  ofstream e(prefix+".edges");e<<702<<" "<<edges.size()<<"\n";for(auto[u,w]:edges)e<<u<<" "<<w<<"\n";
  ofstream j(prefix+".json");j<<"{\"n\":702,\"degree\":5,\"target_diameter\":5,\"skeleton_id\":"<<skeleton_id<<",\"projective_index\":"<<projective_index<<",\"quotient_residues\":[";
  for(int i=0;i<4;i++)j<<(i?",":"")<<r[i];j<<"],\"translation_values\":[";for(int i=0;i<4;i++)j<<(i?",":"")<<v[i];
  j<<"],\"root_missing\":["<<miss[0]<<","<<miss[1]<<"],\"representative_missing_sum\":"<<miss[0]+miss[1]<<",\"bad_unordered_pairs\":"<<351*(miss[0]+miss[1])/2<<",\"seconds_at_best\":"<<seconds<<"}\n";
 }
};
int main(int argc,char**argv){
 if(argc!=4){cerr<<"usage SKELETONS SECONDS OUTPUT_PREFIX\n";return 2;}
 vector<array<int,4>>skeletons;ifstream input(argv[1]);array<int,4>r;while(input>>r[0]>>r[1]>>r[2]>>r[3]){for(int x:r)if(x<0||x>=27)return 2;skeletons.push_back(r);}if(!input.eof()||skeletons.empty())return 2;
 double limit=stod(argv[2]);string prefix=argv[3];Search search;
 signal(SIGINT,handle_stop);signal(SIGTERM,handle_stop);
 auto start=chrono::steady_clock::now();auto seconds=[&](){return chrono::duration<double>(chrono::steady_clock::now()-start).count();};
 unsigned long long visited=0,legal=0,illegal=0;int complete=0,best=1405;bool found=false;map<int,int>score_hist;
 ofstream records(prefix+".skeleton_results.jsonl");
 for(int id=0;id<(int)skeletons.size()&&!found&&!interrupted&&seconds()<limit;id++){
  r=skeletons[id];auto values=search.representatives(r);if(values.size()!=183)return 2;
  int done=0,scored=0,rejected=0,local_best=1405;bool partial=false;
  for(int i=0;i<183;i++){
   if(interrupted||seconds()>=limit){partial=true;break;}done++;visited++;
   auto v=values[i];if(!search.legal(r,v)){illegal++;rejected++;continue;}
   legal++;scored++;search.build(r,v);auto miss=search.score();int score=miss[0]+miss[1];local_best=min(local_best,score);score_hist[score]++;
   if(score<best){best=score;search.save(prefix+".best",r,v,miss,id,i,seconds());cout<<"best "<<best<<" badpairs "<<351*best/2<<" skeleton "<<id<<" projective "<<i<<" seconds "<<seconds()<<endl;}
   if(score==0){found=true;partial=(done<183);break;}
  }
  bool finished=done==183;if(finished)complete++;
  records<<"{\"skeleton_id\":"<<id<<",\"residues\":["<<r[0]<<","<<r[1]<<","<<r[2]<<","<<r[3]<<"],\"status\":\""<<(finished?"COMPLETE":found?"CANDIDATE_FOUND":"PARTIAL")<<"\",\"projective_visited\":"<<done<<",\"legal_fully_scored\":"<<scored<<",\"illegal_rejected\":"<<rejected<<",\"zero_class_excluded\":1,\"next_projective_index\":"<<done<<",\"minimum_missing\":"<<(scored?to_string(local_best):"null")<<",\"elapsed_seconds\":"<<seconds()<<"}\n";records.flush();
  if(partial)break;
 }
 string status=found?"CANDIDATE_COVERED":complete==(int)skeletons.size()?"COMPLETE_NO_SOLUTION":interrupted?"STOPPED":"BUDGET_EXHAUSTED";
 ofstream summary(prefix+".summary.json");summary<<"{\"status\":\""<<status<<"\",\"skeletons_total\":"<<skeletons.size()<<",\"skeletons_completed\":"<<complete<<",\"projective_visited\":"<<visited<<",\"legal_fully_scored\":"<<legal<<",\"illegal_rejected\":"<<illegal<<",\"zero_classes_excluded_in_complete_skeletons\":"<<complete<<",\"minimum_missing_seen\":"<<best<<",\"minimum_is_global_for_input\":"<<(complete==(int)skeletons.size()?"true":"false")<<",\"elapsed_seconds\":"<<seconds()<<",\"score_histogram\":{";
 bool comma=false;for(auto[s,count]:score_hist){summary<<(comma?",":"")<<"\""<<s<<"\":"<<count;comma=true;}summary<<"}}\n";
 cout<<"terminal "<<status<<" completed "<<complete<<" visited "<<visited<<" legal "<<legal<<" illegal "<<illegal<<" best "<<best<<" seconds "<<seconds()<<endl;
}
